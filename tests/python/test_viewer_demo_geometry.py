import unittest
import numpy as np
from pydantic import ValidationError
from daylight_engine.viewer.demo_geometry import DemoParameters, generate_demo_scene
from foton.viewer.geometry import GLASS_MATERIAL, WALL_MATERIAL


def area(vertices, triangles):
    points = vertices[triangles]
    return float(np.sum(np.linalg.norm(np.cross(points[:, 1]-points[:, 0], points[:, 2]-points[:, 0]), axis=1)*.5))


class DemoGeometryTests(unittest.TestCase):
    def test_three_windows_are_real_punched_openings(self):
        scene = generate_demo_scene({"window_count": 3, "window_width": 1.4})
        a = scene.arrays
        self.assertAlmostEqual(area(a["vertices"], a["triangles"][a["triangle_materials"] == GLASS_MATERIAL]), 3*1.4*1.5, places=5)
        self.assertAlmostEqual(area(a["vertices"], a["triangles"][a["triangle_materials"] == WALL_MATERIAL]), 2*(6+9)*3-3*1.4*1.5, places=4)

    def test_tapered_cell_areas_cover_the_actual_room(self):
        for taper in [.5, 1.4]:
            scene = generate_demo_scene({"rear_width_scale": taper})
            self.assertAlmostEqual(float(scene.arrays["sensor_area_weights"].sum()), 6*9*(1+taper)/2, places=4)
            cells = np.asarray(scene.geometry_payload["sensor_cells"])
            self.assertEqual(cells.shape, (216, 4, 3))
            np.testing.assert_allclose(cells.mean(axis=1), scene.arrays["sensor_positions"], atol=1e-5)

    def test_scale_uses_native_instances_with_independent_sensors(self):
        scene = generate_demo_scene({"room_count": 16})
        a = scene.arrays
        self.assertEqual(a["mesh_ranges"].shape, (1,2))
        self.assertEqual(a["instance_transforms"].shape, (16,4,4))
        self.assertEqual(a["sensor_positions"].shape, (3456,3))
        self.assertEqual(len(np.unique(a["sensor_ids"])), 3456)
        self.assertEqual(len(np.unique(a["sensor_room_ids"])), 16)
        self.assertEqual(len(scene.geometry_payload["sensor_cells"]), 3456)
        np.testing.assert_allclose(a["sensor_positions"][216]-a["sensor_positions"][0], a["instance_transforms"][1,:3,3])
        for value in a.values(): self.assertTrue(value.flags.c_contiguous)

    def test_invalid_openings_and_unbounded_load_are_rejected(self):
        for kwargs in [{"window_count":3}, {"room_count":1025}, {"rear_width_scale":0}, {"room_count":16,"sensor_spacing":.1}]:
            with self.assertRaises(ValidationError): DemoParameters(**kwargs)

    def test_l_shape_has_exact_area_and_no_sensors_in_the_notch(self):
        scene = generate_demo_scene({"width":12,"depth":14,"notch_width":7,"notch_depth":8,"sensor_spacing":.8})
        a = scene.arrays
        self.assertAlmostEqual(float(a["sensor_area_weights"].sum()), 112, places=4)
        self.assertAlmostEqual(area(a["vertices"], a["triangles"][a["triangle_materials"] == 1]), 112, places=4)
        self.assertFalse(np.any((a["sensor_positions"][:,0] > 5) & (a["sensor_positions"][:,1] > 6)))
        # Boundary length stays 52 m; the notch adds no interior partition.
        self.assertAlmostEqual(area(a["vertices"], a["triangles"][a["triangle_materials"] == WALL_MATERIAL]), 52*3-4.5, places=4)

    def test_context_is_a_native_opaque_mesh_without_sensors(self):
        scene = generate_demo_scene({"context_height":10})
        a = scene.arrays
        self.assertEqual(a["mesh_ranges"].shape, (2,2))
        np.testing.assert_array_equal(a["instance_mesh_indices"], [0,1])
        np.testing.assert_array_equal(a["instance_room_ids"], [1,0])
        self.assertEqual(a["sensor_positions"].shape, (216,3))
        np.testing.assert_array_equal(a["material_transmittance_rgb"][5], [0,0,0])
        self.assertEqual(np.count_nonzero(a["triangle_materials"] == 5), 12)

    def test_campus_has_1024_native_zones_and_24576_sensors(self):
        a = generate_demo_scene({"room_count":1024,"sensor_spacing":1.5}).arrays
        self.assertEqual(a["instance_transforms"].shape, (1024,4,4))
        self.assertEqual(a["sensor_positions"].shape, (24576,3))
        self.assertEqual(len(np.unique(a["sensor_room_ids"])), 1024)
        self.assertEqual(a["mesh_ranges"].shape, (1,2))
