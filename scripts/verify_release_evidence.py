#!/usr/bin/env python3
"""Reject missing, stale, partial, fallback or failing release evidence."""

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from validation.scenes import SCENE_IDS, SCENE_VERSION

RHINO_SCENARIOS = (
    "fresh_install",
    "open_example",
    "run",
    "cancel",
    "rerun",
    "change_inputs",
    "upgrade_invalidates_reuse",
    "reload_moved_results",
    "honeybee_metrics",
    "ladybug_heatmap",
)


def verify(suite, rhino, commit, backend, system, version):
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    require(suite.get("commit") == commit, "suite was not run on the release commit")
    require(
        suite.get("engine_version") == version,
        "suite wheel version differs from release",
    )
    require(suite.get("suite_version") == SCENE_VERSION, "suite version is obsolete")
    require(
        suite.get("status") == "passed" and suite.get("passed") is True,
        "numerical suite did not pass",
    )
    require(
        suite.get("dirty") is False and suite.get("smoke") is False,
        "dirty or smoke runs cannot qualify releases",
    )
    require(
        suite.get("backend") == backend
        and suite.get("hardware", {}).get("system") == system,
        "suite hardware/platform differs from required target",
    )
    scenes = suite.get("scenes", [])
    require(
        len(scenes) == len(SCENE_IDS) * 2
        and {(s.get("scene"), s.get("sky_density")) for s in scenes}
        == {(s, d) for s in SCENE_IDS for d in (1, 2)},
        "%d scenes in both sky bases are required" % len(SCENE_IDS),
    )
    require(
        all(
            s.get("passed") is True
            and s.get("gpu_executed") is True
            and s.get("oracle_stable") is True
            for s in scenes
        ),
        "missing GPU execution or unstable/failing scene",
    )
    require(
        rhino.get("commit") == commit and rhino.get("engine_version") == version,
        "Rhino evidence is not for this release",
    )
    require(
        str(rhino.get("rhino_version", "")).startswith("8."),
        "Rhino 8 evidence is required",
    )
    require(
        rhino.get("system") == system and rhino.get("backend") == backend,
        "Rhino platform/backend differs",
    )
    scenarios = rhino.get("scenarios", {})
    require(
        all(scenarios.get(name) is True for name in RHINO_SCENARIOS),
        "live Rhino acceptance checklist is incomplete",
    )
    require(
        bool(rhino.get("tested_at")) and bool(rhino.get("notes")),
        "Rhino evidence needs a date and reproduction notes",
    )
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", type=Path, required=True)
    parser.add_argument("--rhino", type=Path, required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--backend", choices=("metal", "vulkan"), required=True)
    parser.add_argument("--system", choices=("Darwin", "Windows"), required=True)
    args = parser.parse_args()
    try:
        errors = verify(
            json.loads(args.suite.read_text()),
            json.loads(args.rhino.read_text()),
            args.commit,
            args.backend,
            args.system,
            args.version,
        )
    except (OSError, ValueError, TypeError) as error:
        errors = [str(error)]
    for error in errors:
        print("Release evidence incomplete: " + error, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
