import { describe, expect, it } from "vitest";
import { normalizeAnalysisResult } from "../api";
import type { GeometryPayload } from "../types";
import { DemoSession } from "./session";
import { SHOTS, type Shot } from "./timeline";

const INITIAL: Shot = { ...SHOTS[0], quality: "final" };
const CHANGED: Shot = { ...INITIAL, quality: "preview", parameters: { ...INITIAL.parameters, width: 7 } };
const MORNING: Shot = { ...INITIAL, timestep: 4113 };
const NOON: Shot = { ...INITIAL, timestep: 4116 };
const geometry: GeometryPayload = {
  vertices: [], triangles: [], triangle_materials: [], material_names: [],
  sensor_positions: [[1, 1, 0.75]], sensor_ids: [17], sensor_area_weights: [1],
  grid: { columns: 1, rows: 1, cell_width: 1, cell_depth: 1 },
  window: { x_min: 1, x_max: 2, z_min: 1, z_max: 2 },
};
function fixture() {
  const messages: Record<string, unknown>[] = [];
  const session = new DemoSession((message) => messages.push(message as Record<string, unknown>), "gothenburg");
  function scene(shot: Shot, revision = 1) {
    session.receive({ type: "scene", client_revision: revision, scene_revision: 41 + revision, parameters: shot.parameters, geometry });
  }
  function result(shot: Shot, quality = shot.quality, revision = 1, extra: Record<string, unknown> = {}) {
    session.receive(normalizeAnalysisResult({ type: "analysis_result", client_revision: revision,
      scene_revision: 41 + revision, selected_timestep: shot.timestep, quality, sensor_ids: [17],
      illuminance_lux: [420], daylight_factor_percent: [2.3], daylight_autonomy_percent: [62], passes_sda: [true],
      annual_metrics_available: true, transport_backend: "metal", ...extra }));
  }
  return { session, messages, scene, result };
}
describe("live GPU shot controller", () => {
  it("publishes matched preview then waits for final refinement", () => {
    const { session, messages, scene, result } = fixture();
    session.request(INITIAL); session.pump(0); scene(INITIAL);
    expect(messages.map((m) => m.type)).toEqual(["set_scene", "analyze"]);
    expect(session.frame).toBeNull();
    result(INITIAL, "preview");
    expect(session.frame?.geometry).toBe(geometry);
    expect(session.ready).toBe(false);
    expect(messages.at(-1)?.quality).toBe("final");
    result(INITIAL);
    expect(session.ready).toBe(true);
  });
  it("ignores wrong scene, hour, quality and client revision", () => {
    const { session, scene, result } = fixture();
    session.request(INITIAL); session.pump(0); scene(INITIAL);
    result(INITIAL, "final");
    result(INITIAL, "preview", 5);
    result(INITIAL, "preview", 1, { scene_revision: 99 });
    result(INITIAL, "preview", 1, { selected_timestep: 0 });
    expect(session.frame).toBeNull();
    result(INITIAL, "preview");
    expect(session.frame).not.toBeNull();
  });
  it("does not queue repeated previews while awaiting the GPU", () => {
    const { session, messages, scene } = fixture();
    session.request(INITIAL); session.pump(0); scene(INITIAL);
    for (let time = 1; time < 10000; time += 100) session.pump(time);
    expect(messages.filter((m) => m.type === "analyze")).toHaveLength(1);
  });
  it("cancels jumps, rejects late frames and caps scene changes at four per second", () => {
    const { session, messages, scene, result } = fixture();
    session.request(INITIAL); session.pump(0); scene(INITIAL);
    session.request(CHANGED); session.pump(10);
    result(INITIAL, "preview");
    expect(session.frame).toBeNull();
    expect(messages.filter((m) => m.type === "set_scene")).toHaveLength(1);
    session.pump(250);
    expect(messages.filter((m) => m.type === "set_scene")).toHaveLength(2);
    expect(messages.some((m) => m.type === "cancel")).toBe(true);
    scene(CHANGED, 3); result(CHANGED, "preview", 3);
    expect(session.frame?.parameters).toEqual(CHANGED.parameters);
    expect(session.ready).toBe(true);
  });
  it("retains the displayed frame during a cancelled jump but rebuilds invalidated coefficients", () => {
    const { session, messages, scene, result } = fixture();
    session.request(INITIAL); session.pump(0); scene(INITIAL);
    result(INITIAL, "preview"); result(INITIAL);
    const visible = session.frame;
    session.request(CHANGED); session.pump(250); scene(CHANGED, 2);
    session.request(INITIAL);
    expect(session.frame).toBe(visible);
    result(CHANGED, "preview", 2);
    expect(session.frame).toBe(visible);
    session.pump(500);
    expect(messages.at(-1)?.type).toBe("set_scene");
    expect(session.ready).toBe(false);
  });
  it("selects hours using completed coefficients and changes metrics without tracing", () => {
    const { session, messages, scene, result } = fixture();
    session.request(MORNING); session.pump(0); scene(MORNING);
    result(MORNING, "preview"); result(MORNING);
    session.request(NOON); session.pump(250);
    expect(messages.at(-1)?.type).toBe("select_timestep");
    expect(session.operation).toBe("hour");
    result(MORNING); // Late previous-hour data must not be accepted.
    expect(session.ready).toBe(false);
    result(NOON);
    expect(session.ready).toBe(true);
    const count = messages.length;
    session.request({ ...NOON, metric: "da" }); session.pump(500);
    expect(session.ready).toBe(true);
    expect(messages).toHaveLength(count);
  });
  it("rejects CPU fallback and mismatched sensors", () => {
    for (const extra of [{ transport_backend: "reference" }, { used_reference_fallback: true }, { sensor_ids: [99] }, { annual_metrics_available: false }]) {
      const { session, scene, result } = fixture();
      session.request(CHANGED); session.pump(0); scene(CHANGED); result(CHANGED, "preview", 1, extra);
      expect(session.error).not.toBeNull();
      expect(session.ready).toBe(false);
      expect(session.frame).toBeNull();
    }
  });
  it("times out, cancels and allows a fresh retry", () => {
    const { session, messages } = fixture();
    session.request(INITIAL); session.pump(0); session.pump(120001);
    expect(session.error).toMatch(/timed out/);
    session.retry(); session.pump(120500);
    expect(session.error).toBeNull();
    expect(messages.filter((m) => m.type === "set_scene")).toHaveLength(2);
  });
});
