"""Honeybee integration for Foton."""

import sys

from daylight_engine.honeybee import (
    AnnualDaylightRun,
    GridAnnualResult,
    HoneybeeStudy,
    Recipe,
    RecipeSettings,
    compare_annual_daylight,
    honeybee_schedule,
    run_annual_daylight,
)
from daylight_engine.honeybee import (
    adapter,
    annual,
    radiance,
    recipe,
    settings,
    validation,
    weather,
)

sys.modules[f"{__name__}.adapter"] = adapter
sys.modules[f"{__name__}.annual"] = annual
sys.modules[f"{__name__}.radiance"] = radiance
sys.modules[f"{__name__}.recipe"] = recipe
sys.modules[f"{__name__}.settings"] = settings
sys.modules[f"{__name__}.validation"] = validation
sys.modules[f"{__name__}.weather"] = weather

__all__ = [
    "AnnualDaylightRun",
    "GridAnnualResult",
    "HoneybeeStudy",
    "Recipe",
    "RecipeSettings",
    "honeybee_schedule",
    "compare_annual_daylight",
    "run_annual_daylight",
]
