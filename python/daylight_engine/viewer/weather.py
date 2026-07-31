"""EPW validation and cached Radiance Perez sky generation."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
from typing import Any

import numpy as np
from platformdirs import user_cache_path

from foton import sky_patch_directions, sky_patch_solid_angles


BASES = {
    "tregenza": {"multiplier": 1, "rows": 146},
    "final": {"multiplier": 2, "rows": 578},
}
MAXIMUM_EPW_BYTES = 32 * 1024 * 1024
PHOTOPIC_WEIGHTS = np.asarray([47.435, 119.93, 11.635], dtype=np.float64)
DEMO_EXTERIOR_ILLUMINANCE_LUX = 10_000.0


def occupancy_schedule(timestep_count: int) -> np.ndarray:
    if timestep_count != 8760:
        raise ValueError("the viewer requires an hourly 8,760-timestep EPW")
    hours = np.arange(timestep_count, dtype=np.uint32) % 24
    return np.ascontiguousarray(((hours >= 8) & (hours < 18)).astype(np.float32))


def parse_radiance_matrix(text: str, rows: int, columns: int) -> np.ndarray:
    header: dict[str, int] = {}
    samples: list[list[float]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            key, value = line.split("=", 1)
            if key in {"NROWS", "NCOLS", "NCOMP"}:
                header[key] = int(value)
            continue
        fields = line.split()
        if len(fields) == 3:
            samples.append([float(value) for value in fields])
    expected_header = {"NROWS": rows, "NCOLS": columns, "NCOMP": 3}
    if header != expected_header:
        raise RuntimeError(
            f"unexpected gendaymtx header {header}; expected {expected_header}"
        )
    if len(samples) != rows * columns:
        raise RuntimeError(
            f"gendaymtx returned {len(samples)} RGB rows; expected {rows * columns}"
        )
    return np.ascontiguousarray(
        np.asarray(samples, dtype=np.float32).reshape(rows, columns, 3)
    )


def _radiance_environment(executable: Path) -> dict[str, str]:
    environment = os.environ.copy()
    ray_paths = [
        value for value in environment.get("RAYPATH", ".").split(os.pathsep) if value
    ]
    candidates = []
    if environment.get("RADIANCE_LIB"):
        candidates.append(Path(environment["RADIANCE_LIB"]).expanduser())
    candidates.append(executable.parent.parent / "lib")
    for candidate in candidates:
        if (candidate / "rayinit.cal").is_file():
            resolved = str(candidate.resolve())
            if resolved not in ray_paths:
                ray_paths.insert(0, resolved)
    environment["RAYPATH"] = os.pathsep.join(ray_paths)
    return environment


def resolve_gendaymtx(configured: str | None = None) -> Path | None:
    candidates: list[str] = []
    if configured:
        candidates.append(configured)
    radiance_bin = os.environ.get("RADIANCE_BIN")
    if radiance_bin:
        candidates.append(str(Path(radiance_bin).expanduser() / "gendaymtx"))
    candidates.extend(
        (
            "/usr/local/radiance/bin/gendaymtx",
            "/opt/radiance/bin/gendaymtx",
        )
    )
    candidates.append("gendaymtx")
    for candidate in candidates:
        located = shutil.which(candidate)
        if located:
            return Path(located).resolve()
        path = Path(candidate).expanduser()
        if path.is_file():
            return path.resolve()
    return None


def executable_version(executable: Path) -> str:
    rtrace = executable.parent / "rtrace"
    version_executable = rtrace if rtrace.is_file() else executable
    completed = subprocess.run(
        [str(version_executable), "-version"],
        text=True,
        capture_output=True,
        check=False,
    )
    output = completed.stdout.strip() or completed.stderr.strip()
    if output:
        return output.splitlines()[0]
    stat = executable.stat()
    return f"gendaymtx-{stat.st_size}-{stat.st_mtime_ns}"


@dataclass(frozen=True)
class WeatherDataset:
    weather_id: str
    filename: str
    north_rotation_degrees: float
    location: dict[str, Any]
    timestep_labels: tuple[str, ...]
    tregenza: np.ndarray
    final: np.ndarray
    occupancy: np.ndarray
    annual_metrics_available: bool
    metadata: dict[str, Any]

    def summary(self) -> dict[str, Any]:
        return {
            "weather_id": self.weather_id,
            "filename": self.filename,
            "north_rotation_degrees": self.north_rotation_degrees,
            "location": self.location,
            "timestep_count": int(self.tregenza.shape[1]),
            "occupied_hours": float(np.sum(self.occupancy)),
            "timestep_labels": list(self.timestep_labels),
            "annual_metrics_available": self.annual_metrics_available,
        }


def cie_overcast_matrix(basis: str, exterior_illuminance_lux: float) -> np.ndarray:
    directions = np.asarray(sky_patch_directions(basis), dtype=np.float64)
    solid_angles = np.asarray(sky_patch_solid_angles(basis), dtype=np.float64)
    relative_luminance = np.where(
        directions[:, 2] > 0.0,
        (1.0 + 2.0 * directions[:, 2]) / 3.0,
        0.0,
    )
    horizontal_response = np.sum(
        relative_luminance * np.maximum(directions[:, 2], 0.0) * solid_angles
    )
    scale = exterior_illuminance_lux / (
        horizontal_response * float(np.sum(PHOTOPIC_WEIGHTS))
    )
    rgb = np.repeat((relative_luminance * scale)[:, None], 3, axis=1)
    return np.ascontiguousarray(rgb[:, None, :], dtype=np.float32)


def built_in_overcast_dataset() -> WeatherDataset:
    label = f"CIE overcast · {DEMO_EXTERIOR_ILLUMINANCE_LUX:,.0f} lux exterior"
    metadata = {
        "source": "built-in-cie-overcast",
        "description": "CIE standard overcast sky normalized by exterior horizontal illuminance",
        "exterior_horizontal_illuminance_lux": DEMO_EXTERIOR_ILLUMINANCE_LUX,
    }
    return WeatherDataset(
        weather_id="cie-overcast-10000lux",
        filename="Built-in CIE overcast",
        north_rotation_degrees=0.0,
        location={"city": "CIE overcast demo", "country": None},
        timestep_labels=(label,),
        tregenza=cie_overcast_matrix(
            "tregenza", DEMO_EXTERIOR_ILLUMINANCE_LUX
        ),
        final=cie_overcast_matrix(
            "reinhart-mf2", DEMO_EXTERIOR_ILLUMINANCE_LUX
        ),
        occupancy=np.ones(1, dtype=np.float32),
        annual_metrics_available=False,
        metadata=metadata,
    )


def _epw_timestep_labels(epw_path: Path) -> tuple[str, ...]:
    lines = epw_path.read_text(encoding="utf-8", errors="replace").splitlines()
    records = lines[8:]
    if len(records) != 8760:
        raise ValueError(f"cached EPW has {len(records)} records; expected 8,760")
    labels = []
    for record in records:
        fields = record.split(",")
        if len(fields) < 5:
            raise ValueError("cached EPW contains a malformed hourly record")
        month, day, hour = (int(fields[index]) for index in (1, 2, 3))
        labels.append(f"{month:02d}/{day:02d} {hour - 1:02d}:00")
    return tuple(labels)


class WeatherStore:
    def __init__(
        self,
        cache_directory: str | Path | None = None,
        gendaymtx: str | None = None,
    ) -> None:
        self.cache_directory = (
            Path(cache_directory).expanduser()
            if cache_directory
            else user_cache_path("foton") / "viewer-weather"
        )
        self.configured_gendaymtx = gendaymtx
        self.demo = built_in_overcast_dataset()
        self._datasets: dict[str, WeatherDataset] = {
            self.demo.weather_id: self.demo
        }
        self.initial = self._restore_latest_annual() or self.demo

    def _restore_latest_annual(self) -> WeatherDataset | None:
        if not self.cache_directory.is_dir():
            return None
        candidates = sorted(
            (
                path
                for path in self.cache_directory.iterdir()
                if path.is_dir() and (path / "metadata.json").is_file()
            ),
            key=lambda path: (path / "metadata.json").stat().st_mtime_ns,
            reverse=True,
        )
        for cache in candidates:
            try:
                metadata = json.loads(
                    (cache / "metadata.json").read_text(encoding="utf-8")
                )
                tregenza = np.load(cache / "tregenza.npy", allow_pickle=False)
                final = np.load(cache / "final.npy", allow_pickle=False)
                if tregenza.shape != (146, 8760, 3):
                    continue
                if final.shape != (578, 8760, 3):
                    continue
                dataset = WeatherDataset(
                    weather_id=str(metadata["weather_id"]),
                    filename=str(metadata["source_filename"]),
                    north_rotation_degrees=float(
                        metadata["north_rotation_degrees"]
                    ),
                    location=dict(metadata.get("location", {})),
                    timestep_labels=_epw_timestep_labels(cache / "weather.epw"),
                    tregenza=np.ascontiguousarray(tregenza, dtype=np.float32),
                    final=np.ascontiguousarray(final, dtype=np.float32),
                    occupancy=occupancy_schedule(8760),
                    annual_metrics_available=True,
                    metadata=metadata,
                )
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            self._datasets[dataset.weather_id] = dataset
            return dataset
        return None

    def status(self) -> dict[str, Any]:
        executable = resolve_gendaymtx(self.configured_gendaymtx)
        return {
            "available": executable is not None,
            "path": str(executable) if executable else None,
            "version": executable_version(executable) if executable else None,
        }

    def get(self, weather_id: str) -> WeatherDataset:
        try:
            return self._datasets[weather_id]
        except KeyError as exc:
            raise KeyError(f"unknown weather_id {weather_id!r}") from exc

    def ingest(
        self,
        epw_bytes: bytes,
        filename: str,
        north_rotation_degrees: float = 0.0,
    ) -> WeatherDataset:
        if not epw_bytes or len(epw_bytes) > MAXIMUM_EPW_BYTES:
            raise ValueError("EPW upload must be between 1 byte and 32 MiB")
        if not np.isfinite(north_rotation_degrees):
            raise ValueError("north rotation must be finite")
        executable = resolve_gendaymtx(self.configured_gendaymtx)
        if executable is None:
            raise RuntimeError(
                "gendaymtx is unavailable; install Radiance or set RADIANCE_BIN"
            )
        version = executable_version(executable)
        digest = hashlib.sha256()
        digest.update(epw_bytes)
        digest.update(f"{north_rotation_degrees:.9g}".encode())
        digest.update(version.encode())
        weather_id = digest.hexdigest()
        if weather_id in self._datasets:
            return self._datasets[weather_id]

        cache = self.cache_directory / weather_id
        cache.mkdir(parents=True, exist_ok=True)
        epw_path = cache / "weather.epw"
        wea_path = cache / "weather.wea"
        epw_path.write_bytes(epw_bytes)
        try:
            from ladybug.epw import EPW
            from ladybug.wea import Wea
        except ImportError as exc:
            raise RuntimeError(
                "ladybug-core is required; install foton-daylight[viewer]"
            ) from exc

        epw = EPW(str(epw_path))
        timestep_count = len(epw.direct_normal_radiation.values)
        if timestep_count != 8760:
            raise ValueError(
                f"the viewer requires 8,760 hourly records; EPW has {timestep_count}"
            )
        wea = Wea.from_epw_file(str(epw_path))
        wea.write(str(wea_path))
        labels = tuple(str(value) for value in wea.datetimes)
        location = {
            "city": getattr(epw.location, "city", None),
            "country": getattr(epw.location, "country", None),
            "latitude": getattr(epw.location, "latitude", None),
            "longitude": getattr(epw.location, "longitude", None),
            "time_zone": getattr(epw.location, "time_zone", None),
        }

        matrices: dict[str, np.ndarray] = {}
        commands: dict[str, list[str]] = {}
        for basis, configuration in BASES.items():
            matrix_path = cache / f"{basis}.npy"
            if matrix_path.is_file():
                matrix = np.load(matrix_path)
            else:
                command = [
                    str(executable),
                    "-m",
                    str(configuration["multiplier"]),
                    "-O0",
                    "-r",
                    f"{north_rotation_degrees:.9g}",
                    str(wea_path),
                ]
                completed = subprocess.run(
                    command,
                    text=True,
                    capture_output=True,
                    env=_radiance_environment(executable),
                    check=False,
                )
                if completed.returncode:
                    detail = completed.stderr.strip() or "no stderr output"
                    raise RuntimeError(
                        f"gendaymtx exited with status {completed.returncode}: {detail}"
                    )
                matrix = parse_radiance_matrix(
                    completed.stdout,
                    configuration["rows"],
                    timestep_count,
                )
                np.save(matrix_path, matrix)
                commands[basis] = command
            expected_shape = (configuration["rows"], timestep_count, 3)
            if matrix.shape != expected_shape:
                raise RuntimeError(
                    f"cached {basis} matrix has shape {matrix.shape}; expected {expected_shape}"
                )
            matrices[basis] = np.ascontiguousarray(matrix, dtype=np.float32)

        metadata = {
            "weather_id": weather_id,
            "source_filename": filename,
            "north_rotation_degrees": north_rotation_degrees,
            "gendaymtx": str(executable),
            "gendaymtx_version": version,
            "commands": commands,
            "location": location,
        }
        (cache / "metadata.json").write_text(
            json.dumps(metadata, indent=2) + "\n",
            encoding="utf-8",
        )
        dataset = WeatherDataset(
            weather_id=weather_id,
            filename=filename,
            north_rotation_degrees=north_rotation_degrees,
            location=location,
            timestep_labels=labels,
            tregenza=matrices["tregenza"],
            final=matrices["final"],
            occupancy=occupancy_schedule(timestep_count),
            annual_metrics_available=True,
            metadata=metadata,
        )
        self._datasets[weather_id] = dataset
        self.initial = dataset
        return dataset
