import json
import unittest
from unittest.mock import Mock
import numpy as np
from daylight_engine.viewer.solar import solar_diagram
from daylight_engine.viewer.app import create_app
from test_viewer_demo import request


class SolarTests(unittest.IsolatedAsyncioTestCase):
    def test_solar_paths_use_weather_midpoints_and_location(self):
        diagram = solar_diagram(57.663, 12.28, 1)
        hourly = np.asarray(diagram['hourly'])
        self.assertEqual(hourly.shape, (8760,5))
        np.testing.assert_allclose(np.linalg.norm(hourly[:,:3],axis=1), 1, atol=1e-6)
        self.assertAlmostEqual(hourly[4116,3], 55.641, places=2)
        self.assertAlmostEqual(hourly[4116,4], 187.033, places=2)
        self.assertLess(hourly[0,2], 0)
        self.assertEqual(len(diagram['monthly_paths']), 12)
        self.assertEqual(len(diagram['analemmas'][2]), 365)
        self.assertEqual(diagram['month_timesteps'][5], 4116)
        self.assertIn('midpoint', diagram['time_convention'])

    async def test_route_uses_loaded_epw_location(self):
        store = Mock()
        store.get.return_value.location = {'latitude':57.663,'longitude':12.28,'time_zone':1}
        store.get.return_value.north_rotation_degrees = 0
        status, body = await request(create_app(engine_factory=Mock,weather_store=store), 'GET', '/api/demo/solar/epw-id')
        self.assertEqual(status,200)
        self.assertEqual(len(json.loads(body)['hourly']),8760)
        store.get.assert_called_with('epw-id')

    async def test_route_rejects_missing_weather_location(self):
        store = Mock()
        store.get.return_value.location = {}
        status, body = await request(create_app(engine_factory=Mock,weather_store=store), 'GET', '/api/demo/solar/missing')
        self.assertEqual(status,400)
        self.assertIn('location',body)
