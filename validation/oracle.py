"""Radiance references independent of Foton's native sky sampler."""

from pathlib import Path
import subprocess
import numpy as np


def patch_samples(density, count, seed=1979):
    """Stratified solid-angle samples from the published Reinhart ring definition."""
    if density not in (1, 2) or count < 1:
        raise ValueError("density must be 1/2 and count positive")
    rng = np.random.default_rng(seed)
    rings = (30, 30, 24, 24, 18, 12, 6)
    increment = np.pi / 2 / (7 * density + 0.5)
    bounds = [(-1.0, 0.0, 0.0, 2 * np.pi)]
    for ring in range(7 * density):
        number = rings[ring // density] * density
        width = 2 * np.pi / number
        bounds.extend(
            (np.sin(ring * increment), np.sin((ring + 1) * increment), i * width, width)
            for i in range(number)
        )
    bounds.append((np.sin(7 * density * increment), 1.0, 0.0, 2 * np.pi))
    directions, weights = [], []
    for low, high, center, width in bounds:
        z = low + (high - low) * (np.arange(count) + rng.random(count)) / count
        azimuth = (
            center
            + (rng.permutation(count) + rng.random(count)) / count * width
            - width / 2
        )
        radius = np.sqrt(1 - z * z)
        directions.append(
            np.column_stack((radius * np.sin(azimuth), radius * np.cos(azimuth), z))
        )
        weights.append((high - low) * width)
    return np.asarray(directions, dtype=np.float32), np.asarray(
        weights, dtype=np.float32
    )


def export_scene(model, folder, density, radiance_bin=None, open_apertures=False):
    from honeybee_radiance.writer import model_to_rad, face_to_rad
    from honeybee_radiance.lightsource.sky.skydome import SkyDome
    from foton.honeybee.radiance import (
        resolve_radiance_executables,
        _radiance_subprocess_environment,
    )

    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    geometry, materials = model_to_rad(model)
    if open_apertures:
        geometry = "\n".join(
            face_to_rad(face, exclude_sub_faces=True) for face in model.faces
        )
    scene = folder / "scene.rad"
    scene.write_text(materials + "\n" + geometry, encoding="utf-8")
    sky = folder / "sky.dome"
    sky.write_text(SkyDome(density, ground_emittance=1).to_radiance(), encoding="ascii")
    executables = resolve_radiance_executables(radiance_bin, required=("oconv",))
    command = [executables["oconv"], str(scene)]
    octree = folder / "scene.oct"
    with octree.open("wb") as output:
        completed = subprocess.run(
            command,
            stdout=output,
            stderr=subprocess.PIPE,
            env=_radiance_subprocess_environment(executables),
        )
    if completed.returncode:
        raise RuntimeError(completed.stderr.decode(errors="replace"))
    return octree, sky, command


def audit_sky_bins(directions, density, radiance_bin=None):
    """Ask Radiance's own reinhart.cal to identify our independently sampled bins."""
    import hashlib
    from foton.honeybee.radiance import (
        resolve_radiance_executables,
        _radiance_subprocess_environment,
    )

    executables = resolve_radiance_executables(radiance_bin, required=("rcalc",))
    environment = _radiance_subprocess_environment(executables)
    library = Path(executables["rcalc"]).parent.parent / "lib" / "reinhart.cal"
    if not library.is_file():
        import os

        library = next(
            (
                Path(p) / "reinhart.cal"
                for p in environment.get("RAYPATH", "").split(os.pathsep)
                if (Path(p) / "reinhart.cal").is_file()
            ),
            library,
        )
    # Bounded audit covers each patch with multiple independent samples.
    selected = np.asarray(directions)[:, :16, :]
    command = [
        executables["rcalc"],
        "-e",
        "MF:%d" % density,
        "-f",
        str(library),
        "-e",
        "Dx=$1;Dy=$2;Dz=$3;$1=rbin",
    ]
    completed = subprocess.run(
        command,
        input="\n".join("%.9g %.9g %.9g" % tuple(v) for v in selected.reshape(-1, 3))
        + "\n",
        capture_output=True,
        text=True,
        env=environment,
    )
    if completed.returncode:
        raise RuntimeError("Radiance sky-bin audit failed: " + completed.stderr)
    bins = np.fromstring(completed.stdout, sep=" ")
    expected = np.repeat(np.arange(selected.shape[0]), selected.shape[1])
    passed = bins.shape == expected.shape and np.array_equal(bins, expected)
    return {
        "passed": bool(passed),
        "ray_count": int(expected.size),
        "command": command,
        "calibration_sha256": hashlib.sha256(library.read_bytes()).hexdigest(),
    }


def difference(reference, candidate, darkness=1e-8):
    reference, candidate = (
        np.asarray(reference, dtype=float),
        np.asarray(candidate, dtype=float),
    )
    if (
        reference.shape != candidate.shape
        or not reference.size
        or not np.isfinite(reference).all()
        or not np.isfinite(candidate).all()
    ):
        return {"passed": False, "error": "invalid comparison arrays"}
    delta = candidate - reference
    absolute = np.abs(delta)
    scale = float(np.sqrt(np.mean(reference**2)))
    maximum = float(absolute.max())
    bias = 100 * float(np.mean(delta)) / max(abs(float(np.mean(reference))), 1e-20)
    rms = 100 * float(np.sqrt(np.mean(delta**2))) / max(scale, 1e-20)
    if max(float(np.abs(reference).max()), float(np.abs(candidate).max())) <= darkness:
        bias = rms = 0.0
    return {
        "bias_percent": bias,
        "rms_normalized_error_percent": rms,
        "absolute_error": {
            "p95": float(np.percentile(absolute, 95)),
            "p99": float(np.percentile(absolute, 99)),
            "maximum": maximum,
        },
        "worst_index": [
            int(x) for x in np.unravel_index(np.argmax(absolute), absolute.shape)
        ],
        "passed": abs(bias) < 1 and rms < 5,
    }


def convergence_by_grid(prepared, first, second):
    grids = []
    for grid in prepared.grid_info:
        start, count = grid["start_sensor_index"], grid["sensor_count"]
        grids.append(
            {
                "identifier": grid["identifier"],
                **difference(
                    first[start : start + count], second[start : start + count]
                ),
            }
        )
    return {"passed": all(g["passed"] for g in grids), "grids": grids}
