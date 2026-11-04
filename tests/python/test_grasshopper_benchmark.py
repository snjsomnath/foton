from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


def _benchmark_module():
    path = Path(__file__).parents[2] / "scripts" / "benchmark_grasshopper.py"
    spec = importlib.util.spec_from_file_location("benchmark_grasshopper", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class GrasshopperBenchmarkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.benchmark = _benchmark_module()

    def test_report_has_one_row_per_stage_and_column_per_scene(self):
        keys = [key for key, _ in self.benchmark.STAGES]
        keys += ["component_total", "honeybee_loader", "round_trip_total"]
        case = {
            "scene": "acceptance",
            "sensors": 2020,
            "output_megabytes": 37.7,
            "median_seconds": dict.fromkeys(keys, 0.25),
        }
        report = {
            "recorded_at_utc": "2026-11-03 12:00:00Z",
            "host": {"model": "Workstation", "cpu": "Test CPU", "memory": "64 GiB", "gpu": "Test GPU"},
            "engine": {"selected_backend": "vulkan", "version": "0.3.0"},
            "weather": "gothenburg.epw",
            "repeats": 3,
            "cases": [case, {**case, "scene": "office_floors", "sensors": 9216}],
        }
        markdown = self.benchmark.report_markdown(report)
        self.assertIn("| acceptance (2020 sensors) | office_floors (9216 sensors) |", markdown)
        self.assertIn("| Result writing | 0.250 | 0.250 |", markdown)
        self.assertIn("| Output folder size (MB) | 37.7 | 37.7 |", markdown)

    def test_event_time_returns_first_matching_stage(self):
        events = [(1.0, {"stage": "preparation"}), (2.0, {"stage": "weather"}), (3.0, {"stage": "weather"})]
        self.assertEqual(self.benchmark._event_time(events, self.benchmark._stage("weather")), 2.0)
        with self.assertRaises(RuntimeError):
            self.benchmark._event_time(events, self.benchmark._stage("output"))


if __name__ == "__main__":
    unittest.main()
