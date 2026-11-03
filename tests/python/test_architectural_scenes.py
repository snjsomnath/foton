"""Geometry contracts and physical interactions for the architectural corpus.

Reference-backend transport checks are deterministic diagnostics, not substitutes
for the converged Radiance and actual-GPU release comparisons.
"""

from functools import lru_cache
import hashlib
import json

import numpy as np
import pytest

from foton import Engine
from foton.honeybee.adapter import prepare_honeybee_scene
from validation.scenes import (
    SCENE_CATEGORIES,
    SCENE_IDS,
    SCENE_SPECS,
    SCENE_VERSION,
    PLAN_FOOTPRINTS,
    WINDOW_PROFILES,
    export_scenes,
    main,
    make_scene,
    scene_dict,
    scene_metadata,
)


@lru_cache(maxsize=None)
def scene(identifier):
    model = make_scene(identifier)
    prepared = prepare_honeybee_scene(
        model, include_aperture_glazing=scene_metadata(identifier)["include_glazing"]
    )
    return model, prepared


def analyze(prepared, *, reflected=False, rows=146):
    engine = Engine({"backend": "reference"})
    result = (
        prepared.create_native_scene(engine)
        .analyze(
            np.ones((rows, 1, 3), dtype=np.float32),
            np.ones(1, dtype=np.float32),
            quality="final",
            direct_samples=64,
            maximum_samples=256 if reflected else 0,
            maximum_bounces=1 if reflected else 0,
            scene_seed=0,
            export_coefficients=True,
        )
        .result()
    )
    return np.asarray(result.coefficients())


@lru_cache(maxsize=None)
def coefficients(identifier, reflected=False, rows=146):
    return analyze(scene(identifier)[1], reflected=reflected, rows=rows)


def test_corpus_has_distinct_documented_architectural_questions():
    assert len(SCENE_IDS) == len(set(SCENE_IDS)) == 106
    assert len({spec.question for spec in SCENE_SPECS}) == len(SCENE_IDS)
    assert set(SCENE_CATEGORIES) == {
        "controls",
        "form",
        "orientation",
        "openings",
        "shading",
        "context",
        "materials",
        "connections",
        "integration",
        "teaching",
    }
    assert sum(spec.category == "teaching" for spec in SCENE_SPECS) == 16
    assert all(spec.interactions and spec.room_count > 0 for spec in SCENE_SPECS)
    with pytest.raises(ValueError, match="Unknown validation scene"):
        scene_metadata("not_a_scene")


@pytest.mark.parametrize("identifier", SCENE_IDS)
def test_models_are_valid_with_workplanes_inside_their_rooms(identifier):
    from ladybug_geometry.geometry3d import Point3D, Vector3D

    model, prepared = scene(identifier)
    assert model.check_all(raise_exception=False, detailed=True) == []
    assert len(model.rooms) == scene_metadata(identifier)["room_count"]
    assert not prepared.validation_warnings
    assert not model.doors
    assert not model.orphaned_apertures
    assert len(prepared.grid_info) == len(model.rooms)
    assert all(np.isfinite(array).all() for array in prepared.arrays.values())
    assert np.all(prepared.arrays["sensor_area_weights"] > 0)
    np.testing.assert_allclose(
        np.linalg.norm(prepared.arrays["sensor_normals"], axis=1), 1, atol=1e-6
    )
    rooms = {room.identifier: room for room in model.rooms}
    for grid in model.properties.radiance.sensor_grids:
        room = rooms[grid.room_identifier]
        assert grid.count > 0
        assert all(
            room.geometry.is_point_inside(
                Point3D(*sensor.pos), Vector3D(1, 0.271, 0.173)
            )
            for sensor in grid.sensors
        ), (identifier, grid.identifier)


