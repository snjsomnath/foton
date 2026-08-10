"""Honeybee integration for Foton."""

import sys

from daylight_engine.honeybee import (
    AnnualDaylightRun,
    GridAnnualResult,
    HoneybeeStudy,
    Recipe,
    RecipeSettings,
    PROTOCOL_NAME,
    PROTOCOL_VERSION,
    compare_annual_daylight,
    compare_coefficient_repeatability,
    compare_coefficient_convergence,
    compare_coefficient_stages,
    compare_converged_annual,
    honeybee_schedule,
    run_annual_daylight,
    verify_official_annual_daylight_loader,
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
from daylight_engine.honeybee import protocol

sys.modules[f"{__name__}.adapter"] = adapter
sys.modules[f"{__name__}.annual"] = annual
sys.modules[f"{__name__}.radiance"] = radiance
sys.modules[f"{__name__}.recipe"] = recipe
sys.modules[f"{__name__}.settings"] = settings
sys.modules[f"{__name__}.validation"] = validation
sys.modules[f"{__name__}.weather"] = weather
sys.modules[f"{__name__}.protocol"] = protocol

__all__ = [
    "AnnualDaylightRun",
    "GridAnnualResult",
    "HoneybeeStudy",
    "Recipe",
    "RecipeSettings",
    "PROTOCOL_NAME",
    "PROTOCOL_VERSION",
    "honeybee_schedule",
    "compare_annual_daylight",
    "compare_coefficient_repeatability",
    "compare_coefficient_convergence",
    "compare_coefficient_stages",
    "compare_converged_annual",
    "verify_official_annual_daylight_loader",
    "run_annual_daylight",
]
