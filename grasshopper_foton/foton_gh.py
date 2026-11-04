"""Pure-Python bridge between IronPython GhPython and ``foton-honeybee``.

This module deliberately uses only Python 2.7-compatible syntax and standard
library modules. Foton and NumPy remain in the external CPython process.
"""

from __future__ import print_function

import hashlib
import json
import math
import os
import shutil
import subprocess
import tempfile
import threading
import time
import sys

try:
    from foton_bridge import resolve_manifest, reusable, reuse_identity
except ImportError:
    # Source checkout; release bundles contain foton_bridge beside this package.
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "python"))
    from foton_bridge import resolve_manifest, reusable, reuse_identity

try:
    import Queue as queue
except ImportError:
    import queue

try:
    string_types = (basestring,)  # noqa: F821
except NameError:
    string_types = (str,)


PROTOCOL_NAME = "foton.honeybee"
PROTOCOL_VERSION = 1
METRICS = ("da", "cda", "udi_lower", "udi", "udi_upper")


class FotonError(RuntimeError):
    pass


class FotonCancelled(FotonError):
    pass


def _subprocess_environment(executable):
    """Build a clean env so external CPython ignores IronPython runtime vars."""
    env = os.environ.copy()
    for key in (
        "PYTHONHOME",
        "PYTHONPATH",
        "PYTHONEXECUTABLE",
        "__PYVENV_LAUNCHER__",
    ):
        env.pop(key, None)
    executable_dir = os.path.dirname(os.path.abspath(executable))
    if executable_dir:
        path = env.get("PATH", "")
        env["PATH"] = (
            executable_dir if not path else executable_dir + os.pathsep + path
        )
    return env


def _text(value):
    if isinstance(value, bytes):
        return value.decode("utf-8", "replace")
    return value


def _file_sha256(path):
    digest = hashlib.sha256()
    stream = open(path, "rb")
    try:
        while True:
            chunk = stream.read(1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
    finally:
        stream.close()
    return digest.hexdigest()


def _json_bytes(value):
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    )
    if not isinstance(encoded, bytes):
        encoded = encoded.encode("utf-8")
    return encoded


def request_data(
    model,
    wea,
    schedule=None,
    backend="auto",
    grid_filter="*",
    north=0.0,
    quality="final",
    sky_density=1,
    threshold=300.0,
    udi_lower=100.0,
    udi_upper=3000.0,
    target_time=50.0,
    direct_samples=None,
    maximum_samples=None,
    maximum_bounces=8,  # keep in step with foton.honeybee.annual.DEFAULT_MAXIMUM_BOUNCES
    scene_seed=0,
    export_illuminance=True,
):
    """Create the same content-based compatibility fingerprint as protocol v1."""
    request = {
        "model": os.path.abspath(model),
        "model_sha256": _file_sha256(model),
        "wea": os.path.abspath(wea),
        "wea_sha256": _file_sha256(wea),
        "schedule": os.path.abspath(schedule) if schedule else None,
        "schedule_sha256": _file_sha256(schedule) if schedule else None,
        "backend": backend,
        "grid_filter": grid_filter,
        "north": float(north),
        "quality": quality,
        "sky_density": int(sky_density),
        "threshold": float(threshold),
        "udi_lower": float(udi_lower),
        "udi_upper": float(udi_upper),
        "target_time": float(target_time),
        "direct_samples": direct_samples,
        "maximum_samples": maximum_samples,
        "maximum_bounces": int(maximum_bounces),
        "scene_seed": int(scene_seed),
        "export_illuminance": bool(export_illuminance),
        "fingerprint_schema": 1,
    }
    compatible = dict(
        (key, value)
        for key, value in request.items()
        if key not in ("model", "wea", "schedule")
    )
    request["fingerprint"] = hashlib.sha256(_json_bytes(compatible)).hexdigest()
    return request


# The package the one-click install puts in Foton's own environment. The lower
# bound is the first release with the built-in sky, the daylight-factor
# command and the background worker these components use.
ENGINE_REQUIREMENT = "foton-daylight[honeybee]>=0.3.2,<0.4"
ENGINE_MINIMUM = (0, 3, 2)
ENGINE_MAXIMUM = (0, 4, 0)
SUPPORTED_PYTHONS = ((3, 13), (3, 12), (3, 11), (3, 10))
DEFAULT_BOUNCES = 8  # keep in step with foton.honeybee.annual.DEFAULT_MAXIMUM_BOUNCES


def _windows():
    # IronPython reports sys.platform as "cli"; os.name is reliable.
    return os.name == "nt"


def _home():
    return os.path.expanduser("~")


def foton_home():
    """Folder holding Foton's own Python environment (``FOTON_HOME`` overrides)."""
    configured = os.environ.get("FOTON_HOME")
    return os.path.abspath(os.path.expanduser(configured or os.path.join(_home(), ".foton")))


def environment_folder():
    return os.path.join(foton_home(), "venv")


def _environment_file(folder, name):
    if _windows():
        return os.path.join(folder, "Scripts", name + ".exe")
    return os.path.join(folder, "bin", name)


def environment_executable():
    return _environment_file(environment_folder(), "foton-honeybee")


def _unique(paths):
    seen, result = set(), []
    for path in paths:
        if not path:
            continue
        key = os.path.normcase(os.path.abspath(path))
        if key not in seen:
            seen.add(key)
            result.append(path)
    return result


def _python_versions():
    return ["{0}{1}".format(major, minor) for major, minor in SUPPORTED_PYTHONS]


