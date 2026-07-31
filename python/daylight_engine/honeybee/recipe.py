"""Ladybug Tools-style recipe facade for Honeybee direct visibility."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re
import shutil
import warnings

import numpy as np

from .adapter import prepare_honeybee_scene
from .radiance import (
    _executable_version,
    resolve_radiance_executables,
    run_radiance_visibility,
)
from .settings import RecipeSettings

_INPUT_NAMES = (
    "model",
    "backend",
    "engine_backend",
    "grid_filter",
    "grid_size",
    "sensor_height",
    "sky_basis",
    "radiance_bin",
)
_OUTPUT_NAMES = (
    "results",
    "comparison_report",
    "metal_visibility",
    "radiance_visibility",
)


class Recipe:
    """Execute a Foton recipe with the familiar LBT method surface."""

    def __init__(self, recipe_name):
        normalized = _normalize_name(recipe_name)
        if normalized != "direct_visibility":
            raise ValueError(
                f"unsupported recipe {recipe_name!r}; expected 'direct_visibility'"
            )
        self._name = normalized
        self._inputs = {
            "model": None,
            "backend": "compare",
            "engine_backend": "auto",
            "grid_filter": "*",
            "grid_size": 0.5,
            "sensor_height": 0.75,
            "sky_basis": "tregenza",
            "radiance_bin": None,
        }
        self._project_folder: Path | None = None
        self._simulation_id: str | None = None

    @property
    def name(self):
        return self._name

    @property
    def tag(self):
        return "foton"

    @property
    def path(self):
        return str(Path(__file__).resolve().parent)

    @property
    def default_project_folder(self):
        return str(Path.cwd() / "foton")

    @property
    def simulation_id(self):
        return self._simulation_id

    @property
    def inputs(self):
        return dict(self._inputs)

    @property
    def outputs(self):
        return list(_OUTPUT_NAMES)

    @property
    def input_names(self):
        return list(_INPUT_NAMES)

    @property
    def output_names(self):
        return list(_OUTPUT_NAMES)

    def input_value_by_name(self, input_name, input_value):
        name = _normalize_name(input_name)
        if name not in self._inputs:
            raise ValueError(
                f"unknown input {input_name!r}; expected {', '.join(_INPUT_NAMES)}"
            )
        if name == "backend" and input_value not in {
            "auto",
            "metal",
            "vulkan",
            "radiance",
            "compare",
        }:
            raise ValueError(
                "backend must be 'auto', 'metal', 'vulkan', 'radiance', or 'compare'"
            )
        if name == "engine_backend" and input_value not in {
            "auto",
            "metal",
            "vulkan",
        }:
            raise ValueError("engine_backend must be 'auto', 'metal', or 'vulkan'")
        if name == "sky_basis":
            input_value = _normalize_sky_basis(input_value)
        if name in {"grid_size", "sensor_height"}:
            input_value = float(input_value)
            if not np.isfinite(input_value) or input_value <= 0:
                raise ValueError(f"{name} must be finite and positive")
        self._inputs[name] = input_value

    def output_value_by_name(self, output_name, project_folder=None):
        name = _normalize_name(output_name)
        if name not in _OUTPUT_NAMES:
            raise ValueError(
                f"unknown output {output_name!r}; expected {', '.join(_OUTPUT_NAMES)}"
            )
        project = (
            Path(project_folder)
            if project_folder is not None
            else self._project_folder
        )
        if project is None:
            raise RuntimeError("run the recipe before requesting outputs")
        paths = _output_paths(project)
        path = paths[name]
        if name != "results" and not path.is_file():
            raise FileNotFoundError(
                f"output {name!r} was not generated for this backend: {path}"
            )
        return str(path)

    def run(
        self,
        settings=None,
        radiance_check=False,
        openstudio_check=False,
        energyplus_check=False,
        queenbee_path=None,
        silent=False,
        debug_folder=None,
    ):
        if openstudio_check or energyplus_check:
            raise ValueError(
                "direct_visibility does not use OpenStudio or EnergyPlus"
            )
        if queenbee_path is not None:
            warnings.warn(
                "queenbee_path is accepted for LBT compatibility but is not used",
                UserWarning,
                stacklevel=2,
            )
        settings = settings or RecipeSettings()
        if not isinstance(settings, RecipeSettings):
            raise TypeError("settings must be a RecipeSettings instance")
        if self._inputs["model"] is None:
            raise ValueError("the required 'model' input has not been set")

        prepared = prepare_honeybee_scene(
            self._inputs["model"],
            grid_filter=self._inputs["grid_filter"],
            grid_size=self._inputs["grid_size"],
            sensor_height=self._inputs["sensor_height"],
        )
        backend = self._inputs["backend"]
        needs_radiance = backend in {"radiance", "compare"} or radiance_check
        radiance_environment = None
        if needs_radiance:
            executables = resolve_radiance_executables(self._inputs["radiance_bin"])
            radiance_environment = {
                name: {
                    "path": path,
                    "version": _executable_version(path),
                }
                for name, path in executables.items()
            }

        root = Path(settings.folder or self.default_project_folder).expanduser()
        project_name = (
            f"{_safe_identifier(prepared.model.identifier)}-direct-visibility"
        )
        project = root.resolve() / project_name
        results = project / "results"
        results.mkdir(parents=True, exist_ok=True)
        self._project_folder = project
        self._simulation_id = project_name

        from foton import __version__

        run_fingerprint = _run_fingerprint(
            prepared.model_fingerprint,
            self._inputs,
            radiance_environment,
            __version__,
        )
        paths = _output_paths(project)
        if settings.reload_old and _cache_is_valid(
            paths, run_fingerprint, backend
        ):
            _report(settings, silent, f"Reused {project}")
            return str(project)

        for path in (
            paths["metal_visibility"],
            paths["radiance_visibility"],
            paths["comparison_report"],
            results / "comparison.json",
            results / "metadata.json",
        ):
            path.unlink(missing_ok=True)

        basis = _normalize_sky_basis(self._inputs["sky_basis"])
        from foton import (
            Engine,
            sky_patch_directions,
            sky_patch_solid_angles,
        )

        directions = np.ascontiguousarray(
            sky_patch_directions(basis), dtype=np.float32
        )
        solid_angles = np.ascontiguousarray(
            sky_patch_solid_angles(basis), dtype=np.float32
        )
        sensor_positions = prepared.arrays["sensor_positions"]
        sensor_normals = prepared.arrays["sensor_normals"]
        cosines = np.maximum(sensor_normals @ directions.T, 0.0)
        patch_weights = np.ascontiguousarray(
            cosines * solid_angles[None, :], dtype=np.float32
        )

        metal_visibility = None
        radiance_visibility = None
        metal_metadata = None
        radiance_metadata = None
        if backend in {"auto", "metal", "vulkan", "compare"}:
            engine_backend = (
                self._inputs["engine_backend"] if backend == "compare" else backend
            )
            engine = Engine({"backend": engine_backend})
            scene = prepared.create_native_scene(engine)
            quality = "preview" if basis == "tregenza" else "final"
            sky = np.zeros((directions.shape[0], 1, 3), dtype=np.float32)
            occupancy = np.ones(1, dtype=np.float32)
            result = scene.analyze(
                sky,
                occupancy,
                quality=quality,
                maximum_samples=0,
                maximum_bounces=0,
                export_coefficients=True,
            ).result()
            if result.used_reference_fallback or result.transport_backend == "reference":
                raise RuntimeError(
                    "direct visibility did not execute on GPU hardware; "
                    f"transport_backend={result.transport_backend!r}, "
                    f"used_reference_fallback={result.used_reference_fallback}"
                )
            coefficients = result.coefficients()
            if coefficients is None:
                raise RuntimeError("native engine did not export direct coefficients")
            metal_visibility = _coefficients_to_visibility(
                coefficients, patch_weights
            )
            np.save(paths["metal_visibility"], metal_visibility)
            metal_metadata = {
                "capabilities": engine.capabilities(),
                "solver": json.loads(result.metadata_json()),
                "timings_ms": result.timings(),
            }

        preserve_debug = debug_folder or settings.debug_folder
        work_directory = (
            Path(debug_folder or settings.debug_folder).expanduser().resolve()
            if preserve_debug
            else project / ".work"
        )
        if backend in {"radiance", "compare"}:
            radiance_run = run_radiance_visibility(
                prepared.model,
                sensor_positions,
                sensor_normals,
                directions,
                patch_weights,
                work_directory=work_directory,
                workers=settings.workers,
                radiance_bin=self._inputs["radiance_bin"],
            )
            radiance_visibility = radiance_run.visibility
            np.save(paths["radiance_visibility"], radiance_visibility)
            radiance_metadata = {
                "commands": radiance_run.commands,
                "versions": radiance_run.versions,
                "elapsed_ms": radiance_run.elapsed_ms,
                "debug_files": radiance_run.files if preserve_debug else None,
            }
        if not preserve_debug:
            shutil.rmtree(work_directory, ignore_errors=True)

        comparison = _compare_visibility(
            metal_visibility,
            radiance_visibility,
            patch_weights,
            prepared.arrays["sensor_area_weights"],
        )
        comparison_json = results / "comparison.json"
        comparison_json.write_text(
            json.dumps(comparison, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        paths["comparison_report"].write_text(
            _comparison_markdown(comparison, backend),
            encoding="utf-8",
        )
        (results / "grid_info.json").write_text(
            json.dumps(prepared.grid_info, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        metadata = {
            "recipe": self._name,
            "recipe_schema": 1,
            "engine_version": __version__,
            "run_fingerprint": run_fingerprint,
            "model_identifier": prepared.model.identifier,
            "model_fingerprint": prepared.model_fingerprint,
            "model_units": "Meters",
            "backend": backend,
            "engine_backend": self._inputs["engine_backend"],
            "sky_basis": basis,
            "matrix_orientation": ["sensor", "sky_patch"],
            "sky_patch_count": int(directions.shape[0]),
            "sensor_count": int(sensor_positions.shape[0]),
            "room_map": prepared.room_map,
            "geometry": prepared.geometry_info,
            "aperture_semantics": "geometric_opening",
            "shade_semantics": "opaque_static",
            "metal": metal_metadata,
            "gpu": metal_metadata,
            "radiance": radiance_metadata,
        }
        (results / "metadata.json").write_text(
            json.dumps(metadata, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        _report(settings, silent, f"Completed {project}")
        return str(project)


def _coefficients_to_visibility(coefficients, patch_weights):
    coefficients = np.asarray(coefficients, dtype=np.float32)
    expected = (*patch_weights.shape, 3)
    if coefficients.shape != expected:
        raise ValueError(
            f"native coefficients have shape {coefficients.shape}; expected {expected}"
        )
    visibility_rgb = np.zeros_like(coefficients)
    valid = patch_weights > 1.0e-8
    np.divide(
        coefficients,
        patch_weights[:, :, None],
        out=visibility_rgb,
        where=valid[:, :, None],
    )
    if not np.isfinite(visibility_rgb).all():
        raise ValueError("native direct visibility contains non-finite values")
    if np.max(np.ptp(visibility_rgb, axis=2), initial=0.0) > 1.0e-4:
        raise ValueError("native direct visibility is not achromatic")
    scalar = visibility_rgb.mean(axis=2)
    near_binary = np.minimum(np.abs(scalar), np.abs(scalar - 1.0))
    if np.any(near_binary[valid] > 1.0e-3):
        raise ValueError("native direct visibility is not near-binary")
    return np.ascontiguousarray(
        np.where(valid & (scalar >= 0.5), 1.0, 0.0), dtype=np.float32
    )


def _compare_visibility(metal, radiance, patch_weights, sensor_area_weights):
    if metal is None or radiance is None:
        return {
            "status": "not_compared",
            "reason": "both hardware-engine and Radiance outputs are required",
        }
    if metal.shape != radiance.shape:
        raise ValueError(
            f"hardware-engine shape {metal.shape} does not match Radiance shape "
            f"{radiance.shape}"
        )
    difference = np.abs(metal - radiance)
    mismatch = difference > 0.01
    weighted_patch = (
        np.asarray(sensor_area_weights, dtype=np.float64)[:, None]
        * np.asarray(patch_weights, dtype=np.float64)
    )
    metal_energy = float(np.sum(metal * weighted_patch))
    radiance_energy = float(np.sum(radiance * weighted_patch))
    relative_energy_error = abs(metal_energy - radiance_energy) / max(
        abs(radiance_energy), 1.0e-12
    )
    return {
        "status": "passed"
        if not mismatch.any() and relative_energy_error < 0.01
        else "failed",
        "matrix_shape": list(metal.shape),
        "maximum_absolute_error": float(difference.max(initial=0.0)),
        "mismatch_count": int(mismatch.sum()),
        "mismatch_rate": float(mismatch.mean()),
        "per_sensor_mismatch_count": mismatch.sum(axis=1).astype(int).tolist(),
        "engine_weighted_visible_energy": metal_energy,
        "metal_weighted_visible_energy": metal_energy,
        "radiance_weighted_visible_energy": radiance_energy,
        "weighted_visible_energy_relative_error": relative_energy_error,
        "thresholds": {
            "maximum_absolute_error": 0.01,
            "mismatch_count": 0,
            "weighted_visible_energy_relative_error": 0.01,
        },
    }


def _comparison_markdown(comparison, backend):
    if comparison["status"] == "not_compared":
        return (
            "# Honeybee Direct-Visibility Comparison\n\n"
            f"- Backend mode: `{backend}`\n"
            "- Status: not compared\n"
            f"- Reason: {comparison['reason']}\n"
        )
    return (
        "# Honeybee Direct-Visibility Comparison\n\n"
        f"- Status: **{comparison['status'].upper()}**\n"
        f"- Matrix shape: `{comparison['matrix_shape']}`\n"
        f"- Maximum absolute error: "
        f"`{comparison['maximum_absolute_error']:.6g}`\n"
        f"- Mismatched rays: `{comparison['mismatch_count']}` "
        f"(`{comparison['mismatch_rate']:.4%}`)\n"
        f"- Weighted visible-energy relative error: "
        f"`{comparison['weighted_visible_energy_relative_error']:.4%}`\n"
        "\nApertures are geometric openings and all static shades are opaque.\n"
    )


def _output_paths(project):
    results = Path(project) / "results"
    return {
        "results": results,
        "comparison_report": results / "comparison.md",
        "metal_visibility": results / "metal_visibility.npy",
        "radiance_visibility": results / "radiance_visibility.npy",
    }


def _cache_is_valid(paths, fingerprint, backend):
    metadata_path = paths["results"] / "metadata.json"
    if not metadata_path.is_file():
        return False
    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    if metadata.get("run_fingerprint") != fingerprint:
        return False
    required = [
        paths["comparison_report"],
        paths["results"] / "comparison.json",
        paths["results"] / "grid_info.json",
    ]
    if backend in {"auto", "metal", "vulkan", "compare"}:
        required.append(paths["metal_visibility"])
    if backend in {"radiance", "compare"}:
        required.append(paths["radiance_visibility"])
    return all(path.is_file() for path in required)


def _run_fingerprint(
    model_fingerprint, inputs, radiance_environment, engine_version
):
    values = {
        "model_fingerprint": model_fingerprint,
        "backend": inputs["backend"],
        "engine_backend": inputs["engine_backend"],
        "grid_filter": inputs["grid_filter"],
        "grid_size": inputs["grid_size"],
        "sensor_height": inputs["sensor_height"],
        "sky_basis": _normalize_sky_basis(inputs["sky_basis"]),
        "radiance": radiance_environment,
        "engine_version": engine_version,
        "recipe_schema": 1,
    }
    return sha256(
        json.dumps(values, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _normalize_name(value):
    if not isinstance(value, str):
        raise TypeError("recipe and input names must be strings")
    return value.strip().lower().replace("-", "_").replace(" ", "_")


def _normalize_sky_basis(value):
    normalized = _normalize_name(value)
    if normalized == "tregenza":
        return "tregenza"
    if normalized in {"reinhart_mf2", "reinhartmf2"}:
        return "reinhart-mf2"
    raise ValueError("sky_basis must be 'tregenza' or 'reinhart-mf2'")


def _safe_identifier(value):
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "-", str(value)).strip("-")
    return safe or "honeybee-model"


def _report(settings, silent, message):
    if settings.report_out and not silent:
        print(message)
