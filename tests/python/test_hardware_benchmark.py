from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch


def _benchmark_module():
    path = Path(__file__).parents[2] / "scripts" / "benchmark_hardware.py"
    spec = importlib.util.spec_from_file_location("benchmark_hardware", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class HardwareBenchmarkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.benchmark = _benchmark_module()

    def _report(self):
        timing = {"median": 1.5, "minimum": 1.4, "maximum": 1.6, "values": [1.5]}
        return {
            "recorded_at_utc": "2026-11-03 12:00:00Z",
            "host": {
                "model": "Workstation",
                "cpu": "Test CPU",
                "memory": "64 GiB",
                "gpu": "Test GPU",
            },
            "engine": {"selected_backend": "vulkan", "version": "0.3.0"},
            "settings": {"direct_samples": 256, "maximum_bounces": 8},
            "weather": "gothenburg.epw",
            "repeats": 5,
            "cases": [
                {
                    "scene": "acceptance",
                    "rooms": 3,
                    "sensors": 2020,
                    "wall_seconds": timing,
                    "tracing_seconds": {**timing, "median": 1.25},
                }
            ],
        }

    def test_report_lists_settings_and_median_timings(self):
        markdown = self.benchmark.report_markdown(self._report())
        self.assertIn("Test GPU / `vulkan`", markdown)
        self.assertIn('"maximum_bounces": 8', markdown)
        self.assertIn("| acceptance | 3 | 2020 | 1.50 s | 1.25 s |", markdown)

    def test_office_floors_gives_every_room_a_glazed_facade_and_grid(self):
        try:
            model = self.benchmark.office_floors_model(floors=2, rooms_per_facade=3)
        except ImportError:
            self.skipTest("honeybee is not installed")
        self.assertEqual(len(model.rooms), 12)
        self.assertTrue(all(len(room.apertures) == 1 for room in model.rooms))
        grids = model.properties.radiance.sensor_grids
        self.assertEqual(len(grids), 12)
        self.assertEqual(sum(len(grid.sensors) for grid in grids), 12 * 36)

    def test_unknown_scene_is_reported_by_name(self):
        with self.assertRaisesRegex(FileNotFoundError, "no_such_scene"):
            self.benchmark._model_path("no_such_scene", None, Path("."))

    def test_dependency_preflight_identifies_the_active_interpreter(self):
        with patch.object(
            self.benchmark.importlib.util,
            "find_spec",
            return_value=None,
        ):
            with self.assertRaisesRegex(
                RuntimeError,
                "repository virtualenv",
            ) as error:
                self.benchmark._require_python_dependencies()
        self.assertIn(self.benchmark.sys.executable, str(error.exception))
        self.assertIn("honeybee_radiance", str(error.exception))


if __name__ == "__main__":
    unittest.main()
