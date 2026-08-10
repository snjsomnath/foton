"""
Load a completed Foton annual-daylight manifest without rerunning the solver.

GhPython inputs
---------------
_manifest   Item, ``run_manifest.json`` path or its containing output folder
_load       Item, Boolean load toggle

GhPython outputs
----------------
report, results, DA, cDA, UDI, UDI_low, UDI_up, sDA, grid_ids, room_ids,
manifest, timings, warnings, folder

``results`` and the metric DataTrees follow the same branch ordering used by
Honeybee annual result components and LB Spatial Heatmap.
"""

from __future__ import print_function

import os
import sys

try:
    from grasshopper_foton.foton_gh import FotonError, load_result_bundle
except ImportError:
    parent = os.environ.get("FOTON_GH_PARENT")
    if parent:
        parent = os.path.abspath(os.path.expanduser(parent))
        if parent not in sys.path:
            sys.path.insert(0, parent)
    try:
        from grasshopper_foton.foton_gh import FotonError, load_result_bundle
    except ImportError:
        raise RuntimeError(
            "Cannot import grasshopper_foton. Add the repository parent directory "
            "to Rhino search paths (for example /Users/ssanjay/GitHub/foton), "
            "or set FOTON_GH_PARENT to that directory."
        )


ghenv.Component.Name = "Foton Annual Results"
ghenv.Component.NickName = "FotonResults"
ghenv.Component.Message = "Protocol 1"
ghenv.Component.Category = "HB-Foton"
ghenv.Component.SubCategory = "4 :: Results"
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


if globals().get("_load", False):
    if not globals().get("_manifest"):
        raise ValueError("Connect a manifest path or Foton output folder.")
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
        warnings = bundle["warnings"]
        folder = bundle["folder"]
        report = "Loaded {0} SensorGrid result branches.".format(len(grid_ids))
        ghenv.Component.Message = "{0} grids".format(len(grid_ids))
    except FotonError as error:
        report = str(error)
        ghenv.Component.Message = "Failed"
        raise RuntimeError(report)

