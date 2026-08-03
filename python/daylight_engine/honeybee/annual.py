"""Reusable Honeybee annual-daylight studies and compatible result folders."""

from __future__ import annotations

import csv
from dataclasses import dataclass
import json
from pathlib import Path
import time
from typing import Any, Iterable

import numpy as np

from .adapter import PreparedHoneybeeScene, prepare_honeybee_scene
from .settings import RecipeSettings
from .weather import AnnualWeather, prepare_annual_weather


PHOTOPIC_WEIGHTS = np.asarray([47.435, 119.93, 11.635], dtype=np.float32)
DEFAULT_THRESHOLD_LUX = 300.0
DEFAULT_UDI_LOWER_LUX = 100.0
DEFAULT_UDI_UPPER_LUX = 3000.0
DEFAULT_TIME_FRACTION = 0.5
SOLVER_REVISION = "radiance-glass-reflection-v3"
QUALITY_PRESETS = {
    "preview": {"direct_samples": 1, "maximum_samples": 64},
    "final": {"direct_samples": 64, "maximum_samples": 4096},
}


@dataclass(frozen=True)
class GridAnnualResult:
    """Sensor-ordered annual metrics for one Honeybee SensorGrid."""

    identifier: str
    full_identifier: str
    room_identifier: str
    sensor_indices: np.ndarray
    area_weights: np.ndarray
    da: np.ndarray
    cda: np.ndarray
    udi_lower: np.ndarray
    udi: np.ndarray
    udi_upper: np.ndarray
    sda: float

    @property
    def sensor_count(self) -> int:
        return int(self.sensor_indices.size)


@dataclass(frozen=True)
class AnnualDaylightRun:
    """Completed annual-daylight analysis grouped in HBJSON grid order."""

    grids: tuple[GridAnnualResult, ...]
    timings: dict[str, float | None]
    results_folder: Path | None
    metadata: dict[str, Any]

    def grid(self, identifier: str) -> GridAnnualResult:
        """Return a grid by identifier or full identifier."""
        matches = [
            grid
            for grid in self.grids
            if identifier in {grid.identifier, grid.full_identifier}
        ]
        if not matches:
            raise KeyError(f"no result grid has identifier {identifier!r}")
        if len(matches) > 1:
            raise KeyError(f"grid identifier {identifier!r} is ambiguous")
        return matches[0]


