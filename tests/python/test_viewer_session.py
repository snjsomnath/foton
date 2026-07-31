from __future__ import annotations

import unittest

import numpy as np

from foton.viewer.session import selected_hour_illuminance


class ViewerSessionTests(unittest.TestCase):
    def test_selected_hour_uses_rgb_photopic_multiplication(self):
        coefficients = np.asarray(
            [
                [
                    [1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                ]
            ],
            dtype=np.float32,
        )
        sky = np.asarray(
            [
                [[2.0, 0.0, 0.0], [3.0, 0.0, 0.0]],
                [[0.0, 4.0, 0.0], [0.0, 5.0, 0.0]],
            ],
            dtype=np.float32,
        )
        lux = selected_hour_illuminance(coefficients, sky, 1)
        self.assertAlmostEqual(float(lux[0]), 3 * 47.435 + 5 * 119.93, places=3)

    def test_selected_hour_validates_dimensions_and_index(self):
        coefficients = np.ones((2, 146, 3), dtype=np.float32)
        sky = np.ones((146, 1, 3), dtype=np.float32)
        with self.assertRaises(ValueError):
            selected_hour_illuminance(coefficients, sky, 1)
        with self.assertRaises(ValueError):
            selected_hour_illuminance(coefficients[:, :145], sky, 0)


if __name__ == "__main__":
    unittest.main()
