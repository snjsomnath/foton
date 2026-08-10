"""Command-line interface for Foton Honeybee workflows."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .annual import run_annual_daylight
from .protocol import (
    PROTOCOL_NAME,
    PROTOCOL_VERSION,
    ProtocolWriter,
    annual_manifest,
    annual_request,
)
from .weather import _default_cache_directory


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="foton-honeybee")
    commands = parser.add_subparsers(dest="command", required=True)
    capabilities = commands.add_parser(
        "capabilities", help="report protocol, engine, and cache capabilities"
    )
    capabilities.add_argument(
        "--backend",
        choices=("auto", "metal", "vulkan", "reference", "cpu"),
        default="auto",
    )
    capabilities.add_argument("--jsonl", action="store_true")
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
    annual.add_argument("--sky-density", choices=(1, 2), type=int, default=1)
    annual.add_argument("--threshold", type=float, default=300)
    annual.add_argument("--udi-lower", type=float, default=100)
    annual.add_argument("--udi-upper", type=float, default=3000)
    annual.add_argument("--target-time", type=float, default=50)
    annual.add_argument("--direct-samples", type=int)
    annual.add_argument("--maximum-samples", type=int)
    annual.add_argument("--maximum-bounces", type=int, default=1)
    annual.add_argument("--scene-seed", type=int, default=0)
    annual.add_argument("--radiance-bin")
    annual.add_argument("--jsonl", action="store_true")
    annual.add_argument(
        "--export-illuminance",
        action=argparse.BooleanOptionalAction,
        default=True,
    )
    return parser


def _capabilities(backend):
    from foton import Engine, __version__

    engine = Engine({"backend": backend})
    return {
        "protocol": PROTOCOL_NAME,
        "protocol_version": PROTOCOL_VERSION,
        "engine_version": __version__,
        "engine": dict(engine.capabilities()),
        "recipes": ["annual_daylight", "direct_visibility"],
        "sky_densities": [1, 2],
        "quality_presets": ["preview", "final"],
        "weather_cache": str(_default_cache_directory()),
    }


def _emit(writer, enabled, event, **payload):
    if enabled:
        writer.emit(event, **payload)


def main(argv=None) -> int:
    args = _parser().parse_args(argv)
    writer = ProtocolWriter(sys.stdout)
    try:
        if args.command == "capabilities":
            payload = _capabilities(args.backend)
            if args.jsonl:
                writer.emit("capabilities", capabilities=payload)
            else:
                print(json.dumps(payload, sort_keys=True))
            return 0

        _emit(
            writer,
            args.jsonl,
            "started",
            recipe="annual_daylight",
            progress=0.0,
            message="Preparing Honeybee annual daylight study",
        )

        def progress(update):
            _emit(writer, args.jsonl, "progress", **update)

        progress(
            {
                "stage": "preparation",
                "progress": 0.02,
                "message": "Validating inputs and preparing the scene",
            }
        )
        request = annual_request(
            model=args.model,
            wea=args.wea,
            schedule=args.schedule,
            backend=args.backend,
            grid_filter=args.grid_filter,
            north=args.north,
            quality=args.quality,
            sky_density=args.sky_density,
            threshold=args.threshold,
            udi_lower=args.udi_lower,
            udi_upper=args.udi_upper,
            target_time=args.target_time,
            direct_samples=args.direct_samples,
            maximum_samples=args.maximum_samples,
            maximum_bounces=args.maximum_bounces,
            scene_seed=args.scene_seed,
            export_illuminance=args.export_illuminance,
        )
        run = run_annual_daylight(
            model=args.model,
            wea=args.wea,
            output_folder=args.output,
            backend=args.backend,
            grid_filter=args.grid_filter,
            schedule=args.schedule,
            north=args.north,
            quality=args.quality,
            sky_density=args.sky_density,
            threshold=args.threshold,
            udi_lower=args.udi_lower,
            udi_upper=args.udi_upper,
            target_time=args.target_time,
            direct_samples=args.direct_samples,
            maximum_samples=args.maximum_samples,
            maximum_bounces=args.maximum_bounces,
            scene_seed=args.scene_seed,
            radiance_bin=args.radiance_bin,
            export_illuminance=args.export_illuminance,
            progress=progress,
        )
        manifest = annual_manifest(run, args.output)
        manifest["request"] = request
        manifest_path = Path(args.output).expanduser().resolve() / "run_manifest.json"
        manifest["manifest"] = str(manifest_path)
        manifest_path.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        if args.jsonl:
            writer.emit(
                "complete",
                progress=1.0,
                message="Annual daylight analysis complete",
                manifest=manifest,
            )
        else:
            print(json.dumps(manifest, sort_keys=True))
        return 0
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception as error:
        if getattr(args, "jsonl", False):
            ProtocolWriter(sys.stderr).emit(
                "failed",
                error_type=error.__class__.__name__,
                message=str(error),
            )
        else:
            print(f"foton-honeybee: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
