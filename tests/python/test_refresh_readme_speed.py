from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest

SCRIPTS = Path(__file__).parents[2] / "scripts"


def _module():
    sys.path.insert(0, str(SCRIPTS))
    path = SCRIPTS / "refresh_readme_speed.py"
    spec = importlib.util.spec_from_file_location("refresh_readme_speed", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def _result(recorded="2026-11-04 08:00:00Z", machine="test-gpu-12345678"):
    return {
        "recorded_at_utc": recorded,
        "fingerprint": {
            "machine_id": machine,
            "model_name": "Workstation",
            "hardware": {"cpu": "AMD Ryzen 9", "memory": "64 GiB"},
            "gpu": {"name": "NVIDIA RTX 4090"},
            "backend": "vulkan",
            "foton": {"version": "0.3.1", "commit": "abcdef0123", "dirty": False},
        },
        "annual": {
            "quality": "final",
            "settings": {"maximum_bounces": 8, "direct_samples": 256, "maximum_samples": 65536},
            "weather": "gothenburg.epw",
            "repeats": 5,
            "cases": [
                {"scene": "acceptance", "rooms": 3, "sensors": 2020, "wall_seconds": {"median": 0.5}},
                {"scene": "office_floors", "rooms": 256, "sensors": 9216, "wall_seconds": {"median": 2.0}},
            ],
        },
        "grasshopper": {
            "repeats": 3,
            "cases": [{"scene": "acceptance", "median_seconds": {"round_trip_total": 0.75}}],
        },
    }


class RefreshReadmeSpeedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.refresh = _module()

    def test_block_states_date_machine_settings_and_times(self):
        path = self.refresh.ROOT / "benchmarks/machines/test-gpu-12345678/20261104T080000Z.json"
        block = self.refresh.speed_block(_result(), path)
        self.assertIn(
            "Measured on 4 November 2026 on a Workstation (AMD Ryzen 9, 64 GiB, NVIDIA RTX 4090), "
            "using Vulkan and Foton 0.3.1 (commit `abcdef0`)",
            block,
        )
        self.assertIn("8 bounces, 256 direct and 65,536 indirect samples", block)
        self.assertIn("| Acceptance model | 3 | 2,020 | 0.50 s | 0.75 s |", block)
        self.assertIn("| Four-storey office block | 256 | 9,216 | 2.00 s | – |", block)
        self.assertIn("benchmarks/machines/test-gpu-12345678/20261104T080000Z.json", block)

    def test_only_the_marked_block_is_replaced(self):
        text = f"intro\n{self.refresh.START}\nold\n{self.refresh.END}\noutro\n"
        updated = self.refresh.replace_block(text, f"{self.refresh.START}\nnew\n{self.refresh.END}")
        self.assertEqual(updated, f"intro\n{self.refresh.START}\nnew\n{self.refresh.END}\noutro\n")
        with self.assertRaises(SystemExit):
            self.refresh.replace_block("no markers", "block")

    def test_newest_result_wins_unless_a_machine_is_named(self):
        older, newer = _result("2026-11-01 08:00:00Z", "a"), _result("2026-11-02 08:00:00Z", "b")
        self.assertIs(self.refresh.select_result([older, newer]), newer)
        self.assertIs(self.refresh.select_result([older, newer], "a"), older)


    def test_default_selection_keeps_newest_run_per_machine_on_newest_version(self):
        old_mac = _result("2026-11-01 08:00:00Z", "mac")
        old_mac["fingerprint"]["foton"]["version"] = "0.3.0"
        new_mac = _result("2026-11-05 08:00:00Z", "mac")
        new_mac["fingerprint"]["foton"]["version"] = "0.3.10"
        l4 = _result("2026-11-05 09:00:00Z", "l4")
        l4["fingerprint"]["foton"]["version"] = "0.3.10"
        self.assertEqual(self.refresh.select_results([old_mac, new_mac, l4]), [new_mac, l4])
        self.assertEqual(self.refresh.select_results([old_mac, new_mac, l4], ["mac"]), [new_mac])

    def test_many_machines_get_one_column_each(self):
        mac, l4 = _result(machine="mac"), _result(machine="l4")
        mac["fingerprint"]["gpu"] = {"name": "Apple M4 Pro"}
        mac["fingerprint"]["backend"] = "metal"
        l4["fingerprint"]["gpu"] = {"name": "NVIDIA L4"}
        l4["grasshopper"] = None
        l4["annual"]["cases"][0]["wall_seconds"] = {"median": 0.25}
        root = self.refresh.ROOT / "benchmarks/machines"
        block = self.refresh.speed_block_many([(mac, root / "mac/a.json"), (l4, root / "l4/b.json")])
        self.assertIn("on 2 machines: Apple M4 Pro (Metal) in a Workstation", block)
        self.assertIn("| Annual run | Rooms | Sensors | Apple M4 Pro (Metal) | NVIDIA L4 (Vulkan) |", block)
        self.assertIn("| Acceptance model | 3 | 2,020 | 0.50 s | 0.25 s |", block)
        self.assertIn("| Acceptance model | 3 | 2,020 | 0.75 s | – |", block)
        self.assertIn("benchmarks/machines/l4/b.json", block)

    def test_many_machines_must_share_settings(self):
        mac, l4 = _result(machine="mac"), _result(machine="l4")
        l4["annual"]["settings"] = {**l4["annual"]["settings"], "maximum_bounces": 2}
        root = self.refresh.ROOT / "benchmarks/machines"
        with self.assertRaises(SystemExit):
            self.refresh.speed_block_many([(mac, root / "a.json"), (l4, root / "b.json")])

    def test_linux_machine_without_a_model_name_is_described_plainly(self):
        fingerprint = _result()["fingerprint"]
        fingerprint["model_name"] = "x86_64"
        fingerprint["hardware"].update(machine="x86_64", system="Linux")
        self.assertEqual(
            self.refresh._machine(fingerprint), "a Linux machine (AMD Ryzen 9, 64 GiB, NVIDIA RTX 4090)"
        )

    def test_hardware_names_are_tidied(self):
        self.assertEqual(self.refresh._tidy("Intel(R) Xeon(R) CPU @ 2.20GHz"), "Intel Xeon")
        self.assertEqual(
            self.refresh._tidy("NVIDIA RTX PRO 6000 Blackwell Server Edition"), "NVIDIA RTX PRO 6000 Blackwell"
        )

if __name__ == "__main__":
    unittest.main()
