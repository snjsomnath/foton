#!/usr/bin/env python3
"""Time cold annual daylight runs at Foton's shipped defaults and save a report.

Each case is a Honeybee model run through ``HoneybeeStudy.annual_daylight`` with
the default ``final`` quality preset, MF:1 sky and default bounce depth, from
model loading to the written DA/UDI results. Every repeat builds a new study
(scene preparation, acceleration structures, GPU upload and tracing), so the
numbers are what a user waits for on a model Foton has not seen before. One
unrecorded warm-up run compiles GPU pipelines and fills the weather cache.

    python scripts/benchmark_hardware.py --backend auto
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import importlib.util
import json
import os
from pathlib import Path
import platform
import re
import socket
import statistics
import subprocess
import sys
import tempfile
import time

from foton import Engine, __version__


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "test_models" / "architectural"
DEFAULT_SCENES = ("teaching_office", "courtyard_rooms", "acceptance", "office_floors")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backend", choices=("auto", "metal", "vulkan"), default="auto")
    parser.add_argument("--output", help="Directory for this benchmark run.")
    parser.add_argument("--label", help="Optional stable label included in the report.")
    parser.add_argument(
        "--scenes",
        nargs="+",
        default=list(DEFAULT_SCENES),
        help="Corpus scene names under test_models/architectural, or office_floors.",
    )
    parser.add_argument("--repeats", type=int, default=5)
    parser.add_argument("--weather", default=str(ROOT / "epw" / "gothenburg.epw"))
    parser.add_argument("--floors", type=int, default=4, help="office_floors storeys.")
    parser.add_argument(
        "--rooms-per-facade", type=int, default=32, help="office_floors rooms per facade per storey."
    )
    parser.add_argument("--quick", action="store_true", help="Use the preview preset and one repeat.")
    return parser.parse_args(argv)


def _safe_identifier(value):
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip("-") or "host"


def _default_output():
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return ROOT / "benchmarks" / "results" / f"{timestamp}-{_safe_identifier(socket.gethostname())}"


def _hardware_record(requested_backend):
    engine = Engine({"backend": requested_backend})
    capabilities = engine.capabilities()
    name = capabilities["name"].lower()
    selected_backend = (
        "metal" if name.startswith("metal") else "vulkan" if name.startswith("vulkan") else "reference"
    )
    if selected_backend == "reference" or not capabilities["hardware_acceleration"]:
        raise RuntimeError(
            "no compatible hardware backend is available; use `daylight-cli hardware` "
            "to inspect Metal/Vulkan requirements"
        )
    return {
        "requested_backend": requested_backend,
        "selected_backend": selected_backend,
        "capabilities": capabilities,
    }


def _command_text(command):
    completed = subprocess.run(
        command,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return completed.stdout.strip() if completed.returncode == 0 else ""


def _memory_gib():
    try:
        byte_count = os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES")
    except (AttributeError, OSError, ValueError):
        return None
    return byte_count / (1024**3)


def _host_record(engine):
    profiler = {}
    if platform.system() == "Darwin":
        for line in _command_text(
            ["system_profiler", "SPHardwareDataType"]
        ).splitlines():
            key, separator, value = line.strip().partition(":")
            if separator and key in {
                "Model Name",
                "Model Identifier",
                "Chip",
                "Total Number of Cores",
                "Memory",
            }:
                profiler[key] = value.strip()
    cpu = profiler.get("Chip") or platform.processor() or platform.machine()
    if cpu == platform.machine() and Path("/proc/cpuinfo").is_file():
        for line in Path("/proc/cpuinfo").read_text(encoding="utf-8").splitlines():
            if line.lower().startswith("model name"):
                cpu = line.partition(":")[2].strip()
                break
    capabilities = engine["capabilities"]
    capability_name = capabilities["name"]
    gpu = capability_name.split(" device:", 1)[-1].split(" (", 1)[0].strip()
    memory = profiler.get("Memory")
    if not memory:
        memory_gib = _memory_gib()
        memory = f"{memory_gib:.1f} GiB" if memory_gib is not None else "unknown"
    os_version = platform.mac_ver()[0] if platform.system() == "Darwin" else platform.release()
    return {
        "hostname": socket.gethostname(),
        "system": platform.system(),
        "release": os_version,
        "machine": platform.machine(),
        "model": profiler.get("Model Name", platform.machine()),
        "model_identifier": profiler.get("Model Identifier"),
        "cpu": cpu,
        "cpu_count": os.cpu_count(),
        "cpu_core_description": profiler.get("Total Number of Cores"),
        "memory": memory,
        "gpu": gpu,
        "python": sys.version.split()[0],
    }


def _require_python_dependencies():
    missing = [
        package
        for package in ("honeybee", "honeybee_radiance")
        if importlib.util.find_spec(package) is None
    ]
    if not missing:
        return
    install_command = f"{sys.executable} -m pip install -e '{ROOT}[honeybee]'"
    raise RuntimeError(
        f"Python interpreter {sys.executable} is missing "
        f"{', '.join(missing)}. Install the benchmark dependencies with:\n"
        f"  {install_command}\n"
        f"Or run this script with the repository virtualenv:\n"
        f"  {ROOT / '.venv/bin/python'} scripts/benchmark_hardware.py ..."
    )


def office_floors_model(floors=4, rooms_per_facade=32, room_size=6.0, height=3.0):
    """Build a double-loaded office block: every room has one glazed facade.

    Two rows of ``room_size`` square rooms face south and north across a shared
    spine wall, with 40 % glazing on the exterior wall and a 1 m sensor grid at
    0.75 m. The defaults give 256 rooms and 9,216 sensors.
    """
    from honeybee.model import Model
    from honeybee.room import Room
    from ladybug_geometry.geometry3d import Vector3D

    rooms, grids = [], []
    for floor in range(floors):
        for row, facade in ((0, Vector3D(0, -1, 0)), (1, Vector3D(0, 1, 0))):
            for column in range(rooms_per_facade):
                room = Room.from_box(
                    f"office_{floor}_{row}_{column}",
                    room_size,
                    room_size,
                    height,
                    origin=_point(column * room_size, row * room_size, floor * height),
                )
                for face in room.faces:
                    if face.normal.is_equivalent(facade, 1e-6):
                        face.apertures_by_ratio(0.4, 0.01)
                grids.append(room.properties.radiance.generate_sensor_grid(1.0, offset=0.75))
                rooms.append(room)
    Room.solve_adjacency(rooms, 0.01)
    model = Model("office_floors", rooms=rooms, tolerance=0.01, angle_tolerance=1.0)
    model.properties.radiance.add_sensor_grids(grids)
    return model


def _point(x, y, z):
    from ladybug_geometry.geometry3d import Point3D

    return Point3D(x, y, z)


def _model_path(identifier, args, work):
    if identifier == "office_floors":
        model = office_floors_model(args.floors, args.rooms_per_facade)
        return Path(model.to_hbjson("office_floors", str(work)))
    path = CORPUS / f"{identifier}.hbjson"
    if not path.is_file():
        raise FileNotFoundError(f"unknown corpus scene {identifier!r}: {path} does not exist")
    return path


def _run_once(model_path, args, quality, weather_cache, output):
    from foton.honeybee import HoneybeeStudy

    started = time.perf_counter()
    study = HoneybeeStudy(str(model_path), backend=args.backend, weather_cache=weather_cache)
    annual = study.annual_daylight(args.weather, quality=quality, output_folder=output)
    wall = time.perf_counter() - started
    return study, annual, wall


def _summary(values):
    return {
        "median": statistics.median(values),
        "minimum": min(values),
        "maximum": max(values),
        "values": values,
    }


def benchmark_scene(identifier, args, quality, weather_cache, work):
    model_path = _model_path(identifier, args, work)
    walls, tracing, preparation = [], [], []
    study = None
    for repeat in range(args.repeats):
        study, annual, wall = _run_once(
            model_path, args, quality, weather_cache, work / identifier / f"run{repeat}"
        )
        walls.append(wall)
        tracing.append(annual.timings["engine_tracing_seconds"])
        preparation.append(annual.timings["study_preparation_seconds"])
        print(f"{identifier} run {repeat + 1}/{args.repeats}: {wall:.3f} s", flush=True)
    prepared = study.prepared
    return {
        "scene": identifier,
        "model": str(model_path.relative_to(ROOT)) if model_path.is_relative_to(ROOT) else model_path.name,
        "rooms": len(prepared.model.rooms),
        "sensors": int(len(prepared.arrays["sensor_positions"])),
        "wall_seconds": _summary(walls),
        "tracing_seconds": _summary(tracing),
        "preparation_seconds": _summary(preparation),
        "last_timings": annual.timings,
    }


def report_markdown(report):
    host = report["host"]
    lines = [
        "# Hardware Benchmark",
        "",
        f"- Recorded: `{report['recorded_at_utc']}`",
        f"- Machine: {host['model']}, {host['cpu']}, {host['memory']}",
        f"- GPU / backend: {host['gpu']} / `{report['engine']['selected_backend']}`",
        f"- Foton: `{report['engine']['version']}`",
        f"- Settings: `{json.dumps(report['settings'], sort_keys=True)}`",
        f"- Weather: `{report['weather']}`",
        f"- Repeats per scene: {report['repeats']} (median shown)",
        "",
        "| Scene | Rooms | Sensors | Cold annual run | GPU tracing |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for case in report["cases"]:
        lines.append(
            f"| {case['scene']} | {case['rooms']} | {case['sensors']} | "
            f"{case['wall_seconds']['median']:.2f} s | "
            f"{case['tracing_seconds']['median']:.2f} s |"
        )
    return "\n".join(lines) + "\n"


def run_suite(args):
    """Run every scene in ``args`` and return the report without writing it."""
    if args.quick:
        args.repeats = 1
    if args.repeats <= 0:
        raise ValueError("repeats must be positive")
    _require_python_dependencies()
    from foton.honeybee.annual import DEFAULT_MAXIMUM_BOUNCES, quality_preset

    quality = "preview" if args.quick else "final"
    engine = _hardware_record(args.backend)
    with tempfile.TemporaryDirectory() as folder:
        work = Path(folder)
        weather_cache = work / "weather_cache"
        _run_once(CORPUS / "teaching_office.hbjson", args, quality, weather_cache, work / "warmup")
        cases = [benchmark_scene(name, args, quality, weather_cache, work) for name in args.scenes]
    return {
        "schema_version": 2,
        "label": args.label,
        "recorded_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ"),
        "host": _host_record(engine),
        "engine": {**engine, "version": __version__},
        "quality": quality,
        "settings": {
            **quality_preset(quality, 1),
            "maximum_bounces": DEFAULT_MAXIMUM_BOUNCES,
            "sky_density": 1,
        },
        "weather": Path(args.weather).name,
        "repeats": args.repeats,
        "cases": cases,
    }


def main():
    args = parse_args()
    output = Path(args.output).resolve() if args.output else _default_output()
    output.mkdir(parents=True, exist_ok=True)
    report = {"run_id": output.name, **run_suite(args)}
    (output / "benchmark.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    markdown = report_markdown(report)
    (output / "benchmark.md").write_text(markdown, encoding="utf-8")
    print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