class HoneybeeStudy:
    """Prepared Honeybee model with a resident native scene and coefficient cache."""

    def __init__(
        self,
        model,
        *,
        backend: str = "auto",
        grid_filter: str = "*",
        grid_size: float = 0.5,
        sensor_height: float = 0.75,
        radiance_bin: str | None = None,
        weather_cache: str | Path | None = None,
    ) -> None:
        started = time.perf_counter()
        self.model_input = model
        self.backend = backend
        self.grid_filter = grid_filter
        self.radiance_bin = radiance_bin
        self.weather_cache = weather_cache
        self.prepared: PreparedHoneybeeScene = prepare_honeybee_scene(
            model,
            grid_filter=grid_filter,
            grid_size=grid_size,
            sensor_height=sensor_height,
            include_aperture_glazing=True,
        )
        from foton import Engine

        self.engine = Engine({"backend": backend})
        self.capabilities = dict(self.engine.capabilities())
        self.scene = self.prepared.create_native_scene(self.engine)
        self._preparation_seconds = time.perf_counter() - started
        self._coefficient_cache: dict[tuple[Any, ...], np.ndarray] = {}
        self._run_count = 0

    def annual_daylight(
        self,
        wea,
        *,
        schedule=None,
        north: float = 0,
        quality: str = "final",
        threshold: float = DEFAULT_THRESHOLD_LUX,
        udi_lower: float = DEFAULT_UDI_LOWER_LUX,
        udi_upper: float = DEFAULT_UDI_UPPER_LUX,
        target_time: float = 50,
        sky_density: int = 1,
        direct_samples: int | None = None,
        maximum_samples: int | None = None,
        maximum_bounces: int = 1,
        scene_seed: int = 0,
        output_folder: str | Path | None = None,
        export_illuminance: bool = False,
        binary_schedule: bool = True,
    ) -> AnnualDaylightRun:
        """Run or re-reduce an annual study using Honeybee metric semantics."""
        run_started = time.perf_counter()
        threshold, udi_lower, udi_upper, time_fraction = _metric_parameters(
            threshold, udi_lower, udi_upper, target_time
        )
        if quality not in QUALITY_PRESETS:
            raise ValueError("quality must be 'preview' or 'final'")
        if direct_samples is None:
            direct_samples = QUALITY_PRESETS[quality]["direct_samples"]
        if maximum_samples is None:
            maximum_samples = QUALITY_PRESETS[quality]["maximum_samples"]
        if isinstance(direct_samples, bool) or int(direct_samples) <= 0:
            raise ValueError("direct_samples must be a positive integer")
        if isinstance(maximum_samples, bool) or int(maximum_samples) < 0:
            raise ValueError("maximum_samples must be a non-negative integer")
        direct_samples = int(direct_samples)
        maximum_samples = int(maximum_samples)
        occupancy = honeybee_schedule(schedule, binary=binary_schedule)

        weather_started = time.perf_counter()
        weather = prepare_annual_weather(
            wea,
            north=north,
            sky_density=sky_density,
            radiance_bin=self.radiance_bin,
            cache_directory=self.weather_cache,
        )
        weather_seconds = time.perf_counter() - weather_started

        cache_key = (
            self.prepared.model_fingerprint,
            self.prepared.geometry_info["material_fingerprint"],
            weather.basis,
            quality,
            direct_samples,
            maximum_samples,
            int(maximum_bounces),
            int(scene_seed),
            SOLVER_REVISION,
        )
        coefficients = self._coefficient_cache.get(cache_key)
        engine_timings: dict[str, float] = {}
        reduction_started = time.perf_counter()
        if coefficients is None:
            job = self.scene.analyze(
                weather.sky,
                occupancy,
                quality=quality,
                metrics=[
                    "da",
                    "cda",
                    "udi_lower",
                    "udi",
                    "udi_upper",
                    "static_sda300_50",
                ],
                threshold_lux=threshold,
                udi_lower_lux=udi_lower,
                udi_upper_lux=udi_upper,
                time_fraction=time_fraction,
                direct_samples=direct_samples,
                maximum_samples=maximum_samples,
                maximum_bounces=int(maximum_bounces),
                scene_seed=int(scene_seed),
                export_coefficients=True,
                export_illuminance=export_illuminance,
            )
            native = job.result()
            coefficients = np.ascontiguousarray(
                native.coefficients(), dtype=np.float32
            )
            self._coefficient_cache[cache_key] = coefficients
            metrics = _native_metrics(native)
            engine_timings = _native_timings(native)
            annual_illuminance = (
                np.asarray(native.annual_illuminance(), dtype=np.float32)
                if export_illuminance
                else None
            )
            coefficient_cache_hit = False
        else:
            native = self.scene.analyze(
                weather.sky,
                occupancy,
                quality=quality,
                metrics=[
                    "da",
                    "cda",
                    "udi_lower",
                    "udi",
                    "udi_upper",
                    "static_sda300_50",
                ],
                threshold_lux=threshold,
                udi_lower_lux=udi_lower,
                udi_upper_lux=udi_upper,
                time_fraction=time_fraction,
                direct_samples=direct_samples,
                maximum_samples=maximum_samples,
                maximum_bounces=int(maximum_bounces),
                scene_seed=int(scene_seed),
                export_coefficients=False,
                export_illuminance=export_illuminance,
                coefficient_override=coefficients,
            ).result()
            metrics = _native_metrics(native)
            engine_timings = _native_timings(native)
            annual_illuminance = (
                np.asarray(native.annual_illuminance(), dtype=np.float32)
                if export_illuminance
                else None
            )
            coefficient_cache_hit = True
        reduction_seconds = time.perf_counter() - reduction_started

        grids = _group_grid_metrics(
            self.prepared,
            metrics,
            target_time=float(target_time),
        )
        write_started = time.perf_counter()
        write_timings = {"raw_export_seconds": 0.0}
        results_folder = None
        if output_folder is not None:
            output = Path(output_folder).expanduser().resolve()
            results_folder = output / "results"
            write_timings = _write_run(
                output,
                self.prepared,
                grids,
                annual_illuminance,
                weather,
                occupancy,
                export_illuminance=export_illuminance,
                threshold=threshold,
                udi_lower=udi_lower,
                udi_upper=udi_upper,
                target_time=float(target_time),
                backend=self.capabilities,
                coefficient_cache_hit=coefficient_cache_hit,
            )
        write_seconds = time.perf_counter() - write_started

        run_seconds = time.perf_counter() - run_started
        timings = {
            "study_preparation_seconds": self._preparation_seconds,
            "weather_seconds": weather_seconds,
            "metric_reduction_seconds": reduction_seconds,
            "write_seconds": write_seconds,
            "total_seconds": run_seconds,
            "cold_end_to_end_seconds": (
                self._preparation_seconds + run_seconds
                if self._run_count == 0
                else None
            ),
            "warm_study_seconds": (
                run_seconds if self._run_count > 0 else None
            ),
            **write_timings,
            **engine_timings,
        }
        metadata = _run_metadata(
            self.prepared,
            weather,
            occupancy,
            threshold=threshold,
            udi_lower=udi_lower,
            udi_upper=udi_upper,
            target_time=float(target_time),
            quality=quality,
            sky_density=int(sky_density),
            direct_samples=direct_samples,
            maximum_samples=maximum_samples,
            maximum_bounces=int(maximum_bounces),
            scene_seed=int(scene_seed),
            backend=self.capabilities,
            coefficient_cache_hit=coefficient_cache_hit,
            export_illuminance=export_illuminance,
            timings=timings,
            output_size_bytes=(
                _directory_size(Path(output_folder).expanduser().resolve())
                if output_folder is not None
                else 0
            ),
            peak_memory_bytes=_peak_memory_bytes(),
        )
        if output_folder is not None:
            output = Path(output_folder).expanduser().resolve()
            (output / "metadata.json").write_text(
                json.dumps(metadata, indent=2, sort_keys=True), encoding="utf-8"
            )
        self._run_count += 1
        return AnnualDaylightRun(
            grids=grids,
            timings=timings,
            results_folder=results_folder,
            metadata=metadata,
        )


