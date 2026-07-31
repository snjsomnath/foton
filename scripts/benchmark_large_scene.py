#!/usr/bin/env python3
"""Benchmark the canonical instanced 1,000-room daylight scene."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import subprocess
import time

import numpy as np

from compare_full_transport_shoebox import (
    add_glass,
    create_native_scene,
    polygon,
    radiance_glass_transmissivity,
)
from compare_honeybee_shoebox import shaded_shoebox
from foton import Engine
from foton.honeybee.adapter import prepare_honeybee_scene
from foton.honeybee.radiance import (
    _radiance_subprocess_environment,
    resolve_radiance_executables,
)


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backend", choices=("auto", "metal", "vulkan"), default="auto")
    parser.add_argument("--output", required=True)
    parser.add_argument("--rooms", type=int, default=1000)
    parser.add_argument("--sensors-per-room", type=int, default=25)
    parser.add_argument("--samples", type=int, default=64)
    parser.add_argument("--bounces", type=int, default=1)
    parser.add_argument("--glass-transmittance", type=float, default=0.6)
    parser.add_argument("--workers", type=int)
    parser.add_argument("--radiance-bin")
    return parser.parse_args()


def large_scene_arrays(room_count, sensors_per_room, glass_transmittance):
    if room_count <= 0 or sensors_per_room <= 0:
        raise ValueError("room and sensor counts must be positive")
    model = shaded_shoebox(embedded_grid=False)
    prepared = prepare_honeybee_scene(model, grid_size=0.5, sensor_height=0.75)
    arrays = add_glass(
        prepared.arrays,
        prepared.model.apertures[0],
        glass_transmittance,
    )

    room_columns = math.ceil(math.sqrt(room_count))
    transforms = np.tile(np.eye(4, dtype=np.float32), (room_count, 1, 1))
    room_ids = np.arange(room_count, dtype=np.uint32)
    for room_index in range(room_count):
        column = room_index % room_columns
        row = room_index // room_columns
        transforms[room_index, 0, 3] = column * 8.0
        transforms[room_index, 1, 3] = row * 11.0

    sensor_columns = math.ceil(math.sqrt(sensors_per_room))
    sensor_rows = math.ceil(sensors_per_room / sensor_columns)
    local_positions = []
    for sensor_index in range(sensors_per_room):
        column = sensor_index % sensor_columns
        row = sensor_index // sensor_columns
        local_positions.append(
            (
                (column + 1) * 6.0 / (sensor_columns + 1),
                (row + 1) * 9.0 / (sensor_rows + 1),
                0.75,
            )
        )
    local_positions = np.asarray(local_positions, dtype=np.float32)
    positions = np.tile(local_positions, (room_count, 1))
    positions = positions.reshape(room_count, sensors_per_room, 3)
    positions[:, :, 0] += transforms[:, None, 0, 3]
    positions[:, :, 1] += transforms[:, None, 1, 3]
    sensor_count = room_count * sensors_per_room

    arrays["instance_transforms"] = np.ascontiguousarray(transforms)
    arrays["instance_mesh_indices"] = np.zeros(room_count, dtype=np.uint32)
    arrays["instance_room_ids"] = room_ids
    arrays["instance_masks"] = np.full(
        room_count,
        arrays["instance_masks"][0],
        dtype=np.uint32,
    )
    arrays["sensor_positions"] = np.ascontiguousarray(
        positions.reshape(sensor_count, 3)
    )
    arrays["sensor_normals"] = np.tile(
        np.asarray([[0.0, 0.0, 1.0]], dtype=np.float32),
        (sensor_count, 1),
    )
    arrays["sensor_ids"] = np.arange(sensor_count, dtype=np.uint32)
    arrays["sensor_room_ids"] = np.repeat(room_ids, sensors_per_room)
    arrays["sensor_area_weights"] = np.full(
        sensor_count,
        54.0 / sensors_per_room,
        dtype=np.float32,
    )
    return arrays


def analyze(scene, samples, bounces):
    sky = np.ones((146, 1, 3), dtype=np.float32)
    occupancy = np.ones(1, dtype=np.float32)
    started = time.perf_counter()
    result = scene.analyze(
        sky,
        occupancy,
        quality="preview",
        maximum_samples=samples,
        maximum_bounces=bounces,
        scene_seed=0,
        export_coefficients=False,
    ).result()
    return result, (time.perf_counter() - started) * 1000.0


def write_large_radiance_scene(path, arrays, glass_transmittance):
    transmissivity = radiance_glass_transmissivity(glass_transmittance)
    chunks = [
        "void plastic diffuse_mat\n0\n0\n5 0.5 0.5 0.5 0 0\n",
        "void glass glass_mat\n0\n0\n"
        f"3 {transmissivity:.9g} {transmissivity:.9g} {transmissivity:.9g}\n",
    ]
    vertices = arrays["vertices"].astype(np.float64)
    for instance_index, transform in enumerate(arrays["instance_transforms"]):
        world_vertices = (
            vertices @ transform[:3, :3].astype(np.float64).T
            + transform[:3, 3].astype(np.float64)
        )
        for triangle_index, triangle in enumerate(arrays["triangles"]):
            material_index = int(arrays["triangle_materials"][triangle_index])
            modifier = "glass_mat" if material_index == 1 else "diffuse_mat"
            chunks.append(
                polygon(
                    modifier,
                    f"room_{instance_index}_triangle_{triangle_index}",
                    world_vertices[np.asarray(triangle, dtype=np.int64)],
                )
            )
    chunks.append(
        """
void glow environment_glow
0
0
4 1 1 1 0

