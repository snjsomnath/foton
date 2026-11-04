#!/usr/bin/env python3
"""Package Rhino-built, source-matched components; refuse stale/missing binaries."""

import argparse
import hashlib
import json
from pathlib import Path
import sys
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def verify_build(root=ROOT):
    folder = root / "grasshopper_foton/distribution"
    manifest = json.loads((folder / "build_manifest.json").read_text())
    if manifest.get("round_trip_passed") is not True:
        raise ValueError("Grasshopper archive round-trip has not passed")
    required = {
        "Foton Settings.ghuser",
        "Foton Annual Daylight.ghuser",
        "Foton Annual Results.ghuser",
        "Foton Daylight Factor.ghuser",
        "Foton First Analysis.gh",
        "Foton First Analysis.ghx",
    }
    if set(manifest.get("artifacts", {})) != required:
        raise ValueError("Grasshopper build is incomplete")
    required_sources = {
        "scripts/build_grasshopper.py",
        "python/foton_bridge/__init__.py",
        "grasshopper_foton/foton_gh.py",
        *(
            folder_name + name + suffix
            for name in (
                "Foton Settings",
                "Foton Annual Daylight",
                "Foton Annual Results",
                "Foton Daylight Factor",
            )
            for folder_name, suffix in (
                ("grasshopper_foton/components/", ".py"),
                ("grasshopper_foton/icons/", ".png"),
            )
        ),
    }
    if set(manifest.get("sources", {})) != required_sources:
        raise ValueError("Grasshopper source provenance is incomplete")
    for prefix, values in (
        (root, manifest["sources"]),
        (folder, manifest["artifacts"]),
    ):
        for path, expected in values.items():
            if hashlib.sha256((prefix / path).read_bytes()).hexdigest() != expected:
                raise ValueError("Rebuild Grasshopper components: changed " + path)
    return manifest


def main():
    import tomllib  # Release tooling runs on Python 3.13; verify_build supports 3.10.

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    manifest = verify_build()
    version = tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]["version"]
    args.output.mkdir(parents=True, exist_ok=True)
    destination = args.output / ("foton-grasshopper-" + version + ".zip")
    from validation.scenes import make_scene

    model = make_scene("overhang_fins", ROOT)
    with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
        for name in manifest["artifacts"]:
            archive.write(ROOT / "grasshopper_foton/distribution" / name, name)
        archive.write(
            ROOT / "grasshopper_foton/distribution/build_manifest.json",
            "build_manifest.json",
        )
        archive.write(ROOT / "docs/grasshopper-quickstart.md", "START_HERE.md")
        archive.write(ROOT / "LICENSE", "LICENSE")
        archive.write(ROOT / "NOTICE", "NOTICE")
        archive.write(ROOT / "epw/gothenburg.epw", "examples/gothenburg.epw")
        archive.writestr(
            "examples/shoebox.hbjson", json.dumps(model.to_dict(), indent=2)
        )
        for package in (ROOT / "grasshopper_foton", ROOT / "python/foton_bridge"):
            for source in package.glob("*.py"):
                archive.write(source, package.name + "/" + source.name)
    print(destination)


if __name__ == "__main__":
    main()
