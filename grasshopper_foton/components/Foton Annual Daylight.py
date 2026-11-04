# Foton: GPU daylight simulation for Grasshopper.
# Copyright (c) 2026 Sanjay Somanath. Released under the MIT licence.
# https://github.com/snjsomnath/foton
"""
Run an annual daylight study on the GPU and get Daylight Autonomy, Continuous
Daylight Autonomy, Useful Daylight Illuminance and Spatial Daylight Autonomy
for every sensor grid in a Honeybee model.

Results are written in the same layout as Honeybee's Annual Daylight recipe,
so connect results to HB Annual Daylight Metrics or HB Annual Results to Data
to use them with other Ladybug Tools components. Pair a metric with the grid
meshes in LB Spatial Heatmap to see it on the model.
-
    Args:
        _model: A Honeybee Model with sensor grids, or the path to an HBJSON file.
        _wea: A Ladybug Wea, or the path to an EPW or WEA weather file.
        schedule_: Optional. An occupancy schedule: a Honeybee schedule, 8760
            values, or a CSV file. Default: 8 am to 6 pm every day.
        north_: Optional. The north direction as degrees counterclockwise from
            the Y axis, or a vector. Default: 0.
        thresholds_: Optional. Illuminance thresholds in lux, as text
            ("-t 300 -lt 100 -ut 3000") or three numbers: the DA threshold,
            then the lower and upper UDI limits. Default: 300, 100, 3000.
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
        reuse_: Optional. True (the default) loads an earlier result for exactly
            the same inputs instead of running again.
        direct_samples_: Optional. Advanced: rays per sky patch for direct light.
            Leave empty to use the quality setting.
        indirect_samples_: Optional. Advanced: rays per sensor for reflected
            light. Leave empty to use the quality setting.
        bounces_: Optional. How many times light reflects. Default: 8, the
            validated setting.
        seed_: Optional. Random seed, so the same inputs give the same
            numbers. Default: 0.
        live_: Optional. True keeps Foton running in the background so slider
            and geometry changes update in seconds. Live runs write no files,
            so results stays empty.
        _run: Set to True to run the study.
    Returns:
        report: Progress and messages from the run.
        results: The results folder, for HB Annual Daylight Metrics and HB
            Annual Results to Data. Empty in live mode.
        DA: Daylight Autonomy (%) for each sensor, one branch per grid.
        cDA: Continuous Daylight Autonomy (%) for each sensor, one branch per grid.
        UDI: Useful Daylight Illuminance (%): occupied hours between the lower
            and upper limits, one branch per grid.
        UDI_low: Percentage of occupied hours below the lower UDI limit.
        UDI_up: Percentage of occupied hours above the upper UDI limit.
        sDA: Spatial Daylight Autonomy (%) for each grid: the share of floor
            area with DA of at least 50 %.
        grid_ids: Sensor grid identifiers, in branch order.
        room_ids: Room identifiers, in branch order.
        manifest: Path to run_manifest.json. Connect to Foton Annual Results to
            reload this run later without running it again.
        timings: How long each stage took, as a dictionary.
        timings_text: The same timings as text, for a Panel.
        warnings: Anything worth checking about the model or the run.
        folder: The Foton output folder.
"""

from __future__ import print_function

import os
import re
import sys

try:
    from grasshopper_foton.foton_gh import COMPONENT_VERSION, FotonCancelled, FotonError
    from grasshopper_foton.foton_gh import run_annual_daylight
except ImportError:
    parent = os.environ.get("FOTON_GH_PARENT")
    if parent:
        parent = os.path.abspath(os.path.expanduser(parent))
        if parent not in sys.path:
            sys.path.insert(0, parent)
    try:
        from grasshopper_foton.foton_gh import COMPONENT_VERSION, FotonCancelled, FotonError
        from grasshopper_foton.foton_gh import run_annual_daylight
    except ImportError:
        raise RuntimeError(
            "Cannot import grasshopper_foton. Add the repository parent directory "
            "to Rhino search paths (for example /Users/ssanjay/GitHub/foton), "
            "or set FOTON_GH_PARENT to that directory."
        )


ghenv.Component.Name = "Foton Annual Daylight"
ghenv.Component.NickName = "FotonAnnual"
ghenv.Component.Message = COMPONENT_VERSION
ghenv.Component.Category = "HB-Foton"
ghenv.Component.SubCategory = "Recipes"
if hasattr(ghenv.Component, "AdditionalHelpFromDocStrings"):
    ghenv.Component.AdditionalHelpFromDocStrings = "2"


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
timings_text = None
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
            maximum_bounces=optional("bounces_"),
            scene_seed=optional("seed_", 0),
            progress=on_progress,
            cancel=cancelled,
            live=bool(optional("live_", False)),
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
        timings_text = "\n".join(
            "{0}: {1}".format(key, timings[key]) for key in sorted(timings.keys())
        )
        warnings = bundle["warnings"]
        folder = bundle["folder"]
        for warning in warnings:
            warn(str(warning))
        reused = bool(bundle["manifest"].get("grasshopper_reused", False))
        live = bool(bundle["manifest"].get("live", False))
        if live:
            messages.append(
                "Live run complete. No files were written; turn live_ off "
                "to save a results folder for Honeybee components."
            )
        else:
            messages.append("Reused compatible results." if reused else "Foton run complete.")
        report = "\n".join(messages)
        ghenv.Component.Message = "Live" if live else "Reused" if reused else "Complete"
    except FotonCancelled as error:
        report = str(error)
        ghenv.Component.Message = "Cancelled"
        warn(report)
    except FotonError as error:
        report = str(error)
        ghenv.Component.Message = "Failed"
        raise RuntimeError(report)
