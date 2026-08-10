#!/usr/bin/env python3
"""Run the stock LBT annual-daylight recipe and preserve reproducibility data."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

from foton.honeybee.radiance import (
    _executable_version,
    _radiance_subprocess_environment,
    resolve_radiance_executables,
)


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True)
    parser.add_argument("--wea", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--radiance-bin")
    parser.add_argument("--north", type=float, default=0.0)
    return parser.parse_args()


def main():
    args = parse_args()
    if args.workers <= 0:
        raise ValueError("--workers must be positive")
    sibling_executable = Path(sys.prefix) / "bin" / "lbt-recipes"
    executable = (
        str(sibling_executable)
        if sibling_executable.is_file()
        else shutil.which("lbt-recipes")
    )
    if executable is None:
        raise FileNotFoundError(
            "lbt-recipes is not installed; install lbt-recipes and setuptools"
        )
    output = Path(args.output).expanduser().resolve()
    output.mkdir(parents=True, exist_ok=True)
    schedule = output / "schedule.csv"
    schedule.write_text(
        "\n".join(
            "1" if 8 <= hour % 24 < 18 else "0" for hour in range(8760)
        )
        + "\n",
        encoding="ascii",
    )
    inputs = {
        "model": str(Path(args.model).expanduser().resolve()),
        "wea": str(Path(args.wea).expanduser().resolve()),
        "schedule": str(schedule),
        "north": float(args.north),
        "grid-filter": "*",
        "radiance-parameters": "-ab 2 -ad 5000 -lw 2e-05 -dr 0",
        "thresholds": "-t 300 -lt 100 -ut 3000",
    }
    inputs_path = output / "inputs.json"
    inputs_path.write_text(
        json.dumps(inputs, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    command = [
        executable,
        "run",
        "annual-daylight",
        str(inputs_path),
        "--project-folder",
        str(output),
        "--workers",
        str(args.workers),
    ]
    environment = os.environ.copy()
    environment["PATH"] = os.pathsep.join(
        [str(Path(sys.prefix) / "bin"), environment.get("PATH", "")]
    )
    if args.radiance_bin:
        environment["RADIANCE_BIN"] = str(
            Path(args.radiance_bin).expanduser().resolve()
        )
        environment["PATH"] = os.pathsep.join(
            [environment["RADIANCE_BIN"], environment["PATH"]]
        )
    started = time.perf_counter()
    completed = subprocess.run(
        command,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env=environment,
        check=False,
    )
    elapsed = time.perf_counter() - started
    log_path = output / "annual-daylight.log"
    log_path.write_text(completed.stdout, encoding="utf-8")
    if completed.returncode:
        raise RuntimeError(
            "stock annual-daylight failed with exit code "
            f"{completed.returncode}; see {log_path}"
        )
    projects = [
        path
        for path in output.iterdir()
        if path.is_dir()
        and (path / "results" / "grids_info.json").is_file()
    ]
    if len(projects) != 1:
        raise RuntimeError(
            f"expected one completed annual-daylight project; found {projects}"
        )
    executables = resolve_radiance_executables(args.radiance_bin)
    radiance_environment = _radiance_subprocess_environment(executables)
    version = subprocess.run(
        [executable, "--version"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    ).stdout.strip()
    manifest = {
        "schema_version": 1,
        "recipe": "annual-daylight",
        "project": str(projects[0]),
        "elapsed_seconds": elapsed,
        "command": command,
        "inputs": inputs,
        "occupied_hours": 3650,
        "lbt_recipes_version": version,
        "radiance": {
            name: {
                "path": path,
                "version": _executable_version(path, radiance_environment),
            }
            for name, path in executables.items()
        },
        "log": str(log_path),
    }
    manifest_path = output / "reference_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(manifest_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
