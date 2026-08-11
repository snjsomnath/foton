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
    maximum_bounces=1,
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


def discover_executable(configured=None):
    """Find the external Foton CLI without assuming a Python installation."""
    configured = configured or os.environ.get("FOTON_HONEYBEE_EXE")
    if configured:
        path = os.path.abspath(os.path.expanduser(str(configured)))
        if not os.path.isfile(path):
            raise FotonError("Configured foton-honeybee executable does not exist: " + path)
        return path
    try:
        from distutils.spawn import find_executable

        path = find_executable("foton-honeybee")
    except ImportError:
        path = None
    if path:
        return os.path.abspath(path)
    raise FotonError(
        "foton-honeybee was not found on PATH. Connect its full path to executable_."
    )


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


def capabilities(executable=None, backend="auto"):
    executable = discover_executable(executable)
    env = _subprocess_environment(executable)
    process = subprocess.Popen(
        [executable, "capabilities", "--backend", str(backend)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        raise FotonError(_text(stderr).strip() or "Foton capability check failed")
    result = json.loads(_text(stdout))
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


def _prepare_inputs(model, wea, schedule):
    folder = tempfile.mkdtemp(prefix="foton-gh-inputs-")
    try:
        return (
            folder,
            _copy_or_write_model(model, folder),
            _copy_or_write_weather(wea, folder),
            _copy_or_write_schedule(schedule, folder),
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
    return manifest


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


def load_result_bundle(value):
    """Load manifest metrics in immutable SensorGrid order."""
    manifest = load_manifest(value) if isinstance(value, string_types) else value
    identifiers, rooms, sda = [], [], []
    metric_branches = dict((metric, []) for metric in METRICS)
    for grid in manifest["grids"]:
        identifiers.append(grid["identifier"])
        rooms.append(grid.get("room_identifier"))
        sda.append(float(grid["sda"]))
        for metric in METRICS:
            metric_branches[metric].append(
                _metric_values(grid["metrics"][metric], grid["sensor_count"])
            )
    return {
        "manifest": manifest,
        "manifest_path": manifest.get("manifest"),
        "results": [manifest["results_folder"]],
        "folder": manifest["output_folder"],
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


def _run_process(command, progress=None, cancel=None):
    env = _subprocess_environment(command[0])
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,
        env=env,
    )
    messages = queue.Queue()
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
                process.terminate()
                started = time.time()
                while process.poll() is None and time.time() - started < 2.0:
                    time.sleep(0.05)
                if process.poll() is None:
                    process.kill()
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
    except KeyboardInterrupt:
        process.terminate()
        raise FotonCancelled("Foton annual daylight was cancelled")
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
    maximum_bounces=1,
    scene_seed=0,
    progress=None,
    cancel=None,
):
    """Run Foton externally and return a Ladybug/Honeybee-friendly result bundle."""
    executable = discover_executable(executable)
    limits = thresholds(thresholds_value)
    temp_folder, model_path, weather_path, schedule_path = _prepare_inputs(
        model, wea, schedule
    )
    try:
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
            maximum_bounces=int(maximum_bounces),
            scene_seed=int(scene_seed),
            export_illuminance=True,
        )
        requested_output = os.path.abspath(os.path.expanduser(output_folder))
        existing_manifest = os.path.join(requested_output, "run_manifest.json")
        if reuse and os.path.isfile(existing_manifest):
            existing = load_manifest(existing_manifest)
            if existing.get("request", {}).get("fingerprint") == request["fingerprint"]:
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
            str(int(maximum_bounces)),
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

