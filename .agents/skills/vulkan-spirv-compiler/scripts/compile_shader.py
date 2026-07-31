#!/usr/bin/env python3
"""Compile a GLSL shader to Vulkan SPIR-V with actionable diagnostics."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="GLSL shader path")
    parser.add_argument("--output", type=Path, help="SPIR-V output path")
    parser.add_argument("--target-env", default="vulkan1.3", help="glslang target environment")
    parser.add_argument("--validator", default="glslangValidator", help="Validator executable")
    parser.add_argument(
        "--spirv-val",
        nargs="?",
        const="spirv-val",
        help="Run SPIR-V Tools validation, optionally with an explicit executable",
    )
    parser.add_argument(
        "--require-ray-query",
        action="store_true",
        help="Require a ray-query extension declaration in the shader",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    shader = args.input.expanduser().resolve()
    if not shader.is_file():
        print(f"error: shader does not exist: {shader}", file=sys.stderr)
        return 2
    if shader.suffix.lower() not in {".glsl", ".comp"}:
        print(f"error: expected a .glsl or .comp shader, got: {shader}", file=sys.stderr)
        return 2

    source = shader.read_text(encoding="utf-8")
    if args.require_ray_query and "#extension GL_EXT_ray_query : require" not in source:
        print(
            "error: --require-ray-query requires '#extension GL_EXT_ray_query : require'",
            file=sys.stderr,
        )
        return 2

    validator = shutil.which(args.validator) or (
        str(Path(args.validator).expanduser().resolve()) if Path(args.validator).is_file() else None
    )
    if not validator:
        print(
            f"error: could not find {args.validator!r}; install the Vulkan SDK or pass --validator",
            file=sys.stderr,
        )
        return 127

    output = args.output.expanduser().resolve() if args.output else shader.parent / "bin" / f"{shader.stem}.spv"
    output.parent.mkdir(parents=True, exist_ok=True)
    command = [validator, "-V", "--target-env", args.target_env, str(shader), "-o", str(output)]
    try:
        completed = subprocess.run(command, check=False, text=True, capture_output=True)
    except OSError as exc:
        print(f"error: failed to execute {validator}: {exc}", file=sys.stderr)
        return 126

    if completed.stdout:
        print(completed.stdout, end="")
    if completed.stderr:
        print(completed.stderr, end="", file=sys.stderr)
    if completed.returncode:
        print(f"error: glslangValidator exited with status {completed.returncode}", file=sys.stderr)
        return completed.returncode
    if not output.is_file():
        print(f"error: compiler reported success but did not create {output}", file=sys.stderr)
        return 1
    if args.spirv_val:
        spirv_val = shutil.which(args.spirv_val) or (
            str(Path(args.spirv_val).expanduser().resolve())
            if Path(args.spirv_val).is_file()
            else None
        )
        if not spirv_val:
            print(
                f"error: could not find {args.spirv_val!r}; install SPIR-V Tools or pass its path",
                file=sys.stderr,
            )
            return 127
        validated = subprocess.run(
            [spirv_val, "--target-env", args.target_env, str(output)],
            check=False,
            text=True,
            capture_output=True,
        )
        if validated.stdout:
            print(validated.stdout, end="")
        if validated.stderr:
            print(validated.stderr, end="", file=sys.stderr)
        if validated.returncode:
            print(f"error: spirv-val exited with status {validated.returncode}", file=sys.stderr)
            return validated.returncode
    print(f"compiled: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