def candidate_executables():
    """Every place ``foton-honeybee`` is usually installed, most likely first.

    Rhino rarely inherits the PATH of a terminal (on macOS never), so the
    usual pip, venv and pipx locations are searched as well as PATH.
    """
    name = "foton-honeybee.exe" if _windows() else "foton-honeybee"
    home = _home()
    folders = [os.path.dirname(environment_executable())]
    folders.extend(os.environ.get("PATH", "").split(os.pathsep))
    if _windows():
        local = os.environ.get("LOCALAPPDATA", os.path.join(home, "AppData", "Local"))
        roaming = os.environ.get("APPDATA", os.path.join(home, "AppData", "Roaming"))
        for version in _python_versions():
            folders.append(os.path.join(local, "Programs", "Python", "Python" + version, "Scripts"))
            folders.append(os.path.join(roaming, "Python", "Python" + version, "Scripts"))
            folders.append(os.path.join("C:" + os.sep, "Program Files", "Python" + version, "Scripts"))
        folders.append(os.path.join(home, ".local", "bin"))
        folders.append(os.path.join(home, "ladybug_tools", "python", "Scripts"))
    else:
        for version in _python_versions():
            dotted = version[0] + "." + version[1:]
            folders.append("/Library/Frameworks/Python.framework/Versions/" + dotted + "/bin")
            folders.append(os.path.join(home, "Library", "Python", dotted, "bin"))
        folders.extend([
            os.path.join(home, ".local", "bin"),
            "/opt/homebrew/bin",
            "/usr/local/bin",
            os.path.join(home, "ladybug_tools", "python", "bin"),
        ])
    return _unique(os.path.join(folder, name) for folder in folders if folder)


def discover_executable(configured=None):
    """Find ``foton-honeybee``: the connected path, Foton's own environment, then the usual places."""
    configured = configured or os.environ.get("FOTON_HONEYBEE_EXE")
    if configured:
        path = os.path.abspath(os.path.expanduser(str(configured)))
        if not os.path.isfile(path):
            raise FotonError("Configured foton-honeybee executable does not exist: " + path)
        return path
    for path in candidate_executables():
        if os.path.isfile(path):
            return os.path.abspath(path)
    raise FotonError(
        "foton-honeybee was not found. Set install_ to True on Foton Settings to "
        "install it, or connect its full path to executable_. Looked in "
        + environment_folder() + ", on PATH and in the usual Python folders."
    )


def _version_tuple(text):
    parts = []
    for item in str(text).split(".")[:3]:
        digits = ""
        for character in item:
            if not character.isdigit():
                break
            digits += character
        parts.append(int(digits or 0))
    while len(parts) < 3:
        parts.append(0)
    return tuple(parts)


def engine_version_supported(version):
    value = _version_tuple(version)
    return ENGINE_MINIMUM <= value < ENGINE_MAXIMUM


def _base_python_candidates(configured=None):
    """Python 3.10 to 3.13 interpreters that could host Foton's environment."""
    commands = []
    if configured:
        commands.append([os.path.abspath(os.path.expanduser(str(configured)))])
    home = _home()
    if _windows():
        launcher = os.path.join(os.environ.get("WINDIR", "C:" + os.sep + "Windows"), "py.exe")
        if os.path.isfile(launcher):
            for major, minor in SUPPORTED_PYTHONS:
                commands.append([launcher, "-{0}.{1}".format(major, minor)])
        local = os.environ.get("LOCALAPPDATA", os.path.join(home, "AppData", "Local"))
        for version in _python_versions():
            commands.append([os.path.join(local, "Programs", "Python", "Python" + version, "python.exe")])
            commands.append([os.path.join("C:" + os.sep, "Program Files", "Python" + version, "python.exe")])
        # The Python that the Ladybug Tools installer ships, when it is new enough.
        commands.append([os.path.join(home, "ladybug_tools", "python", "python.exe")])
    else:
        for version in _python_versions():
            dotted = version[0] + "." + version[1:]
            commands.append(["/Library/Frameworks/Python.framework/Versions/" + dotted + "/bin/python3"])
            commands.append(["/opt/homebrew/bin/python" + dotted])
            commands.append(["/usr/local/bin/python" + dotted])
            commands.append(["/usr/bin/python" + dotted])
        commands.append([os.path.join(home, "ladybug_tools", "python", "bin", "python3")])
        commands.append(["/opt/homebrew/bin/python3"])
        commands.append(["/usr/local/bin/python3"])
        if not os.path.isdir("/Library/Frameworks"):
            # Not macOS, where /usr/bin/python3 can open an Xcode install prompt.
            commands.append(["/usr/bin/python3"])
    seen, result = set(), []
    for command in commands:
        if not os.path.isfile(command[0]):
            continue
        key = tuple(command)
        if key not in seen:
            seen.add(key)
            result.append(command)
    return result


_PYTHON_PROBE = (
    "import sys, venv, ensurepip; "
    "print('%d.%d' % sys.version_info[:2])"
)


def find_base_python(configured=None):
    """Return ``(command, "3.x")`` for the first usable Python, or raise FotonError."""
    tried = []
    for command in _base_python_candidates(configured):
        try:
            code, lines = _stream_command(command + ["-c", _PYTHON_PROBE], timeout=30.0)
        except (OSError, FotonError):
            tried.append(" ".join(command) + " (would not start)")
            continue
        text = "".join(lines).strip().splitlines()
        found = text[-1].strip() if text else ""
        if code == 0 and _version_tuple(found)[:2] in SUPPORTED_PYTHONS:
            return command, found
        tried.append(" ".join(command) + " (" + (found or "unusable") + ")")
    detail = "; ".join(tried) if tried else "none found"
    raise FotonError(
        "Foton needs Python 3.10 to 3.13 to install into. Install one from "
        "python.org, or connect a python executable to python_. Tried: " + detail
    )


# When no Python 3.10 to 3.13 is installed, Foton fetches uv (a single-file
# Python installer from Astral) and lets it download a private Python. Both
# live in Foton's own folder, so nothing else on the computer changes.
UV_PYTHON = "3.12"
UV_DOWNLOAD = "https://github.com/astral-sh/uv/releases/latest/download/"


def _system():
    if _windows():
        return "windows"
    if os.path.isdir("/System/Library/CoreServices"):
        return "macos"
    return "linux"


