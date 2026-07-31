import * as THREE from "three";
import type { AnalysisResult, MetricMode } from "./types";

export interface MetricDefinition {
  label: string;
  unit: string;
  minimum: number;
  maximum: number;
}

export const METRICS: Record<MetricMode, MetricDefinition> = {
  illuminance: {
    label: "Illuminance",
    unit: "lux",
    minimum: 0,
    maximum: 2500,
  },
  df: {
    label: "Daylight factor",
    unit: "%",
    minimum: 0,
    maximum: 5,
  },
  da: {
    label: "Daylight autonomy",
    unit: "%",
    minimum: 0,
    maximum: 100,
  },
  sda: {
    label: "sDA pass",
    unit: "",
    minimum: 0,
    maximum: 1,
  },
};

const STOPS = [
  [0.0, "#3b0f70"],
  [0.12, "#173bb4"],
  [0.3, "#00a6df"],
  [0.48, "#2ad07f"],
  [0.64, "#dcec42"],
  [0.78, "#ffc72c"],
  [0.9, "#ff7a1a"],
  [1.0, "#e31a1c"],
] as const;

export function metricValues(
  analysis: AnalysisResult | null,
  metric: MetricMode,
): number[] {
  if (!analysis) return [];
  if (metric === "illuminance") return analysis.illuminance_lux;
  if (metric === "df") return analysis.daylight_factor_percent;
  if (metric === "da") return analysis.daylight_autonomy_percent;
  return analysis.passes_sda.map((value) => (value ? 1 : 0));
}

export function colorForValue(value: number, metric: MetricMode): THREE.Color {
  if (metric === "sda") {
    return new THREE.Color(value >= 0.5 ? "#47d18c" : "#e85d75");
  }
  const definition = METRICS[metric];
  const normalized = THREE.MathUtils.clamp(
    (value - definition.minimum) / (definition.maximum - definition.minimum),
    0,
    1,
  );
  for (let index = 1; index < STOPS.length; index += 1) {
    const [upperPosition, upperColor] = STOPS[index];
    const [lowerPosition, lowerColor] = STOPS[index - 1];
    if (normalized <= upperPosition) {
      const local =
        (normalized - lowerPosition) / (upperPosition - lowerPosition);
      return new THREE.Color(lowerColor).lerp(
        new THREE.Color(upperColor),
        local,
      );
    }
  }
  return new THREE.Color(STOPS.at(-1)?.[1] ?? "#e31a1c");
}

export function gridCornerValues(
  sensorValues: number[],
  columns: number,
  rows: number,
): number[] {
  if (sensorValues.length !== columns * rows) return [];
  const corners: number[] = [];
  for (let row = 0; row <= rows; row += 1) {
    for (let column = 0; column <= columns; column += 1) {
      let sum = 0;
      let count = 0;
      for (const sensorRow of [row - 1, row]) {
        for (const sensorColumn of [column - 1, column]) {
          if (
            sensorRow >= 0 &&
            sensorRow < rows &&
            sensorColumn >= 0 &&
            sensorColumn < columns
          ) {
            sum += sensorValues[sensorRow * columns + sensorColumn];
            count += 1;
          }
        }
      }
      corners.push(count ? sum / count : 0);
    }
  }
  return corners;
}

export function metricValueLabel(
  analysis: AnalysisResult,
  metric: MetricMode,
  sensorIndex: number,
): string {
  const values = metricValues(analysis, metric);
  const value = values[sensorIndex] ?? 0;
  if (metric === "sda") return value >= 0.5 ? "Pass" : "Fail";
  return `${value.toFixed(metric === "illuminance" ? 0 : 2)} ${METRICS[metric].unit}`;
}
