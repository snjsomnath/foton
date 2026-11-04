"""Run the Honeybee recipes behind ``foton-honeybee`` and its background worker.

The one-shot commands (``annual-daylight``, ``daylight-factor``) and the
``serve`` worker share these functions, so a result written by either is the
same. The worker passes in a resident :class:`HoneybeeStudy`; the one-shot
commands build a fresh one.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable

from foton_bridge import backend_identifier, portable_manifest, reuse_identity

from .annual import DEFAULT_MAXIMUM_BOUNCES, QUALITY_PRESETS, HoneybeeStudy
from .protocol import (
    PROTOCOL_NAME,
    PROTOCOL_VERSION,
    annual_manifest,
    annual_request,
    input_file_fingerprint,
)

Progress = Callable[[dict[str, Any]], None]

ANNUAL_DEFAULTS = {
    "schedule": None,
    "backend": "auto",
    "grid_filter": "*",
    "north": 0.0,
    "quality": "final",
    "sky_density": 1,
    "threshold": 300.0,
    "udi_lower": 100.0,
    "udi_upper": 3000.0,
    "target_time": 50.0,
    "direct_samples": None,
    "maximum_samples": None,
    "maximum_bounces": DEFAULT_MAXIMUM_BOUNCES,
    "scene_seed": 0,
    "radiance_bin": None,
    "sky_source": "foton",
    "export_illuminance": True,
}
DAYLIGHT_FACTOR_DEFAULTS = {
    "backend": "auto",
    "grid_filter": "*",
    "quality": "final",
    "sky_density": 1,
    "direct_samples": None,
    "maximum_samples": None,
    "maximum_bounces": DEFAULT_MAXIMUM_BOUNCES,
    "scene_seed": 0,
}
METRIC_NAMES = ("da", "cda", "udi_lower", "udi", "udi_upper")


def _options(defaults, options):
    unknown = set(options) - set(defaults) - {"model", "wea", "output"}
    if unknown:
        raise ValueError("unknown option(s): " + ", ".join(sorted(unknown)))
    merged = dict(defaults)
    merged.update({key: value for key, value in options.items() if value is not None})
    if not merged.get("model"):
        raise ValueError("a model is required")
    return merged


def new_study(options) -> HoneybeeStudy:
    return HoneybeeStudy(
        options["model"],
        backend=options.get("backend", "auto"),
        grid_filter=options.get("grid_filter", "*"),
        radiance_bin=options.get("radiance_bin"),
        sky_source=options.get("sky_source", "foton"),
    )


def study_key(options) -> tuple:
    """What a resident study depends on: the model's bytes and scene options."""
    return (
        input_file_fingerprint(options["model"]),
        options.get("backend", "auto"),
        options.get("grid_filter", "*"),
        options.get("radiance_bin"),
        options.get("sky_source", "foton"),
    )


def annual_daylight(
    options: dict[str, Any],
    progress: Progress | None = None,
    study: HoneybeeStudy | None = None,
) -> dict[str, Any]:
    """Run annual daylight and return its manifest.

    With ``output`` set, the full Honeybee results folder and
    ``run_manifest.json`` are written exactly as ``foton-honeybee
    annual-daylight`` always has. Without it (the worker's live mode) nothing
    is written and the manifest carries the metric values inline.
    """
    options = _options(ANNUAL_DEFAULTS, options)
    if not options.get("wea"):
        raise ValueError("a weather file is required")
    output = options.get("output")
    _progress(progress, "preparation", 0.02, "Validating inputs and preparing the scene")
    if study is None:
        study = new_study(options)
    run = study.annual_daylight(
        options["wea"],
        schedule=options["schedule"],
        north=float(options["north"]),
        quality=options["quality"],
        sky_density=int(options["sky_density"]),
        threshold=float(options["threshold"]),
        udi_lower=float(options["udi_lower"]),
        udi_upper=float(options["udi_upper"]),
        target_time=float(options["target_time"]),
        direct_samples=options["direct_samples"],
        maximum_samples=options["maximum_samples"],
        maximum_bounces=int(options["maximum_bounces"]),
        scene_seed=int(options["scene_seed"]),
        output_folder=output,
        export_illuminance=bool(options["export_illuminance"]) and output is not None,
        progress=progress,
    )
    if output is None:
        return _live_manifest("annual_daylight", run, _annual_grid_values)

    request = annual_request(
        model=options["model"],
        wea=options["wea"],
        schedule=options["schedule"],
        backend=options["backend"],
        grid_filter=options["grid_filter"],
        north=options["north"],
        quality=options["quality"],
        sky_density=options["sky_density"],
        threshold=options["threshold"],
        udi_lower=options["udi_lower"],
        udi_upper=options["udi_upper"],
        target_time=options["target_time"],
        direct_samples=options["direct_samples"],
        maximum_samples=options["maximum_samples"],
        maximum_bounces=options["maximum_bounces"],
        scene_seed=options["scene_seed"],
        export_illuminance=options["export_illuminance"],
    )
    manifest = annual_manifest(run, output)
    manifest["request"] = request
    from foton import __version__

    solver = run.metadata.get("solver", {})
    manifest["reuse_identity"] = reuse_identity(
        request,
        {
            "quality_settings": QUALITY_PRESETS,
            "provenance": {
                "engine_version": __version__,
                "solver_revision": solver.get("solver_revision"),
                "selected_backend": backend_identifier(solver.get("backend")),
                "weather_version": run.metadata.get("weather", {}).get("sky_version"),
                "sky_source": run.metadata.get("weather", {}).get("sky_source"),
            },
        },
    )
    _add_common_warnings(manifest, options["quality"], solver.get("backend"))
    return _write_manifest(manifest, output)


