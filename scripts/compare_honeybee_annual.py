#!/usr/bin/env python3
"""Compare Foton annual output with a stock or converged Radiance result."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from foton.honeybee import compare_annual_daylight


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--foton", required=True)
    parser.add_argument("--radiance", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--oracle", choices=("stock", "converged"), default="stock")
    parser.add_argument("--radiance-manifest")
    parser.add_argument("--fail-on-threshold", action="store_true")
    args = parser.parse_args()
    foton_metadata = json.loads(
        Path(args.foton, "metadata.json").read_text(encoding="utf-8")
    )
    foton_seconds = foton_metadata["timings"]["cold_end_to_end_seconds"]
    radiance_seconds = None
    if args.radiance_manifest:
        radiance_seconds = json.loads(
            Path(args.radiance_manifest).read_text(encoding="utf-8")
        )["elapsed_seconds"]
    report = compare_annual_daylight(
        args.foton,
        args.radiance,
        model=args.model,
        foton_seconds=foton_seconds,
        radiance_seconds=radiance_seconds,
        output_folder=args.output,
        oracle=args.oracle,
    )
    print(Path(args.output).expanduser().resolve() / "comparison.json")
    return 1 if args.fail_on_threshold and not report["passed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
