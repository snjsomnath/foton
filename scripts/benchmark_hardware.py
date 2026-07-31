#!/usr/bin/env python3
"""Run reproducible Honeybee/Radiance hardware comparisons and save a report."""

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
import subprocess
import sys
import time

from foton import Engine, __version__
from foton.honeybee.radiance import resolve_radiance_executables


ROOT = Path(__file__).resolve().parents[1]
HARDWARE_TABLE_START = "<!-- BENCHMARK_HARDWARE:START -->"
HARDWARE_TABLE_END = "<!-- BENCHMARK_HARDWARE:END -->"
HARDWARE_TABLE_HEADER = (
    "| Run | Date (UTC) | Host | OS | Model | CPU | Cores | RAM | GPU | Backend | Engine |\n"
    "| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | --- | --- |"
)
README_TABLE_START = "<!-- BENCHMARK_RESULTS:START -->"
README_TABLE_END = "<!-- BENCHMARK_RESULTS:END -->"
README_TABLE_HEADER = (
    "| Run | Fixture | Scale | Samples / bounces | Accuracy vs Radiance | "
    "Scene / AS | Trace | Annual | Wall | Radiance |\n"
    "| --- | --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |"
)


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backend", choices=("auto", "metal", "vulkan"), default="auto")
    parser.add_argument("--output", help="Directory for this benchmark run.")
    parser.add_argument("--label", help="Optional stable label included in the report.")
    parser.add_argument("--samples", type=int, default=4096)
    parser.add_argument("--bounces", type=int, default=2)
    parser.add_argument("--workers", type=int)
    parser.add_argument("--radiance-bin")
    parser.add_argument("--glass-transmittance", type=float, default=0.6)
    parser.add_argument("--large-rooms", type=int, default=1000)
    parser.add_argument("--large-sensors-per-room", type=int, default=25)
    parser.add_argument("--large-samples", type=int, default=64)
    parser.add_argument("--large-bounces", type=int, default=1)
    parser.add_argument("--quick", action="store_true", help="Use 256 samples and one bounce.")
    parser.add_argument("--append-readme", action="store_true")
    return parser.parse_args()


def _safe_identifier(value):
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip("-") or "host"


def _default_output():
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return ROOT / "benchmarks" / "results" / f"{timestamp}-{_safe_identifier(socket.gethostname())}"


def _command_log_path(output, name):
    return output / f"{name}.log"


def run_command(name, command, output):
    started = time.perf_counter()
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    elapsed_ms = (time.perf_counter() - started) * 1000.0
    log_path = _command_log_path(output, name)
    log_path.write_text(completed.stdout, encoding="utf-8")
    if completed.returncode:
        output_tail = "\n".join(completed.stdout.strip().splitlines()[-20:])
        raise RuntimeError(
            f"{name} failed with exit code {completed.returncode}; see {log_path}\n\n"
            f"{output_tail}"
        )
    return {
        "name": name,
        "argv": command,
        "elapsed_ms": elapsed_ms,
        "log": log_path.name,
    }


def _load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise RuntimeError(f"expected benchmark output was not created: {path}") from error


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


def _require_radiance(radiance_bin):
    try:
        return resolve_radiance_executables(radiance_bin)
    except FileNotFoundError as error:
        raise RuntimeError(
            "Radiance is required for benchmark comparisons. Install the "
            "`oconv` and `rcontrib` executables, add them to PATH, or pass "
            "--radiance-bin /path/to/radiance/bin (or set RADIANCE_BIN). "
            "On macOS with Homebrew: `brew install radiance`."
        ) from error


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


def _format_percent(value):
    return "n/a" if value is None else f"{value:.3f}%"


def _format_ms(value):
    return "n/a" if value is None else f"{value:.2f} ms"


def _table_value(value):
    return str(value).replace("|", "/").replace("\n", " ")


def hardware_readme_row(report):
    host = report["host"]
    return "| " + " | ".join(
        (
            _table_value(report["run_id"]),
            _table_value(report["recorded_at_utc"]),
            _table_value(host["hostname"]),
            _table_value(
                f"{'macOS' if host['system'] == 'Darwin' else host['system']} "
                f"{host['release']}"
            ),
            _table_value(host["model"]),
            _table_value(host["cpu"]),
            str(host["cpu_count"]),
            _table_value(host["memory"]),
            _table_value(host["gpu"]),
            _table_value(report["engine"]["selected_backend"]),
            _table_value(report["engine"]["version"]),
        )
    ) + " |"