def run_annual_daylight(
    *,
    model,
    wea,
    output_folder: str | Path | None = None,
    backend: str = "auto",
    grid_filter: str = "*",
    schedule=None,
    north: float = 0,
    quality: str = "final",
    sky_density: int = 1,
    export_illuminance: bool = False,
    **kwargs,
) -> AnnualDaylightRun:
    """One-call convenience wrapper around :class:`HoneybeeStudy`."""
    study = HoneybeeStudy(
        model,
        backend=backend,
        grid_filter=grid_filter,
        radiance_bin=kwargs.pop("radiance_bin", None),
        weather_cache=kwargs.pop("weather_cache", None),
    )
    return study.annual_daylight(
        wea,
        schedule=schedule,
        north=north,
        quality=quality,
        sky_density=sky_density,
        output_folder=output_folder,
        export_illuminance=export_illuminance,
        **kwargs,
    )


class AnnualDaylightRecipe:
    """LBT-style recipe facade for Foton's annual-daylight study."""

    _input_names = (
        "model",
        "wea",
        "backend",
        "grid_filter",
        "schedule",
        "north",
        "quality",
        "sky_density",
        "direct_samples",
        "maximum_samples",
        "maximum_bounces",
        "threshold",
        "udi_lower",
        "udi_upper",
        "target_time",
        "radiance_bin",
        "export_illuminance",
    )
    _output_names = ("results", "metrics", "grid_summary", "metadata")

    def __init__(self) -> None:
        self._name = "annual_daylight"
        self._inputs = {
            "model": None,
            "wea": None,
            "backend": "auto",
            "grid_filter": "*",
            "schedule": None,
            "north": 0.0,
            "quality": "final",
            "sky_density": 1,
            "direct_samples": None,
            "maximum_samples": None,
            "maximum_bounces": 1,
            "threshold": 300.0,
            "udi_lower": 100.0,
            "udi_upper": 3000.0,
            "target_time": 50.0,
            "radiance_bin": None,
            "export_illuminance": True,
        }
        self._project_folder: Path | None = None
        self._simulation_id: str | None = None

    @property
    def name(self):
        return self._name

    @property
    def tag(self):
        return "foton"

    @property
    def path(self):
        return str(Path(__file__).resolve().parent)

    @property
    def default_project_folder(self):
        return str(Path.cwd() / "foton")

    @property
    def simulation_id(self):
        return self._simulation_id

    @property
    def inputs(self):
        return dict(self._inputs)

    @property
    def outputs(self):
        return list(self._output_names)

    @property
    def input_names(self):
        return list(self._input_names)

    @property
    def output_names(self):
        return list(self._output_names)

    def input_value_by_name(self, input_name, input_value):
        name = str(input_name).strip().lower().replace("-", "_").replace(" ", "_")
        if name not in self._inputs:
            raise ValueError(
                f"unknown input {input_name!r}; expected {', '.join(self._input_names)}"
            )
        if name == "backend" and input_value not in {
            "auto",
            "metal",
            "vulkan",
            "reference",
            "cpu",
        }:
            raise ValueError("invalid Foton backend")
        if name == "quality" and input_value not in {"preview", "final"}:
            raise ValueError("quality must be 'preview' or 'final'")
        if (
            name == "sky_density"
            and (
                isinstance(input_value, bool)
                or input_value not in {1, 2}
            )
        ):
            raise ValueError("sky_density must be 1 or 2")
        if name in {"direct_samples", "maximum_samples"} and input_value is not None:
            minimum = 1 if name == "direct_samples" else 0
            if isinstance(input_value, bool) or int(input_value) < minimum:
                raise ValueError(f"{name} must be at least {minimum}")
        if name == "maximum_bounces" and (
            isinstance(input_value, bool) or int(input_value) < 0
        ):
            raise ValueError("maximum_bounces must be non-negative")
        self._inputs[name] = input_value

    def output_value_by_name(self, output_name, project_folder=None):
        name = str(output_name).strip().lower().replace("-", "_")
        if name not in self._output_names:
            raise ValueError(f"unknown output {output_name!r}")
        project = (
            Path(project_folder)
            if project_folder is not None
            else self._project_folder
        )
        if project is None:
            raise RuntimeError("run the recipe before requesting outputs")
        return str(
            {
                "results": project / "results",
                "metrics": project / "metrics",
                "grid_summary": project / "grid_summary.csv",
                "metadata": project / "metadata.json",
            }[name]
        )

    def run(
        self,
        settings=None,
        radiance_check=False,
        openstudio_check=False,
        energyplus_check=False,
        queenbee_path=None,
        silent=False,
        debug_folder=None,
    ):
        del radiance_check, openstudio_check, energyplus_check
        del queenbee_path, silent, debug_folder
        settings = settings or RecipeSettings()
        if not isinstance(settings, RecipeSettings):
            raise TypeError("settings must be a RecipeSettings instance")
        if self._inputs["model"] is None or self._inputs["wea"] is None:
            raise ValueError("annual_daylight requires both 'model' and 'wea'")
        root = Path(settings.folder or self.default_project_folder).expanduser()
        model_name = Path(str(self._inputs["model"])).stem or "model"
        self._simulation_id = f"{model_name}-annual-daylight"
        self._project_folder = root.resolve() / self._simulation_id
        run_annual_daylight(
            model=self._inputs["model"],
            wea=self._inputs["wea"],
            output_folder=self._project_folder,
            backend=self._inputs["backend"],
            grid_filter=self._inputs["grid_filter"],
            schedule=self._inputs["schedule"],
            north=float(self._inputs["north"]),
            quality=self._inputs["quality"],
            sky_density=int(self._inputs["sky_density"]),
            direct_samples=self._inputs["direct_samples"],
            maximum_samples=self._inputs["maximum_samples"],
            maximum_bounces=int(self._inputs["maximum_bounces"]),
            threshold=float(self._inputs["threshold"]),
            udi_lower=float(self._inputs["udi_lower"]),
            udi_upper=float(self._inputs["udi_upper"]),
            target_time=float(self._inputs["target_time"]),
            radiance_bin=self._inputs["radiance_bin"],
            export_illuminance=bool(self._inputs["export_illuminance"]),
        )
        return str(self._project_folder)