def _machine():
    """``arm64`` or ``x86_64`` for the running computer."""
    try:
        import clr  # noqa: F401  (IronPython inside Rhino)
        from System.Runtime.InteropServices import Architecture, RuntimeInformation

        arm = RuntimeInformation.OSArchitecture == Architecture.Arm64
        return "arm64" if arm else "x86_64"
    except ImportError:
        import platform

        machine = platform.machine().lower()
        return "arm64" if machine in ("arm64", "aarch64") else "x86_64"


def uv_asset():
    """The name of the uv release archive for this computer."""
    arch = "aarch64" if _machine() == "arm64" else "x86_64"
    system = _system()
    if system == "windows":
        return "uv-{0}-pc-windows-msvc.zip".format(arch)
    if system == "macos":
        return "uv-{0}-apple-darwin.tar.gz".format(arch)
    return "uv-{0}-unknown-linux-gnu.tar.gz".format(arch)


def uv_executable():
    return os.path.join(foton_home(), "uv", "uv.exe" if _windows() else "uv")


def _system_tool(name):
    """curl and tar ship with macOS and with Windows 10 (1803) and later."""
    if _windows():
        path = os.path.join(os.environ.get("WINDIR", "C:" + os.sep + "Windows"), "System32", name + ".exe")
    else:
        path = os.path.join("/usr/bin", name)
    return path if os.path.isfile(path) else name


def uv_environment():
    """Keep uv's Python, cache and settings inside Foton's folder."""
    home = foton_home()
    return {
        "UV_PYTHON_INSTALL_DIR": os.path.join(home, "python"),
        "UV_CACHE_DIR": os.path.join(home, "cache"),
        "UV_PYTHON_PREFERENCE": "only-managed",
        "UV_NO_CONFIG": "1",
    }


def ensure_uv(progress=None, cancel=None):
    """Download uv into Foton's folder unless it is already there."""
    target = uv_executable()
    if os.path.isfile(target):
        return target

    def report(line):
        if progress is not None and line.strip():
            progress(line.rstrip())

    folder = os.path.dirname(target)
    staging = tempfile.mkdtemp(prefix="uv-", dir=_ensure_folder(foton_home()))
    try:
        archive = os.path.join(staging, uv_asset())
        report("Downloading uv from " + UV_DOWNLOAD + uv_asset())
        code, lines = _stream_command(
            [_system_tool("curl"), "-fsSL", "--retry", "2", "-o", archive, UV_DOWNLOAD + uv_asset()],
            report,
            cancel,
        )
        if code != 0 or not os.path.isfile(archive):
            raise FotonError(
                "Could not download uv. Check the internet connection, or install "
                "Python 3.10 to 3.13 from python.org and try again:\n" + "".join(lines[-10:])
            )
        unpacked = os.path.join(staging, "unpacked")
        os.makedirs(unpacked)
        code, lines = _stream_command([_system_tool("tar"), "-xf", archive, "-C", unpacked], report, cancel)
        if code != 0:
            raise FotonError("Could not unpack uv:\n" + "".join(lines[-10:]))
        name = os.path.basename(target)
        found = None
        for root, _directories, files in os.walk(unpacked):
            if name in files:
                found = os.path.join(root, name)
                break
        if found is None:
            raise FotonError("The uv download did not contain " + name)
        _ensure_folder(folder)
        shutil.move(found, target)
        if not _windows():
            os.chmod(target, 0o755)
    finally:
        shutil.rmtree(staging, True)
    return target


def _ensure_folder(folder):
    if not os.path.isdir(folder):
        os.makedirs(folder)
    return folder


def install_foton(python=None, progress=None, cancel=None, upgrade=False):
    """Create Foton's own environment and pip install the engine into it.

    Nothing is installed when the environment already holds a supported
    version and ``upgrade`` is False, so a toggle left on costs one check.
    Returns the path of the installed ``foton-honeybee``.
    """
    executable = environment_executable()
    if not upgrade and os.path.isfile(executable):
        try:
            current = capabilities(executable)
            if engine_version_supported(current.get("engine_version")):
                if progress is not None:
                    progress("Foton {0} is already installed in {1}".format(
                        current.get("engine_version"), environment_folder()))
                return executable
        except FotonError:
            pass
    folder = environment_folder()

    def report(line):
        if progress is not None and line.strip():
            progress(line.rstrip())

    if not os.path.isfile(_environment_file(folder, "python")):
        try:
            command, version = find_base_python(python)
        except FotonError:
            if python:
                raise  # the user chose a Python; don't silently use another
            command = None
        _ensure_folder(os.path.dirname(folder))
        if command is not None:
            report("Using Python {0}: {1}".format(version, " ".join(command)))
            report("Creating Foton's environment in " + folder)
            code, lines = _stream_command(command + ["-m", "venv", folder], report, cancel)
        else:
            report("No Python 3.10 to 3.13 found. Foton will download its own Python "
                   + UV_PYTHON + " into " + foton_home())
            uv = ensure_uv(progress, cancel)
            report("Creating Foton's environment in " + folder)
            code, lines = _stream_command(
                [uv, "venv", "--seed", "--python", UV_PYTHON, folder],
                report,
                cancel,
                extra_env=uv_environment(),
            )
        if code != 0:
            raise FotonError("Could not create " + folder + ":\n" + "".join(lines[-20:]))
    python_path = _environment_file(folder, "python")
    report("Installing " + ENGINE_REQUIREMENT + "")
    code, lines = _stream_command(
        [python_path, "-m", "pip", "install", "--upgrade",
         "--disable-pip-version-check", ENGINE_REQUIREMENT],
        report,
        cancel,
    )
    if code != 0:
        raise FotonError("pip could not install Foton:\n" + "".join(lines[-20:]))
    if not os.path.isfile(executable):
        raise FotonError("The install finished but " + executable + " is missing")
    return executable


