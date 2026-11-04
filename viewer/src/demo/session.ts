import { normalizeAnalysisResult } from "../api";
import type { AnalysisResult, GeometryPayload, ServerMessage } from "../types";
import type { DemoParameters, Shot } from "./timeline";

export interface DemoFrame {
  responseMs?: number;
  geometry: GeometryPayload;
  analysis: AnalysisResult;
  parameters: DemoParameters;
}
type Pending = { revision: number; shot: Shot; stage: "scene" | "preview" | "final" | "hour"; geometry?: GeometryPayload; sceneRevision?: number; started: number };

/** One request chain at a time; only matched geometry/results become a frame. */
export class DemoSession {
  frame: DemoFrame | null = null;
  ready = false;
  phase = "Preparing room";
  error: string | null = null;
  operation: "transport" | "hour" = "transport";
  private revision = 0;
  private reusable = true;
  private pending: Pending | null = null;
  private queued: Shot | null = null;
  private lastSceneAt = -Infinity;
  private target: Shot | null = null;
  constructor(private send: (message: object) => void, private weatherId: string) {}

  request(shot: Shot) {
    this.target = shot;
    this.ready = false;
    this.error = null;
    this.queued = shot;
    if (this.pending) {
      this.send({ type: "cancel" });
      // Invalidate every response from the superseded chain immediately.
      this.revision += 1;
      this.pending = null;
      this.reusable = false;
    }
    this.phase = "Updating scene";
  }
  pump(now: number) {
    if (this.pending && now - this.pending.started > 120_000) {
      this.fail("The GPU calculation timed out. Retry this chapter.");
    }
    const shot = this.queued;
    if (!shot || this.pending || this.error || now - this.lastSceneAt < 250) return;
    this.queued = null;
    const sameScene = this.reusable && this.frame && JSON.stringify(shot.parameters) === JSON.stringify(this.frame.parameters);
    const qualityReady = this.frame && (shot.quality === "preview" || this.frame.analysis.quality === "final");
    if (sameScene && qualityReady) {
      if (this.frame!.analysis.selected_timestep === shot.timestep) {
        this.ready = true; this.phase = "Ready"; return;
      }
      this.operation = "hour";
      this.phase = "Selecting hour";
      this.pending = { revision: this.revision, shot, stage: "hour", geometry: this.frame!.geometry,
        sceneRevision: this.frame!.analysis.scene_revision, started: now };
      this.send({ type: "select_timestep", client_revision: this.revision, selected_timestep: shot.timestep });
      return;
    }
    this.operation = "transport";
    this.lastSceneAt = now;
    this.revision += 1;
    this.pending = { revision: this.revision, shot, stage: "scene", started: now };
    this.send({ type: "set_scene", demo: true, client_revision: this.revision, parameters: shot.parameters });
  }
  receive(message: ServerMessage) {
    const pending = this.pending;
    if (!pending) return;
    if (!("client_revision" in message) || message.client_revision !== pending.revision) return;
    if (message.type === "error") { this.fail(message.message); return; }
    if (message.type === "scene" && pending.stage === "scene") {
      pending.geometry = message.geometry;
      pending.sceneRevision = message.scene_revision;
      pending.shot = { ...pending.shot, parameters: { ...pending.shot.parameters, ...message.parameters } };
      this.analyze("preview");
    } else if (message.type === "analysis_result") {
      const result = normalizeAnalysisResult(message);
      if (!pending.geometry || pending.stage === "scene" || result.scene_revision !== pending.sceneRevision ||
          result.selected_timestep !== pending.shot.timestep ||
          (pending.stage !== "hour" && result.quality !== pending.stage) ||
          (pending.stage === "hour" && result.quality !== this.frame?.analysis.quality)) return;
      if (result.used_reference_fallback || !["metal", "vulkan"].includes(result.transport_backend.toLowerCase())) {
        this.fail("This demo requires native Metal or Vulkan GPU transport. CPU reference fallback was detected."); return;
      }
      if (!result.annual_metrics_available || result.sensor_ids.length !== pending.geometry.sensor_ids.length ||
          result.sensor_ids.some((id, index) => id !== pending.geometry!.sensor_ids[index]) ||
          [result.illuminance_lux, result.daylight_factor_percent, result.daylight_autonomy_percent, result.passes_sda]
            .some((values) => values.length !== result.sensor_ids.length)) {
        this.fail("The analysis does not match the room’s annual sensor data. Retry this chapter."); return;
      }
      this.reusable = true;
      this.frame = { geometry: pending.geometry, analysis: result, parameters: pending.shot.parameters, responseMs: performance.now() - pending.started };
      if (pending.stage === "preview" && pending.shot.quality === "final") {
        this.analyze("final");
      } else {
        this.pending = null; this.ready = true; this.phase = "Ready";
      }
    }
  }
  private analyze(quality: "preview" | "final") {
    if (!this.pending) return;
    this.pending.stage = quality;
    this.phase = quality === "preview" ? "GPU preview" : "GPU refinement";
    this.send({ type: "analyze", client_revision: this.pending.revision, weather_id: this.weatherId,
      quality, selected_timestep: this.pending.shot.timestep });
  }
  fail(message: string) {
    this.send({ type: "cancel" });
    this.revision += 1;
    this.pending = null; this.queued = null;
    this.error = message; this.ready = false; this.phase = "Paused";
  }
  retry() { if (this.target) { this.frame = null; this.request(this.target); } }
}
