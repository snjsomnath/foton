#!/usr/bin/env python3
"""Time annual runs and fingerprint their outputs, to compare two Foton builds.

Run it once with each build installed, then compare the two output folders:

    python scripts/benchmark_vulkan_identity.py run --output /content/profile-old
    python scripts/benchmark_vulkan_identity.py run --output /content/profile-new
    python scripts/benchmark_vulkan_identity.py compare /content/profile-old /content/profile-new

Each scene runs as a plain annual study and again with hourly illuminance
exported, the way the Grasshopper component asks for it. The output files of
the last repeat are hashed, so ``compare`` shows whether two builds wrote
byte-identical results, and how long each stage took.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import statistics
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

STAGES = (
    "engine_tracing_seconds",
    "engine_annual_reduction_seconds",
    "metric_reduction_seconds",
    "raw_export_seconds",
    "study_preparation_seconds",
)


def _hashes(folder):
    hashes = {}
    for path in sorted(Path(folder).rglob("*")):
        if path.is_file():
            hashes[str(path.relative_to(folder))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return hashes


def run(args):
    from benchmark_hardware import _model_path
    from foton import Engine, __version__
    from foton.honeybee import HoneybeeStudy

    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    capabilities = dict(Engine({"backend": args.backend}).capabilities())
    report = {"version": __version__, "capabilities": capabilities, "cases": []}
    with tempfile.TemporaryDirectory() as folder:
        work = Path(folder)
        weather_cache = work / "weather_cache"
        options = argparse.Namespace(floors=4, rooms_per_facade=32)
        for scene in args.scenes:
            model = _model_path(scene, options, work)
            for hourly in (False, True):
                walls, stages = [], {stage: [] for stage in STAGES}
                for repeat in range(args.repeats + 1):
                    result_folder = output / "results" / f"{scene}-{'hourly' if hourly else 'annual'}"
                    started = time.perf_counter()
                    study = HoneybeeStudy(str(model), backend=args.backend, weather_cache=weather_cache)
                    annual = study.annual_daylight(
                        args.weather,
                        quality=args.quality,
                        output_folder=result_folder,
                        export_illuminance=hourly,
                    )
                    wall = time.perf_counter() - started
                    if repeat == 0:
                        continue  # warm-up: pipelines and the weather cache
                    walls.append(wall)
                    for stage in STAGES:
                        stages[stage].append(float(annual.timings.get(stage) or 0.0))
                case = {
                    "scene": scene,
                    "hourly": hourly,
                    "wall_seconds": statistics.median(walls),
                    **{stage: statistics.median(values) for stage, values in stages.items()},
                    "hashes": _hashes(result_folder),
                }
                report["cases"].append(case)
                print(
                    f"{scene:16s} {'hourly' if hourly else 'annual':6s} "
                    f"wall {case['wall_seconds']:7.3f} s  "
                    f"tracing {case['engine_tracing_seconds']:7.3f} s  "
                    f"reduce {case['engine_annual_reduction_seconds']:6.3f} s  "
                    f"metrics {case['metric_reduction_seconds']:7.3f} s",
                    flush=True,
                )
    (output / "profile.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


def compare(args):
    old = json.loads((Path(args.old) / "profile.json").read_text(encoding="utf-8"))
    new = json.loads((Path(args.new) / "profile.json").read_text(encoding="utf-8"))
    print(f"old {old['version']} {old['capabilities'].get('name')}")
    print(f"new {new['version']} {new['capabilities'].get('name')}")
    identical = True
    for before, after in zip(old["cases"], new["cases"]):
        label = f"{before['scene']} {'hourly' if before['hourly'] else 'annual'}"
        differing = sorted(
            name
            for name in set(before["hashes"]) | set(after["hashes"])
            if before["hashes"].get(name) != after["hashes"].get(name)
        )
        identical &= not differing
        print(f"\n{label}: {len(before['hashes'])} files, {len(differing)} differ")
        for name in differing[:10]:
            print(f"  differs: {name}")
        for key in ("wall_seconds", *STAGES):
            a, b = before[key], after[key]
            speedup = f"{a / b:5.2f}x" if b > 0 else "     -"
            print(f"  {key:34s} {a:8.3f} s -> {b:8.3f} s  {speedup}")
    print("\nall outputs byte-identical" if identical else "\nOUTPUTS DIFFER")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    run_parser = commands.add_parser("run")
    run_parser.add_argument("--output", required=True)
    run_parser.add_argument("--backend", default="vulkan")
    run_parser.add_argument("--quality", default="final")
    run_parser.add_argument("--repeats", type=int, default=3)
    run_parser.add_argument("--scenes", nargs="+", default=["acceptance", "office_floors"])
    run_parser.add_argument("--weather", default=str(ROOT / "epw" / "gothenburg.epw"))
    compare_parser = commands.add_parser("compare")
    compare_parser.add_argument("old")
    compare_parser.add_argument("new")
    args = parser.parse_args()
    run(args) if args.command == "run" else compare(args)


if __name__ == "__main__":
    main()
