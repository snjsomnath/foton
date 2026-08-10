from __future__ import annotations

from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np
from honeybee.model import Model
from honeybee.room import Room

from foton.honeybee import honeybee_schedule
from foton.honeybee import HoneybeeStudy
from foton import Engine
from foton.honeybee.adapter import prepare_honeybee_scene
from foton.honeybee.annual import _reduce_coefficients
from foton.honeybee.weather import parse_radiance_binary_matrix
from foton.honeybee.weather import AnnualWeather
from foton.honeybee.validation import _metrics_from_sunup


ROOT = Path(__file__).resolve().parents[2]
ACCEPTANCE_MODEL = ROOT / "test_models" / "test.hbjson"


class HoneybeeScheduleTests(unittest.TestCase):
    @patch("foton.honeybee.annual.prepare_annual_weather")
    def test_threshold_only_rerun_reuses_coefficients(self, prepare_weather):
        prepare_weather.return_value = AnnualWeather(
            sky=np.zeros((146, 8760, 3), dtype=np.float32),
            sun_up_hours=(),
            weather_id="test-weather",
            source="test.epw",
            location={},
            north=0.0,
            sky_density=1,
            basis="tregenza",
            cache_hit=True,
            gendaymtx="gendaymtx",
            gendaymtx_version="test",
        )
        study = HoneybeeStudy(
            Model("Cache", [Room.from_box("Room", 2, 2, 3)]),
            backend="reference",
            grid_size=5,
        )
        first = study.annual_daylight(
            "test.epw", maximum_samples=0, maximum_bounces=0
        )
        second = study.annual_daylight(
            "test.epw",
            threshold=400,
            maximum_samples=0,
            maximum_bounces=0,
        )
        self.assertFalse(first.metadata["solver"]["coefficient_cache_hit"])
        self.assertTrue(second.metadata["solver"]["coefficient_cache_hit"])
        self.assertEqual(second.timings["coefficient_trace_seconds"], 0.0)

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

    def test_converged_annual_metrics_account_for_occupied_night_hours(self):
        metrics = _metrics_from_sunup(
            np.asarray([[0, 100, 300, 3001]], dtype=np.float64),
            np.ones(4, dtype=bool),
            occupied_total=6,
        )
        self.assertAlmostEqual(float(metrics["da"][0]), 2 / 6 * 100)
        self.assertAlmostEqual(float(metrics["cda"][0]), (1 / 3 + 2) / 6 * 100)
        self.assertAlmostEqual(float(metrics["udi_lower"][0]), 3 / 6 * 100)
        self.assertAlmostEqual(float(metrics["udi"][0]), 2 / 6 * 100)
        self.assertAlmostEqual(float(metrics["udi_upper"][0]), 1 / 6 * 100)


class AcceptanceFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared = prepare_honeybee_scene(
            ACCEPTANCE_MODEL, include_aperture_glazing=True
        )

    def test_exact_grid_order_and_ranges(self):
        facts = [
            ("classroom_01", 0, 175),
            ("office_02", 175, 960),
            ("office_01", 1135, 885),
        ]
        self.assertEqual(
            int(self.prepared.arrays["sensor_positions"].shape[0]), 2020
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

    def test_clean_model_and_materials_are_resolved(self):
        self.assertEqual(self.prepared.validation_warnings, ())
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
        self.assertEqual(len(glass), 2)
        by_identifier = {item["identifier"]: item for item in glass}
        exterior = by_identifier["generic_exterior_window_vis_0.64"]
        interior = by_identifier["generic_interior_window_vis_0.88"]
        np.testing.assert_allclose(
            exterior["radiance_transmissivity_rgb"],
            [0.697576182] * 3,
            atol=1e-6,
            rtol=0,
        )
        np.testing.assert_allclose(
            exterior["solver_transmittance_rgb"], [0.64] * 3, atol=1e-6, rtol=0
        )
        np.testing.assert_allclose(
            interior["solver_transmittance_rgb"], [0.88] * 3, atol=1e-6, rtol=0
        )
        self.assertEqual(
            len(self.prepared.geometry_info["material_fingerprint"]), 64
        )
        self.assertEqual(
            self.prepared.geometry_info["aperture_mode"], "thin_glass"
        )
        pairs = self.prepared.geometry_info["surface_aperture_pairs"]
        self.assertEqual(len(pairs), 1)
        self.assertEqual(
            set(pairs[0]["aperture_identifiers"]),
            {"Ajd_Aperture_0abbf8bb", "Aperture_0abbf8bb"},
        )
        self.assertEqual(
            pairs[0]["modifiers"], ["generic_interior_window_vis_0.88"] * 2
        )
        self.assertEqual(
            pairs[0]["exported_aperture_identifier"],
            "Ajd_Aperture_0abbf8bb",
        )
        self.assertEqual(
            self.prepared.geometry_info["shifted_surface_face_identifiers"],
            [
                "office_02_19089ea1..Face4",
                "office_02_19089ea1..Face6",
            ],
        )
        self.assertAlmostEqual(
            self.prepared.geometry_info["surface_face_offset_m"], -0.02
        )

    def test_classroom_grid_belongs_only_to_sealed_room(self):
        classroom = next(
            info
            for info in self.prepared.grid_info
            if info["identifier"] == "classroom_01"
        )
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

    def test_near_corner_secondary_ray_does_not_escape_classroom(self):
        arrays = self.prepared.arrays
        classroom = next(
            info
            for info in self.prepared.grid_info
            if info["identifier"] == "classroom_01"
        )
        sensor_index = int(classroom["start_sensor_index"])
        engine = Engine({"backend": "reference"})
        scene = engine.create_scene(
            arrays["vertices"],
            arrays["triangles"],
            arrays["triangle_materials"],
            arrays["mesh_ranges"],
            arrays["instance_transforms"],
            arrays["instance_mesh_indices"],
            arrays["instance_room_ids"],
            arrays["instance_masks"],
            arrays["material_kinds"],
            arrays["material_diffuse_rgb"],
            arrays["material_transmittance_rgb"],
            arrays["sensor_positions"][sensor_index : sensor_index + 1],
            arrays["sensor_normals"][sensor_index : sensor_index + 1],
            arrays["sensor_ids"][sensor_index : sensor_index + 1],
            arrays["sensor_room_ids"][sensor_index : sensor_index + 1],
            arrays["sensor_area_weights"][sensor_index : sensor_index + 1],
        )
        result = scene.analyze(
            np.zeros((146, 1, 3), dtype=np.float32),
            np.ones(1, dtype=np.float32),
            quality="final",
            direct_samples=64,
            maximum_samples=470,
            maximum_bounces=1,
            scene_seed=0,
            export_coefficients=True,
        ).result()
        self.assertEqual(
            int(np.count_nonzero(result.coefficients())),
            0,
        )


if __name__ == "__main__":
    unittest.main()
