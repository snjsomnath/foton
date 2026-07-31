#!/usr/bin/env python3
"""Compute DF, daylight autonomy, and area-weighted sDA."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import numpy as np


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--annual-lux", type=Path)
    parser.add_argument("--occupied-mask", type=Path)
    parser.add_argument("--weights", type=Path)
    parser.add_argument("--df-interior", type=Path)
    parser.add_argument("--df-exterior", type=float)
    parser.add_argument("--sda-threshold", type=float, default=300.0)
    parser.add_argument("--sda-time-fraction", type=float, default=0.5)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--sensor-out", type=Path)
    return parser.parse_args()


def load_array(path: Path, label: str) -> np.ndarray:
    try:
        array = np.asarray(np.load(path), dtype=np.float64)
    except (OSError, ValueError) as exc:
        raise ValueError(f"could not load {label}: {exc}") from exc
    if not np.isfinite(array).all():
        raise ValueError(f"{label} contains non-finite values")
    return array


def default_occupied_mask(timestep_count: int) -> np.ndarray:
    if timestep_count != 8760:
        raise ValueError("provide --occupied-mask when annual data does not contain 8760 hours")
    hour_of_day = np.arange(timestep_count) % 24
    return (hour_of_day >= 8) & (hour_of_day < 18)


def main() -> int:
    args = parse_args()
    if not args.annual_lux and not args.df_interior:
        print("error: provide --annual-lux, --df-interior, or both", file=sys.stderr)
        return 2
    if (args.df_interior is None) != (args.df_exterior is None):
        print("error: --df-interior and --df-exterior must be supplied together", file=sys.stderr)
        return 2
    if args.sda_threshold <= 0 or not 0 < args.sda_time_fraction <= 1:
        print("error: sDA threshold and time fraction must be positive", file=sys.stderr)
        return 2

    payload: dict[str, object] = {"format": "vulkan-daylight-metrics-v1"}
    sensor_rows: dict[str, np.ndarray] = {}
    sensor_count: int | None = None
    try:
        if args.annual_lux:
            annual = load_array(args.annual_lux, "annual illuminance")
            if annual.ndim != 2 or annual.shape[1] == 0:
                raise ValueError("annual illuminance must have shape [sensor, timestep]")
            if np.any(annual < 0):
                raise ValueError("annual illuminance cannot be negative")
            sensor_count = annual.shape[0]
            occupied = (
                load_array(args.occupied_mask, "occupied mask").astype(bool)
                if args.occupied_mask
                else default_occupied_mask(annual.shape[1])
            )
            if occupied.ndim != 1 or len(occupied) != annual.shape[1] or not occupied.any():
                raise ValueError("occupied mask must select at least one matching timestep")
            weights = (
                load_array(args.weights, "sensor weights")
                if args.weights
                else np.ones(sensor_count, dtype=np.float64)
            )
            if weights.shape != (sensor_count,) or np.any(weights <= 0):
                raise ValueError("sensor weights must be a positive [sensor] array")
            autonomy = np.mean(annual[:, occupied] >= args.sda_threshold, axis=1)
            passes = autonomy >= args.sda_time_fraction
            sda = 100.0 * float(np.sum(weights[passes])) / float(np.sum(weights))
            payload["sda"] = {
                "spatial_percent": sda,
                "illuminance_threshold_lux": args.sda_threshold,
                "time_fraction": args.sda_time_fraction,
                "occupied_timestep_count": int(np.sum(occupied)),
                "area_weighted": args.weights is not None,
            }
            sensor_rows["daylight_autonomy_fraction"] = autonomy
            sensor_rows["sda_pass"] = passes.astype(np.int8)

        if args.df_interior:
            interior = load_array(args.df_interior, "DF interior illuminance").reshape(-1)
            if args.df_exterior <= 0 or np.any(interior < 0):
                raise ValueError("DF illuminance values must be non-negative and exterior must be positive")
            if sensor_count is not None and len(interior) != sensor_count:
                raise ValueError("DF and annual arrays must contain the same sensor count")
            sensor_count = len(interior)
            daylight_factor = 100.0 * interior / args.df_exterior
            payload["daylight_factor"] = {
                "mean_percent": float(np.mean(daylight_factor)),
                "minimum_percent": float(np.min(daylight_factor)),
                "maximum_percent": float(np.max(daylight_factor)),
                "exterior_horizontal_illuminance_lux": args.df_exterior,
            }
            sensor_rows["daylight_factor_percent"] = daylight_factor
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    output = args.out.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.sensor_out:
        sensor_output = args.sensor_out.expanduser().resolve()
        sensor_output.parent.mkdir(parents=True, exist_ok=True)
        columns = list(sensor_rows)
        with sensor_output.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["sensor_index", *columns])
            for index in range(sensor_count or 0):
                writer.writerow([index, *[sensor_rows[column][index] for column in columns]])
    print(f"wrote metrics: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
