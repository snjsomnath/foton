from __future__ import annotations

import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
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
        return {
            "run_id": "test-run",
            "recorded_at_utc": "2026-07-31 12:00:00Z",
            "host": {
                "hostname": "gpu-host",
                "system": "Linux",
                "release": "6.0",
                "model": "Workstation",
                "cpu": "Test CPU",
                "cpu_count": 16,
                "memory": "64 GiB",
                "gpu": "Test GPU",
            },
            "engine": {"selected_backend": "vulkan", "version": "0.1.0"},
            "direct_visibility": {
                "comparison": {
                    "mismatch_count": 3,
                    "weighted_visible_energy_relative_error": 0.00125,
                },
                "metadata": {"sensor_count": 216, "sky_patch_count": 146},
                "engine": {
                    "timings_ms": {
                        "acceleration_structure_ms": 1.0,
                        "tracing_ms": 2.0,
                        "annual_reduction_ms": 0.1,
                    }
                },
                "radiance": {"elapsed_ms": 50.0},
            },
            "full_transport": {
                "samples": 4096,
                "bounces": 2,
                "comparison": {
                    "shape": [216, 146, 3],
                    "nmbe_percent": -0.5,
                    "cvrmse_percent": 1.25,
                },
                "engine": {
                    "transport_backend": "vulkan",
                    "wall_clock_ms": 20.0,
                    "timings_ms": {
                        "acceleration_structure_ms": 1.0,
                        "tracing_ms": 12.5,
                        "annual_reduction_ms": 3.0,
                    },
                },
                "radiance": {"elapsed_ms": 100.0},
                "annual": {
                    "timestep_count": 8760,
                    "radiance_total_ms": 125.0,
                    "illuminance_comparison": {
                        "nmbe_percent": -0.25,
                        "cvrmse_percent": 2.0,
                    },
                    "metric_differences": {
                        "static_sda_300_50_percentage_points": 1.5
                    },
                },
            },
            "large_scene": {
                "rooms": 1000,
                "sensor_count": 25000,
                "samples": 64,
                "bounces": 1,
                "first_run": {
                    "wall_clock_ms": 250.0,
                    "timings_ms": {
                        "acceleration_structure_ms": 20.0,
                        "tracing_ms": 200.0,
                        "annual_reduction_ms": 5.0,
                    },
                },
                "scene_commit_ms": 15.0,
                "resident_scene_reuse": {
                    "wall_clock_ms": 180.0,
                    "timings_ms": {
                        "acceleration_structure_ms": 0.0,
                        "tracing_ms": 130.0,
                        "annual_reduction_ms": 4.0,
                    },
                },
                "radiance": {
                    "cold_wall_clock_ms": 5000.0,
                    "cached_wall_clock_ms": 4000.0,
                },
            },
        }

    def test_readme_rows_include_hardware_scale_and_accuracy(self):
        report = self._report()
        hardware = self.benchmark.hardware_readme_row(report)
        rows = self.benchmark.benchmark_readme_rows(report)
        self.assertIn("| Test GPU | vulkan |", hardware)
        self.assertEqual(len(rows), 5)
        self.assertIn("0.125% energy", rows[0])
        self.assertIn("NMBE -0.500%", rows[1])
        self.assertIn("8760 hours", rows[2])
        self.assertIn("125.00 ms", rows[2])
        self.assertIn("1000 rooms / 25000 sensors", rows[3])
        self.assertIn("15.00 ms", rows[3])
        self.assertIn("5000.00 ms", rows[3])
        self.assertIn("resident BLAS/TLAS reuse", rows[4])
        self.assertIn("4000.00 ms", rows[4])

    def test_append_readme_row_uses_markers_and_avoids_duplicates(self):
        with TemporaryDirectory() as folder:
            readme = Path(folder) / "README.md"
            readme.write_text(
                "before\n"
                f"{self.benchmark.README_TABLE_START}\n"
                f"{self.benchmark.README_TABLE_HEADER}\n"
                f"{self.benchmark.README_TABLE_END}\n"
                "after\n",
                encoding="utf-8",
            )
            row = "| sample |"
            self.assertTrue(self.benchmark.append_readme_row(readme, row))
            self.assertFalse(self.benchmark.append_readme_row(readme, row))
            text = readme.read_text(encoding="utf-8")
        self.assertEqual(text.count(row), 1)
        self.assertLess(text.index(row), text.index(self.benchmark.README_TABLE_END))

    def test_radiance_preflight_explains_how_to_configure_binaries(self):
        with patch.object(
            self.benchmark,
            "resolve_radiance_executables",
            side_effect=FileNotFoundError("not found"),
        ):
            with self.assertRaisesRegex(RuntimeError, "brew install radiance"):
                self.benchmark._require_radiance(None)

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
