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
DEMO_NAME = "Foton Interactive Demo"
DEMO_ROOM = "grasshopper_foton/examples/demo_room.py"

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
# Build the bridge once per Rhino session: the stamp changes with its source.
if getattr(sys.modules.get("grasshopper_foton.foton_gh"), "__file__", None) != "foton_embedded_%s.py":
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
''' % (stamp, common, stamp, bridge, component, name)


LAST_RUN_CODE = '''"""Find the newest saved run of this demo, and the DA threshold it used.

It is wired to the Save run button rather than to the run itself, so moving a
slider does not make Foton Annual Results and Honeybee read the folder again.
The button's release, once the run has finished, picks up the new folder.
"""
import glob
import json
import os

run = None
threshold = None
if default:
    saved = glob.glob(os.path.join(str(default) + "*", "run_manifest.json"))
    if saved:
        newest = max(saved, key=os.path.getmtime)
        run = os.path.dirname(newest)
        with open(newest) as stream:
            threshold = json.load(stream).get("request", {}).get("threshold")
'''

DF_SWITCH_CODE = '''"""Lock Foton Daylight Factor, and everything it feeds, while the toggle is off.

A locked component does not run, so dragging a slider waits only for the
annual study. Locking has to wait until the current solution has finished.
"""
import Grasshopper

document = ghenv.Component.OnPingDocument()
locked = not on
targets = []
for factor in [obj for obj in document.Objects if obj.Name == "Foton Daylight Factor"]:
    targets.append(factor)
    # Its heatmap and panel: Ladybug resets component nicknames, so follow the wires.
    for output in factor.Params.Output:
        for recipient in output.Recipients:
            targets.append(recipient.Attributes.GetTopLevel.DocObject)
if any(obj.Locked != locked for obj in targets):
    def apply(doc):
        for obj in targets:
            obj.Locked = locked
            obj.ExpireSolution(False)
    document.ScheduleSolution(1, Grasshopper.Kernel.GH_Document.GH_ScheduleDelegate(apply))
'''

AGREEMENT_CODE = '''"""Compare Foton's DA with Honeybee's reading of the same results folder."""


def values(tree):
    if tree is None:
        return []
    return [float(str(value)) for value in tree.AllData() if value is not None]


foton, honeybee = values(foton_DA), values(hb_DA)
if not foton or len(foton) != len(honeybee):
    agreement = "Click Save run to compare Foton with Honeybee."
else:
    difference = max(abs(a - b) for a, b in zip(foton, honeybee))
    agreement = "Honeybee reads the saved run: {0} sensors, largest DA difference {1:.2f} %".format(
        len(foton), difference)
