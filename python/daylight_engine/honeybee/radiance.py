"""Native Radiance direct-visibility execution for Honeybee comparisons."""

from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path
import shutil
import subprocess
import time

import numpy as np


@dataclass(frozen=True)
class RadianceRun:
    visibility: np.ndarray
    commands: list[list[str]]
    versions: dict[str, str]
    elapsed_ms: float
    files: dict[str, str]


def resolve_radiance_executables(radiance_bin=None):
    searched: list[str] = []
    candidate_directories: list[Path] = []
    if radiance_bin:
        candidate_directories.append(Path(radiance_bin).expanduser())
    if os.environ.get("RADIANCE_BIN"):
        candidate_directories.append(Path(os.environ["RADIANCE_BIN"]).expanduser())
    try:
        from honeybee_radiance.config import folders

        if folders.radbin_path:
            candidate_directories.append(Path(folders.radbin_path).expanduser())
    except ImportError:
        pass
    candidate_directories.extend(
        sorted(Path("/Applications").glob("OpenStudio-*/Radiance/bin"), reverse=True)
    )

    for directory in candidate_directories:
        searched.append(str(directory))
        if not directory.is_dir():
            continue
        found = {
            name: directory / name for name in ("oconv", "rcontrib")
        }
        if all(path.is_file() and os.access(path, os.X_OK) for path in found.values()):
            return {name: str(path.resolve()) for name, path in found.items()}

    found = {name: shutil.which(name) for name in ("oconv", "rcontrib")}
    if all(found.values()):
        return found
    missing = [name for name, path in found.items() if path is None]
    search_detail = ", ".join(searched) if searched else "no configured directories"
    raise FileNotFoundError(
        "missing Radiance executable(s) "
        f"{', '.join(missing)}; checked {search_detail} and PATH. "
        "Set the recipe 'radiance_bin' input or RADIANCE_BIN."
    )


def run_radiance_visibility(
    model,
    sensor_positions,
    sensor_normals,
    patch_directions,
    patch_weights,
    *,
    work_directory,
    workers=None,
    radiance_bin=None,
) -> RadianceRun:
    executables = resolve_radiance_executables(radiance_bin)
    subprocess_environment = _radiance_subprocess_environment(executables)
    work_directory = Path(work_directory)
    work_directory.mkdir(parents=True, exist_ok=True)
    scene_path = work_directory / "scene.rad"
    octree_path = work_directory / "scene.oct"
    modifiers_path = work_directory / "modifiers.txt"
    rays_path = work_directory / "patch_center_rays.pts"
    _write_honeybee_radiance_scene(model, scene_path)
    modifiers_path.write_text("__de_sky\n__de_ground\n", encoding="utf-8")

    origins = np.asarray(sensor_positions, dtype=np.float64)
    normals = np.asarray(sensor_normals, dtype=np.float64)
    directions = np.asarray(patch_directions, dtype=np.float64)
    ray_origins = origins[:, None, :] + normals[:, None, :] * 1.0e-4
    ray_origins = np.broadcast_to(
        ray_origins, (origins.shape[0], directions.shape[0], 3)
    )
    ray_directions = np.broadcast_to(
        directions[None, :, :], (origins.shape[0], directions.shape[0], 3)
    )
    rays = np.concatenate((ray_origins, ray_directions), axis=2).reshape(-1, 6)
    ray_text = "\n".join(" ".join(f"{value:.9g}" for value in ray) for ray in rays)
    rays_path.write_text(ray_text + "\n", encoding="ascii")

    commands: list[list[str]] = []
    started = time.perf_counter()
    oconv_command = [executables["oconv"], str(scene_path)]
    commands.append(oconv_command)
    with octree_path.open("wb") as octree:
        completed = subprocess.run(
            oconv_command,
            stdout=octree,
            stderr=subprocess.PIPE,
            env=subprocess_environment,
            check=False,
        )
    if completed.returncode != 0:
        raise RuntimeError(
            "oconv failed with exit code "
            f"{completed.returncode}: {completed.stderr.decode(errors='replace').strip()}"
        )

    rcontrib_command = [
        executables["rcontrib"],
        "-h",
        "-w",
        "-ab",
        "0",
        "-M",
        str(modifiers_path),
    ]
    if workers:
        rcontrib_command.extend(["-n", str(workers)])
    rcontrib_command.append(str(octree_path))
    commands.append(rcontrib_command)
    completed = subprocess.run(
        rcontrib_command,
        input=ray_text + "\n",
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=subprocess_environment,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            "rcontrib failed with exit code "
            f"{completed.returncode}: {completed.stderr.strip()}"
        )
    visibility = _parse_rcontrib_visibility(completed.stdout, rays.shape[0])
    visibility = visibility.reshape(origins.shape[0], directions.shape[0])
    visibility = np.where(np.asarray(patch_weights) > 1.0e-8, visibility, 0.0)
    elapsed_ms = (time.perf_counter() - started) * 1_000.0
    versions = {
        name: _executable_version(path) for name, path in executables.items()
    }
    return RadianceRun(
        visibility=np.ascontiguousarray(visibility, dtype=np.float32),
        commands=commands,
        versions=versions,
        elapsed_ms=elapsed_ms,
        files={
            "scene": str(scene_path),
            "octree": str(octree_path),
            "modifiers": str(modifiers_path),
            "rays": str(rays_path),
        },
    )