def honeybee_schedule(schedule=None, *, binary: bool = True) -> np.ndarray:
    """Return an hourly schedule, binarizing values at Honeybee's 0.1 cutoff."""
    if schedule is None:
        hours = np.arange(8760, dtype=np.uint32) % 24
        values = ((hours >= 8) & (hours < 18)).astype(np.float32)
    elif isinstance(schedule, (str, Path)):
        path = Path(schedule).expanduser().resolve()
        values = np.loadtxt(path, delimiter="," if path.suffix.lower() == ".csv" else None)
    elif hasattr(schedule, "values"):
        values = np.asarray(schedule.values, dtype=np.float32)
    else:
        values = np.asarray(schedule, dtype=np.float32)
    values = np.ravel(values)
    if values.size != 8760:
        raise ValueError(f"schedule has {values.size} values; expected 8760")
    if not np.isfinite(values).all() or np.any(values < 0):
        raise ValueError("schedule values must be finite and non-negative")
    if binary:
        values = (values >= 0.1).astype(np.float32)
    if float(np.sum(values)) <= 0:
        raise ValueError("schedule must contain at least one occupied hour")
    return np.ascontiguousarray(values, dtype=np.float32)


def _metric_parameters(threshold, lower, upper, target_time):
    values = tuple(float(value) for value in (threshold, lower, upper, target_time))
    threshold, lower, upper, target_time = values
    if (
        not all(np.isfinite(values))
        or threshold <= 0
        or lower < 0
        or upper <= lower
        or not 0 <= target_time <= 100
    ):
        raise ValueError("annual daylight thresholds or target_time are invalid")
    return threshold, lower, upper, target_time / 100.0


