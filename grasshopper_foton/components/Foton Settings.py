"""
Discover and inspect the external ``foton-honeybee`` installation.

GhPython inputs
---------------
executable_  Item, optional explicit ``foton-honeybee``/``.exe`` path
backend_     Item, optional backend to inspect; default ``auto``
_check       Item, Boolean check toggle

GhPython outputs
----------------
report, executable, engine_version, protocol_version, backend, capabilities,
cache_folder
"""

from __future__ import print_function

import json

from grasshopper_foton.foton_gh import FotonError, capabilities as get_capabilities


ghenv.Component.Name = "Foton Settings"
ghenv.Component.NickName = "FotonSettings"
ghenv.Component.Message = "Protocol 1"
ghenv.Component.Category = "HB-Foton"
ghenv.Component.SubCategory = "0 :: Settings"
ghenv.Component.AdditionalHelpFromDocStrings = "1"


report = None
executable = None
engine_version = None
protocol_version = None
backend = None
capabilities = None
cache_folder = None


if globals().get("_check", False):
    try:
        data = get_capabilities(
            globals().get("executable_"), globals().get("backend_") or "auto"
        )
        executable = data["executable"]
        engine_version = data["engine_version"]
        protocol_version = data["protocol_version"]
        backend = data.get("engine", {}).get("backend")
        capabilities = data
        cache_folder = data.get("weather_cache")
        report = json.dumps(data, indent=2, sort_keys=True)
        ghenv.Component.Message = "{0} / {1}".format(engine_version, backend)
    except FotonError as error:
        report = str(error)
        ghenv.Component.Message = "Not found"
        raise RuntimeError(report)

