"""Canonical Ladybug/Radiance weather preparation for annual daylight."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
from typing import Any

import numpy as np


REINHART_MF2_ROWS = 578


@dataclass(frozen=True)
class AnnualWeather:
    """A Radiance sky matrix and the metadata needed by Honeybee outputs."""

    sky: np.ndarray
    sun_up_hours: tuple[float, ...]
    weather_id: str
    source: str
    location: dict[str, Any]
    north: float
    cache_hit: bool
    gendaymtx: str
    gendaymtx_version: str


def prepare_annual_weather(
    wea_or_epw,
    *,
    north: float = 0,
    radiance_bin: str | None = None,
    cache_directory: str | Path | None = None,
) -> AnnualWeather:
    """Prepare the canonical hourly Reinhart MF:2 matrix with ``gendaymtx``."""
    try:
        from ladybug.epw import EPW
        from ladybug.wea import Wea
    except ImportError as error:
        raise ImportError(
            "Annual Honeybee studies require ladybug-core; install "
            "'foton-daylight[honeybee]'"
        ) from error

    north = float(north)
    if not np.isfinite(north):
        raise ValueError("north must be finite")
    wea, source, source_bytes = _coerce_wea(wea_or_epw, EPW, Wea)
    if len(wea) != 8760 or int(wea.timestep) != 1:
        raise ValueError("annual daylight requires an hourly 8,760-timestep WEA")
    executable = resolve_gendaymtx(radiance_bin)
    version = executable_version(executable)
    digest = sha256()
    digest.update(source_bytes)
    digest.update(
        f"\0north={north:.12g}\0mf=2\0binary-sky=v3\0{version}".encode(
            "utf-8"
        )
    )
    weather_id = digest.hexdigest()

    cache_root = (
        Path(cache_directory).expanduser()
        if cache_directory is not None
        else _default_cache_directory()
    )
    cache = cache_root / weather_id
    matrix_path = cache / "reinhart-mf2.npy"
    metadata_path = cache / "metadata.json"
    if matrix_path.is_file() and metadata_path.is_file():
        matrix = np.load(matrix_path, allow_pickle=False)
        if matrix.shape == (REINHART_MF2_ROWS, 8760, 3):
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            return AnnualWeather(
                sky=np.ascontiguousarray(matrix, dtype=np.float32),
                sun_up_hours=tuple(
                    float(value) for value in metadata["sun_up_hours"]
                ),
                weather_id=weather_id,
                source=source,
                location=dict(metadata["location"]),
                north=north,
                cache_hit=True,
                gendaymtx=str(executable),
                gendaymtx_version=version,
            )

    cache.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="foton-weather-") as temporary:
        wea_path = Path(temporary) / "weather.wea"
        wea.write(str(wea_path))
        command = [
            str(executable),
            "-m",
            "2",
            "-of",
            "-O0",
            "-r",
            f"{north:.12g}",
            str(wea_path),
        ]
        completed = subprocess.run(
            command,
            capture_output=True,
            check=False,
            env=_radiance_environment(executable),
        )
        if completed.returncode != 0:
            detail = (
                completed.stderr.decode("utf-8", errors="replace").strip()
                or completed.stdout[:1000].decode(
                    "utf-8", errors="replace"
                ).strip()
            )
            raise RuntimeError(f"gendaymtx failed ({completed.returncode}): {detail}")
        matrix = parse_radiance_binary_matrix(
            completed.stdout, REINHART_MF2_ROWS, 8760
        )
        sun_matrix_path = Path(temporary) / "sunpath.mtx"
        sun_modifiers_path = Path(temporary) / "suns.mod"
        sun_command = [
            str(executable),
            "-n",
            "-D",
            str(sun_matrix_path),
            "-M",
            str(sun_modifiers_path),
            "-O0",
            "-r",
            f"{north:.12g}",
            str(wea_path),
        ]
        completed = subprocess.run(
            sun_command,
            text=True,
            capture_output=True,
            check=False,
            env=_radiance_environment(executable),
        )
        if completed.returncode != 0:
            detail = completed.stderr.strip() or completed.stdout.strip()
            raise RuntimeError(
                f"gendaymtx sunpath failed ({completed.returncode}): {detail}"
            )
        sun_up_hours = tuple(
            int(line.strip().split("solar", 1)[1]) / 60.0
            for line in sun_modifiers_path.read_text(
                encoding="utf-8"
            ).splitlines()
            if line.strip()
        )

    sun_down_mask = np.ones(8760, dtype=bool)
    sun_down_mask[np.asarray(sun_up_hours, dtype=np.uint32)] = False
    matrix[:, sun_down_mask, :] = 0
    location = _location_dict(wea.location)
    metadata = {
        "schema_version": 1,
        "weather_id": weather_id,
        "source": source,
        "north": north,
        "basis": "reinhart-mf2",
        "rows": REINHART_MF2_ROWS,
        "timestep_count": 8760,
        "sun_up_hours": list(sun_up_hours),
        "location": location,
        "gendaymtx": str(executable),
        "gendaymtx_version": version,
        "command": command,
        "sun_command": sun_command,
    }
    np.save(matrix_path, matrix, allow_pickle=False)
    metadata_path.write_text(
        json.dumps(metadata, indent=2, sort_keys=True), encoding="utf-8"
    )
    return AnnualWeather(
        sky=matrix,
        sun_up_hours=sun_up_hours,
        weather_id=weather_id,
        source=source,
        location=location,
        north=north,
        cache_hit=False,
        gendaymtx=str(executable),
        gendaymtx_version=version,
    )


def parse_radiance_matrix(text: str, rows: int, columns: int) -> np.ndarray:
    """Parse an ASCII Radiance matrix without changing row/column ordering."""
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
    expected = {"NROWS": rows, "NCOLS": columns, "NCOMP": 3}
    if header != expected:
        raise RuntimeError(
            f"unexpected gendaymtx header {header}; expected {expected}"
        )
    if len(samples) != rows * columns:
        raise RuntimeError(
            f"gendaymtx returned {len(samples)} RGB rows; "
            f"expected {rows * columns}"
        )
    return np.ascontiguousarray(
        np.asarray(samples, dtype=np.float32).reshape(rows, columns, 3)
    )


def parse_radiance_binary_matrix(
    content: bytes, rows: int, columns: int
) -> np.ndarray:
    """Parse a native-endian ``gendaymtx -of`` matrix."""
    header_end = content.find(b"\n\n")
    if header_end < 0:
        raise RuntimeError("gendaymtx float matrix has no header terminator")
    header_text = content[:header_end].decode("ascii", errors="strict")
    header = {}
    for line in header_text.splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            if key in {"NROWS", "NCOLS", "NCOMP"}:
                header[key] = int(value)
    expected = {"NROWS": rows, "NCOLS": columns, "NCOMP": 3}
    if header != expected:
        raise RuntimeError(
            f"unexpected gendaymtx header {header}; expected {expected}"
        )
    payload = memoryview(content)[header_end + 2 :]
    expected_values = rows * columns * 3
    values = np.frombuffer(payload, dtype=np.float32)
    if values.size != expected_values:
        raise RuntimeError(
            f"gendaymtx returned {values.size} floats; expected {expected_values}"
        )
    return np.array(
        values.reshape(rows, columns, 3),
        dtype=np.float32,
        order="C",
        copy=True,
    )


def resolve_gendaymtx(configured: str | None = None) -> Path:
    """Resolve the Radiance executable, including Honeybee's configured install."""
    candidates: list[str] = []
    if configured:
        configured_path = Path(configured).expanduser()
        candidates.append(
            str(configured_path / "gendaymtx")
            if configured_path.is_dir()
            else str(configured_path)
        )
    radiance_bin = os.environ.get("RADIANCE_BIN")
    if radiance_bin:
        candidates.append(str(Path(radiance_bin).expanduser() / "gendaymtx"))
    try:
        from honeybee_radiance.config import folders

        if folders.radbin_path:
            candidates.append(str(Path(folders.radbin_path) / "gendaymtx"))
    except (ImportError, AttributeError):
        pass
    candidates.extend(
        (
            "/usr/local/radiance/bin/gendaymtx",
            "/opt/radiance/bin/gendaymtx",
            "gendaymtx",
        )
    )
    for candidate in candidates:
        located = shutil.which(candidate)
        if located:
            return Path(located).resolve()
        path = Path(candidate)
        if path.is_file():
            return path.resolve()
    raise FileNotFoundError(
        "gendaymtx was not found; install Radiance or set RADIANCE_BIN"
    )


