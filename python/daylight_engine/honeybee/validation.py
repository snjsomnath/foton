"""Structural, numerical, and performance gates for annual-daylight results."""

from __future__ import annotations

import json
from pathlib import Path
import platform
import sys
from typing import Any

import numpy as np

from .adapter import prepare_honeybee_scene


METRICS = ("da", "cda", "udi_lower", "udi", "udi_upper")


def verify_official_annual_daylight_loader(
    foton_folder,
    *,
    tolerance_percentage_points=0.05,
) -> dict[str, Any]:
    """Load Foton output with the official Honeybee result API and recompute metrics."""
    try:
        from honeybee_radiance_postprocess.results import AnnualDaylight
    except ImportError as error:
        raise ImportError(
            "official loader verification requires "
            "honeybee-radiance-postprocess"
        ) from error
    root = Path(foton_folder).expanduser().resolve()
    loader = AnnualDaylight(_results_folder(root))
    calls = {
        "da": loader.daylight_autonomy,
        "cda": loader.continuous_daylight_autonomy,
        "udi": loader.useful_daylight_illuminance,
        "udi_lower": loader.useful_daylight_illuminance_lower,
        "udi_upper": loader.useful_daylight_illuminance_upper,
    }
    metric_results = {}
    maximum_error = 0.0
    for metric, method in calls.items():
        arrays, grid_info = method()
        grids = []
        for values, info in zip(arrays, grid_info, strict=True):
            grid_id = info["full_id"]
            expected = _metric_values(root, metric, grid_id)
            error = float(
                np.max(
                    np.abs(np.asarray(values, dtype=np.float64) - expected),
                    initial=0,
                )
            )
            maximum_error = max(maximum_error, error)
            grids.append(
                {
                    "identifier": grid_id,
                    "maximum_error_percentage_points": error,
                    "passed": bool(error <= tolerance_percentage_points),
                }
            )
        metric_results[metric] = grids
    return {
        "passed": bool(maximum_error <= tolerance_percentage_points),
        "tolerance_percentage_points": float(tolerance_percentage_points),
        "maximum_error_percentage_points": maximum_error,
        "metrics": metric_results,
    }


def compare_coefficient_repeatability(
    prepared,
    *,
    radiance_direct_runs,
    radiance_full_runs,
    output_folder: str | Path | None = None,
) -> dict[str, Any]:
    """Measure the stochastic floor across repeated Radiance coefficient runs."""
    direct_runs = [
        np.asarray(value, dtype=np.float64) for value in radiance_direct_runs
    ]
    full_runs = [
        np.asarray(value, dtype=np.float64) for value in radiance_full_runs
    ]
    if len(direct_runs) < 2 or len(full_runs) != len(direct_runs):
        raise ValueError(
            "repeatability requires at least two matching direct/full runs"
        )
    shapes = {
        value.shape for value in (*direct_runs, *full_runs)
    }
    if len(shapes) != 1:
        raise ValueError(f"repeatability coefficient shapes differ: {shapes}")

    pair_results = []
    for first in range(len(direct_runs)):
        for second in range(first + 1, len(direct_runs)):
            grids = []
            for info in prepared.grid_info:
                start = int(info["start_sensor_index"])
                end = start + int(info["sensor_count"])
                direct = _coefficient_statistics(
                    direct_runs[first][start:end],
                    direct_runs[second][start:end],
                    global_sensor_offset=start,
                    nmbe_gate=2.0,
                    cvrmse_gate=5.0,
                )
                indirect = _coefficient_statistics(
                    (
                        full_runs[first][start:end]
                        - direct_runs[first][start:end]
                    ),
                    (
                        full_runs[second][start:end]
                        - direct_runs[second][start:end]
                    ),
                    global_sensor_offset=start,
                    nmbe_gate=3.0,
                    cvrmse_gate=10.0,
                )
                grids.append(
                    {
                        "identifier": info["identifier"],
                        "direct": direct,
                        "indirect": indirect,
                    }
                )
            pair_results.append(
                {
                    "first_run": first,
                    "second_run": second,
                    "grids": grids,
                }
            )
    oracle_stable = all(
        stage["passed"]
        for pair in pair_results
        for grid in pair["grids"]
        for stage in (grid["direct"], grid["indirect"])
    )
    report = {
        "schema_version": 1,
        "run_count": len(direct_runs),
        "oracle_stable_at_release_gates": bool(oracle_stable),
        "pairs": pair_results,
    }
    if output_folder is not None:
        output = Path(output_folder).expanduser().resolve()
        output.mkdir(parents=True, exist_ok=True)
        (output / "radiance_repeatability.json").write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        (output / "radiance_repeatability.md").write_text(
            _repeatability_markdown(report), encoding="utf-8"
        )
    return report


