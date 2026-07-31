"""Local web viewer for Foton."""

import sys

from daylight_engine.viewer import RoomParameters, create_app, generate_parametric_scene
from daylight_engine.viewer import app, geometry, session, weather

sys.modules[f"{__name__}.app"] = app
sys.modules[f"{__name__}.geometry"] = geometry
sys.modules[f"{__name__}.session"] = session
sys.modules[f"{__name__}.weather"] = weather

__all__ = ["RoomParameters", "create_app", "generate_parametric_scene"]
