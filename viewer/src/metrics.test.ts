import { describe, expect, it } from "vitest";
import { colorForValue, gridCornerValues, metricValues } from "./metrics";
import type { AnalysisResult } from "./types";

const result = {
  illuminance_lux: [100, 500],
  daylight_factor_percent: [1.2, 2.4],
  daylight_autonomy_percent: [40, 80],
  passes_sda: [false, true],
} as AnalysisResult;

describe("viewer metrics", () => {
  it("selects the documented sensor array", () => {
    expect(metricValues(result, "illuminance")).toEqual([100, 500]);
    expect(metricValues(result, "df")).toEqual([1.2, 2.4]);
    expect(metricValues(result, "da")).toEqual([40, 80]);
    expect(metricValues(result, "sda")).toEqual([0, 1]);
  });

  it("clamps continuous colors and distinguishes sDA states", () => {
    expect(colorForValue(-100, "illuminance").getHexString()).toBe(
      colorForValue(0, "illuminance").getHexString(),
    );
    expect(colorForValue(5000, "illuminance").getHexString()).toBe(
      colorForValue(2500, "illuminance").getHexString(),
    );
    expect(colorForValue(0, "sda").getHexString()).not.toBe(
      colorForValue(1, "sda").getHexString(),
    );
  });

  it("averages adjacent sensors onto continuous grid corners", () => {
    expect(gridCornerValues([1, 3, 5, 7], 2, 2)).toEqual([
      1, 2, 3,
      3, 4, 5,
      5, 6, 7,
    ]);
  });
});
