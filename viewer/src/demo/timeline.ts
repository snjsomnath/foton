import type { AnalysisQuality, MetricMode, RoomParameters } from "../types";
import storyboard from "./storyboard.json";

export interface DemoParameters extends RoomParameters {
  window_count: number; window_gap: number; rear_width_scale: number; room_count: number;
  notch_width: number; notch_depth: number; context_height: number; context_offset: number; context_distance: number;
}
export const DEFAULT_PARAMETERS: DemoParameters = {
  notch_width: 0, notch_depth: 0, context_height: 0, context_offset: 0, context_distance: 4,
  window_count: 1, window_gap: 0.4, rear_width_scale: 1, room_count: 1,
  width: 6, depth: 9, height: 3, window_width: 3, window_height: 1.5,
  sill_height: 1, window_offset: 0, glazing_enabled: true,
  glazing_transmittance: 0.6, overhang_depth: 0.75, left_fin_depth: 0.5,
  right_fin_depth: 0.5, wall_reflectance: 0.7, floor_reflectance: 0.2,
  ceiling_reflectance: 0.8, shade_reflectance: 0.5,
  sensor_spacing: 0.5, workplane_height: 0.75,
};
export interface Shot {
  chapter: string; duration: number; title: string; caption: string; detail: string;
  metric: MetricMode; quality: AnalysisQuality; parameters: DemoParameters;
  timestep: number; camera: [number, number, number]; cameraEnd: [number, number, number];
  overview?: { from: number[][]; to: number[][]; leadIn: number };
  focus: "facade" | "zone" | "scene"; focusEnd: "facade" | "zone" | "scene";
  solar: "off" | "day" | "year"; sliders: (keyof DemoParameters)[];
}
// EPW records are hourly, non-leap-year, and indexed by start of hour.
export const june21Hour = (hour: number) => 171 * 24 + hour;
export const SHOTS: Shot[] = storyboard.map((shot) => ({
  ...shot, overview: shot.overview ?? undefined, metric: shot.metric as MetricMode, quality: shot.quality as AnalysisQuality,
  parameters: { ...DEFAULT_PARAMETERS, ...shot.parameters },
  timestep: shot.timestep ?? june21Hour(shot.hour ?? 12), camera: shot.camera as [number, number, number],
  cameraEnd: shot.cameraEnd as [number, number, number], focus: shot.focus as Shot["focus"],
  focusEnd: shot.focusEnd as Shot["focusEnd"], solar: shot.solar as Shot["solar"], sliders: shot.sliders as Shot["sliders"],
}));
export const CHAPTERS = SHOTS.flatMap((shot, index) =>
  index === 0 || shot.chapter !== SHOTS[index - 1].chapter ? [{ name: shot.chapter, index }] : []);
export const TOTAL_DURATION = SHOTS.reduce((sum, shot) => sum + shot.duration, 0);

/** Story time only advances while the displayed result matches the shot. */
export class PlaybackClock {
  index = 0;
  elapsed = 0;
  playing = false;
  ended = false;
  loop = false;
  jump(index: number) {
    this.index = Math.max(0, Math.min(SHOTS.length - 1, index));
    this.elapsed = 0;
    this.ended = false;
  }
  restart() { this.jump(0); this.playing = true; }
  tick(delta: number, ready: boolean): boolean {
    if (!this.playing || !ready || this.ended) return false;
    this.elapsed += Math.max(0, Math.min(delta, 0.1));
    if (this.elapsed < SHOTS[this.index].duration) return false;
    if (this.index === SHOTS.length - 1) {
      if (this.loop) { this.jump(0); return true; }
      this.elapsed = SHOTS[this.index].duration;
      this.playing = false;
      this.ended = true;
      return false;
    }
    this.jump(this.index + 1);
    return true;
  }
  get progress() {
    return (SHOTS.slice(0, this.index).reduce((sum, shot) => sum + shot.duration, 0) + this.elapsed) / TOTAL_DURATION;
  }
}

export interface SolarDiagram { hourly: number[][]; monthly_paths: number[][][]; analemmas: number[][][]; month_timesteps: number[]; time_convention: string; }
