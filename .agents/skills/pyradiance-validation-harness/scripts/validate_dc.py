#!/usr/bin/env python3
"""Validate a GPU daylight-coefficient matrix against a Radiance reference."""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np


BASIS_ROWS = {"tregenza": 146, "reinhart-mf2": 578}
PHOTOPIC_WEIGHTS = np.asarray([47.435, 119.93, 11.635], dtype=np.float64)


def radiance_environment(executable: str) -> dict[str, str]:
    environment = os.environ.copy()
    candidates = []
    if environment.get("RADIANCE_LIB"):
        candidates.append(Path(environment["RADIANCE_LIB"]).expanduser())
    resolved_executable = shutil.which(executable) or executable
    executable_path = Path(resolved_executable).expanduser().resolve()
    candidates.append(executable_path.parent.parent / "lib")
    ray_paths = [
        value
        for value in environment.get("RAYPATH", ".").split(os.pathsep)
        if value
    ]
    for directory in candidates:
        if (directory / "rayinit.cal").is_file():
            resolved = str(directory.resolve())
            if resolved not in ray_paths:
                ray_paths.insert(0, resolved)
    environment["RAYPATH"] = os.pathsep.join(ray_paths)
    return environment


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--oct", required=True, type=Path)
    parser.add_argument("--pts", required=True, type=Path)
    parser.add_argument("--gpu", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--rcontrib", default="rcontrib")
    parser.add_argument("--rcontrib-args", default=os.environ.get("RADIANCE_RCONTRIB_ARGS", ""))
    parser.add_argument("--reference", type=Path, help="Precomputed whitespace-separated reference matrix")
    parser.add_argument("--basis", choices=(*BASIS_ROWS, "custom"), default="tregenza")
    parser.add_argument(
        "--mode",
        choices=("direct-visibility", "daylight-coefficient", "annual-illuminance"),
        default="daylight-coefficient",
    )
    parser.add_argument("--radiance-components", choices=("rgb", "scalar"), default="rgb")
    parser.add_argument("--nmbe-limit", type=float, default=5.0)
    parser.add_argument("--cvrmse-limit", type=float, default=10.0)
    parser.add_argument("--max-absolute-limit", type=float, default=0.01)
    parser.add_argument("--fail-on-threshold", action="store_true")
    return parser.parse_args()


def sensor_count(path: Path) -> int:
    count = 0
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if line:
            if len(line.split()) < 6:
                raise ValueError("sensor file contains a row with fewer than 6 values")
            count += 1
    if count == 0:
        raise ValueError("sensor file contains no rows")
    return count


def read_gpu_csv(
    path: Path,
    expected_sensors: int,
    expected_patches: int | None,
) -> np.ndarray:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("GPU CSV has no header")
        fields = {field.strip().lower(): field for field in reader.fieldnames}
        sensor_field = fields.get("sensor_index") or fields.get("sensor")
        patch_field = fields.get("sky_patch_index") or fields.get("sky_patch") or fields.get("patch")
        value_field = fields.get("coefficient") or fields.get("value")
        if not sensor_field or not patch_field or not value_field:
            raise ValueError("GPU CSV requires sensor_index, sky_patch_index, and coefficient/value columns")
        entries: dict[tuple[int, int], float] = {}
        max_patch = -1
        for row_number, row in enumerate(reader, 2):
            try:
                sensor = int(row[sensor_field])
                patch = int(row[patch_field])
                value = float(row[value_field])
            except (TypeError, ValueError) as exc:
                raise ValueError(f"GPU CSV row {row_number}: invalid index or value") from exc
            if sensor < 0 or sensor >= expected_sensors or patch < 0:
                raise ValueError(f"GPU CSV row {row_number}: index is outside the expected range")
            if expected_patches is not None and patch >= expected_patches:
                raise ValueError(
                    f"GPU CSV row {row_number}: patch {patch} exceeds {expected_patches - 1}"
                )
            if not math.isfinite(value):
                raise ValueError(f"GPU CSV row {row_number}: value must be finite")
            key = (sensor, patch)
            if key in entries:
                raise ValueError(f"GPU CSV row {row_number}: duplicate sensor/patch cell {key}")
            entries[key] = value
            max_patch = max(max_patch, patch)
    if max_patch < 0:
        raise ValueError("GPU CSV contains no data rows")
    patch_count = expected_patches or max_patch + 1
    if expected_patches is not None and max_patch + 1 != expected_patches:
        raise ValueError(
            f"GPU CSV contains {max_patch + 1} patch indices; {expected_patches} required"
        )
    matrix = np.full((expected_sensors, patch_count), np.nan, dtype=np.float64)
    for (sensor, patch), value in entries.items():
        matrix[sensor, patch] = value
    if np.isnan(matrix).any():
        missing = int(np.isnan(matrix).sum())
        raise ValueError(f"GPU CSV is missing {missing} sensor/sky-patch cells")
    return matrix


def read_reference(path: Path, expected_shape: tuple[int, int]) -> np.ndarray:
    try:
        matrix = np.load(path) if path.suffix == ".npy" else np.loadtxt(path)
    except (OSError, ValueError) as exc:
        raise ValueError(f"could not read reference matrix: {exc}") from exc
    matrix = np.asarray(matrix, dtype=np.float64)
    if matrix.ndim == 1:
        matrix = matrix.reshape((expected_shape[0], -1))
    if matrix.shape != expected_shape:
        raise ValueError(f"reference shape {matrix.shape} does not match GPU shape {expected_shape}")
    return matrix


def run_rcontrib(args: argparse.Namespace, expected_shape: tuple[int, int]) -> np.ndarray:
    if not args.rcontrib_args.strip():
        raise RuntimeError(
            "live rcontrib validation requires --rcontrib-args or RADIANCE_RCONTRIB_ARGS"
        )
    command = [args.rcontrib, "-I+", "-h", *shlex.split(args.rcontrib_args), str(args.oct)]
    sensor_text = args.pts.read_text(encoding="utf-8")
    try:
        completed = subprocess.run(
            command,
            input=sensor_text,
            text=True,
            capture_output=True,
            env=radiance_environment(args.rcontrib),
            check=False,
        )
    except OSError as exc:
        raise RuntimeError(f"could not execute rcontrib: {exc}") from exc
    if completed.returncode:
        detail = completed.stderr.strip() or "no stderr output"
        raise RuntimeError(f"rcontrib exited with status {completed.returncode}: {detail}")
    values = np.fromstring(completed.stdout, sep=" ", dtype=np.float64)
    expected_size = expected_shape[0] * expected_shape[1]
    component_count = 3 if args.radiance_components == "rgb" else 1
    if values.size != expected_size * component_count:
        raise RuntimeError(
            f"rcontrib returned {values.size} values; expected "
            f"{expected_size * component_count} for {args.radiance_components} shape {expected_shape}"
        )
    if component_count == 3:
        rgb = values.reshape((*expected_shape, 3))
        return rgb @ PHOTOPIC_WEIGHTS
    return values.reshape(expected_shape)


def metrics(reference: np.ndarray, gpu: np.ndarray) -> dict[str, float | None]:
    difference = gpu - reference
    reference_mean = float(np.mean(reference))
    nmbe = None
    cvrmse = None
    if reference_mean != 0:
        nmbe = 100.0 * float(np.sum(difference)) / float(np.sum(reference))
        cvrmse = 100.0 * float(np.sqrt(np.mean(difference**2))) / abs(reference_mean)
    return {
        "nmbe_percent": nmbe,
        "cvrmse_percent": cvrmse,
        "mean_absolute_error": float(np.mean(np.abs(difference))),
        "max_absolute_error": float(np.max(np.abs(difference))),
        "reference_mean": reference_mean,
    }


def passes(args: argparse.Namespace, result: dict[str, float | None]) -> bool:
    if args.mode == "direct-visibility":
        return bool(result["max_absolute_error"] <= args.max_absolute_limit)
    return bool(
        result["nmbe_percent"] is not None
        and result["cvrmse_percent"] is not None
        and abs(result["nmbe_percent"]) <= args.nmbe_limit
        and result["cvrmse_percent"] <= args.cvrmse_limit
    )


def write_report(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    metrics_payload = payload["metrics"]
    nmbe = metrics_payload["nmbe_percent"]
    cvrmse = metrics_payload["cvrmse_percent"]
    nmbe_text = "undefined" if nmbe is None else f"{nmbe:.6f}%"
    cvrmse_text = "undefined" if cvrmse is None else f"{cvrmse:.6f}%"
    markdown = "\n".join(
        [
            "# Daylight Coefficient Validation",
            "",
            f"- GPU matrix shape: `{payload['gpu_shape']}`",
            f"- Validation mode: `{payload['mode']}`",
            f"- Sky basis: `{payload['basis']}`",
            f"- Reference source: `{payload['reference_source']}`",
            f"- NMBE: `{nmbe_text}`",
            f"- CV(RMSE): `{cvrmse_text}`",
            f"- Mean absolute error: `{metrics_payload['mean_absolute_error']:.9g}`",
            f"- Maximum absolute error: `{metrics_payload['max_absolute_error']:.9g}`",
            f"- Passed thresholds: `{payload['passed']}`",
            "",
            "Metrics use the dense zero-based `[sensor, sky_patch]` matrix contract.",
            "",
        ]
    )
    path.write_text(markdown, encoding="utf-8")
    json_path = path.with_suffix(".json")
    json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    required_paths = [(args.oct, "octree"), (args.pts, "sensor file"), (args.gpu, "GPU CSV")]
    if args.reference:
        required_paths.append((args.reference, "reference matrix"))
    for path, label in required_paths:
        if not path.expanduser().is_file():
            print(f"error: {label} does not exist: {path}", file=sys.stderr)
            return 2
    try:
        sensors = sensor_count(args.pts)
        expected_patches = BASIS_ROWS.get(args.basis)
        gpu = read_gpu_csv(args.gpu, sensors, expected_patches)
        reference = (
            read_reference(args.reference, gpu.shape)
            if args.reference
            else run_rcontrib(args, gpu.shape)
        )
        result = metrics(reference, gpu)
        passed = passes(args, result)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    payload = {
        "format": "vulkan-daylight-validation-v1",
        "gpu_shape": [int(value) for value in gpu.shape],
        "mode": args.mode,
        "basis": args.basis,
        "reference_source": str(args.reference) if args.reference else "rcontrib",
        "metrics": result,
        "thresholds": {
            "nmbe_percent": args.nmbe_limit,
            "cvrmse_percent": args.cvrmse_limit,
            "max_absolute_error": args.max_absolute_limit,
        },
        "passed": passed,
    }
    write_report(args.out.expanduser().resolve(), payload)
    print(f"passed: {passed}")
    if result["nmbe_percent"] is not None:
        print(f"NMBE: {result['nmbe_percent']:.6f}%")
        print(f"CV(RMSE): {result['cvrmse_percent']:.6f}%")
    print(f"maximum absolute error: {result['max_absolute_error']:.9g}")
    return 1 if args.fail_on_threshold and not passed else 0


if __name__ == "__main__":
    raise SystemExit(main())
