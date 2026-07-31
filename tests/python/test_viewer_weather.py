from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import numpy as np

from foton import sky_patch_directions, sky_patch_solid_angles
from foton.viewer.weather import (
    DEMO_EXTERIOR_ILLUMINANCE_LUX,
    PHOTOPIC_WEIGHTS,
    WeatherStore,
    _epw_timestep_labels,
    occupancy_schedule,
    parse_radiance_matrix,
)


class ViewerWeatherTests(unittest.TestCase):
    def test_fixed_schedule_has_3650_occupied_hours(self):
        occupancy = occupancy_schedule(8760)
        self.assertEqual(float(np.sum(occupancy)), 3650.0)
        np.testing.assert_array_equal(
            occupancy[:24],
            np.asarray([0] * 8 + [1] * 10 + [0] * 6, dtype=np.float32),
        )

    def test_schedule_rejects_nonannual_input(self):
        with self.assertRaises(ValueError):
            occupancy_schedule(24)

    def test_matrix_parser_preserves_patch_major_orientation(self):
        text = "\n".join(
            [
                "#?RADIANCE",
                "NROWS=2",
                "NCOLS=2",
                "NCOMP=3",
                "",
                "1 2 3",
                "4 5 6",
                "7 8 9",
                "10 11 12",
            ]
        )
        matrix = parse_radiance_matrix(text, 2, 2)
        self.assertEqual(matrix.shape, (2, 2, 3))
        np.testing.assert_array_equal(matrix[1, 0], [7, 8, 9])

    def test_matrix_parser_rejects_bad_header(self):
        with self.assertRaises(RuntimeError):
            parse_radiance_matrix("NROWS=1\nNCOLS=1\nNCOMP=3\n1 1 1", 2, 1)

    def test_built_in_overcast_is_normalized_and_nonannual(self):
        with TemporaryDirectory() as directory:
            store = WeatherStore(cache_directory=directory)
        demo = store.demo
        self.assertEqual(store.initial.weather_id, demo.weather_id)
        self.assertFalse(demo.annual_metrics_available)
        self.assertEqual(demo.tregenza.shape, (146, 1, 3))
        self.assertEqual(demo.final.shape, (578, 1, 3))
        directions = np.asarray(sky_patch_directions("tregenza"))
        solid_angles = np.asarray(sky_patch_solid_angles("tregenza"))
        exterior = np.sum(
            demo.tregenza[:, 0, 0]
            * np.maximum(directions[:, 2], 0.0)
            * solid_angles
            * float(np.sum(PHOTOPIC_WEIGHTS))
        )
        self.assertAlmostEqual(
            float(exterior), DEMO_EXTERIOR_ILLUMINANCE_LUX, delta=0.5
        )

    def test_cached_epw_labels_use_start_of_hour(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "weather.epw"
            header = ["header"] * 8
            records = [
                f"2024,{(index // 744) % 12 + 1},1,{index % 24 + 1},60"
                for index in range(8760)
            ]
            path.write_text("\n".join(header + records), encoding="utf-8")
            labels = _epw_timestep_labels(path)
        self.assertEqual(labels[0], "01/01 00:00")
        self.assertEqual(labels[23], "01/01 23:00")


if __name__ == "__main__":
    unittest.main()
