#!/usr/bin/env python3
"""Audit runtime-compiled MSL for version-gated ray-tracing features."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


CHECKS = (
    (
        re.compile(r"\batomic_float\b"),
        "atomic_float is not in the baseline profile; use fixed-point atomics or an explicit supported language version",
    ),
    (
        re.compile(r"\bintersection_query\s*<"),
        "intersection_query is version-gated; use intersector<triangle_data, instancing>",
    ),
    (
        re.compile(r"\bintersection_params\b"),
        "intersection_params is version-gated; configure an intersector directly",
    ),
    (
        re.compile(r"\b(?:get_)?(?:candidate|committed)_intersection"),
        "candidate/committed query methods require the version-gated query API",
    ),
    (
        re.compile(r"\buser_instance_id\b"),
        "user_instance_id may be unavailable; use descriptor-order instance_id for metadata",
    ),
)

PRIVATE_CHECKS = (
    (
        re.compile(r"\b_intersection_params\b"),
        "_intersection_params is a private compiler type and must not be used",
    ),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check runtime-compiled Metal sources for baseline compatibility."
    )
    parser.add_argument("paths", nargs="+", type=Path, help="MSL source files to audit")
    parser.add_argument(
        "--allow-version-gated",
        action="store_true",
        help="Allow public version-gated APIs after host-side feature checks",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    failures: list[str] = []
    checks = PRIVATE_CHECKS if args.allow_version_gated else PRIVATE_CHECKS + CHECKS

    for path in args.paths:
        if not path.is_file():
            failures.append(f"{path}: file does not exist")
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for pattern, message in checks:
                if pattern.search(line):
                    failures.append(f"{path}:{line_number}: {message}")

    if failures:
        print("\n".join(failures))
        return 1

    print(f"MSL compatibility check passed for {len(args.paths)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
