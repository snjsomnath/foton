"""Daylight factor for Honeybee models, in Honeybee's results layout."""

from __future__ import annotations

import csv
from dataclasses import dataclass
import json
from pathlib import Path
import time
from typing import Any, Callable

import numpy as np

from .annual import (
    DEFAULT_MAXIMUM_BOUNCES,
    HoneybeeStudy,
    SOLVER_REVISION,
    _report_progress,
    quality_preset,
)

SKY_BASIS = {1: "tregenza", 2: "reinhart-mf2"}
# Same photopic weights as the engine's own daylight factor (Radiance RGB).
_PHOTOPIC = np.asarray([0.265, 0.67, 0.065], dtype=np.float32)


@dataclass(frozen=True)
class GridDaylightFactor:
    """Sensor-ordered daylight factor for one Honeybee SensorGrid."""

    identifier: str
    full_identifier: str
    room_identifier: str
    sensor_indices: np.ndarray
    values: np.ndarray

    @property
    def sensor_count(self) -> int:
        """Number of sensors in this grid."""
        return int(self.sensor_indices.size)

    @property
    def mean(self) -> float:
        """Average daylight factor of the grid, in percent."""
        return float(np.mean(self.values))


@dataclass(frozen=True)
class DaylightFactorRun:
    """Completed daylight factor analysis grouped in HBJSON grid order."""

    grids: tuple[GridDaylightFactor, ...]
    timings: dict[str, float | None]
    results_folder: Path | None
    metadata: dict[str, Any]


def overcast_daylight_factor(coefficients: np.ndarray, basis: str) -> np.ndarray:
    """Per-sensor daylight factor (%) under a CIE overcast sky.

    Mirrors the engine's ``compute_daylight_factor``: patch luminance
    ``(1 + 2 sin(altitude)) / 3``, no ground patch, divided by the unobstructed
    horizontal illuminance of the same discretised sky.
    """
    from foton import sky_patch_directions, sky_patch_solid_angles

    directions = np.asarray(sky_patch_directions(basis), dtype=np.float32)
    solid_angles = np.asarray(sky_patch_solid_angles(basis), dtype=np.float32)
    height = np.maximum(directions[:, 2], 0.0)
    luminance = (1.0 + 2.0 * height) / 3.0
    luminance[0] = 0.0
    exterior = float(np.sum(luminance[1:] * height[1:] * solid_angles[1:]))
    interior = np.einsum(
        "spr,p,r->s", coefficients, luminance, _PHOTOPIC, optimize=True
    )
    return (100.0 * interior / exterior).astype(np.float32)


