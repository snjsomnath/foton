"""Dependency-free, Python 2.7 compatible contracts shared with GhPython."""
from __future__ import print_function

import copy
import hashlib
import json
import math
import os


PATH_FIELDS = ("manifest", "output_folder", "results_folder", "metrics_folder",
               "grid_summary", "metadata")


def backend_identifier(value):
    name = value.get("backend") or value.get("name", "") if isinstance(value, dict) else value or ""
    name = name.lower()
    return "metal" if "metal" in name else "vulkan" if "vulkan" in name else "reference"


def map_paths(manifest, convert):
    result = copy.deepcopy(manifest)
    for key in PATH_FIELDS:
        if result.get(key) is not None:
            result[key] = convert(result[key])
    for grid in result.get("grids", []):
        grid["metrics"] = dict((k, convert(v)) for k, v in grid.get("metrics", {}).items())
        if grid.get("raw_illuminance"):
            grid["raw_illuminance"] = convert(grid["raw_illuminance"])
    return result


def resolve_manifest(manifest, manifest_path):
    root = os.path.dirname(os.path.abspath(manifest_path))
    result = map_paths(manifest, lambda p: os.path.normpath(os.path.join(root, p)))
    result["manifest"] = os.path.abspath(manifest_path)
    return result


def portable_manifest(manifest, root):
    result = map_paths(manifest, lambda p: os.path.relpath(p, root).replace(os.sep, "/"))
    result["path_schema"] = 1
    return result


def reuse_identity(request, capabilities):
    """Return None for old/incomplete provenance; never guess compatibility."""
    provenance = capabilities.get("provenance", {})
    required = ("engine_version", "solver_revision", "selected_backend", "weather_version")
    if any(not provenance.get(key) for key in required):
        return None
    resolved = dict(request)
    for key in ("model", "wea", "schedule", "fingerprint"):
        resolved.pop(key, None)
    preset = capabilities.get("quality_settings", {}).get(request.get("quality", "final"))
    if not preset:
        return None
    for key in ("direct_samples", "maximum_samples"):
        if resolved.get(key) is None:
            resolved[key] = preset[key]
    payload = {"schema": 1, "request": resolved, "provenance": provenance}
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    payload["fingerprint"] = hashlib.sha256(encoded.encode("ascii")).hexdigest()
    return payload


def reusable(manifest, identity):
    if not identity or manifest.get("reuse_identity") != identity:
        return False
    if manifest.get("status") != "complete" or not manifest.get("grids"):
        return False
    try:
        for key in ("metadata", "grid_summary"):
            if not os.path.isfile(manifest.get(key, "")):
                return False
        for grid in manifest["grids"]:
            for metric in ("da", "cda", "udi_lower", "udi", "udi_upper"):
                with open(grid["metrics"][metric]) as stream:
                    values = [float(x) for x in stream.read().split()]
                if len(values) != grid["sensor_count"] or any(math.isnan(v) or math.isinf(v) for v in values):
                    return False
            if identity["request"].get("export_illuminance"):
                if not os.path.isfile(grid.get("raw_illuminance") or ""):
                    return False
        return True
    except (IOError, OSError, ValueError, TypeError, KeyError):
        return False
