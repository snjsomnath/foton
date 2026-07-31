#!/usr/bin/env python3
"""Compare hardware-accelerated multi-bounce shoebox coefficients with Radiance."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import time

import numpy as np

from compare_honeybee_shoebox import shaded_shoebox
from foton import Engine, sky_patch_directions
from foton.honeybee.adapter import prepare_honeybee_scene
from foton.honeybee.radiance import (
    _executable_version,
    _radiance_subprocess_environment,
    resolve_radiance_executables,
)


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--backend",
        choices=("auto", "metal", "vulkan"),
        default="auto",
        help="Hardware engine backend. Radiance always supplies the reference.",
    )
    parser.add_argument("--output", default="simulation/full-transport")
    parser.add_argument("--samples", type=int, default=4096)
    parser.add_argument("--bounces", type=int, default=2)
    parser.add_argument("--workers", type=int)
    parser.add_argument("--radiance-bin")
    parser.add_argument("--glass-transmittance", type=float)
    parser.add_argument(
        "--annual",
        action="store_true",
        help="Compare 8,760-hour illuminance, DA, and sDA from both coefficient matrices.",
    )
    return parser.parse_args()


def radiance_glass_transmissivity(transmittance):
    if transmittance == 0:
        return 0.0
    return (
        np.sqrt(0.8402528435 + 0.0072522239 * transmittance * transmittance)
        - 0.9166530661
    ) / (0.0036261119 * transmittance)


def add_glass(arrays, aperture, transmittance):
    if not 0 <= transmittance <= 1:
        raise ValueError("glass transmittance must be within [0, 1]")
    output = {name: value.copy() for name, value in arrays.items()}
    if output["mesh_ranges"].shape != (1, 2):
        raise ValueError("the full-transport fixture requires one room mesh")
    if output["mesh_ranges"][0, 0] != 0:
        raise ValueError("the room mesh must begin at triangle zero")

    mesh = aperture.geometry.triangulated_mesh3d
    vertex_offset = output["vertices"].shape[0]
    vertices = np.asarray(
        [[vertex.x, vertex.y, vertex.z] for vertex in mesh.vertices],
        dtype=np.float32,
    )
    triangles = []
    for face in mesh.faces:
        indices = [vertex_offset + int(index) for index in face]
        for index in range(1, len(indices) - 1):
            triangles.append([indices[0], indices[index], indices[index + 1]])
    triangles = np.asarray(triangles, dtype=np.uint32)
    output["vertices"] = np.ascontiguousarray(
        np.concatenate((output["vertices"], vertices), axis=0)
    )
    output["triangles"] = np.ascontiguousarray(
        np.concatenate((output["triangles"], triangles), axis=0)
    )
    output["triangle_materials"] = np.ascontiguousarray(
        np.concatenate(
            (
                output["triangle_materials"],
                np.ones(triangles.shape[0], dtype=np.uint32),
            )
        )
    )
    output["mesh_ranges"][0, 1] += triangles.shape[0]
    output["material_kinds"] = np.ascontiguousarray([0, 1], dtype=np.uint32)
    output["material_diffuse_rgb"] = np.ascontiguousarray(
        [[0.5, 0.5, 0.5], [0.0, 0.0, 0.0]], dtype=np.float32
    )
    output["material_transmittance_rgb"] = np.ascontiguousarray(
        [[0.0, 0.0, 0.0], [transmittance] * 3], dtype=np.float32
    )
    return output


def create_native_scene(engine, arrays):
    return engine.create_scene(
        arrays["vertices"],
        arrays["triangles"],
        arrays["triangle_materials"],
        arrays["mesh_ranges"],
        arrays["instance_transforms"],
        arrays["instance_mesh_indices"],
        arrays["instance_room_ids"],
        arrays["instance_masks"],
        arrays["material_kinds"],
        arrays["material_diffuse_rgb"],
        arrays["material_transmittance_rgb"],
        arrays["sensor_positions"],
        arrays["sensor_normals"],
        arrays["sensor_ids"],
        arrays["sensor_room_ids"],
        arrays["sensor_area_weights"],
    )


def polygon(modifier, identifier, vertices):
    values = "\n".join(
        f"    {vertex[0]:.9g} {vertex[1]:.9g} {vertex[2]:.9g}"
        for vertex in vertices
    )
    return (
        f"{modifier} polygon {identifier}\n"
        "0\n"
        "0\n"
        f"{len(vertices) * 3}\n"
        f"{values}\n"
    )


def write_radiance_scene(path, arrays, glass_transmittance):
    chunks = ["void plastic diffuse_mat\n0\n0\n5 0.5 0.5 0.5 0 0\n"]
    if glass_transmittance is not None:
        transmissivity = radiance_glass_transmissivity(glass_transmittance)
        chunks.append(
            "void glass glass_mat\n"
            "0\n"
            "0\n"
            f"3 {transmissivity:.9g} {transmissivity:.9g} {transmissivity:.9g}\n"
        )
    vertices = arrays["vertices"]
    for triangle_index, triangle in enumerate(arrays["triangles"]):
        material_index = int(arrays["triangle_materials"][triangle_index])
        modifier = "glass_mat" if material_index == 1 else "diffuse_mat"
        chunks.append(
            polygon(
                modifier,
                f"triangle_{triangle_index}",
                vertices[np.asarray(triangle, dtype=np.int64)],
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


def run_radiance(
    arrays,
    output,
    samples,
    diffuse_bounces,
    workers,
    radiance_bin,
    glass_transmittance,
):
    executables = resolve_radiance_executables(radiance_bin)
    environment = _radiance_subprocess_environment(executables)
    scene_path = output / "scene.rad"
    octree_path = output / "scene.oct"
    write_radiance_scene(scene_path, arrays, glass_transmittance)

    oconv_command = [executables["oconv"], str(scene_path)]
    with octree_path.open("wb") as octree:
        completed = subprocess.run(
            oconv_command,
            stdout=octree,
            stderr=subprocess.PIPE,
            env=environment,
            check=False,
        )
    if completed.returncode:
        raise RuntimeError(completed.stderr.decode(errors="replace").strip())

    command = [
        executables["rcontrib"],
        "-I+",
        "-h",
        "-w",
        "-V-",
        "-ab",
        str(diffuse_bounces + 1),
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
        command.extend(["-n", str(workers)])
    command.append(str(octree_path))
    sensor_rows = np.concatenate(
        (arrays["sensor_positions"], arrays["sensor_normals"]), axis=1
    )
    sensor_text = "\n".join(
        " ".join(f"{value:.9g}" for value in row) for row in sensor_rows
    )
    started = time.perf_counter()
    completed = subprocess.run(
        command,
        input=sensor_text + "\n",
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=environment,
        check=False,
    )
    elapsed_ms = (time.perf_counter() - started) * 1000.0
    if completed.returncode:
        raise RuntimeError(completed.stderr.strip())
    values = np.fromstring(completed.stdout, sep=" ", dtype=np.float64)
    expected = arrays["sensor_positions"].shape[0] * 146 * 3
    if values.size != expected:
        raise RuntimeError(
            f"rcontrib returned {values.size} values; expected {expected}"
        )
    return (
        np.ascontiguousarray(
            values.reshape(arrays["sensor_positions"].shape[0], 146, 3),
            dtype=np.float32,
        ),
        [oconv_command, command],
        elapsed_ms,
        {
            name: _executable_version(path)
            for name, path in executables.items()
        },
    )


def comparison(reference, candidate):
    difference = candidate.astype(np.float64) - reference.astype(np.float64)
    reference_mean = float(np.mean(reference))
    return {
        "shape": list(reference.shape),
        "nmbe_percent": (
            100.0 * float(np.sum(difference)) / float(np.sum(reference))
            if np.sum(reference) != 0
            else None
        ),
        "cvrmse_percent": (
            100.0 * float(np.sqrt(np.mean(difference**2))) / abs(reference_mean)
            if reference_mean != 0
            else None
        ),
        "mean_absolute_error": float(np.mean(np.abs(difference))),
        "maximum_absolute_error": float(np.max(np.abs(difference))),
        "reference_energy": float(np.sum(reference)),
        "candidate_energy": float(np.sum(candidate)),
    }


def deterministic_annual_sky():
    timestep_count = 8760
    timestep = np.arange(timestep_count, dtype=np.float32)
    hour = np.mod(timestep, 24.0)
    day = np.floor(timestep / 24.0)
    daylight = np.maximum(np.sin(np.pi * (hour - 6.0) / 12.0), 0.0)
    season = 0.72 + 0.28 * np.cos(2.0 * np.pi * (day - 172.0) / 365.0)
    deterministic_cloud = 0.78 + 0.22 * np.sin(0.37 * day + 0.11 * hour) ** 2
    temporal = daylight * season * deterministic_cloud

    directions = np.asarray(sky_patch_directions("tregenza"), dtype=np.float32)
    altitude_weight = 0.25 + 0.75 * np.maximum(directions[:, 2], 0.0)
    scalar = 14.0 * altitude_weight[:, None] * temporal[None, :]
    sky = np.stack((scalar * 0.92, scalar, scalar * 1.08), axis=2)
    occupancy = np.asarray((hour >= 8.0) & (hour < 18.0), dtype=np.float32)
    return np.ascontiguousarray(sky, dtype=np.float32), occupancy


def annual_illuminance(coefficients, sky):
    return np.ascontiguousarray(
        np.einsum(
            "spc,ptc,c->st",
            coefficients.astype(np.float64),
            sky.astype(np.float64),
            np.asarray([47.435, 119.93, 11.635], dtype=np.float64),
            optimize=True,
        ),
        dtype=np.float32,
    )


def annual_metrics(illuminance, occupancy, sensor_area_weights):
    occupied = occupancy > 0
    if not np.any(occupied):
        raise ValueError("annual occupancy schedule has no occupied hours")
    daylight_autonomy = np.mean(illuminance[:, occupied] >= 300.0, axis=1)
    passing = daylight_autonomy >= 0.5
    weights = np.asarray(sensor_area_weights, dtype=np.float64)
    static_sda = 100.0 * float(np.sum(weights[passing])) / float(np.sum(weights))
    return {
        "occupied_hours": int(np.count_nonzero(occupied)),
        "mean_daylight_autonomy": float(np.mean(daylight_autonomy)),
        "minimum_daylight_autonomy": float(np.min(daylight_autonomy)),
        "maximum_daylight_autonomy": float(np.max(daylight_autonomy)),
        "static_sda_300_50_percent": static_sda,
        "per_sensor_daylight_autonomy": daylight_autonomy.astype(float).tolist(),
    }


def annual_comparison(
    engine_coefficients,
    radiance_coefficients,
    sky,
    occupancy,
    sensor_area_weights,
    engine_result,
):
    engine_started = time.perf_counter()
    engine_lux = annual_illuminance(engine_coefficients, sky)
    engine_postprocess_ms = (time.perf_counter() - engine_started) * 1000.0
    radiance_started = time.perf_counter()
    radiance_lux = annual_illuminance(radiance_coefficients, sky)
    radiance_postprocess_ms = (time.perf_counter() - radiance_started) * 1000.0
    occupied = occupancy > 0
    engine_metrics = annual_metrics(engine_lux, occupancy, sensor_area_weights)
    radiance_metrics = annual_metrics(radiance_lux, occupancy, sensor_area_weights)
    backend_da = np.asarray(engine_result.daylight_autonomy(), dtype=np.float64)
    cpu_da = np.asarray(
        engine_metrics["per_sensor_daylight_autonomy"], dtype=np.float64
    )
    backend_sda = np.asarray(engine_result.static_sda_300_50(), dtype=np.float64)
    return {
        "sky": "deterministic-annual-stress-sky-v1",
        "timestep_count": int(sky.shape[1]),
        "occupied_hours": int(np.count_nonzero(occupied)),
        "engine_postprocess_ms": engine_postprocess_ms,
        "radiance_postprocess_ms": radiance_postprocess_ms,
        "illuminance_comparison": comparison(
            radiance_lux[:, occupied], engine_lux[:, occupied]
        ),
        "engine_metrics": engine_metrics,
        "radiance_metrics": radiance_metrics,
        "metric_differences": {
            "mean_daylight_autonomy": engine_metrics["mean_daylight_autonomy"]
            - radiance_metrics["mean_daylight_autonomy"],
            "static_sda_300_50_percentage_points": engine_metrics[
                "static_sda_300_50_percent"
            ]
            - radiance_metrics["static_sda_300_50_percent"],
        },
        "engine_reduction_contract": {
            "maximum_daylight_autonomy_error": float(
                np.max(np.abs(backend_da - cpu_da), initial=0.0)
            ),
            "static_sda_300_50_error_percentage_points": float(
                np.max(
                    np.abs(
                        backend_sda
                        - engine_metrics["static_sda_300_50_percent"]
                    ),
                    initial=0.0,
                )
            ),
        },
    }


def report_markdown(payload):
    metrics = payload["comparison"]
    uniform_metrics = payload["uniform_sky_sensor_comparison"]
    lines = [
            "# Full Hardware Transport Comparison",
            "",
            f"- Basis: `tregenza`",
            f"- Matrix shape: `{metrics['shape']}`",
            f"- Samples: `{payload['samples']}`",
            f"- Diffuse bounces: `{payload['bounces']}`",
            f"- Radiance ambient bounces: `{payload['radiance']['ambient_bounces']}`",
            f"- Glass visible transmittance: `{payload['glass_transmittance']}`",
            f"- Requested backend: `{payload['engine']['requested_backend']}`",
            f"- Transport backend: `{payload['engine']['transport_backend']}`",
            f"- Reference fallback: `{payload['engine']['used_reference_fallback']}`",
            f"- NMBE: `{metrics['nmbe_percent']:.4f}%`",
            f"- CV(RMSE): `{metrics['cvrmse_percent']:.4f}%`",
            f"- Mean absolute error: `{metrics['mean_absolute_error']:.8g}`",
            f"- Maximum absolute error: `{metrics['maximum_absolute_error']:.8g}`",
            f"- Uniform-sky sensor NMBE: `{uniform_metrics['nmbe_percent']:.4f}%`",
            f"- Uniform-sky sensor CV(RMSE): `{uniform_metrics['cvrmse_percent']:.4f}%`",
            f"- Engine tracing: `{payload['engine']['timings_ms']['tracing_ms']:.4f} ms`",
            f"- Radiance rcontrib: `{payload['radiance']['elapsed_ms']:.4f} ms`",
        ]
    annual = payload.get("annual")
    if annual:
        annual_metrics = annual["illuminance_comparison"]
        lines.extend(
            [
                "",
                "## Annual Metrics",
                "",
                f"- Timesteps: `{annual['timestep_count']}`",
                f"- Occupied hours: `{annual['occupied_hours']}`",
                f"- Illuminance NMBE: `{annual_metrics['nmbe_percent']:.4f}%`",
                f"- Illuminance CV(RMSE): `{annual_metrics['cvrmse_percent']:.4f}%`",
                "- Mean DA difference: "
                f"`{annual['metric_differences']['mean_daylight_autonomy']:.6f}`",
                "- sDA difference: "
                f"`{annual['metric_differences']['static_sda_300_50_percentage_points']:.4f} pp`",
                "- Engine/CPU reduction maximum DA error: "
                f"`{annual['engine_reduction_contract']['maximum_daylight_autonomy_error']:.8g}`",
            ]
        )
    lines.append("")
    return "\n".join(lines)


def main():
    args = parse_args()
    if args.samples <= 0 or args.bounces <= 0:
        raise ValueError("samples and bounces must be positive")
    output = Path(args.output).expanduser().resolve()
    output.mkdir(parents=True, exist_ok=True)

    model = shaded_shoebox(embedded_grid=True)
    prepared = prepare_honeybee_scene(model)
    arrays = {name: value.copy() for name, value in prepared.arrays.items()}
    if args.glass_transmittance is not None:
        arrays = add_glass(
            arrays,
            prepared.model.apertures[0],
            args.glass_transmittance,
        )

    engine = Engine({"backend": args.backend})
    scene = create_native_scene(engine, arrays)
    if args.annual:
        sky, occupancy = deterministic_annual_sky()
    else:
        sky = np.zeros((146, 1, 3), dtype=np.float32)
        occupancy = np.ones(1, dtype=np.float32)
    started = time.perf_counter()
    result = scene.analyze(
        sky,
        occupancy,
        quality="preview",
        maximum_samples=args.samples,
        maximum_bounces=args.bounces,
        scene_seed=0,
        export_coefficients=True,
    ).result()
    wall_clock_ms = (time.perf_counter() - started) * 1000.0
    if result.used_reference_fallback or result.transport_backend == "reference":
        raise RuntimeError(
            "full transport did not execute entirely on GPU hardware; "
            f"transport_backend={result.transport_backend!r}, "
            f"used_reference_fallback={result.used_reference_fallback}"
        )
    if args.backend != "auto" and result.transport_backend != args.backend:
        raise RuntimeError(
            f"requested backend {args.backend!r} but engine used "
            f"{result.transport_backend!r}"
        )
    coefficients = result.coefficients()
    if coefficients is None:
        raise RuntimeError("native engine did not export transport coefficients")
    engine_coefficients = np.ascontiguousarray(coefficients, dtype=np.float32)
    radiance, commands, radiance_ms, versions = run_radiance(
        arrays,
        output,
        args.samples,
        args.bounces,
        args.workers,
        args.radiance_bin,
        args.glass_transmittance,
    )
    np.save(output / "engine_coefficients.npy", engine_coefficients)
    np.save(output / "radiance_coefficients.npy", radiance)

    payload = {
        "samples": args.samples,
        "bounces": args.bounces,
        "glass_transmittance": args.glass_transmittance,
        "comparison": comparison(radiance, engine_coefficients),
        "uniform_sky_sensor_comparison": comparison(
            np.sum(radiance, axis=1),
            np.sum(engine_coefficients, axis=1),
        ),
        "engine": {
            "requested_backend": args.backend,
            "transport_backend": result.transport_backend,
            "used_reference_fallback": result.used_reference_fallback,
            "timings_ms": result.timings(),
            "wall_clock_ms": wall_clock_ms,
        },
        "radiance": {
            "commands": commands,
            "versions": versions,
            "ambient_bounces": args.bounces + 1,
            "elapsed_ms": radiance_ms,
        },
    }
    if args.annual:
        payload["annual"] = annual_comparison(
            engine_coefficients,
            radiance,
            sky,
            occupancy,
            arrays["sensor_area_weights"],
            result,
        )
        payload["annual"]["radiance_total_ms"] = (
            radiance_ms + payload["annual"]["radiance_postprocess_ms"]
        )
    (output / "comparison.json").write_text(
        json.dumps(payload, indent=2) + "\n",
        encoding="utf-8",
    )
    report = report_markdown(payload)
    (output / "comparison.md").write_text(report, encoding="utf-8")
    print(report)
    print(output / "comparison.md")


if __name__ == "__main__":
    main()