def daylight_factor_run(
    study: HoneybeeStudy,
    *,
    quality: str = "final",
    sky_density: int = 1,
    direct_samples: int | None = None,
    maximum_samples: int | None = None,
    maximum_bounces: int = DEFAULT_MAXIMUM_BOUNCES,
    scene_seed: int = 0,
    output_folder: str | Path | None = None,
    progress: Callable[[dict[str, Any]], None] | None = None,
) -> DaylightFactorRun:
    """Compute the daylight factor for every grid of a prepared study.

    Traces the sky coefficients (or reuses ones the study already traced with the
    same settings) and applies a CIE overcast sky. When ``output_folder`` is set
    the results are written in Honeybee's daylight factor layout.
    """
    started = time.perf_counter()
    if isinstance(sky_density, bool) or int(sky_density) not in SKY_BASIS:
        raise ValueError("sky_density must be 1 (Tregenza) or 2 (Reinhart MF:2)")
    sky_density = int(sky_density)
    preset = quality_preset(quality, sky_density)
    direct_samples = int(
        preset["direct_samples"] if direct_samples is None else direct_samples
    )
    maximum_samples = int(
        preset["maximum_samples"] if maximum_samples is None else maximum_samples
    )
    if direct_samples <= 0:
        raise ValueError("direct_samples must be a positive integer")
    if maximum_samples < 0:
        raise ValueError("maximum_samples must be a non-negative integer")
    if int(maximum_bounces) < 0:
        raise ValueError("maximum_bounces must be non-negative")
    basis = SKY_BASIS[sky_density]
    _report_progress(
        progress, "transport", 0.2, "Tracing direct and diffuse daylight coefficients"
    )
    coefficients, cache_hit, engine_timings = study._coefficients(
        basis=basis,
        quality=quality,
        direct_samples=direct_samples,
        maximum_samples=maximum_samples,
        maximum_bounces=int(maximum_bounces),
        scene_seed=int(scene_seed),
    )
    _report_progress(progress, "metrics", 0.8, "Daylight factor ready")
    values = overcast_daylight_factor(coefficients, basis)
    grids = _group_grids(study.prepared, values)

    write_started = time.perf_counter()
    results_folder = None
    if output_folder is not None:
        _report_progress(progress, "output", 0.9, "Writing result files")
        output = Path(output_folder).expanduser().resolve()
        results_folder = _write_results(output, grids)
    write_seconds = time.perf_counter() - write_started
    timings = {
        "study_preparation_seconds": study._preparation_seconds,
        "coefficient_trace_seconds": (
            0.0 if cache_hit else engine_timings.get("engine_tracing_seconds", 0.0)
        ),
        "write_seconds": write_seconds,
        "total_seconds": time.perf_counter() - started,
        **engine_timings,
    }
    metadata = {
        "schema_version": 1,
        "recipe": "daylight_factor",
        "sky": "CIE overcast, sky patches without ground",
        "model_fingerprint": study.prepared.model_fingerprint,
        "model_identifier": study.prepared.model.identifier,
        "sensor_count": int(values.size),
        "grid_order": [grid.identifier for grid in grids],
        "validation_warnings": list(study.prepared.validation_warnings),
        "solver": {
            "backend": study.capabilities,
            "quality": quality,
            "solver_revision": SOLVER_REVISION,
            "sky_basis": basis,
            "sky_density": sky_density,
            "direct_samples": direct_samples,
            "maximum_samples": maximum_samples,
            "maximum_bounces": int(maximum_bounces),
            "scene_seed": int(scene_seed),
            "coefficient_cache_hit": cache_hit,
        },
        "timings": timings,
    }
    if output_folder is not None:
        (Path(output_folder).expanduser().resolve() / "metadata.json").write_text(
            json.dumps(metadata, indent=2, sort_keys=True), encoding="utf-8"
        )
    _report_progress(progress, "output", 0.98, "Result manifest ready")
    return DaylightFactorRun(
        grids=grids,
        timings=timings,
        results_folder=results_folder,
        metadata=metadata,
    )


def run_daylight_factor(
    *,
    model,
    output_folder: str | Path | None = None,
    backend: str = "auto",
    grid_filter: str = "*",
    **kwargs,
) -> DaylightFactorRun:
    """One-call convenience wrapper around :meth:`HoneybeeStudy.daylight_factor`."""
    study = HoneybeeStudy(model, backend=backend, grid_filter=grid_filter)
    return study.daylight_factor(output_folder=output_folder, **kwargs)


def _group_grids(prepared, values):
    room_by_id = {value: key for key, value in prepared.room_map.items()}
    grids = []
    for info in prepared.grid_info:
        start = int(info["start_sensor_index"])
        end = start + int(info["sensor_count"])
        room_ids = info["room_ids"]
        grids.append(
            GridDaylightFactor(
                identifier=info["identifier"],
                full_identifier=info["full_identifier"],
                room_identifier=(
                    room_by_id.get(room_ids[0], "")
                    if len(room_ids) == 1
                    else "<multiple>"
                ),
                sensor_indices=np.arange(start, end, dtype=np.uint32),
                values=np.asarray(values[start:end], dtype=np.float32),
            )
        )
    return tuple(grids)


def _write_results(output: Path, grids) -> Path:
    """Write Honeybee's daylight-factor layout: one ``.res`` file per grid."""
    results = output / "results"
    results.mkdir(parents=True, exist_ok=True)
    grids_info = [
        {
            "name": grid.identifier,
            "identifier": grid.identifier,
            "full_id": grid.full_identifier,
            "count": grid.sensor_count,
            "group": grid.room_identifier,
            "room_identifier": grid.room_identifier,
            "start_sensor_index": int(grid.sensor_indices[0]),
        }
        for grid in grids
    ]
    (results / "grids_info.json").write_text(
        json.dumps(grids_info, indent=2), encoding="utf-8"
    )
    for grid in grids:
        (results / f"{grid.full_identifier}.res").write_text(
            "".join("%.4f\n" % value for value in grid.values.tolist()),
            encoding="latin-1",
            newline="\n",
        )
    with (output / "grid_summary.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(("grid", "room", "sensor_count", "mean_df", "min_df", "max_df"))
        for grid in grids:
            writer.writerow(
                (
                    grid.full_identifier,
                    grid.room_identifier,
                    grid.sensor_count,
                    grid.mean,
                    float(np.min(grid.values)),
                    float(np.max(grid.values)),
                )
            )
    return results
