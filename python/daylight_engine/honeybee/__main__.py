"""Command-line interface for Foton Honeybee workflows."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .annual import run_annual_daylight


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m foton.honeybee")
    commands = parser.add_subparsers(dest="command", required=True)
    annual = commands.add_parser(
        "annual-daylight", help="run annual daylight from HBJSON and EPW/WEA"
    )
    annual.add_argument("--model", required=True)
    annual.add_argument("--wea", required=True)
    annual.add_argument("--output", required=True)
    annual.add_argument(
        "--backend",
        choices=("auto", "metal", "vulkan", "reference", "cpu"),
        default="auto",
    )
    annual.add_argument("--grid-filter", default="*")
    annual.add_argument("--schedule")
    annual.add_argument("--north", type=float, default=0)
    annual.add_argument("--quality", choices=("preview", "final"), default="final")
    annual.add_argument("--threshold", type=float, default=300)
    annual.add_argument("--udi-lower", type=float, default=100)
    annual.add_argument("--udi-upper", type=float, default=3000)
    annual.add_argument("--target-time", type=float, default=50)
    annual.add_argument("--maximum-samples", type=int, default=256)
    annual.add_argument("--maximum-bounces", type=int, default=1)
    annual.add_argument("--scene-seed", type=int, default=0)
    annual.add_argument("--radiance-bin")
    annual.add_argument(
        "--export-illuminance",
        action=argparse.BooleanOptionalAction,
        default=True,
    )
    return parser


def main(argv=None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "annual-daylight":
        run = run_annual_daylight(
            model=args.model,
            wea=args.wea,
            output_folder=args.output,
            backend=args.backend,
            grid_filter=args.grid_filter,
            schedule=args.schedule,
            north=args.north,
            quality=args.quality,
            threshold=args.threshold,
            udi_lower=args.udi_lower,
            udi_upper=args.udi_upper,
            target_time=args.target_time,
            maximum_samples=args.maximum_samples,
            maximum_bounces=args.maximum_bounces,
            scene_seed=args.scene_seed,
            radiance_bin=args.radiance_bin,
            export_illuminance=args.export_illuminance,
        )
        manifest = {
            "recipe": "annual_daylight",
            "status": "complete",
            "results_folder": str(run.results_folder),
            "metadata": str(Path(args.output).expanduser().resolve() / "metadata.json"),
            "grids": [
                {
                    "identifier": grid.identifier,
                    "full_identifier": grid.full_identifier,
                    "room_identifier": grid.room_identifier,
                    "sensor_count": grid.sensor_count,
                    "sda": grid.sda,
                }
                for grid in run.grids
            ],
            "timings": run.timings,
        }
        print(json.dumps(manifest, sort_keys=True))
        return 0
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
