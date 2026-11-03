from __future__ import annotations

import unittest

import numpy as np

from foton.honeybee.annual import DEFAULT_MAXIMUM_BOUNCES, QUALITY_PRESETS, quality_preset
from foton.honeybee.validation import (
    DARK_GRID_MAXIMUM_LUX,
    DARK_GRID_MEAN_LUX,
    _physically_dark,
)


class QualityPresetTests(unittest.TestCase):
    def test_final_budget_scales_with_patch_count(self):
        mf1 = quality_preset("final", 1)
        mf2 = quality_preset("final", 2)
        self.assertEqual(mf1, QUALITY_PRESETS["final"])
        self.assertEqual(mf2["direct_samples"], mf1["direct_samples"])
        # Four times the sky patches, four times the shared indirect budget.
        self.assertEqual(mf2["maximum_samples"], 4 * mf1["maximum_samples"])
        self.assertEqual(mf1["maximum_samples"], 65536)
        self.assertEqual(mf2["maximum_samples"], 262144)

    def test_preview_scales_too_and_returns_a_copy(self):
        preview = quality_preset("preview", 2)
        self.assertEqual(preview["maximum_samples"], 4 * QUALITY_PRESETS["preview"]["maximum_samples"])
        preview["maximum_samples"] = 0
        self.assertEqual(QUALITY_PRESETS["preview"]["maximum_samples"], 64)

    def test_rejects_unknown_quality_and_bad_density(self):
        with self.assertRaises(ValueError):
            quality_preset("draft", 1)
        with self.assertRaises(ValueError):
            quality_preset("final", 0)
        with self.assertRaises(ValueError):
            quality_preset("final", True)

    def test_viewer_final_pass_uses_the_mf2_budget(self):
        from daylight_engine.viewer import session

        source = open(session.__file__, encoding="utf-8").read()
        self.assertIn('quality_preset("final", 2)', source)
        self.assertIn("DEFAULT_MAXIMUM_BOUNCES", source)
        self.assertEqual(DEFAULT_MAXIMUM_BOUNCES, 8)


class PhysicallyDarkGridTests(unittest.TestCase):
    def test_radiance_leak_in_a_windowless_room_counts_as_dark(self):
        reference = np.zeros((175, 4000))
        reference[52, 1200] = 1.84  # one hour of leakage through coincident faces
        reference[10:20, :] = 0.003
        candidate = np.zeros_like(reference)
        self.assertTrue(_physically_dark(reference, candidate))

    def test_a_dim_but_lit_room_is_not_dark(self):
        reference = np.full((36, 4000), 1.5)  # a deep borrowed-light room
        candidate = reference * 0.97
        self.assertFalse(_physically_dark(reference, candidate))
        reference = np.zeros((36, 4000))
        reference[0, 0] = DARK_GRID_MAXIMUM_LUX + 1  # a real patch of light somewhere
        self.assertFalse(_physically_dark(reference, np.zeros_like(reference)))

    def test_candidate_light_in_a_dark_reference_is_not_dark(self):
        reference = np.zeros((36, 4000))
        candidate = np.full((36, 4000), DARK_GRID_MEAN_LUX * 3)
        self.assertFalse(_physically_dark(reference, candidate))


if __name__ == "__main__":
    unittest.main()
