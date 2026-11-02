#!/usr/bin/env python3
"""Run reproducible beta validation. Missing evidence never becomes PASS.

Run from a checkout with foton-daylight[honeybee], lbt-recipes and Radiance installed.
CPU/smoke/partial runs are diagnostics and cannot qualify a GPU release.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import numpy as np
from foton import Engine, __version__
from foton.honeybee import HoneybeeStudy, compare_annual_daylight
from foton.honeybee.adapter import prepare_honeybee_scene
from foton.honeybee.annual import (
    DEFAULT_MAXIMUM_BOUNCES,
    PHOTOPIC_WEIGHTS,
    honeybee_schedule,
    quality_preset,
)
from foton.honeybee.radiance import (
    run_radiance_coefficient_stages,
    run_radiance_integrated_direct,
)
from foton.honeybee.validation import (
    compare_coefficient_stages,
    compare_coefficient_convergence,
    compare_converged_annual,
    verify_official_annual_daylight_loader,
)
from foton.honeybee.weather import prepare_annual_weather
from scripts.validate_honeybee_coefficients import trace_coefficients
from validation.scenes import (
    SCENE_CATEGORIES,
    SCENE_IDS,
    SCENE_SPECS,
    SCENE_VERSION,
    make_scene,
    scene_metadata,
)
from validation.oracle import (
    patch_samples,
    export_scene,
    convergence_by_grid,
    difference,
    audit_sky_bins,
)


def write_report(folder, name, report):
    folder.mkdir(parents=True, exist_ok=True)

    # Strict JSON: unavailable/undefined numerical values are explicit strings.
    def clean(value):
        if isinstance(value, dict):
            return {k: clean(v) for k, v in value.items()}
        if isinstance(value, (list, tuple)):
            return [clean(v) for v in value]
        if isinstance(value, float) and not np.isfinite(value):
            return str(value)
        return value

    report = clean(report)
    (folder / (name + ".json")).write_text(
        json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n"
    )
    lines = [
        "# Foton " + name.replace("_", " "),
        "",
        "Status: **" + report.get("status", "diagnostic") + "**",
        "",
    ]
    if "scenes" in report:
        lines += ["| Scene | Sky density | Status |", "| --- | --- | --- |"]
        lines += [
            "| %s | %s | %s |" % (r["scene"], r["sky_density"], r["status"])
            for r in report["scenes"]
        ]
    else:
        lines += ["```json", json.dumps(report, indent=2), "```"]
    (folder / (name + ".md")).write_text("\n".join(lines) + "\n")


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate_models(directory, identifiers):
    """Reject stale, incomplete or modified exported fixtures before execution."""
    from honeybee.model import Model

    directory = Path(directory).resolve()
    manifest = json.loads((directory / "manifest.json").read_text())
    if (
        manifest.get("suite_version") != SCENE_VERSION
        or manifest.get("units") != "Meters"
    ):
        raise ValueError("Fixture manifest version or units do not match the corpus")
    records = manifest.get("scenes", [])
    names = [record["identifier"] for record in records]
    if len(names) != len(set(names)) or manifest.get("scene_count") != len(names):
        raise ValueError(
            "Fixture manifest contains duplicate scenes or incorrect count"
        )
    if not set(identifiers).issubset(names) or not set(names).issubset(SCENE_IDS):
        raise ValueError("Fixture manifest does not cover the selected scenes")
    paths = {}
    for record in records:
        identifier = record["identifier"]
        if record["file"] != identifier + ".hbjson":
            raise ValueError("Unexpected fixture filename: " + identifier)
        path = directory / record["file"]
        if digest(path) != record["sha256"]:
            raise ValueError("Fixture hash mismatch: " + identifier)
        model = Model.from_hbjson(str(path))
        if model.units != "Meters" or (model.user_data or {}).get(
            "validation_scene"
        ) != scene_metadata(identifier):
            raise ValueError("Fixture metadata mismatch: " + identifier)
        if model.check_all(raise_exception=False, detailed=True):
            raise ValueError("Invalid fixture: " + identifier)
        paths[identifier] = path
    return paths


def hardware():
    commands = (
        (["system_profiler", "SPDisplaysDataType", "-json"],)
        if sys.platform == "darwin"
        else (
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "Get-CimInstance Win32_VideoController | Select-Object Name,DriverVersion | ConvertTo-Json",
            ],
        )
        if os.name == "nt"
        else (["vulkaninfo", "--summary"],)
    )
    result = {
        "platform": platform.platform(),
        "system": platform.system(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }
    for command in commands:
        try:
            completed = subprocess.run(
                command, capture_output=True, text=True, timeout=30
            )
            result["driver_diagnostics"] = (
                completed.stdout.strip() or completed.stderr.strip()
            )
            if sys.platform == "darwin" and completed.returncode == 0:
                displays = json.loads(completed.stdout)["SPDisplaysDataType"]
                result["driver_diagnostics"] = [
                    {
                        key: value
                        for key, value in device.items()
                        if key != "spdisplays_ndrvs"
                    }
                    for device in displays
                ]
        except (OSError, subprocess.TimeoutExpired) as error:
            result["driver_diagnostics"] = str(error)
    return result


def run_scene(args, identifier, density, output):
    if args.models_dir:
        from honeybee.model import Model

        model = Model.from_hbjson(str(args.model_paths[identifier]))
    else:
        model = make_scene(identifier, ROOT)
    model_path = Path(model.to_hbjson("model", str(output), indent=2))
    metadata = scene_metadata(identifier)
    prepared = prepare_honeybee_scene(
        model, include_aperture_glazing=metadata["include_glazing"]
    )
    octree, dome, export_command = export_scene(
        model,
        output / "oracle",
        density,
        args.radiance_bin,
        not metadata["include_glazing"],
    )
    rows = 146 if density == 1 else 578
    preset = quality_preset("preview" if args.smoke else "final", density)
    candidate = trace_coefficients(
        prepared,
        backend=args.backend,
        rows=rows,
        direct_samples=preset["direct_samples"],
        indirect_samples=preset["maximum_samples"],
    )
    for stage in ("direct", "full"):
        np.save(output / ("foton_" + stage + ".npy"), candidate[stage])

    direct_runs = []
    sky_audit = audit_sky_bins(
        patch_samples(density, 32)[0], density, args.radiance_bin
    )
    if not sky_audit["passed"]:
        raise RuntimeError(
            "Independent sky samples disagree with Radiance patch numbering"
        )
    # MF:2 spreads the same ambient-ray budget over four times as many sky
    # bins, so per-coefficient Monte Carlo noise roughly doubles; the RMS
    # stability gates follow. Energy (bias) gates are unchanged.
    stability_rms_gate = 5.0 if density == 1 else 10.0
    # Direct integration doubles its sample budget until two successive
    # levels agree (borrowed-light grids carry little direct energy and are
    # noisy at 1,024 samples per patch); the last level is the reference.
    direct_counts = (4, 16, 64) if args.smoke else (256, 1024, 4096, 16384)
    direct_stability = None
    for count in direct_counts:
        print(f"  Independent direct integration: {count} samples/patch", flush=True)
        directions, weights = patch_samples(density, count)
        direct_runs.append(
            run_radiance_integrated_direct(
                prepared.arrays["sensor_positions"],
                prepared.arrays["sensor_normals"],
                directions,
                weights,
                octree=octree,
                sky_dome=dome,
                work_directory=output / ("direct_%d" % count),
                workers=args.workers,
                radiance_bin=args.radiance_bin,
                binary_io=args.direct_io == "binary",
            )
        )
        if len(direct_runs) >= 2:
            direct_stability = convergence_by_grid(
                prepared,
                direct_runs[-2].coefficients,
                direct_runs[-1].coefficients,
                rms_gate=stability_rms_gate,
            )
            direct_stability["samples_per_patch"] = [
                direct_counts[len(direct_runs) - 2],
                direct_counts[len(direct_runs) - 1],
            ]
            if direct_stability["passed"]:
                break

    # Independently vary depth and sample budget. The one-bounce level stays as a
    # diagnostic of how much reflected light the candidate's default depth adds.
    # Depth stability compares 8 and 12 material bounces: the 2026-11-02 sweep put
    # glazed rooms within 0.5% there, while 4 vs 8 differ by ~2% from physics
    # alone and would mark every converged reference unstable.
    levels = (
        ((64, 1), (128, 8), (128, 12), (256, 12))
        if args.smoke
        else ((20000, 1), (40000, 8), (40000, 12), (80000, 12))
    )
    references, oracle_records = [], []
    for samples, bounces in levels:
        # Four replicates to start; noisy references (rooflights, borrowed
        # light) get four more at a time, up to twelve, until the replicate
        # halves agree. Every replicate feeds the level's mean.
        runs = []
        while True:
            for replicate in range(len(runs), len(runs) + 4):
                print(
                    f"  Radiance: ad={samples}, bounces={bounces}, replicate={replicate + 1}",
                    flush=True,
                )
                run = run_radiance_coefficient_stages(
                    prepared.arrays["sensor_positions"],
                    prepared.arrays["sensor_normals"],
                    octree=octree,
                    sky_dome=dome,
                    sky_density=density,
                    work_directory=output
                    / ("ad%d_b%d_r%d" % (samples, bounces, replicate)),
                    workers=args.workers,
                    radiance_bin=args.radiance_bin,
                    material_bounces=bounces,
                    radiance_parameters=("-ad", str(samples), "-lw", "1e-7", "-dr", "0"),
                )
                runs.append(run)
            repeatability = compare_coefficient_convergence(
                prepared,
                radiance_direct_runs=[r.direct for r in runs],
                radiance_full_runs=[r.full for r in runs],
                rms_gate_percent=stability_rms_gate,
            )
            if repeatability["oracle_stable"] or len(runs) >= 12:
                break
        references.append(np.mean([r.full for r in runs], axis=0))
        oracle_records.append(
            {
                "samples": samples,
                "material_bounces": bounces,
                "repeatability": repeatability,
                "runs": [
                    {
                        "commands": r.commands,
                        "versions": r.versions,
                        "timings_ms": r.timings_ms,
                    }
                    for r in runs
                ],
            }
        )
    depth_stability = convergence_by_grid(
        prepared, references[1], references[2], rms_gate=stability_rms_gate
    )
    sample_stability = convergence_by_grid(
        prepared, references[2], references[3], rms_gate=stability_rms_gate
    )
    # The one-bounce level is a diagnostic, not part of the reference, so its
    # replicate repeatability (noisy at ad=20000) does not decide stability.
    stable = (
        direct_stability["passed"]
        and depth_stability["passed"]
        and sample_stability["passed"]
        and all(r["repeatability"]["oracle_stable"] for r in oracle_records[1:])
    )
    stages = compare_coefficient_stages(
        prepared,
        foton_direct=candidate["direct"],
        foton_full=candidate["full"],
        radiance_direct=direct_runs[-1].coefficients,
        radiance_full=references[-1],
        output_folder=output,
    )
    one_bounce = compare_coefficient_stages(
        prepared,
        foton_direct=candidate["direct"],
        foton_full=candidate["full"],
        radiance_direct=direct_runs[-1].coefficients,
        radiance_full=references[0],
    )
    for comparison in (stages, one_bounce):
        for grid in comparison["grids"]:
            for stage in grid["stages"].values():
                worst = stage["worst"]
                worst["position"] = prepared.arrays["sensor_positions"][
                    worst["global_sensor_index"]
                ].tolist()
    np.save(output / "radiance_converged_full.npy", references[-1])

    directions, _ = patch_samples(density, 1)
    z = directions[:, 0, 2].clip(0)
    skies = {
        "uniform": np.ones(rows),
        "overcast": (1 + 2 * z) / 3,
        "horizon": (z < 0.15).astype(float),
        "north": directions[:, 0, 1].clip(0),
        "east": directions[:, 0, 0].clip(0),
        "south": (-directions[:, 0, 1]).clip(0),
        "west": (-directions[:, 0, 0]).clip(0),
    }
    controlled = {}
    uniform_level = uniform_rms = None
    for name, sky in skies.items():
        sky[0] = 0
        ref = np.einsum("spr,p,r->s", references[-1], sky, PHOTOPIC_WEIGHTS)
        actual = np.einsum("spr,p,r->s", candidate["full"], sky, PHOTOPIC_WEIGHTS)
        controlled[name] = difference(ref, actual)
        if uniform_level is None:
            uniform_level = float(np.mean(np.abs(ref)))
            uniform_rms = float(np.sqrt(np.mean(np.square(ref))))
        # A sky the room cannot see (north sky through a south window) leaves a
        # reference of Radiance leakage only; relative error there is noise.
        near_zero = float(np.mean(np.abs(ref))) <= max(1e-3 * uniform_level, 1e-3)
        # Per-sensor scatter is judged against the uniform-sky level, so a
        # component worth 0.3% of the light (horizon band into a rooflight)
        # is weighed by its effect on the result; its bias is still gated.
        rms_to_uniform = (
            100.0
            * float(np.sqrt(np.mean(np.square(actual - ref))))
            / max(uniform_rms, 1e-20)
        )
        # A sky worth under 0.5 % of the uniform-sky light (north sky reaching
        # a south room off its louvres) cannot move a metric; its bias is
        # recorded but not gated, matching the indirect-stage waiver.
        negligible = float(np.mean(np.abs(ref))) <= 0.005 * uniform_level
        controlled[name]["physically_near_zero"] = near_zero
        controlled[name]["negligible"] = bool(negligible and not near_zero)
        controlled[name]["reference_mean"] = float(np.mean(ref))
        controlled[name]["reference_fraction_of_uniform"] = float(
            np.mean(np.abs(ref)) / max(uniform_level, 1e-20)
        )
        controlled[name]["rms_normalized_to_uniform_percent"] = rms_to_uniform
        controlled[name]["passed"] = (
            near_zero
            or negligible
            or (
                abs(controlled[name].get("bias_percent", float("inf"))) < 5
                and rms_to_uniform < 10
            )
        )
    study = HoneybeeStudy(
        model,
        backend=args.backend,
        radiance_bin=args.radiance_bin,
        weather_cache=output.parent.parent / "weather_cache",
    )
    if identifier == "black_open":
        # This fixture deliberately removes glazing in both independent exports.
        study.prepared = prepared
        study.scene = prepared.create_native_scene(study.engine)
    annual_output = output / "annual"
    annual = study.annual_daylight(
        args.weather,
        output_folder=annual_output,
        export_illuminance=True,
        quality="preview" if args.smoke else "final",
        sky_density=density,
    )
    cached = study.annual_daylight(
        args.weather,
        output_folder=output / "annual_cached",
        export_illuminance=True,
        quality="preview" if args.smoke else "final",
        sky_density=density,
    )
    weather = prepare_annual_weather(
        args.weather,
        sky_density=density,
        radiance_bin=args.radiance_bin,
        cache_directory=output.parent.parent / "weather_cache",
    )
    indices = np.asarray(weather.sun_up_hours, dtype=int)
    annual_comparison = compare_converged_annual(
        prepared,
        foton_folder=annual_output,
        radiance_coefficients=references[-1],
        sky_matrix=weather.sky[:, indices],
        sun_up_hours=weather.sun_up_hours,
        schedule=honeybee_schedule(),
        output_folder=output,
    )
    loader = verify_official_annual_daylight_loader(annual_output)
    darkness = {
        "required": identifier == "sealed",
        "passed": True,
        "maximum_lux": None,
        "tolerance_lux": 1e-6,
    }
    if identifier == "sealed":
        arrays = list((annual_output / "results").rglob("*.npy"))
        darkness["maximum_lux"] = max(float(np.max(np.abs(np.load(p)))) for p in arrays)
        darkness["passed"] = darkness["maximum_lux"] <= darkness["tolerance_lux"]
    stock = {"status": "not_applicable", "passed": True}
    if identifier == "acceptance":
        command = [
            sys.executable,
            str(ROOT / "scripts/run_honeybee_annual_reference.py"),
            "--model",
            str(model_path),
            "--wea",
            str(args.weather),
            "--output",
            str(output / "stock"),
            "--workers",
            str(args.workers),
        ]
        if args.radiance_bin:
            command += ["--radiance-bin", args.radiance_bin]
        with (output / "stock.log").open("w") as log:
            subprocess.run(command, stdout=log, stderr=subprocess.STDOUT, check=True)
        reference_manifest = json.loads(
            (output / "stock/reference_manifest.json").read_text()
        )
        stock = compare_annual_daylight(
            annual_output,
            reference_manifest["project"],
            model=model_path,
            foton_seconds=annual.timings["cold_end_to_end_seconds"],
            radiance_seconds=reference_manifest["elapsed_seconds"],
            output_folder=output / "stock_comparison",
            oracle="stock",
        )
        stock["reference_sky_density"] = 1  # Stock recipe fixes MF:1 internally.
        stock["candidate_sky_density"] = density
    gpu = all(
        not candidate["metadata"][stage].get("used_reference_fallback", True)
        and candidate["metadata"][stage].get("transport_backend") == args.backend
        for stage in ("direct", "full")
    )
    numerical = (
        stable
        and stages["passed"]
        and annual_comparison["passed"]
        and darkness["passed"]
        and all(x["passed"] for x in controlled.values())
    )
    passed = numerical and loader["passed"]
    status = (
        "incomplete"
        if args.smoke or not stable or not gpu
        else "passed"
        if passed
        else "failed"
    )
    return {
        "scene": identifier,
        "scene_spec": metadata,
        "model_summary": {
            "rooms": len(model.rooms),
            "apertures": len(model.apertures),
            "shades": len(model.shades),
            "sensors": len(prepared.arrays["sensor_positions"]),
            "floor_area": model.floor_area,
            "aperture_area": sum(aperture.area for aperture in model.apertures),
        },
        "sky_density": density,
        "status": status,
        "passed": status == "passed",
        "model_sha256": digest(model_path),
        "weather_sha256": digest(args.weather),
        "gpu_executed": gpu,
        "candidate": candidate["metadata"],
        "sky_bin_audit": sky_audit,
        "settings": {**preset, "maximum_bounces": DEFAULT_MAXIMUM_BOUNCES},
        "direct_io": args.direct_io,
        "oracle_stable": stable,
        "direct_stability": direct_stability,
        "depth_stability": depth_stability,
        "sample_stability": sample_stability,
        "oracle_levels": oracle_records,
        "export_command": export_command,
        "direct_oracles": [
            {
                "commands": r.commands,
                "versions": r.versions,
                "sample_count": r.sample_count,
                "elapsed_ms": r.elapsed_ms,
                "worker_pool_size": args.workers,
                "invocation_count": r.invocation_count,
            }
            for r in direct_runs
        ],
        "coefficients": stages,
        "one_bounce_diagnostic": one_bounce,
        "controlled_skies": controlled,
        "annual": annual_comparison,
        "outcomes": {
            "numerical_correctness": "incomplete"
            if not stable
            else "passed"
            if numerical
            else "failed",
            "honeybee_compatibility": "passed" if loader["passed"] else "failed",
            "performance": "measured",
        },
        "compatibility": {"official_loader": loader, "stock": stock},
        "darkness": darkness,
        "performance": {
            "candidate_cold": annual.timings,
            "candidate_cached": cached.timings,
            "coefficient_stages_seconds": candidate["timings_seconds"],
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--backend", choices=("metal", "vulkan", "reference"), required=True
    )
    parser.add_argument("--scene", choices=SCENE_IDS, action="append")
    parser.add_argument("--category", choices=SCENE_CATEGORIES, action="append")
    parser.add_argument("--sky-density", choices=(1, 2), type=int, action="append")
    parser.add_argument("--weather", type=Path, default=ROOT / "epw/gothenburg.epw")
    parser.add_argument(
        "--models-dir", type=Path, help="Use validated exported HBJSON fixtures"
    )
    parser.add_argument(
        "--wheel", type=Path, help="Installed wheel archived with this campaign"
    )
    parser.add_argument("--radiance-bin")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--direct-io", choices=("binary", "ascii"), default="binary")
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    if args.workers < 1:
        parser.error("workers must be positive")
    scenes = tuple(
        spec.identifier
        for spec in SCENE_SPECS
        if (not args.scene or spec.identifier in args.scene)
        and (not args.category or spec.category in args.category)
    )
    if not scenes:
        parser.error("No scenes match the selected scenes and categories")
    densities = tuple(dict.fromkeys(args.sky_density or (1, 2)))
    args.output = args.output.resolve()
    args.weather = args.weather.resolve()
    if args.models_dir:
        try:
            args.model_paths = validate_models(args.models_dir, scenes)
        except (ValueError, KeyError, OSError) as error:
            parser.error(str(error))
    # Never contaminate evidence with artifacts from another execution.
    args.output.mkdir(parents=True, exist_ok=False)
    commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()
    dirty = bool(
        subprocess.check_output(
            ["git", "status", "--porcelain", "--untracked-files=normal"],
            cwd=ROOT,
            text=True,
        ).strip()
    )
    report = {
        "schema_version": 1,
        "suite_version": SCENE_VERSION,
        "commit": commit,
        "dirty": dirty,
        "engine_version": __version__,
        "hardware": hardware(),
        "backend": args.backend,
        "dependencies": dict(
            sorted(
                (dist.metadata["Name"], dist.version)
                for dist in importlib.metadata.distributions()
                if dist.metadata["Name"]
            )
        ),
        "fixtures": {
            "manifest_sha256": digest(args.models_dir / "manifest.json"),
            "directory": str(args.models_dir.resolve()),
        }
        if args.models_dir
        else None,
        "wheel_sha256": digest(args.wheel) if args.wheel else None,
        "weather": str(args.weather),
        "weather_sha256": digest(args.weather) if args.weather.exists() else None,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "smoke": args.smoke,
        "status": "incomplete",
        "expected_case_count": len(SCENE_IDS) * 2,
        "selected_case_count": len(scenes) * len(densities),
        "scenes": [],
    }
    import daylight_engine._native as native

    report["native_module"] = {
        "path": native.__file__,
        "sha256": digest(native.__file__),
    }
    started = time.perf_counter()
    try:
        report["capabilities"] = dict(Engine({"backend": args.backend}).capabilities())
        for identifier in scenes:
            for density in densities:
                output = args.output / identifier / ("mf%d" % density)
                output.mkdir(parents=True)
                print("Validating %s / MF:%d" % (identifier, density), flush=True)
                case_started = time.perf_counter()
                try:
                    result = run_scene(args, identifier, density, output)
                except Exception as error:
                    result = {
                        "scene": identifier,
                        "scene_spec": scene_metadata(identifier),
                        "sky_density": density,
                        "status": "incomplete",
                        "passed": False,
                        "error": str(error),
                        "error_type": type(error).__name__,
                    }
                    import traceback

                    (output / "error.log").write_text(traceback.format_exc())
                result["elapsed_seconds"] = time.perf_counter() - case_started
                result["result_class"] = (
                    "execution_error"
                    if "error" in result
                    else "unstable_reference"
                    if result.get("oracle_stable") is False
                    else "accuracy_failure"
                    if result.get("outcomes", {}).get("numerical_correctness")
                    == "failed"
                    else "passed"
                    if result["passed"]
                    else "incomplete"
                )
                write_report(output, "report", result)
                report["scenes"].append(result)
                write_report(args.output, "suite", report)
        complete = (
            set(scenes) == set(SCENE_IDS)
            and set(densities) == {1, 2}
            and len(report["scenes"]) == len(SCENE_IDS) * 2
        )
        report["status"] = (
            "passed"
            if complete
            and not dirty
            and not args.smoke
            and all(r["passed"] for r in report["scenes"])
            else "failed"
            if any(r["status"] == "failed" for r in report["scenes"])
            else "incomplete"
        )
    except Exception as error:
        report["error"] = str(error)
    finally:
        report["elapsed_seconds"] = time.perf_counter() - started
        report["accounted_case_count"] = len(report["scenes"])
        report["result_counts"] = {
            kind: sum(r.get("result_class") == kind for r in report["scenes"])
            for kind in (
                "passed",
                "accuracy_failure",
                "unstable_reference",
                "execution_error",
                "incomplete",
            )
        }
        report["passed"] = report["status"] == "passed"
        write_report(args.output, "suite", report)
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
