"""
Run Foton annual daylight through the external ``foton-honeybee`` executable.

GhPython component setup (IronPython 2.7):

Inputs
------
_model             Item, Honeybee Model or HBJSON path
_wea               Item, Ladybug Wea or EPW/WEA path
schedule_           Item, optional 8760-value collection/schedule or CSV path
north_              Item, optional degrees or Rhino vector; default 0
thresholds_         Item, optional ``-t 300 -lt 100 -ut 3000`` or 3 values
grid_filter_        Item, optional identifier wildcard; default ``*``
quality_            Item, ``preview`` or ``final``; default ``final``
sky_density_        Item, 1 (Tregenza) or 2 (Reinhart MF:2); default 1
backend_            Item, ``auto``, ``metal``, ``vulkan``, or ``reference``
output_folder_      Item, requested output folder
executable_         Item, optional full path to ``foton-honeybee``
reuse_              Item, reuse a compatible completed output; default True
direct_samples_     Item, optional advanced override
indirect_samples_   Item, optional advanced override
bounces_            Item, optional diffuse bounce count; default 1
seed_               Item, optional deterministic seed; default 0
_run                Item, Boolean run toggle

Outputs
-------
report              Text progress/warnings
results             One-item results-folder list; connect to HB annual result components
DA, cDA              Sensor values in one DataTree branch per SensorGrid
UDI, UDI_low, UDI_up Sensor values in one DataTree branch per SensorGrid
sDA                  One area-weighted percentage per SensorGrid
grid_ids, room_ids   Lists in the same order as the DataTree branches
manifest             Path to ``run_manifest.json``
timings              Timing dictionary
warnings             Validation warnings
folder               Foton output folder

Add the repository parent folder to Rhino's IronPython module search paths so
``grasshopper_foton`` can be imported. Foton itself runs in external CPython.
"""

from __future__ import print_function

import os
import re
import sys

try:
    from grasshopper_foton.foton_gh import FotonCancelled, FotonError
    from grasshopper_foton.foton_gh import run_annual_daylight
except ImportError:
    parent = os.environ.get("FOTON_GH_PARENT")
    if parent:
        parent = os.path.abspath(os.path.expanduser(parent))
        if parent not in sys.path:
            sys.path.insert(0, parent)
    try:
        from grasshopper_foton.foton_gh import FotonCancelled, FotonError
        from grasshopper_foton.foton_gh import run_annual_daylight
    except ImportError:
        raise RuntimeError(
            "Cannot import grasshopper_foton. Add the repository parent directory "
            "to Rhino search paths (for example /Users/ssanjay/GitHub/foton), "
            "or set FOTON_GH_PARENT to that directory."
        )


ghenv.Component.Name = "Foton Annual Daylight"
ghenv.Component.NickName = "FotonAnnual"
ghenv.Component.Message = "Protocol 1"
ghenv.Component.Category = "HB-Foton"
ghenv.Component.SubCategory = "3 :: Recipes"
if hasattr(ghenv.Component, "AdditionalHelpFromDocStrings"):
    ghenv.Component.AdditionalHelpFromDocStrings = "1"


report = None
results = None
DA = None
cDA = None
UDI = None
UDI_low = None
UDI_up = None
sDA = None
grid_ids = None
room_ids = None
manifest = None
timings = None
warnings = None
folder = None


def optional(name, default=None):
    value = globals().get(name, default)
    return default if value is None else value


def default_output(model):
    identifier = getattr(model, "identifier", "annual_daylight")
    identifier = re.sub(r"[^A-Za-z0-9_.-]+", "_", str(identifier))
    try:
        from honeybee.config import folders as hb_folders

        root = hb_folders.default_simulation_folder
    except ImportError:
        root = os.path.join(os.path.expanduser("~"), "foton_simulation")
    return os.path.join(root, identifier, "foton_annual_daylight")


messages = []


def on_progress(message):
    event = message.get("event", "progress")
    detail = message.get("message", event)
    progress_value = message.get("progress")
    if progress_value is not None:
        detail = "{0:.0f}% {1}".format(float(progress_value) * 100.0, detail)
    messages.append(detail)
    ghenv.Component.Message = detail
    try:
        import Rhino

        Rhino.RhinoApp.Wait()
    except ImportError:
        pass


def warn(message):
    try:
        from Grasshopper.Kernel import GH_RuntimeMessageLevel

        ghenv.Component.AddRuntimeMessage(GH_RuntimeMessageLevel.Warning, message)
    except ImportError:
        pass


def cancelled():
    """Let ESC terminate the external process during a long trace."""
    try:
        import scriptcontext

        return bool(scriptcontext.escape_test(False))
    except ImportError:
        return False


if globals().get("_run", False):
    if globals().get("_model") is None or globals().get("_wea") is None:
        raise ValueError("Connect both _model and _wea before setting _run to True.")
    requested_output = optional("output_folder_", default_output(_model))
    try:
        bundle = run_annual_daylight(
            _model,
            _wea,
            requested_output,
            schedule=optional("schedule_"),
            north=optional("north_", 0.0),
            thresholds_value=optional("thresholds_"),
            grid_filter=optional("grid_filter_", "*"),
            quality=optional("quality_", "final"),
            sky_density=optional("sky_density_", 1),
            backend=optional("backend_", "auto"),
            executable=optional("executable_"),
            reuse=bool(optional("reuse_", True)),
            direct_samples=optional("direct_samples_"),
            maximum_samples=optional("indirect_samples_"),
            maximum_bounces=optional("bounces_", 1),
            scene_seed=optional("seed_", 0),
            progress=on_progress,
            cancel=cancelled,
        )
        results = bundle["results"]
        DA, cDA = bundle["da"], bundle["cda"]
        UDI, UDI_low, UDI_up = (
            bundle["udi"],
            bundle["udi_low"],
            bundle["udi_up"],
        )
        sDA = bundle["sda"]
        grid_ids, room_ids = bundle["grid_ids"], bundle["room_ids"]
        manifest = bundle["manifest_path"]
        timings = bundle["timings"]
        warnings = bundle["warnings"]
        folder = bundle["folder"]
        for warning in warnings:
            warn(str(warning))
        reused = bool(bundle["manifest"].get("grasshopper_reused", False))
        messages.append("Reused compatible results." if reused else "Foton run complete.")
        report = "\n".join(messages)
        ghenv.Component.Message = "Reused" if reused else "Complete"
    except FotonCancelled as error:
        report = str(error)
        ghenv.Component.Message = "Cancelled"
        warn(report)
    except FotonError as error:
        report = str(error)
        ghenv.Component.Message = "Failed"
        raise RuntimeError(report)
