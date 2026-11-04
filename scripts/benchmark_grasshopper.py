#!/usr/bin/env python3
"""Time the Grasshopper round trip stage by stage, outside Rhino.

Runs ``grasshopper_foton.foton_gh.run_annual_daylight`` exactly as the Foton
Annual Daylight component does: serialise the Honeybee Model to HBJSON, stage
inputs, spawn ``foton-honeybee annual-daylight --jsonl``, stream its progress
events and load the metric files back into per-grid lists. The JSONL events are
timestamped as they arrive, so the subprocess time splits into Python start-up,
scene build, sky, tracing, metric reduction and result writing. Finally the
results folder is read with Honeybee's ``AnnualDaylight`` loader, the path the
Honeybee/Ladybug result components take.

Rhino itself is not involved: HBJSON serialisation and metric loading run in
CPython here and in IronPython inside Grasshopper, and the DataTree conversion
falls back to plain lists.

    python scripts/benchmark_grasshopper.py --repeats 3
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import shutil
import statistics
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from benchmark_hardware import (  # noqa: E402
    CORPUS,
    _hardware_record,
    _host_record,
    _require_python_dependencies,
    office_floors_model,
)
from foton import __version__  # noqa: E402
from grasshopper_foton import foton_gh  # noqa: E402

DEFAULT_SCENES = ("teaching_office", "acceptance", "office_floors")
STAGES = (
    ("hbjson_export", "HBJSON export"),
    ("input_staging", "Input staging and hashing"),
    ("process_startup", "Process start-up and imports"),
    ("scene_build", "Scene build and GPU upload"),
    ("sky", "Annual sky matrix"),
    ("tracing", "GPU tracing"),
    ("metrics", "Metric reduction"),
    ("result_writing", "Result writing"),
    ("process_exit", "Process exit"),
    ("metric_loading", "Metric loading in the component"),
)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backend", choices=("auto", "metal", "vulkan"), default="auto")
    parser.add_argument("--output", help="Directory for the report.")
    parser.add_argument("--scenes", nargs="+", default=list(DEFAULT_SCENES))
    parser.add_argument("--repeats", type=int, default=3)
    parser.add_argument("--weather", default=str(ROOT / "epw" / "gothenburg.epw"))
    parser.add_argument(
        "--executable",
        default=str(Path(sys.executable).with_name("foton-honeybee")),
        help="foton-honeybee executable (default: the one next to this Python).",
    )
    return parser.parse_args(argv)


def _model(identifier):
    from honeybee.model import Model

    if identifier == "office_floors":
        return office_floors_model()
    return Model.from_hbjson(str(CORPUS / f"{identifier}.hbjson"))


def _event_time(events, predicate):
    for stamp, message in events:
        if predicate(message):
            return stamp
    raise RuntimeError("expected progress event was not reported")


def _stage(name):
    return lambda message: message.get("stage") == name


def round_trip(model, args, folder):
    """Run one cold component round trip and return stage durations in seconds."""
    marks, events = {}, []
    copy_model = foton_gh._copy_or_write_model
    popen = foton_gh.subprocess.Popen
    load_bundle = foton_gh.load_result_bundle

    def timed_copy(value, destination):
        started = time.perf_counter()
        path = copy_model(value, destination)
        marks["export"] = time.perf_counter() - started
        return path

    def timed_popen(*popen_args, **popen_kwargs):
        marks["spawn"] = time.perf_counter()
        return popen(*popen_args, **popen_kwargs)

    def timed_load(value):
        marks["load_started"] = time.perf_counter()
        bundle = load_bundle(value)
        marks["load_finished"] = time.perf_counter()
        return bundle

    def progress(message):
        stamp = time.perf_counter()
        if message.get("event") == "complete":
            marks["complete"] = stamp
        events.append((stamp, message))

    foton_gh._copy_or_write_model = timed_copy
    foton_gh.subprocess.Popen = timed_popen
    foton_gh.load_result_bundle = timed_load
    try:
        started = time.perf_counter()
        bundle = foton_gh.run_annual_daylight(
            model,
            args.weather,
            str(folder),
            backend=args.backend,
            executable=args.executable,
            reuse=False,
            progress=progress,
        )
        finished = time.perf_counter()
    finally:
        foton_gh._copy_or_write_model = copy_model
        foton_gh.subprocess.Popen = popen
        foton_gh.load_result_bundle = load_bundle

    first = events[0][0]
    weather = _event_time(events, _stage("weather"))
    # The first event after the sky stages marks the start of tracing.
    tracing = _event_time(
        [event for event in events if event[0] > weather],
        lambda message: message.get("stage") not in ("weather", "schedule"),
    )
    metrics = _event_time(events, _stage("metrics"))
    output = _event_time(events, _stage("output"))
    stages = {
        "hbjson_export": marks["export"],
        "input_staging": marks["spawn"] - started - marks["export"],
        "process_startup": first - marks["spawn"],
        "scene_build": weather - first,
        "sky": tracing - weather,
        "tracing": metrics - tracing,
        "metrics": output - metrics,
        "result_writing": marks["complete"] - output,
        "process_exit": marks["load_started"] - marks["complete"],
        "metric_loading": marks["load_finished"] - marks["load_started"],
    }
    stages["component_total"] = finished - started
    manifest = bundle["manifest"]
    return stages, manifest, bundle


def honeybee_loader_seconds(results_folder):
    """Load hourly illuminance and recompute DA with Honeybee's result API."""
    from honeybee_radiance_postprocess.results import AnnualDaylight

    started = time.perf_counter()
    AnnualDaylight(results_folder).daylight_autonomy()
    return time.perf_counter() - started


