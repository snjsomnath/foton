from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import threading
import unittest
from unittest.mock import patch

import numpy as np

from foton.honeybee.__main__ import main
from foton.honeybee.protocol import (
    PROTOCOL_NAME,
    PROTOCOL_VERSION,
    annual_request,
    parse_message,
)
from honeybee_foton import (
    AnnualDaylightRequest,
    FotonClient,
    FotonProcessCancelled,
    FotonProcessError,
    load_grid_result_branches,
)
from honeybee_foton.client import _resolve_output


class ProtocolTests(unittest.TestCase):
    def test_request_fingerprint_tracks_input_content(self):
        with TemporaryDirectory() as folder:
            model = Path(folder, "model.hbjson")
            weather = Path(folder, "weather.epw")
            model.write_text("first", encoding="utf-8")
            weather.write_text("weather", encoding="utf-8")
            first = annual_request(model=model, wea=weather)
            model.write_text("second", encoding="utf-8")
            second = annual_request(model=model, wea=weather)
        self.assertNotEqual(first["fingerprint"], second["fingerprint"])

    def test_message_parser_rejects_unknown_versions(self):
        with self.assertRaises(ValueError):
            parse_message(
                json.dumps(
                    {
                        "protocol": PROTOCOL_NAME,
                        "protocol_version": PROTOCOL_VERSION + 1,
                        "event": "progress",
                    }
                )
            )

    @patch("daylight_engine.honeybee.__main__.run_annual_daylight")
    def test_cli_jsonl_emits_progress_and_complete_manifest(self, run):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            model = root / "model.hbjson"
            weather = root / "weather.epw"
            output = root / "output"
            output.mkdir()
            model.write_text("model", encoding="utf-8")
            weather.write_text("weather", encoding="utf-8")
            grid = SimpleNamespace(
                identifier="grid",
                full_identifier="grid",
                room_identifier="room",
                sensor_count=1,
                sensor_indices=np.asarray([0]),
                sda=0.0,
            )
            run.return_value = SimpleNamespace(
                results_folder=output / "results",
                grids=(grid,),
                timings={"total_seconds": 1.0},
                metadata={
                    "weather": {"cache_hit": False},
                    "solver": {
                        "coefficient_cache_hit": False,
                        "solver_revision": "test",
                    },
                    "validation_warnings": [],
                },
            )
            stdout = StringIO()
            with redirect_stdout(stdout):
                code = main(
                    [
                        "annual-daylight",
                        "--jsonl",
                        "--model",
                        str(model),
                        "--wea",
                        str(weather),
                        "--output",
                        str(output),
                    ]
                )
            messages = [json.loads(line) for line in stdout.getvalue().splitlines()]
            manifest = json.loads((output / "run_manifest.json").read_text())
        self.assertEqual(code, 0)
        self.assertEqual([item["event"] for item in messages], ["started", "progress", "complete"])
        self.assertEqual(manifest["request"]["fingerprint"], messages[-1]["manifest"]["request"]["fingerprint"])

    def test_result_loader_preserves_grid_branches(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            grids = []
            for identifier, values in (("first", [1.0, 2.0]), ("second", [3.0])):
                metrics = {}
                for metric in ("da", "cda", "udi_lower", "udi", "udi_upper"):
                    path = root / f"{identifier}-{metric}.txt"
                    np.savetxt(path, values)
                    metrics[metric] = str(path)
                grids.append(
                    {
                        "identifier": identifier,
                        "full_identifier": identifier,
                        "room_identifier": f"{identifier}-room",
                        "sensor_count": len(values),
                        "sda": 50.0,
                        "metrics": metrics,
                    }
                )
            manifest = {
                "protocol": PROTOCOL_NAME,
                "protocol_version": PROTOCOL_VERSION,
                "status": "complete",
                "grids": grids,
            }
            branches = load_grid_result_branches(manifest)
        self.assertEqual(branches.identifiers, ("first", "second"))
        self.assertEqual(branches.da, ([1.0, 2.0], [3.0]))

    def test_bridge_command_has_no_python_runner(self):
        request = AnnualDaylightRequest(
            model="model.hbjson", wea="weather.epw", output_folder="results"
        )
        command = request.command("foton-honeybee", Path("results"))
        self.assertEqual(command[:3], ["foton-honeybee", "annual-daylight", "--jsonl"])
        self.assertNotIn("python", command)

    def test_bridge_uses_unique_output_folders(self):
        with TemporaryDirectory() as folder:
            output = Path(folder, "result")
            output.mkdir()
            request = AnnualDaylightRequest(
                model="model.hbjson",
                wea="weather.epw",
                output_folder=str(output),
            )
            self.assertEqual(
                _resolve_output(request, "unique"),
                output.with_name("result-001").resolve(),
            )

    def test_bridge_atomically_reserves_unique_output_folders(self):
        with TemporaryDirectory() as folder:
            output = Path(folder, "result")
            request = AnnualDaylightRequest(
                model="model.hbjson",
                wea="weather.epw",
                output_folder=str(output),
            )
            first = _resolve_output(request, "unique", reserve=True)
            second = _resolve_output(request, "unique", reserve=True)
            self.assertTrue(first.is_dir())
            self.assertTrue(second.is_dir())
            self.assertEqual(first, output.resolve())
            self.assertEqual(second, output.with_name("result-001").resolve())

    @patch("honeybee_foton.client.subprocess.Popen")
    def test_bridge_propagates_nonzero_process_failures(self, popen):
        process = popen.return_value
        process.stdout = iter(())
        process.stderr = iter(("failure detail\n",))
        process.poll.return_value = 1
        process.wait.return_value = 1
        with TemporaryDirectory() as folder:
            request = AnnualDaylightRequest(
                model="model.hbjson",
                wea="weather.epw",
                output_folder=str(Path(folder, "results")),
            )
            client = FotonClient(sys.executable)
            with self.assertRaisesRegex(FotonProcessError, "failure detail"):
                client.run_annual_daylight(request)

    @patch("honeybee_foton.client.subprocess.Popen")
    def test_bridge_cancellation_terminates_process(self, popen):
        process = popen.return_value
        process.stdout = iter(())
        process.stderr = iter(())
        process.poll.return_value = None
        process.wait.return_value = 0
        cancelled = threading.Event()
        cancelled.set()
        with TemporaryDirectory() as folder:
            request = AnnualDaylightRequest(
                model="model.hbjson",
                wea="weather.epw",
                output_folder=str(Path(folder, "results")),
            )
            client = FotonClient(sys.executable)
            with self.assertRaises(FotonProcessCancelled):
                client.run_annual_daylight(request, cancel_event=cancelled)
        process.terminate.assert_called_once()


if __name__ == "__main__":
    unittest.main()
