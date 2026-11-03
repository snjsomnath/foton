from __future__ import annotations

import asyncio
import json
import numpy as np
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import Mock

from foton.viewer.app import create_app
from daylight_engine.viewer.demo_geometry import DemoParameters, generate_demo_scene

ROOT = Path(__file__).resolve().parents[2]


async def request(app, method, path):
    messages = []
    finished = asyncio.Event()
    delivered = False

    async def receive():
        nonlocal delivered
        if not delivered:
            delivered = True
            return {"type": "http.request", "body": b"", "more_body": False}
        # Behave like a real client: disconnect only once the response is
        # complete. Starlette 1.10 listens for the disconnect while it streams
        # a file, and a receive() that kept answering with the request would
        # spin that listener forever (the Python 3.13 CI jobs hung on this).
        await finished.wait()
        return {"type": "http.disconnect"}

    async def send(message):
        messages.append(message)
        if message["type"] == "http.response.body" and not message.get("more_body", False):
            finished.set()

    async with app.router.lifespan_context(app):
        await app({
            "type": "http", "asgi": {"version": "3.0"}, "http_version": "1.1",
            "method": method, "scheme": "http", "path": path,
            "raw_path": path.encode(), "query_string": b"", "root_path": "",
            "headers": [], "server": ("127.0.0.1", 8000), "client": ("127.0.0.1", 12345),
        }, receive, send)
    status = next(message["status"] for message in messages if message["type"] == "http.response.start")
    body = b"".join(message.get("body", b"") for message in messages if message["type"] == "http.response.body")
    return status, body.decode()


class ViewerDemoTests(unittest.IsolatedAsyncioTestCase):
    def test_every_scripted_room_is_valid(self):
        storyboard = json.loads((ROOT / "viewer/src/demo/storyboard.json").read_text())
        for shot in storyboard:
            with self.subTest(shot=shot["detail"]):
                parameters = DemoParameters(**shot["parameters"])
                scene = generate_demo_scene(parameters)
                self.assertGreater(len(scene.geometry_payload["sensor_ids"]), 0)
                if shot.get("overview"):
                    vertices = np.asarray(scene.geometry_payload["vertices"])
                    np.testing.assert_allclose(shot["overview"]["from"], [vertices.min(axis=0), vertices.max(axis=0)], atol=1e-5)
        self.assertAlmostEqual(sum(shot["duration"] for shot in storyboard), 72)

    async def test_demo_weather_uses_fixed_asset_and_existing_weather_store(self):
        store = Mock()
        store.ingest.return_value.summary.return_value = {"weather_id": "test", "annual_metrics_available": True}
        with TemporaryDirectory() as directory:
            path = Path(directory) / "gothenburg.epw"
            path.write_bytes(b"local-weather")
            app = create_app(engine_factory=Mock, weather_store=store, demo_weather_path=path)
            status, body = await request(app, "POST", "/api/demo/weather")
            self.assertEqual(status, 200)
            self.assertEqual(json.loads(body)["weather_id"], "test")
            store.ingest.assert_called_once_with(b"local-weather", "gothenburg.epw", 0.0)

    async def test_missing_asset_and_converter_report_actionable_setup_errors(self):
        store = Mock()
        with TemporaryDirectory() as directory:
            path = Path(directory) / "gothenburg.epw"
            app = create_app(engine_factory=Mock, weather_store=store, demo_weather_path=path)
            status, body = await request(app, "POST", "/api/demo/weather")
            self.assertEqual(status, 503)
            self.assertIn("epw/gothenburg.epw", json.loads(body)["detail"])
            store.ingest.assert_not_called()
            path.write_bytes(b"weather")
            store.ingest.side_effect = RuntimeError("gendaymtx is unavailable; install Radiance or set RADIANCE_BIN")
            status, body = await request(app, "POST", "/api/demo/weather")
            self.assertEqual(status, 503)
            self.assertIn("RADIANCE_BIN", json.loads(body)["detail"])

    async def test_both_built_frontend_entries_are_served(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.html").write_text("original viewer")
            (root / "demo.html").write_text("cinematic viewer")
            app = create_app(engine_factory=Mock, weather_store=Mock(), frontend_directory=root)
            self.assertEqual(await request(app, "GET", "/"), (200, "original viewer"))
            self.assertEqual(await request(app, "GET", "/demo.html"), (200, "cinematic viewer"))


if __name__ == "__main__":
    unittest.main()
