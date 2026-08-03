from __future__ import annotations

from pathlib import Path
import unittest

import numpy as np

from foton.honeybee import honeybee_schedule
from foton.honeybee.adapter import prepare_honeybee_scene
from foton.honeybee.annual import _reduce_coefficients
from foton.honeybee.weather import parse_radiance_binary_matrix


ROOT = Path(__file__).resolve().parents[2]
ACCEPTANCE_MODEL = ROOT / "test_models" / "test.hbjson"


class HoneybeeScheduleTests(unittest.TestCase):
    def test_binary_gendaymtx_parser_preserves_order(self):
        values = np.arange(12, dtype=np.float32)
        content = (
            b"#?RADIANCE\nNROWS=2\nNCOLS=2\nNCOMP=3\nFORMAT=float\n\n"
            + values.tobytes()
        )
        matrix = parse_radiance_binary_matrix(content, 2, 2)
        np.testing.assert_array_equal(matrix.ravel(), values)
        self.assertTrue(matrix.flags.writeable)

    def test_default_schedule_matches_recipe_hours(self):
        schedule = honeybee_schedule()
        self.assertEqual(float(schedule.sum()), 3650.0)
        np.testing.assert_array_equal(
            np.flatnonzero(schedule[:24]), np.arange(8, 18)
        )

    def test_recipe_schedule_uses_point_one_cutoff(self):
        schedule = np.zeros(8760, dtype=np.float32)
        schedule[:4] = [0.0, 0.099, 0.1, 0.75]
        result = honeybee_schedule(schedule)
        np.testing.assert_array_equal(result[:4], [0, 0, 1, 1])

    def test_metric_threshold_boundaries_match_honeybee(self):
        # One patch and one RGB component are sufficient to exercise boundaries.
        coefficients = np.zeros((1, 578, 3), dtype=np.float32)
        coefficients[0, 0, 0] = 1.0 / 47.435
        sky = np.zeros((578, 8760, 3), dtype=np.float32)
        sky[0, :6, 0] = [0, 99, 100, 299, 300, 3000]
        sky[0, 6, 0] = 3001
        occupancy = np.zeros(8760, dtype=np.float32)
        occupancy[:7] = 1
        metrics = _reduce_coefficients(
            coefficients,
            sky,
            occupancy,
            threshold=300,
            udi_lower=100,
            udi_upper=3000,
        )
        self.assertAlmostEqual(float(metrics["da"][0]), 3 / 7 * 100, places=4)
        self.assertAlmostEqual(
            float(metrics["udi_lower"][0]), 2 / 7 * 100, places=4
        )
        self.assertAlmostEqual(float(metrics["udi"][0]), 4 / 7 * 100, places=4)
        self.assertAlmostEqual(
            float(metrics["udi_upper"][0]), 1 / 7 * 100, places=4
        )


class AcceptanceFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared = prepare_honeybee_scene(
            ACCEPTANCE_MODEL, include_aperture_glazing=True
        )

    def test_exact_grid_order_and_ranges(self):
        facts = [
            ("office_02", 0, 490),
            ("office_01", 490, 885),
            ("classroom_01", 1375, 175),
        ]
        self.assertEqual(
            int(self.prepared.arrays["sensor_positions"].shape[0]), 1550
        )
        self.assertEqual(len(self.prepared.grid_info), 3)
        for info, (identifier, start, count) in zip(
            self.prepared.grid_info, facts, strict=True
        ):
            self.assertEqual(info["identifier"], identifier)
            self.assertEqual(info["start_sensor_index"], start)
            self.assertEqual(info["sensor_count"], count)

    def test_positions_normals_and_areas_preserve_embedded_grids(self):
        positions = self.prepared.arrays["sensor_positions"]
        normals = self.prepared.arrays["sensor_normals"]
        areas = self.prepared.arrays["sensor_area_weights"]
        embedded = self.prepared.model.properties.radiance.sensor_grids
        for grid, info in zip(embedded, self.prepared.grid_info, strict=True):
            start = info["start_sensor_index"]
            end = start + info["sensor_count"]
            expected_positions = np.asarray(list(grid.positions))
            expected_normals = np.asarray(list(grid.directions))
            expected_normals /= np.linalg.norm(
                expected_normals, axis=1, keepdims=True
            )
            np.testing.assert_allclose(
                positions[start:end], expected_positions, atol=1e-6, rtol=0
            )
            np.testing.assert_allclose(
                normals[start:end], expected_normals, atol=1e-6, rtol=0
            )
            self.assertTrue(np.all(areas[start:end] > 0))

    def test_collision_is_warning_and_materials_are_resolved(self):
        warning_codes = {
            str(item.get("code")) for item in self.prepared.validation_warnings
        }
        self.assertIn("000108", warning_codes)
        materials = self.prepared.geometry_info["materials"]
        diffuse = {
            round(float(item["diffuse_rgb"][0]), 6)
            for item in materials
            if item["modifier_type"] == "Plastic"
        }
        self.assertTrue({0.2, 0.5, 0.8}.issubset(diffuse))
        glass = [
            item for item in materials if item["modifier_type"] == "Glass"
        ]
        self.assertTrue(glass)
        for material in glass:
            np.testing.assert_allclose(
                material["transmittance_rgb"],
                [0.640804765] * 3,
                atol=1e-6,
                rtol=0,
            )
        self.assertEqual(
            self.prepared.geometry_info["aperture_mode"], "thin_glass"
        )

    def test_classroom_grid_belongs_only_to_sealed_room(self):
        classroom = self.prepared.grid_info[2]
        classroom_identifier = next(
            room.identifier
            for room in self.prepared.model.rooms
            if room.display_name == "classroom_01"
        )
        room_id = self.prepared.room_map[classroom_identifier]
        self.assertEqual(classroom["room_ids"], [room_id])
        start = classroom["start_sensor_index"]
        end = start + classroom["sensor_count"]
        np.testing.assert_array_equal(
            self.prepared.arrays["sensor_room_ids"][start:end], room_id
        )
        classroom_room = next(
            room
            for room in self.prepared.model.rooms
            if room.display_name == "classroom_01"
        )
        self.assertEqual(sum(len(face.apertures) for face in classroom_room.faces), 0)


if __name__ == "__main__":
    unittest.main()