environment_glow source sky
0
0
4 0 0 1 180

environment_glow source ground
0
0
4 0 0 -1 180
""".strip()
    )
    path.write_text("\n\n".join(chunks) + "\n", encoding="utf-8")


def _run_checked(command, *, environment, stdin=None, stdout=None):
    started = time.perf_counter()
    completed = subprocess.run(
        command,
        stdin=stdin,
        stdout=stdout,
        stderr=subprocess.PIPE,
        env=environment,
        check=False,
    )
    elapsed_ms = (time.perf_counter() - started) * 1000.0
    if completed.returncode:
        raise RuntimeError(completed.stderr.decode(errors="replace").strip())
    return elapsed_ms


def benchmark_radiance(
    arrays,
    output_directory,
    samples,
    bounces,
    workers,
    radiance_bin,
    glass_transmittance,
):
    output_directory.mkdir(parents=True, exist_ok=True)
    executables = resolve_radiance_executables(radiance_bin)
    environment = _radiance_subprocess_environment(executables)
    scene_path = output_directory / "scene.rad"
    octree_path = output_directory / "scene.oct"
    sensors_path = output_directory / "sensors.pts"

    scene_started = time.perf_counter()
    write_large_radiance_scene(scene_path, arrays, glass_transmittance)
    scene_write_ms = (time.perf_counter() - scene_started) * 1000.0
    sensor_rows = np.concatenate(
        (arrays["sensor_positions"], arrays["sensor_normals"]), axis=1
    )
    np.savetxt(sensors_path, sensor_rows, fmt="%.9g")

    oconv_command = [executables["oconv"], str(scene_path)]
    with octree_path.open("wb") as octree:
        octree_ms = _run_checked(
            oconv_command,
            environment=environment,
            stdout=octree,
        )
    rcontrib_command = [
        executables["rcontrib"],
        "-I+",
        "-h",
        "-w",
        "-V-",
        "-ab",
        str(bounces + 1),
        "-ad",
        str(samples),
        "-as",
        "0",
        "-aa",
        "0",
        "-lr",
        "-10",
        "-lw",
        f"{1.0 / max(samples * 10, 1):.9g}",
        "-e",
        "MF:1",
        "-f",
        "reinhart.cal",
        "-b",
        "rbin",
        "-bn",
        "Nrbins",
        "-m",
        "environment_glow",
    ]
    if workers:
        rcontrib_command.extend(["-n", str(workers)])
    rcontrib_command.append(str(octree_path))

    trace_times = []
    for _ in range(2):
        with sensors_path.open("rb") as sensors:
            trace_times.append(
                _run_checked(
                    rcontrib_command,
                    environment=environment,
                    stdin=sensors,
                    stdout=subprocess.DEVNULL,
                )
            )
    return {
        "scene_write_ms": scene_write_ms,
        "octree_build_ms": octree_ms,
        "first_trace_ms": trace_times[0],
        "cached_trace_ms": trace_times[1],
        "cold_wall_clock_ms": octree_ms + trace_times[0],
        "cached_wall_clock_ms": trace_times[1],
        "commands": [oconv_command, rcontrib_command],
    }


def main():
    args = parse_args()
    if args.samples <= 0 or args.bounces <= 0:
        raise ValueError("samples and bounces must be positive")
    output = Path(args.output).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    arrays = large_scene_arrays(
        args.rooms,
        args.sensors_per_room,
        args.glass_transmittance,
    )
    engine = Engine({"backend": args.backend})
    commit_started = time.perf_counter()
    scene = create_native_scene(engine, arrays)
    commit_ms = (time.perf_counter() - commit_started) * 1000.0
    first, first_wall_ms = analyze(scene, args.samples, args.bounces)
    cached, cached_wall_ms = analyze(scene, args.samples, args.bounces)
    if first.used_reference_fallback or first.transport_backend == "reference":
        raise RuntimeError("large-scene benchmark did not execute on GPU hardware")
    if args.backend != "auto" and first.transport_backend != args.backend:
        raise RuntimeError(
            f"requested backend {args.backend!r} but engine used "
            f"{first.transport_backend!r}"
        )

    radiance = benchmark_radiance(
        arrays,
        output.parent / "large_radiance",
        args.samples,
        args.bounces,
        args.workers,
        args.radiance_bin,
        args.glass_transmittance,
    )
    payload = {
        "fixture": "canonical-instanced-shoebox-1000-v1",
        "rooms": args.rooms,
        "sensors_per_room": args.sensors_per_room,
        "sensor_count": args.rooms * args.sensors_per_room,
        "mesh_count": int(arrays["mesh_ranges"].shape[0]),
        "instance_count": int(arrays["instance_transforms"].shape[0]),
        "triangles_per_room": int(arrays["triangles"].shape[0]),
        "samples": args.samples,
        "bounces": args.bounces,
        "glass_transmittance": args.glass_transmittance,
        "estimated_input_bytes": int(sum(value.nbytes for value in arrays.values())),
        "scene_commit_ms": commit_ms,
        "transport_backend": first.transport_backend,
        "capabilities": engine.capabilities(),
        "first_run": {
            "wall_clock_ms": first_wall_ms,
            "timings_ms": first.timings(),
            "room_metric_count": len(first.room_ids()),
            "sensor_metric_count": len(first.sensor_ids()),
        },
        "resident_scene_reuse": {
            "wall_clock_ms": cached_wall_ms,
            "timings_ms": cached.timings(),
            "room_metric_count": len(cached.room_ids()),
            "sensor_metric_count": len(cached.sensor_ids()),
        },
        "radiance": radiance,
    }
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