def _native_metrics(result):
    return {
        "da": 100.0
        * np.asarray(result.daylight_autonomy(), dtype=np.float32),
        "cda": 100.0
        * np.asarray(result.continuous_daylight_autonomy(), dtype=np.float32),
        "udi_lower": 100.0
        * np.asarray(
            result.useful_daylight_illuminance_lower(), dtype=np.float32
        ),
        "udi": 100.0
        * np.asarray(result.useful_daylight_illuminance(), dtype=np.float32),
        "udi_upper": 100.0
        * np.asarray(
            result.useful_daylight_illuminance_upper(), dtype=np.float32
        ),
    }


def _native_timings(result):
    return {
        f"engine_{key[:-3]}_seconds": float(value) / 1000.0
        for key, value in dict(result.timings()).items()
        if key.endswith("_ms")
    }


def _reduce_coefficients(
    coefficients,
    sky,
    occupancy,
    *,
    threshold,
    udi_lower,
    udi_upper,
    sensor_chunk=64,
):
    occupied = np.flatnonzero(occupancy > 0)
    occupied_weight = float(np.sum(occupancy[occupied]))
    selected_sky = sky[:, occupied, :]
    selected_weights = occupancy[occupied][None, :]
    sensor_count = coefficients.shape[0]
    output = {
        name: np.zeros(sensor_count, dtype=np.float32)
        for name in ("da", "cda", "udi_lower", "udi", "udi_upper")
    }
    for start in range(0, sensor_count, sensor_chunk):
        end = min(start + sensor_chunk, sensor_count)
        illuminance = np.einsum(
            "spr,ptr,r->st",
            coefficients[start:end],
            selected_sky,
            PHOTOPIC_WEIGHTS,
            optimize=True,
        )
        output["da"][start:end] = (
            100.0
            * np.sum((illuminance >= threshold) * selected_weights, axis=1)
            / occupied_weight
        )
        output["cda"][start:end] = (
            100.0
            * np.sum(
                np.minimum(illuminance / threshold, 1.0) * selected_weights,
                axis=1,
            )
            / occupied_weight
        )
        output["udi_lower"][start:end] = (
            100.0
            * np.sum((illuminance < udi_lower) * selected_weights, axis=1)
            / occupied_weight
        )
        output["udi"][start:end] = (
            100.0
            * np.sum(
                ((illuminance >= udi_lower) & (illuminance <= udi_upper))
                * selected_weights,
                axis=1,
            )
            / occupied_weight
        )
        output["udi_upper"][start:end] = (
            100.0
            * np.sum((illuminance > udi_upper) * selected_weights, axis=1)
            / occupied_weight
        )
    return output


