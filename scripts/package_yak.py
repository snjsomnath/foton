#!/usr/bin/env python3
"""Build the Rhino Package Manager (Yak) package from the verified Grasshopper build.

The package holds the four Foton user objects, the two example definitions with
their model and weather file, and the licence. It reuses the Rhino-built components
that ``package_grasshopper.py`` checks; nothing is rebuilt here.
"""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

YAK_MAC = "/Applications/Rhino 8.app/Contents/Resources/bin/yak"
YAK_WINDOWS = r"C:\Program Files\Rhino 8\System\Yak.exe"
USER_OBJECTS = (
    "Foton Settings.ghuser",
    "Foton Annual Daylight.ghuser",
    "Foton Annual Results.ghuser",
    "Foton Daylight Factor.ghuser",
)
STAGED = (
    "manifest.yml",
    "icon.png",
    *USER_OBJECTS,
    "Foton First Analysis.gh",
    "Foton Interactive Demo.gh",
    "examples/shoebox.hbjson",
    "examples/gothenburg.epw",
    "LICENSE",
    "NOTICE",
)


def project_version(root=ROOT):
    text = (root / "pyproject.toml").read_text()
    for line in text.splitlines():
        if line.startswith("version = "):
            return line.split("=", 1)[1].strip().strip('"')
    raise ValueError("pyproject.toml has no version")


def manifest_version(root=ROOT):
    for line in (root / "grasshopper_foton/yak/manifest.yml").read_text().splitlines():
        if line.startswith("version:"):
            return line.split(":", 1)[1].strip()
    raise ValueError("manifest.yml has no version")


def find_yak():
    for candidate in (os.environ.get("YAK"), YAK_MAC, YAK_WINDOWS, shutil.which("yak")):
        if candidate and Path(candidate).is_file():
            return candidate
    raise FileNotFoundError("Yak not found: install Rhino 8 or set YAK to the yak executable")


def stage(folder, root=ROOT):
    """Copy the package contents into ``folder`` and return their relative paths."""
    from scripts.package_grasshopper import verify_build

    verify_build(root)
    if manifest_version(root) != project_version(root):
        raise ValueError("grasshopper_foton/yak/manifest.yml version differs from pyproject.toml")
    if folder.exists():
        shutil.rmtree(folder)
    (folder / "examples").mkdir(parents=True)
    distribution = root / "grasshopper_foton/distribution"
    shutil.copy2(root / "grasshopper_foton/yak/manifest.yml", folder / "manifest.yml")
    shutil.copy2(root / "grasshopper_foton/yak/icon.png", folder / "icon.png")
    for name in (*USER_OBJECTS, "Foton First Analysis.gh", "Foton Interactive Demo.gh"):
        shutil.copy2(distribution / name, folder / name)
    from validation.scenes import make_scene

    model = make_scene("overhang_fins", root)
    (folder / "examples/shoebox.hbjson").write_text(json.dumps(model.to_dict(), indent=2))
    shutil.copy2(root / "epw/gothenburg.epw", folder / "examples/gothenburg.epw")
    shutil.copy2(root / "LICENSE", folder / "LICENSE")
    shutil.copy2(root / "NOTICE", folder / "NOTICE")
    return sorted(p.relative_to(folder).as_posix() for p in folder.rglob("*") if p.is_file())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    version = project_version()
    folder = args.output / "yak"
    staged = stage(folder)
    if staged != sorted(STAGED):
        raise ValueError("unexpected package contents: " + ", ".join(staged))
    subprocess.run([find_yak(), "build", "--platform", "any"], cwd=folder, check=True)
    # Without a .gha or .rhp, Yak tags the package for any Rhino version: "any-any".
    built = list(folder.glob("foton-" + version + "-*.yak"))
    if len(built) != 1:
        raise FileNotFoundError("yak build did not write foton-" + version + "-*.yak")
    built = built[0]
    destination = args.output / built.name
    shutil.move(str(built), destination)
    print(destination)


if __name__ == "__main__":
    main()
