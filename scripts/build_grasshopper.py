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

COMPONENT_NAMES = (
    "Foton Settings",
    "Foton Annual Daylight",
    "Foton Annual Results",
    "Foton Daylight Factor",
)


def source(path):
    with open(os.path.join(ROOT, path), "r") as stream:
        return stream.read()


def component_spec(name, code=None):
    """Read a component's ports, help text and placement from its source.

    The docstring is the one place each input and output is described:
    ``Args:`` and ``Returns:`` list them in order as ``name: description``,
    with longer descriptions continued on more deeply indented lines.
    """
    if code is None:
        code = source("grasshopper_foton/components/" + name + ".py")
    docstring = code.split('"""', 2)[1]
    head, _, ports = docstring.partition("Args:")
    inputs_text, _, outputs_text = ports.partition("Returns:")

    def entries(text):
        result = []
        for line in text.splitlines():
            name, separator, text = line.strip().partition(": ")
            port = line.startswith(" " * 8) and not line.startswith(" " * 9)
            if port and separator and name.replace("_", "").isalnum():
                result.append([name, text.strip()])
            elif line.strip() and result:
                result[-1][1] += " " + line.strip()
        return [tuple(entry) for entry in result]

    description = "\n\n".join(
        " ".join(paragraph.split())
        for paragraph in head.strip().rstrip("-").split("\n\n")
        if paragraph.strip()
    )

    def setting(key):
        return assigned_text(code, "ghenv.Component." + key)

    return {
        "name": name,
        "nickname": setting("NickName"),
        "category": setting("Category"),
        "subcategory": setting("SubCategory"),
        "description": description,
        "inputs": entries(inputs_text),
        "outputs": entries(outputs_text),
        "icon": "grasshopper_foton/icons/" + name + ".png",
    }


def assigned_text(code, target):
    """The quoted string assigned to ``target`` on a line of its own.

    Plain string handling rather than ``re``: Rhino's IronPython 2 runs regular
    expressions on .NET, where multiline anchors behave differently.
    """
    prefix = target + " = "
    for line in code.splitlines():
        line = line.strip()
        if line.startswith(prefix) and line[len(prefix):][:1] in ("\"", "'"):
            return line[len(prefix) + 1:-1]
    raise RuntimeError("No %s found" % target)


