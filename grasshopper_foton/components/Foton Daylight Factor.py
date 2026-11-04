"""
Run Foton daylight factor through the external ``foton-honeybee`` executable.

Daylight factor is the indoor illuminance under a CIE overcast sky as a
percentage of the unobstructed outdoor illuminance. No weather file is needed.

GhPython component setup (IronPython 2.7):

Inputs
------
_model             Item, Honeybee Model or HBJSON path
grid_filter_        Item, optional identifier wildcard; default ``*``
quality_            Item, ``preview`` or ``final``; default ``final``
sky_density_        Item, 1 (Tregenza) or 2 (Reinhart MF:2); default 1
backend_            Item, ``auto``, ``metal``, ``vulkan``, or ``reference``
output_folder_      Item, requested output folder
executable_         Item, optional full path to ``foton-honeybee``
bounces_            Item, optional diffuse bounce count; default 8 (the validated setting)
live_               Item, keep Foton running between runs for fast slider
                    changes; writes no files, so ``results`` stays empty
_run                Item, Boolean run toggle

Outputs
-------
report              Text progress/warnings
results             One-item results-folder list in Honeybee's daylight-factor
                    layout (one .res file per SensorGrid); empty in live mode
DF                  Daylight factor (%) in one DataTree branch per SensorGrid
mean_DF             Mean daylight factor (%) per SensorGrid
grid_ids, room_ids  Lists in the same order as the DataTree branches
timings_text        Timing lines for direct Panel display
folder              Foton output folder

Pair ``DF`` with the SensorGrid meshes in LB Spatial Heatmap; branch and
sensor order follow the HBJSON model.
"""

from __future__ import print_function

import os
import re
import sys

try:
    from grasshopper_foton.foton_gh import FotonCancelled, FotonError
    from grasshopper_foton.foton_gh import run_daylight_factor
except ImportError:
    parent = os.environ.get("FOTON_GH_PARENT")
    if parent:
        parent = os.path.abspath(os.path.expanduser(parent))
        if parent not in sys.path:
            sys.path.insert(0, parent)
    try:
        from grasshopper_foton.foton_gh import FotonCancelled, FotonError
        from grasshopper_foton.foton_gh import run_daylight_factor
    except ImportError:
        raise RuntimeError(
            "Cannot import grasshopper_foton. Add the repository parent directory "
            "to Rhino search paths (for example /Users/ssanjay/GitHub/foton), "
            "or set FOTON_GH_PARENT to that directory."
        )


ghenv.Component.Name = "Foton Daylight Factor"
ghenv.Component.NickName = "FotonDF"
ghenv.Component.Message = "Protocol 1"
ghenv.Component.Category = "HB-Foton"
ghenv.Component.SubCategory = "3 :: Recipes"
if hasattr(ghenv.Component, "AdditionalHelpFromDocStrings"):
    ghenv.Component.AdditionalHelpFromDocStrings = "1"


report = None
results = None
DF = None
mean_DF = None
grid_ids = None
room_ids = None
timings_text = None
folder = None


def optional(name, default=None):
    value = globals().get(name, default)
    return default if value is None else value


def default_output(model):
    identifier = getattr(model, "identifier", "daylight_factor")
    identifier = re.sub(r"[^A-Za-z0-9_.-]+", "_", str(identifier))
    try:
        from honeybee.config import folders as hb_folders

        root = hb_folders.default_simulation_folder
    except ImportError:
        root = os.path.join(os.path.expanduser("~"), "foton_simulation")
    return os.path.join(root, identifier, "foton_daylight_factor")


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
    if globals().get("_model") is None:
        raise ValueError("Connect _model before setting _run to True.")
    live = bool(optional("live_", False))
    try:
        bundle = run_daylight_factor(
            _model,
            optional("output_folder_", default_output(_model)),
            grid_filter=optional("grid_filter_", "*"),
            quality=optional("quality_", "final"),
            sky_density=optional("sky_density_", 1),
            backend=optional("backend_", "auto"),
            executable=optional("executable_"),
            maximum_bounces=optional("bounces_"),
            progress=on_progress,
            cancel=cancelled,
            live=live,
        )
        results = bundle["results"]
        DF = bundle["df"]
        mean_DF = bundle["mean_df"]
        grid_ids, room_ids = bundle["grid_ids"], bundle["room_ids"]
        timings = bundle["timings"]
        timings_text = "\n".join(
            "{0}: {1}".format(key, timings[key]) for key in sorted(timings.keys())
        )
        folder = bundle["folder"]
        for warning in bundle["warnings"]:
            warn(str(warning))
        if live:
            messages.append(
                "Live run complete. No files were written; turn live_ off "
                "to save a results folder."
            )
        else:
            messages.append("Foton run complete.")
        report = "\n".join(messages)
        ghenv.Component.Message = "Live" if live else "Complete"
    except FotonCancelled as error:
        report = str(error)
        ghenv.Component.Message = "Cancelled"
        warn(report)
    except FotonError as error:
        report = str(error)
        ghenv.Component.Message = "Failed"
        raise RuntimeError(report)
