import type { AnalysisResult, StatusPayload, WeatherSummary } from "./types";

type AnalysisPayload = Partial<AnalysisResult> & Record<string, unknown>;

type SummaryPayload = Partial<AnalysisResult["summary"]> & Record<string, unknown>;

function toNumber(value: unknown, fallback = 0): number {
  if (typeof value === "number" && Number.isFinite(value)) return value;
  if (typeof value === "string") {
    const parsed = Number(value);
    if (Number.isFinite(parsed)) return parsed;
  }
  return fallback;
}

function toNumberArray(value: unknown): number[] {
  if (Array.isArray(value)) {
    return value.map((entry) => toNumber(entry));
  }
  return [];
}

function toBooleanArray(value: unknown): boolean[] {
  if (Array.isArray(value)) {
    return value.map((entry) => Boolean(entry));
  }
  return [];
}

function toObject(value: unknown): Record<string, unknown> | null {
  return value && typeof value === "object" && !Array.isArray(value)
    ? (value as Record<string, unknown>)
    : null;
}

function asAnalysisPayload(value: AnalysisResult | AnalysisPayload): AnalysisPayload {
  return value as AnalysisPayload;
}

function average(values: number[]): number {
  if (!values.length) return 0;
  return values.reduce((sum, value) => sum + value, 0) / values.length;
}

export function normalizeAnalysisResult(payload: AnalysisResult | AnalysisPayload): AnalysisResult {
  const result = asAnalysisPayload(payload);
  const summary = toObject(result.summary) as SummaryPayload | null;
  const timings = toObject(result.timings_ms) ?? toObject(result.timings) ?? {};

  const illuminance = toNumberArray(
    result.illuminance_lux ?? result.illuminance ?? result.illuminance_values,
  );
  const daylightFactor = toNumberArray(
    result.daylight_factor_percent ?? result.daylight_factor ?? result.df,
  );
  const daylightAutonomy = toNumberArray(
    result.daylight_autonomy_percent ?? result.daylight_autonomy ?? result.da,
  );
  const passesSda = toBooleanArray(result.passes_sda ?? result.sda_passes);
  const derivedPassesSda = passesSda.length
    ? passesSda
    : daylightAutonomy.map((value) => value >= 50.0);

  const selectedTimestep = toNumber(result.selected_timestep, 0);
  const selectedTimestepLabel =
    typeof result.selected_timestep_label === "string"
      ? result.selected_timestep_label
      : `Timestep ${selectedTimestep + 1}`;

  const summaryValues = {
    mean_lux: toNumber(
      summary?.mean_lux ?? summary?.mean_illuminance_lux ?? result.mean_lux,
      illuminance.length ? average(illuminance) : 0,
    ),
    minimum_lux: toNumber(
      summary?.minimum_lux ?? result.minimum_lux,
      illuminance.length ? Math.min(...illuminance) : 0,
    ),
    maximum_lux: toNumber(
      summary?.maximum_lux ?? result.maximum_lux,
      illuminance.length ? Math.max(...illuminance) : 0,
    ),
    mean_df_percent: toNumber(
      summary?.mean_df_percent ?? summary?.mean_daylight_factor_percent ?? result.mean_df_percent,
      daylightFactor.length ? average(daylightFactor) : 0,
    ),
    minimum_df_percent: toNumber(
      summary?.minimum_df_percent ?? result.minimum_df_percent,
      daylightFactor.length ? Math.min(...daylightFactor) : 0,
    ),
    maximum_df_percent: toNumber(
      summary?.maximum_df_percent ?? result.maximum_df_percent,
      daylightFactor.length ? Math.max(...daylightFactor) : 0,
    ),
    room_sda_percent: toNumber(
      summary?.room_sda_percent ?? summary?.room_sda_percentage ?? result.room_sda_percent,
      0,
    ),
  };

  return {
    type: "analysis_result",
    client_revision: toNumber(result.client_revision, 0),
    scene_revision: toNumber(result.scene_revision, 0),
    quality: result.quality === "final" ? "final" : "preview",
    annual_metrics_available: Boolean(result.annual_metrics_available),
    selected_timestep: selectedTimestep,
    selected_timestep_label: selectedTimestepLabel,
    sensor_ids: toNumberArray(result.sensor_ids).map((value) => Math.trunc(value)),
    illuminance_lux: illuminance,
    daylight_factor_percent: daylightFactor,
    daylight_autonomy_percent: daylightAutonomy,
    passes_sda: derivedPassesSda,
    room_ids: toNumberArray(result.room_ids).map((value) => Math.trunc(value)),
    static_sda_300_50_percent: toNumberArray(result.static_sda_300_50_percent ?? result.static_sda_300_50),
    summary: summaryValues,
    sample_count: toNumber(result.sample_count, 0),
    bounce_count: toNumber(result.bounce_count, 0),
    convergence: toNumber(result.convergence, 0),
    transport_backend: String(
      result.transport_backend ?? result.backend ?? "unknown",
    ),
    used_reference_fallback: Boolean(result.used_reference_fallback),
    timings_ms: {
      tracing_ms: toNumber(
        timings.tracing_ms ?? timings.trace_ms ?? result.tracing_ms ?? result.trace_ms,
        0,
      ),
      annual_reduction_ms: toNumber(
        timings.annual_reduction_ms ?? timings.annual_metrics_ms ?? result.annual_reduction_ms ?? result.annual_metrics_ms,
        0,
      ),
    },
    total_latency_ms: toNumber(result.total_latency_ms ?? result.total_latency, 0),
  };
}

export async function fetchStatus(): Promise<StatusPayload> {
  const response = await fetch("/api/status");
  if (!response.ok) throw new Error(`Status request failed: ${response.status}`);
  return response.json() as Promise<StatusPayload>;
}

export async function uploadWeather(
  file: File,
  northRotationDegrees: number,
): Promise<WeatherSummary> {
  const body = new FormData();
  body.append("file", file);
  body.append("north_rotation_degrees", String(northRotationDegrees));
  const response = await fetch("/api/weather", { method: "POST", body });
  if (!response.ok) {
    const detail = await response.text();
    throw new Error(detail || `Weather upload failed: ${response.status}`);
  }
  return response.json() as Promise<WeatherSummary>;
}

export function sessionSocketUrl(): string {
  const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
  return `${protocol}//${window.location.host}/api/session`;
}
