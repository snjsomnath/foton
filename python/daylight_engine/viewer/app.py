"""FastAPI application for the local daylight viewer."""

from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

from fastapi import FastAPI, File, Form, UploadFile, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from foton import Engine

from .session import ViewerSession
from .weather import WeatherStore


def create_app(
    *,
    engine_factory: Any = None,
    weather_store: WeatherStore | None = None,
    frontend_directory: str | Path | None = None,
) -> FastAPI:
    factory = engine_factory or Engine
    store = weather_store or WeatherStore()

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        try:
            app.state.engine = factory()
            app.state.engine_error = None
        except Exception as exc:
            app.state.engine = None
            app.state.engine_error = str(exc)
        app.state.weather_store = store
        yield

    app = FastAPI(
        title="Foton Viewer",
        version="0.1.0",
        lifespan=lifespan,
    )

    @app.get("/api/status")
    async def status() -> dict[str, Any]:
        capabilities = None
        if app.state.engine is not None:
            capabilities = app.state.engine.capabilities()
        return {
            "engine": {
                "available": app.state.engine is not None,
                "error": app.state.engine_error,
                "capabilities": capabilities,
            },
            "gendaymtx": app.state.weather_store.status(),
            "initial_weather": app.state.weather_store.initial.summary(),
            "session_model": "single-local-session",
        }

    @app.post("/api/weather")
    async def upload_weather(
        file: UploadFile = File(...),
        north_rotation_degrees: float = Form(0.0),
    ) -> dict[str, Any]:
        payload = await file.read()
        dataset = await asyncio.to_thread(
            app.state.weather_store.ingest,
            payload,
            file.filename or "weather.epw",
            north_rotation_degrees,
        )
        return dataset.summary()

    @app.websocket("/api/session")
    async def session_socket(websocket: WebSocket) -> None:
        await websocket.accept()
        if app.state.engine is None:
            await websocket.send_json(
                {
                    "type": "error",
                    "request_type": "connect",
                    "message": app.state.engine_error or "Foton engine is unavailable",
                }
            )
            await websocket.close(code=1011)
            return
        session = ViewerSession(app.state.engine, app.state.weather_store)
        send_lock = asyncio.Lock()

        async def send(message: dict[str, Any]) -> None:
            async with send_lock:
                await websocket.send_json(message)

        await send({"type": "connected"})
        try:
            while True:
                message = await websocket.receive_json()
                message_type = message.get("type")
                try:
                    if message_type == "set_scene":
                        await session.set_scene(
                            int(message["client_revision"]),
                            message["parameters"],
                            send,
                        )
                    elif message_type == "analyze":
                        await session.start_analysis(
                            int(message["client_revision"]),
                            str(message["weather_id"]),
                            str(message["quality"]),
                            int(message.get("selected_timestep", 0)),
                            send,
                        )
                    elif message_type == "select_timestep":
                        await session.select_timestep(
                            int(message["client_revision"]),
                            int(message["selected_timestep"]),
                            send,
                        )
                    elif message_type == "cancel":
                        session._cancel_active()
                    else:
                        raise ValueError(f"unknown message type {message_type!r}")
                except (KeyError, TypeError, ValueError, RuntimeError) as exc:
                    await send(
                        {
                            "type": "error",
                            "request_type": message_type,
                            "client_revision": message.get("client_revision"),
                            "message": str(exc),
                        }
                    )
        except WebSocketDisconnect:
            pass
        finally:
            await session.close()

    default_frontend = Path(__file__).resolve().parents[3] / "viewer" / "dist"
    frontend = Path(frontend_directory) if frontend_directory else default_frontend
    if frontend.is_dir():
        assets = frontend / "assets"
        if assets.is_dir():
            app.mount("/assets", StaticFiles(directory=assets), name="assets")

        @app.get("/{path:path}")
        async def frontend_route(path: str) -> FileResponse:
            requested = frontend / path
            if path and requested.is_file():
                return FileResponse(requested)
            return FileResponse(frontend / "index.html")

    return app


app = create_app()
