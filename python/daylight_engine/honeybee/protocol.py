"""Versioned wire protocol for external Honeybee and Grasshopper clients."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
from typing import Any, TextIO


PROTOCOL_NAME = "foton.honeybee"
PROTOCOL_VERSION = 1


@dataclass
class ProtocolWriter:
    stream: TextIO
    sequence: int = 0

    def emit(self, event: str, **payload) -> dict[str, Any]:
        message = {
            "protocol": PROTOCOL_NAME,
            "protocol_version": PROTOCOL_VERSION,
            "sequence": self.sequence,
            "event": event,
            **payload,
        }
        self.sequence += 1
        self.stream.write(json.dumps(message, sort_keys=True) + "\n")
        self.stream.flush()
        return message


def input_file_fingerprint(path) -> str:
    digest = sha256()
    with Path(path).expanduser().resolve().open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def annual_request(
    *,
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
) -> dict[str, Any]:
    model_path = Path(model).expanduser().resolve()
    weather_path = Path(wea).expanduser().resolve()
    schedule_path = Path(schedule).expanduser().resolve() if schedule else None
    request = {
        "model": str(model_path),
        "model_sha256": input_file_fingerprint(model_path),
        "wea": str(weather_path),
        "wea_sha256": input_file_fingerprint(weather_path),
        "schedule": str(schedule_path) if schedule_path else None,
        "schedule_sha256": (
            input_file_fingerprint(schedule_path) if schedule_path else None
        ),
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
    compatibility_request = {
        key: value
        for key, value in request.items()
        if key not in {"model", "wea", "schedule"}
    }
    encoded = json.dumps(
        compatibility_request,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
    request["fingerprint"] = sha256(encoded).hexdigest()
    return request


def annual_manifest(run, output_folder) -> dict[str, Any]:
    from foton import __version__

    output = Path(output_folder).expanduser().resolve()
    results = Path(run.results_folder).resolve() if run.results_folder else None
    grids = []
    extensions = {
        "da": "da",
        "cda": "cda",
        "udi_lower": "udi",
        "udi": "udi",
        "udi_upper": "udi",
    }
    for grid in run.grids:
        metric_paths = {
            metric: str(
                output / "metrics" / metric / f"{grid.full_identifier}.{extension}"
            )
            for metric, extension in extensions.items()
        }
        raw_path = (
            results
            / "__static_apertures__"
            / "default"
            / "total"
            / f"{grid.full_identifier}.npy"
            if results is not None
            else None
        )
        grids.append(
            {
                "identifier": grid.identifier,
                "full_identifier": grid.full_identifier,
                "room_identifier": grid.room_identifier,
                "sensor_count": grid.sensor_count,
                "start_sensor_index": int(grid.sensor_indices[0]),
                "sda": float(grid.sda),
                "metrics": metric_paths,
                "raw_illuminance": (
                    str(raw_path)
                    if raw_path is not None and raw_path.is_file()
                    else None
                ),
            }
        )
    return {
        "protocol": PROTOCOL_NAME,
        "protocol_version": PROTOCOL_VERSION,
        "recipe": "annual_daylight",
        "status": "complete",
        "output_folder": str(output),
        "results_folder": str(results) if results is not None else None,
        "metrics_folder": str(output / "metrics"),
        "grid_summary": str(output / "grid_summary.csv"),
        "metadata": str(output / "metadata.json"),
        "grids": grids,
        "cache": {
            "weather_hit": bool(
                run.metadata.get("weather", {}).get("cache_hit", False)
            ),
            "coefficients_hit": bool(
                run.metadata.get("solver", {}).get(
                    "coefficient_cache_hit", False
                )
            ),
        },
        "versions": {
            "engine": __version__,
            "solver_revision": run.metadata.get("solver", {}).get(
                "solver_revision"
            ),
            "protocol": PROTOCOL_VERSION,
        },
        "warnings": list(run.metadata.get("validation_warnings", [])),
        "timings": run.timings,
    }


def parse_message(line: str) -> dict[str, Any]:
    try:
        message = json.loads(line)
    except json.JSONDecodeError as error:
        raise ValueError("Foton protocol line is not valid JSON") from error
    if not isinstance(message, dict):
        raise ValueError("Foton protocol message must be a JSON object")
    if message.get("protocol") != PROTOCOL_NAME:
        raise ValueError("message does not use the Foton Honeybee protocol")
    if message.get("protocol_version") != PROTOCOL_VERSION:
        raise ValueError(
            "unsupported Foton Honeybee protocol version "
            f"{message.get('protocol_version')!r}"
        )
    if not isinstance(message.get("event"), str):
        raise ValueError("Foton protocol message has no event")
    return message