def _stream_command(command, on_line=None, cancel=None, timeout=None, extra_env=None):
    """Run a command, passing each output line on; returns (exit code, lines)."""
    env = _subprocess_environment(command[0])
    if extra_env:
        env.update(extra_env)
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env=env,
    )
    lines = _mailbox()

    def read():
        while True:
            line = process.stdout.readline()
            if not line:
                break
            lines.put(_text(line))
        lines.put(None)

    reader = threading.Thread(target=read)
    reader.daemon = True
    reader.start()
    collected = []
    started = time.time()
    try:
        while True:
            if cancel is not None and cancel():
                raise FotonCancelled("Cancelled")
            if timeout is not None and time.time() - started > timeout:
                raise FotonError("Timed out: " + " ".join(command))
            try:
                line = lines.get(True, 0.1)
            except queue.Empty:
                continue
            if line is None:
                break
            collected.append(line)
            if on_line is not None:
                on_line(line)
    except BaseException:
        _signal_process(process, force=True)
        process.wait()
        raise
    code = process.wait()
    reader.join(1.0)
    return code, collected


def _parse_protocol_line(line):
    try:
        message = json.loads(_text(line))
    except Exception as error:
        raise FotonError("Invalid JSONL from foton-honeybee: {0}".format(error))
    if message.get("protocol") != PROTOCOL_NAME:
        raise FotonError("The process returned an unknown protocol")
    if int(message.get("protocol_version", -1)) != PROTOCOL_VERSION:
        raise FotonError(
            "Unsupported Foton protocol version: {0}".format(
                message.get("protocol_version")
            )
        )
    return message


def _signal_process(process, force=False):
    """Stop CPython children using CPython or Rhino's .NET subprocess wrapper."""
    if process.poll() is not None:
        return
    method = getattr(process, "kill" if force else "terminate", None)
    if method is not None:
        method()
    else:
        # Rhino 8 IronPython exposes System.Diagnostics.Process directly.
        process.process.Kill()


def capabilities(executable=None, backend="auto", output=None):
    executable = discover_executable(executable)
    env = _subprocess_environment(executable)
    command = [executable, "capabilities", "--backend", str(backend)]
    if output:
        command.extend(["--output", str(output)])
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )
    timed_out = []
    def expire():
        timed_out.append(True)
        _signal_process(process, force=True)
    timer = threading.Timer(30.0, expire)
    timer.start()
    try:
        stdout, stderr = process.communicate()
        # Rhino's IronPython communicate() drains pipes without setting returncode.
        return_code = process.wait()
    finally:
        timer.cancel()
    if timed_out:
        raise FotonError("Foton preflight timed out after 30 seconds")
    if return_code != 0:
        raise FotonError(_text(stderr).strip() or "Foton capability check failed")
    try:
        result = json.loads(_text(stdout))
    except ValueError as error:
        raise FotonError("Invalid capability response: " + str(error))
    if result.get("protocol") != PROTOCOL_NAME:
        raise FotonError("The executable does not provide the Foton Honeybee protocol")
    if int(result.get("protocol_version", -1)) != PROTOCOL_VERSION:
        raise FotonError("The executable uses an unsupported protocol version")
    result["executable"] = executable
    return result


def north_angle(value):
    """Convert a Honeybee numeric/vector north input to degrees from +Y."""
    if value is None:
        return 0.0
    if isinstance(value, (int, float)):
        angle = float(value)
    elif hasattr(value, "X") and hasattr(value, "Y"):
        x_value, y_value = float(value.X), float(value.Y)
        if abs(x_value) + abs(y_value) <= 1.0e-12:
            raise FotonError("The north vector cannot have zero length")
        angle = math.degrees(math.atan2(-x_value, y_value))
    elif hasattr(value, "x") and hasattr(value, "y"):
        x_value, y_value = float(value.x), float(value.y)
        if abs(x_value) + abs(y_value) <= 1.0e-12:
            raise FotonError("The north vector cannot have zero length")
        angle = math.degrees(math.atan2(-x_value, y_value))
    else:
        raise FotonError("north_ must be a number or a 2D/3D vector")
    if angle < -360.0 or angle > 360.0:
        raise FotonError("north_ must be between -360 and 360 degrees")
    return angle


def thresholds(value=None):
    """Parse Honeybee's ``-t/-lt/-ut`` threshold string."""
    result = {"threshold": 300.0, "udi_lower": 100.0, "udi_upper": 3000.0}
    if value is None or value == "":
        return result
    if isinstance(value, string_types):
        tokens = str(value).replace(",", " ").split()
        mapping = {"-t": "threshold", "-lt": "udi_lower", "-ut": "udi_upper"}
        index = 0
        while index < len(tokens):
            key = mapping.get(tokens[index])
            if key is None or index + 1 >= len(tokens):
                raise FotonError("Invalid thresholds_: " + str(value))
            result[key] = float(tokens[index + 1])
            index += 2
    else:
        values = list(value)
        if len(values) != 3:
            raise FotonError("thresholds_ must contain DA, UDI-low, and UDI-high")
        result = dict(zip(("threshold", "udi_lower", "udi_upper"), map(float, values)))
    if not (0 <= result["udi_lower"] <= result["udi_upper"]):
        raise FotonError("UDI thresholds must satisfy 0 <= lower <= upper")
    if result["threshold"] < 0:
        raise FotonError("The DA threshold cannot be negative")
    return result


class _DotNetMailbox(object):
    """A queue whose timed ``get`` wakes as soon as an item arrives.

    IronPython's ``Queue.get(True, timeout)`` polls with sleeps of up to
    50 ms, which a sub-second live run pays on every message. .NET's
    ``BlockingCollection`` waits on a kernel event instead.
    """

    def __init__(self, collection):
        self._collection = collection

    def put(self, item):
        self._collection.Add(item)

    def get(self, block=True, timeout=None):
        milliseconds = -1 if timeout is None else int(timeout * 1000)
        taken, item = self._collection.TryTake(milliseconds if block else 0)
        if not taken:
            raise queue.Empty()
        return item


def _mailbox():
    """A thread-safe queue for reader threads; .NET-backed under IronPython."""
    if sys.platform == "cli":
        try:
            from System import Object
            from System.Collections.Concurrent import BlockingCollection

            return _DotNetMailbox(BlockingCollection[Object]())
        except Exception:
            pass
    return queue.Queue()