def _write_honeybee_radiance_scene(model, path):
    try:
        from honeybee_radiance.lib.modifiers import black
        from honeybee_radiance.writer import (
            face_to_rad,
            shade_mesh_to_rad,
            shade_to_rad,
        )
    except ImportError as error:
        raise ImportError(
            "Radiance comparison requires honeybee-radiance; install "
            "'foton-daylight[honeybee]'"
        ) from error

    chunks = [
        "# Honeybee direct-visibility scene",
        black.to_radiance(),
    ]
    face_shades = set()
    for face in model.faces:
        chunks.append(face_to_rad(face, blk=True, exclude_sub_faces=True))
        face_shades.update(shade.identifier for shade in face.shades)
    for shade in model.shades:
        if shade.identifier not in face_shades:
            chunks.append(shade_to_rad(shade, blk=True))
    for shade_mesh in model.shade_meshes:
        chunks.append(shade_mesh_to_rad(shade_mesh, blk=True))
    chunks.append(
        """
void glow __de_sky
0
0
4 1 1 1 0

__de_sky source __de_sky_source
0
0
4 0 0 1 180

void glow __de_ground
0
0
4 1 1 1 0

__de_ground source __de_ground_source
0
0
4 0 0 -1 180
""".strip()
    )
    Path(path).write_text("\n\n".join(chunks) + "\n", encoding="utf-8")


def _parse_rcontrib_visibility(output, ray_count):
    try:
        values = np.fromstring(output, dtype=np.float64, sep=" ")
    except ValueError as error:
        raise ValueError("rcontrib output contains non-numeric values") from error
    if values.size == ray_count * 6:
        rgb = values.reshape(ray_count, 2, 3).sum(axis=1)
    elif values.size == ray_count * 3:
        rgb = values.reshape(ray_count, 3)
    else:
        raise ValueError(
            "rcontrib output has inconsistent dimensions: expected "
            f"{ray_count * 3} or {ray_count * 6} values, got {values.size}"
        )
    if not np.isfinite(rgb).all():
        raise ValueError("rcontrib output contains non-finite values")
    if np.max(np.ptp(rgb, axis=1), initial=0.0) > 1.0e-4:
        raise ValueError("rcontrib direct visibility output is not achromatic")
    scalar = rgb.mean(axis=1)
    if np.any((scalar < -1.0e-4) | (scalar > 1.0001)):
        raise ValueError("rcontrib direct visibility values fall outside [0, 1]")
    if np.any(np.minimum(np.abs(scalar), np.abs(scalar - 1.0)) > 1.0e-3):
        raise ValueError("rcontrib direct visibility output is not near-binary")
    return (scalar >= 0.5).astype(np.float32)


def _radiance_subprocess_environment(executables):
    environment = os.environ.copy()
    library_directories: list[Path] = []
    if environment.get("RADIANCE_LIB"):
        library_directories.append(Path(environment["RADIANCE_LIB"]).expanduser())
    try:
        from honeybee_radiance.config import folders

        if folders.radlib_path:
            library_directories.append(Path(folders.radlib_path).expanduser())
    except ImportError:
        pass

    for executable in executables.values():
        library_directories.append(Path(executable).resolve().parent.parent / "lib")

    ray_paths = [
        path
        for path in environment.get("RAYPATH", ".").split(os.pathsep)
        if path
    ]
    for directory in library_directories:
        if (directory / "rayinit.cal").is_file():
            resolved = str(directory.resolve())
            if resolved not in ray_paths:
                ray_paths.insert(0, resolved)
    environment["RAYPATH"] = os.pathsep.join(ray_paths)
    return environment


def _executable_version(path):
    completed = subprocess.run(
        [path, "-version"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    output = (completed.stdout or completed.stderr).strip()
    return output.splitlines()[0] if output else "unknown"
