# Foton: GPU daylight simulation for Grasshopper.
# Copyright (c) 2026 The Foton contributors. Released under the MIT licence.
# https://github.com/snjsomnath/foton
"""
Load a saved Foton annual daylight run without running it again.

Connect the manifest output of Foton Annual Daylight, or a results folder,
and the outputs match the ones that run produced.
-
    Args:
        _manifest: The path to run_manifest.json, or the folder that holds it.
        _load: Set to True to load the results.
    Returns:
        report: What was loaded.
        results: The results folder, for HB Annual Daylight Metrics and HB
            Annual Results to Data.
        DA: Daylight Autonomy (%) for each sensor, one branch per grid.
        cDA: Continuous Daylight Autonomy (%) for each sensor, one branch per grid.
        UDI: Useful Daylight Illuminance (%) for each sensor, one branch per grid.
        UDI_low: Percentage of occupied hours below the lower UDI limit.
        UDI_up: Percentage of occupied hours above the upper UDI limit.
        sDA: Spatial Daylight Autonomy (%) for each grid.
        grid_ids: Sensor grid identifiers, in branch order.
        room_ids: Room identifiers, in branch order.
        manifest: Path to the loaded run_manifest.json.
        timings: How long each stage of the original run took.
        timings_text: The same timings as text, for a Panel.
        warnings: Warnings recorded with the run.
        folder: The Foton output folder.
"""

from __future__ import print_function

import os
import sys

try:
    from grasshopper_foton.foton_gh import COMPONENT_VERSION, FotonError, load_result_bundle
except ImportError:
    parent = os.environ.get("FOTON_GH_PARENT")
    if parent:
        parent = os.path.abspath(os.path.expanduser(parent))
        if parent not in sys.path:
            sys.path.insert(0, parent)
    try:
        from grasshopper_foton.foton_gh import COMPONENT_VERSION, FotonError, load_result_bundle
    except ImportError:
        raise RuntimeError(
            "Cannot import grasshopper_foton. Add the repository parent directory "
            "to Rhino search paths (for example /Users/ssanjay/GitHub/foton), "
            "or set FOTON_GH_PARENT to that directory."
        )


ghenv.Component.Name = "Foton Annual Results"
ghenv.Component.NickName = "FotonResults"
ghenv.Component.Message = COMPONENT_VERSION
ghenv.Component.Category = "HB-Foton"
ghenv.Component.SubCategory = "Foton"
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


if globals().get("_load", False) and not globals().get("_manifest"):
    # Nothing to load yet: a live run, or a run that has not been saved.
    report = (
        "No saved Foton run to load. Connect a manifest path or output folder, "
        "or turn live_ off on Foton Annual Daylight and run it to save one."
    )
    ghenv.Component.Message = "Waiting"
elif globals().get("_load", False):
    try:
        bundle = load_result_bundle(_manifest)
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
        report = "Loaded {0} SensorGrid result branches.".format(len(grid_ids))
        ghenv.Component.Message = "{0} grids".format(len(grid_ids))
    except FotonError as error:
        report = str(error)
        ghenv.Component.Message = "Failed"
        raise RuntimeError(report)

