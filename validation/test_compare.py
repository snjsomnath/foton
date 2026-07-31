import unittest

import numpy as np

from compare import error_metrics


class ErrorMetricTests(unittest.TestCase):
    def test_identical_arrays_have_zero_error(self):
        metrics = error_metrics(np.array([100.0, 200.0]), np.array([100.0, 200.0]))
        self.assertEqual(metrics["nmbe_percent"], 0.0)
        self.assertEqual(metrics["cv_rmse_percent"], 0.0)

    def test_known_bias_and_rmse(self):
        metrics = error_metrics(np.array([100.0, 100.0]), np.array([90.0, 110.0]))
        self.assertAlmostEqual(metrics["nmbe_percent"], 0.0)
        self.assertAlmostEqual(metrics["cv_rmse_percent"], 10.0)


if __name__ == "__main__":
    unittest.main()

