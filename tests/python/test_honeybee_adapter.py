from __future__ import annotations

import importlib.util
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import numpy as np

from honeybee.model import Model
from honeybee.room import Room

from foton.honeybee.adapter import (
    _append_geometry,
    prepare_honeybee_scene,
)
from foton.honeybee.radiance import (
    _glow_modifiers,
    _parse_rcontrib_visibility,
    _radiance_subprocess_environment,
    _write_honeybee_radiance_scene,
    run_radiance_visibility,
)
from foton.honeybee.recipe import (
    Recipe,
    _coefficients_to_visibility,
)
from foton.honeybee.settings import RecipeSettings
from foton.honeybee.validation import compare_coefficient_repeatability
from foton.honeybee.validation import compare_coefficient_convergence
from scripts.validate_honeybee_coefficients import _ray_is_on_triangle_edge


class HoneybeeAdapterTests(unittest.TestCase):
    def test_overlapping_rooms_remain_a_recorded_warning(self):
        model = Model(
            "Overlap",
            [Room.from_box("RoomA", 2, 2, 2), Room.from_box("RoomB", 2, 2, 2)],
        )
        prepared = prepare_honeybee_scene(model)
        self.assertEqual(
            {str(item.get("code")) for item in prepared.validation_warnings},
            {"000108"},
        )

    def test_conversion_does_not_mutate_model_units(self):
        room = Room.from_box("Room", 20, 30, 10)
        model = Model("Imperial", [room], units="Feet")
        prepared = prepare_honeybee_scene(
            model, grid_size=2.0, sensor_height=2.5
        )
        self.assertEqual(model.units, "Feet")
        self.assertEqual(prepared.model.units, "Meters")
        self.assertEqual(prepared.arrays["vertices"].dtype, np.float32)
        self.assertTrue(prepared.arrays["vertices"].flags.c_contiguous)

    def test_punched_geometry_preserves_opening_area(self):
        room = Room.from_box("Room", 6, 9, 3)
        wall = room[3]
        aperture = wall.aperture_by_width_height(3, 1.5, 1)
        vertices, triangles, materials = [], [], []
        _append_geometry(
            wall.punched_geometry, vertices, triangles, materials
        )
        vertices = np.asarray(vertices)
        triangle_area = 0.0
        for triangle in triangles:
            first, second, third = vertices[triangle]
            triangle_area += np.linalg.norm(
                np.cross(second - first, third - first)
            ) * 0.5
        self.assertAlmostEqual(
            triangle_area,
            wall.geometry.area - aperture.geometry.area,
            places=5,
        )

    def test_auto_grid_has_stable_upward_sensors(self):
        room = Room.from_box("Room", 2, 2, 3)
        model = Model("Grid", [room])
        prepared = prepare_honeybee_scene(
            model, grid_size=0.5, sensor_height=0.75
        )
        arrays = prepared.arrays
        self.assertGreater(arrays["sensor_positions"].shape[0], 0)
        np.testing.assert_allclose(
            arrays["sensor_normals"],
            np.tile([0.0, 0.0, 1.0], (arrays["sensor_normals"].shape[0], 1)),
        )
        np.testing.assert_array_equal(
            arrays["sensor_ids"],
            np.arange(arrays["sensor_ids"].size, dtype=np.uint32),
        )
        self.assertEqual(prepared.grid_info[0]["source"], "automatic")

    def test_aperture_shade_is_included_as_opaque_geometry(self):
        room = Room.from_box("Room", 6, 9, 3)
        aperture = room[3].aperture_by_width_height(3, 1.5, 1)
        aperture.overhang(0.75)
        model = Model("Shade", [room])
        unshaded = Model("NoShade", [Room.from_box("Room2", 6, 9, 3)])
        unshaded.rooms[0][3].aperture_by_width_height(3, 1.5, 1)
        shaded_scene = prepare_honeybee_scene(model)
        unshaded_scene = prepare_honeybee_scene(unshaded)
        self.assertGreater(
            shaded_scene.geometry_info["triangle_count"],
            unshaded_scene.geometry_info["triangle_count"],
        )


