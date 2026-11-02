from pathlib import Path
import json
import shutil
import sys
from unittest.mock import patch

import numpy as np
import pytest

from foton_bridge import portable_manifest, resolve_manifest, reusable, reuse_identity
from foton.honeybee.adapter import prepare_honeybee_scene
from foton.honeybee.radiance import resolve_radiance_executables
from honeybee_foton.results import load_manifest
from grasshopper_foton.foton_gh import load_result_bundle
from validation.scenes import SCENE_IDS, SCENE_VERSION, make_scene
from validation.oracle import patch_samples, difference

ROOT = Path(__file__).resolve().parents[2]


def capabilities():
    return {
        "quality_settings": {"final": {"direct_samples": 64, "maximum_samples": 4096}},
        "provenance": {
            "engine_version": "0.2.0",
            "solver_revision": "v5",
            "selected_backend": "metal",
            "weather_version": "rad1",
        },
    }


@pytest.mark.parametrize(
    "field",
    ["engine_version", "solver_revision", "selected_backend", "weather_version"],
)
def test_reuse_invalidated_by_provenance(field):
    request = {"quality": "final", "direct_samples": None, "maximum_samples": None}
    first = capabilities()
    second = capabilities()
    second["provenance"][field] = "changed"
    assert reuse_identity(request, first) != reuse_identity(request, second)
    assert reuse_identity(request, {}) is None
    assert not reusable({"status": "complete"}, reuse_identity(request, first))


def test_resolved_presets_participate_in_identity():
    implicit = {"quality": "final", "direct_samples": None, "maximum_samples": None}
    explicit = dict(implicit, direct_samples=64, maximum_samples=4096)
    assert reuse_identity(implicit, capabilities()) == reuse_identity(
        explicit, capabilities()
    )
    changed = capabilities()
    changed["quality_settings"]["final"]["maximum_samples"] = 8192
    assert reuse_identity(implicit, capabilities()) != reuse_identity(implicit, changed)


def test_portable_result_can_move_and_load_in_both_bridges(tmp_path):
    from test_grasshopper_foton import write_metric_manifest

    old = tmp_path / "old"
    manifest = write_metric_manifest(old)
    portable = portable_manifest(manifest, str(old))
    (old / "run_manifest.json").write_text(json.dumps(portable))
    new = tmp_path / "moved"
    shutil.move(str(old), str(new))
    loaded = load_manifest(new)
    assert loaded["output_folder"] == str(new)
    assert load_result_bundle(str(new))["da"] == [[0.0, 1.0], [1.0]]
    # Existing absolute-path manifests remain readable.
    assert resolve_manifest(manifest, str(new / "run_manifest.json"))[
        "output_folder"
    ] == str(old)


def test_configured_radiance_directory_uses_executable_resolution(tmp_path):
    calls = []

    def locate(command):
        calls.append(command)
        return command + ".exe" if str(tmp_path) in command else None

    with patch("daylight_engine.honeybee.radiance.shutil.which", side_effect=locate):
        found = resolve_radiance_executables(tmp_path)
    assert found["oconv"].endswith("oconv.exe")
    assert all(str(tmp_path) in value for value in found.values())


@pytest.mark.parametrize("identifier", SCENE_IDS)
def test_validation_scene_is_valid_and_units_are_equivalent(identifier):
    model = make_scene(identifier, ROOT)
    original = prepare_honeybee_scene(
        model, include_aperture_glazing=identifier != "black_open"
    )
    model.convert_to_units("Millimeters")
    converted = prepare_honeybee_scene(
        model, include_aperture_glazing=identifier != "black_open"
    )
    np.testing.assert_allclose(
        original.arrays["vertices"], converted.arrays["vertices"], atol=1e-5
    )
    np.testing.assert_allclose(
        original.arrays["sensor_positions"],
        converted.arrays["sensor_positions"],
        atol=1e-5,
    )
    assert [g["identifier"] for g in original.grid_info] == [
        g["identifier"] for g in converted.grid_info
    ]
    if identifier == "acceptance":
        assert [g["sensor_count"] for g in original.grid_info] == [175, 960, 885]


@pytest.mark.parametrize("density,rows", [(1, 146), (2, 578)])
def test_independent_sky_sampler_covers_sphere(density, rows):
    rays, weights = patch_samples(density, 128)
    assert rays.shape == (rows, 128, 3)
    np.testing.assert_allclose(np.linalg.norm(rays, axis=2), 1, atol=1e-6)
    assert weights.sum() == pytest.approx(4 * np.pi)
    assert np.all(rays[0, :, 2] < 0)
    assert np.all(rays[1:, :, 2] > 0)
    assert not np.array_equal(rays, patch_samples(density, 128, seed=2)[0])