def benchmark_readme_rows(report):
    run_id = report["run_id"]
    direct = report["direct_visibility"]
    direct_metrics = direct["comparison"]
    direct_timings = direct["engine"]["timings_ms"]
    full = report["full_transport"]
    full_metrics = full["comparison"]
    full_timings = full["engine"]["timings_ms"]
    annual = full["annual"]
    annual_metrics = annual["illuminance_comparison"]
    large = report["large_scene"]
    large_timings = large["first_run"]["timings_ms"]

    def row(
        fixture,
        scale,
        samples,
        accuracy,
        timings,
        wall,
        radiance,
        scene_build=None,
    ):
        return "| " + " | ".join(
            (
                _table_value(run_id),
                _table_value(fixture),
                _table_value(scale),
                _table_value(samples),
                _table_value(accuracy),
                _format_ms(
                    scene_build
                    if scene_build is not None
                    else timings.get("acceleration_structure_ms")
                ),
                _format_ms(timings.get("tracing_ms")),
                _format_ms(timings.get("annual_reduction_ms")),
                _format_ms(wall),
                _format_ms(radiance),
            )
        ) + " |"

    return [
        row(
            "Honeybee direct visibility",
            f"{direct['metadata']['sensor_count']} sensors × {direct['metadata']['sky_patch_count']} patches",
            "0 / 0",
            f"{direct_metrics['mismatch_count']} mismatches; "
            f"{100.0 * direct_metrics['weighted_visible_energy_relative_error']:.3f}% energy",
            direct_timings,
            direct["engine"].get("wall_clock_ms"),
            direct["radiance"].get("elapsed_ms"),
        ),
        row(
            "Diffuse + thin glass coefficients",
            f"{full_metrics['shape'][0]} sensors × {full_metrics['shape'][1]} patches",
            f"{full['samples']} / {full['bounces']}",
            f"NMBE {_format_percent(full_metrics['nmbe_percent'])}; "
            f"CV(RMSE) {_format_percent(full_metrics['cvrmse_percent'])}",
            full_timings,
            full["engine"].get("wall_clock_ms"),
            full["radiance"].get("elapsed_ms"),
        ),
        row(
            "Annual illuminance + DA/sDA",
            f"{full_metrics['shape'][0]} sensors × {annual['timestep_count']} hours",
            f"{full['samples']} / {full['bounces']}",
            f"NMBE {_format_percent(annual_metrics['nmbe_percent'])}; "
            f"CV(RMSE) {_format_percent(annual_metrics['cvrmse_percent'])}; "
            f"sDA Δ {annual['metric_differences']['static_sda_300_50_percentage_points']:.2f} pp",
            full_timings,
            full["engine"].get("wall_clock_ms"),
            annual.get("radiance_total_ms"),
        ),
        row(
            "1,000-room resident scene",
            f"{large['rooms']} rooms / {large['sensor_count']} sensors",
            f"{large['samples']} / {large['bounces']}",
            "performance fixture",
            large_timings,
            large["first_run"].get("wall_clock_ms"),
            large.get("radiance", {}).get("cold_wall_clock_ms"),
            scene_build=large.get("scene_commit_ms"),
        ),
        row(
            "1,000-room resident scene (cached)",
            f"{large['rooms']} rooms / {large['sensor_count']} sensors",
            f"{large['samples']} / {large['bounces']}",
            "resident BLAS/TLAS reuse",
            large["resident_scene_reuse"]["timings_ms"],
            large["resident_scene_reuse"].get("wall_clock_ms"),
            large.get("radiance", {}).get("cached_wall_clock_ms"),
        ),
    ]


def append_table_rows(readme_path, start_marker, end_marker, rows):
    content = readme_path.read_text(encoding="utf-8")
    start = content.find(start_marker)
    end = content.find(end_marker)
    if start < 0 or end < 0 or end <= start:
        raise RuntimeError(
            f"{readme_path} does not contain the benchmark table markers"
        )
    prefix = content[:end].rstrip()
    suffix = content[end:]
    existing = set(prefix.splitlines())
    additions = [row for row in rows if row not in existing]
    if not additions:
        return 0
    addition_text = "\n".join(additions)
    readme_path.write_text(
        f"{prefix}\n{addition_text}\n{suffix}", encoding="utf-8"
    )
    return len(additions)


def append_readme_row(readme_path, row):
    return bool(
        append_table_rows(
            readme_path,
            README_TABLE_START,
            README_TABLE_END,
            [row],
        )
    )


def report_markdown(report):
    direct = report["direct_visibility"]
    full = report["full_transport"]
    metrics = full["comparison"]
    return "\n".join(
        (
            "# Hardware Benchmark",
            "",
            f"- Recorded: `{report['recorded_at_utc']}`",
            f"- Host: `{report['host']['hostname']}`",
            f"- CPU: `{report['host']['cpu']}`",
            f"- GPU: `{report['host']['gpu']}`",
            f"- Selected backend: `{report['engine']['selected_backend']}`",
            f"- Large scene: `{report['large_scene']['rooms']} rooms / "
            f"{report['large_scene']['sensor_count']} sensors`",
            f"- Direct mismatched rays: `{direct['comparison']['mismatch_count']}`",
            "- Direct weighted visible-energy error: "
            f"`{direct['comparison']['weighted_visible_energy_relative_error']:.4%}`",
            f"- Full transport NMBE: `{metrics['nmbe_percent']:.4f}%`",
            f"- Full transport CV(RMSE): `{metrics['cvrmse_percent']:.4f}%`",
            "- Engine tracing: "
            f"`{full['engine']['timings_ms']['tracing_ms']:.4f} ms`",
            f"- Radiance rcontrib: `{full['radiance']['elapsed_ms']:.4f} ms`",
            "",
            "## README hardware row",
            "",
            hardware_readme_row(report),
            "",
            "## README benchmark rows",
            "",
            *benchmark_readme_rows(report),
            "",
        )
    )