def _copy_or_write_model(model, folder):
    destination = os.path.join(folder, "model.hbjson")
    if isinstance(model, string_types):
        source = os.path.abspath(os.path.expanduser(str(model)))
        if not os.path.isfile(source):
            raise FotonError("HBJSON model does not exist: " + source)
        shutil.copy2(source, destination)
        return destination
    if hasattr(model, "to_hbjson"):
        return model.to_hbjson("model.hbjson", folder=folder)
    raise FotonError("_model must be an HBJSON path or a Honeybee Model")


def _copy_or_write_weather(weather, folder):
    if isinstance(weather, string_types):
        source = os.path.abspath(os.path.expanduser(str(weather)))
        if not os.path.isfile(source):
            raise FotonError("EPW/WEA file does not exist: " + source)
        extension = os.path.splitext(source)[1].lower()
        if extension not in (".epw", ".wea"):
            raise FotonError("Weather input must be an EPW or WEA file")
        destination = os.path.join(folder, "weather" + extension)
        shutil.copy2(source, destination)
        return destination
    if hasattr(weather, "write"):
        destination = os.path.join(folder, "weather.wea")
        weather.write(destination)
        return destination
    raise FotonError("_wea must be an EPW/WEA path or a Ladybug Wea")


def _schedule_values(schedule):
    if schedule is None:
        return None
    if isinstance(schedule, string_types):
        return None
    value = getattr(schedule, "values", schedule)
    if callable(value):
        value = value()
    return list(value)


def _copy_or_write_schedule(schedule, folder):
    if schedule is None:
        return None
    destination = os.path.join(folder, "schedule.csv")
    if isinstance(schedule, string_types):
        source = os.path.abspath(os.path.expanduser(str(schedule)))
        if not os.path.isfile(source):
            raise FotonError("Schedule file does not exist: " + source)
        shutil.copy2(source, destination)
        return destination
    values = _schedule_values(schedule)
    if len(values) != 8760:
        raise FotonError("schedule_ must contain exactly 8760 hourly values")
    stream = open(destination, "w")
    try:
        stream.write("\n".join(str(float(value)) for value in values))
        stream.write("\n")
    finally:
        stream.close()
    return destination


def _prepare_inputs(model, wea, schedule, copy_files=True):
    """Stage the inputs in a new temporary folder.

    A live run reads files where they are (``copy_files=False``): the worker
    keys its caches on file contents, so copying a 1.6 MB EPW on every slider
    change only costs time. Objects (a Honeybee Model, a Wea) are still written.
    """
    folder = tempfile.mkdtemp(prefix="foton-gh-inputs-")

    def stage(value, write, kind, extensions):
        if not copy_files and isinstance(value, string_types):
            path = os.path.abspath(os.path.expanduser(str(value)))
            if not os.path.isfile(path):
                raise FotonError(kind + " does not exist: " + path)
            if extensions and os.path.splitext(path)[1].lower() not in extensions:
                raise FotonError("Weather input must be an EPW or WEA file")
            return path
        return write(value, folder)

    try:
        return (
            folder,
            stage(model, _copy_or_write_model, "HBJSON model", None),
            stage(wea, _copy_or_write_weather, "EPW/WEA file", (".epw", ".wea")),
            None if schedule is None else stage(
                schedule, _copy_or_write_schedule, "Schedule file", None
            ),
        )
    except Exception:
        shutil.rmtree(folder, ignore_errors=True)
        raise


def _reserve_output(folder):
    folder = os.path.abspath(os.path.expanduser(folder))
    parent = os.path.dirname(folder)
    if parent and not os.path.isdir(parent):
        os.makedirs(parent)
    for index in range(1000000):
        candidate = folder if index == 0 else "{0}-{1:03d}".format(folder, index)
        try:
            os.mkdir(candidate)
            return candidate
        except OSError:
            if not os.path.isdir(candidate):
                raise
    raise FotonError("Could not reserve an output folder beside " + folder)


def _manifest_path(value):
    path = os.path.abspath(os.path.expanduser(str(value)))
    return os.path.join(path, "run_manifest.json") if os.path.isdir(path) else path


def load_manifest(value):
    path = _manifest_path(value)
    if not os.path.isfile(path):
        raise FotonError("Foton manifest does not exist: " + path)
    stream = open(path, "r")
    try:
        manifest = json.load(stream)
    finally:
        stream.close()
    if manifest.get("protocol") != PROTOCOL_NAME:
        raise FotonError("The file is not a Foton Honeybee manifest")
    if int(manifest.get("protocol_version", -1)) != PROTOCOL_VERSION:
        raise FotonError("The manifest uses an unsupported protocol version")
    if manifest.get("status") != "complete":
        raise FotonError("The Foton run is not complete")
    if not isinstance(manifest.get("grids"), list):
        raise FotonError("The Foton manifest has no SensorGrid results")
    return resolve_manifest(manifest, path)


def _metric_values(path, count):
    values = []
    stream = open(path, "r")
    try:
        for line in stream:
            values.extend(float(item) for item in line.split())
    finally:
        stream.close()
    if len(values) != int(count):
        raise FotonError(
            "Metric file {0} contains {1} values; expected {2}".format(
                path, len(values), count
            )
        )
    if any(math.isnan(value) or math.isinf(value) for value in values):
        raise FotonError("Metric file contains non-finite values: " + path)
    return values


def _coerce_numeric(value):
    """Convert numeric-looking strings to native numbers for GhPython outputs."""
    if isinstance(value, dict):
        return dict((key, _coerce_numeric(item)) for key, item in value.items())
    if isinstance(value, list):
        return [_coerce_numeric(item) for item in value]
    if isinstance(value, tuple):
        return tuple(_coerce_numeric(item) for item in value)
    if isinstance(value, string_types):
        text = str(value).strip()
        if not text:
            return value
        if text.isdigit() or (text.startswith("-") and text[1:].isdigit()):
            try:
                return int(text)
            except Exception:
                return value
        try:
            return float(text)
        except Exception:
            return value
    return value


