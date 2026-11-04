# Foton: GPU daylight simulation for Grasshopper.
# Copyright (c) 2026 Sanjay Somanath. Released under the MIT licence.
# https://github.com/snjsomnath/foton
"""
Find Foton on this computer, install it if needed, and check that it can use
the GPU.

Most people connect nothing but a Boolean Toggle to _check. The first time,
set install_ to True: Foton is installed into its own folder (~/.foton), with
its own Python if this computer has none. Nothing outside that folder changes.
After that, Check reports the Foton version and the GPU it will use.
-
    Args:
        executable_: Optional. Full path to foton-honeybee (foton-honeybee.exe on
            Windows). Leave empty to look in ~/.foton, on PATH and in the usual
            Python folders.
        backend_: Optional. The GPU backend to check: auto (the default), metal,
            vulkan, or reference (a slow CPU fallback for diagnosis only).
        python_: Optional. A Python 3.10 to 3.13 for install_ to build Foton's
            environment from. Leave empty to use one found on this computer,
            or a private Python 3.12 if there is none.
        install_: Set to True once to install Foton, or to upgrade an older
            version, and then check it. Needs an internet connection and takes
            a minute or two.
        _check: Set to True to find Foton and report what it can run on.
    Returns:
        report: What was found or installed, and the full check report.
        executable: Path to foton-honeybee. Connect it to executable_ on the
            other Foton components if Foton is not in a standard place.
        engine_version: The installed Foton version.
        protocol_version: The version of the protocol the components use to
            talk to Foton.
        backend: The backend Foton will use, such as metal or vulkan.
        capabilities: The full check report as a dictionary.
        cache_folder: Folder where Foton keeps prepared weather data.
"""

from __future__ import print_function

import json
import os
import sys

try:
    from grasshopper_foton.foton_gh import COMPONENT_VERSION, FotonError, capabilities as get_capabilities, install_foton
except ImportError:
    parent = os.environ.get("FOTON_GH_PARENT")
    if parent:
        parent = os.path.abspath(os.path.expanduser(parent))
        if parent not in sys.path:
            sys.path.insert(0, parent)
    try:
        from grasshopper_foton.foton_gh import COMPONENT_VERSION, FotonError, capabilities as get_capabilities, install_foton
    except ImportError:
        raise RuntimeError(
            "Cannot import grasshopper_foton. Add the repository parent directory "
            "to Rhino search paths (for example /Users/ssanjay/GitHub/foton), "
            "or set FOTON_GH_PARENT to that directory."
        )


ghenv.Component.Name = "Foton Settings"
ghenv.Component.NickName = "FotonSettings"
ghenv.Component.Message = COMPONENT_VERSION
ghenv.Component.Category = "HB-Foton"
ghenv.Component.SubCategory = "Settings"
if hasattr(ghenv.Component, "AdditionalHelpFromDocStrings"):
    ghenv.Component.AdditionalHelpFromDocStrings = "2"


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
