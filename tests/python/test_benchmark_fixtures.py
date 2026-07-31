from __future__ import annotations

from pathlib import Path
import sys
import unittest

import numpy as np


SCRIPTS = Path(__file__).parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from benchmark_large_scene import large_scene_arrays
from benchmark_large_scene import write_large_radiance_scene
from compare_full_transport_shoebox import (
    annual_metrics,
    deterministic_annual_sky,
)


class BenchmarkFixtureTests(unittest.TestCase):
    def test_deterministic_annual_sky_has_lm83_style_schedule(self):
        sky, occupancy = deterministic_annual_sky()
        self.assertEqual(sky.shape, (146, 8760, 3))
        self.assertEqual(occupancy.shape, (8760,))
        self.assertEqual(int(np.sum(occupancy)), 3650)
        self.assertTrue(np.isfinite(sky).all())
        self.assertGreater(float(np.max(sky)), 0.0)

    def test_annual_metrics_use_area_weighted_sda(self):
        illuminance = np.asarray(
            [[400.0, 400.0], [400.0, 0.0], [0.0, 0.0]], dtype=np.float32
        )
        metrics = annual_metrics(
            illuminance,
            np.ones(2, dtype=np.float32),
            np.asarray([2.0, 1.0, 1.0], dtype=np.float32),
        )
        self.assertEqual(metrics["mean_daylight_autonomy"], 0.5)
        self.assertEqual(metrics["static_sda_300_50_percent"], 75.0)

    def test_large_scene_fixture_has_instancing_and_area_weights(self):
        arrays = large_scene_arrays(4, 3, 0.6)
        self.assertEqual(arrays["mesh_ranges"].shape, (1, 2))
        self.assertEqual(arrays["instance_transforms"].shape, (4, 4, 4))
        self.assertEqual(arrays["sensor_positions"].shape, (12, 3))
        self.assertEqual(arrays["sensor_room_ids"].tolist(), [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3])
        np.testing.assert_allclose(arrays["sensor_area_weights"], 18.0)
        self.assertEqual(float(np.sum(arrays["sensor_area_weights"])), 216.0)

    def test_large_radiance_scene_expands_every_instance(self):
        arrays = large_scene_arrays(2, 1, 0.6)
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as folder:
            scene = Path(folder) / "scene.rad"
            write_large_radiance_scene(scene, arrays, 0.6)
            text = scene.read_text(encoding="utf-8")
        self.assertIn("room_0_triangle_0", text)
        self.assertIn("room_1_triangle_25", text)
        self.assertEqual(text.count(" polygon room_"), 52)


if __name__ == "__main__":
    unittest.main()
