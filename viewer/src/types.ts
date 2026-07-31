export type MetricMode = "illuminance" | "df" | "da" | "sda";
export type AnalysisQuality = "preview" | "final";

export interface RoomParameters {
  width: number;
  depth: number;
  height: number;
  window_width: number;
  window_height: number;
  sill_height: number;
  window_offset: number;
  glazing_enabled: boolean;
  glazing_transmittance: number;
  overhang_depth: number;
  left_fin_depth: number;
  right_fin_depth: number;
  wall_reflectance: number;
  floor_reflectance: number;
  ceiling_reflectance: number;
  shade_reflectance: number;
  sensor_spacing: number;
  workplane_height: number;
}

export interface GeometryPayload {
  vertices: number[][];
  triangles: number[][];
  triangle_materials: number[];
  material_names: string[];
  sensor_positions: number[][];
  sensor_ids: number[];
  sensor_area_weights: number[];
  grid: {
    columns: number;
    rows: number;
    cell_width: number;
    cell_depth: number;
  };
  window: {
    x_min: number;
    x_max: number;
    z_min: number;
    z_max: number;
  };
}

export interface SceneMessage {
  type: "scene";
  client_revision: number;
  scene_revision: number;
  parameters: RoomParameters;
  geometry: GeometryPayload;
}

export interface AnalysisResult {
  type: "analysis_result";
  client_revision: number;
  scene_revision: number;
  quality: AnalysisQuality;
  annual_metrics_available: boolean;
  selected_timestep: number;
  selected_timestep_label: string;
  sensor_ids: number[];
  illuminance_lux: number[];
  daylight_factor_percent: number[];
  daylight_autonomy_percent: number[];
  passes_sda: boolean[];
  room_ids: number[];
  static_sda_300_50_percent: number[];
  summary: {
    mean_lux: number;
    minimum_lux: number;
    maximum_lux: number;
    mean_df_percent: number;
    minimum_df_percent: number;
    maximum_df_percent: number;
    room_sda_percent: number;
  };
  sample_count: number;
  bounce_count: number;
  convergence: number;
  transport_backend: string;
  used_reference_fallback: boolean;
  timings_ms: Record<string, number>;
  total_latency_ms: number;
}

export interface WeatherSummary {
  weather_id: string;
  filename: string;
  north_rotation_degrees: number;
  location: {
    city?: string;
    country?: string;
    latitude?: number;
    longitude?: number;
  };
  timestep_count: number;
  occupied_hours: number;
  timestep_labels: string[];
  annual_metrics_available: boolean;
}

export interface StatusPayload {
  engine: {
    available: boolean;
    error: string | null;
    capabilities: Record<string, unknown> | null;
  };
  gendaymtx: {
    available: boolean;
    path: string | null;
    version: string | null;
  };
  initial_weather: WeatherSummary;
  session_model: string;
}

export type ServerMessage =
  | { type: "connected" }
  | SceneMessage
  | {
      type: "analysis_started";
      client_revision: number;
      scene_revision: number;
      quality: AnalysisQuality;
    }
  | {
      type: "analysis_progress";
      client_revision: number;
      scene_revision: number;
      quality: AnalysisQuality;
      status: string;
      progress: number;
      message?: string;
    }
  | AnalysisResult
  | {
      type: "error";
      request_type: string;
      client_revision?: number;
      message: string;
    };
