"""Rhino-independent controllers for the initial Grasshopper components.

The actual Grasshopper wrappers only need to map component inputs to these
controllers and convert each returned tuple entry to one DataTree branch.
"""

from __future__ import annotations

from dataclasses import dataclass

from .client import AnnualDaylightRequest, FotonClient
from .results import load_grid_result_branches, load_manifest


@dataclass(frozen=True)
class FotonSettings:
    executable: str | None = None
    backend: str = "auto"

    def capabilities(self):
        return FotonClient(self.executable).capabilities(self.backend)


class AnnualDaylightComponent:
    """Controller for the ``Foton Annual Daylight`` component."""

    def __init__(self, settings=None):
        self.settings = settings or FotonSettings()

    def run(self, request: AnnualDaylightRequest, **process_options):
        manifest = FotonClient(self.settings.executable).run_annual_daylight(
            request, **process_options
        )
        return manifest, load_grid_result_branches(manifest)

    def run_async(self, request: AnnualDaylightRequest, **process_options):
        """Start a cancelable background process suitable for GH task components."""
        return FotonClient(self.settings.executable).run_annual_daylight_async(
            request, **process_options
        )


class AnnualResultsComponent:
    """Controller for the ``Foton Annual Results`` component."""

    @staticmethod
    def load(manifest_path):
        manifest = load_manifest(manifest_path)
        return manifest, load_grid_result_branches(manifest)
