"""Inspect an external installation without starting an analysis."""

from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
import tempfile
import subprocess
from foton_bridge import backend_identifier

from .annual import QUALITY_PRESETS, SOLVER_REVISION
from .weather import (
    _default_cache_directory,
    foton_sky_version,
    resolve_gendaymtx,
    executable_version,
    probe_gendaymtx,
)


def inspect_installation(backend="auto", output=None, radiance_bin=None):
    """Check that Foton, its GPU backend and its Python dependencies are ready.

    Returns a report with versions, the selected backend, the quality presets and
    any errors or warnings, without running an analysis. A missing Radiance is a
    warning, because annual runs do not need it.
    """
    from foton import Engine, __version__

    engine = dict(Engine({"backend": backend}).capabilities())
    selected = backend_identifier(engine)
    dependencies, errors, warnings = {}, [], []
    for package in (
        "numpy",
        "honeybee-core",
        "honeybee-radiance",
        "honeybee-radiance-postprocess",
        "ladybug-core",
        "platformdirs",
    ):
        try:
            dependencies[package] = version(package)
        except PackageNotFoundError:
            errors.append("Missing " + package + "; install foton-daylight[honeybee]")
    # Annual skies come from Foton's built-in Perez model; gendaymtx is an
    # optional alternative (sky_source="gendaymtx") and the validation
    # oracle, so a missing Radiance is reported, never an error.
    weather_version = foton_sky_version()
    executable, gendaymtx_version, gendaymtx_note = None, None, None
    try:
        executable = resolve_gendaymtx(radiance_bin)
        gendaymtx_version = executable_version(executable)
        probe_gendaymtx(executable)
    except (OSError, RuntimeError, subprocess.TimeoutExpired) as error:
        executable, gendaymtx_version = None, None
        gendaymtx_note = str(error)
    directories = {
        "cache": _default_cache_directory(),
        "output": Path(output) if output else Path.home() / "foton_simulation",
    }
    writable = {}
    for key, path in directories.items():
        try:
            path.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryFile(dir=path):
                pass
            writable[key] = True
        except OSError as error:
            writable[key] = False
            errors.append("Cannot write %s directory: %s" % (key, error))
    if selected == "reference":
        warnings.append(
            "CPU reference fallback selected; GPU performance is unavailable."
        )
    return {
        "engine": engine,
        "engine_version": __version__,
        "selected_backend": selected,
        "weather_cache": str(directories["cache"]),
        "quality_settings": QUALITY_PRESETS,
        "dependencies": dependencies,
        "directories_writable": writable,
        "sky_source": "foton",
        "sky_version": weather_version,
        "sky_sources": {
            "foton": {"available": True, "version": weather_version},
            "gendaymtx": {
                "available": executable is not None,
                "executable": str(executable) if executable else None,
                "version": gendaymtx_version,
                "note": gendaymtx_note,
            },
        },
        "gendaymtx": str(executable) if executable else None,
        "errors": errors,
        "warnings": warnings,
        "ready": not errors,
        "provenance": {
            "engine_version": __version__,
            "solver_revision": SOLVER_REVISION,
            "selected_backend": selected,
            "weather_version": weather_version,
            "sky_source": "foton",
        },
    }
