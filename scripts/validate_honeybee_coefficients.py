#!/usr/bin/env python3
"""Validate staged Foton coefficients against a Honeybee annual-daylight project."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import time

import numpy as np

from foton import Engine, sky_patch_directions, sky_patch_solid_angles
from foton.honeybee.adapter import (
    _resolved_modifier,
    prepare_honeybee_scene,
)
from foton.honeybee.radiance import (
    run_radiance_coefficient_stages,
    run_radiance_visibility,
)
from foton.honeybee.validation import (
    compare_coefficient_repeatability,
    compare_coefficient_stages,
)


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True)
    parser.add_argument(
        "--honeybee-project",
        required=True,
        help="Completed Honeybee annual-daylight project containing model/ and resources/.",
    )
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--backend",
        choices=("auto", "metal", "vulkan", "reference", "cpu"),
        default="auto",
    )
    parser.add_argument("--sky-density", choices=(1, 2), type=int, default=1)
    parser.add_argument("--direct-samples", type=int, default=64)
    parser.add_argument("--indirect-samples", type=int, default=4096)
    parser.add_argument("--workers", type=int)
    parser.add_argument("--radiance-bin")
    parser.add_argument(
        "--radiance-replicates",
        type=int,
        default=2,
        help="Independent rfluxmtx runs used to measure oracle repeatability.",
    )
    parser.add_argument("--fail-on-threshold", action="store_true")
    return parser.parse_args()


def trace_coefficients(
    prepared,
    *,
    backend,
    rows,
    direct_samples,
    indirect_samples,
):
    engine = Engine({"backend": backend})
    scene = prepared.create_native_scene(engine)
    sky = np.zeros((rows, 1, 3), dtype=np.float32)
    occupancy = np.ones(1, dtype=np.float32)

    started = time.perf_counter()
    direct_result = scene.analyze(
        sky,
        occupancy,
        quality="final",
        direct_samples=direct_samples,
        maximum_samples=0,
        maximum_bounces=0,
        scene_seed=0,
        export_coefficients=True,
    ).result()
    direct_seconds = time.perf_counter() - started
    started = time.perf_counter()
    full_result = scene.analyze(
        sky,
        occupancy,
        quality="final",
        direct_samples=direct_samples,
        maximum_samples=indirect_samples,
        maximum_bounces=1,
        scene_seed=0,
        export_coefficients=True,
    ).result()
    full_seconds = time.perf_counter() - started
    return {
        "direct": np.ascontiguousarray(
            direct_result.coefficients(), dtype=np.float32
        ),
        "full": np.ascontiguousarray(
            full_result.coefficients(), dtype=np.float32
        ),
        "timings_seconds": {
            "direct": direct_seconds,
            "full": full_seconds,
        },
        "metadata": {
            "capabilities": dict(engine.capabilities()),
            "direct": json.loads(direct_result.metadata_json()),
            "full": json.loads(full_result.metadata_json()),
        },
    }


def audit_sensor_files(prepared, project):
    grid_folder = project / "model" / "grid"
    grids = []
    passed = True
    for info in prepared.grid_info:
        path = grid_folder / f"{info['full_identifier']}.pts"
        if not path.is_file():
            path = grid_folder / f"{info['identifier']}.pts"
        if not path.is_file():
            grids.append(
                {
                    "identifier": info["identifier"],
                    "passed": False,
                    "reason": f"missing {path}",
                }
            )
            passed = False
            continue
        reference = np.atleast_2d(np.loadtxt(path, dtype=np.float64))
        start = int(info["start_sensor_index"])
        end = start + int(info["sensor_count"])
        positions = prepared.arrays["sensor_positions"][start:end].astype(
            np.float64
        )
        normals = prepared.arrays["sensor_normals"][start:end].astype(
            np.float64
        )
        expected_shape = (end - start, 6)
        shape_match = reference.shape == expected_shape
        position_error = (
            float(np.max(np.abs(reference[:, :3] - positions), initial=0))
            if shape_match
            else float("inf")
        )
        normal_error = (
            float(np.max(np.abs(reference[:, 3:] - normals), initial=0))
            if shape_match
            else float("inf")
        )
        grid_passed = (
            shape_match and position_error <= 1.0e-6 and normal_error <= 1.0e-6
        )
        passed &= grid_passed
        grids.append(
            {
                "identifier": info["identifier"],
                "file": str(path),
                "shape": list(reference.shape),
                "maximum_position_error_m": position_error,
                "maximum_normal_error": normal_error,
                "passed": bool(grid_passed),
            }
        )
    return {"passed": bool(passed), "grids": grids}


def _radiance_polygons(path):
    tokens = []
    for line in path.read_text(encoding="utf-8").splitlines():
        content = line.split("#", 1)[0].strip()
        if content:
            tokens.extend(content.split())
    polygons = []
    index = 0
    while index < len(tokens):
        modifier, primitive, identifier = tokens[index : index + 3]
        index += 3
        string_count = int(tokens[index])
        index += 1 + string_count
        integer_count = int(tokens[index])
        index += 1 + integer_count
        real_count = int(tokens[index])
        index += 1
        values = np.asarray(
            [float(value) for value in tokens[index : index + real_count]],
            dtype=np.float64,
        )
        index += real_count
        if primitive == "polygon":
            if real_count < 9 or real_count % 3:
                raise ValueError(f"invalid polygon {identifier!r} in {path}")
            polygons.append(
                {
                    "modifier": modifier,
                    "identifier": identifier,
                    "vertices": values.reshape(-1, 3),
                }
            )
    return polygons


def _polygon_area(vertices):
    normal = np.zeros(3, dtype=np.float64)
    for current, following in zip(
        vertices, np.roll(vertices, -1, axis=0), strict=True
    ):
        normal += np.cross(current, following)
    return 0.5 * float(np.linalg.norm(normal))


def _polygon_normal(vertices):
    normal = np.zeros(3, dtype=np.float64)
    for current, following in zip(
        vertices, np.roll(vertices, -1, axis=0), strict=True
    ):
        normal += np.cross(current, following)
    length = float(np.linalg.norm(normal))
    return normal / length if length else normal


def _cyclic_boundary_error(reference, candidate):
    if reference.shape != candidate.shape:
        return float("inf")
    return min(
        float(
            np.max(
                np.abs(reference - np.roll(candidate, shift, axis=0)),
                initial=0,
            )
        )
        for shift in range(reference.shape[0])
    )


def audit_geometry(prepared, project):
    paths = (
        project / "model" / "scene" / "envelope.rad",
        project / "model" / "aperture" / "aperture.rad",
    )
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        return {"passed": False, "missing_files": missing}
    polygons = [
        polygon
        for path in paths
        for polygon in _radiance_polygons(path)
    ]
    expected_objects = {
        obj.identifier: obj
        for obj in (*prepared.model.faces, *prepared.model.apertures)
    }
    surface_results = []
    surface_passed = True
    for polygon in polygons:
        obj = expected_objects.get(polygon["identifier"])
        if obj is None:
            surface_results.append(
                {
                    "identifier": polygon["identifier"],
                    "passed": False,
                    "reason": "identifier is absent from the Honeybee model",
                }
            )
            surface_passed = False
            continue
        geometry = (
            obj.punched_geometry
            if obj.__class__.__name__ == "Face"
            else obj.geometry
        )
        expected_vertices = np.asarray(
            [[point.x, point.y, point.z] for point in geometry.vertices],
            dtype=np.float64,
        )
        boundary_error = _cyclic_boundary_error(
            polygon["vertices"], expected_vertices
        )
        normal_error = float(
            np.max(
                np.abs(
                    _polygon_normal(polygon["vertices"])
                    - _polygon_normal(expected_vertices)
                ),
                initial=0,
            )
        )
        area_error = abs(
            _polygon_area(polygon["vertices"])
            - _polygon_area(expected_vertices)
        )
        expected_material = _resolved_modifier(obj).identifier
        item_passed = (
            polygon["modifier"] == expected_material
            and boundary_error <= 1.0e-6
            and normal_error <= 1.0e-6
            and area_error <= 1.0e-6
        )
        surface_passed &= item_passed
        surface_results.append(
            {
                "identifier": polygon["identifier"],
                "radiance_material": polygon["modifier"],
                "honeybee_material": expected_material,
                "maximum_boundary_error_m": boundary_error,
                "maximum_orientation_error": normal_error,
                "absolute_area_error_m2": area_error,
                "passed": bool(item_passed),
            }
        )
    reference_areas = {}
    for polygon in polygons:
        reference_areas.setdefault(polygon["modifier"], 0.0)
        reference_areas[polygon["modifier"]] += _polygon_area(
            polygon["vertices"]
        )

    vertices = prepared.arrays["vertices"].astype(np.float64)
    candidate_areas = {}
    materials = {
        int(item["index"]): item["identifier"]
        for item in prepared.geometry_info["materials"]
    }
    for triangle, material_index in zip(
        prepared.arrays["triangles"],
        prepared.arrays["triangle_materials"],
        strict=True,
    ):
        first, second, third = vertices[triangle]
        area = 0.5 * float(
            np.linalg.norm(np.cross(second - first, third - first))
        )
        identifier = materials[int(material_index)]
        candidate_areas.setdefault(identifier, 0.0)
        candidate_areas[identifier] += area
    material_ids = sorted(set(reference_areas) | set(candidate_areas))
    material_results = []
    passed = surface_passed
    for identifier in material_ids:
        reference = reference_areas.get(identifier, 0.0)
        candidate = candidate_areas.get(identifier, 0.0)
        error = abs(candidate - reference)
        tolerance = max(1.0e-6, reference * 1.0e-6)
        material_passed = error <= tolerance
        passed &= material_passed
        material_results.append(
            {
                "identifier": identifier,
                "radiance_area_m2": reference,
                "foton_area_m2": candidate,
                "absolute_error_m2": error,
                "passed": bool(material_passed),
            }
        )
    expected_identifiers = {
        obj.identifier
        for obj in (
            *prepared.model.faces,
            *prepared.model.apertures,
        )
    }
    actual_identifiers = {item["identifier"] for item in polygons}
    missing_identifiers = sorted(expected_identifiers - actual_identifiers)
    passed &= not missing_identifiers
    return {
        "passed": bool(passed),
        "radiance_polygon_count": len(polygons),
        "foton_triangle_count": int(
            prepared.arrays["triangles"].shape[0]
        ),
        "missing_honeybee_identifiers": missing_identifiers,
        "surfaces": surface_results,
        "materials": material_results,
    }


def center_visibility(prepared, *, backend, sky_density, output, workers, radiance_bin):
    basis = "tregenza" if sky_density == 1 else "reinhart-mf2"
    directions = np.asarray(sky_patch_directions(basis), dtype=np.float64)
    angles = np.asarray(sky_patch_solid_angles(basis), dtype=np.float64)
    normals = prepared.arrays["sensor_normals"].astype(np.float64)
    weights = (
        np.maximum(np.einsum("si,pi->sp", normals, directions), 0.0)
        * angles[None, :]
    )
    engine = Engine({"backend": backend})
    scene = prepared.create_native_scene(engine)
    result = scene.analyze(
        np.zeros((directions.shape[0], 1, 3), dtype=np.float32),
        np.ones(1, dtype=np.float32),
        quality="final",
        direct_samples=1,
        maximum_samples=0,
        maximum_bounces=0,
        export_coefficients=True,
    ).result()
    coefficients = np.asarray(result.coefficients(), dtype=np.float32)
    candidate = np.zeros(weights.shape, dtype=np.float32)
    valid = weights > 1.0e-8
    candidate[valid] = np.mean(coefficients, axis=2)[valid] / weights[valid]
    candidate = (candidate >= 0.5).astype(np.float32)
    reference_run = run_radiance_visibility(
        prepared.model,
        prepared.arrays["sensor_positions"],
        normals,
        directions.astype(np.float32),
        weights.astype(np.float32),
        work_directory=output / "center_visibility",
        workers=workers,
        radiance_bin=radiance_bin,
    )
    difference = np.abs(candidate - reference_run.visibility)
    np.save(output / "foton_center_visibility.npy", candidate)
    np.save(
        output / "radiance_center_visibility.npy",
        reference_run.visibility,
    )
    return {
        "passed": bool(not np.any(difference > 0.01)),
        "shape": list(candidate.shape),
        "mismatch_count": int(np.count_nonzero(difference > 0.01)),
        "maximum_absolute_error": float(np.max(difference, initial=0)),
        "radiance_commands": reference_run.commands,
        "radiance_versions": reference_run.versions,
        "radiance_elapsed_ms": reference_run.elapsed_ms,
    }


def main():
    args = parse_args()
    if args.direct_samples <= 0:
        raise ValueError("--direct-samples must be positive")
    if args.indirect_samples <= 0:
        raise ValueError("--indirect-samples must be positive")
    if args.radiance_replicates < 2:
        raise ValueError("--radiance-replicates must be at least 2")
    output = Path(args.output).expanduser().resolve()
    output.mkdir(parents=True, exist_ok=True)
    project = Path(args.honeybee_project).expanduser().resolve()
    octree = project / "resources" / "scene.oct"
    sky_dome = project / "resources" / "sky.dome"
    rows = 146 if args.sky_density == 1 else 578

    prepared = prepare_honeybee_scene(
        args.model, include_aperture_glazing=True
    )
    open_prepared = prepare_honeybee_scene(
        args.model, include_aperture_glazing=False
    )
    sensor_audit = audit_sensor_files(prepared, project)
    geometry_audit = audit_geometry(prepared, project)
    visibility = center_visibility(
        open_prepared,
        backend=args.backend,
        sky_density=args.sky_density,
        output=output,
        workers=args.workers,
        radiance_bin=args.radiance_bin,
    )
    foton = trace_coefficients(
        prepared,
        backend=args.backend,
        rows=rows,
        direct_samples=args.direct_samples,
        indirect_samples=args.indirect_samples,
    )
    np.save(output / "foton_direct.npy", foton["direct"])
    np.save(output / "foton_full.npy", foton["full"])
    np.save(
        output / "foton_indirect.npy",
        foton["full"].astype(np.float64) - foton["direct"].astype(np.float64),
    )
    radiance_runs = [
        run_radiance_coefficient_stages(
            prepared.arrays["sensor_positions"],
            prepared.arrays["sensor_normals"],
            octree=octree,
            sky_dome=sky_dome,
            sky_density=args.sky_density,
            work_directory=output / f"radiance_run_{index:02d}",
            workers=args.workers,
            radiance_bin=args.radiance_bin,
        )
        for index in range(args.radiance_replicates)
    ]
    radiance_direct = np.mean(
        np.stack([run.direct for run in radiance_runs]), axis=0
    ).astype(np.float32)
    radiance_full = np.mean(
        np.stack([run.full for run in radiance_runs]), axis=0
    ).astype(np.float32)
    np.save(output / "radiance_direct_mean.npy", radiance_direct)
    np.save(output / "radiance_full_mean.npy", radiance_full)
    repeatability = compare_coefficient_repeatability(
        prepared,
        radiance_direct_runs=[run.direct for run in radiance_runs],
        radiance_full_runs=[run.full for run in radiance_runs],
        output_folder=output,
    )
    comparison = compare_coefficient_stages(
        prepared,
        foton_direct=foton["direct"],
        foton_full=foton["full"],
        radiance_direct=radiance_direct,
        radiance_full=radiance_full,
        output_folder=output,
    )
    payload = {
        "schema_version": 1,
        "passed": bool(
            sensor_audit["passed"]
            and geometry_audit["passed"]
            and visibility["passed"]
            and repeatability["oracle_stable_at_release_gates"]
            and comparison["passed"]
        ),
        "model": str(Path(args.model).expanduser().resolve()),
        "honeybee_project": str(project),
        "sky_density": args.sky_density,
        "sensor_audit": sensor_audit,
        "geometry_audit": geometry_audit,
        "center_visibility": visibility,
        "coefficient_comparison": comparison,
        "radiance_repeatability": repeatability,
        "foton": foton["metadata"],
        "foton_timings_seconds": foton["timings_seconds"],
        "radiance": [
            {
                "commands": run.commands,
                "versions": run.versions,
                "timings_ms": run.timings_ms,
                "files": run.files,
            }
            for run in radiance_runs
        ],
    }
    (output / "parity_manifest.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(output / "coefficient_comparison.md")
    print(output / "parity_manifest.json")
    if args.fail_on_threshold and not payload["passed"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
