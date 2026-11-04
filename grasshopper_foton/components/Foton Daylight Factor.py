# Foton: GPU daylight simulation for Grasshopper.
# Copyright (c) 2026 Sanjay Somanath. Released under the MIT licence.
# https://github.com/snjsomnath/foton
"""
Run a daylight factor study on the GPU for every sensor grid in a Honeybee
model.

Daylight factor is the light indoors under an overcast sky, as a percentage of
the light outdoors. It needs no weather file. Results are written in the same
layout as Honeybee's Daylight Factor recipe. Pair DF with the grid meshes in
LB Spatial Heatmap to see it on the model.
-
    Args:
        _model: A Honeybee Model with sensor grids, or the path to an HBJSON file.
        grid_filter_: Optional. Which sensor grids to run, by identifier;
            wildcards like "Office*" work. Default: all grids.
        quality_: Optional. "final" (the default, validated against Radiance)
            or "preview" (faster and noisier, for quick design checks).
        sky_density_: Optional. 1 for 145 sky patches (Tregenza, the default)
            or 2 for 577 (Reinhart MF:2).
        backend_: Optional. auto (the default), metal, vulkan, or reference (a
            slow CPU fallback for diagnosis only).
        output_folder_: Optional. Where to write results. Default: a folder named
            after the model in Honeybee's simulation folder.
        executable_: Optional. Path to foton-honeybee, usually from Foton Settings.
        bounces_: Optional. How many times light reflects. Default: 8, the
            validated setting.
        live_: Optional. True keeps Foton running in the background so changes
            update in seconds. Live runs write no files, so results stays empty.
        _run: Set to True to run the study.
    Returns:
        report: Progress and messages from the run.
        results: The results folder, in Honeybee's daylight factor layout.
            Empty in live mode.
        DF: Daylight factor (%) for each sensor, one branch per grid.
        mean_DF: Average daylight factor (%) for each grid.
        grid_ids: Sensor grid identifiers, in branch order.
        room_ids: Room identifiers, in branch order.
        timings_text: How long each stage took, as text for a Panel.
        folder: The Foton output folder.
"""

from __future__ import print_function

import os
import re
import sys

try:
    from grasshopper_foton.foton_gh import COMPONENT_VERSION, FotonCancelled, FotonError
    from grasshopper_foton.foton_gh import run_daylight_factor
except ImportError:
    parent = os.environ.get("FOTON_GH_PARENT")
    if parent:
        parent = os.path.abspath(os.path.expanduser(parent))
        if parent not in sys.path:
            sys.path.insert(0, parent)
    try:
        from grasshopper_foton.foton_gh import COMPONENT_VERSION, FotonCancelled, FotonError
        from grasshopper_foton.foton_gh import run_daylight_factor
    except ImportError:
        raise RuntimeError(
            "Cannot import grasshopper_foton. Add the repository parent directory "
            "to Rhino search paths (for example /Users/ssanjay/GitHub/foton), "
            "or set FOTON_GH_PARENT to that directory."
        )


ghenv.Component.Name = "Foton Daylight Factor"
ghenv.Component.NickName = "FotonDF"
ghenv.Component.Message = COMPONENT_VERSION
ghenv.Component.Category = "HB-Foton"
ghenv.Component.SubCategory = "Recipes"
if hasattr(ghenv.Component, "AdditionalHelpFromDocStrings"):
    ghenv.Component.AdditionalHelpFromDocStrings = "2"


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