@pytest.mark.parametrize("identifier", SCENE_IDS)
def test_generation_and_hbjson_roundtrip_preserve_transport_contract(identifier):
    from honeybee.model import Model
    from honeybee_radiance.writer import model_to_rad

    model, prepared = scene(identifier)
    assert model.to_dict() == make_scene(identifier).to_dict()
    reloaded = Model.from_dict(json.loads(json.dumps(model.to_dict())))
    restored = prepare_honeybee_scene(
        reloaded, include_aperture_glazing=scene_metadata(identifier)["include_glazing"]
    )
    assert restored.model_fingerprint == prepared.model_fingerprint
    for key, expected in prepared.arrays.items():
        np.testing.assert_array_equal(restored.arrays[key], expected)
    geometry, materials = model_to_rad(reloaded)
    assert "polygon" in geometry
    assert "plastic" in materials
    assert "glass" in materials or not model.apertures


@pytest.mark.parametrize("identifier", SCENE_IDS)
@pytest.mark.parametrize("rows", (146, 578))
def test_reference_transport_is_finite_nonnegative_and_sealed_room_is_dark(
    identifier, rows
):
    values = coefficients(identifier, reflected=True, rows=rows)
    assert values.shape == (
        len(scene(identifier)[1].arrays["sensor_positions"]),
        rows,
        3,
    )
    assert np.isfinite(values).all()
    assert np.all(values >= 0)
    if identifier == "sealed":
        assert not values.any()
    else:
        assert values.sum() > 0


@pytest.mark.parametrize(
    "identifier",
    (
        "overhang_fins",
        "deep_overhang",
        "asymmetric_fins",
        "horizontal_louvres",
        "vertical_louvres",
        "eggcrate",
        "light_shelf",
        "balcony_above",
        "recessed_window",
        "context_obstruction",
        "urban_canyon",
        "courtyard_context",
        "offset_tower",
    ),
)
def test_opaque_shading_cannot_add_direct_sky_light(identifier):
    base = coefficients("side_lit_reference")
    shaded = coefficients(identifier)
    assert shaded.shape == base.shape
    assert np.all(shaded <= base + 1e-6)
    assert shaded.sum() < base.sum() * 0.999


def test_eggcrate_retains_both_horizontal_and_vertical_shading_masks():
    combined = coefficients("eggcrate")
    for identifier in ("horizontal_louvres", "vertical_louvres"):
        assert np.all(combined <= coefficients(identifier) + 1e-6)
        assert combined.sum() < coefficients(identifier).sum()


def test_material_changes_preserve_direct_light_and_change_reflected_light():
    direct = coefficients("side_lit_reference")
    for identifier in ("dark_interior", "bright_ceiling", "coloured_walls"):
        np.testing.assert_allclose(coefficients(identifier), direct, atol=1e-6)
    full = coefficients("side_lit_reference", reflected=True)
    assert coefficients("dark_interior", reflected=True).sum() < full.sum()
    assert coefficients("bright_ceiling", reflected=True).sum() > full.sum()
    coloured = coefficients("coloured_walls", reflected=True)
    assert coloured[:, :, 0].sum() > coloured[:, :, 1].sum() > coloured[:, :, 2].sum()
    dimmed = coefficients("low_transmittance")
    assert 0 < dimmed.sum() < direct.sum()
    assert np.all(dimmed <= direct + 1e-6)


def test_reflective_neighbour_changes_reflection_without_changing_direct_mask():
    np.testing.assert_allclose(
        coefficients("reflective_neighbour"),
        coefficients("context_obstruction"),
        atol=1e-6,
    )
    assert (
        coefficients("reflective_neighbour", reflected=True).sum()
        > coefficients("context_obstruction", reflected=True).sum()
    )


@pytest.mark.parametrize(
    "identifier,pairs",
    (
        ("interior_glazing", 1),
        ("three_room_chain", 2),
        ("glazed_corridor", 2),
        ("atrium_borrowed_light", 2),
    ),
)
def test_borrowed_light_pairs_are_exported_once_and_all_zones_receive_light(
    identifier, pairs
):
    model, prepared = scene(identifier)
    internal = [
        ap
        for ap in model.apertures
        if ap.boundary_condition.__class__.__name__ == "Surface"
    ]
    assert len(internal) == pairs * 2
    paired = prepared.geometry_info["surface_aperture_pairs"]
    assert len(paired) == pairs
    assert all(pair["exported_aperture_identifier"] for pair in paired)
    values = coefficients(identifier, reflected=True)
    for grid in prepared.grid_info:
        start, count = grid["start_sensor_index"], grid["sensor_count"]
        assert values[start : start + count].sum() > 0, (identifier, grid["identifier"])