def list_to_data_tree(branches):
    """Return a Grasshopper DataTree when Ladybug Rhino is available."""
    try:
        from ladybug_rhino.grasshopper import list_to_data_tree as lb_tree

        return lb_tree(branches)
    except ImportError:
        pass
    try:
        from Grasshopper import DataTree
        from Grasshopper.Kernel.Data import GH_Path
        from System import Object

        tree = DataTree[Object]()
        for branch_index, branch in enumerate(branches):
            path = GH_Path(branch_index)
            for value in branch:
                tree.Add(value, path)
        return tree
    except ImportError:
        return branches


def _grid_values(grid, metric):
    """A grid's values for ``metric``: inline in a live reply, else from its file."""
    inline = grid.get("values")
    if inline is not None:
        values = [float(value) for value in inline[metric]]
        if len(values) != int(grid["sensor_count"]):
            raise FotonError("Live result has the wrong number of values")
        return values
    return _metric_values(grid["metrics"][metric], grid["sensor_count"])


def load_result_bundle(value):
    """Load manifest metrics in immutable SensorGrid order."""
    manifest = load_manifest(value) if isinstance(value, string_types) else value
    if manifest.get("recipe") == "daylight_factor":
        return load_daylight_factor_bundle(manifest)
    identifiers, rooms, sda = [], [], []
    metric_branches = dict((metric, []) for metric in METRICS)
    for grid in manifest["grids"]:
        identifiers.append(grid["identifier"])
        rooms.append(grid.get("room_identifier"))
        sda.append(float(grid["sda"]))
        for metric in METRICS:
            metric_branches[metric].append(_grid_values(grid, metric))
    results_folder = manifest.get("results_folder")
    return {
        "manifest": manifest,
        "manifest_path": manifest.get("manifest"),
        "results": [results_folder] if results_folder else [],
        "folder": manifest.get("output_folder"),
        "grid_ids": identifiers,
        "room_ids": rooms,
        "da": list_to_data_tree(metric_branches["da"]),
        "cda": list_to_data_tree(metric_branches["cda"]),
        "udi": list_to_data_tree(metric_branches["udi"]),
        "udi_low": list_to_data_tree(metric_branches["udi_lower"]),
        "udi_up": list_to_data_tree(metric_branches["udi_upper"]),
        "sda": sda,
        "timings": _coerce_numeric(manifest.get("timings", {})),
        "warnings": manifest.get("warnings", []),
    }


def load_daylight_factor_bundle(value):
    """Load daylight factor values in immutable SensorGrid order."""
    manifest = load_manifest(value) if isinstance(value, string_types) else value
    identifiers, rooms, means, branches = [], [], [], []
    for grid in manifest["grids"]:
        identifiers.append(grid["identifier"])
        rooms.append(grid.get("room_identifier"))
        means.append(float(grid["mean_df"]))
        branches.append(_grid_values(grid, "df"))
    results_folder = manifest.get("results_folder")
    return {
        "manifest": manifest,
        "manifest_path": manifest.get("manifest"),
        "results": [results_folder] if results_folder else [],
        "folder": manifest.get("output_folder"),
        "grid_ids": identifiers,
        "room_ids": rooms,
        "df": list_to_data_tree(branches),
        "mean_df": means,
        "timings": _coerce_numeric(manifest.get("timings", {})),
        "warnings": manifest.get("warnings", []),
    }


# Background worker ------------------------------------------------------------
#
# A live run talks to one long-lived ``foton-honeybee serve`` process per
# executable. Grasshopper re-runs a component's whole script on every solve, so
# the process is kept in a module that survives those re-runs.

WORKER_START_TIMEOUT = 120.0


def _worker_registry():
    holder = sys.modules.get("_foton_worker_registry")
    if holder is None:
        import types

        holder = types.ModuleType("_foton_worker_registry")
        holder.workers = {}
        sys.modules["_foton_worker_registry"] = holder
    return holder.workers


def stop_workers():
    """Stop every background worker this Rhino session started."""
    workers = _worker_registry()
    for key in list(workers.keys()):
        _stop_worker(workers.pop(key))


def _stop_worker(worker):
    process = worker["process"]
    try:
        if process.poll() is None:
            _signal_process(process, force=True)
            process.wait()
    except Exception:
        pass


