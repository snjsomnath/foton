import * as THREE from 'three';
import type { DemoFrame } from './session';
import type { MetricMode } from '../types';
import { cellBuffers } from './rendering';
import { colorForValue, metricValues } from '../metrics';

export interface PreparedSurface { name: string; positions: Float32Array; normals: Float32Array; edges: Float32Array; }
export interface PreparedGeometry { surfaces: PreparedSurface[]; cells: Float32Array; bounds: number[]; }
export interface PreparedScene { frame: DemoFrame; metric: MetricMode; geometry: PreparedGeometry; colors: Float32Array; }

/** Runs in the preparation worker. No WebGL or DOM work is needed here. */
export function prepareGeometry(frame: DemoFrame): PreparedGeometry {
  const g = frame.geometry;
  const positions = new Float32Array(g.vertices.length * 3);
  g.vertices.forEach((v, i) => positions.set(v, i * 3));
  const byMaterial = g.material_names.map(() => [] as number[]);
  g.triangles.forEach((triangle, i) => byMaterial[g.triangle_materials[i]].push(...triangle));
  const surfaces: PreparedSurface[] = [];
  g.material_names.forEach((name, i) => {
    if (name === 'ceiling' || !byMaterial[i].length) return;
    const compact = new Float32Array(byMaterial[i].length * 3);
    byMaterial[i].forEach((vertex, j) => compact.set(positions.subarray(vertex * 3, vertex * 3 + 3), j * 3));
    const buffer = new THREE.BufferGeometry();
    buffer.setAttribute('position', new THREE.BufferAttribute(compact, 3));
    buffer.computeVertexNormals();
    const edges = new THREE.EdgesGeometry(buffer, 25);
    surfaces.push({name, positions: compact, normals: buffer.getAttribute('normal').array as Float32Array,
      edges: edges.getAttribute('position').array as Float32Array});
    edges.dispose(); buffer.dispose();
  });
  const bounds = new THREE.Box3().setFromBufferAttribute(new THREE.BufferAttribute(positions, 3));
  return { surfaces, cells: new Float32Array(cellBuffers(frame, 'illuminance').positions),
    bounds: [...bounds.min.toArray(), ...bounds.max.toArray()] };
}

export function prepareColors(frame: Pick<DemoFrame, 'analysis'>, metric: MetricMode): Float32Array {
  const values = metricValues(frame.analysis, metric), colors = new Float32Array(values.length * 18);
  values.forEach((value, i) => {
    const c = colorForValue(value, metric);
    for (let j = 0; j < 6; j++) colors.set([c.r, c.g, c.b], i * 18 + j * 3);
  });
  return colors;
}
export interface PrepareRequest { id: number; key: number; frame: Omit<DemoFrame, 'geometry'>; geometry?: DemoFrame['geometry']; metric: MetricMode; }
export interface PrepareResponse { id: number; key: number; geometry?: PreparedGeometry; colors?: Float32Array; error?: string; }