def test_opaque_shared_slab_prevents_light_leaking_between_storeys():
    model = make_scene("stacked_rooms")
    for face in model.rooms[0].faces:
        face.remove_sub_faces()
    prepared = prepare_honeybee_scene(model, include_aperture_glazing=True)
    values = analyze(prepared, reflected=True)
    lower, upper = prepared.grid_info
    assert not values[
        lower["start_sensor_index"] : lower["start_sensor_index"]
        + lower["sensor_count"]
    ].any()
    assert values[upper["start_sensor_index"] :].sum() > 0


@pytest.mark.parametrize(
    "identifier,normal",
    (
        ("side_lit_reference", (0, -1, 0)),
        ("north_facing", (0, 1, 0)),
        ("east_facing", (1, 0, 0)),
        ("west_facing", (-1, 0, 0)),
    ),
)
def test_orientation_cases_have_the_intended_glazing_normal(identifier, normal):
    np.testing.assert_allclose(
        tuple(scene(identifier)[0].apertures[0].normal), normal, atol=1e-6
    )


def test_oblique_rotation_transforms_shades_and_workplanes_together():
    from ladybug_geometry.geometry3d import Point3D

    model = make_scene("rotated_37")
    model.rotate_xy(-37, Point3D(3, 3, 0))
    original = make_scene("overhang_fins")
    np.testing.assert_allclose(tuple(model.apertures[0].normal), (0, -1, 0), atol=1e-6)
    for actual, expected in zip(model.shades, original.shades):
        np.testing.assert_allclose(
            [tuple(p) for p in actual.geometry.boundary],
            [tuple(p) for p in expected.geometry.boundary],
            atol=1e-6,
        )
    np.testing.assert_allclose(
        [sensor.pos for sensor in model.properties.radiance.sensor_grids[0].sensors],
        [sensor.pos for sensor in original.properties.radiance.sensor_grids[0].sensors],
        atol=1e-6,
    )