def _start_worker(executable):
    env = _subprocess_environment(executable)
    process = subprocess.Popen(
        [executable, "serve"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )
    worker = {
        "process": process,
        "messages": _mailbox(),
        "errors": [],
        "next_id": 1,
        "ready": False,
    }

    def read_stdout():
        while True:
            line = process.stdout.readline()
            if not line:
                break
            worker["messages"].put(line)
        worker["messages"].put(None)

    def read_stderr():
        while True:
            line = process.stderr.readline()
            if not line:
                break
            worker["errors"].append(_text(line))
            del worker["errors"][:-50]

    for target in (read_stdout, read_stderr):
        thread = threading.Thread(target=target)
        thread.daemon = True
        thread.start()
    return worker


def _worker_error(worker, message):
    detail = "".join(worker["errors"]).strip()
    return FotonError(message + (": " + detail if detail else ""))


def _next_message(worker, cancel, deadline=None):
    while True:
        if cancel is not None and cancel():
            raise FotonCancelled("Foton was cancelled")
        if deadline is not None and time.time() > deadline:
            raise _worker_error(worker, "The Foton worker did not start in time")
        try:
            line = worker["messages"].get(True, 0.1)
        except queue.Empty:
            continue
        if line is None:
            raise _worker_error(worker, "The Foton worker stopped")
        return _parse_protocol_line(line)


def _worker(executable, cancel=None):
    workers = _worker_registry()
    key = os.path.normcase(os.path.abspath(executable))
    worker = workers.get(key)
    if worker is not None and worker["process"].poll() is not None:
        workers.pop(key, None)
        worker = None
    if worker is None:
        worker = _start_worker(executable)
        workers[key] = worker
        try:
            deadline = time.time() + WORKER_START_TIMEOUT
            while not worker["ready"]:
                if _next_message(worker, cancel, deadline).get("event") == "ready":
                    worker["ready"] = True
        except BaseException:
            workers.pop(key, None)
            _stop_worker(worker)
            raise
    return worker


def _write_line(stream, line):
    data = line + "\n"
    try:
        stream.write(data)
    except TypeError:
        # CPython 3 pipes take bytes; IronPython's take text.
        stream.write(data.encode("utf-8"))
    stream.flush()


# Shortest gap between progress updates passed on from a live run.
LIVE_PROGRESS_INTERVAL = 0.25


def worker_request(executable, command, options, progress=None, cancel=None):
    """Send one request to the background worker and return its manifest."""
    executable = discover_executable(executable)
    worker = _worker(executable, cancel)
    workers = _worker_registry()
    key = os.path.normcase(os.path.abspath(executable))
    request_id = str(worker["next_id"])
    worker["next_id"] += 1
    line = json.dumps({"id": request_id, "command": command, "options": options})
    last_progress = None
    try:
        _write_line(worker["process"].stdin, line)
        while True:
            message = _next_message(worker, cancel)
            if message.get("request_id") != request_id:
                continue
            event = message.get("event")
            if event == "complete":
                return message.get("manifest") or {}
            if event == "failed":
                raise FotonError(message.get("message") or "Foton failed")
            # Each progress call redraws Rhino; a live run that ends in a
            # fraction of a second only needs the first one.
            now = time.time()
            if progress is not None and (
                last_progress is None or now - last_progress >= LIVE_PROGRESS_INTERVAL
            ):
                last_progress = now
                progress(message)
    except FotonError as error:
        if not isinstance(error, FotonCancelled) and worker["process"].poll() is None:
            # A failed request leaves a healthy worker ready for the next one.
            raise
        workers.pop(key, None)
        _stop_worker(worker)
        raise
    except BaseException as error:
        # Cancelled mid-trace, or the pipe broke: the worker's state is unknown.
        workers.pop(key, None)
        _stop_worker(worker)
        if isinstance(error, KeyboardInterrupt):
            raise FotonCancelled("Foton was cancelled")
        if isinstance(error, (IOError, OSError, ValueError)):
            raise _worker_error(worker, "Could not reach the Foton worker")
        raise


def _run_process(command, progress=None, cancel=None):
    env = _subprocess_environment(command[0])
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,
        env=env,
    )
    messages = _mailbox()
    errors = []

    def read_stdout():
        while True:
            line = process.stdout.readline()
            if not line:
                break
            messages.put(("message", line))
        messages.put(("done", None))

    def read_stderr():
        while True:
            line = process.stderr.readline()
            if not line:
                break
            errors.append(_text(line))

    stdout_thread = threading.Thread(target=read_stdout)
    stderr_thread = threading.Thread(target=read_stderr)
    stdout_thread.daemon = True
    stderr_thread.daemon = True
    stdout_thread.start()
    stderr_thread.start()
    manifest = None
    stdout_done = False
    try:
        while process.poll() is None or not stdout_done:
            if cancel is not None and cancel():
                raise FotonCancelled("Foton annual daylight was cancelled")
            try:
                kind, line = messages.get(True, 0.1)
            except queue.Empty:
                continue
            if kind == "done":
                stdout_done = True
                continue
            message = _parse_protocol_line(line)
            if progress is not None:
                progress(message)
            if message.get("event") == "complete":
                manifest = message.get("manifest")
    except BaseException as error:
        if process.poll() is None:
            _signal_process(process)
            started = time.time()
            while process.poll() is None and time.time() - started < 2.0:
                time.sleep(0.05)
            if process.poll() is None:
                _signal_process(process, force=True)
        process.wait()
        stdout_thread.join(1.0)
        stderr_thread.join(1.0)
        if isinstance(error, KeyboardInterrupt):
            raise FotonCancelled("Foton annual daylight was cancelled")
        raise
    return_code = process.wait()
    stdout_thread.join(1.0)
    stderr_thread.join(1.0)
    if return_code != 0:
        raise FotonError(
            "Foton exited with code {0}: {1}".format(
                return_code, "".join(errors).strip()
            )
        )
    if manifest is None:
        raise FotonError("Foton completed without returning a result manifest")
    return manifest


