import { describe, expect, it } from "vitest";
import { normalizeAnalysisResult } from "./api";

describe("viewer API compatibility", () => {
  it("normalizes alternate analysis payload fields from newer Foton releases", () => {
    const normalized = normalizeAnalysisResult({
      quality: "final",
      annual_metrics_available: true,
      selected_timestep: 7,
      selected_timestep_label: "07:00",
      illuminance: [100, 200],
      daylight_factor: [1.2, 2.4],
      daylight_autonomy: [40, 80],
      sda_passes: [false, true],
      summary: {
        mean_lux: 150,
        minimum_lux: 100,
        maximum_lux: 200,
        mean_df_percent: 1.8,
        minimum_df_percent: 1.2,
        maximum_df_percent: 2.4,
        room_sda_percent: 75,
      },
      timings: {
        trace_ms: 12.5,
        annual_metrics_ms: 3.5,
      },
    });

    expect(normalized.illuminance_lux).toEqual([100, 200]);
    expect(normalized.daylight_factor_percent).toEqual([1.2, 2.4]);
    expect(normalized.daylight_autonomy_percent).toEqual([40, 80]);
    expect(normalized.passes_sda).toEqual([false, true]);
    expect(normalized.summary.mean_lux).toBe(150);
    expect(normalized.summary.mean_df_percent).toBe(1.8);
    expect(normalized.summary.room_sda_percent).toBe(75);
    expect(normalized.timings_ms.tracing_ms).toBe(12.5);
    expect(normalized.timings_ms.annual_reduction_ms).toBe(3.5);
  });
});
