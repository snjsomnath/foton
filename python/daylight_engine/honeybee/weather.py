"""Annual sky matrices from EPW/WEA weather.

The default sky comes from Foton's own Perez all-weather model in
``daylight_core::sky::perez`` (Perez, Seals and Michalsky 1993 over Tregenza
1987 / Reinhart patches), reached through ``daylight_engine.perez_sky_matrix``.
Radiance's ``gendaymtx`` remains available as an alternative source
(``sky_source="gendaymtx"``) and is the oracle the built-in sky is validated
against; it is no longer needed at run time.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from hashlib import sha256
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
from typing import Any

import numpy as np


SKY_ROWS = {1: 146, 2: 578}
SKY_BASIS = {1: "tregenza", 2: "reinhart-mf2"}
SKY_SOURCES = ("foton", "gendaymtx")
#: Bump when the built-in sky model changes what it computes; it keys the
#: weather cache for ``sky_source="foton"``.
FOTON_SKY_REVISION = 1


@dataclass(frozen=True)
class AnnualWeather:
    """A Radiance sky matrix and the metadata needed by Honeybee outputs."""

    sky: np.ndarray
    sun_up_hours: tuple[float, ...]
    weather_id: str
    source: str
    location: dict[str, Any]
    north: float
    sky_density: int
    basis: str
    cache_hit: bool
    gendaymtx: str | None
    gendaymtx_version: str | None
    sky_source: str = "gendaymtx"
    sky_version: str = ""


# Prepared weather kept in memory by a long-lived process: see ``memo`` on
# :func:`prepare_annual_weather`. Each entry holds a sky matrix (15 MB at
# Tregenza, 60 MB at MF:2), so only the most recent few are kept.
WeatherMemo = dict
MAXIMUM_REMEMBERED_WEATHER = 2


def _remember(memo, key, weather: AnnualWeather) -> AnnualWeather:
    if memo is None or key is None:
        return weather
    # The memo hands the same array to later runs, so nothing may write to it.
    weather.sky.flags.writeable = False
    memo.pop(key, None)
    memo[key] = weather
    while len(memo) > MAXIMUM_REMEMBERED_WEATHER:
        memo.pop(next(iter(memo)))
    return weather


def foton_sky_version() -> str:
    """Version string recorded for matrices from the built-in sky model."""
    from daylight_engine import __version__

    return f"foton-sky-r{FOTON_SKY_REVISION} (foton-daylight {__version__})"


def prepare_annual_weather(
    wea_or_epw,
    *,
    north: float = 0,
    sky_density: int = 1,
    radiance_bin: str | None = None,
    cache_directory: str | Path | None = None,
    sky_source: str = "foton",
    memo: WeatherMemo | None = None,
) -> AnnualWeather:
    """Prepare the hourly sky matrix an annual study consumes.

    The matrix is shaped ``(patches, 8760, 3)`` float32: RGB visible radiance
    in W/sr/m^2 per Radiance sky patch (ground patch first), with sun-down
    hours zeroed. ``sky_source="foton"`` (default) computes it with Foton's
    own Perez model; ``"gendaymtx"`` runs Radiance's ``gendaymtx -O0`` and
    needs a Radiance installation. Both are cached under a key that includes
    the source, so switching sources never serves the other's matrix.

    ``memo`` keeps prepared weather in memory between calls, keyed by the
    weather file's bytes and every setting that shapes the matrix. A
    long-lived process (the ``serve`` worker) uses it to skip re-parsing the
    EPW and re-loading the matrix from disk on every run; the arrays it
    returns are the same ones, so results are identical.
    """
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
    if isinstance(sky_density, bool) or sky_density not in SKY_ROWS:
        raise ValueError("sky_density must be 1 (Tregenza) or 2 (Reinhart MF:2)")
    if sky_source not in SKY_SOURCES:
        raise ValueError("sky_source must be 'foton' or 'gendaymtx'")
    sky_density = int(sky_density)
    rows = SKY_ROWS[sky_density]
    basis = SKY_BASIS[sky_density]
    memo_key = None
    if memo is not None and isinstance(wea_or_epw, (str, Path)):
        path = Path(wea_or_epw).expanduser().resolve()
        if path.is_file():
            memo_key = (
                sha256(path.read_bytes()).hexdigest(),
                path.suffix.lower(),
                north,
                sky_density,
                sky_source,
                str(radiance_bin) if sky_source == "gendaymtx" else None,
                str(cache_directory) if cache_directory is not None else None,
            )
            remembered = memo.get(memo_key)
            if remembered is not None:
                return replace(remembered, source=str(path), cache_hit=True)
    wea, source, source_bytes = _coerce_wea(wea_or_epw, EPW, Wea)
    if len(wea) != 8760 or int(wea.timestep) != 1:
        raise ValueError("annual daylight requires an hourly 8,760-timestep WEA")
    if sky_source == "gendaymtx":
        executable = resolve_gendaymtx(radiance_bin)
        version = executable_version(executable)
        cache_salt = f"\0north={north:.12g}\0mf={sky_density}\0binary-sky=v4\0{version}"
    else:
        executable = None
        version = foton_sky_version()
        cache_salt = (
            f"\0north={north:.12g}\0mf={sky_density}\0binary-sky=v4"
            f"\0sky=foton\0r{FOTON_SKY_REVISION}"
        )
    digest = sha256()
    digest.update(source_bytes)
    digest.update(cache_salt.encode("utf-8"))
    weather_id = digest.hexdigest()

    cache_root = (
        Path(cache_directory).expanduser()
        if cache_directory is not None
        else _default_cache_directory()
    )
    cache = cache_root / weather_id
    matrix_path = cache / f"{basis}.npy"
    metadata_path = cache / "metadata.json"
    if matrix_path.is_file() and metadata_path.is_file():
        matrix = np.load(matrix_path, allow_pickle=False)
        if matrix.shape == (rows, 8760, 3):
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            return _remember(memo, memo_key, AnnualWeather(
                sky=np.ascontiguousarray(matrix, dtype=np.float32),
                sun_up_hours=tuple(
                    float(value) for value in metadata["sun_up_hours"]
                ),
                weather_id=weather_id,
                source=source,
                location=dict(metadata["location"]),
                north=north,
                sky_density=sky_density,
                basis=basis,
                cache_hit=True,
                gendaymtx=str(executable) if executable else None,
                gendaymtx_version=version if executable else None,
                sky_source=sky_source,
                sky_version=version,
            ))

    cache.mkdir(parents=True, exist_ok=True)
    if sky_source == "foton":
        matrix, sun_up_hours = foton_sky_matrix(
            wea, north=north, sky_density=sky_density
        )
        command = None
        sun_command = None
    else:
        matrix, sun_up_hours, command, sun_command = _gendaymtx_sky_matrix(
            wea, executable, north=north, sky_density=sky_density, rows=rows
        )

    sun_down_mask = np.ones(8760, dtype=bool)
    sun_down_mask[np.asarray(sun_up_hours, dtype=np.uint32)] = False
    matrix[:, sun_down_mask, :] = 0
    location = _location_dict(wea.location)
    metadata = {
        "schema_version": 2,
        "weather_id": weather_id,
        "source": source,
        "north": north,
        "basis": basis,
        "sky_density": sky_density,
        "rows": rows,
        "timestep_count": 8760,
        "sun_up_hours": list(sun_up_hours),
        "location": location,
        "sky_source": sky_source,
        "sky_version": version,
        "gendaymtx": str(executable) if executable else None,
        "gendaymtx_version": version if executable else None,
        "command": command,
        "sun_command": sun_command,
    }
    np.save(matrix_path, matrix, allow_pickle=False)
    metadata_path.write_text(
        json.dumps(metadata, indent=2, sort_keys=True), encoding="utf-8"
    )
    return _remember(memo, memo_key, AnnualWeather(
        sky=matrix,
        sun_up_hours=sun_up_hours,
        weather_id=weather_id,
        source=source,
        location=location,
        north=north,
        sky_density=sky_density,
        basis=basis,
        cache_hit=False,
        gendaymtx=str(executable) if executable else None,
        gendaymtx_version=version if executable else None,
        sky_source=sky_source,
        sky_version=version,
    ))


def wea_irradiance_arrays(wea) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Direct-normal, diffuse-horizontal (W/m^2) and hour-of-year arrays.

    Irradiances are truncated to whole W/m^2 exactly as Ladybug writes them
    to a WEA file, so both sky sources see the same numbers.
    """
    direct = np.trunc(
        np.asarray(wea.direct_normal_irradiance.values, dtype=np.float64)
    ).astype(np.float32)
    diffuse = np.trunc(
        np.asarray(wea.diffuse_horizontal_irradiance.values, dtype=np.float64)
    ).astype(np.float32)
    hours = np.asarray(wea.hoys, dtype=np.float64)
    return direct, diffuse, hours


