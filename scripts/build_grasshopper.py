"""Run with Rhino 8's _-RunPythonScript to build real .ghuser/.gh artifacts.

No user-object installation or changes to the active document are performed.
The generated scripts embed the dependency-free bridge, so users need no paths.
"""
from __future__ import print_function

import hashlib
import json
import os
import traceback

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT = os.path.join(ROOT, "grasshopper_foton", "distribution")

COMPONENTS = (
    ("Foton Settings", ("executable_", "backend_", "python_", "install_", "_check"),
     ("report", "executable", "engine_version", "protocol_version", "backend", "capabilities", "cache_folder")),
    ("Foton Annual Daylight", ("_model", "_wea", "schedule_", "north_", "thresholds_", "grid_filter_", "quality_", "sky_density_", "backend_", "output_folder_", "executable_", "reuse_", "direct_samples_", "indirect_samples_", "bounces_", "seed_", "live_", "_run"),
     ("report", "results", "DA", "cDA", "UDI", "UDI_low", "UDI_up", "sDA", "grid_ids", "room_ids", "manifest", "timings", "timings_text", "warnings", "folder")),
    ("Foton Annual Results", ("_manifest", "_load"),
     ("report", "results", "DA", "cDA", "UDI", "UDI_low", "UDI_up", "sDA", "grid_ids", "room_ids", "manifest", "timings", "timings_text", "warnings", "folder")),
    ("Foton Daylight Factor", ("_model", "grid_filter_", "quality_", "sky_density_", "backend_", "output_folder_", "executable_", "bounces_", "live_", "_run"),
     ("report", "results", "DF", "mean_DF", "grid_ids", "room_ids", "timings_text", "folder")),
)


def source(path):
    with open(os.path.join(ROOT, path), "r") as stream:
        return stream.read()


def embedded_script(name):
    common = source("python/foton_bridge/__init__.py")
    bridge = source("grasshopper_foton/foton_gh.py")
    component = source("grasshopper_foton/components/" + name + ".py")
    # Each component holds its own bridge module references after loading.
    stamp = hashlib.sha256((common + bridge).encode("utf-8")).hexdigest()[:12]
    return '''from __future__ import print_function
import sys, types
_common = types.ModuleType("foton_bridge")
exec(compile(%r, "foton_bridge", "exec"), _common.__dict__)
sys.modules["foton_bridge"] = _common
_package = types.ModuleType("grasshopper_foton")
_package.__path__ = []
_bridge = types.ModuleType("grasshopper_foton.foton_gh")
_bridge.__file__ = "foton_embedded_%s.py"
exec(compile(%r, "foton_gh", "exec"), _bridge.__dict__)
_package.foton_gh = _bridge
sys.modules["grasshopper_foton"] = _package
sys.modules["grasshopper_foton.foton_gh"] = _bridge
exec(compile(%r, %r, "exec"), globals())
''' % (common, stamp, bridge, component, name)


