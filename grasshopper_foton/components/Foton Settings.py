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
            or a private Python 3.12 if there is none. Type uv to always
            download the private Python, even when one is installed.
        install_: Set to True once to install Foton, or to upgrade an older
            version, and then check it. It runs in the background, so Rhino
            stays usable, and the component shows how long it has run. Needs an
            internet connection and takes a minute or two, longer if Foton has
            to download its own Python. Set to False to stop it.
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
import time

try:
    from grasshopper_foton.foton_gh import COMPONENT_VERSION, FotonError, capabilities as get_capabilities
    from grasshopper_foton.foton_gh import background_install, cancel_install, install_log_path, install_status, reset_install
except ImportError:
    parent = os.environ.get("FOTON_GH_PARENT")
    if parent:
        parent = os.path.abspath(os.path.expanduser(parent))
        if parent not in sys.path:
            sys.path.insert(0, parent)
    try:
        from grasshopper_foton.foton_gh import COMPONENT_VERSION, FotonError, capabilities as get_capabilities
        from grasshopper_foton.foton_gh import background_install, cancel_install, install_log_path, install_status, reset_install
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
ghenv.Component.SubCategory = "Foton"
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


def error(message):
    # A runtime error turns the component red but, unlike raising, still lets
    # the outputs below be set, so report shows the whole log.
    from Grasshopper.Kernel import GH_RuntimeMessageLevel

    ghenv.Component.AddRuntimeMessage(GH_RuntimeMessageLevel.Error, str(message))


def remark(message):
    from Grasshopper.Kernel import GH_RuntimeMessageLevel

    ghenv.Component.AddRuntimeMessage(GH_RuntimeMessageLevel.Remark, str(message))


def check_again_in(milliseconds):
    """Run this component again shortly, to show install progress.

    The install runs on a background thread, so Rhino stays usable; this
    component only looks at its progress once a second.
    """
    from Grasshopper.Kernel import GH_Document

    document = ghenv.Component.OnPingDocument()
    if document is None:
        return
    component = ghenv.Component

    def expire(_document):
        component.ExpireSolution(False)

    document.ScheduleSolution(milliseconds, GH_Document.GH_ScheduleDelegate(expire))


install_log = []
configured = globals().get("executable_")
installing = bool(globals().get("install_", False)) and not configured
if not installing:
    # Turning install_ off stops a running install and forgets a finished one.
    cancel_install()
    reset_install()
else:
    state = background_install(globals().get("python_"))
    install_log = list(state["log"])
    if state["running"]:
        seconds = int(time.time() - state["started"])
        report = "\n".join(install_log[-30:])
        ghenv.Component.Message = "Installing {0}:{1:02d}".format(seconds // 60, seconds % 60)
        remark(
            "Installing Foton in the background; Rhino stays usable. The first "
            "install can take a few minutes. Set install_ to False to stop it."
        )
        check_again_in(1000)
    elif state["error"]:
        report = "\n".join(install_log + [state["error"], "Full log: " + install_log_path()])
        ghenv.Component.Message = "Install failed"
        error(state["error"])
    else:
        configured = state["executable"]

waiting = installing and configured is None

if not waiting and (globals().get("_check", False) or installing):
    try:
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
    except FotonError as failure:
        report = "\n".join(install_log + [str(failure)])
        ghenv.Component.Message = "Not found"
        error(failure)
