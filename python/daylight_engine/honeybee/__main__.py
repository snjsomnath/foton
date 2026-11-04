"""Command-line interface for Foton Honeybee workflows."""

from __future__ import annotations

import argparse
import json
import sys

from .annual import DEFAULT_MAXIMUM_BOUNCES
from .commands import annual_daylight, daylight_factor
from .protocol import PROTOCOL_NAME, PROTOCOL_VERSION, ProtocolWriter
from .weather import _default_cache_directory
from .preflight import inspect_installation

BACKENDS = ("auto", "metal", "vulkan", "reference", "cpu")


def _trace_arguments(parser):
    parser.add_argument("--model", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--backend", choices=BACKENDS, default="auto")
    parser.add_argument("--grid-filter", default="*")
    parser.add_argument("--quality", choices=("preview", "final"), default="final")
    parser.add_argument("--sky-density", choices=(1, 2), type=int, default=1)
    parser.add_argument("--direct-samples", type=int)
    parser.add_argument("--maximum-samples", type=int)
    parser.add_argument(
        "--maximum-bounces", type=int, default=DEFAULT_MAXIMUM_BOUNCES
    )
    parser.add_argument("--scene-seed", type=int, default=0)
    parser.add_argument("--jsonl", action="store_true")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="foton-honeybee")
    commands = parser.add_subparsers(dest="command", required=True)
    capabilities = commands.add_parser(
        "capabilities", help="report protocol, engine, and cache capabilities"
    )
    capabilities.add_argument("--backend", choices=BACKENDS, default="auto")
    capabilities.add_argument("--jsonl", action="store_true")
    capabilities.add_argument("--output")
    capabilities.add_argument("--radiance-bin")
    annual = commands.add_parser(
        "annual-daylight", help="run annual daylight from HBJSON and EPW/WEA"
    )
    _trace_arguments(annual)
    annual.add_argument("--wea", required=True)
    annual.add_argument("--schedule")
    annual.add_argument("--north", type=float, default=0)
    annual.add_argument("--threshold", type=float, default=300)
    annual.add_argument("--udi-lower", type=float, default=100)
    annual.add_argument("--udi-upper", type=float, default=3000)
    annual.add_argument("--target-time", type=float, default=50)
    annual.add_argument("--radiance-bin")
    annual.add_argument(
        "--sky-source",
        choices=("foton", "gendaymtx"),
        default="foton",
        help="sky matrix source: Foton's built-in Perez sky (default) or "
        "Radiance's gendaymtx",
    )
    annual.add_argument(
        "--export-illuminance",
        action=argparse.BooleanOptionalAction,
        default=True,
    )
    factor = commands.add_parser(
        "daylight-factor",
        help="run daylight factor (CIE overcast sky) from HBJSON",
    )
    _trace_arguments(factor)
    commands.add_parser(
        "serve",
        help="keep studies warm and answer JSON-lines requests on stdin",
    )
    return parser


def _capabilities(backend, output=None, radiance_bin=None):
    inspected = inspect_installation(backend, output, radiance_bin)
    return {
        **inspected,
        "protocol": PROTOCOL_NAME,
        "protocol_version": PROTOCOL_VERSION,
        "recipes": ["annual_daylight", "daylight_factor", "direct_visibility"],
        "worker": True,
        "sky_densities": [1, 2],
        "quality_presets": ["preview", "final"],
        "weather_cache": str(_default_cache_directory()),
    }


def _options(args):
    options = dict(vars(args))
    for key in ("command", "jsonl"):
        options.pop(key, None)
    return options


def main(argv=None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "serve":
        from .worker import serve

        return serve()
    writer = ProtocolWriter(sys.stdout)
    try:
        if args.command == "capabilities":
            payload = _capabilities(args.backend, args.output, args.radiance_bin)
            if args.jsonl:
                writer.emit("capabilities", capabilities=payload)
            else:
                print(json.dumps(payload, sort_keys=True))
            return 0

        recipe = args.command.replace("-", "_")
        run = annual_daylight if args.command == "annual-daylight" else daylight_factor
        if args.jsonl:
            writer.emit(
                "started",
                recipe=recipe,
                progress=0.0,
                message="Preparing Honeybee "
                + ("annual daylight" if recipe == "annual_daylight" else "daylight factor")
                + " study",
            )

        def progress(update):
            if args.jsonl:
                writer.emit("progress", **update)

        manifest = run(_options(args), progress=progress)
        if args.jsonl:
            writer.emit(
                "complete",
                progress=1.0,
                message=(
                    "Annual daylight analysis complete"
                    if recipe == "annual_daylight"
                    else "Daylight factor analysis complete"
                ),
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