def compare_coefficient_stages(
    prepared,
    *,
    foton_direct,
    foton_full,
    radiance_direct,
    radiance_full,
    output_folder: str | Path | None = None,
) -> dict[str, Any]:
    """Compare direct and isolated one-bounce coefficient stages by grid."""
    arrays = {
        "foton_direct": np.asarray(foton_direct, dtype=np.float64),
        "foton_full": np.asarray(foton_full, dtype=np.float64),
        "radiance_direct": np.asarray(radiance_direct, dtype=np.float64),
        "radiance_full": np.asarray(radiance_full, dtype=np.float64),
    }
    shapes = {name: value.shape for name, value in arrays.items()}
    if len(set(shapes.values())) != 1:
        raise ValueError(f"coefficient shapes do not match: {shapes}")
    expected_sensors = int(prepared.arrays["sensor_positions"].shape[0])
    shape = next(iter(shapes.values()))
    if len(shape) != 3 or shape[0] != expected_sensors or shape[2] != 3:
        raise ValueError(
            "coefficient arrays must have shape "
            f"[{expected_sensors}, sky_patch, 3]; got {shape}"
        )
    stages = {
        "direct": (arrays["radiance_direct"], arrays["foton_direct"], 2.0, 5.0),
        "indirect": (
            arrays["radiance_full"] - arrays["radiance_direct"],
            arrays["foton_full"] - arrays["foton_direct"],
            3.0,
            10.0,
        ),
        "full": (arrays["radiance_full"], arrays["foton_full"], 5.0, 10.0),
    }
    grids = []
    for info in prepared.grid_info:
        start = int(info["start_sensor_index"])
        count = int(info["sensor_count"])
        end = start + count
        stage_results = {}
        for stage_name, (reference, candidate, nmbe_gate, cvrmse_gate) in stages.items():
            stage_results[stage_name] = _coefficient_statistics(
                reference[start:end],
                candidate[start:end],
                global_sensor_offset=start,
                nmbe_gate=nmbe_gate,
                cvrmse_gate=cvrmse_gate,
            )
        grids.append(
            {
                "identifier": info["identifier"],
                "full_identifier": info["full_identifier"],
                "start_sensor_index": start,
                "sensor_count": count,
                "stages": stage_results,
            }
        )
    passed = all(
        grid["stages"]["direct"]["passed"]
        and grid["stages"]["indirect"]["passed"]
        for grid in grids
    )
    report = {
        "schema_version": 1,
        "passed": bool(passed),
        "matrix_shape": list(shape),
        "gates": {
            "direct": {"absolute_nmbe_percent": 2.0, "cvrmse_percent": 5.0},
            "indirect": {"absolute_nmbe_percent": 3.0, "cvrmse_percent": 10.0},
        },
        "grids": grids,
    }
    if output_folder is not None:
        output = Path(output_folder).expanduser().resolve()
        output.mkdir(parents=True, exist_ok=True)
        (output / "coefficient_comparison.json").write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        (output / "coefficient_comparison.md").write_text(
            _coefficient_markdown(report), encoding="utf-8"
        )
    return report


