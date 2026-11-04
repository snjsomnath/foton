"""FastAPI application for the local daylight viewer."""

from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

from fastapi import FastAPI, File, Form, HTTPException, UploadFile, WebSocket, WebSocketDisconnect
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
    demo_weather_path: str | Path | None = None,
) -> FastAPI:
    """Build the viewer's FastAPI app.

    The arguments let tests swap in a fake engine, a weather store or another
    frontend folder. The built frontend is served from ``viewer/dist`` when it
    exists.
    """
    factory = engine_factory or Engine
    store = weather_store or WeatherStore()
    demo_epw = Path(demo_weather_path) if demo_weather_path else (
        Path(__file__).resolve().parents[3] / "epw" / "gothenburg.epw"
    )
    demo_weather_lock = asyncio.Lock()

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
        version="0.3.3",
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

    @app.post("/api/demo/weather")
    async def demo_weather() -> dict[str, Any]:
        # Fixed local asset, never a client-supplied filesystem path. Serialize
        # ingestion so repeated mounts cannot race while creating weather caches.
        async with demo_weather_lock:
            try:
                payload = await asyncio.to_thread(demo_epw.read_bytes)
                dataset = await asyncio.to_thread(
                    app.state.weather_store.ingest, payload, demo_epw.name, 0.0,
                )
            except FileNotFoundError as exc:
                raise HTTPException(
                    status_code=503,
                    detail="Demo weather is missing. Run from a Foton checkout containing epw/gothenburg.epw.",
                ) from exc
            except (OSError, RuntimeError, ValueError) as exc:
                raise HTTPException(status_code=503, detail=str(exc)) from exc
        return dataset.summary()

    @app.get("/api/demo/solar/{weather_id}")
    async def demo_solar(weather_id: str) -> dict[str, Any]:
        from .solar import solar_diagram
        try:
            dataset = app.state.weather_store.get(weather_id)
            location = dataset.location
            return await asyncio.to_thread(solar_diagram, float(location["latitude"]),
                float(location["longitude"]), float(location.get("time_zone", 1)), dataset.north_rotation_degrees)
        except (KeyError, ValueError, TypeError) as exc:
            raise HTTPException(status_code=400, detail="Solar diagram requires a weather dataset with location metadata.") from exc

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
                            demo=message.get("demo") is True,
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
