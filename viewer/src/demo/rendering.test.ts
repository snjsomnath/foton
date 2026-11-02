import { describe, expect, it } from "vitest";
import * as THREE from "three";
import { boxCorners, cellBuffers, fitDistance } from "./rendering";
import { normalizeAnalysisResult } from "../api";
import { DEFAULT_PARAMETERS } from "./timeline";
import { colorForValue } from "../metrics";

describe("cinematic framing and cells", () => {
  it("keeps all corners inside the safe frame during rotations, aspect changes and scale jumps", () => {
    const boxes = [new THREE.Box3(new THREE.Vector3(-2, -3, 0), new THREE.Vector3(8, 10, 4)),
      new THREE.Box3(new THREE.Vector3(0, -2, 0), new THREE.Vector3(40, 51, 4))];
    for (const box of boxes) for (const aspect of [0.7, 1, 1.777, 2.5]) for (const azimuth of [-150, -60, 0, 50, 120]) for (const elevation of [20, 50, 82]) {
      const angle = THREE.MathUtils.degToRad(azimuth), up = THREE.MathUtils.degToRad(elevation);
      const direction = new THREE.Vector3(Math.sin(angle)*Math.cos(up), -Math.cos(angle)*Math.cos(up), Math.sin(up));
      // A lagging target is the important case during sudden room-size changes.
      const target = new THREE.Vector3(3, 4.5, 1.5);
      const corners = boxCorners(box);
      const camera = new THREE.PerspectiveCamera(40, aspect, .1, 1000);
      camera.up.set(0,0,1);
      camera.position.copy(target).addScaledVector(direction, fitDistance(corners,target,direction,40,aspect));
      camera.lookAt(target); camera.updateMatrixWorld();
      for (const corner of corners) {
        corner.project(camera);
        expect(Math.abs(corner.x)).toBeLessThanOrEqual(.820001);
        expect(Math.abs(corner.y)).toBeLessThanOrEqual(.820001);
        expect(corner.z).toBeLessThan(1);
      }
    }
  });
  it("assigns exactly one sensor color to each cell and leaves a gap", () => {
    const cells=cellBuffers({parameters: DEFAULT_PARAMETERS, analysis: normalizeAnalysisResult({illuminance_lux:[100,2000]}), geometry:{
      vertices:[],triangles:[],triangle_materials:[],material_names:[],sensor_positions:[[.5,.5,.75],[1.5,.5,.75]],
      sensor_ids:[0,1],sensor_area_weights:[1,1],grid:{columns:2,rows:1,cell_width:1,cell_depth:1},window:{x_min:1,x_max:2,z_min:1,z_max:2},
    }}, "illuminance");
    for(let cell=0;cell<2;cell++) {
      const color=colorForValue([100,2000][cell],"illuminance");
      for(let vertex=0;vertex<6;vertex++) expect(cells.colors.slice(cell*18+vertex*3,cell*18+vertex*3+3)).toEqual([color.r,color.g,color.b]);
    }
    expect(cells.positions[0]).toBeGreaterThan(0);
    expect(cells.positions[3]).toBeLessThan(1);
    expect(cells.positions[2]).toBeGreaterThan(.75);
  });
});
