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
