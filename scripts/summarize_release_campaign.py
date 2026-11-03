#!/usr/bin/env python3
"""Produce a concise campaign account without treating unstable oracles as passes."""

import argparse
import json
from pathlib import Path


def summarize(directory):
    suite = json.loads((directory / "suite.json").read_text())
    records = suite["scenes"]
    counts = {}
    for record in records:
        kind = record.get("result_class", "incomplete")
        counts[kind] = counts.get(kind, 0) + 1
    lines = [
        "# Architectural validation campaign",
        "",
        f"Accounted: {len(records)}/{suite['selected_case_count']} selected comparisons; corpus requires {suite['expected_case_count']}.",
        f"Release qualification: {suite['status']}; dirty snapshot: {suite['dirty']}; smoke: {suite['smoke']}.",
        f"Backend: {suite['backend']}; elapsed: {suite.get('elapsed_seconds', sum(record.get('elapsed_seconds', 0) for record in records)):.1f} s.",
        "",
        "Unstable references are inconclusive, not confirmed accuracy failures or passes.",
        "",
        "| Result class | Comparisons |",
        "| --- | ---: |",
        *[
            f"| {kind} | {counts.get(kind, 0)} |"
            for kind in (
                "passed",
                "accuracy_failure",
                "unstable_reference",
                "execution_error",
                "incomplete",
            )
        ],
        "",
        "| Scene | Basis | Result | Time (s) | Worst full-coefficient sensor / patch / RGB | Worst annual position / hour / lux error |",
        "| --- | --- | --- | ---: | --- | --- |",
    ]
    for record in records:
        coefficient_grids = record.get("coefficients", {}).get("grids", [])
        annual_grids = record.get("annual", {}).get("grids", [])
        worst_coefficient = max(
            (grid["stages"]["full"] for grid in coefficient_grids),
            key=lambda stage: stage["absolute_error"]["maximum"],
            default=None,
        )
        worst_annual = max(
            (grid["illuminance"] for grid in annual_grids),
            key=lambda stage: stage["maximum_absolute_error_lux"],
            default=None,
        )
        coefficient_text = "—"
        if worst_coefficient:
            worst = worst_coefficient["worst"]
            coefficient_text = f"{worst['global_sensor_index']} / {worst['sky_patch_index']} / {worst['rgb_channel']}; position={worst.get('position', 'not recorded')}; max={worst_coefficient['absolute_error']['maximum']:.6g}, bias={float(worst_coefficient['nmbe_percent']):.2f}%, RMS={float(worst_coefficient['rms_normalized_rmse_percent']):.2f}%"
        annual_text = "—"
        if worst_annual:
            worst = worst_annual["worst"]
            annual_text = f"{worst['position']} / {worst['hour_of_year']}; max={worst_annual['maximum_absolute_error_lux']:.2f} lux"
        lines.append(
            f"| {record['scene']} | MF:{record['sky_density']} | {record.get('result_class', 'incomplete')} | {record.get('elapsed_seconds', 0):.1f} | {coefficient_text} | {annual_text} |"
        )
    errors = [record for record in records if "error" in record]
    if errors:
        lines += ["", "## Execution errors", ""]
        lines += [
            f"- {record['scene']} / MF:{record['sky_density']}: {record['error_type']}: {record['error']}"
            for record in errors
        ]
    compatibility_failures = []
    for record in records:
        for check, result in record.get("compatibility", {}).items():
            if result.get("passed") is not False:
                continue
            detail = ""
            if check == "stock":
                detail = (
                    f"; reference MF:{result.get('reference_sky_density', 'unknown')}, "
                    f"candidate MF:{result.get('candidate_sky_density', record['sky_density'])}"
                )
            compatibility_failures.append(
                f"- {record['scene']} / MF:{record['sky_density']}: {check}{detail}."
            )
    if compatibility_failures:
        lines += [
            "",
            "## Compatibility failures",
            "",
            "These checks are reported independently of reference stability and do not change the numerical result classes above.",
            "",
            *compatibility_failures,
        ]
    lines += [
        "",
        "Windows Vulkan and live Rhino acceptance remain separate requirements. Dirty-snapshot results cannot qualify a release.",
        "",
    ]
    (directory / "campaign.md").write_text("\n".join(lines))
    return {
        "accounted": len(records),
        "selected": suite["selected_case_count"],
        "result_counts": counts,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    print(json.dumps(summarize(parser.parse_args().directory), indent=2))