def main():
    import clr
    import Rhino
    Rhino.PlugIns.PlugIn.LoadPlugIn(Rhino.PlugIns.PlugIn.IdFromName("Grasshopper"))
    clr.AddReference("Grasshopper")
    clr.AddReference("GH_IO")
    import Grasshopper as gh
    from Grasshopper.Kernel import GH_Document, GH_UserObject, GH_ParamAccess
    from GH_IO.Serialization import GH_Archive
    from System import Guid
    from System.Drawing import PointF

    if not os.path.isdir(OUTPUT):
        os.makedirs(OUTPUT)
    document = GH_Document()
    # The built-in, cross-platform legacy GhPython component; external engine stays CPython.
    component_id = Guid("410755b1-224a-4c1e-a407-bf32fb45ea7e")

    def make_component(name, inputs, outputs, code, x, y):
        obj = gh.Instances.ComponentServer.EmitObjectProxy(component_id).CreateInstance()
        obj.CreateAttributes()
        obj.HiddenOutOutput = True
        while obj.Params.Input.Count:
            obj.Params.UnregisterInputParameter(obj.Params.Input[0], True)
        while obj.Params.Output.Count:
            obj.Params.UnregisterOutputParameter(obj.Params.Output[0], True)
        from Grasshopper.Kernel import GH_ParameterSide
        for side, names in ((GH_ParameterSide.Input, inputs), (GH_ParameterSide.Output, outputs)):
            for index, port_name in enumerate(names):
                param = obj.CreateParameter(side, index)
                param.Name = param.NickName = port_name
                param.Description = port_name
                param.Access = GH_ParamAccess.item
                param.Optional = True
                if side == GH_ParameterSide.Input:
                    obj.Params.RegisterInputParam(param)
                else:
                    obj.Params.RegisterOutputParam(param)
        obj.Name = obj.NickName = name
        obj.Category = "HB-Foton"
        obj.SubCategory = "Recipes"
        obj.Code = code
        obj.Params.OnParametersChanged()
        obj.Attributes.Pivot = PointF(x, y)
        document.AddObject(obj, False)
        return obj

    objects, output_files = [], []
    for index, (name, inputs, outputs) in enumerate(COMPONENTS):
        obj = make_component(name, inputs, outputs, embedded_script(name), 400 + index * 400, 250)
        objects.append(obj)
        user = GH_UserObject()
        user.SetDataFromObject(obj)
        user.Description.Name = name
        user.Description.NickName = name.replace(" ", "")
        user.Description.Category = "HB-Foton"
        user.Description.SubCategory = "Recipes"
        user.BaseGuid = obj.ComponentGuid
        user.Path = os.path.join(OUTPUT, name + ".ghuser")
        if not user.SaveToFile():
            raise RuntimeError("Failed to save " + user.Path)
        loaded = GH_UserObject(user.Path)
        loaded.ReadFromFile()
        restored = loaded.InstantiateObject()
        if restored is None or [p.Name for p in restored.Params.Input] != list(inputs):
            raise RuntimeError("User object round-trip failed: " + name)
        output_files.append(name + ".ghuser")

    example_code = '''import os
root = os.path.dirname(ghenv.Component.OnPingDocument().FilePath)
model = os.path.join(root, "examples", "shoebox.hbjson")
weather = os.path.join(root, "examples", "gothenburg.epw")
output = os.path.join(os.path.expanduser("~"), "foton_simulation", "first_example")
'''
    paths = make_component("Example files", (), ("model", "weather", "output"), example_code, 100, 400)
    annual = objects[1]
    for destination, index in (("_model", 0), ("_wea", 1), ("output_folder_", 2)):
        next(p for p in annual.Params.Input if p.Name == destination).AddSource(paths.Params.Output[index])
    next(p for p in annual.Params.Input if p.Name == "executable_").AddSource(objects[0].Params.Output[1])
    next(p for p in objects[2].Params.Input if p.Name == "_manifest").AddSource(annual.Params.Output[10])
    factor = objects[3]
    next(p for p in factor.Params.Input if p.Name == "_model").AddSource(paths.Params.Output[0])
    next(p for p in factor.Params.Input if p.Name == "executable_").AddSource(objects[0].Params.Output[1])
    from Grasshopper.Kernel.Special import GH_BooleanToggle, GH_Panel
    for obj, port, x, y in ((objects[0], "_check", 100, 100), (annual, "_run", 450, 100), (objects[2], "_load", 950, 100), (factor, "_run", 1350, 100)):
        toggle = GH_BooleanToggle()
        toggle.CreateAttributes()
        toggle.Value = False
        toggle.Attributes.Pivot = PointF(x, y)
        document.AddObject(toggle, False)
        next(p for p in obj.Params.Input if p.Name == port).AddSource(toggle)
    panel = GH_Panel()
    panel.CreateAttributes()
    panel.UserText = "Foton beta: toggle install_ on Foton Settings once (or pip install foton-daylight[honeybee] yourself), then Check, then Run. Radiance is not needed. Turn live_ on for fast slider changes. Read START_HERE.md. CPU fallback is diagnostic only."
    panel.Attributes.Pivot = PointF(100, 650)
    document.AddObject(panel, False)
    archive = GH_Archive()
    archive.AppendObject(document, "Definition")
    for extension in ("gh", "ghx"):
        name = "Foton First Analysis." + extension
        if not archive.WriteToFile(os.path.join(OUTPUT, name), True, False):
            raise RuntimeError("Cannot write " + name)
        output_files.append(name)
    # Reload the native binary to catch serialization failures before packaging.
    loaded_archive = GH_Archive()
    loaded_archive.ReadFromFile(os.path.join(OUTPUT, "Foton First Analysis.gh"))
    restored_document = GH_Document()
    if not loaded_archive.ExtractObject(restored_document, "Definition"):
        raise RuntimeError("Example document round-trip failed")
    sources = ["scripts/build_grasshopper.py", "python/foton_bridge/__init__.py", "grasshopper_foton/foton_gh.py"] + ["grasshopper_foton/components/" + c[0] + ".py" for c in COMPONENTS]
    def sha(path):
        with open(path, "rb") as stream:
            return hashlib.sha256(stream.read()).hexdigest()
    import Rhino
    manifest = {"schema_version": 1, "rhino_version": str(Rhino.RhinoApp.Version), "round_trip_passed": True,
                "sources": dict((p, sha(os.path.join(ROOT, p))) for p in sources),
                "artifacts": dict((p, sha(os.path.join(OUTPUT, p))) for p in output_files)}
    with open(os.path.join(OUTPUT, "build_manifest.json"), "w") as stream:
        json.dump(manifest, stream, indent=2, sort_keys=True)
    print("Foton Grasshopper artifacts built in " + OUTPUT)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        if not os.path.isdir(OUTPUT):
            os.makedirs(OUTPUT)
        with open(os.path.join(OUTPUT, "build_error.log"), "w") as stream:
            stream.write(traceback.format_exc())
        raise
