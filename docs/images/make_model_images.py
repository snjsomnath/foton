"""Draw the four README benchmark models with their daylight results.

Each picture shows a model with its roof taken off, its sensor grid, and the
daylight autonomy (DA) of every sensor from one annual Foton run in Gothenburg
weather at Foton's default quality.

Run from the repository root:

    pip install -e ".[honeybee]" matplotlib
    python docs/images/make_model_images.py            # draw from saved results
    python docs/images/make_model_images.py --compute  # re-run Foton first
    python docs/images/make_model_images.py --compute acceptance  # just one model

The DA values are saved in docs/images/benchmark-models-da.json, so the
picture can be redrawn without a GPU. ``--compute`` runs Foton on whatever
backend this machine has (Metal, Vulkan or the CPU fallback) and rewrites that
file.

The script lives under docs/ so that changing it never touches the release
evidence or starts a CI run.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.collections import PolyCollection  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs" / "images"
RESULTS = OUT / "benchmark-models-da.json"
WEATHER = ROOT / "epw" / "gothenburg.epw"
CORPUS = ROOT / "test_models" / "architectural"

# The same four models, in the same order, as the speed chart.
MODELS = (
    ("teaching_office", "Teaching office"),
    ("courtyard_rooms", "Courtyard, 4 rooms"),
    ("acceptance", "Acceptance model, 3 rooms"),
    ("office_floors", "Office block, 256 rooms"),
)

SURFACE = "#ffffff"
INK = "#0b0b0b"
INK_SECONDARY = "#52514e"
EDGE = "#8a8984"
FLOOR = "#f0efec"
WALL = "#e4e3df"
WALL_SIDE = "#d6d5d0"
GLASS = "#f7fbff"
GLASS_SEE_THROUGH = (0.85, 0.89, 0.91, 0.35)  # pale and see-through
SHADE = "#b9b8b3"
# One-hue blue ramp, light (little daylight) to dark (daylit most of the year).
DA_COLOURS = LinearSegmentedColormap.from_list(
    "da", ["#cde2fb", "#86b6ef", "#3987e5", "#256abf", "#104281"]
)

# Camera (azimuth, elevation) in degrees, looking from the south-west and
# above. The long office block is turned so it runs across the picture.
CAMERAS = {"office_floors": (-12, 45)}
DEFAULT_CAMERA = (-35, 38)
_camera = [math.radians(DEFAULT_CAMERA[0]), math.radians(DEFAULT_CAMERA[1])]


# --------------------------------------------------------------------------
# Models and results
# --------------------------------------------------------------------------


def _load_model(identifier: str):
    from honeybee.model import Model

    if identifier == "office_floors":
        sys.path.insert(0, str(ROOT / "scripts"))
        from benchmark_hardware import office_floors_model

        return office_floors_model()
    return Model.from_hbjson(str(CORPUS / f"{identifier}.hbjson"))


def compute(identifiers) -> None:
    """Run Foton on the given models and save their per-sensor DA."""
    import tempfile

    from foton.honeybee import HoneybeeStudy

    with tempfile.TemporaryDirectory() as work:
        for identifier in identifiers:
            model = _load_model(identifier)
            path = Path(model.to_hbjson(identifier, work))
            study = HoneybeeStudy(str(path), backend="auto")
            run = study.annual_daylight(str(WEATHER), quality="final")
            grids = [
                {
                    "identifier": grid.identifier,
                    "sda": round(float(grid.sda), 1),
                    "da": [round(float(value), 1) for value in grid.da],
                }
                for grid in run.grids
            ]
            # Re-read before writing, so several runs can share the file.
            results = {"weather": WEATHER.name, "quality": "final", "models": {}}
            if RESULTS.is_file():
                results = json.loads(RESULTS.read_text())
            results["models"][identifier] = {
                "backend": study.capabilities.get("name", ""),
                "grids": grids,
            }
            RESULTS.write_text(json.dumps(results, separators=(",", ":")) + "\n")
            sensors = sum(len(grid["da"]) for grid in grids)
            print(f"{identifier}: {sensors} sensors, saved to {RESULTS.relative_to(ROOT)}")


# --------------------------------------------------------------------------
# Drawing
# --------------------------------------------------------------------------


def _project(point):
    """Axonometric projection to (screen x, screen y, depth)."""
    x, y, z = point
    azimuth, elevation = _camera
    ca, sa = math.cos(azimuth), math.sin(azimuth)
    u = x * ca - y * sa
    v = x * sa + y * ca  # distance away from the camera, in plan
    screen_y = z * math.cos(elevation) + v * math.sin(elevation)
    depth = v * math.cos(elevation) - z * math.sin(elevation)
    return u, screen_y, depth


def _toward_camera():
    azimuth, elevation = _camera
    ca, sa = math.cos(azimuth), math.sin(azimuth)
    # Unit vector from the scene to the camera.
    return (-sa * math.cos(elevation), -ca * math.cos(elevation), math.sin(elevation))


def _poly(face3d):
    return [_project((p.x, p.y, p.z)) for p in face3d.vertices]


def _faces_toward_camera(normal) -> bool:
    cam = _toward_camera()
    return normal.x * cam[0] + normal.y * cam[1] + normal.z * cam[2] > 1e-6


def _sensor_cells(grid):
    """One polygon per sensor: its mesh face, shrunk a little to leave a gap."""
    cells = []
    for face in grid.mesh.face_vertices:
        cx = sum(p.x for p in face) / len(face)
        cy = sum(p.y for p in face) / len(face)
        cz = sum(p.z for p in face) / len(face)
        cells.append(
            [_project((cx + 0.85 * (p.x - cx), cy + 0.85 * (p.y - cy), cz + 0.85 * (p.z - cz))) for p in face]
        )
    return cells


def draw_model(ax, identifier: str, label: str, results: dict) -> None:
    """Draw one model, roof off, storey by storey from the bottom up."""
    azimuth, elevation = CAMERAS.get(identifier, DEFAULT_CAMERA)
    _camera[:] = [math.radians(azimuth), math.radians(elevation)]
    model = _load_model(identifier)
    grids = {grid.identifier: grid for grid in model.properties.radiance.sensor_grids}
    values = {grid["identifier"]: grid["da"] for grid in results["grids"]}

    # Sensors and room faces are grouped by storey so upper floors cover
    # lower ones. Front walls of the top storey are drawn as outlines only,
    # so you can see into the rooms.
    storeys = sorted({round(room.min.z, 2) for room in model.rooms})
    top = storeys[-1]
    layers = []  # (sort key, polygons, face colours, edge colour, line width)

    for room in model.rooms:
        level = storeys.index(round(room.min.z, 2))
        for face in room.faces:
            kind = face.type.name
            normal = face.normal
            if kind == "RoofCeiling":
                continue
            poly = _poly(face.geometry)
            depth = sum(p[2] for p in poly) / len(poly)
            if kind == "Floor":
                layers.append(((level, 0, -depth), [poly], [FLOOR], EDGE, 0.3))
                continue
            front = _faces_toward_camera(normal)
            interior = face.boundary_condition.name == "Surface"
            if front and (round(room.min.z, 2) == top or interior):
                # See-through: outline only, with glass panes outlined too.
                layers.append(((level, 3, -depth), [poly], ["none"], EDGE, 0.5))
                for aperture in face.apertures:
                    layers.append(
                        ((level, 3, -depth), [_poly(aperture.geometry)], [GLASS_SEE_THROUGH], INK_SECONDARY, 0.6)
                    )
                continue
            colour = WALL if not front else WALL_SIDE
            order = 1 if not front else 4
            layers.append(((level, order, -depth), [poly], [colour], EDGE, 0.3))
            for aperture in face.apertures:
                layers.append(
                    ((level, order, -depth + 1e-3), [_poly(aperture.geometry)], [GLASS], EDGE, 0.3)
                )

    for grid_id, grid in grids.items():
        floor_z = grid.mesh.min.z - 0.75
        level = min(range(len(storeys)), key=lambda i: abs(storeys[i] - floor_z))
        da = values[grid_id]
        polys = _sensor_cells(grid)
        colours = [DA_COLOURS(v / 100.0) for v in da]
        layers.append(((level, 2, 0.0), polys, colours, "none", 0.0))

    # Shades (overhangs, fins, neighbouring blocks) go on top, far ones first.
    shade_layers = []
    for shade in model.shades:
        poly = _poly(shade.geometry)
        depth = sum(p[2] for p in poly) / len(poly)
        shade_layers.append(((len(storeys), 0, -depth), [poly], [SHADE], EDGE, 0.3))

    for _, polys, colours, edge, width in sorted(layers + shade_layers, key=lambda layer: layer[0]):
        flat = [[(p[0], p[1]) for p in poly] for poly in polys]
        ax.add_collection(
            PolyCollection(flat, facecolors=colours, edgecolors=edge, linewidths=width)
        )

    ax.autoscale_view()
    ax.set_aspect("equal")
    ax.axis("off")
    sensors = sum(len(g["da"]) for g in results["grids"])
    mean_da = sum(sum(g["da"]) for g in results["grids"]) / sensors
    ax.set_title(
        f"{label}\n{sensors:,} sensors, mean DA {mean_da:.0f} %",
        fontsize=11,
        color=INK,
        loc="left",
        linespacing=1.4,
    )


def _style() -> None:
    names = {font.name for font in font_manager.fontManager.ttflist}
    family = "Inter" if "Inter" in names else "DejaVu Sans"
    plt.rcParams.update({"font.family": family, "font.size": 11, "figure.facecolor": SURFACE})


def draw(results: dict) -> Path:
    _style()
    fig = plt.figure(figsize=(10, 7.4))
    grid = fig.add_gridspec(2, 3, height_ratios=[1.25, 1], left=0.03, right=0.97, top=0.78, bottom=0.12, hspace=0.25, wspace=0.08)
    axes = [fig.add_subplot(grid[0, i]) for i in range(3)] + [fig.add_subplot(grid[1, :])]
    for ax, (identifier, label) in zip(axes, MODELS):
        draw_model(ax, identifier, label, results["models"][identifier])

    fig.text(0.03, 0.965, "The benchmark models and their results", fontsize=15, fontweight="semibold", color=INK, va="top")
    fig.text(
        0.03,
        0.915,
        "Roof off. Each square is a sensor, coloured by daylight autonomy: the share of working hours\n"
        "with at least 300 lux from daylight alone. Gothenburg weather, Foton's default quality.",
        fontsize=10.5,
        color=INK_SECONDARY,
        va="top",
    )
    bar = fig.add_axes([0.3, 0.05, 0.4, 0.022])
    gradient = [[i / 255 for i in range(256)]]
    bar.imshow(gradient, aspect="auto", cmap=DA_COLOURS, extent=(0, 100, 0, 1))
    bar.set_yticks([])
    bar.set_xticks([0, 25, 50, 75, 100])
    bar.set_xticklabels(["0 %", "25 %", "50 %", "75 %", "100 %"], fontsize=9.5, color=INK_SECONDARY)
    bar.tick_params(length=0)
    for spine in bar.spines.values():
        spine.set_visible(False)
    bar.set_title("Daylight autonomy (DA)", fontsize=9.5, color=INK_SECONDARY, pad=4)

    path = OUT / "benchmark-models.png"
    fig.savefig(path, dpi=200)
    plt.close(fig)
    # A 256-colour palette keeps the file small with no visible change.
    from PIL import Image

    Image.open(path).convert("RGB").quantize(256, dither=Image.Dither.NONE).save(path, optimize=True)
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--compute",
        nargs="*",
        metavar="MODEL",
        help="Re-run Foton before drawing: all four models, or only the ones named.",
    )
    args = parser.parse_args()
    if args.compute is not None:
        compute(args.compute or [identifier for identifier, _ in MODELS])
    path = draw(json.loads(RESULTS.read_text()))
    print(f"Wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
