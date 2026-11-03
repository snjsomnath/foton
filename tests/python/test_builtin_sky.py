"""Foton's built-in Perez sky against Radiance's ``gendaymtx``.

The golden file under ``tests/fixtures/sky`` holds ``gendaymtx -O0`` columns
for a spread of sun-up hours of the three repository EPWs at Tregenza and
Reinhart MF:2 density (exported by ``scripts/export_sky_golden.py``), so the
comparison runs on machines without Radiance. When ``gendaymtx`` is
installed the whole year is compared live as well.
"""

from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import tempfile
from unittest.mock import patch

import numpy as np
import pytest

from daylight_engine import perez_sky_matrix

ROOT = Path(__file__).resolve().parents[2]
GOLDEN = ROOT / "tests/fixtures/sky/gendaymtx-golden.npz"
EPWS = ("gothenburg", "phoenix", "seattle")
BASES = {1: "tregenza", 2: "reinhart-mf2"}
# Agreement is expected at single-precision level; anything above this is a
# convention mismatch to chase, not a tolerance to widen.
RELATIVE_TOLERANCE = 1e-5
MEANINGFUL_RADIANCE = 1e-3


def _relative_difference(ours, reference):
    """Largest |ours - reference| / max(reference column) per hour."""
    scale = np.max(reference, axis=(0, 2))
    meaningful = scale > MEANINGFUL_RADIANCE
    difference = np.max(np.abs(ours - reference), axis=(0, 2))
    return difference[meaningful] / scale[meaningful], meaningful


def test_golden_file_is_small_enough_for_the_repository():
    assert GOLDEN.stat().st_size < 900_000


@pytest.mark.parametrize("name", EPWS)
@pytest.mark.parametrize("density", (1, 2))
def test_matches_gendaymtx_golden_columns(name, density):
    golden = np.load(GOLDEN)
    latitude, longitude, time_zone = golden[f"{name}/location"]
    matrix, sun_up, _altitude, _azimuth = perez_sky_matrix(
        float(latitude),
        float(longitude),
        float(time_zone),
        golden[f"{name}/direct_normal"],
        golden[f"{name}/diffuse_horizontal"],
        basis=BASES[density],
        hour_of_year=golden[f"{name}/hour_of_year"],
    )
    hours = golden[f"{name}/mf{density}/hours"]
    reference = golden[f"{name}/mf{density}/columns"]
    assert matrix.shape == (reference.shape[0], 8760, 3)
    assert matrix.dtype == np.float32
    relative, meaningful = _relative_difference(matrix[:, hours, :], reference)
    assert meaningful.all()
    assert relative.max() <= RELATIVE_TOLERANCE, (
        f"{name} MF:{density}: worst per-hour relative difference {relative.max():.3e}"
    )
    np.testing.assert_array_equal(sun_up, golden[f"{name}/sun_up"])


def test_sun_up_hours_follow_the_half_disc_rule():
    golden = np.load(GOLDEN)
    latitude, longitude, time_zone = golden["gothenburg/location"]
    _matrix, sun_up, altitude, _azimuth = perez_sky_matrix(
        float(latitude),
        float(longitude),
        float(time_zone),
        golden["gothenburg/direct_normal"],
        golden["gothenburg/diffuse_horizontal"],
    )
    expected = altitude > -np.radians(0.533 / 2)
    np.testing.assert_array_equal(sun_up, expected)
    assert 4000 < int(sun_up.sum()) < 4800


def test_rejects_malformed_inputs():
    direct = np.zeros(24, dtype=np.float32)
    with pytest.raises(ValueError):
        perez_sky_matrix(57.66, 12.28, 1.0, direct, np.zeros(23, dtype=np.float32))
    with pytest.raises(ValueError):
        perez_sky_matrix(57.66, 12.28, 1.0, direct, direct, basis="mf3")
    with pytest.raises(ValueError):
        perez_sky_matrix(
            57.66, 12.28, 1.0, direct, direct, hour_of_year=np.full(24, 9e9)
        )
    with pytest.raises(ValueError):
        perez_sky_matrix(57.66, 12.28, 1.0, direct - 1.0, direct)


def test_exact_sine_normalisation_differs_only_at_the_table_level():
    golden = np.load(GOLDEN)
    latitude, longitude, time_zone = golden["seattle/location"]
    arguments = (
        float(latitude),
        float(longitude),
        float(time_zone),
        golden["seattle/direct_normal"],
        golden["seattle/diffuse_horizontal"],
    )
    oracle, *_ = perez_sky_matrix(*arguments)
    exact, *_ = perez_sky_matrix(*arguments, oracle_cosine_table=False)
    relative, _meaningful = _relative_difference(exact, oracle)
    assert 0 < relative.max() < 2e-3


def _gendaymtx():
    try:
        from foton.honeybee.weather import resolve_gendaymtx

        return resolve_gendaymtx(None)
    except (FileNotFoundError, ImportError):
        return None


