import * as THREE from "three";
import { colorForValue, metricValues } from "../metrics";
import type { DemoFrame } from "./session";
import type { MetricMode } from "../types";

export function boxCorners(box: THREE.Box3): THREE.Vector3[] {
  return [box.min.x, box.max.x].flatMap(x => [box.min.y, box.max.y].flatMap(y =>
    [box.min.z, box.max.z].map(z => new THREE.Vector3(x, y, z))));
}

/** Exact perspective fit for the current view, including off-center targets. */
export function fitDistance(corners: THREE.Vector3[], target: THREE.Vector3,
  direction: THREE.Vector3, fov: number, aspect: number, safe = 0.82): number {
  const right = new THREE.Vector3().crossVectors(new THREE.Vector3(0, 0, 1), direction).normalize();
  const up = new THREE.Vector3().crossVectors(direction, right).normalize();
  const tangent = Math.tan(THREE.MathUtils.degToRad(fov / 2));
  return Math.max(1, ...corners.map(corner => {
    const offset = corner.clone().sub(target);
    return offset.dot(direction) + Math.max(Math.abs(offset.dot(right)) / (tangent * aspect * safe),
      Math.abs(offset.dot(up)) / (tangent * safe));
  }));
}

/** Six vertices per sensor, one exact sensor color; no corner averaging. */
export function cellBuffers(frame: DemoFrame, metric: MetricMode) {
  const values = metricValues(frame.analysis, metric);
  const { columns, cell_width: cw, cell_depth: cd } = frame.geometry.grid;
  const positions: number[] = [], colors: number[] = [];
  frame.geometry.sensor_positions.forEach(([x, y, z], index) => {
    const quad = frame.geometry.sensor_cells?.[index] ?? [
      [x - cw / 2, y - cd / 2, z], [x + cw / 2, y - cd / 2, z],
      [x + cw / 2, y + cd / 2, z], [x - cw / 2, y + cd / 2, z],
    ];
    const center = new THREE.Vector3().fromArray(quad[0]).add(new THREE.Vector3().fromArray(quad[2])).multiplyScalar(0.5);
    const color = colorForValue(values[index] ?? 0, metric);
    for (const vertex of [0, 1, 2, 0, 2, 3]) {
      const point = new THREE.Vector3().fromArray(quad[vertex]).sub(center).multiplyScalar(0.955).add(center);
      positions.push(point.x, point.y, point.z + 0.02);
      colors.push(color.r, color.g, color.b);
    }
  });
  return { positions, colors, columns };
}
