"""Honeybee integration for Foton."""

import sys

from daylight_engine.honeybee import Recipe, RecipeSettings
from daylight_engine.honeybee import adapter, radiance, recipe, settings

sys.modules[f"{__name__}.adapter"] = adapter
sys.modules[f"{__name__}.radiance"] = radiance
sys.modules[f"{__name__}.recipe"] = recipe
sys.modules[f"{__name__}.settings"] = settings

__all__ = ["Recipe", "RecipeSettings"]
