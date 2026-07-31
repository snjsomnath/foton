#!/usr/bin/env python3
"""Validate and serialize a Radiance-style sensor grid."""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

import numpy as np


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--csv-out", required=True, type=Path)
    parser.add_argument("--npy-out", required=True, type=Path)
    parser.add_argument("--metadata-out", type=Path)
    parser.add_argument("--room-index", type=int, default=0)
    normal_group = parser.add_mutually_exclusive_group()
    normal_group.add_argument("--normalize-normals", action="store_true")
    normal_group.add_argument("--preserve-normal-length", action="store_true")
    return parser.parse_args()


def read_sensors(path: Path, normalize: bool) -> np.ndarray:
    rows: list[list[float]] = []
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue
        fields = line.split()
        if len(fields) < 6:
            raise ValueError(f"line {line_number}: expected at least 6 numeric values")
        try:
            values = [float(value) for value in fields[:6]]
        except ValueError as exc:
            raise ValueError(f"line {line_number}: non-numeric coordinate or normal") from exc
        if not all(math.isfinite(value) for value in values):
            raise ValueError(f"line {line_number}: values must be finite")
        normal_length = math.sqrt(sum(value * value for value in values[3:]))
        if normal_length == 0:
            raise ValueError(f"line {line_number}: normal must have non-zero length")
        if normalize:
            values[3:] = [value / normal_length for value in values[3:]]
        rows.append(values)
    if not rows:
        raise ValueError("sensor file contains no sensor rows")
    return np.asarray(rows, dtype=np.float32)


def main() -> int:
    args = parse_args()
    source = args.input.expanduser().resolve()
    if not source.is_file():
        print(f"error: sensor file does not exist: {source}", file=sys.stderr)
        return 2
    if args.room_index < 0:
        print("error: --room-index must be non-negative", file=sys.stderr)
        return 2
    try:
        sensors = read_sensors(source, not args.preserve_normal_length)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    csv_path = args.csv_out.expanduser().resolve()
    npy_path = args.npy_out.expanduser().resolve()
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    npy_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["room_index", "sensor_index", "x", "y", "z", "nx", "ny", "nz"])
        for index, row in enumerate(sensors):
            writer.writerow([args.room_index, index, *[f"{value:.9g}" for value in row]])
    np.save(npy_path, sensors)
    if args.metadata_out:
        metadata_path = args.metadata_out.expanduser().resolve()
        metadata_path.parent.mkdir(parents=True, exist_ok=True)
        metadata = {
            "format": "vulkan-daylight-sensor-grid-v1",
            "source": str(source),
            "room_index": args.room_index,
            "sensor_count": int(len(sensors)),
            "shape": [int(value) for value in sensors.shape],
            "columns": ["x", "y", "z", "nx", "ny", "nz"],
            "normals_normalized": not args.preserve_normal_length,
        }
        metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(f"prepared {len(sensors)} sensors")
    print(f"csv: {csv_path}")
    print(f"npy: {npy_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