def daylight_factor(
    options: dict[str, Any],
    progress: Progress | None = None,
    study: HoneybeeStudy | None = None,
) -> dict[str, Any]:
    """Run daylight factor and return its manifest (inline values without ``output``)."""
    options = _options(DAYLIGHT_FACTOR_DEFAULTS, options)
    output = options.get("output")
    _progress(progress, "preparation", 0.02, "Validating inputs and preparing the scene")
    if study is None:
        study = new_study(options)
    run = study.daylight_factor(
        quality=options["quality"],
        sky_density=int(options["sky_density"]),
        direct_samples=options["direct_samples"],
        maximum_samples=options["maximum_samples"],
        maximum_bounces=int(options["maximum_bounces"]),
        scene_seed=int(options["scene_seed"]),
        output_folder=output,
        progress=progress,
    )
    if output is None:
        return _live_manifest("daylight_factor", run, _df_grid_values)

    from foton import __version__

    root = Path(output).expanduser().resolve()
    grids = []
    for grid in run.grids:
        grids.append(
            {
                "identifier": grid.identifier,
                "full_identifier": grid.full_identifier,
                "room_identifier": grid.room_identifier,
                "sensor_count": grid.sensor_count,
                "start_sensor_index": int(grid.sensor_indices[0]),
                "mean_df": grid.mean,
                "metrics": {
                    "df": str(run.results_folder / f"{grid.full_identifier}.res")
                },
            }
        )
    manifest = {
        "protocol": PROTOCOL_NAME,
        "protocol_version": PROTOCOL_VERSION,
        "recipe": "daylight_factor",
        "status": "complete",
        "output_folder": str(root),
        "results_folder": str(run.results_folder),
        "grid_summary": str(root / "grid_summary.csv"),
        "metadata": str(root / "metadata.json"),
        "grids": grids,
        "versions": {
            "engine": __version__,
            "solver_revision": run.metadata["solver"]["solver_revision"],
            "protocol": PROTOCOL_VERSION,
        },
        "warnings": list(run.metadata.get("validation_warnings", [])),
        "timings": run.timings,
        "request": {
            key: options[key] for key in DAYLIGHT_FACTOR_DEFAULTS
        },
    }
    _add_common_warnings(manifest, options["quality"], run.metadata["solver"]["backend"])
    return _write_manifest(manifest, output)


def _add_common_warnings(manifest, quality, backend):
    if quality == "preview":
        manifest["warnings"].append("Preview quality: use final quality for reported results.")
    if backend_identifier(backend) == "reference":
        manifest["warnings"].append(
            "CPU reference fallback selected; GPU performance is unavailable."
        )


def _write_manifest(manifest, output):
    manifest_path = Path(output).expanduser().resolve() / "run_manifest.json"
    manifest["manifest"] = str(manifest_path)
    temporary = manifest_path.with_suffix(".tmp")
    temporary.write_text(
        json.dumps(
            portable_manifest(manifest, str(manifest_path.parent)),
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    temporary.replace(manifest_path)
    return manifest


def _rounded(values, digits=2):
    # The same decimals the result files carry, so live and saved runs agree.
    text = "%." + str(digits) + "f"
    return [float(text % value) for value in values.tolist()]


def _annual_grid_values(grid):
    return {
        "sda": float(grid.sda),
        "values": {name: _rounded(getattr(grid, name)) for name in METRIC_NAMES},
    }


def _df_grid_values(grid):
    return {"mean_df": grid.mean, "values": {"df": _rounded(grid.values, 4)}}


def _live_manifest(recipe, run, values):
    manifest = {
        "protocol": PROTOCOL_NAME,
        "protocol_version": PROTOCOL_VERSION,
        "recipe": recipe,
        "status": "complete",
        "live": True,
        "output_folder": None,
        "results_folder": None,
        "grids": [],
        "warnings": list(run.metadata.get("validation_warnings", [])),
        "timings": run.timings,
    }
    for grid in run.grids:
        entry = {
            "identifier": grid.identifier,
            "full_identifier": grid.full_identifier,
            "room_identifier": grid.room_identifier,
            "sensor_count": grid.sensor_count,
        }
        entry.update(values(grid))
        manifest["grids"].append(entry)
    solver = run.metadata.get("solver", {})
    _add_common_warnings(manifest, solver.get("quality"), solver.get("backend"))
    return manifest


def _progress(callback, stage, value, message):
    if callback is not None:
        callback({"stage": stage, "progress": float(value), "message": message})
