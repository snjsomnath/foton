"""
Discover and inspect the external ``foton-honeybee`` installation.

GhPython inputs
---------------
executable_  Item, optional explicit ``foton-honeybee``/``.exe`` path
backend_     Item, optional backend to inspect; default ``auto``
python_      Item, optional Python 3.10-3.13 to install into; found automatically
install_     Item, Boolean: install Foton into its own environment (~/.foton)
             if it is missing or too old, then check it
_check       Item, Boolean check toggle

Without executable_, Foton is looked for in its own environment, on PATH and
in the usual Python folders, so most users connect nothing.

GhPython outputs
----------------
report, executable, engine_version, protocol_version, backend, capabilities,
cache_folder
"""

from __future__ import print_function

import json
import os
import sys

try:
    from grasshopper_foton.foton_gh import FotonError, capabilities as get_capabilities, install_foton
except ImportError:
    parent = os.environ.get("FOTON_GH_PARENT")
    if parent:
        parent = os.path.abspath(os.path.expanduser(parent))
        if parent not in sys.path:
            sys.path.insert(0, parent)
    try:
        from grasshopper_foton.foton_gh import FotonError, capabilities as get_capabilities, install_foton
    except ImportError:
        raise RuntimeError(
            "Cannot import grasshopper_foton. Add the repository parent directory "
            "to Rhino search paths (for example /Users/ssanjay/GitHub/foton), "
            "or set FOTON_GH_PARENT to that directory."
        )


ghenv.Component.Name = "Foton Settings"
ghenv.Component.NickName = "FotonSettings"
ghenv.Component.Message = "Protocol 1"
ghenv.Component.Category = "HB-Foton"
ghenv.Component.SubCategory = "0 :: Settings"
if hasattr(ghenv.Component, "AdditionalHelpFromDocStrings"):
    ghenv.Component.AdditionalHelpFromDocStrings = "1"


report = None
executable = None
engine_version = None
protocol_version = None
backend = None
capabilities = None
cache_folder = None


def warn(message):
    from Grasshopper.Kernel import GH_RuntimeMessageLevel

    ghenv.Component.AddRuntimeMessage(GH_RuntimeMessageLevel.Warning, str(message))


def cancelled():
    try:
        import scriptcontext

        return bool(scriptcontext.escape_test(False))
    except ImportError:
        return False


install_log = []


def on_install(line):
    install_log.append(line)
    ghenv.Component.Message = "Installing"
    try:
        import Rhino

        Rhino.RhinoApp.Wait()
    except ImportError:
        pass


if globals().get("_check", False) or globals().get("install_", False):
    try:
        configured = globals().get("executable_")
        if globals().get("install_", False) and not configured:
            configured = install_foton(
                globals().get("python_"), progress=on_install, cancel=cancelled
            )
        data = get_capabilities(configured, globals().get("backend_") or "auto")
        executable = data["executable"]
        engine_version = data["engine_version"]
        protocol_version = data["protocol_version"]
        backend = data.get("selected_backend", data.get("engine", {}).get("name"))
        capabilities = data
        cache_folder = data.get("weather_cache")
        report = "\n".join(install_log + [json.dumps(data, indent=2, sort_keys=True)])
        ghenv.Component.Message = "{0} / {1}".format(engine_version, backend)
        if not data.get("ready", True):
            ghenv.Component.Message = "Setup required"
        for message in data.get("errors", []) + data.get("warnings", []):
            warn(message)
    except FotonError as error:
        report = "\n".join(install_log + [str(error)])
        ghenv.Component.Message = "Not found"
        raise RuntimeError(report)
