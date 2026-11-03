#!/usr/bin/env python3
"""Archive immutable inputs and source inventory for a diagnostic campaign."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--wheel", type=Path, required=True)
    parser.add_argument(
        "--models-dir", type=Path, default=ROOT / "test_models/architectural"
    )
    parser.add_argument("--weather", type=Path, default=ROOT / "epw/gothenburg.epw")
    args = parser.parse_args()
    if args.output.resolve().is_relative_to(ROOT):
        parser.error("Campaign archives must be outside the source checkout")
    args.output.mkdir(parents=True, exist_ok=False)
    shutil.copytree(args.models_dir, args.output / "models")
    shutil.copy2(args.weather, args.output / args.weather.name)
    shutil.copy2(args.wheel, args.output / args.wheel.name)
    inventory = {}
    names = (
        subprocess.check_output(
            ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT,
        )
        .decode()
        .split("\0")
    )
    for name in sorted(set(names) - {""}):
        source = ROOT / name
        if not source.is_file():
            continue
        target = args.output / "source" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        inventory[name] = hashlib.sha256(source.read_bytes()).hexdigest()
    report = {
        "commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "dirty_status": subprocess.check_output(
            ["git", "status", "--porcelain"], cwd=ROOT, text=True
        ),
        "source_sha256": inventory,
        "input_sha256": {
            str(path.relative_to(args.output)): hashlib.sha256(
                path.read_bytes()
            ).hexdigest()
            for path in args.output.rglob("*")
            if path.is_file() and "source" not in path.relative_to(args.output).parts
        },
        "dependencies": subprocess.check_output(
            [sys.executable, "-m", "pip", "freeze"], text=True
        ).splitlines(),
    }
    (args.output / "snapshot.json").write_text(
        json.dumps(report, sort_keys=True, indent=2) + "\n"
    )
    (args.output / "working-tree.patch").write_bytes(
        subprocess.check_output(["git", "diff", "--binary", "HEAD"], cwd=ROOT)
    )
    print("Frozen campaign inputs: " + str(args.output))


if __name__ == "__main__":
    main()
