#!/usr/bin/env python3
"""Collect the converged Radiance references of a finished campaign into a
portable bundle that `validate_release_suite.py --reuse-references` can consume.

The references are independent of the GPU backend: they describe the scene,
not the engine. A machine without the cores to redo the Radiance oracle (a
cloud GPU with two vCPUs) can therefore validate its backend against the same
converged references the Metal campaign was judged by. Only cases whose oracle
ran to completion are exported; the bundle records where they came from.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from validation.scenes import SCENE_IDS  # noqa: E402

BUNDLE_SCHEMA_VERSION = 1
ARRAYS = (
    "radiance_converged_full.npy",
    "radiance_integrated_direct.npy",
    "radiance_one_bounce_full.npy",
)
# Report fields describing the oracle rather than the candidate; a reusing
# run carries them over verbatim.
CARRIED_FIELDS = (
    "scene",
    "sky_density",
    "scene_spec",
    "model_sha256",
    "model_summary",
    "oracle_stable",
    "direct_stability",
    "depth_stability",
    "sample_stability",
    "oracle_levels",
    "direct_oracles",
    "export_command",
)


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def sensor_grid_array(hbjson_path):
    """Sensor positions and directions in model order, as the HBJSON stores
    them: the geometry the coefficients index, independent of Honeybee's other
    serialisation details. Shape (sensors, 6)."""
    model = json.loads(Path(hbjson_path).read_text())
    radiance = (model.get("properties") or {}).get("radiance") or {}
    grids = radiance.get("sensor_grids") or []
    rows = [
        list(sensor.get("pos", ())) + list(sensor.get("dir", ()))
        for grid in grids
        for sensor in grid.get("sensors", [])
    ]
    return np.asarray(rows, dtype=np.float64).reshape(-1, 6)


def sensor_grid_digest(hbjson_path):
    """SHA-256 of the sensor grid array's bytes. Informational: libm
    implementations differ in the last bit of rotated coordinates, so the
    consuming suite compares the array numerically."""
    return hashlib.sha256(sensor_grid_array(hbjson_path).tobytes()).hexdigest()


def export_case(case_dir, destination):
    report = json.loads((case_dir / "report.json").read_text())
    if "error" in report or not report.get("oracle_levels"):
        return None, "oracle did not complete"
    missing = [field for field in CARRIED_FIELDS if field not in report]
    if missing:
        return None, "report lacks " + ", ".join(missing)
    direct_count = report["direct_oracles"][-1]["sample_count"]
    direct_path = case_dir / ("direct_%d" % direct_count) / "radiance_integrated_direct.npy"
    one_bounce = report["oracle_levels"][0]
    replicates = sorted(
        case_dir.glob(
            "ad%d_b%d_r*/radiance_full.npy"
            % (one_bounce["samples"], one_bounce["material_bounces"])
        )
    )
    converged_path = case_dir / "radiance_converged_full.npy"
    model_path = case_dir / "model.hbjson"
    if (
        not direct_path.exists()
        or not converged_path.exists()
        or not model_path.exists()
        or not replicates
    ):
        return None, "reference arrays or model are missing"
    destination.mkdir(parents=True)
    shutil.copyfile(converged_path, destination / ARRAYS[0])
    shutil.copyfile(direct_path, destination / ARRAYS[1])
    np.save(
        destination / ARRAYS[2],
        np.mean([np.load(p) for p in replicates], axis=0).astype(np.float32),
    )
    reference = {field: report[field] for field in CARRIED_FIELDS}
    np.save(destination / "sensor_grid.npy", sensor_grid_array(model_path))
    reference["sensor_grid_file"] = "sensor_grid.npy"
    reference["sensor_grid_sha256"] = sensor_grid_digest(model_path)
    reference["arrays"] = {name: sha256(destination / name) for name in ARRAYS}
    reference["one_bounce_replicates"] = len(replicates)
    (destination / "reference.json").write_text(json.dumps(reference, indent=2))
    return reference, None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "campaign", type=Path, help="Finished campaign directory holding suite.json"
    )
    parser.add_argument("--output", type=Path, required=True, help="New bundle directory")
    args = parser.parse_args()
    suite = json.loads((args.campaign / "suite.json").read_text())
    args.output.mkdir(parents=True, exist_ok=False)
    bundle = {
        "schema_version": BUNDLE_SCHEMA_VERSION,
        "source": {
            "campaign": args.campaign.resolve().name,
            "commit": suite.get("commit"),
            "dirty": suite.get("dirty"),
            "smoke": suite.get("smoke"),
            "suite_version": suite.get("suite_version"),
            "engine_version": suite.get("engine_version"),
            "backend": suite.get("backend"),
            "hardware": suite.get("hardware"),
            "weather_sha256": suite.get("weather_sha256"),
            "started_at": suite.get("started_at"),
        },
        "cases": [],
        "skipped": [],
    }
    for identifier in SCENE_IDS:
        for density in (1, 2):
            case_dir = args.campaign / identifier / ("mf%d" % density)
            skipped = {"scene": identifier, "sky_density": density}
            if not (case_dir / "report.json").exists():
                bundle["skipped"].append({**skipped, "reason": "no report"})
                continue
            reference, reason = export_case(
                case_dir, args.output / identifier / ("mf%d" % density)
            )
            if reference is None:
                bundle["skipped"].append({**skipped, "reason": reason})
                continue
            bundle["cases"].append(
                {
                    "scene": identifier,
                    "sky_density": density,
                    "oracle_stable": reference["oracle_stable"],
                    "model_sha256": reference["model_sha256"],
                    "sensor_grid_sha256": reference["sensor_grid_sha256"],
                    "arrays": reference["arrays"],
                }
            )
    (args.output / "bundle.json").write_text(json.dumps(bundle, indent=2))
    print(
        "%d cases exported, %d skipped, from %s (%s)"
        % (
            len(bundle["cases"]),
            len(bundle["skipped"]),
            bundle["source"]["campaign"],
            (bundle["source"]["commit"] or "")[:12],
        )
    )
    return 0 if bundle["cases"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
