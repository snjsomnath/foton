#!/usr/bin/env python3
"""Generate a Radiance-compatible Perez sky matrix from an EPW file."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np


BASES = {
    "tregenza": {"multiplier": 1, "rows": 146},
    "reinhart-mf2": {"multiplier": 2, "rows": 578},
}


def radiance_environment(executable: str) -> dict[str, str]:
    environment = os.environ.copy()
    candidates = []
    if environment.get("RADIANCE_LIB"):
        candidates.append(Path(environment["RADIANCE_LIB"]).expanduser())
    executable_path = Path(executable).expanduser().resolve()
    candidates.append(executable_path.parent.parent / "lib")
    ray_paths = [
        value
        for value in environment.get("RAYPATH", ".").split(os.pathsep)
        if value
    ]
    for directory in candidates:
        if (directory / "rayinit.cal").is_file():
            resolved = str(directory.resolve())
            if resolved not in ray_paths:
                ray_paths.insert(0, resolved)
    environment["RAYPATH"] = os.pathsep.join(ray_paths)
    return environment


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--epw", required=True, type=Path)
    parser.add_argument("--basis", choices=sorted(BASES), default="tregenza")
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--metadata-out", required=True, type=Path)
    parser.add_argument("--gendaymtx", default="gendaymtx")
    parser.add_argument("--output-type", choices=("visible", "solar"), default="visible")
    parser.add_argument("--north-rotation", type=float, default=0.0)
    return parser.parse_args()


def parse_matrix(text: str) -> tuple[np.ndarray, dict[str, int]]:
    header: dict[str, int] = {}
    samples: list[list[float]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            key, value = line.split("=", 1)
            if key in {"NROWS", "NCOLS", "NCOMP"}:
                header[key] = int(value)
            continue
        fields = line.split()
        if len(fields) != 3:
            continue
        try:
            samples.append([float(value) for value in fields])
        except ValueError as exc:
            raise RuntimeError(f"invalid gendaymtx data row: {line}") from exc
    if set(header) != {"NROWS", "NCOLS", "NCOMP"}:
        raise RuntimeError("gendaymtx output is missing NROWS, NCOLS, or NCOMP")
    if header["NCOMP"] != 3:
        raise RuntimeError(f"expected 3 RGB components, got {header['NCOMP']}")
    expected = header["NROWS"] * header["NCOLS"]
    if len(samples) != expected:
        raise RuntimeError(f"gendaymtx returned {len(samples)} RGB rows; expected {expected}")
    matrix = np.asarray(samples, dtype=np.float32).reshape(
        header["NROWS"], header["NCOLS"], header["NCOMP"]
    )
    return matrix, header


def generate(
    epw_path: Path,
    basis: str,
    gendaymtx: str,
    output_type: str,
    north_rotation: float,
) -> tuple[np.ndarray, dict[str, object]]:
    try:
        from ladybug.epw import EPW
    except ImportError as exc:
        raise RuntimeError("ladybug-core is required; install requirements.txt") from exc

    epw = EPW(str(epw_path))
    direct_count = len(epw.direct_normal_radiation.values)
    diffuse_count = len(epw.diffuse_horizontal_radiation.values)
    if direct_count != diffuse_count:
        raise RuntimeError("EPW weather collections have inconsistent lengths")

    executable = shutil.which(gendaymtx) or (
        str(Path(gendaymtx).expanduser().resolve()) if Path(gendaymtx).is_file() else None
    )
    if not executable:
        raise RuntimeError(f"could not find {gendaymtx!r}; install Radiance or pass --gendaymtx")
    basis_config = BASES[basis]
    output_flag = "-O0" if output_type == "visible" else "-O1"
    command = [
        executable,
        "-m",
        str(basis_config["multiplier"]),
        output_flag,
        "-r",
        str(north_rotation),
        str(epw_path),
    ]
    completed = subprocess.run(
        command,
        text=True,
        capture_output=True,
        env=radiance_environment(executable),
        check=False,
    )
    if completed.returncode:
        detail = completed.stderr.strip() or "no stderr output"
        raise RuntimeError(f"gendaymtx exited with status {completed.returncode}: {detail}")
    matrix, header = parse_matrix(completed.stdout)
    if header["NROWS"] != basis_config["rows"]:
        raise RuntimeError(
            f"{basis} must produce {basis_config['rows']} rows, got {header['NROWS']}"
        )
    if header["NCOLS"] != direct_count:
        raise RuntimeError(
            f"gendaymtx produced {header['NCOLS']} timesteps; EPW contains {direct_count}"
        )

    location = epw.location
    metadata = {
        "format": "vulkan-daylight-sky-matrix-v1",
        "source_epw": str(epw_path),
        "basis": basis,
        "reinhart_multiplier": basis_config["multiplier"],
        "patch_order": "radiance-gendaymtx-ground-first",
        "ground_patch_index": 0,
        "row_count": int(matrix.shape[0]),
        "timestep_count": int(matrix.shape[1]),
        "shape": [int(value) for value in matrix.shape],
        "components": ["red", "green", "blue"],
        "output_type": output_type,
        "units": "W/sr/m2",
        "north_rotation_degrees": north_rotation,
        "location": {
            "city": getattr(location, "city", None),
            "latitude": getattr(location, "latitude", None),
            "longitude": getattr(location, "longitude", None),
            "time_zone": getattr(location, "time_zone", None),
        },
    }
    return matrix, metadata


def main() -> int:
    args = parse_args()
    epw_path = args.epw.expanduser().resolve()
    if not epw_path.is_file():
        print(f"error: EPW file does not exist: {epw_path}", file=sys.stderr)
        return 2
    try:
        matrix, metadata = generate(
            epw_path,
            args.basis,
            args.gendaymtx,
            args.output_type,
            args.north_rotation,
        )
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    output = args.out.expanduser().resolve()
    metadata_output = args.metadata_out.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    metadata_output.parent.mkdir(parents=True, exist_ok=True)
    np.save(output, matrix)
    metadata_output.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(f"generated matrix with shape {matrix.shape}")
    print(f"matrix: {output}")
    print(f"metadata: {metadata_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