def test_sample_export_contains_all_reloadable_models_and_hashes(tmp_path):
    from honeybee.model import Model

    folder = tmp_path / "models"
    manifest = export_scenes(folder)
    assert manifest["scene_count"] == len(SCENE_IDS)
    assert manifest["suite_version"] == SCENE_VERSION
    assert len(list(folder.glob("*.hbjson"))) == len(SCENE_IDS)
    for record in manifest["scenes"]:
        path = folder / record["file"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == record["sha256"]
        reloaded = Model.from_hbjson(str(path))
        assert reloaded.user_data["validation_scene"] == scene_metadata(
            record["identifier"]
        )
        assert len(reloaded.rooms) == record["room_count"]
    with pytest.raises(FileExistsError):
        export_scenes(folder)


def test_scene_cli_filters_categories_and_lists_without_exporting(capsys):
    assert main(["--list", "--category", "orientation"]) == 0
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == 4
    assert all("[orientation]" in line for line in lines)


def test_saved_sample_corpus_matches_current_generator_and_manifest():
    from pathlib import Path

    folder = Path(__file__).resolve().parents[2] / "test_models/architectural"
    manifest = json.loads((folder / "manifest.json").read_text())
    assert manifest["suite_version"] == SCENE_VERSION
    assert manifest["scene_count"] == len(SCENE_IDS)
    assert {record["identifier"] for record in manifest["scenes"]} == set(SCENE_IDS)
    for record in manifest["scenes"]:
        path = folder / record["file"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == record["sha256"]
        assert json.loads(path.read_text()) == scene_dict(
            make_scene(record["identifier"])
        )


def test_model_hashes_are_reproducible_across_python_hash_seeds():
    import os
    from pathlib import Path
    import subprocess
    import sys

    root = Path(__file__).resolve().parents[2]
    records = json.loads(
        (root / "test_models/architectural/manifest.json").read_text()
    )["scenes"]
    expected = {record["identifier"]: record["sha256"] for record in records}
    script = (
        "import hashlib,json; from validation.scenes import SCENE_IDS,make_scene,scene_dict; "
        "print(json.dumps({i:hashlib.sha256((json.dumps(scene_dict(make_scene(i)),"
        "sort_keys=True,indent=2)+chr(10)).encode()).hexdigest() for i in SCENE_IDS}))"
    )
    for seed in ("1", "2"):
        actual = subprocess.check_output(
            [sys.executable, "-c", script],
            cwd=root,
            env={**os.environ, "PYTHONHASHSEED": seed},
            text=True,
        )
        assert json.loads(actual) == expected


@pytest.mark.parametrize(
    "selection,expected,status",
    (
        ([], len(SCENE_IDS) * 2, "passed"),
        (["--category", "connections"], 12, "incomplete"),
        (
            [
                "--scene",
                "rooflit",
                "--scene",
                "rooflit",
                "--sky-density",
                "1",
                "--sky-density",
                "1",
            ],
            1,
            "incomplete",
        ),
    ),
)
def test_comparison_runner_counts_cases_and_cannot_qualify_a_subset(
    monkeypatch, tmp_path, selection, expected, status
):
    import sys
    from types import SimpleNamespace
    import scripts.validate_release_suite as suite

    output = tmp_path / "suite"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "validate_release_suite",
            "--backend",
            "metal",
            "--output",
            str(output),
            *selection,
        ],
    )
    monkeypatch.setattr(suite, "hardware", lambda: {"system": "Darwin"})
    monkeypatch.setattr(
        suite,
        "Engine",
        lambda config: SimpleNamespace(
            capabilities=lambda: {"hardware_acceleration": True}
        ),
    )
    monkeypatch.setattr(
        suite.subprocess,
        "check_output",
        lambda command, **kwargs: "abc\n" if "rev-parse" in command else "",
    )
    monkeypatch.setattr(
        suite,
        "run_scene",
        lambda args, name, density, folder: {
            "scene": name,
            "sky_density": density,
            "status": "passed",
            "passed": True,
        },
    )
    assert suite.main() == (0 if status == "passed" else 1)
    report = json.loads((output / "suite.json").read_text())
    assert report["expected_case_count"] == len(SCENE_IDS) * 2
    assert report["selected_case_count"] == len(report["scenes"]) == expected
    assert report["status"] == status


def test_release_evidence_rejects_a_truncated_or_duplicated_corpus():
    from scripts.verify_release_evidence import verify_suite

    def errors(records):
        return verify_suite(
            {"scenes": records}, "abc", "0.2.0", "metal", {}, lambda a, b: None
        )[0]

    complete = [
        {"scene": identifier, "sky_density": density}
        for identifier in SCENE_IDS
        for density in (1, 2)
    ]
    message = f"metal suite: {len(SCENE_IDS)} scenes in both sky bases are required"
    assert message not in errors(complete)
    assert message in errors(complete[:-1])
    assert message in errors(complete[:-1] + [complete[0]])


PLAN_IDS = tuple(
    f"plan_{family}_{profile}"
    for family in PLAN_FOOTPRINTS
    for profile in WINDOW_PROFILES
)


def test_plan_matrix_is_complete():
    assert len(PLAN_IDS) == 40
    assert set(PLAN_IDS).issubset(SCENE_IDS)
    assert all(
        scene_metadata(identifier)["category"] == "form" for identifier in PLAN_IDS
    )