def wea_site(wea) -> tuple[float, float, float]:
    """Latitude, longitude (degrees east) and time zone (hours) of a WEA.

    Ladybug writes the WEA header with two decimals of latitude and
    longitude and a whole number of meridian degrees; the same rounding is
    applied here so the built-in sky evaluates the sun exactly where
    ``gendaymtx`` reading that header would.
    """
    location = wea.location
    latitude = float("%.2f" % float(location.latitude))
    longitude = -float("%.2f" % -float(location.longitude))
    meridian_degrees = int(-float(location.time_zone) * 15)
    return latitude, longitude, -meridian_degrees / 15.0


def foton_sky_matrix(
    wea, *, north: float = 0, sky_density: int = 1
) -> tuple[np.ndarray, tuple[float, ...]]:
    """Foton's built-in Perez sky for a Ladybug WEA.

    Returns the ``(patches, steps, 3)`` float32 matrix before sun-down
    masking and the sun-up hours (hour of year, centred like the WEA).
    """
    from daylight_engine import perez_sky_matrix

    direct, diffuse, hours = wea_irradiance_arrays(wea)
    latitude, longitude, time_zone = wea_site(wea)
    matrix, sun_up, _altitude, _azimuth = perez_sky_matrix(
        latitude,
        longitude,
        time_zone,
        direct,
        diffuse,
        basis=SKY_BASIS[int(sky_density)],
        north=float(north),
        hour_of_year=hours,
    )
    sun_up_hours = tuple(float(hour) for hour in hours[np.asarray(sun_up, dtype=bool)])
    return np.ascontiguousarray(matrix, dtype=np.float32), sun_up_hours