def _folder_bytes(folder):
    return sum(path.stat().st_size for path in Path(folder).rglob("*") if path.is_file())


def benchmark_scene(identifier, args, work):
    model = _model(identifier)
    runs = []
    for repeat in range(args.repeats):
        folder = work / identifier / f"run{repeat}"
        stages, manifest, bundle = round_trip(model, args, folder)
        stages["honeybee_loader"] = honeybee_loader_seconds(manifest["results_folder"])
        stages["round_trip_total"] = stages["component_total"] + stages["honeybee_loader"]
        runs.append(
            {
                "stages": stages,
                "output_bytes": _folder_bytes(manifest["output_folder"]),
                "inner_timings": manifest.get("timings", {}),
            }
        )
        print(
            f"{identifier} run {repeat + 1}/{args.repeats}: "
            f"component {stages['component_total']:.2f} s, "
            f"round trip {stages['round_trip_total']:.2f} s",
            flush=True,
        )
        shutil.rmtree(manifest["output_folder"], ignore_errors=True)
    keys = runs[0]["stages"].keys()
    median = {key: statistics.median(run["stages"][key] for run in runs) for key in keys}
    return {
        "scene": identifier,
        "rooms": len(model.rooms),
        "sensors": sum(len(grid.sensors) for grid in model.properties.radiance.sensor_grids),
        "output_megabytes": statistics.median(run["output_bytes"] for run in runs) / 1e6,
        "median_seconds": median,
        "runs": runs,
    }


def report_markdown(report):
    host = report["host"]
    cases = report["cases"]
    lines = [
        "# Grasshopper Round-Trip Benchmark",
        "",
        f"- Recorded: `{report['recorded_at_utc']}`",
        f"- Machine: {host['model']}, {host['cpu']}, {host['memory']}",
        f"- GPU / backend: {host['gpu']} / `{report['engine']['selected_backend']}`",
        f"- Foton: `{report['engine']['version']}`, `final` preset, 8 bounces, MF:1",
        f"- Weather: `{report['weather']}`",
        f"- Repeats per scene: {report['repeats']} (median shown, seconds)",
        "- Path: `foton_gh.run_annual_daylight` in CPython; Rhino not running",
        "",
        "| Stage | " + " | ".join(f"{c['scene']} ({c['sensors']} sensors)" for c in cases) + " |",
        "| --- | " + " | ".join("---:" for _ in cases) + " |",
    ]
    rows = list(STAGES) + [
        ("component_total", "**Component total**"),
        ("honeybee_loader", "Honeybee AnnualDaylight load + DA"),
        ("round_trip_total", "**Round trip total**"),
    ]
    for key, label in rows:
        lines.append(
            f"| {label} | " + " | ".join(f"{c['median_seconds'][key]:.3f}" for c in cases) + " |"
        )
    lines.append(
        "| Output folder size (MB) | "
        + " | ".join(f"{c['output_megabytes']:.1f}" for c in cases)
        + " |"
    )
    return "\n".join(lines) + "\n"


def run_suite(args):
    """Run every scene in ``args`` and return the report without writing it."""
    _require_python_dependencies()
    engine = _hardware_record(args.backend)
    timestamp = datetime.now(timezone.utc)
    with tempfile.TemporaryDirectory() as folder:
        work = Path(folder)
        # Warm-up: fills the per-user weather cache and compiles GPU pipelines.
        round_trip(_model("teaching_office"), args, work / "warmup")
        cases = [benchmark_scene(name, args, work) for name in args.scenes]
    return {
        "schema_version": 1,
        "recorded_at_utc": timestamp.strftime("%Y-%m-%d %H:%M:%SZ"),
        "host": _host_record(engine),
        "engine": {**engine, "version": __version__},
        "executable": Path(args.executable).name,
        "weather": Path(args.weather).name,
        "repeats": args.repeats,
        "cases": cases,
    }


def main():
    args = parse_args()
    output = (
        Path(args.output).resolve()
        if args.output
        else ROOT
        / "benchmarks"
        / "results"
        / f"{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}-grasshopper"
    )
    output.mkdir(parents=True, exist_ok=True)
    report = run_suite(args)
    (output / "benchmark.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    markdown = report_markdown(report)
    (output / "benchmark.md").write_text(markdown, encoding="utf-8")
    print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
