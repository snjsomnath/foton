"""Sweep diffuse bounce depth in Foton and Radiance to pick a default.

For each scene the script runs Radiance (rfluxmtx) at several material bounce
depths to find where the reference itself converges, then runs Foton at the same
depths and reports indirect/full-coefficient error against the deepest Radiance
run. Results land in a dated folder under validation/results/.

    python scripts/bounce_sweep.py --output validation/results/<date>-bounce-sweep
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from foton import Engine  # noqa: E402
from foton.honeybee.adapter import prepare_honeybee_scene  # noqa: E402
from foton.honeybee.radiance import run_radiance_coefficient_stages  # noqa: E402
from validation.oracle import difference, export_scene  # noqa: E402
from validation.scenes import make_scene, scene_metadata  # noqa: E402

DEFAULT_SCENES = (
    "sealed",
    "black_open",
    "coloured_glass",
    "dark_interior",
    "deep_reflective",
    "interior_glazing",
)


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True)
    parser.add_argument("--scenes", nargs="+", default=list(DEFAULT_SCENES))
    parser.add_argument("--bounces", nargs="+", type=int, default=[1, 2, 4, 6, 8, 12])
    parser.add_argument("--sky-density", choices=(1, 2), type=int, default=1)
    parser.add_argument("--backend", default="metal")
    parser.add_argument("--direct-samples", type=int, default=64)
    parser.add_argument("--indirect-samples", type=int, default=4096)
    parser.add_argument("--ambient-divisions", type=int, default=40000)
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--radiance-bin")
    return parser.parse_args()


def ratio(candidate, reference):
    reference = float(np.asarray(reference).sum())
    return round(float(np.asarray(candidate).sum()) / reference, 4) if reference > 0 else None


def summarise(reference, candidate):
    stats = difference(reference, candidate)
    return {
        "bias_percent": round(stats["bias_percent"], 3),
        "rms_percent": round(stats["rms_normalized_error_percent"], 3),
        "energy_ratio": ratio(candidate, reference),
    }


def run_scene(identifier, args, engine, output):
    folder = output / identifier
    folder.mkdir(parents=True, exist_ok=True)
    metadata = scene_metadata(identifier)
    model = make_scene(identifier, ROOT)
    prepared = prepare_honeybee_scene(
        model, include_aperture_glazing=metadata["include_glazing"]
    )
    octree, dome, _ = export_scene(
        model, folder / "oracle", args.sky_density, args.radiance_bin,
        not metadata["include_glazing"],
    )
    positions = prepared.arrays["sensor_positions"]
    normals = prepared.arrays["sensor_normals"]
    rows = 146 if args.sky_density == 1 else 578

    radiance = {}
    for bounces in args.bounces:
        print(f"  Radiance {identifier}: bounces={bounces}", flush=True)
        run = run_radiance_coefficient_stages(
            positions, normals, octree=octree, sky_dome=dome,
            sky_density=args.sky_density,
            work_directory=folder / f"radiance_b{bounces}",
            workers=args.workers, radiance_bin=args.radiance_bin,
            material_bounces=bounces,
            radiance_parameters=("-ad", str(args.ambient_divisions), "-lw", "1e-7", "-dr", "0"),
        )
        radiance[bounces] = {
            "direct": run.direct.astype(np.float64),
            "full": run.full.astype(np.float64),
            "indirect": run.indirect.astype(np.float64),
            "seconds": sum(run.timings_ms.values()) / 1000.0,
        }

    scene = prepared.create_native_scene(engine)
    sky = np.zeros((rows, 1, 3), dtype=np.float32)
    occupancy = np.ones(1, dtype=np.float32)
    foton = {}
    for bounces in args.bounces:
        kwargs = dict(
            quality="final", direct_samples=args.direct_samples,
            maximum_samples=args.indirect_samples, maximum_bounces=bounces,
            scene_seed=0, export_coefficients=True,
        )
        scene.analyze(sky, occupancy, **kwargs).result()
        started = time.perf_counter()
        result = scene.analyze(sky, occupancy, **kwargs).result()
        wall_ms = (time.perf_counter() - started) * 1000.0
        full = np.asarray(result.coefficients(), dtype=np.float64).reshape(len(positions), rows, 3)
        np.save(folder / f"foton_full_b{bounces}.npy", full.astype(np.float32))
        foton[bounces] = {"full": full, "wall_ms": wall_ms}

    deepest = max(args.bounces)
    reference = radiance[deepest]

    record = {
        "scene": identifier,
        "sensors": int(len(positions)),
        "reference_bounces": deepest,
        "radiance": {},
        "foton": {},
    }
    for bounces in args.bounces:
        r = radiance[bounces]
        record["radiance"][bounces] = {
            "seconds": round(r["seconds"], 1),
            "energy_vs_deepest": ratio(r["full"], reference["full"]),
            "full_vs_deepest": summarise(reference["full"], r["full"]),
        }
        f = foton[bounces]
        indirect = f["full"] - reference["direct"]
        record["foton"][bounces] = {
            "wall_ms": round(f["wall_ms"], 2),
            "energy_vs_1_bounce": ratio(f["full"], foton[args.bounces[0]]["full"]),
            "full_vs_deepest": summarise(reference["full"], f["full"]),
            "indirect_vs_deepest": summarise(reference["indirect"], indirect),
            "full_vs_same_bounces": summarise(radiance[bounces]["full"], f["full"]),
        }
    (folder / "summary.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
    return record


def write_markdown(records, args, output):
    lines = [
        "# Bounce sweep",
        "",
        f"Sky density MF:{args.sky_density}, Radiance `-ad {args.ambient_divisions} -lw 1e-7`, "
        f"Foton {args.backend} direct={args.direct_samples} indirect={args.indirect_samples}.",
        "Errors are against the deepest Radiance run (material bounces = "
        f"{max(args.bounces)}). Bias/RMS in percent of the reference.",
        "",
    ]
    for record in records:
        lines += [f"## {record['scene']} ({record['sensors']} sensors)", ""]
        lines += ["| bounces | Radiance s | Radiance energy / deepest | Radiance full bias % | Foton ms | Foton energy / 1-bounce | Foton full bias % | Foton full RMS % | Foton indirect bias % |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for bounces in args.bounces:
            r = record["radiance"][bounces]
            f = record["foton"][bounces]
            lines.append(
                f"| {bounces} | {r['seconds']} | {r['energy_vs_deepest']} | {r['full_vs_deepest']['bias_percent']} "
                f"| {f['wall_ms']} | {f['energy_vs_1_bounce']} | {f['full_vs_deepest']['bias_percent']} "
                f"| {f['full_vs_deepest']['rms_percent']} | {f['indirect_vs_deepest']['bias_percent']} |"
            )
        lines.append("")
    (output / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    args = parse_args()
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    engine = Engine({"backend": args.backend})
    print("backend:", dict(engine.capabilities())["name"], flush=True)
    records = []
    for identifier in args.scenes:
        print(f"Scene {identifier}", flush=True)
        records.append(run_scene(identifier, args, engine, output))
        write_markdown(records, args, output)
        (output / "summary.json").write_text(
            json.dumps(records, indent=2, default=str), encoding="utf-8"
        )
    print("done", flush=True)


if __name__ == "__main__":
    main()
