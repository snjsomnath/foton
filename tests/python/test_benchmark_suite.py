from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).parents[2] / "scripts"


def _module(name):
    sys.path.insert(0, str(SCRIPTS))
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


HOST = {
    "system": "Linux",
    "release": "6.6",
    "machine": "x86_64",
    "model": "Workstation",
    "model_identifier": None,
    "cpu": "Test CPU",
    "cpu_count": 16,
    "memory": "64.0 GiB",
    "gpu": "Test GPU",
    "python": "3.13.0",
}


def _result(machine_id, recorded, commit="a" * 40, quick=False, gpu="Test GPU"):
    return {
        "recorded_at_utc": recorded,
        "quick": quick,
        "fingerprint": {
            "machine_id": machine_id,
            "model_name": "Workstation",
            "hardware": {"model": "Workstation", "cpu": "Test CPU", "memory": "64 GiB"},
            "gpu": {"name": gpu, "driver": "580.82"},
            "os": "Linux 6.6",
            "backend": "vulkan",
            "foton": {"version": "0.3.1", "commit": commit, "dirty": False},
        },
        "annual": {"cases": [{"scene": "acceptance", "wall_seconds": {"median": 1.5}}]},
        "grasshopper": {
            "cases": [{"scene": "acceptance", "median_seconds": {"round_trip_total": 2.25}}]
        },
    }


class BenchmarkSuiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.suite = _module("benchmark_suite")
        cls.compare = _module("compare_benchmarks")

    def _fingerprint(self, **changes):
        engine = {"selected_backend": "vulkan", "version": "0.3.1"}
        gpu = {"vendor": "NVIDIA", "driver": changes.pop("driver", "580.82")}
        with patch.object(self.suite, "_gpu_details", return_value=gpu), patch.object(
            self.suite, "_git_commit", return_value={"commit": "abc", "dirty": False}
        ):
            return self.suite.machine_fingerprint({**HOST, **changes}, engine)

    def test_machine_id_depends_on_hardware_only(self):
        base = self._fingerprint()
        self.assertTrue(base["machine_id"].startswith("test-cpu-test-gpu-"))
        self.assertEqual(base["machine_id"], self._fingerprint(release="6.8", driver="590.1")["machine_id"])
        self.assertNotEqual(base["machine_id"], self._fingerprint(gpu="Other GPU")["machine_id"])

    def test_comparison_keeps_newest_full_run_per_machine_and_commit(self):
        with TemporaryDirectory() as folder:
            for name, result in {
                "one/old.json": _result("one", "2026-11-01 10:00:00Z"),
                "one/new.json": _result("one", "2026-11-02 10:00:00Z"),
                "one/smoke.json": _result("one", "2026-11-03 10:00:00Z", quick=True),
                "two/run.json": _result("two", "2026-11-02 10:00:00Z", gpu="Tesla T4"),
            }.items():
                path = Path(folder) / name
                path.parent.mkdir(exist_ok=True)
                path.write_text(json.dumps(result))
            results = self.compare.newest_per_machine(self.compare.load_results(folder))
        self.assertEqual(sorted(r["recorded_at_utc"] for r in results), ["2026-11-02 10:00:00Z"] * 2)
        table = self.compare.comparison_markdown(results)
        self.assertIn("Annual: acceptance", table)
        self.assertIn("Round trip: acceptance", table)
        self.assertIn("| Tesla T4, driver 580.82 | vulkan |", table)
        self.assertIn("0.3.1 `aaaaaaa` | 2026-11-02 | 1.50 | 2.25 |", table)


if __name__ == "__main__":
    unittest.main()