def component_version():
    return assigned_text(source("grasshopper_foton/foton_gh.py"), "COMPONENT_VERSION")


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
    from Grasshopper.Kernel import GH_Document, GH_Exposure, GH_UserObject, GH_ParamAccess
    from GH_IO.Serialization import GH_Archive
    from System import Guid
    from System.Drawing import PointF

    if not os.path.isdir(OUTPUT):
        os.makedirs(OUTPUT)
    document = GH_Document()
    # Rhino 8's "IronPython 2 Script" component. The legacy GhPython component
    # (410755b1-...) is marked obsolete in Rhino 8, which shows an "OLD" badge and
    # hides it from the ribbon. The external engine stays in CPython either way.
    component_id = Guid("97aa26ef-88ae-4ba6-98a6-ed6ddeca11d1")

    from System.Drawing import Bitmap

    def make_component(name, inputs, outputs, code, x, y, spec=None):
        obj = gh.Instances.ComponentServer.EmitObjectProxy(component_id).CreateInstance()
        obj.CreateAttributes()
        obj.UsingStandardOutputParam = False
        while obj.Params.Input.Count:
            obj.Params.UnregisterInputParameter(obj.Params.Input[0], True)
        while obj.Params.Output.Count:
            obj.Params.UnregisterOutputParameter(obj.Params.Output[0], True)
        from Grasshopper.Kernel import GH_ParameterSide
        for side, ports in ((GH_ParameterSide.Input, inputs), (GH_ParameterSide.Output, outputs)):
            for index, (port_name, hint) in enumerate(ports):
                param = obj.CreateParameter(side, index)
                param.Name = param.NickName = port_name
                # The tooltip shown when hovering over the input or output.
                param.Description = hint
                param.Access = GH_ParamAccess.item
                param.Optional = True
                if side == GH_ParameterSide.Input:
                    obj.Params.RegisterInputParam(param)
                else:
                    obj.Params.RegisterOutputParam(param)
        obj.Name = name
        obj.NickName = spec["nickname"] if spec else name
        obj.Category = spec["category"] if spec else "HB-Foton"
        obj.SubCategory = spec["subcategory"] if spec else "Recipes"
        if spec:
            obj.Description = spec["description"]
            obj.Message = version
            try:
                obj.SetIconOverride(Bitmap(os.path.join(ROOT, spec["icon"])))
            except Exception as error:  # the user object's own icon still applies
                print("WARNING: %s icon override failed: %s" % (name, error))
        obj.SetSource(code)
        obj.Params.OnParametersChanged()
        obj.VariableParameterMaintenance()
        # Rhino 8's script component can reset parameter text while it reads
        # the script, so set the tooltips again once it has settled.
        for params, ports in ((obj.Params.Input, inputs), (obj.Params.Output, outputs)):
            for param, (_, hint) in zip(params, ports):
                param.Description = hint
        obj.Attributes.Pivot = PointF(x, y)
        document.AddObject(obj, False)
        return obj

    version = component_version()
    objects, output_files, help_warnings = [], [], []
    for index, name in enumerate(COMPONENT_NAMES):
        spec = component_spec(name)
        inputs = [port for port, _ in spec["inputs"]]
        obj = make_component(name, spec["inputs"], spec["outputs"], embedded_script(name), 400 + index * 400, 250, spec)
        objects.append(obj)
        user = GH_UserObject()
        user.SetDataFromObject(obj)
        user.Description.Name = name
        user.Description.NickName = spec["nickname"]
        user.Description.Description = spec["description"] + "\n\nFoton " + version + " - https://github.com/snjsomnath/foton"
        user.Description.Category = spec["category"]
        user.Description.SubCategory = spec["subcategory"]
        user.Icon = Bitmap(os.path.join(ROOT, spec["icon"]))
        user.BaseGuid = obj.ComponentGuid
        # Without this a user object can inherit a hidden exposure, and
        # Grasshopper leaves it out of the ribbon and the canvas search.
        user.Exposure = GH_Exposure.primary
        user.Path = os.path.join(OUTPUT, name + ".ghuser")
        if not user.SaveToFile():
            raise RuntimeError("Failed to save " + user.Path)
        loaded = GH_UserObject(user.Path)
        loaded.ReadFromFile()
        restored = loaded.InstantiateObject()
        if restored is None or [p.Name for p in restored.Params.Input] != list(inputs):
            raise RuntimeError("User object round-trip failed: " + name)
        # Recorded rather than raised, so the build finishes and every loss is
        # listed at once; package_grasshopper.py refuses a build with any.
        for params, ports in ((restored.Params.Input, spec["inputs"]), (restored.Params.Output, spec["outputs"])):
            for param, (port, hint) in zip(params, ports):
                if param.Description != hint:
                    help_warnings.append("%s %s tooltip after reload: %r" % (name, port, param.Description))
        if loaded.Exposure != GH_Exposure.primary:
            raise RuntimeError("User object is not exposed in the ribbon: " + name)
        if loaded.Icon is None:
            help_warnings.append("%s has no icon after reload" % name)
        if not loaded.Description.Description.startswith(spec["description"][:40]):
            help_warnings.append("%s description after reload: %r" % (name, loaded.Description.Description))
        if loaded.Description.SubCategory != spec["subcategory"]:
            raise RuntimeError("User object is in the wrong ribbon panel: " + name)
        if restored.Obsolete:
            raise RuntimeError("User object is built on an obsolete component: " + name)
        restored_source = restored.TryGetSource()
        if not (restored_source[0] if isinstance(restored_source, tuple) else restored_source):
            raise RuntimeError("User object lost its script: " + name)
        output_files.append(name + ".ghuser")

    example_code = '''import os
root = os.path.dirname(ghenv.Component.OnPingDocument().FilePath)
model = os.path.join(root, "examples", "shoebox.hbjson")
weather = os.path.join(root, "examples", "gothenburg.epw")
output = os.path.join(os.path.expanduser("~"), "foton_simulation", "first_example")
'''
    paths = make_component(
        "Example files",
        (),
        (
            ("model", "The example shoebox model (HBJSON) next to this file."),
            ("weather", "The Gothenburg weather file next to this file."),
            ("output", "Where the example writes its results."),
        ),
        example_code,
        100,
        400,
    )
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
    panel.UserText = "Foton " + version + ": GPU daylight for Grasshopper.\n1. First time only: set install_ on Foton Settings to True. Foton installs into ~/.foton, with its own Python if needed.\n2. Toggle _check: it should name your GPU.\n3. Toggle _run on Foton Annual Daylight or Foton Daylight Factor.\nTurn live_ on for quick updates while you move sliders. Hover over any input for help. Guide: START_HERE.md"
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
    sources = (
        ["scripts/build_grasshopper.py", "python/foton_bridge/__init__.py", "grasshopper_foton/foton_gh.py"]
        + ["grasshopper_foton/components/" + name + ".py" for name in COMPONENT_NAMES]
        + ["grasshopper_foton/icons/" + name + ".png" for name in COMPONENT_NAMES]
    )
    def sha(path):
        with open(path, "rb") as stream:
            return hashlib.sha256(stream.read()).hexdigest()
    import Rhino
    manifest = {"schema_version": 1, "rhino_version": str(Rhino.RhinoApp.Version), "round_trip_passed": True,
                "help_and_icons_verified": not help_warnings, "help_warnings": help_warnings,
                "sources": dict((p, sha(os.path.join(ROOT, p))) for p in sources),
                "artifacts": dict((p, sha(os.path.join(OUTPUT, p))) for p in output_files)}
    with open(os.path.join(OUTPUT, "build_manifest.json"), "w") as stream:
        json.dump(manifest, stream, indent=2, sort_keys=True)
    for warning in help_warnings:
        print("WARNING: " + warning)
    print("Foton Grasshopper artifacts built in " + OUTPUT)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        if not os.path.isdir(OUTPUT):
            os.makedirs(OUTPUT)
        with open(os.path.join(OUTPUT, "build_error.log"), "w") as stream:
            stream.write(traceback.format_exc())
        # Print instead of raising, so Rhino shows no blocking error dialog.
        print("Foton Grasshopper build FAILED; see " + os.path.join(OUTPUT, "build_error.log"))
        print(traceback.format_exc())
