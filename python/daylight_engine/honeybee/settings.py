"""Ladybug Tools-compatible settings for Foton recipes."""

from __future__ import annotations

from pathlib import Path


class RecipeSettings:
    """Execution settings matching the public ``lbt_recipes`` constructor."""

    def __init__(
        self,
        folder=None,
        workers=None,
        reload_old=False,
        report_out=False,
        debug_folder=None,
    ):
        if workers is not None and (not isinstance(workers, int) or workers <= 0):
            raise ValueError("workers must be a positive integer or None")
        self.folder = str(Path(folder).expanduser()) if folder is not None else None
        self.workers = workers
        self.reload_old = bool(reload_old)
        self.report_out = bool(report_out)
        self.debug_folder = (
            str(Path(debug_folder).expanduser()) if debug_folder is not None else None
        )

    def __repr__(self):
        return (
            "RecipeSettings("
            f"folder={self.folder!r}, workers={self.workers!r}, "
            f"reload_old={self.reload_old!r}, report_out={self.report_out!r}, "
            f"debug_folder={self.debug_folder!r})"
        )