class RecipeContractTests(unittest.TestCase):
    def test_converged_oracle_compares_replicate_half_means(self):
        prepared = SimpleNamespace(
            grid_info=[
                {
                    "identifier": "grid",
                    "start_sensor_index": 0,
                    "sensor_count": 1,
                }
            ]
        )
        direct = np.ones((1, 2, 3), dtype=np.float32)
        full = direct * 1.5
        stable = compare_coefficient_convergence(
            prepared,
            radiance_direct_runs=[direct.copy() for _ in range(4)],
            radiance_full_runs=[full.copy() for _ in range(4)],
        )
        self.assertTrue(stable["oracle_stable"])
        unstable = compare_coefficient_convergence(
            prepared,
            radiance_direct_runs=[direct, direct, direct * 1.2, direct * 1.2],
            radiance_full_runs=[full, full, full * 1.2, full * 1.2],
        )
        self.assertFalse(unstable["oracle_stable"])

    def test_sky_dome_glow_modifiers_are_discovered(self):
        with TemporaryDirectory() as folder:
            path = Path(folder, "sky.dome")
            path.write_text(
                "void glow sky_glow\n0\n0\n4 1 1 1 0\n\n"
                "sky_glow source sky\n0\n0\n4 0 0 1 180\n",
                encoding="ascii",
            )
            self.assertEqual(_glow_modifiers(path), ["sky_glow"])

    def test_exact_edge_ray_classification(self):
        vertices = np.asarray(
            [[0, 0, 1], [1, 0, 1], [0, 1, 1]], dtype=np.float64
        )
        triangles = np.asarray([[0, 1, 2]], dtype=np.uint32)
        self.assertTrue(
            _ray_is_on_triangle_edge(
                [0.5, 0, 0], [0, 0, 1], vertices, triangles
            )
        )
        self.assertFalse(
            _ray_is_on_triangle_edge(
                [0.25, 0.25, 0], [0, 0, 1], vertices, triangles
            )
        )

    def test_radiance_repeatability_detects_stable_and_unstable_oracles(self):
        prepared = SimpleNamespace(
            grid_info=[
                {
                    "identifier": "grid",
                    "start_sensor_index": 0,
                    "sensor_count": 1,
                }
            ]
        )
        direct = np.ones((1, 2, 3), dtype=np.float32)
        full = direct * 1.5
        stable = compare_coefficient_repeatability(
            prepared,
            radiance_direct_runs=[direct, direct.copy()],
            radiance_full_runs=[full, full.copy()],
        )
        self.assertTrue(stable["oracle_stable_at_release_gates"])
        unstable = compare_coefficient_repeatability(
            prepared,
            radiance_direct_runs=[direct, direct * 1.2],
            radiance_full_runs=[full, full * 1.2],
        )
        self.assertFalse(unstable["oracle_stable_at_release_gates"])

    def test_recipe_accepts_lbt_style_names(self):
        recipe = Recipe("direct-visibility")
        recipe.input_value_by_name("sky basis", "reinhart_mf2")
        self.assertEqual(recipe.name, "direct_visibility")
        self.assertEqual(recipe.inputs["sky_basis"], "reinhart-mf2")
        annual = Recipe("annual_daylight")
        self.assertEqual(annual.name, "annual_daylight")
        self.assertTrue(annual.inputs["export_illuminance"])
        self.assertEqual(annual.inputs["sky_density"], 1)
        self.assertIsNone(annual.inputs["direct_samples"])
        self.assertIsNone(annual.inputs["maximum_samples"])

    def test_recipe_settings_validate_workers(self):
        with self.assertRaises(ValueError):
            RecipeSettings(workers=0)

    def test_coefficients_normalize_to_visibility(self):
        weights = np.asarray([[0.5, 0.0, 0.25]], dtype=np.float32)
        coefficients = np.asarray(
            [[[0.5, 0.5, 0.5], [0, 0, 0], [0, 0, 0]]],
            dtype=np.float32,
        )
        visibility = _coefficients_to_visibility(coefficients, weights)
        np.testing.assert_array_equal(
            visibility, np.asarray([[1, 0, 0]], dtype=np.float32)
        )

    def test_rcontrib_parser_accepts_two_modifiers(self):
        output = "1 1 1 0 0 0\n0 0 0 0 0 0\n"
        visibility = _parse_rcontrib_visibility(output, 2)
        np.testing.assert_array_equal(
            visibility, np.asarray([1, 0], dtype=np.float32)
        )

    def test_rcontrib_parser_rejects_bad_dimensions(self):
        with self.assertRaises(ValueError):
            _parse_rcontrib_visibility("1 1", 1)

    def test_radiance_environment_discovers_sibling_library(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            bin_directory = root / "bin"
            library_directory = root / "lib"
            bin_directory.mkdir()
            library_directory.mkdir()
            (library_directory / "rayinit.cal").write_text("", encoding="ascii")
            environment = _radiance_subprocess_environment(
                {
                    "oconv": str(bin_directory / "oconv"),
                    "rcontrib": str(bin_directory / "rcontrib"),
                }
            )
        self.assertEqual(
            environment["RAYPATH"].split(os.pathsep)[0],
            str(library_directory.resolve()),
        )

    @patch(
        "foton.honeybee.radiance._write_honeybee_radiance_scene"
    )
    @patch(
        "foton.honeybee.radiance.resolve_radiance_executables",
        return_value={"oconv": "/rad/oconv", "rcontrib": "/rad/rcontrib"},
    )
    @patch(
        "foton.honeybee.radiance._executable_version",
        return_value="Radiance test",
    )
    @patch("foton.honeybee.radiance.subprocess.run")
    def test_radiance_command_uses_explicit_direct_rays(
        self,
        run,
        _version,
        _resolve,
        write_scene,
    ):
        run.side_effect = [
            SimpleNamespace(returncode=0, stderr=b""),
            SimpleNamespace(
                returncode=0,
                stdout="1 1 1 0 0 0\n",
                stderr="",
            ),
        ]
        with TemporaryDirectory() as folder:
            result = run_radiance_visibility(
                object(),
                np.asarray([[0, 0, 1]], dtype=np.float32),
                np.asarray([[0, 0, 1]], dtype=np.float32),
                np.asarray([[0, 0, 1]], dtype=np.float32),
                np.asarray([[1]], dtype=np.float32),
                work_directory=folder,
                workers=2,
            )
            self.assertEqual(result.visibility.tolist(), [[1.0]])
            self.assertEqual(result.commands[0][0], "/rad/oconv")
            self.assertIn("-ab", result.commands[1])
            self.assertIn("-n", result.commands[1])
            rays = Path(folder, "patch_center_rays.pts").read_text()
            self.assertIn("1.0001", rays)
            write_scene.assert_called_once()


@unittest.skipUnless(
    importlib.util.find_spec("honeybee_radiance"),
    "honeybee-radiance is not installed",
)
class HoneybeeRadianceIntegrationTests(unittest.TestCase):
    def test_embedded_grid_and_writer_preserve_open_aperture_and_shade(self):
        from honeybee_radiance.sensorgrid import SensorGrid

        room = Room.from_box("Room", 6, 9, 3)
        aperture = room[3].aperture_by_width_height(
            3, 1.5, 1, aperture_identifier="SouthWindow"
        )
        aperture.overhang(0.75, base_name="SouthOverhang")
        model = Model("Embedded", [room])
        grid = SensorGrid.from_mesh3d(
            "RoomGrid", room.generate_grid(0.5, offset=0.75)
        )
        grid.room_identifier = room.identifier
        model.properties.radiance.add_sensor_grid(grid)

        prepared = prepare_honeybee_scene(model)
        self.assertEqual(prepared.grid_info[0]["source"], "embedded")
        with TemporaryDirectory() as folder:
            path = Path(folder, "scene.rad")
            _write_honeybee_radiance_scene(prepared.model, path)
            text = path.read_text()
        self.assertNotIn("SouthWindow polygon", text)
        self.assertIn("SouthOverhang", text)


if __name__ == "__main__":
    unittest.main()