def _coefficient_statistics(
    reference,
    candidate,
    *,
    global_sensor_offset,
    nmbe_gate,
    cvrmse_gate,
):
    difference = candidate - reference
    reference_mean = float(np.mean(reference))
    reference_maximum = float(np.max(np.abs(reference), initial=0))
    candidate_maximum = float(np.max(np.abs(candidate), initial=0))
    physically_near_zero = max(reference_maximum, candidate_maximum) <= 1.0e-3
    if physically_near_zero:
        nmbe = cvrmse = 0.0
    elif abs(reference_mean) <= 1.0e-20:
        maximum = float(np.max(np.abs(difference), initial=0))
        nmbe = cvrmse = 0.0 if maximum <= 1.0e-8 else float("inf")
    else:
        nmbe = 100.0 * float(np.mean(difference)) / reference_mean
        cvrmse = (
            100.0 * float(np.sqrt(np.mean(np.square(difference))))
            / abs(reference_mean)
        )
    absolute = np.abs(difference)
    flat_index = int(np.argmax(absolute)) if absolute.size else 0
    local_sensor, patch, channel = np.unravel_index(flat_index, absolute.shape)
    reference_energy = float(np.sum(reference))
    candidate_energy = float(np.sum(candidate))
    return {
        "nmbe_percent": nmbe,
        "cvrmse_percent": cvrmse,
        "reference_energy": reference_energy,
        "candidate_energy": candidate_energy,
        "relative_energy_error_percent": (
            0.0
            if physically_near_zero
            else 100.0
            * abs(candidate_energy - reference_energy)
            / max(abs(reference_energy), 1.0e-20)
        ),
        "physically_near_zero": physically_near_zero,
        "absolute_error": {
            "p50": float(np.percentile(absolute, 50)),
            "p90": float(np.percentile(absolute, 90)),
            "p95": float(np.percentile(absolute, 95)),
            "p99": float(np.percentile(absolute, 99)),
            "maximum": float(np.max(absolute, initial=0)),
        },
        "worst": {
            "global_sensor_index": int(global_sensor_offset + local_sensor),
            "local_sensor_index": int(local_sensor),
            "sky_patch_index": int(patch),
            "rgb_channel": int(channel),
            "reference": float(reference[local_sensor, patch, channel]),
            "candidate": float(candidate[local_sensor, patch, channel]),
        },
        "passed": bool(abs(nmbe) < nmbe_gate and cvrmse < cvrmse_gate),
    }


def _coefficient_markdown(report):
    lines = [
        "# Foton / Radiance coefficient-stage comparison",
        "",
        f"Overall: **{'PASS' if report['passed'] else 'FAIL'}**",
        "",
        "| Grid | Stage | NMBE | CV(RMSE) | Energy error | Gate |",
        "|---|---|---:|---:|---:|:---:|",
    ]
    for grid in report["grids"]:
        for stage in ("direct", "indirect", "full"):
            values = grid["stages"][stage]
            lines.append(
                f"| {grid['identifier']} | {stage} | "
                f"{values['nmbe_percent']:.3f}% | "
                f"{values['cvrmse_percent']:.3f}% | "
                f"{values['relative_energy_error_percent']:.3f}% | "
                f"{'PASS' if values['passed'] else 'FAIL'} |"
            )
    return "\n".join(lines) + "\n"


def _repeatability_markdown(report):
    lines = [
        "# Radiance coefficient repeatability",
        "",
        "Oracle stability at release gates: "
        f"**{'PASS' if report['oracle_stable_at_release_gates'] else 'FAIL'}**",
        "",
        "| Runs | Grid | Stage | NMBE | CV(RMSE) | Gate |",
        "|---|---|---|---:|---:|:---:|",
    ]
    for pair in report["pairs"]:
        label = f"{pair['first_run']} / {pair['second_run']}"
        for grid in pair["grids"]:
            for stage_name in ("direct", "indirect"):
                values = grid[stage_name]
                lines.append(
                    f"| {label} | {grid['identifier']} | {stage_name} | "
                    f"{values['nmbe_percent']:.3f}% | "
                    f"{values['cvrmse_percent']:.3f}% | "
                    f"{'PASS' if values['passed'] else 'FAIL'} |"
                )
    return "\n".join(lines) + "\n"