@pytest.mark.parametrize("identifier", PLAN_IDS)
def test_plan_solids_windows_and_triangulation(identifier):
    from ladybug_geometry.geometry3d import Point3D, Vector3D
    from foton.honeybee.adapter import _append_geometry

    model, prepared = scene(identifier)
    room = model.rooms[0]
    metadata = scene_metadata(identifier)
    expected = {"i": 90, "j": 63, "l": 54, "t": 63, "cross": 63}[
        metadata["footprint_family"]
    ]
    assert model.units == "Meters"
    assert room.geometry.is_solid
    assert room.floor_area == pytest.approx(expected)
    assert room.volume == pytest.approx(expected * 3)
    assert len(model.apertures) == (
        len(PLAN_FOOTPRINTS[metadata["footprint_family"]])
        if metadata["window_profile"] == "distributed"
        else 1
    )
    if metadata["window_profile"] in ("small_center", "triangle", "circle", "arch"):
        assert model.apertures[0].area == pytest.approx(1.44)
    if metadata["window_profile"] == "large_center":
        assert model.apertures[0].area == pytest.approx(4.8)
    for face in room.faces:
        assert face.check_sub_faces_valid(raise_exception=False) == ""
        assert face.check_sub_faces_overlapping(raise_exception=False) == ""
        # Exercise the actual adapter triangulation, independently for each face.
        vertices, triangles, materials = [], [], []
        _append_geometry(face.punched_geometry, vertices, triangles, materials, 0)
        xyz = np.asarray(vertices)[np.asarray(triangles)]
        areas = (
            np.linalg.norm(
                np.cross(xyz[:, 1] - xyz[:, 0], xyz[:, 2] - xyz[:, 0]), axis=1
            )
            / 2
        )
        assert areas.sum() == pytest.approx(
            face.area - sum(a.area for a in face.apertures), abs=1e-6
        )
        for centroid in xyz.mean(axis=1):
            point = Point3D(*centroid)
            assert face.geometry.is_point_on_face(point, 1e-7)
            assert not any(
                aperture.geometry.is_point_on_face(point, 1e-7)
                for aperture in face.apertures
            )
            if face.normal.z < -0.9:
                assert room.geometry.is_point_inside(
                    Point3D(point.x, point.y, 0.1), Vector3D(1, 0.271, 0.173)
                )
    # Full closed opaque+glass transport mesh must preserve the whole envelope.
    xyz = prepared.arrays["vertices"][prepared.arrays["triangles"]]
    area = (
        np.linalg.norm(
            np.cross(xyz[:, 1] - xyz[:, 0], xyz[:, 2] - xyz[:, 0]), axis=1
        ).sum()
        / 2
    )
    assert area == pytest.approx(sum(face.area for face in room.faces), abs=1e-4)


@pytest.mark.parametrize("family", PLAN_FOOTPRINTS)
@pytest.mark.parametrize("rows", (146, 578))
def test_larger_plan_window_cannot_reduce_direct_light(family, rows):
    small = coefficients(f"plan_{family}_small_center", rows=rows)
    large = coefficients(f"plan_{family}_large_center", rows=rows)
    assert np.all(large >= small - 1e-6)
    assert large.sum() > small.sum()


def test_frozen_models_reject_stale_hash_missing_coverage_and_metadata(tmp_path):
    from scripts.validate_release_suite import validate_models

    directory = tmp_path / "models"
    manifest = export_scenes(directory, ("plan_cross_distributed",))
    assert set(validate_models(directory, ("plan_cross_distributed",))) == {
        "plan_cross_distributed"
    }
    with pytest.raises(ValueError, match="cover"):
        validate_models(directory, SCENE_IDS)
    path = directory / "manifest.json"
    manifest["suite_version"] -= 1
    path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError, match="version"):
        validate_models(directory, ("plan_cross_distributed",))
    manifest["suite_version"] = SCENE_VERSION
    path.write_text(json.dumps(manifest))
    model_path = directory / manifest["scenes"][0]["file"]
    model_path.write_text(model_path.read_text() + " ")
    with pytest.raises(ValueError, match="hash mismatch"):
        validate_models(directory, ("plan_cross_distributed",))
