#!/usr/bin/env python3
"""Generate a deterministic Radiance shoebox and sensor grid."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--width", type=float, default=6.0)
    parser.add_argument("--depth", type=float, default=9.0)
    parser.add_argument("--height", type=float, default=3.0)
    parser.add_argument("--window-width", type=float, default=3.0)
    parser.add_argument("--window-height", type=float, default=1.5)
    parser.add_argument("--window-sill", type=float, default=0.9)
    parser.add_argument("--sensor-spacing", type=float, default=0.5)
    parser.add_argument("--sensor-height", type=float, default=0.75)
    parser.add_argument("--edge-offset", type=float, default=0.25)
    return parser.parse_args()


def polygon(material: str, name: str, vertices: list[tuple[float, float, float]]) -> str:
    coordinates = "\n".join(f"    {x:g} {y:g} {z:g}" for x, y, z in vertices)
    return f"{material} polygon {name}\n0\n0\n{len(vertices) * 3}\n{coordinates}\n"


def validate(args: argparse.Namespace) -> None:
    positive = {
        "width": args.width,
        "depth": args.depth,
        "height": args.height,
        "window width": args.window_width,
        "window height": args.window_height,
        "sensor spacing": args.sensor_spacing,
    }
    for label, value in positive.items():
        if not math.isfinite(value) or value <= 0:
            raise ValueError(f"{label} must be positive and finite")
    if args.window_width >= args.width:
        raise ValueError("window width must be smaller than room width")
    if args.window_sill < 0 or args.window_sill + args.window_height >= args.height:
        raise ValueError("window must fit inside the south wall")
    if not 0 < args.sensor_height < args.height:
        raise ValueError("sensor height must be inside the room")
    if not 0 <= args.edge_offset < min(args.width, args.depth) / 2:
        raise ValueError("edge offset must fit inside the floor plan")


def generate_geometry(args: argparse.Namespace) -> str:
    width, depth, height = args.width, args.depth, args.height
    window_min = (width - args.window_width) / 2
    window_max = window_min + args.window_width
    sill = args.window_sill
    head = sill + args.window_height
    surfaces = [
        polygon("floor_mat", "floor", [(0, 0, 0), (0, depth, 0), (width, depth, 0), (width, 0, 0)]),
        polygon("ceiling_mat", "ceiling", [(0, 0, height), (width, 0, height), (width, depth, height), (0, depth, height)]),
        polygon("wall_mat", "north_wall", [(0, depth, 0), (0, depth, height), (width, depth, height), (width, depth, 0)]),
        polygon("wall_mat", "west_wall", [(0, 0, 0), (0, 0, height), (0, depth, height), (0, depth, 0)]),
        polygon("wall_mat", "east_wall", [(width, 0, 0), (width, depth, 0), (width, depth, height), (width, 0, height)]),
        polygon("wall_mat", "south_left", [(0, 0, 0), (window_min, 0, 0), (window_min, 0, height), (0, 0, height)]),
        polygon("wall_mat", "south_right", [(window_max, 0, 0), (width, 0, 0), (width, 0, height), (window_max, 0, height)]),
        polygon("wall_mat", "south_below", [(window_min, 0, 0), (window_max, 0, 0), (window_max, 0, sill), (window_min, 0, sill)]),
        polygon("wall_mat", "south_above", [(window_min, 0, head), (window_max, 0, head), (window_max, 0, height), (window_min, 0, height)]),
    ]
    return "\n".join(surfaces)


def sensor_grid(args: argparse.Namespace) -> list[tuple[float, float, float, int, int, int]]:
    sensors = []
    x = args.edge_offset
    while x <= args.width - args.edge_offset + 1e-9:
        y = args.edge_offset
        while y <= args.depth - args.edge_offset + 1e-9:
            sensors.append((x, y, args.sensor_height, 0, 0, 1))
            y += args.sensor_spacing
        x += args.sensor_spacing
    return sensors


def main() -> int:
    args = parse_args()
    try:
        validate(args)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    output = args.output_dir.expanduser().resolve()
    output.mkdir(parents=True, exist_ok=True)
    materials = "\n".join(
        [
            "void plastic wall_mat\n0\n0\n5 0.7 0.7 0.7 0 0\n",
            "void plastic floor_mat\n0\n0\n5 0.2 0.2 0.2 0 0\n",
            "void plastic ceiling_mat\n0\n0\n5 0.8 0.8 0.8 0 0\n",
        ]
    )
    sensors = sensor_grid(args)
    (output / "materials.rad").write_text(materials, encoding="utf-8")
    (output / "room.rad").write_text(generate_geometry(args), encoding="utf-8")
    sensor_text = "\n".join(" ".join(f"{value:g}" for value in row) for row in sensors) + "\n"
    (output / "sensors.pts").write_text(sensor_text, encoding="utf-8")
    metadata = {
        "format": "vulkan-daylight-benchmark-scene-v1",
        "coordinate_system": "right-handed, +Z up, +Y north, aperture on south wall at y=0",
        "dimensions_m": {"width": args.width, "depth": args.depth, "height": args.height},
        "reflectance": {"walls": 0.7, "floor": 0.2, "ceiling": 0.8},
        "window": {
            "type": "open_aperture",
            "width_m": args.window_width,
            "height_m": args.window_height,
            "sill_m": args.window_sill,
        },
        "sensor_grid": {
            "count": len(sensors),
            "spacing_m": args.sensor_spacing,
            "height_m": args.sensor_height,
            "edge_offset_m": args.edge_offset,
        },
    }
    (output / "scene.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(f"generated {len(sensors)} sensors in {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
