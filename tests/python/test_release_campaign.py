"""Frozen-input guards and faithful diagnostic campaign reporting."""

import hashlib
import json

import pytest

from scripts.summarize_release_campaign import summarize
from scripts.validate_release_suite import validate_models
from validation.scenes import (
    PLAN_FOOTPRINTS,
    WINDOW_PROFILES,
    SCENE_IDS,
    export_scenes,
    make_scene,
)


@pytest.mark.parametrize("family", PLAN_FOOTPRINTS)
@pytest.mark.parametrize("profile", WINDOW_PROFILES)
def test_plan_window_dimensions_position_and_materials(family, profile):
    from honeybee_radiance.modifier.material import Glass

    model = make_scene(f"plan_{family}_{profile}")
    points = PLAN_FOOTPRINTS[family]
    start, end = points[:2]  # Explicit lowest south-facing edge in these outlines.
    for face in model.faces:
        assert face.properties.radiance.modifier.average_reflectance == pytest.approx(
            0.5
        )
    for aperture in model.apertures:
        assert (
            aperture.properties.radiance.modifier.to_dict()
            == Glass.from_single_transmittance("clear", 0.6).to_dict()
        )
    if profile == "distributed":
        for aperture in model.apertures:
            assert aperture.area == pytest.approx(1.2)
            assert aperture.geometry.min.z == pytest.approx(0.8)
            assert aperture.geometry.max.z == pytest.approx(2)
        return
    aperture = model.apertures[0]
    assert aperture.normal.y == pytest.approx(-1)
    assert all(
        vertex.y == pytest.approx(start[1]) for vertex in aperture.geometry.boundary
    )
    low, high = aperture.geometry.min, aperture.geometry.max
    width = end[0] - start[0]
    if profile == "offset_low":
        assert low.x == pytest.approx(start[0] + 0.2)
        assert low.z == pytest.approx(0.2)
    elif profile == "offset_high":
        assert high.x == pytest.approx(end[0] - 0.2)
        assert low.z == pytest.approx(1.6)
    else:
        assert (low.x + high.x) / 2 == pytest.approx(start[0] + width / 2)
        assert (low.z + high.z) / 2 == pytest.approx(1.5)
    if profile in ("small_center", "large_center", "offset_low", "offset_high"):
        assert high.x - low.x == pytest.approx(
            2.4 if profile == "large_center" else 1.2
        )
        assert high.z - low.z == pytest.approx(2 if profile == "large_center" else 1.2)
    if profile == "triangle":
        assert len(aperture.geometry.boundary) == 3
        assert high.x - low.x == pytest.approx(2)
        assert high.z - low.z == pytest.approx(1.44)
    if profile == "circle":
        assert len(aperture.geometry.boundary) == 32
    if profile == "arch":
        assert len(aperture.geometry.boundary) == 19
        assert high.x - low.x == pytest.approx(1.2)


def test_complete_saved_corpus_is_accepted_including_original_acceptance_identifier():
    from pathlib import Path

    root = Path(__file__).resolve().parents[2]
    assert set(validate_models(root / "test_models/architectural", SCENE_IDS)) == set(
        SCENE_IDS
    )


@pytest.mark.parametrize("mutation", ("duplicate", "filename", "metadata", "units"))
def test_modified_fixture_manifest_or_model_is_rejected(tmp_path, mutation):
    folder = tmp_path / "models"
    manifest = export_scenes(folder, ("plan_cross_distributed",))
    record = manifest["scenes"][0]
    if mutation == "duplicate":
        manifest["scenes"].append(record)
        manifest["scene_count"] = 2
    elif mutation == "filename":
        record["file"] = "../other.hbjson"
    else:
        path = folder / record["file"]
        model = json.loads(path.read_text())
        if mutation == "metadata":
            model["user_data"]["validation_scene"]["window_profile"] = "wrong"
        else:
            model["units"] = "Feet"
        path.write_text(json.dumps(model))
        record["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    (folder / "manifest.json").write_text(json.dumps(manifest))
    with pytest.raises(ValueError):
        validate_models(folder, ("plan_cross_distributed",))


def test_campaign_report_distinguishes_inconclusive_failure_and_execution_error(
    tmp_path,
):
    records = [
        {
            "scene": "sealed",
            "sky_density": index % 2 + 1,
            "result_class": kind,
            "elapsed_seconds": 2.5,
            **(
                {"error": "missing executable", "error_type": "FileNotFoundError"}
                if kind == "execution_error"
                else {}
            ),
        }
        for index, kind in enumerate(
            ("passed", "accuracy_failure", "unstable_reference", "execution_error")
        )
    ]
    records[1]["coefficients"] = {
        "grids": [
            {
                "stages": {
                    "full": {
                        "absolute_error": {"maximum": 1.0},
                        "nmbe_percent": "inf",
                        "rms_normalized_rmse_percent": "inf",
                        "worst": {
                            "global_sensor_index": 3,
                            "sky_patch_index": 7,
                            "rgb_channel": 2,
                        },
                    }
                }
            }
        ]
    }
    records[2]["annual"] = {
        "grids": [
            {
                "illuminance": {
                    "maximum_absolute_error_lux": 123.0,
                    "worst": {"position": [1, 2, 0.75], "hour_of_year": 999.5},
                }
            }
        ]
    }
    records[2]["compatibility"] = {
        "official_loader": {"passed": True},
        "stock": {
            "passed": False,
            "reference_sky_density": 1,
            "candidate_sky_density": 2,
        },
    }
    suite = {
        "scenes": records,
        "selected_case_count": 180,
        "expected_case_count": 180,
        "dirty": True,
        "smoke": False,
        "status": "incomplete",
        "backend": "metal",
    }
    (tmp_path / "suite.json").write_text(json.dumps(suite))
    result = summarize(tmp_path)
    assert result["accounted"] == 4
    assert set(result["result_counts"]) == {
        "passed",
        "accuracy_failure",
        "unstable_reference",
        "execution_error",
    }
    text = (tmp_path / "campaign.md").read_text()
    assert "4/180" in text
    assert "10.0 s" in text
    assert "inconclusive" in text
    assert "missing executable" in text
    assert "3 / 7 / 2" in text
    assert "bias=inf%" in text
    assert "123.00 lux" in text
    assert "Compatibility failures" in text
    assert "reference MF:1, candidate MF:2" in text