def executable_version(executable: Path) -> str:
    """Return a stable Radiance version string for cache invalidation."""
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


def _coerce_wea(value, epw_type, wea_type):
    if isinstance(value, (str, Path)):
        path = Path(value).expanduser().resolve()
        if not path.is_file():
            raise FileNotFoundError(path)
        source_bytes = path.read_bytes()
        suffix = path.suffix.lower()
        if suffix == ".epw":
            return wea_type.from_epw_file(str(path)), str(path), source_bytes
        if suffix == ".wea":
            return wea_type.from_file(str(path)), str(path), source_bytes
        raise ValueError("weather path must end in .epw or .wea")
    if isinstance(value, epw_type):
        wea = wea_type.from_epw_file(value.file_path) if value.file_path else None
        if wea is None:
            raise ValueError("an in-memory EPW must have a source file path")
        text = wea.to_file_string()
        return wea, "<EPW object>", text.encode("utf-8")
    if isinstance(value, wea_type):
        text = value.to_file_string()
        return value, "<WEA object>", text.encode("utf-8")
    raise TypeError("wea must be an EPW/WEA object or an .epw/.wea path")


def _location_dict(location) -> dict[str, Any]:
    return {
        "city": location.city,
        "state": location.state,
        "country": location.country,
        "latitude": float(location.latitude),
        "longitude": float(location.longitude),
        "time_zone": float(location.time_zone),
        "elevation": float(location.elevation),
    }


def _radiance_environment(executable: Path) -> dict[str, str]:
    environment = os.environ.copy()
    ray_paths = [
        value for value in environment.get("RAYPATH", ".").split(os.pathsep) if value
    ]
    for candidate in (
        Path(environment["RADIANCE_LIB"]).expanduser()
        if environment.get("RADIANCE_LIB")
        else None,
        executable.parent.parent / "lib",
    ):
        if candidate is not None and (candidate / "rayinit.cal").is_file():
            resolved = str(candidate.resolve())
            if resolved not in ray_paths:
                ray_paths.insert(0, resolved)
    environment["RAYPATH"] = os.pathsep.join(ray_paths)
    return environment


def _default_cache_directory() -> Path:
    try:
        from platformdirs import user_cache_path
    except ImportError as error:
        raise ImportError(
            "Annual Honeybee studies require platformdirs; install "
            "'foton-daylight[honeybee]'"
        ) from error
    return user_cache_path("foton") / "honeybee-weather"
