"""Single-session WebSocket orchestration for the local viewer."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
import json
import time
from typing import Any, Awaitable, Callable

import numpy as np

from .geometry import ParametricScene, RoomParameters, generate_parametric_scene
from .weather import WeatherDataset, WeatherStore


PHOTOPIC_WEIGHTS = np.asarray([47.435, 119.93, 11.635], dtype=np.float32)
SendMessage = Callable[[dict[str, Any]], Awaitable[None]]


@dataclass
class AnalysisCache:
    client_revision: int
    scene_revision: int
    quality: str
    weather: WeatherDataset
    coefficients: np.ndarray
    sensor_ids: list[int]
    daylight_factor: np.ndarray
    daylight_autonomy: np.ndarray
    room_ids: list[int]
    static_sda: list[float]
    sample_count: int
    bounce_count: int
    timings: dict[str, float]
    metadata: dict[str, Any]
    total_latency_ms: float


def selected_hour_illuminance(
    coefficients: np.ndarray,
    sky: np.ndarray,
    timestep: int,
) -> np.ndarray:
    if coefficients.ndim != 3 or coefficients.shape[2] != 3:
        raise ValueError("coefficients must have shape [sensor,patch,3]")
    if sky.ndim != 3 or sky.shape[2] != 3:
        raise ValueError("sky must have shape [patch,timestep,3]")
    if coefficients.shape[1] != sky.shape[0]:
        raise ValueError("coefficient and sky patch counts do not match")
    if not 0 <= timestep < sky.shape[1]:
        raise ValueError(f"selected timestep {timestep} is out of range")
    response_rgb = np.einsum(
        "spr,pr->sr",
        coefficients.astype(np.float32, copy=False),
        sky[:, timestep, :].astype(np.float32, copy=False),
        optimize=True,
    )
    return np.ascontiguousarray(response_rgb @ PHOTOPIC_WEIGHTS, dtype=np.float32)


class ViewerSession:
    def __init__(self, engine: Any, weather_store: WeatherStore) -> None:
        self.engine = engine
        self.weather_store = weather_store
        self.generated: ParametricScene | None = None
        self.scene: Any | None = None
        self.client_revision = -1
        self.active_job: Any | None = None
        self.active_task: asyncio.Task[None] | None = None
        self.analysis_token = 0
        self.caches: dict[str, AnalysisCache] = {}

    async def close(self) -> None:
        self._cancel_active()
        if self.active_task:
            try:
                await self.active_task
            except (asyncio.CancelledError, RuntimeError):
                pass

    def _cancel_active(self) -> None:
        self.analysis_token += 1
        if self.active_job is not None:
            self.active_job.cancel()
            self.active_job = None
        if self.active_task is not None and not self.active_task.done():
            self.active_task.cancel()
        self.active_task = None

    async def set_scene(
        self,
        client_revision: int,
        parameters: dict[str, Any],
        send: SendMessage,
    ) -> None:
        self._cancel_active()
        generated = generate_parametric_scene(RoomParameters.model_validate(parameters))
        scene = await asyncio.to_thread(generated.create_native_scene, self.engine)
        self.generated = generated
        self.scene = scene
        self.client_revision = client_revision
        self.caches.clear()
        await send(
            {
                "type": "scene",
                "client_revision": client_revision,
                "scene_revision": int(scene.revision),
                "parameters": generated.parameters.model_dump(),
                "geometry": generated.geometry_payload,
            }
        )

    async def start_analysis(
        self,
        client_revision: int,
        weather_id: str,
        quality: str,
        selected_timestep: int,
        send: SendMessage,
    ) -> None:
        if self.scene is None or self.generated is None:
            raise ValueError("create a scene before starting analysis")
        if client_revision != self.client_revision:
            raise ValueError("analysis revision does not match the current scene")
        if quality not in {"preview", "final"}:
            raise ValueError("quality must be 'preview' or 'final'")
        weather = self.weather_store.get(weather_id)
        if quality == "final" and not weather.annual_metrics_available:
            raise ValueError("the built-in overcast demo supports preview quality only")
        sky = weather.tregenza if quality == "preview" else weather.final
        maximum_samples, maximum_bounces = (64, 1) if quality == "preview" else (4096, 2)
        if not 0 <= selected_timestep < sky.shape[1]:
            raise ValueError("selected timestep is out of range")

        self._cancel_active()
        self.analysis_token += 1
        token = self.analysis_token
        job = self.scene.analyze(
            sky,
            weather.occupancy,
            quality=quality,
            metrics=["df", "da", "static_sda300_50"],
            maximum_samples=maximum_samples,
            maximum_bounces=maximum_bounces,
            scene_seed=0,
            export_coefficients=True,
            supersede=True,
        )
        self.active_job = job
        await send(
            {
                "type": "analysis_started",
                "client_revision": client_revision,
                "scene_revision": int(self.scene.revision),
                "quality": quality,
            }
        )
        self.active_task = asyncio.create_task(
            self._collect_result(
                token,
                job,
                client_revision,
                quality,
                weather,
                selected_timestep,
                send,
            )
        )

    async def _collect_result(
        self,
        token: int,
        job: Any,
        client_revision: int,
        quality: str,
        weather: WeatherDataset,
        selected_timestep: int,
        send: SendMessage,
    ) -> None:
        started = time.perf_counter()
        try:
            while True:
                snapshot = job.poll()
                if token != self.analysis_token:
                    return
                await send(
                    {
                        "type": "analysis_progress",
                        "client_revision": client_revision,
                        "scene_revision": int(snapshot.solver_revision),
                        "quality": quality,
                        "status": snapshot.status,
                        "progress": float(snapshot.progress),
                        "message": snapshot.message,
                    }
                )
                if snapshot.status not in {"queued", "running"}:
                    break
                await asyncio.sleep(0.025)
            result = await asyncio.to_thread(job.result)
            if token != self.analysis_token or client_revision != self.client_revision:
                return
            coefficients = result.coefficients()
            if coefficients is None:
                raise RuntimeError("viewer analyses require exported coefficients")
            metadata = json.loads(result.metadata_json())
            cache = AnalysisCache(
                client_revision=client_revision,
                scene_revision=int(result.solver_revision),
                quality=quality,
                weather=weather,
                coefficients=np.ascontiguousarray(coefficients, dtype=np.float32),
                sensor_ids=[int(value) for value in result.sensor_ids()],
                daylight_factor=np.asarray(result.daylight_factor(), dtype=np.float32),
                daylight_autonomy=np.asarray(
                    result.daylight_autonomy(), dtype=np.float32
                )
                * 100.0,
                room_ids=[int(value) for value in result.room_ids()],
                static_sda=[float(value) for value in result.static_sda_300_50()],
                sample_count=int(result.sample_count),
                bounce_count=int(result.bounce_count),
                timings={key: float(value) for key, value in result.timings().items()},
                metadata=metadata,
                total_latency_ms=(time.perf_counter() - started) * 1000.0,
            )
            self.caches[quality] = cache
            await send(self._result_payload(cache, selected_timestep))
        except asyncio.CancelledError:
            job.cancel()
            raise
        except RuntimeError as exc:
            if token == self.analysis_token:
                await send(
                    {
                        "type": "error",
                        "request_type": "analyze",
                        "client_revision": client_revision,
                        "message": str(exc),
                    }
                )
        finally:
            if token == self.analysis_token:
                self.active_job = None
                self.active_task = None

    async def select_timestep(
        self,
        client_revision: int,
        selected_timestep: int,
        send: SendMessage,
    ) -> None:
        if client_revision != self.client_revision:
            raise ValueError("selected-hour revision does not match the current scene")
        cache = self.caches.get("final") or self.caches.get("preview")
        if cache is None:
            raise ValueError("no completed analysis is available")
        await send(self._result_payload(cache, selected_timestep))

    def _result_payload(
        self,
        cache: AnalysisCache,
        selected_timestep: int,
    ) -> dict[str, Any]:
        sky = (
            cache.weather.tregenza
            if cache.quality == "preview"
            else cache.weather.final
        )
        illuminance = selected_hour_illuminance(
            cache.coefficients,
            sky,
            selected_timestep,
        )
        daylight_factor = cache.daylight_factor
        daylight_autonomy = cache.daylight_autonomy
        room_sda = cache.static_sda[0] if cache.static_sda else 0.0
        return {
            "type": "analysis_result",
            "client_revision": cache.client_revision,
            "scene_revision": cache.scene_revision,
            "quality": cache.quality,
            "annual_metrics_available": cache.weather.annual_metrics_available,
            "selected_timestep": selected_timestep,
            "selected_timestep_label": cache.weather.timestep_labels[selected_timestep],
            "sensor_ids": cache.sensor_ids,
            "illuminance_lux": illuminance.tolist(),
            "daylight_factor_percent": daylight_factor.tolist(),
            "daylight_autonomy_percent": daylight_autonomy.tolist(),
            "passes_sda": (daylight_autonomy >= 50.0).tolist(),
            "room_ids": cache.room_ids,
            "static_sda_300_50_percent": cache.static_sda,
            "summary": {
                "mean_lux": float(np.mean(illuminance)),
                "minimum_lux": float(np.min(illuminance)),
                "maximum_lux": float(np.max(illuminance)),
                "mean_df_percent": float(np.mean(daylight_factor)),
                "minimum_df_percent": float(np.min(daylight_factor)),
                "maximum_df_percent": float(np.max(daylight_factor)),
                "room_sda_percent": room_sda,
            },
            "sample_count": cache.sample_count,
            "bounce_count": cache.bounce_count,
            "convergence": float(cache.metadata.get("convergence", 0.0)),
            "transport_backend": cache.metadata.get("transport_backend"),
            "used_reference_fallback": bool(
                cache.metadata.get("used_reference_fallback", False)
            ),
            "timings_ms": cache.timings,
            "total_latency_ms": cache.total_latency_ms,
        }