@pytest.mark.skipif(_gendaymtx() is None, reason="gendaymtx is not installed")
@pytest.mark.parametrize("name", EPWS)
@pytest.mark.parametrize("density", (1, 2))
def test_matches_live_gendaymtx_for_the_whole_year(name, density):
    pytest.importorskip("ladybug")
    from ladybug.wea import Wea

    from foton.honeybee.weather import (
        SKY_ROWS,
        _radiance_environment,
        foton_sky_matrix,
        parse_radiance_binary_matrix,
    )

    executable = _gendaymtx()
    wea = Wea.from_epw_file(str(ROOT / "epw" / f"{name}.epw"))
    with tempfile.TemporaryDirectory(prefix="foton-sky-test-") as temporary:
        wea_path = Path(temporary) / "weather.wea"
        wea.write(str(wea_path))
        completed = subprocess.run(
            [str(executable), "-m", str(density), "-of", "-O0", str(wea_path)],
            check=True,
            capture_output=True,
            env=_radiance_environment(executable),
        )
        modifiers = Path(temporary) / "suns.mod"
        subprocess.run(
            [
                str(executable),
                "-n",
                "-D",
                str(Path(temporary) / "sun.mtx"),
                "-M",
                str(modifiers),
                "-O0",
                str(wea_path),
            ],
            check=True,
            capture_output=True,
            env=_radiance_environment(executable),
        )
        reference_sun_up = tuple(
            int(line.strip().split("solar", 1)[1]) / 60.0
            for line in modifiers.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
    reference = parse_radiance_binary_matrix(
        completed.stdout, SKY_ROWS[density], 8760
    )
    matrix, sun_up_hours = foton_sky_matrix(wea, sky_density=density)
    relative, meaningful = _relative_difference(matrix, reference)
    print(
        f"{name} MF:{density}: {int(meaningful.sum())} lit hours, worst per-hour "
        f"relative difference {relative.max():.3e}"
    )
    assert relative.max() <= RELATIVE_TOLERANCE
    assert sun_up_hours == reference_sun_up


def test_prepare_annual_weather_uses_the_built_in_sky_by_default(tmp_path):
    pytest.importorskip("ladybug")
    from foton.honeybee.weather import prepare_annual_weather

    with patch(
        "foton.honeybee.weather.resolve_gendaymtx",
        side_effect=FileNotFoundError("gendaymtx was not found"),
    ):
        weather = prepare_annual_weather(
            ROOT / "epw/seattle.epw", sky_density=1, cache_directory=tmp_path
        )
    assert weather.sky_source == "foton"
    assert weather.sky_version.startswith("foton-sky-r")
    assert weather.gendaymtx is None
    assert weather.sky.shape == (146, 8760, 3)
    assert weather.sky.dtype == np.float32
    assert not weather.cache_hit
    indices = np.asarray(weather.sun_up_hours, dtype=int)
    down = np.ones(8760, dtype=bool)
    down[indices] = False
    assert np.all(weather.sky[:, down, :] == 0)
    assert np.any(weather.sky[:, indices, :] > 0)
    assert all(hour % 1 == 0.5 for hour in weather.sun_up_hours)
    again = prepare_annual_weather(
        ROOT / "epw/seattle.epw", sky_density=1, cache_directory=tmp_path
    )
    assert again.cache_hit and again.sky_source == "foton"
    np.testing.assert_array_equal(again.sky, weather.sky)
    with pytest.raises(ValueError):
        prepare_annual_weather(
            ROOT / "epw/seattle.epw", cache_directory=tmp_path, sky_source="radiance"
        )


@pytest.mark.skipif(_gendaymtx() is None, reason="gendaymtx is not installed")
def test_sky_sources_are_cached_apart_and_agree(tmp_path):
    pytest.importorskip("ladybug")
    from foton.honeybee.weather import prepare_annual_weather

    foton = prepare_annual_weather(
        ROOT / "epw/phoenix.epw", sky_density=1, cache_directory=tmp_path
    )
    radiance = prepare_annual_weather(
        ROOT / "epw/phoenix.epw",
        sky_density=1,
        cache_directory=tmp_path,
        sky_source="gendaymtx",
    )
    assert foton.weather_id != radiance.weather_id
    assert radiance.sky_source == "gendaymtx" and radiance.gendaymtx
    assert foton.sun_up_hours == radiance.sun_up_hours
    relative, _meaningful = _relative_difference(foton.sky, radiance.sky)
    assert relative.max() <= RELATIVE_TOLERANCE


def test_preflight_reports_sky_source_without_radiance():
    pytest.importorskip("honeybee")
    from daylight_engine.honeybee.preflight import inspect_installation

    with patch(
        "daylight_engine.honeybee.preflight.resolve_gendaymtx",
        side_effect=FileNotFoundError("gendaymtx was not found"),
    ):
        report = inspect_installation("reference")
    assert report["sky_source"] == "foton"
    assert report["sky_sources"]["foton"]["available"]
    assert not report["sky_sources"]["gendaymtx"]["available"]
    assert report["gendaymtx"] is None
    assert not any("gendaymtx" in message for message in report["errors"])
    assert report["provenance"]["weather_version"].startswith("foton-sky-r")