def compare_annual_daylight(
    foton_folder,
    radiance_folder,
    *,
    model=None,
    foton_seconds: float | None = None,
    radiance_seconds: float | None = None,
    output_folder: str | Path | None = None,
) -> dict[str, Any]:
    """Compare compatible Foton and Honeybee Radiance result trees."""
    foton_root = Path(foton_folder).expanduser().resolve()
    radiance_root = Path(radiance_folder).expanduser().resolve()
    foton_results = _results_folder(foton_root)
    radiance_results = _results_folder(radiance_root)
    foton_info = _json(foton_results / "grids_info.json")
    radiance_info = _json(radiance_results / "grids_info.json")
    foton_ids = [item["full_id"] for item in foton_info]
    radiance_ids = [item["full_id"] for item in radiance_info]
    foton_counts = [int(item["count"]) for item in foton_info]
    radiance_counts = [int(item["count"]) for item in radiance_info]
    foton_hours = np.loadtxt(foton_results / "sun-up-hours.txt")
    radiance_hours = np.loadtxt(radiance_results / "sun-up-hours.txt")

    structural = {
        "grid_ids_match": foton_ids == radiance_ids,
        "grid_counts_match": foton_counts == radiance_counts,
        "sun_up_hours_match": bool(
            np.array_equal(foton_hours, radiance_hours)
        ),
    }
    official_loader = verify_official_annual_daylight_loader(foton_root)
    prepared = None
    if model is not None:
        prepared = prepare_honeybee_scene(
            model, include_aperture_glazing=True
        )
        expected_ids = [item["full_identifier"] for item in prepared.grid_info]
        expected_counts = [item["sensor_count"] for item in prepared.grid_info]
        structural["model_grid_ids_match"] = expected_ids == foton_ids
        structural["model_grid_counts_match"] = expected_counts == foton_counts

    grids = []
    for grid_index, (grid_id, count) in enumerate(
        zip(foton_ids, foton_counts, strict=True)
    ):
        foton_raw = np.load(
            foton_results
            / "__static_apertures__"
            / "default"
            / "total"
            / f"{grid_id}.npy",
            allow_pickle=False,
        ).astype(np.float64)
        radiance_raw = np.load(
            radiance_results
            / "__static_apertures__"
            / "default"
            / "total"
            / f"{grid_id}.npy",
            allow_pickle=False,
        ).astype(np.float64)
        expected_shape = (count, len(foton_hours))
        shape_match = (
            foton_raw.shape == radiance_raw.shape == expected_shape
        )
        if not shape_match:
            raise ValueError(
                f"grid {grid_id!r} raw shapes do not match: "
                f"{foton_raw.shape}, {radiance_raw.shape}, {expected_shape}"
            )
        difference = foton_raw - radiance_raw
        reference_mean = float(np.mean(radiance_raw))
        if reference_mean == 0:
            nmbe = cvrmse = (
                0.0 if np.max(np.abs(difference), initial=0) <= 1.0e-6 else float("inf")
            )
        else:
            nmbe = 100.0 * float(np.mean(difference)) / reference_mean
            cvrmse = (
                100.0
                * float(np.sqrt(np.mean(np.square(difference))))
                / reference_mean
            )
        absolute_error = np.abs(difference)
        worst_flat = int(np.argmax(absolute_error)) if absolute_error.size else 0
        worst_sensor, worst_hour = np.unravel_index(
            worst_flat, absolute_error.shape
        )
        per_sensor_maximum = np.max(absolute_error, axis=1)
        metric_results = {}
        for metric in METRICS:
            foton_values = _metric_values(foton_root, metric, grid_id)
            radiance_values = _metric_values(
                radiance_root, metric, grid_id
            )
            metric_error = np.abs(foton_values - radiance_values)
            metric_results[metric] = {
                "mean_absolute_error_percentage_points": float(
                    np.mean(metric_error)
                ),
                "maximum_error_percentage_points": float(
                    np.max(metric_error, initial=0)
                ),
                "passed": bool(np.mean(metric_error) < 2.0),
            }
        area_weights = (
            _grid_area_weights(prepared, grid_index)
            if prepared is not None
            else np.ones(count, dtype=np.float64)
        )
        foton_da = _metric_values(foton_root, "da", grid_id)
        radiance_da = _metric_values(radiance_root, "da", grid_id)
        foton_sda = _sda(foton_da, area_weights)
        radiance_sda = _sda(radiance_da, area_weights)
        sda_difference = abs(foton_sda - radiance_sda)
        grids.append(
            {
                "identifier": grid_id,
                "sensor_count": count,
                "raw_shape": list(foton_raw.shape),
                "illuminance": {
                    "nmbe_percent": nmbe,
                    "cvrmse_percent": cvrmse,
                    "absolute_error_lux": {
                        "p50": float(np.percentile(absolute_error, 50)),
                        "p90": float(np.percentile(absolute_error, 90)),
                        "p95": float(np.percentile(absolute_error, 95)),
                        "p99": float(np.percentile(absolute_error, 99)),
                        "maximum": float(
                            np.max(absolute_error, initial=0)
                        ),
                    },
                    "per_sensor_maximum_error_lux": {
                        "p50": float(np.percentile(per_sensor_maximum, 50)),
                        "p90": float(np.percentile(per_sensor_maximum, 90)),
                        "p95": float(np.percentile(per_sensor_maximum, 95)),
                        "p99": float(np.percentile(per_sensor_maximum, 99)),
                        "maximum": float(
                            np.max(per_sensor_maximum, initial=0)
                        ),
                    },
                    "worst": {
                        "sensor_index": int(worst_sensor),
                        "sun_up_hour_index": int(worst_hour),
                        "hour_of_year": float(foton_hours[worst_hour]),
                        "foton_lux": float(
                            foton_raw[worst_sensor, worst_hour]
                        ),
                        "radiance_lux": float(
                            radiance_raw[worst_sensor, worst_hour]
                        ),
                    },
                    "passed": bool(abs(nmbe) < 5.0 and cvrmse < 10.0),
                },
                "metrics": metric_results,
                "sda": {
                    "foton_percent": foton_sda,
                    "radiance_percent": radiance_sda,
                    "difference_percentage_points": sda_difference,
                    "passed": bool(sda_difference < 2.0),
                },
            }
        )

    speedup = (
        float(radiance_seconds) / float(foton_seconds)
        if radiance_seconds and foton_seconds
        else None
    )
    performance = {
        "foton_seconds": foton_seconds,
        "radiance_seconds": radiance_seconds,
        "speedup": speedup,
        "passed": None if speedup is None else bool(speedup >= 10.0),
    }
    passed = (
        all(structural.values())
        and official_loader["passed"]
        and all(
            grid["illuminance"]["passed"]
            and grid["sda"]["passed"]
            and all(
                result["passed"] for result in grid["metrics"].values()
            )
            for grid in grids
        )
        and performance["passed"] is not False
    )
    report = {
        "schema_version": 1,
        "passed": bool(passed),
        "structural": structural,
        "official_loader": official_loader,
        "grids": grids,
        "performance": performance,
        "versions": {
            "python": sys.version.split()[0],
            "platform": platform.platform(),
        },
        "folders": {
            "foton": str(foton_root),
            "radiance": str(radiance_root),
        },
    }
    if output_folder is not None:
        output = Path(output_folder).expanduser().resolve()
        output.mkdir(parents=True, exist_ok=True)
        (output / "comparison.json").write_text(
            json.dumps(report, indent=2, sort_keys=True), encoding="utf-8"
        )
        (output / "comparison.md").write_text(
            _markdown_report(report), encoding="utf-8"
        )
    return report