'''

DEMO_FILES_CODE = '''import os
root = os.path.dirname(ghenv.Component.OnPingDocument().FilePath)
weather = os.path.join(root, "examples", "gothenburg.epw")
output = os.path.join(os.path.expanduser("~"), "foton_simulation", "interactive_demo")
'''

DEMO_HELP = (
    "How to use this demo (Foton {version})\n"
    "1. First time only: set install_ on Foton Settings to True and wait for it to finish.\n"
    "2. Drag the Room sliders. Daylight autonomy on the floor updates as you drag.\n"
    "3. Toggle Neighbour block and move it closer. Turn on Daylight factor to see it on the plan "
    "beside the room (each slider move then takes a little longer).\n"
    "4. Press Save run to write a results folder and compare Foton with Honeybee.\n"
    "Blue groups are Foton's own components (HB-Foton tab), green ones Ladybug Tools, "
    "orange ones only belong to this demo. Needs Ladybug Tools."
)


def build_demo(make_component, version):
    """Lay out "Foton Interactive Demo": sliders, a live room and a saved run, left to right."""
    import Grasshopper as gh
    from Grasshopper.Kernel import GH_Document, GH_ParamAccess
    from Grasshopper.Kernel.Special import (
        GH_BooleanToggle, GH_ButtonObject, GH_ColourSwatch, GH_Group, GH_NumberSlider, GH_Panel,
    )
    from Grasshopper.GUI.Base import GH_SliderAccuracy
    from System import Decimal
    from System.Drawing import Color, PointF, RectangleF

    demo = GH_Document()
    server = gh.Instances.ComponentServer

    def place(obj, x, y):
        if obj.Attributes is None:
            obj.CreateAttributes()
        obj.Attributes.Pivot = PointF(x, y)
        demo.AddObject(obj, False)
        return obj

    def top_left(obj, x, y):
        """Move a component so its top-left corner is at (x, y); its pivot is mid-height."""
        obj.Attributes.ExpireLayout()
        obj.Attributes.PerformLayout()
        bounds, pivot = obj.Attributes.Bounds, obj.Attributes.Pivot
        obj.Attributes.Pivot = PointF(pivot.X + x - bounds.Left, pivot.Y + y - bounds.Top)
        obj.Attributes.ExpireLayout()
        obj.Attributes.PerformLayout()
        return obj

    def foton(name, x, y):
        spec = component_spec(name)
        return top_left(make_component(
            name, spec["inputs"], spec["outputs"], embedded_script(name), x, y, spec, target=demo), x, y)

    def script(name, inputs, outputs, code, x, y):
        return top_left(make_component(name, inputs, outputs, code, x, y, target=demo), x, y)

    def ladybug(name, x, y):
        proxy = server.FindObjectByName(name, True, True)
        if proxy is None or proxy.Obsolete:
            raise RuntimeError(name + " was not found: build the demo in a Rhino with Ladybug Tools")
        return top_left(place(proxy.CreateInstance(), x, y), x, y)

    def slider(label, low, high, value, decimals, x, y):
        obj = GH_NumberSlider()
        obj.CreateAttributes()
        obj.Slider.Minimum = Decimal(low)
        obj.Slider.Maximum = Decimal(high)
        obj.Slider.DecimalPlaces = decimals
        obj.Slider.Type = GH_SliderAccuracy.Integer if decimals == 0 else GH_SliderAccuracy.Float
        obj.SetSliderValue(Decimal(value))
        obj.NickName = label
        obj.Attributes.Bounds = RectangleF(x, y, 300, 20)
        return place(obj, x, y)

    def toggle(label, value, x, y):
        obj = GH_BooleanToggle()
        obj.CreateAttributes()
        obj.NickName = label
        obj.Value = value
        return place(obj, x, y)

    def panel(text, x, y, width=220, height=40):
        obj = GH_Panel()
        obj.CreateAttributes()
        obj.UserText = text
        obj.Attributes.Bounds = RectangleF(x, y, width, height)
        return place(obj, x, y)

    def inp(obj, name):
        return next(p for p in obj.Params.Input if name in (p.Name, p.NickName))

    def out(obj, name):
        return next(p for p in obj.Params.Output if name in (p.Name, p.NickName))

    def wire(source, obj, name):
        # A panel is itself a parameter, with no inputs of its own.
        (obj if isinstance(obj, GH_Panel) else inp(obj, name)).AddSource(source)

    def group(label, members, colour):
        obj = GH_Group()
        obj.CreateAttributes()
        obj.NickName = label
        obj.Colour = colour
        for member in members:
            obj.AddObject(member.InstanceGuid)
        demo.AddObject(obj, False)

    # 1. Room: everything a designer would drag.
    room_sliders = [
        ("width", slider("Room width (m)", 3, 12, 6, 1, 40, 260)),
        ("depth", slider("Room depth (m)", 3, 12, 10, 1, 40, 290)),
        ("height", slider("Room height (m)", 2.4, 5, 3, 1, 40, 320)),
        ("floors", slider("Floors", 1, 6, 1, 0, 40, 370)),
        ("rooms", slider("Rooms per floor", 1, 6, 1, 0, 40, 400)),
        ("rotation", slider("Rotation (degrees)", -180, 180, 0, 0, 40, 450)),
        ("wwr_south", slider("Window-to-wall, south", 0, 0.9, 0.3, 2, 40, 500)),
        ("wwr_east", slider("Window-to-wall, east", 0, 0.9, 0, 2, 40, 530)),
        ("wwr_north", slider("Window-to-wall, north", 0, 0.9, 0, 2, 40, 560)),
        ("wwr_west", slider("Window-to-wall, west", 0, 0.9, 0, 2, 40, 590)),
        ("overhang", slider("Overhang depth (m)", 0, 2, 0.5, 2, 40, 640)),
    ]
    neighbour = toggle("Neighbour block", False, 40, 690)
    distance = slider("Distance to neighbour (m)", 3, 30, 10, 1, 40, 720)
    help_panel = panel(DEMO_HELP.format(version=version), 40, 20, 330, 200)

    # 2. Model: the room builder and the shipped weather file.
    with open(os.path.join(ROOT, DEMO_ROOM), "r") as stream:
        room_code = stream.read()
    room = script(
        "Demo Room",
        [(name, "From the Room sliders.") for name, _ in room_sliders]
        + [("neighbour", "True adds a block facing the south wall."),
           ("distance", "Distance from the south wall to the block, in metres.")],
        (
            ("model", "The Honeybee Model, with a sensor grid at desk height."),
            ("grid_mesh", "Each room's sensor grid as a mesh, for the DA heatmap."),
            ("df_mesh", "The same grids beside the building, for the DF heatmap."),
            ("walls", "Walls with their windows cut out."),
            ("glass", "Windows."),
            ("shades", "Overhangs."),
            ("context", "The neighbouring block."),
        ),
        room_code,
        480,
        260,
    )
    room.Hidden = True
    for name, obj in room_sliders:
        wire(obj, room, name)
    wire(neighbour, room, "neighbour")
    wire(distance, room, "distance")
    files = script("Demo files", (), (("weather", "The Gothenburg weather file next to this file."),
                                      ("output", "Where Save run writes its results.")),
                   DEMO_FILES_CODE, 480, 620)
    previews = []
    for name, colour, y in (
        ("walls", Color.FromArgb(255, 236, 234, 228), 720),
        ("glass", Color.FromArgb(90, 150, 200, 235), 780),
        ("shades", Color.FromArgb(255, 70, 74, 82), 840),
        ("context", Color.FromArgb(255, 190, 190, 195), 900),
    ):
        swatch = GH_ColourSwatch()
        swatch.CreateAttributes()
        swatch.SwatchColour = colour
        place(swatch, 480, y + 10)
        preview = ladybug("Custom Preview", 600, y - 5)
        wire(out(room, name), preview, "Geometry")
        wire(swatch, preview, "Material")
        previews.extend([swatch, preview])

    # 3. Foton, live: both studies rerun whenever the room changes.
    settings = foton("Foton Settings", 1000, 960)
    install = toggle("Install", False, 840, 1040)
    check = toggle("Check", True, 840, 1070)
    wire(install, settings, "install_")
    wire(check, settings, "_check")
    threshold = slider("DA threshold (lux)", 100, 1000, 300, 0, 700, 100)
    live = toggle("Live", True, 840, 720)
    run = toggle("Run", True, 840, 750)
    annual = foton("Foton Annual Daylight", 1000, 140)
    factor = foton("Foton Daylight Factor", 1000, 640)
    for obj in (annual, factor):
        wire(out(room, "model"), obj, "_model")
        wire(out(settings, "executable"), obj, "executable_")
        wire(live, obj, "live_")
        wire(run, obj, "_run")
    wire(out(files, "weather"), annual, "_wea")
    wire(threshold, annual, "thresholds_")
    # Daylight factor stays off while dragging: one live study is quicker than two.
    factor_on = toggle("Daylight factor", False, 480, 1020)
    factor_switch = script("Daylight factor switch", (("on", "True runs Foton Daylight Factor and its heatmap."),),
                           (), DF_SWITCH_CODE, 620, 1010)
    wire(factor_on, factor_switch, "on")

    # 4. Results: DA on the room, DF on the plan beside it.
    da_map = ladybug("LB Spatial Heatmap", 1420, 160)
    wire(out(annual, "DA"), da_map, "_values")
    wire(out(room, "grid_mesh"), da_map, "_mesh")
    da_title = panel("Daylight autonomy (%)", 1250, 300, 150, 20)
    wire(da_title, da_map, "legend_title_")
    df_map = ladybug("LB Spatial Heatmap", 1420, 640)
    factor.Locked = df_map.Locked = True
    wire(out(factor, "DF"), df_map, "_values")
    wire(out(room, "df_mesh"), df_map, "_mesh")
    df_title = panel("Daylight factor (%)", 1250, 780, 150, 20)
    wire(df_title, df_map, "legend_title_")
    sda = panel("", 1620, 180, 160, 40)
    sda.NickName = "sDA (%)"
    wire(out(annual, "sDA"), sda, "Input")
    mean_df = panel("", 1620, 660, 160, 40)
    mean_df.NickName = "Mean DF (%)"
    mean_df.Locked = True
    wire(out(factor, "mean_DF"), mean_df, "Input")

    # 5. A saved run, read back by Foton Annual Results and Honeybee.
    save = GH_ButtonObject()
    save.CreateAttributes()
    save.NickName = "Save run"
    place(save, 1900, 560)
    saved = foton("Foton Annual Daylight", 2040, 140)
    wire(out(room, "model"), saved, "_model")
    wire(out(files, "weather"), saved, "_wea")
    wire(out(files, "output"), saved, "output_folder_")
    wire(threshold, saved, "thresholds_")
    wire(out(settings, "executable"), saved, "executable_")
    wire(save, saved, "_run")
    last = script("Last saved run", (("saved", "The Save run button, so a new run is picked up."),
                                     ("default", "Where Foton saves the demo's runs.")),
                  (("run", "The newest saved run."), ("threshold", "The DA threshold that run used.")),
                  LAST_RUN_CODE, 2300, 300)
    wire(save, last, "saved")
    wire(out(files, "output"), last, "default")
    results = foton("Foton Annual Results", 2580, 200)
    wire(out(last, "run"), results, "_manifest")
    load = toggle("Load", True, 2480, 420)
    wire(load, results, "_load")
    metrics = ladybug("HB Annual Daylight Metrics", 2900, 260)
    wire(out(results, "results"), metrics, "_results")
    # The saved run's own threshold, so Honeybee matches it after the slider moves on.
    wire(out(last, "threshold"), metrics, "_threshold_")
    agreement = script(
        "Honeybee agreement",
        (("foton_DA", "DA from Foton Annual Results."), ("hb_DA", "DA from HB Annual Daylight Metrics.")),
        (("agreement", "How closely the two agree."),),
        AGREEMENT_CODE,
        3160,
        280,
    )
    for param in agreement.Params.Input:
        param.Access = GH_ParamAccess.tree
    wire(out(results, "DA"), agreement, "foton_DA")
    wire(out(metrics, "DA"), agreement, "hb_DA")
    agreement_panel = panel("", 3360, 290, 280, 60)
    wire(out(agreement, "agreement"), agreement_panel, "Input")

    foton_colour = Color.FromArgb(70, 120, 180, 255)
    ladybug_colour = Color.FromArgb(70, 120, 220, 140)
    demo_colour = Color.FromArgb(90, 255, 180, 90)
    foton_label = "Foton components (in the HB-Foton tab)"
    demo_label = "Demo only, not part of Foton"
    group(demo_label + ": room sliders", [obj for _, obj in room_sliders] + [neighbour, distance], demo_colour)
    group(demo_label + ": room builder", [room, files] + previews, demo_colour)
    group(demo_label + ": daylight factor on or off", [factor_on, factor_switch], demo_colour)
    group(foton_label + ": live runs", [settings, install, check, threshold, live, run, annual, factor],
          foton_colour)
    group("Ladybug Tools: heatmaps", [da_map, df_map, da_title, df_title, sda, mean_df], ladybug_colour)
    group(foton_label + ": saved run", [save, saved], foton_colour)
    group(demo_label + ": keeps the last run", [last], demo_colour)
    group(foton_label + ": reads the saved run", [results, load], foton_colour)
    group("Honeybee: reads Foton's results folder", [metrics], ladybug_colour)
    group(demo_label + ": compares the two", [agreement, agreement_panel], demo_colour)
    return demo


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

    def make_component(name, inputs, outputs, code, x, y, spec=None, target=None):
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
        obj.SubCategory = spec["subcategory"] if spec else "Foton"
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
        # Rhino 8's script component rebuilds each parameter's Description from
        # its type hint whenever it reads the script or a saved file; only the
        # script parameter's ToolTip is kept, and Description then shows it.
        for params, ports in ((obj.Params.Input, inputs), (obj.Params.Output, outputs)):
            for param, (_, hint) in zip(params, ports):
                param.ToolTip = hint
                param.Description = hint
        # The component's own Description is rebuilt from its Tooltip the same
        # way, which matters for the copies saved in the example definition.
        if spec:
            obj.Tooltip = spec["description"]
            obj.Description = spec["description"]
        obj.Attributes.Pivot = PointF(x, y)
        (document if target is None else target).AddObject(obj, False)
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
    for obj, port, x, y in ((objects[0], "install_", 100, 40), (objects[0], "_check", 100, 100), (annual, "_run", 450, 100), (objects[2], "_load", 950, 100), (factor, "_run", 1350, 100)):
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
    def save_definition(definition, title):
        archive = GH_Archive()
        archive.AppendObject(definition, "Definition")
        for extension in ("gh", "ghx"):
            name = title + "." + extension
            if not archive.WriteToFile(os.path.join(OUTPUT, name), True, False):
                raise RuntimeError("Cannot write " + name)
            output_files.append(name)
        # Reload the native binary to catch serialization failures before packaging.
        loaded_archive = GH_Archive()
        loaded_archive.ReadFromFile(os.path.join(OUTPUT, title + ".gh"))
        restored_document = GH_Document()
        if not loaded_archive.ExtractObject(restored_document, "Definition"):
            raise RuntimeError(title + " round-trip failed")
        for restored in restored_document.Objects:
            if restored.Name in COMPONENT_NAMES:
                spec = component_spec(restored.Name)
                if restored.Description != spec["description"]:
                    help_warnings.append("%s description in %s: %r" % (restored.Name, title, restored.Description))
                for params, ports in ((restored.Params.Input, spec["inputs"]), (restored.Params.Output, spec["outputs"])):
                    for param, (port, hint) in zip(params, ports):
                        if param.Description != hint:
                            help_warnings.append("%s %s tooltip in %s: %r" % (restored.Name, port, title, param.Description))

    save_definition(document, "Foton First Analysis")
    save_definition(build_demo(make_component, version), DEMO_NAME)
    sources = (
        ["scripts/build_grasshopper.py", "python/foton_bridge/__init__.py", "grasshopper_foton/foton_gh.py"]
        + ["grasshopper_foton/components/" + name + ".py" for name in COMPONENT_NAMES]
        + ["grasshopper_foton/icons/" + name + ".png" for name in COMPONENT_NAMES]
        + [DEMO_ROOM]
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
