"""Draw the README charts from the committed benchmark and validation results.

Run from the repository root:

    pip install matplotlib
    python scripts/make_readme_charts.py

It writes two PNG files to docs/images/:

* speed-vs-radiance.png: one annual run of the acceptance model, Foton
  against Honeybee's annual-daylight recipe (Radiance).
* accuracy-sda.png: spatial daylight autonomy for every sensor grid in the
  validation corpus, Foton against converged Radiance.

The charts only read files that are already in the repository, so anyone can
redraw them and check the numbers.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "images"

# Sources. Change these when a newer benchmark or campaign replaces them.
BENCHMARK = ROOT / "benchmarks/results/20261103T195604Z-CM-GHHXPN239T/benchmark.json"
CAMPAIGN = ROOT / "validation/results/2026-11-03-architectural-v4-metal-0.3.0-release"
STOCK = CAMPAIGN / "acceptance/mf1/stock_comparison/comparison.json"

# Colours: one accent for Foton, a neutral grey for the reference.
SURFACE = "#ffffff"
INK = "#0b0b0b"
INK_SECONDARY = "#52514e"
GRID = "#e4e3df"
FOTON = "#2a78d6"
REFERENCE = "#a3a29c"


def _style() -> None:
    """Use Inter when it is installed, and a quiet, consistent chart style."""
    names = {font.name for font in font_manager.fontManager.ttflist}
    family = "Inter" if "Inter" in names else "DejaVu Sans"
    plt.rcParams.update(
        {
            "font.family": family,
            "font.size": 11,
            "axes.edgecolor": GRID,
            "axes.labelcolor": INK_SECONDARY,
            "axes.facecolor": SURFACE,
            "figure.facecolor": SURFACE,
            "xtick.color": INK_SECONDARY,
            "ytick.color": INK_SECONDARY,
            "axes.spines.top": False,
            "axes.spines.right": False,
        }
    )


def _title(fig, title: str, subtitle: str) -> None:
    fig.text(0.04, 0.95, title, fontsize=15, fontweight="semibold", color=INK, va="top")
    fig.text(0.04, 0.875, subtitle, fontsize=10.5, color=INK_SECONDARY, va="top")


def speed_chart() -> Path:
    """Bar chart of one cold annual run on the acceptance model (2,020 sensors)."""
    benchmark = json.loads(BENCHMARK.read_text())
    acceptance = next(case for case in benchmark["cases"] if case["scene"] == "acceptance")
    foton_seconds = acceptance["wall_seconds"]["median"]
    radiance_seconds = json.loads(STOCK.read_text())["performance"]["radiance_seconds"]

    labels = ["Honeybee + Radiance 5.4\n(12 CPU workers)", "Foton\n(Apple M4 Pro GPU)"]
    values = [radiance_seconds, foton_seconds]
    colours = [REFERENCE, FOTON]

    fig, ax = plt.subplots(figsize=(8, 3.4))
    fig.subplots_adjust(left=0.27, right=0.9, top=0.72, bottom=0.27)
    bars = ax.barh(labels, values, color=colours, height=0.5)
    ax.invert_yaxis()
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_width() + max(values) * 0.015,
            bar.get_y() + bar.get_height() / 2,
            f"{value:.1f} s",
            va="center",
            fontsize=12,
            fontweight="semibold",
            color=INK,
        )
    ax.set_xlim(0, max(values) * 1.12)
    ax.set_xlabel("Seconds for a full annual daylight run (lower is better)")
    ax.xaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0, labelsize=11, labelcolor=INK)
    ax.spines["left"].set_visible(False)
    _title(
        fig,
        f"One annual study: {radiance_seconds:.1f} s with Radiance, {foton_seconds:.1f} s with Foton",
        "Acceptance model, 3 rooms, 2,020 sensors, Gothenburg weather. "
        "Each tool at its own defaults.",
    )
    fig.text(
        0.04,
        0.03,
        "Radiance's recipe uses 2 ambient bounces, Foton uses 8. Measured on one MacBook Pro, 3 Nov 2026.",
        fontsize=9,
        color=INK_SECONDARY,
    )
    path = OUT / "speed-vs-radiance.png"
    fig.savefig(path, dpi=200)
    plt.close(fig)
    return path


def accuracy_chart() -> Path:
    """Scatter of sDA per sensor grid, Foton against converged Radiance."""
    suite = json.loads((CAMPAIGN / "suite.json").read_text())
    radiance, foton = [], []
    for scene in suite["scenes"]:
        # One point per grid: use the 146-patch sky, Foton's default.
        if scene.get("sky_density") != 1:
            continue
        for grid in (scene.get("annual") or {}).get("grids", []):
            radiance.append(grid["sda"]["radiance_percent"])
            foton.append(grid["sda"]["foton_percent"])
    model_count = sum(1 for scene in suite["scenes"] if scene.get("sky_density") == 1)

    fig, ax = plt.subplots(figsize=(6.4, 6.4))
    fig.subplots_adjust(left=0.14, right=0.95, top=0.80, bottom=0.11)
    ax.plot([0, 100], [0, 100], color=INK_SECONDARY, linewidth=1, linestyle=(0, (4, 3)), zorder=1)
    ax.scatter(
        radiance,
        foton,
        s=34,
        color=FOTON,
        alpha=0.75,
        edgecolor=SURFACE,
        linewidth=0.8,
        zorder=2,
    )
    ax.text(70, 66, "Foton = Radiance", rotation=45, rotation_mode="anchor", ha="center", va="top", fontsize=9.5, color=INK_SECONDARY)
    ax.set_xlim(-3, 103)
    ax.set_ylim(-3, 103)
    ax.set_aspect("equal")
    ax.set_xlabel("sDA from Radiance (%)")
    ax.set_ylabel("sDA from Foton (%)")
    ax.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    _title(
        fig,
        "Foton agrees with Radiance, room by room",
        f"Spatial daylight autonomy for {len(radiance)} sensor grids in {model_count} test models.\n"
        "Radiance references were run until they stopped changing.",
    )
    path = OUT / "accuracy-sda.png"
    fig.savefig(path, dpi=200)
    plt.close(fig)
    return path


def main() -> None:
    _style()
    OUT.mkdir(parents=True, exist_ok=True)
    for path in (speed_chart(), accuracy_chart()):
        print(f"Wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