def _results_folder(root):
    candidate = root / "results"
    return candidate if candidate.is_dir() else root


def _metric_values(root, metric, grid_id):
    extension = "da" if metric == "da" else "cda" if metric == "cda" else "udi"
    return np.atleast_1d(
        np.loadtxt(root / "metrics" / metric / f"{grid_id}.{extension}")
    )


def _grid_area_weights(prepared, grid_index):
    info = prepared.grid_info[grid_index]
    start = int(info["start_sensor_index"])
    end = start + int(info["sensor_count"])
    return prepared.arrays["sensor_area_weights"][start:end].astype(np.float64)


def _sda(da, weights):
    return 100.0 * float(np.sum(weights[da >= 50])) / float(np.sum(weights))


def _json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def _markdown_report(report):
    lines = [
        "# Foton / Honeybee Radiance annual-daylight comparison",
        "",
        f"Overall: **{'PASS' if report['passed'] else 'FAIL'}**",
        "",
        "| Grid | NMBE | CV(RMSE) | sDA Δ | Raw gate | Metric gates |",
        "|---|---:|---:|---:|:---:|:---:|",
    ]
    for grid in report["grids"]:
        metrics_pass = all(
            value["passed"] for value in grid["metrics"].values()
        )
        lines.append(
            f"| {grid['identifier']} | "
            f"{grid['illuminance']['nmbe_percent']:.3f}% | "
            f"{grid['illuminance']['cvrmse_percent']:.3f}% | "
            f"{grid['sda']['difference_percentage_points']:.3f} pp | "
            f"{'PASS' if grid['illuminance']['passed'] else 'FAIL'} | "
            f"{'PASS' if metrics_pass else 'FAIL'} |"
        )
    speedup = report["performance"]["speedup"]
    if speedup is not None:
        lines.extend(("", f"End-to-end speedup: **{speedup:.2f}×**"))
    return "\n".join(lines) + "\n"