def _group_grid_metrics(prepared, metrics, *, target_time):
    room_by_id = {value: key for key, value in prepared.room_map.items()}
    weights = prepared.arrays["sensor_area_weights"]
    grids = []
    for info in prepared.grid_info:
        start = int(info["start_sensor_index"])
        end = start + int(info["sensor_count"])
        indices = np.arange(start, end, dtype=np.uint32)
        grid_weights = np.asarray(weights[start:end], dtype=np.float32)
        da = np.asarray(metrics["da"][start:end], dtype=np.float32)
        represented_area = float(np.sum(grid_weights))
        sda = (
            100.0
            * float(np.sum(grid_weights[da >= target_time]))
            / represented_area
        )
        room_ids = info["room_ids"]
        room_identifier = (
            room_by_id.get(room_ids[0], "")
            if len(room_ids) == 1
            else "<multiple>"
        )
        grids.append(
            GridAnnualResult(
                identifier=info["identifier"],
                full_identifier=info["full_identifier"],
                room_identifier=room_identifier,
                sensor_indices=indices,
                area_weights=grid_weights,
                da=da,
                cda=np.asarray(metrics["cda"][start:end], dtype=np.float32),
                udi_lower=np.asarray(
                    metrics["udi_lower"][start:end], dtype=np.float32
                ),
                udi=np.asarray(metrics["udi"][start:end], dtype=np.float32),
                udi_upper=np.asarray(
                    metrics["udi_upper"][start:end], dtype=np.float32
                ),
                sda=sda,
            )
        )
    return tuple(grids)


def _honeybee_grids_info(prepared, grids):
    return [
        {
            "name": grid.identifier,
            "identifier": grid.identifier,
            "full_id": grid.full_identifier,
            "count": grid.sensor_count,
            "group": grid.room_identifier,
            "room_identifier": grid.room_identifier,
            "start_sensor_index": int(grid.sensor_indices[0]),
            "light_path": [["__static_apertures__"]],
        }
        for grid in grids
    ]


def _write_run(
    output,
    prepared,
    grids,
    annual_illuminance,
    weather,
    occupancy,
    *,
    export_illuminance,
    threshold,
    udi_lower,
    udi_upper,
    target_time,
    backend,
    coefficient_cache_hit,
):
    raw_export_seconds = 0.0
    output.mkdir(parents=True, exist_ok=True)
    results = output / "results"
    metrics_folder = output / "metrics"
    results.mkdir(parents=True, exist_ok=True)
    metrics_folder.mkdir(parents=True, exist_ok=True)
    grids_info = _honeybee_grids_info(prepared, grids)
    encoded_info = json.dumps(grids_info, indent=2)
    (results / "grids_info.json").write_text(encoded_info, encoding="utf-8")
    np.savetxt(
        results / "sun-up-hours.txt",
        np.asarray(weather.sun_up_hours, dtype=np.float32),
        fmt="%.1f",
    )
    (results / "study_info.json").write_text(
        json.dumps(
            {"timestep": 1, "study_hours": list(range(8760))}, indent=2
        ),
        encoding="utf-8",
    )
    for metric_name, extension in (
        ("da", "da"),
        ("cda", "cda"),
        ("udi_lower", "udi"),
        ("udi", "udi"),
        ("udi_upper", "udi"),
    ):
        folder = metrics_folder / metric_name
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "grids_info.json").write_text(encoded_info, encoding="utf-8")
        for grid in grids:
            np.savetxt(
                folder / f"{grid.full_identifier}.{extension}",
                getattr(grid, metric_name),
                fmt="%.2f",
            )

    if export_illuminance:
        raw_started = time.perf_counter()
        raw_folder = (
            results
            / "__static_apertures__"
            / "default"
            / "total"
        )
        raw_folder.mkdir(parents=True, exist_ok=True)
        if annual_illuminance is None:
            raise RuntimeError("raw illuminance was not returned by the backend")
        sun_up_indices = np.asarray(weather.sun_up_hours, dtype=np.uint32)
        for grid in grids:
            start = int(grid.sensor_indices[0])
            end = start + grid.sensor_count
            grid_values = annual_illuminance[start:end][:, sun_up_indices]
            target = np.lib.format.open_memmap(
                raw_folder / f"{grid.full_identifier}.npy",
                mode="w+",
                dtype=np.float32,
                shape=(grid.sensor_count, len(weather.sun_up_hours)),
            )
            target[:] = grid_values
            if not np.any(grid_values):
                # The official loader skips metric calculation for an exactly
                # zero matrix. A positive subnormal remains physically zero at
                # daylight thresholds while preserving UDI-low evaluation.
                target[:] = np.finfo(np.float32).tiny
            target.flush()
            del target
        raw_export_seconds = time.perf_counter() - raw_started

    with (output / "grid_summary.csv").open(
        "w", newline="", encoding="utf-8"
    ) as stream:
        writer = csv.writer(stream)
        writer.writerow(
            (
                "grid",
                "room",
                "sensor_count",
                "mean_da",
                "mean_cda",
                "mean_udi_lower",
                "mean_udi",
                "mean_udi_upper",
                "sda",
            )
        )
        for grid in grids:
            writer.writerow(
                (
                    grid.full_identifier,
                    grid.room_identifier,
                    grid.sensor_count,
                    float(np.mean(grid.da)),
                    float(np.mean(grid.cda)),
                    float(np.mean(grid.udi_lower)),
                    float(np.mean(grid.udi)),
                    float(np.mean(grid.udi_upper)),
                    grid.sda,
                )
            )
    return {"raw_export_seconds": raw_export_seconds}


