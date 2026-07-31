#!/usr/bin/env python3
"""Compare candidate daylight arrays with Radiance reference arrays."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def error_metrics(reference: np.ndarray, candidate: np.ndarray) -> dict[str, float]:
    reference = np.asarray(reference, dtype=np.float64)
    candidate = np.asarray(candidate, dtype=np.float64)
    if reference.shape != candidate.shape:
        raise ValueError(
            f"shape mismatch: reference {reference.shape}, candidate {candidate.shape}"
        )
    if reference.size == 0 or not np.isfinite(reference).all() or not np.isfinite(candidate).all():
        raise ValueError("arrays must be non-empty and finite")
    mean_reference = float(reference.mean())
    if abs(mean_reference) <= np.finfo(np.float64).eps:
        raise ValueError("reference mean must be non-zero for normalized metrics")
    error = candidate - reference
    nmbe = 100.0 * float(error.mean()) / mean_reference
    cv_rmse = 100.0 * float(np.sqrt(np.mean(error * error))) / abs(mean_reference)
    maximum_absolute_error = float(np.max(np.abs(error)))
    return {
        "nmbe_percent": nmbe,
        "absolute_nmbe_percent": abs(nmbe),
        "cv_rmse_percent": cv_rmse,
        "maximum_absolute_error": maximum_absolute_error,
    }


def load_array(path: Path) -> np.ndarray:
    if path.suffix.lower() == ".npy":
        return np.load(path)
    return np.loadtxt(path, delimiter=",")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--nmbe-limit", type=float, default=5.0)
    parser.add_argument("--cv-rmse-limit", type=float, default=10.0)
    arguments = parser.parse_args()

    metrics = error_metrics(
        load_array(arguments.reference),
        load_array(arguments.candidate),
    )
    metrics["passes"] = (
        metrics["absolute_nmbe_percent"] < arguments.nmbe_limit
        and metrics["cv_rmse_percent"] < arguments.cv_rmse_limit
    )
    arguments.out.parent.mkdir(parents=True, exist_ok=True)
    arguments.out.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metrics, indent=2))
    return 0 if metrics["passes"] else 2


if __name__ == "__main__":
    raise SystemExit(main())

