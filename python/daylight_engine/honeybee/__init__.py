"""Honeybee compatibility API for Foton recipes."""

from .annual import (
    AnnualDaylightRun,
    GridAnnualResult,
    HoneybeeStudy,
    honeybee_schedule,
    run_annual_daylight,
)
from .recipe import Recipe
from .protocol import PROTOCOL_NAME, PROTOCOL_VERSION
from .settings import RecipeSettings
from .validation import (
    compare_annual_daylight,
    compare_coefficient_repeatability,
    compare_coefficient_convergence,
    compare_coefficient_stages,
    compare_converged_annual,
    verify_official_annual_daylight_loader,
)

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
