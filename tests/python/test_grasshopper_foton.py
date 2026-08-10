from __future__ import annotations

import ast
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from foton.honeybee.protocol import annual_request
from grasshopper_foton import foton_gh


ROOT = Path(__file__).resolve().parents[2]


def write_metric_manifest(root, request=None):
    root = Path(root)
    results = root / "results"
    results.mkdir(parents=True, exist_ok=True)
    grids = []
    for index, (identifier, count) in enumerate((('first', 2), ('second', 1))):
        paths = {}
        for metric in foton_gh.METRICS:
            extension = "da" if metric == "da" else "cda" if metric == "cda" else "udi"
            path = root / "metrics" / metric / f"{identifier}.{extension}"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("\n".join(str(index + value) for value in range(count)) + "\n")
            paths[metric] = str(path)
        grids.append(
            {
                "identifier": identifier,
                "full_identifier": identifier,
                "room_identifier": f"room-{index}",
                "sensor_count": count,
                "sda": 50.0 + index,
                "metrics": paths,
            }
        )
    manifest_path = root / "run_manifest.json"
    manifest = {
        "protocol": foton_gh.PROTOCOL_NAME,
        "protocol_version": foton_gh.PROTOCOL_VERSION,
        "status": "complete",
        "output_folder": str(root),
        "results_folder": str(results),
        "manifest": str(manifest_path),
        "grids": grids,
        "timings": {"total_seconds": 1.0},
        "warnings": [],
        "request": request or {},
    }
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    return manifest


class GrasshopperFotonTests(unittest.TestCase):
    def test_fingerprint_is_path_independent_and_matches_native_protocol(self):
        with TemporaryDirectory() as folder:
            first = Path(folder, "first")
            second = Path(folder, "second")
            first.mkdir()
            second.mkdir()
            for root in (first, second):
                Path(root, "model.hbjson").write_text("model", encoding="utf-8")
                Path(root, "weather.epw").write_text("weather", encoding="utf-8")
            native_first = annual_request(
                model=first / "model.hbjson", wea=first / "weather.epw"
            )
            native_second = annual_request(
                model=second / "model.hbjson", wea=second / "weather.epw"
            )
            ironpython = foton_gh.request_data(
                str(second / "model.hbjson"), str(second / "weather.epw")
            )
        self.assertEqual(native_first["fingerprint"], native_second["fingerprint"])
        self.assertEqual(native_first["fingerprint"], ironpython["fingerprint"])

    def test_honeybee_threshold_and_north_semantics(self):
        self.assertEqual(
            foton_gh.thresholds("-ut 2000 -t 250 -lt 50"),
            {"threshold": 250.0, "udi_lower": 50.0, "udi_upper": 2000.0},
        )
        vector = type("Vector", (), {"X": -1.0, "Y": 0.0})()
        self.assertAlmostEqual(foton_gh.north_angle(vector), 90.0)

    def test_result_bundle_preserves_grid_branches(self):
        with TemporaryDirectory() as folder:
            write_metric_manifest(folder)
            bundle = foton_gh.load_result_bundle(folder)
        self.assertEqual(bundle["grid_ids"], ["first", "second"])
        self.assertEqual(bundle["room_ids"], ["room-0", "room-1"])
        self.assertEqual(bundle["da"], [[0.0, 1.0], [1.0]])
        self.assertEqual(bundle["sda"], [50.0, 51.0])
        self.assertEqual(len(bundle["results"]), 1)

    def test_compatible_run_is_reused_without_starting_process(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            model = root / "model.hbjson"
            weather = root / "weather.epw"
            executable = root / "foton-honeybee"
            model.write_text("model", encoding="utf-8")
            weather.write_text("weather", encoding="utf-8")
            executable.write_text("executable", encoding="utf-8")
            request = foton_gh.request_data(str(model), str(weather))
            output = root / "output"
            write_metric_manifest(output, request=request)
            with patch("grasshopper_foton.foton_gh._run_process") as process:
                bundle = foton_gh.run_annual_daylight(
                    str(model),
                    str(weather),
                    str(output),
                    executable=str(executable),
                    reuse=True,
                )
        process.assert_not_called()
        self.assertTrue(bundle["manifest"]["grasshopper_reused"])

    def test_new_run_invokes_executable_directly_and_exports_raw_results(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            model = root / "model.hbjson"
            weather = root / "weather.epw"
            executable = root / "foton-honeybee"
            model.write_text("model", encoding="utf-8")
            weather.write_text("weather", encoding="utf-8")
            executable.write_text("executable", encoding="utf-8")
            commands = []

            def completed(command, progress=None, cancel=None):
                commands.append(command)
                output = Path(command[command.index("--output") + 1])
                return write_metric_manifest(output)

            with patch("grasshopper_foton.foton_gh._run_process", side_effect=completed):
                bundle = foton_gh.run_annual_daylight(
                    str(model),
                    str(weather),
                    str(root / "output"),
                    executable=str(executable),
                    reuse=False,
                )
        command = commands[0]
        self.assertEqual(Path(command[0]).resolve(), executable.resolve())
        self.assertEqual(command[1:3], ["annual-daylight", "--jsonl"])
        self.assertIn("--export-illuminance", command)
        self.assertNotIn("python", [item.lower() for item in command])
        self.assertEqual(bundle["grid_ids"], ["first", "second"])

    def test_component_sources_are_python_2_compatible_in_style(self):
        components = ROOT / "grasshopper_foton" / "components"
        sources = list(components.glob("*.py"))
        self.assertEqual(len(sources), 3)
        for path in sources:
            source = path.read_text(encoding="utf-8")
            ast.parse(source, filename=str(path))
            self.assertNotIn("from pathlib", source)
            self.assertNotIn("subprocess", source)
            self.assertNotRegex(source, r"(^|[^A-Za-z])f['\"]")


if __name__ == "__main__":
    unittest.main()