def _gendaymtx_sky_matrix(wea, executable: Path, *, north, sky_density, rows):
    with tempfile.TemporaryDirectory(prefix="foton-weather-") as temporary:
        wea_path = Path(temporary) / "weather.wea"
        wea.write(str(wea_path))
        command = [
            str(executable),
            "-m",
            str(sky_density),
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
            completed.stdout, rows, 8760
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
    return matrix, sun_up_hours, command, sun_command


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
    rtrace = shutil.which(str(executable.parent / "rtrace"))
    version_executable = rtrace or executable
    completed = subprocess.run(
        [str(version_executable), "-version"],
        text=True,
        capture_output=True,
        check=False,
        env=_radiance_environment(executable),
        timeout=10,
    )
    output = completed.stdout.strip() or completed.stderr.strip()
    if output:
        return output.splitlines()[0]
    stat = executable.stat()
    return f"gendaymtx-{stat.st_size}-{stat.st_mtime_ns}"


def probe_gendaymtx(executable: Path):
    """Reject older Radiance builds without the annual sun-path export flags."""
    with tempfile.TemporaryDirectory(prefix="foton-preflight-") as folder:
        root = Path(folder)
        wea = root / "probe.wea"
        wea.write_text("place probe\nlatitude 0\nlongitude 0\ntime_zone 0\nsite_elevation 0\nweather_data_file_units 1\n3 21 12.5 500 100\n", encoding="ascii")
        completed = subprocess.run(
            [str(executable), "-n", "-D", str(root / "sun.mtx"), "-M", str(root / "suns.mod"), str(wea)],
            capture_output=True, text=True, timeout=10, env=_radiance_environment(executable),
        )
        if completed.returncode or not (root / "suns.mod").is_file():
            raise RuntimeError(
                "This gendaymtx cannot export annual sun paths (-n/-D/-M); "
                "install Radiance 5.4a or newer and set RADIANCE_BIN, or use "
                "Foton's built-in sky (sky_source='foton'). "
                + completed.stderr.strip()
            )


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
