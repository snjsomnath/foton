import { describe, expect, it } from 'vitest';
import { prepareColors, prepareGeometry } from './scenePreparation';
import { DEFAULT_PARAMETERS } from './timeline';
import { normalizeAnalysisResult } from '../api';
import { cellBuffers } from './rendering';
import type { DemoFrame } from './session';

const frame: DemoFrame = {parameters: DEFAULT_PARAMETERS, analysis: normalizeAnalysisResult({illuminance_lux:[100,2000], daylight_factor_percent:[1,8], daylight_autonomy_percent:[30,70], passes_sda:[false,true]}), geometry:{
  vertices:[[0,0,0],[2,0,0],[2,1,0],[0,1,0]],triangles:[[0,1,2],[0,2,3]],triangle_materials:[0,0],material_names:['floor'],
  sensor_positions:[[.5,.5,.75],[1.5,.5,.75]],sensor_ids:[0,1],sensor_area_weights:[1,1],grid:{columns:2,rows:1,cell_width:1,cell_depth:1},window:{x_min:0,x_max:2,z_min:1,z_max:2},
}};
describe('worker scene preparation', () => {
  it('prepares bounds, normals, boundary edges and discrete cells without WebGL', () => {
    const prepared = prepareGeometry(frame);
    expect(prepared.bounds).toEqual([0,0,0,2,1,0]);
    expect(prepared.surfaces[0].positions.length).toBe(18);
    expect(prepared.surfaces[0].normals.length).toBe(18);
    expect(prepared.surfaces[0].edges.length).toBe(24); // Four edges, no diagonal seam.
    expect(prepared.cells.length).toBe(36);
    expect(prepared.cells[2]).toBeCloseTo(.77);
  });
  it('color-only updates preserve the existing metric colors for all four maps', () => {
    for (const metric of ['illuminance','df','da','sda'] as const) {
      expect(prepareColors(frame, metric)).toEqual(new Float32Array(cellBuffers(frame, metric).colors));
    }
  });
});