def run_annual_daylight(
    model,
    wea,
    output_folder,
    schedule=None,
    north=0.0,
    thresholds_value=None,
    grid_filter="*",
    quality="final",
    sky_density=1,
    backend="auto",
    executable=None,
    reuse=True,
    direct_samples=None,
    maximum_samples=None,
    maximum_bounces=None,
    scene_seed=0,
    progress=None,
    cancel=None,
    live=False,
):
    """Run Foton externally and return a Ladybug/Honeybee-friendly result bundle.

    ``live=True`` sends the run to the background worker, which keeps the
    scene and traced coefficients between runs and writes no files: the
    bundle's ``results`` is empty, so Honeybee's result components need a
    saved (non-live) run.
    """
    executable = discover_executable(executable)
    limits = thresholds(thresholds_value)
    maximum_bounces = DEFAULT_BOUNCES if maximum_bounces is None else int(maximum_bounces)
    temp_folder, model_path, weather_path, schedule_path = _prepare_inputs(
        model, wea, schedule, copy_files=not live
    )
    try:
        if live:
            options = {
                "model": model_path,
                "wea": weather_path,
                "schedule": schedule_path,
                "backend": str(backend or "auto"),
                "grid_filter": str(grid_filter or "*"),
                "north": north_angle(north),
                "quality": str(quality or "final"),
                "sky_density": int(sky_density or 1),
                "threshold": limits["threshold"],
                "udi_lower": limits["udi_lower"],
                "udi_upper": limits["udi_upper"],
                "maximum_bounces": maximum_bounces,
                "scene_seed": int(scene_seed),
                "direct_samples": None if direct_samples is None else int(direct_samples),
                "maximum_samples": None if maximum_samples is None else int(maximum_samples),
            }
            manifest = worker_request(
                executable, "annual-daylight", options, progress=progress, cancel=cancel
            )
            manifest["grasshopper_reused"] = False
            return load_result_bundle(manifest)
        request = request_data(
            model_path,
            weather_path,
            schedule_path,
            backend=backend or "auto",
            grid_filter=grid_filter or "*",
            north=north_angle(north),
            quality=quality or "final",
            sky_density=int(sky_density or 1),
            threshold=limits["threshold"],
            udi_lower=limits["udi_lower"],
            udi_upper=limits["udi_upper"],
            direct_samples=direct_samples,
            maximum_samples=maximum_samples,
            maximum_bounces=maximum_bounces,
            scene_seed=int(scene_seed),
            export_illuminance=True,
        )
        requested_output = os.path.abspath(os.path.expanduser(output_folder))
        identity = None
        existing_manifest = os.path.join(requested_output, "run_manifest.json")
        if reuse and os.path.isfile(existing_manifest):
            current = capabilities(executable, backend or "auto", requested_output)
            identity = reuse_identity(request, current)
            try:
                existing = load_manifest(existing_manifest)
            except (FotonError, ValueError, IOError, TypeError):
                existing = {}
            if reusable(existing, identity):
                existing["grasshopper_reused"] = True
                if progress is not None:
                    progress({"event": "reused", "manifest": existing})
                return load_result_bundle(existing)
        output = _reserve_output(requested_output)
        input_folder = os.path.join(output, "inputs")
        os.mkdir(input_folder)
        final_model = os.path.join(input_folder, "model.hbjson")
        final_weather = os.path.join(
            input_folder, "weather" + os.path.splitext(weather_path)[1].lower()
        )
        shutil.copy2(model_path, final_model)
        shutil.copy2(weather_path, final_weather)
        final_schedule = None
        if schedule_path:
            final_schedule = os.path.join(input_folder, "schedule.csv")
            shutil.copy2(schedule_path, final_schedule)
        command = [
            executable,
            "annual-daylight",
            "--jsonl",
            "--model",
            final_model,
            "--wea",
            final_weather,
            "--output",
            output,
            "--backend",
            str(backend or "auto"),
            "--grid-filter",
            str(grid_filter or "*"),
            "--north",
            str(north_angle(north)),
            "--quality",
            str(quality or "final"),
            "--sky-density",
            str(int(sky_density or 1)),
            "--threshold",
            str(limits["threshold"]),
            "--udi-lower",
            str(limits["udi_lower"]),
            "--udi-upper",
            str(limits["udi_upper"]),
            "--maximum-bounces",
            str(maximum_bounces),
            "--scene-seed",
            str(int(scene_seed)),
            "--export-illuminance",
        ]
        if final_schedule:
            command.extend(["--schedule", final_schedule])
        if direct_samples is not None:
            command.extend(["--direct-samples", str(int(direct_samples))])
        if maximum_samples is not None:
            command.extend(["--maximum-samples", str(int(maximum_samples))])
        manifest = _run_process(command, progress=progress, cancel=cancel)
        manifest["grasshopper_reused"] = False
        return load_result_bundle(manifest)
    finally:
        shutil.rmtree(temp_folder, ignore_errors=True)


def run_daylight_factor(
    model,
    output_folder,
    grid_filter="*",
    quality="final",
    sky_density=1,
    backend="auto",
    executable=None,
    direct_samples=None,
    maximum_samples=None,
    maximum_bounces=None,
    scene_seed=0,
    progress=None,
    cancel=None,
    live=False,
):
    """Run daylight factor (CIE overcast sky) and return a result bundle.

    A saved run writes Honeybee's daylight-factor layout (one ``.res`` file
    per grid) into a new numbered folder; a live run uses the worker and
    writes nothing.
    """
    executable = discover_executable(executable)
    maximum_bounces = DEFAULT_BOUNCES if maximum_bounces is None else int(maximum_bounces)
    folder = tempfile.mkdtemp(prefix="foton-gh-inputs-")
    try:
        model_path = _copy_or_write_model(model, folder)
        settings = {
            "backend": str(backend or "auto"),
            "grid_filter": str(grid_filter or "*"),
            "quality": str(quality or "final"),
            "sky_density": int(sky_density or 1),
            "maximum_bounces": maximum_bounces,
            "scene_seed": int(scene_seed),
            "direct_samples": None if direct_samples is None else int(direct_samples),
            "maximum_samples": None if maximum_samples is None else int(maximum_samples),
        }
        if live:
            options = dict(settings)
            options["model"] = model_path
            manifest = worker_request(
                executable, "daylight-factor", options, progress=progress, cancel=cancel
            )
            return load_daylight_factor_bundle(manifest)
        output = _reserve_output(os.path.abspath(os.path.expanduser(output_folder)))
        input_folder = os.path.join(output, "inputs")
        os.mkdir(input_folder)
        final_model = os.path.join(input_folder, "model.hbjson")
        shutil.copy2(model_path, final_model)
        command = [
            executable,
            "daylight-factor",
            "--jsonl",
            "--model",
            final_model,
            "--output",
            output,
            "--backend",
            settings["backend"],
            "--grid-filter",
            settings["grid_filter"],
            "--quality",
            settings["quality"],
            "--sky-density",
            str(settings["sky_density"]),
            "--maximum-bounces",
            str(maximum_bounces),
            "--scene-seed",
            str(settings["scene_seed"]),
        ]
        if direct_samples is not None:
            command.extend(["--direct-samples", str(int(direct_samples))])
        if maximum_samples is not None:
            command.extend(["--maximum-samples", str(int(maximum_samples))])
        manifest = _run_process(command, progress=progress, cancel=cancel)
        return load_daylight_factor_bundle(manifest)
    finally:
        shutil.rmtree(folder, ignore_errors=True)

