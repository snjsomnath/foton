#!/usr/bin/env python3
"""Verify the committed release evidence named in validation/release-evidence.json.

A release is qualified by evidence that lives in the repository: one complete
numerical suite per GPU backend and at least one live Rhino 8 checklist, each
produced on the release commit or on an ancestor that differs from it only by
evidence, documentation, tests, workflows and this verifier. Cases outside the
gates must be named, with a
reason, in validation/known-open-cases.json; everything else must pass.
"""

import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from validation.scenes import SCENE_IDS, SCENE_VERSION  # noqa: E402

RHINO_SCENARIOS = (
    "install",
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
REQUIRED_BACKENDS = ("metal", "vulkan")
NUMERICAL_SYSTEMS = {"metal": ("Darwin",), "vulkan": ("Windows", "Linux")}
RHINO_SYSTEMS = ("Darwin", "Windows")
# Paths that may differ between the commit evidence was produced on and the
# release commit without invalidating the evidence: nothing here changes what
# the engine, the scenes or the suite compute. The verifier, the tests and the
# workflows only read results; they are listed so that tightening the gate
# after a campaign does not force the campaign to be rerun.
EVIDENCE_ONLY_PATHS = (
    "validation/results/",
    "validation/release-evidence.json",
    "validation/known-open-cases.json",
    "validation/rhino-evidence.example.json",
    "docs/",
    "README.md",
    "CHANGELOG.md",
    "epw/README.md",
    "scripts/verify_release_evidence.py",
    "tests/",
    ".github/",
    ".gitattributes",
    ".gitignore",
)
# A numerical suite from an earlier version still qualifies a release when the
# engine is unchanged since: only these paths changed, and the version files
# changed only on their version lines. None of them is imported by the suite.
ENGINE_UNCHANGED_PATHS = (
    "grasshopper_foton/",
    "scripts/build_grasshopper.py",
    "scripts/package_grasshopper.py",
    "scripts/check_grasshopper.py",
    "scripts/package_yak.py",
    "viewer/",
    "CONTRIBUTING.md",
    "benchmarks/",
)
VERSION_FILES = (
    "Cargo.toml",
    "Cargo.lock",
    "pyproject.toml",
    "python/daylight_engine/viewer/app.py",
    "viewer/package.json",
    "viewer/package-lock.json",
    "grasshopper_foton/yak/manifest.yml",
)
OPEN_CASE_CLASSES = ("accuracy_failure", "unstable_reference")
# Each backend's evidence is also indifferent to the other backend's crate.
BACKEND_ONLY_PATHS = {
    "metal": ("crates/daylight-vulkan/",),
    "vulkan": ("crates/daylight-metal/",),
}
# The Rhino checklist exercises the Grasshopper bundle and the engine; it never
# runs the numerical suite, its scene generator or its oracle.
RHINO_IGNORED_PATHS = (
    "validation/",
    "scripts/validate_release_suite.py",
    "scripts/export_reference_bundle.py",
    "scripts/run_honeybee_annual_reference.py",
    "benchmarks/",
)


def git_changed_paths(evidence_commit, release_commit, root=ROOT):
    """Paths that differ between two commits, or None when the first is not an
    ancestor of the second (or either is unknown)."""
    if evidence_commit == release_commit:
        return []
    try:
        subprocess.run(
            ["git", "merge-base", "--is-ancestor", evidence_commit, release_commit],
            cwd=root,
            check=True,
            capture_output=True,
        )
        output = subprocess.check_output(
            ["git", "diff", "--name-only", evidence_commit, release_commit],
            cwd=root,
            text=True,
        )
    except (subprocess.CalledProcessError, OSError):
        return None
    return [line for line in output.splitlines() if line]


def git_version_only(evidence_commit, release_commit, paths, root=ROOT):
    """True when every changed line of ``paths`` between the commits mentions a version."""
    if not paths:
        return True
    try:
        output = subprocess.check_output(
            ["git", "diff", "-U0", evidence_commit, release_commit, "--", *paths],
            cwd=root,
            text=True,
        )
    except (subprocess.CalledProcessError, OSError):
        return False
    for line in output.splitlines():
        if line.startswith(("+++", "---")) or not line.startswith(("+", "-")):
            continue
        if "version" not in line.lower():
            return False
    return True


def _engine_unchanged(evidence_commit, release_commit, changed_paths, version_only, backend):
    """True when only non-engine paths and version numbers changed since the evidence."""
    if not evidence_commit:
        return False
    changed = changed_paths(evidence_commit, release_commit)
    if changed is None:
        return False
    allowed = EVIDENCE_ONLY_PATHS + BACKEND_ONLY_PATHS.get(backend, ()) + ENGINE_UNCHANGED_PATHS
    versions = [p for p in changed if p in VERSION_FILES]
    if any(p not in VERSION_FILES and not p.startswith(allowed) for p in changed):
        return False
    return version_only(evidence_commit, release_commit, versions)


def _commit_error(label, evidence_commit, release_commit, changed_paths, backend=None, also_ignored=()):
    if not evidence_commit:
        return f"{label} records no commit"
    changed = changed_paths(evidence_commit, release_commit)
    if changed is None:
        return f"{label} was produced on {evidence_commit[:12]}, which is not the release commit or one of its ancestors"
    ignored = EVIDENCE_ONLY_PATHS + BACKEND_ONLY_PATHS.get(backend, ()) + tuple(also_ignored)
    foreign = [p for p in changed if not p.startswith(ignored)]
    if foreign:
        return (
            f"{label} was produced on {evidence_commit[:12]}; the release commit also changes "
            + ", ".join(foreign[:5])
            + (" ..." if len(foreign) > 5 else "")
        )
    return None


def verify_known_open_cases(known):
    errors = []
    cases = known.get("cases") if isinstance(known, dict) else None
    if not isinstance(cases, list):
        return ["known-open-cases file has no case list"], {}
    allowed = {}
    for case in cases:
        key = (case.get("scene"), case.get("sky_density"))
        if key[0] not in SCENE_IDS or key[1] not in (1, 2):
            errors.append(f"known open case {key} is not a corpus case")
            continue
        classes = tuple(case.get("result_classes", ()))
        if not classes or any(c not in OPEN_CASE_CLASSES for c in classes):
            errors.append(f"known open case {key} must name result classes from {OPEN_CASE_CLASSES}")
        if not case.get("reason") or not case.get("documented_in"):
            errors.append(f"known open case {key} needs a reason and a documented_in reference")
        allowed[key] = classes
    return errors, allowed


def verify_suite(
    suite, release_commit, version, backend, allowed_open, changed_paths, version_only=git_version_only
):
    errors = []
    label = f"{backend} suite"

    def require(condition, message):
        if not condition:
            errors.append(f"{label}: {message}")

    reused = suite.get("engine_version") != version and _engine_unchanged(
        suite.get("commit"), release_commit, changed_paths, version_only, backend
    )
    if not reused:
        commit_error = _commit_error(label, suite.get("commit"), release_commit, changed_paths, backend)
        if commit_error:
            errors.append(commit_error)
        require(
            suite.get("engine_version") == version,
            "wheel version differs from the release, and the engine changed since",
        )
    require(suite.get("suite_version") == SCENE_VERSION, "suite version is obsolete")
    require(suite.get("dirty") is False and suite.get("smoke") is False, "dirty or smoke runs cannot qualify releases")
    require(suite.get("backend") == backend, "backend differs from the manifest entry")
    system = suite.get("hardware", {}).get("system")
    require(system in NUMERICAL_SYSTEMS.get(backend, ()), f"{system!r} is not a supported system for {backend}")
    # A suite may be judged against the converged Radiance references of an
    # earlier clean campaign on this corpus (scripts/export_reference_bundle.py);
    # the references describe the scenes, not the engine under test.
    source = suite.get("reference_source")
    if source is not None:
        require(
            isinstance(source, dict)
            and source.get("suite_version") == SCENE_VERSION
            and source.get("dirty") is False
            and source.get("smoke") is False
            and bool(source.get("commit")),
            "reused references must come from a clean final run of this corpus and name its commit",
        )
    scenes = suite.get("scenes", [])
    require(
        len(scenes) == len(SCENE_IDS) * 2
        and {(s.get("scene"), s.get("sky_density")) for s in scenes}
        == {(s, d) for s in SCENE_IDS for d in (1, 2)},
        "%d scenes in both sky bases are required" % len(SCENE_IDS),
    )
    open_cases = []
    for scene in scenes:
        key = (scene.get("scene"), scene.get("sky_density"))
        require(scene.get("gpu_executed") is True, f"{key} did not execute on the GPU")
        if source is not None:
            require(
                (scene.get("reference_source") or {}).get("geometry_matches") is True,
                f"{key} was not checked against the geometry of its reused reference",
            )
        result_class = scene.get("result_class")
        if scene.get("passed") is True and scene.get("oracle_stable") is True and result_class == "passed":
            continue
        if result_class in allowed_open.get(key, ()):
            open_cases.append(key)
            continue
        require(False, f"{key} is {result_class or 'not passed'} and not a documented open case")
    return errors, {
        "backend": backend,
        "system": system,
        "machine": suite.get("hardware", {}).get("machine"),
        "device": _device_name(suite),
        "commit": suite.get("commit"),
        "engine_version": suite.get("engine_version"),
        "reused": bool(reused),
        "references": source.get("commit") if isinstance(source, dict) else None,
        "passed": len(scenes) - len(open_cases),
        "open": sorted(open_cases),
    }


def _device_name(suite):
    diagnostics = suite.get("hardware", {}).get("driver_diagnostics") or []
    for entry in diagnostics:
        if isinstance(entry, dict):
            for key in ("_name", "name", "device", "model"):
                if entry.get(key):
                    return str(entry[key])
    return None


def verify_rhino(rhino, release_commit, version, changed_paths):
    errors = []
    label = "Rhino evidence"

    def require(condition, message):
        if not condition:
            errors.append(f"{label}: {message}")

    commit_error = _commit_error(
        label,
        rhino.get("commit"),
        release_commit,
        changed_paths,
        rhino.get("backend"),
        RHINO_IGNORED_PATHS,
    )
    if commit_error:
        errors.append(commit_error)
    require(rhino.get("engine_version") == version, "engine version differs from the release")
    require(str(rhino.get("rhino_version", "")).startswith("8."), "Rhino 8 is required")
    require(rhino.get("system") in RHINO_SYSTEMS, "system must be Darwin or Windows")
    require(rhino.get("backend") in REQUIRED_BACKENDS, "backend must be metal or vulkan")
    scenarios = rhino.get("scenarios", {})
    missing = [name for name in RHINO_SCENARIOS if scenarios.get(name) is not True]
    require(not missing, "checklist incomplete: " + ", ".join(missing))
    require(bool(rhino.get("tested_at")) and bool(rhino.get("notes")), "needs a date and reproduction notes")
    return errors, {
        "system": rhino.get("system"),
        "backend": rhino.get("backend"),
        "rhino_version": rhino.get("rhino_version"),
        "commit": rhino.get("commit"),
    }


def verify(
    manifest, release_commit, version, *, load, changed_paths=git_changed_paths, version_only=git_version_only
):
    """Return (errors, summary) for a release-evidence manifest.

    `load(path)` returns the parsed JSON for a repository-relative path.
    """
    errors = []
    summary = {"numerical": [], "rhino": []}
    if manifest.get("version") != version:
        errors.append("evidence manifest is for version %r, not %s" % (manifest.get("version"), version))
    try:
        known = load(manifest.get("known_open_cases", "validation/known-open-cases.json"))
    except (OSError, ValueError) as error:
        errors.append(f"known-open-cases: {error}")
        known = {}
    known_errors, allowed_open = verify_known_open_cases(known)
    errors.extend(known_errors)

    seen_backends = set()
    for entry in manifest.get("numerical", []):
        backend = entry.get("backend")
        try:
            suite = load(entry["suite"])
        except (KeyError, OSError, ValueError) as error:
            errors.append(f"{backend} suite: cannot read evidence ({error})")
            continue
        suite_errors, record = verify_suite(
            suite, release_commit, version, backend, allowed_open, changed_paths, version_only
        )
        errors.extend(suite_errors)
        seen_backends.add(backend)
        summary["numerical"].append(record)
    for backend in REQUIRED_BACKENDS:
        if backend not in seen_backends:
            errors.append(f"no numerical evidence for the {backend} backend")

    rhino_entries = manifest.get("rhino", [])
    if not rhino_entries:
        errors.append("no live Rhino 8 evidence")
    for path in rhino_entries:
        try:
            rhino = load(path)
        except (OSError, ValueError) as error:
            errors.append(f"Rhino evidence: cannot read {path} ({error})")
            continue
        rhino_errors, record = verify_rhino(rhino, release_commit, version, changed_paths)
        errors.extend(rhino_errors)
        summary["rhino"].append(record)
    return errors, summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=ROOT / "validation/release-evidence.json")
    parser.add_argument("--commit", required=True, help="release commit SHA")
    parser.add_argument("--version", required=True, help="package version being released")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()

    def load(path):
        return json.loads((root / path).read_text())

    try:
        manifest = json.loads(args.manifest.read_text())
        errors, summary = verify(
            manifest,
            args.commit,
            args.version,
            load=load,
            changed_paths=lambda a, b: git_changed_paths(a, b, root),
            version_only=lambda a, b, paths: git_version_only(a, b, paths, root),
        )
    except (OSError, ValueError, TypeError) as error:
        errors, summary = [str(error)], {"numerical": [], "rhino": []}
    for record in summary["numerical"]:
        print(
            f"{record['backend']} on {record['system']} ({record['device'] or record['machine']}): "
            f"{record['passed']} cases passed, {len(record['open'])} documented open"
            + (
                f" (Radiance references reused from {record['references'][:12]})"
                if record.get("references")
                else ""
            )
            + (
                f"; engine unchanged since {record['engine_version']}, so that run still applies"
                if record.get("reused")
                else ""
            )
        )
    for record in summary["rhino"]:
        print(f"Rhino {record['rhino_version']} on {record['system']} with {record['backend']}: checklist complete")
    for error in errors:
        print("Release evidence incomplete: " + error, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
