"""Manifest loading and already grid-grouped result conversion."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

import numpy as np

from foton.honeybee.protocol import PROTOCOL_NAME, PROTOCOL_VERSION
from foton_bridge import resolve_manifest


@dataclass(frozen=True)
class GridResultBranches:
    """Annual metrics grouped by sensor grid, ready to become Grasshopper branches.

    Each tuple has one entry per grid, in the order the grids appear in the
    model. DA, cDA and UDI hold one value per sensor, in percent; ``sda`` holds
    one value per grid.
    """

    identifiers: tuple[str, ...]
    room_identifiers: tuple[str, ...]
    da: tuple[list[float], ...]
    cda: tuple[list[float], ...]
    udi_lower: tuple[list[float], ...]
    udi: tuple[list[float], ...]
    udi_upper: tuple[list[float], ...]
    sda: tuple[float, ...]


def load_manifest(path) -> dict[str, Any]:
    """Read a ``run_manifest.json`` (or the folder that holds it).

    Checks that it is a complete Foton manifest of the supported protocol
    version, and turns its relative paths into absolute ones.
    """
    manifest_path = Path(path).expanduser().resolve()
    if manifest_path.is_dir():
        manifest_path = manifest_path / "run_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("protocol") != PROTOCOL_NAME:
        raise ValueError("result manifest is not a Foton Honeybee manifest")
    if manifest.get("protocol_version") != PROTOCOL_VERSION:
        raise ValueError(
            f"unsupported manifest protocol {manifest.get('protocol_version')!r}"
        )
    if manifest.get("status") != "complete":
        raise ValueError("Foton result manifest is not complete")
    if not isinstance(manifest.get("grids"), list):
        raise ValueError("Foton result manifest has no grid list")
    return resolve_manifest(manifest, str(manifest_path))


def _metric(grid, name):
    path = Path(grid["metrics"][name]).expanduser().resolve()
    values = np.atleast_1d(np.loadtxt(path, dtype=np.float64))
    count = int(grid["sensor_count"])
    if values.shape != (count,):
        raise ValueError(
            f"grid {grid['identifier']!r} metric {name!r} has shape "
            f"{values.shape}; expected {(count,)}"
        )
    if not np.isfinite(values).all():
        raise ValueError(
            f"grid {grid['identifier']!r} metric {name!r} is non-finite"
        )
    return values.tolist()


def load_grid_result_branches(manifest_or_path) -> GridResultBranches:
    """Load every grid's metric files named in a manifest and group them for Grasshopper."""
    manifest = (
        load_manifest(manifest_or_path)
        if isinstance(manifest_or_path, (str, Path))
        else manifest_or_path
    )
    grids = manifest["grids"]
    return GridResultBranches(
        identifiers=tuple(grid["identifier"] for grid in grids),
        room_identifiers=tuple(grid["room_identifier"] for grid in grids),
        da=tuple(_metric(grid, "da") for grid in grids),
        cda=tuple(_metric(grid, "cda") for grid in grids),
        udi_lower=tuple(_metric(grid, "udi_lower") for grid in grids),
        udi=tuple(_metric(grid, "udi") for grid in grids),
        udi_upper=tuple(_metric(grid, "udi_upper") for grid in grids),
        sda=tuple(float(grid["sda"]) for grid in grids),
    )
