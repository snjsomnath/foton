from __future__ import annotations

import unittest

import numpy as np
from pydantic import ValidationError

from foton.viewer.geometry import (
    FLOOR_MATERIAL,
    GLASS_MATERIAL,
    SHADE_MATERIAL,
    WALL_MATERIAL,
    RoomParameters,
    generate_parametric_scene,
)


def triangle_area(vertices: np.ndarray, triangles: np.ndarray) -> float:
    points = vertices[triangles]
    return float(
        np.sum(
            0.5
            * np.linalg.norm(
                np.cross(points[:, 1] - points[:, 0], points[:, 2] - points[:, 0]),
                axis=1,
            )
        )
    )


class ViewerGeometryTests(unittest.TestCase):
    def test_default_scene_has_punched_wall_glass_shades_and_216_sensors(self):
        generated = generate_parametric_scene()
        arrays = generated.arrays
        vertices = arrays["vertices"]
        triangles = arrays["triangles"]
        materials = arrays["triangle_materials"]

        wall_area = triangle_area(vertices, triangles[materials == WALL_MATERIAL])
        expected_wall_area = 2 * 9 * 3 + 6 * 3 + (6 * 3 - 3 * 1.5)
        self.assertAlmostEqual(wall_area, expected_wall_area, places=5)
        self.assertAlmostEqual(
            triangle_area(vertices, triangles[materials == FLOOR_MATERIAL]),
            54.0,
            places=5,
        )
        self.assertAlmostEqual(
            triangle_area(vertices, triangles[materials == GLASS_MATERIAL]),
            4.5,
            places=5,
        )
        self.assertGreater(
            triangle_area(vertices, triangles[materials == SHADE_MATERIAL]),
            0.0,
        )
        self.assertEqual(arrays["sensor_positions"].shape, (216, 3))
        self.assertAlmostEqual(float(np.sum(arrays["sensor_area_weights"])), 54.0)

    def test_sensor_grid_is_row_major_upward_and_contiguous(self):
        arrays = generate_parametric_scene().arrays
        np.testing.assert_array_equal(
            arrays["sensor_ids"],
            np.arange(216, dtype=np.uint32),
        )
        np.testing.assert_allclose(
            arrays["sensor_normals"],
            np.tile([0.0, 0.0, 1.0], (216, 1)),
        )
        self.assertLess(
            arrays["sensor_positions"][0, 1],
            arrays["sensor_positions"][12, 1],
        )
        for array in arrays.values():
            self.assertTrue(array.flags.c_contiguous)

    def test_open_aperture_omits_glass_triangles(self):
        generated = generate_parametric_scene({"glazing_enabled": False})
        self.assertFalse(
            np.any(generated.arrays["triangle_materials"] == GLASS_MATERIAL)
        )

    def test_invalid_window_and_workplane_are_rejected(self):
        with self.assertRaises(ValidationError):
            RoomParameters(width=3, window_width=3)
        with self.assertRaises(ValidationError):
            RoomParameters(height=3, workplane_height=3)


if __name__ == "__main__":
    unittest.main()
