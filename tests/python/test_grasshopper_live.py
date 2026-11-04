"""Executable discovery, one-click install, the background worker and daylight factor."""

from __future__ import annotations

import json
import os
from pathlib import Path
import stat
import sys
from unittest.mock import patch

import numpy as np
import pytest

from grasshopper_foton import foton_gh

ROOT = Path(__file__).resolve().parents[2]
MODEL = ROOT / "test_models" / "architectural" / "teaching_office.hbjson"
WEATHER = ROOT / "epw" / "gothenburg.epw"


def _make_executable(path: Path, body: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")
    path.chmod(path.stat().st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
    return path


@pytest.fixture
def cli(tmp_path):
    """A ``foton-honeybee`` that runs this checkout's CLI in this interpreter."""
    if os.name == "nt":
        pytest.skip("the wrapper script is POSIX shell")
    wrapper = _make_executable(
        tmp_path / "bin" / "foton-honeybee",
        "#!/bin/sh\nexec '{0}' -m daylight_engine.honeybee \"$@\"\n".format(sys.executable),
    )
    yield str(wrapper)
    foton_gh.stop_workers()


# Discovery and install -------------------------------------------------------


def test_discovery_finds_fotons_own_environment_without_path(tmp_path, monkeypatch):
    monkeypatch.setenv("FOTON_HOME", str(tmp_path / "home"))
    monkeypatch.setenv("PATH", str(tmp_path / "empty"))
    monkeypatch.delenv("FOTON_HONEYBEE_EXE", raising=False)
    executable = Path(foton_gh.environment_executable())
    _make_executable(executable, "#!/bin/sh\n")
    assert foton_gh.candidate_executables()[0] == str(executable)
    assert Path(foton_gh.discover_executable()) == executable


def test_discovery_failure_points_to_install(tmp_path, monkeypatch):
    monkeypatch.setenv("FOTON_HOME", str(tmp_path / "home"))
    monkeypatch.setenv("PATH", str(tmp_path / "empty"))
    monkeypatch.delenv("FOTON_HONEYBEE_EXE", raising=False)
    monkeypatch.setattr(foton_gh, "candidate_executables", lambda: [str(tmp_path / "missing")])
    with pytest.raises(foton_gh.FotonError, match="install_"):
        foton_gh.discover_executable()


def test_candidates_cover_usual_python_folders(monkeypatch):
    monkeypatch.setattr(foton_gh, "_windows", lambda: False)
    candidates = foton_gh.candidate_executables()
    assert any("/Library/Frameworks/Python.framework/Versions/3.13/bin" in c for c in candidates)
    assert any(c.endswith(os.path.join(".local", "bin", "foton-honeybee")) for c in candidates)
    monkeypatch.setattr(foton_gh, "_windows", lambda: True)
    windows = foton_gh.candidate_executables()
    assert all(c.endswith("foton-honeybee.exe") for c in windows)
    assert any(os.path.join("Python313", "Scripts") in c for c in windows)


def test_engine_version_range_matches_this_release():
    import re

    # tomllib is Python 3.11+; CI also runs 3.10.
    text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    version = re.search(r'^version = "([^"]+)"', text, re.MULTILINE).group(1)
    # Main may still carry the previous patch number until the release bump;
    # from 0.3.2 on, the components must accept the engine they ship with.
    assert foton_gh._version_tuple(version)[:2] == foton_gh.ENGINE_MINIMUM[:2]
    if foton_gh._version_tuple(version) >= foton_gh.ENGINE_MINIMUM:
        assert foton_gh.engine_version_supported(version)
    assert not foton_gh.engine_version_supported("0.3.2")
    assert not foton_gh.engine_version_supported("0.4.0")
    assert foton_gh.engine_version_supported("0.3.3.dev1")
    assert ">=0.3.3,<0.4" in foton_gh.ENGINE_REQUIREMENT


def test_find_base_python_accepts_a_supported_interpreter():
    command, version = foton_gh.find_base_python(sys.executable)
    assert command == [os.path.abspath(sys.executable)]
    assert version == "%d.%d" % sys.version_info[:2]


def test_find_base_python_rejects_an_old_interpreter(tmp_path, monkeypatch):
    if os.name == "nt":
        pytest.skip("POSIX shell stand-in")
    old = _make_executable(tmp_path / "python3.9", "#!/bin/sh\necho 3.9\n")
    monkeypatch.setattr(foton_gh, "_base_python_candidates", lambda configured=None: [[str(old)]])
    with pytest.raises(foton_gh.FotonError, match="3.10 to 3.13"):
        foton_gh.find_base_python()


def test_install_is_skipped_when_a_supported_engine_is_present(tmp_path, monkeypatch):
    monkeypatch.setenv("FOTON_HOME", str(tmp_path))
    _make_executable(Path(foton_gh.environment_executable()), "#!/bin/sh\n")
    with patch.object(foton_gh, "capabilities", return_value={"engine_version": "0.3.3"}), \
            patch.object(foton_gh, "_stream_command") as run:
        assert foton_gh.install_foton() == foton_gh.environment_executable()
    run.assert_not_called()


def test_install_creates_environment_then_pip_installs(tmp_path, monkeypatch):
    monkeypatch.setenv("FOTON_HOME", str(tmp_path))
    commands = []

    def fake(command, on_line=None, cancel=None, timeout=None):
        commands.append(command)
        if command[1:3] == ["-m", "venv"]:
            _make_executable(Path(foton_gh._environment_file(command[3], "python")), "")
        if "pip" in command:
            _make_executable(Path(foton_gh.environment_executable()), "")
        return 0, []

    with patch.object(foton_gh, "find_base_python", return_value=(["/fake/python3"], "3.12")), \
            patch.object(foton_gh, "_stream_command", side_effect=fake):
        assert foton_gh.install_foton() == foton_gh.environment_executable()
    assert commands[0] == ["/fake/python3", "-m", "venv", foton_gh.environment_folder()]
    assert commands[1][1:4] == ["-m", "pip", "install"]
    assert commands[1][-1] == foton_gh.ENGINE_REQUIREMENT


def test_install_uses_uv_when_no_python_is_found(tmp_path, monkeypatch):
    monkeypatch.setenv("FOTON_HOME", str(tmp_path))
    calls = []

    def fake(command, on_line=None, cancel=None, timeout=None, extra_env=None):
        calls.append((command, extra_env))
        if command[1:2] == ["venv"]:
            _make_executable(Path(foton_gh._environment_file(command[-1], "python")), "")
        if "pip" in command:
            _make_executable(Path(foton_gh.environment_executable()), "")
        return 0, []

    missing = foton_gh.FotonError("Foton needs Python 3.10 to 3.13")
    with patch.object(foton_gh, "find_base_python", side_effect=missing), \
            patch.object(foton_gh, "ensure_uv", return_value="/fake/uv"), \
            patch.object(foton_gh, "_stream_command", side_effect=fake):
        assert foton_gh.install_foton() == foton_gh.environment_executable()
    venv, environment = calls[0]
    assert venv == ["/fake/uv", "venv", "--seed", "--python", foton_gh.UV_PYTHON,
                    foton_gh.environment_folder()]
    # uv's Python and cache stay inside Foton's folder.
    assert environment["UV_PYTHON_INSTALL_DIR"].startswith(str(tmp_path))
    assert environment["UV_CACHE_DIR"].startswith(str(tmp_path))
    assert calls[1][0][1:4] == ["-m", "pip", "install"]


def test_install_does_not_swap_a_python_the_user_chose(tmp_path, monkeypatch):
    monkeypatch.setenv("FOTON_HOME", str(tmp_path))
    missing = foton_gh.FotonError("Foton needs Python 3.10 to 3.13")
    with patch.object(foton_gh, "find_base_python", side_effect=missing), \
            patch.object(foton_gh, "ensure_uv") as uv:
        with pytest.raises(foton_gh.FotonError):
            foton_gh.install_foton(python="/opt/python3.9")
    uv.assert_not_called()


@pytest.mark.parametrize(
    "system, machine, asset",
    [
        ("macos", "arm64", "uv-aarch64-apple-darwin.tar.gz"),
        ("macos", "x86_64", "uv-x86_64-apple-darwin.tar.gz"),
        ("windows", "x86_64", "uv-x86_64-pc-windows-msvc.zip"),
        ("windows", "arm64", "uv-aarch64-pc-windows-msvc.zip"),
    ],
)
def test_uv_download_matches_the_computer(monkeypatch, system, machine, asset):
    monkeypatch.setattr(foton_gh, "_system", lambda: system)
    monkeypatch.setattr(foton_gh, "_machine", lambda: machine)
    assert foton_gh.uv_asset() == asset


def test_ensure_uv_unpacks_the_binary_into_fotons_folder(tmp_path, monkeypatch):
    if os.name == "nt":
        pytest.skip("POSIX tar stand-in")
    monkeypatch.setenv("FOTON_HOME", str(tmp_path))
    import tarfile

    source = tmp_path / "src" / "uv-aarch64-apple-darwin"
    _make_executable(source / "uv", "#!/bin/sh\necho uv\n")
    built = tmp_path / "uv.tar.gz"
    with tarfile.open(built, "w:gz") as archive:
        archive.add(source, arcname=source.name)

    def fake(command, on_line=None, cancel=None, timeout=None, extra_env=None):
        if command[1] == "-fsSL":
            Path(command[command.index("-o") + 1]).write_bytes(built.read_bytes())
            return 0, []
        return foton_gh.subprocess.call(["tar"] + command[1:]), []

    with patch.object(foton_gh, "_stream_command", side_effect=fake):
        path = foton_gh.ensure_uv()
    assert path == foton_gh.uv_executable()
    assert os.access(path, os.X_OK)
    assert [p.name for p in tmp_path.iterdir() if p.name.startswith("uv-")] == []


# Bounce default ---------------------------------------------------------------


def test_grasshopper_runs_default_to_the_validated_bounce_depth(tmp_path):
    from foton.honeybee.annual import DEFAULT_MAXIMUM_BOUNCES

    assert foton_gh.DEFAULT_BOUNCES == DEFAULT_MAXIMUM_BOUNCES
    executable = _make_executable(tmp_path / "foton-honeybee", "")
    commands = []
    with patch.object(foton_gh, "_run_process", side_effect=lambda c, **_: commands.append(c) or {}), \
            patch.object(foton_gh, "load_result_bundle", return_value={}):
        foton_gh.run_annual_daylight(str(MODEL), str(WEATHER), str(tmp_path / "out"),
                                     executable=str(executable), reuse=False)
    command = commands[0]
    assert command[command.index("--maximum-bounces") + 1] == str(DEFAULT_MAXIMUM_BOUNCES)
    components = ROOT / "grasshopper_foton" / "components"
    for name in ("Foton Annual Daylight.py", "Foton Daylight Factor.py"):
        source = (components / name).read_text(encoding="utf-8")
        assert 'maximum_bounces=optional("bounces_")' in source


# Engine side: daylight factor and the worker ---------------------------------


def test_daylight_factor_matches_the_engine_and_honeybee_layout(tmp_path):
    from foton.honeybee import HoneybeeStudy

    study = HoneybeeStudy(str(MODEL), backend="reference")
    run = study.daylight_factor(quality="preview", output_folder=tmp_path)
    rows = 146
    native = study.scene.analyze(
        np.zeros((rows, 1, 3), dtype=np.float32), np.ones(1, dtype=np.float32),
        quality="preview", metrics=["da"], direct_samples=1, maximum_samples=64,
        maximum_bounces=8, scene_seed=0, export_coefficients=True,
    ).result()
    expected = np.asarray(native.daylight_factor(), dtype=np.float32)
    values = np.concatenate([grid.values for grid in run.grids])
    np.testing.assert_allclose(values, expected, rtol=1e-5, atol=1e-6)
    info = json.loads((tmp_path / "results" / "grids_info.json").read_text())
    assert [item["full_id"] for item in info] == [g.full_identifier for g in run.grids]
    written = np.loadtxt(tmp_path / "results" / (run.grids[0].full_identifier + ".res"))
    assert written.shape == (run.grids[0].sensor_count,)


def test_daylight_factor_and_annual_share_traced_coefficients():
    from foton.honeybee import HoneybeeStudy

    first = HoneybeeStudy(str(MODEL), backend="reference")
    annual = first.annual_daylight(str(WEATHER), quality="preview")
    factor = first.daylight_factor(quality="preview")
    assert factor.metadata["solver"]["coefficient_cache_hit"] is True
    second = HoneybeeStudy(str(MODEL), backend="reference")
    second.daylight_factor(quality="preview")
    again = second.annual_daylight(str(WEATHER), quality="preview")
    assert again.metadata["solver"]["coefficient_cache_hit"] is True
    for left, right in zip(annual.grids, again.grids):
        np.testing.assert_array_equal(left.da, right.da)
        np.testing.assert_array_equal(left.udi, right.udi)


def test_daylight_factor_cli_writes_a_manifest(tmp_path):
    from daylight_engine.honeybee.__main__ import main

    output = tmp_path / "df"
    assert main(["daylight-factor", "--model", str(MODEL), "--output", str(output),
                 "--backend", "reference", "--quality", "preview"]) == 0
    bundle = foton_gh.load_result_bundle(str(output))
    assert bundle["grid_ids"] == ["teaching_office_grid"]
    assert bundle["results"] == [str(output / "results")]
    assert len(bundle["df"][0]) == 96 and bundle["mean_df"][0] > 0


def test_live_annual_matches_a_saved_run_and_reuses_coefficients(cli, tmp_path):
    common = dict(executable=cli, backend="reference", quality="preview")
    saved = foton_gh.run_annual_daylight(str(MODEL), str(WEATHER), str(tmp_path / "saved"),
                                         reuse=False, **common)
    live = foton_gh.run_annual_daylight(str(MODEL), str(WEATHER), str(tmp_path / "unused"),
                                        live=True, **common)
    assert live["da"] == saved["da"] and live["udi"] == saved["udi"]
    assert live["sda"] == pytest.approx(saved["sda"])
    assert live["results"] == [] and live["folder"] is None
    assert not (tmp_path / "unused").exists()
    assert live["manifest"]["worker"] == {"study_reused": False}

    changed = foton_gh.run_annual_daylight(str(MODEL), str(WEATHER), str(tmp_path / "unused"),
                                           live=True, thresholds_value="-t 500", **common)
    assert changed["manifest"]["worker"] == {"study_reused": True}
    assert changed["timings"]["coefficient_trace_seconds"] == 0.0
    assert changed["da"] != live["da"]

    factor = foton_gh.run_daylight_factor(str(MODEL), str(tmp_path / "unused"), live=True, **common)
    assert factor["timings"]["coefficient_trace_seconds"] == 0.0
    saved_factor = foton_gh.run_daylight_factor(str(MODEL), str(tmp_path / "df"), **common)
    assert factor["df"] == saved_factor["df"]
    assert saved_factor["results"] and os.path.isdir(saved_factor["results"][0])


def test_worker_survives_a_failed_request(cli, tmp_path):
    broken = tmp_path / "broken.hbjson"
    broken.write_text("{}", encoding="utf-8")
    with pytest.raises(foton_gh.FotonError):
        foton_gh.run_daylight_factor(str(broken), str(tmp_path), executable=cli,
                                     backend="reference", quality="preview", live=True)
    workers = foton_gh._worker_registry()
    process = next(iter(workers.values()))["process"]
    assert process.poll() is None
    result = foton_gh.run_daylight_factor(str(MODEL), str(tmp_path), executable=cli,
                                          backend="reference", quality="preview", live=True)
    assert result["grid_ids"] == ["teaching_office_grid"]
    assert next(iter(workers.values()))["process"] is process


def test_cancelling_stops_the_worker_and_the_next_run_restarts_it(cli, tmp_path):
    with pytest.raises(foton_gh.FotonCancelled):
        foton_gh.run_daylight_factor(str(MODEL), str(tmp_path), executable=cli,
                                     backend="reference", quality="preview", live=True,
                                     cancel=lambda: True)
    assert foton_gh._worker_registry() == {}
    result = foton_gh.run_daylight_factor(str(MODEL), str(tmp_path), executable=cli,
                                          backend="reference", quality="preview", live=True)
    assert len(result["df"][0]) == 96


def test_worker_protocol_keeps_library_output_off_stdout():
    import io
    from daylight_engine.honeybee.worker import serve

    requests = io.StringIO('{"id": "a", "command": "ping"}\nnot json\n{"id": "b", "command": "shutdown"}\n')
    replies = io.StringIO()
    assert serve(requests, replies) == 0
    events = [json.loads(line) for line in replies.getvalue().splitlines()]
    assert [e["event"] for e in events] == ["ready", "complete", "failed", "complete"]
    assert events[1]["request_id"] == "a" and events[3]["request_id"] == "b"


def test_worker_keeps_weather_in_memory_across_studies_with_identical_results(tmp_path):
    import shutil
    from daylight_engine.honeybee.weather import prepare_annual_weather
    from daylight_engine.honeybee.worker import Worker

    # The bridge copies the EPW to a new temporary path on every request.
    first_copy = tmp_path / "a" / "weather.epw"
    second_copy = tmp_path / "b" / "weather.epw"
    for copy in (first_copy, second_copy):
        copy.parent.mkdir()
        shutil.copy2(WEATHER, copy)
    memo = {}
    cache = tmp_path / "cache"
    first = prepare_annual_weather(first_copy, cache_directory=cache, memo=memo)
    second = prepare_annual_weather(second_copy, cache_directory=cache, memo=memo)
    assert second.sky is first.sky and not second.sky.flags.writeable
    assert second.source == str(second_copy.resolve()) and second.cache_hit
    assert second.weather_id == first.weather_id
    assert prepare_annual_weather(first_copy, north=10, cache_directory=cache, memo=memo).sky is not first.sky

    class Collect:
        def __init__(self):
            self.events = []

        def emit(self, event, **fields):
            self.events.append(dict(fields, event=event))

    def live(worker, model, weather):
        writer = Collect()
        options = {"model": str(model), "wea": str(weather), "backend": "reference",
                   "quality": "preview"}
        worker.handle({"id": "1", "command": "annual-daylight", "options": options}, writer)
        return writer.events[-1]["manifest"]

    other = ROOT / "test_models" / "architectural" / "teaching_depth6.hbjson"
    warm = Worker()
    live(warm, other, first_copy)
    reused = live(warm, MODEL, second_copy)
    assert len(warm.weather_memo) == 1
    fresh = live(Worker(), MODEL, first_copy)
    assert reused["grids"] == fresh["grids"]