def _run_metadata(
    prepared,
    weather,
    occupancy,
    *,
    threshold,
    udi_lower,
    udi_upper,
    target_time,
    quality,
    sky_density,
    direct_samples,
    maximum_samples,
    maximum_bounces,
    scene_seed,
    backend,
    coefficient_cache_hit,
    export_illuminance,
    timings,
    output_size_bytes,
    peak_memory_bytes,
):
    return {
        "schema_version": 1,
        "recipe": "annual_daylight",
        "model_fingerprint": prepared.model_fingerprint,
        "model_identifier": prepared.model.identifier,
        "sensor_count": int(prepared.arrays["sensor_positions"].shape[0]),
        "grid_order": [item["identifier"] for item in prepared.grid_info],
        "geometry": prepared.geometry_info,
        "validation_warnings": list(prepared.validation_warnings),
        "weather": {
            "weather_id": weather.weather_id,
            "source": weather.source,
            "north": weather.north,
            "location": weather.location,
            "basis": weather.basis,
            "sky_density": sky_density,
            "sun_up_hour_count": len(weather.sun_up_hours),
            "cache_hit": weather.cache_hit,
            "gendaymtx": weather.gendaymtx,
            "gendaymtx_version": weather.gendaymtx_version,
        },
        "schedule": {
            "occupied_hours": float(np.sum(occupancy)),
            "binary_honeybee_semantics": bool(
                np.all((occupancy == 0) | (occupancy == 1))
            ),
        },
        "thresholds": {
            "da_lux": threshold,
            "udi_lower_lux": udi_lower,
            "udi_upper_lux": udi_upper,
            "sda_target_time_percent": target_time,
        },
        "solver": {
            "backend": backend,
            "quality": quality,
            "solver_revision": SOLVER_REVISION,
            "material_fingerprint": prepared.geometry_info[
                "material_fingerprint"
            ],
            "direct_samples": direct_samples,
            "maximum_samples": maximum_samples,
            "maximum_bounces": maximum_bounces,
            "scene_seed": scene_seed,
            "coefficient_cache_hit": coefficient_cache_hit,
        },
        "export_illuminance": export_illuminance,
        "resources": {
            "peak_memory_bytes": peak_memory_bytes,
            "output_size_bytes": output_size_bytes,
        },
        "timings": timings,
    }


def _directory_size(directory):
    return sum(
        path.stat().st_size
        for path in directory.rglob("*")
        if path.is_file()
    )


def _peak_memory_bytes():
    try:
        import resource
        import sys

        value = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        return value if sys.platform == "darwin" else value * 1024
    except (ImportError, OSError, ValueError):
        return None