def main():
    args = parse_args()
    if args.quick:
        args.samples = 256
        args.bounces = 1
        args.large_samples = 8
    if args.samples <= 0 or args.bounces <= 0:
        raise ValueError("samples and bounces must be positive")
    if not 0 <= args.glass_transmittance <= 1:
        raise ValueError("glass transmittance must be within [0, 1]")

    _require_python_dependencies()
    output = Path(args.output).expanduser().resolve() if args.output else _default_output()
    engine = _hardware_record(args.backend)
    _require_radiance(args.radiance_bin)
    output.mkdir(parents=True, exist_ok=False)

    direct_output = output / "direct"
    full_output = output / "full"
    large_output = output / "large_scene.json"
    direct_command = [
        sys.executable,
        "scripts/compare_honeybee_shoebox.py",
        "--backend",
        "compare",
        "--engine-backend",
        args.backend,
        "--output",
        str(direct_output),
        "--basis",
        "tregenza",
        "--auto-grid",
    ]
    full_command = [
        sys.executable,
        "scripts/compare_full_transport_shoebox.py",
        "--backend",
        args.backend,
        "--output",
        str(full_output),
        "--samples",
        str(args.samples),
        "--bounces",
        str(args.bounces),
        "--glass-transmittance",
        str(args.glass_transmittance),
        "--annual",
    ]
    large_command = [
        sys.executable,
        "scripts/benchmark_large_scene.py",
        "--backend",
        args.backend,
        "--output",
        str(large_output),
        "--rooms",
        str(args.large_rooms),
        "--sensors-per-room",
        str(args.large_sensors_per_room),
        "--samples",
        str(args.large_samples),
        "--bounces",
        str(args.large_bounces),
        "--glass-transmittance",
        str(args.glass_transmittance),
    ]
    if args.workers:
        large_command.extend(("--workers", str(args.workers)))
    if args.radiance_bin:
        large_command.extend(("--radiance-bin", args.radiance_bin))
    if args.workers:
        direct_command.extend(("--workers", str(args.workers)))
        full_command.extend(("--workers", str(args.workers)))
    if args.radiance_bin:
        direct_command.extend(("--radiance-bin", args.radiance_bin))
        full_command.extend(("--radiance-bin", args.radiance_bin))
    commands = [
        run_command("direct_visibility", direct_command, output),
        run_command("full_transport", full_command, output),
        run_command("large_scene", large_command, output),
    ]

    direct_results = direct_output / "ShadedShoebox-direct-visibility" / "results"
    direct_metadata = _load_json(direct_results / "metadata.json")
    report = {
        "schema_version": 2,
        "run_id": output.name,
        "recorded_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ"),
        "label": args.label,
        "host": _host_record(engine),
        "engine": {"version": __version__, **engine},
        "workload": {
            "fixtures": [
                "Honeybee shaded shoebox direct visibility v1",
                "Honeybee diffuse/glass transport v1",
                "deterministic annual stress sky v1",
                "canonical instanced 1,000-room scene v1",
            ],
            "direct_basis": "tregenza",
            "samples": args.samples,
            "diffuse_bounces": args.bounces,
            "glass_transmittance": args.glass_transmittance,
        },
        "direct_visibility": {
            "comparison": _load_json(direct_results / "comparison.json"),
            "engine": direct_metadata["gpu"],
            "radiance": direct_metadata["radiance"],
            "metadata": direct_metadata,
        },
        "full_transport": _load_json(full_output / "comparison.json"),
        "large_scene": _load_json(large_output),
        "commands": commands,
    }
    benchmark_json = output / "benchmark.json"
    benchmark_json.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    benchmark_md = output / "benchmark.md"
    benchmark_md.write_text(report_markdown(report), encoding="utf-8")
    hardware_row = hardware_readme_row(report)
    benchmark_rows = benchmark_readme_rows(report)
    if args.append_readme:
        hardware_count = append_table_rows(
            ROOT / "README.md",
            HARDWARE_TABLE_START,
            HARDWARE_TABLE_END,
            [hardware_row],
        )
        result_count = append_table_rows(
            ROOT / "README.md",
            README_TABLE_START,
            README_TABLE_END,
            benchmark_rows,
        )
        print(
            f"Appended {hardware_count} hardware row and {result_count} benchmark rows."
        )
    print(benchmark_md)
    print(hardware_row)
    print("\n".join(benchmark_rows))


if __name__ == "__main__":
    main()