def test_darkness_and_nonfinite_values_cannot_pass_convergence():
    assert difference(np.zeros(4), np.zeros(4))["passed"]
    assert not difference(np.zeros(4), np.ones(4) * 0.001)["passed"]
    assert not difference(np.zeros(4), np.full(4, np.nan))["passed"]


def test_release_gate_rejects_missing_or_stale_evidence():
    from scripts.verify_release_evidence import verify, RHINO_SCENARIOS

    suite = {
        "commit": "abc",
        "engine_version": "0.2.0",
        "suite_version": SCENE_VERSION,
        "status": "passed",
        "passed": True,
        "dirty": False,
        "smoke": False,
        "backend": "metal",
        "hardware": {"system": "Darwin"},
        "scenes": [
            {
                "scene": name,
                "sky_density": d,
                "passed": True,
                "gpu_executed": True,
                "oracle_stable": True,
            }
            for name in SCENE_IDS
            for d in (1, 2)
        ],
    }
    rhino = {
        "commit": "abc",
        "engine_version": "0.2.0",
        "rhino_version": "8.35",
        "backend": "metal",
        "system": "Darwin",
        "tested_at": "2026-09-15",
        "notes": "isolated test environment",
        "scenarios": dict.fromkeys(RHINO_SCENARIOS, True),
    }
    assert not verify(suite, rhino, "abc", "metal", "Darwin", "0.2.0")
    assert verify(suite, rhino, "new", "metal", "Darwin", "0.2.0")
    assert verify(suite, {}, "abc", "metal", "Darwin", "0.2.0")
    suite["scenes"][0]["gpu_executed"] = False
    assert verify(suite, rhino, "abc", "metal", "Darwin", "0.2.0")


def test_invalid_process_output_reaps_child(tmp_path):
    from honeybee_foton import FotonClient, AnnualDaylightRequest

    with patch("honeybee_foton.client.subprocess.Popen") as popen:
        process = popen.return_value
        process.stdout = iter(["not-json\n"])
        process.stderr = iter([])
        process.poll.return_value = None
        process.wait.return_value = 0
        client = FotonClient(sys.executable)
        with pytest.raises(ValueError, match="not valid JSON"):
            client.run_annual_daylight(
                AnnualDaylightRequest("model", "weather", str(tmp_path / "output"))
            )
        process.terminate.assert_called_once()
        process.wait.assert_called()


def test_missing_metric_invalidates_reuse(tmp_path):
    from test_grasshopper_foton import write_metric_manifest

    manifest = write_metric_manifest(tmp_path)
    identity = reuse_identity(
        {"quality": "final", "export_illuminance": False}, capabilities()
    )
    manifest["reuse_identity"] = identity
    for key in ("metadata", "grid_summary"):
        path = tmp_path / key
        path.write_text("test")
        manifest[key] = str(path)
    assert reusable(manifest, identity)
    Path(manifest["grids"][0]["metrics"]["da"]).unlink()
    assert not reusable(manifest, identity)


def test_ironpython_capabilities_waits_for_exit(tmp_path):
    from grasshopper_foton.foton_gh import capabilities as inspect

    executable = tmp_path / "foton-honeybee"
    executable.touch()
    payload = {"protocol": "foton.honeybee", "protocol_version": 1}
    with patch("grasshopper_foton.foton_gh.subprocess.Popen") as popen:
        process = popen.return_value
        process.communicate.return_value = (json.dumps(payload), "")
        process.returncode = None
        process.wait.return_value = 0
        assert inspect(str(executable))["protocol_version"] == 1
        process.wait.assert_called_once()


def test_ironpython_cancellation_uses_dotnet_process():
    from types import SimpleNamespace
    from unittest.mock import Mock
    from grasshopper_foton.foton_gh import _signal_process

    native = SimpleNamespace(Kill=Mock())
    child = SimpleNamespace(poll=lambda: None, process=native)
    _signal_process(child)
    native.Kill.assert_called_once()


def test_packaged_components_match_current_sources():
    from scripts.package_grasshopper import verify_build

    assert verify_build()["round_trip_passed"]


@pytest.mark.parametrize("north", [0, 90, 180, -90])
def test_north_rotation_matches_numeric_and_vector_inputs(north):
    from grasshopper_foton.foton_gh import north_angle
    from types import SimpleNamespace

    angle = np.deg2rad(north)
    vector = SimpleNamespace(X=-np.sin(angle), Y=np.cos(angle))
    assert north_angle(vector) == pytest.approx(north)
