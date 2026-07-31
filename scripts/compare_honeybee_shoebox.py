#!/usr/bin/env python3
"""Run the Honeybee shaded-shoebox direct-visibility comparison."""

from __future__ import annotations

import argparse
from pathlib import Path

from honeybee.aperture import Aperture
from honeybee.model import Model
from honeybee.room import Room
from honeybee.shade import Shade
from ladybug_geometry.geometry3d.face import Face3D
from ladybug_geometry.geometry3d.pointvector import Point3D

from foton.honeybee import Recipe, RecipeSettings


def shaded_shoebox(embedded_grid=True):
    room = Room.from_box("Shoebox", 6.0, 9.0, 3.0)
    south_face = room[3]
    aperture = south_face.aperture_by_width_height(
        3.0, 1.5, sill_height=1.0, aperture_identifier="SouthWindow"
    )
    aperture.overhang(0.75, base_name="SouthOverhang")
    aperture.add_outdoor_shade(
        _side_fin("SouthWindow_LeftFin", 1.5, 0.5)
    )
    aperture.add_outdoor_shade(
        _side_fin("SouthWindow_RightFin", 4.5, 0.5)
    )
    model = Model("ShadedShoebox", [room])
    if embedded_grid:
        try:
            from honeybee_radiance.sensorgrid import SensorGrid
        except ImportError as error:
            raise RuntimeError(
                "embedded fixture grids require honeybee-radiance; "
                "use --auto-grid or install foton-daylight[honeybee]"
            ) from error
        mesh = room.generate_grid(0.5, offset=0.75)
        grid = SensorGrid.from_mesh3d("ShoeboxGrid", mesh)
        grid.room_identifier = room.identifier
        model.properties.radiance.add_sensor_grid(grid)
    return model


def _side_fin(identifier, x, depth):
    geometry = Face3D(
        (
            Point3D(x, 0.0, 1.0),
            Point3D(x, -depth, 1.0),
            Point3D(x, -depth, 2.5),
            Point3D(x, 0.0, 2.5),
        )
    )
    return Shade(identifier, geometry)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="simulation")
    parser.add_argument(
        "--backend",
        choices=("auto", "metal", "vulkan", "radiance", "compare"),
        default="compare",
    )
    parser.add_argument(
        "--engine-backend",
        choices=("auto", "metal", "vulkan"),
        default="auto",
        help="Hardware engine backend when --backend=compare.",
    )
    parser.add_argument("--basis", choices=("tregenza", "reinhart-mf2"), default="tregenza")
    parser.add_argument("--radiance-bin")
    parser.add_argument("--workers", type=int)
    parser.add_argument("--auto-grid", action="store_true")
    parser.add_argument("--reload-old", action="store_true")
    args = parser.parse_args()

    model = shaded_shoebox(embedded_grid=not args.auto_grid)
    fixture_folder = Path(args.output).expanduser().resolve() / "fixture"
    fixture_folder.mkdir(parents=True, exist_ok=True)
    model.to_hbjson("shaded_shoebox", str(fixture_folder), indent=2)

    recipe = Recipe("direct_visibility")
    recipe.input_value_by_name("model", model)
    recipe.input_value_by_name("backend", args.backend)
    recipe.input_value_by_name("engine_backend", args.engine_backend)
    recipe.input_value_by_name("sky_basis", args.basis)
    if args.radiance_bin:
        recipe.input_value_by_name("radiance_bin", args.radiance_bin)
    project = recipe.run(
        RecipeSettings(
            folder=args.output,
            workers=args.workers,
            reload_old=args.reload_old,
            report_out=True,
        )
    )
    print(recipe.output_value_by_name("comparison_report", project))


if __name__ == "__main__":
    main()
