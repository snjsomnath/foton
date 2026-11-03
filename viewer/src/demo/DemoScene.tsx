import { useEffect, useRef } from "react";
import * as THREE from "three";
import type { Shot, SolarDiagram } from "./timeline";
import { boxCorners, fitDistance } from "./rendering";

function disposeGroup(group: THREE.Group) {
  group.traverse(object => {
    if (object instanceof THREE.Mesh || object instanceof THREE.Line) {
      object.geometry.dispose();
      (Array.isArray(object.material) ? object.material : [object.material]).forEach(material => material.dispose());
    }
  });
  group.clear();
}
import type { PreparedScene } from "./scenePreparation";

type Motion = { attribute: THREE.BufferAttribute; from: Float32Array; to: Float32Array };

export function DemoScene({ prepared, shot, playback, solar, onError }: {
  prepared: PreparedScene | null; shot: Shot;
  playback: () => { shot: Shot; playing: boolean; progress: number };
  solar: SolarDiagram | null; onError: (message: string) => void;
}) {
  const frame = prepared?.frame ?? null;
  const container = useRef<HTMLDivElement>(null);
  const content = useRef<THREE.Group | null>(null);
  const solarContent = useRef<THREE.Group | null>(null);
  const sunMarker = useRef<THREE.Mesh | null>(null);
  const solarBounds = useRef(new THREE.Box3());
  const solarPoints = useRef<THREE.Vector3[]>([]);
  const bounds = useRef(new THREE.Box3(new THREE.Vector3(0, -2, 0), new THREE.Vector3(6, 9, 3)));
  const transitions = useRef<Motion[]>([]);
  const boundsVersion = useRef(0);
  const changedAt = useRef(0);
  const boundsTimer = useRef<number | undefined>(undefined);
  const installed = useRef<PreparedScene["geometry"] | null>(null);
  const current = useRef({ frame, shot, playback, solar, onError });
  current.current = { frame, shot, playback, solar, onError };
  useEffect(() => {
    if (!container.current) return;
    const element = container.current;
    let renderer: THREE.WebGLRenderer;
    try { renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true }); }
    catch { current.current.onError("WebGL is unavailable. Enable hardware acceleration and reload."); return; }
    // Capture resolution follows the stage; Retina supersampling competes with transport.
    renderer.setPixelRatio(1);
    renderer.outputColorSpace = THREE.SRGBColorSpace;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.1;
    element.appendChild(renderer.domElement);
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(40, 1, 0.1, 1000);
    camera.up.set(0, 0, 1);
    const group = new THREE.Group();
    content.current = group; scene.add(group);
    const sky = new THREE.Group(); solarContent.current = sky; scene.add(sky);
    scene.add(new THREE.HemisphereLight(0xffffff, 0xc0c9cd, 2.5));
    const key = new THREE.DirectionalLight(0xfff8ef, 2.5); key.position.set(-7, -8, 17); scene.add(key);
    const fill = new THREE.DirectionalLight(0xe1ebff, 1); fill.position.set(12, 8, 10); scene.add(fill);
    let resized = false;
    const resize = () => {
      resized = true;
      renderer.setSize(element.clientWidth, element.clientHeight, false);
      camera.aspect = element.clientWidth / Math.max(element.clientHeight, 1);
      camera.updateProjectionMatrix();
    };
    const observer = new ResizeObserver(resize); observer.observe(element); resize();
    let animation = 0, previous = performance.now(), motionTime = 0, radius = 1;
    const target = bounds.current.getCenter(new THREE.Vector3());
    const direction = new THREE.Vector3(-0.5, -0.6, 0.65).normalize();
    const desiredDirection = new THREE.Vector3();
    let previousShot = current.current.shot;
    let previousFrame = current.current.frame;
    let previousBoundsVersion = -1;
    const render = (now: number) => {
      const dt = Math.min((now - previous) / 1000, 0.1); previous = now;
      const state = { ...current.current, ...current.current.playback() };
      const viewChanged = resized || state.shot !== previousShot || state.frame !== previousFrame || boundsVersion.current !== previousBoundsVersion;
      if (state.playing) motionTime += dt;
      const progress = THREE.MathUtils.clamp(state.progress, 0, 1);
      // Short parameter beats form one continuous move; easing each beat causes pulses.
      const easedProgress = state.shot.duration < 1 ? progress : progress * progress * (3 - 2 * progress);
      const [azimuth, elevation, distance] = state.shot.camera.map((v, i) => THREE.MathUtils.lerp(v, state.shot.cameraEnd[i], easedProgress));
      const theta = THREE.MathUtils.degToRad(azimuth + Math.sin(motionTime * 0.45) * 1.4);
      const phi = THREE.MathUtils.degToRad(elevation);
      desiredDirection.set(Math.sin(theta) * Math.cos(phi), -Math.cos(theta) * Math.cos(phi), Math.sin(phi));
      const subject = (focus: Shot["focus"]) => {
        const p = state.frame?.parameters;
        if (!p || focus === "scene") return bounds.current.clone();
        if (focus === "zone") return new THREE.Box3(new THREE.Vector3(0, -Math.max(p.overhang_depth, p.left_fin_depth, p.right_fin_depth), 0), new THREE.Vector3(p.width, p.depth, p.height));
        const centerX = p.width / 2 + p.window_offset;
        const half = (p.window_count * p.window_width + (p.window_count - 1) * p.window_gap) / 2 + .5;
        return new THREE.Box3(new THREE.Vector3(centerX - half, -Math.max(p.overhang_depth, p.left_fin_depth, p.right_fin_depth) - .3, 0),
          new THREE.Vector3(centerX + half, 2.4, p.height));
      };
      const focusBounds = subject(state.shot.focus), endBounds = subject(state.shot.focusEnd);
      focusBounds.min.lerp(endBounds.min, easedProgress); focusBounds.max.lerp(endBounds.max, easedProgress);
      if (state.shot.overview) {
        const cue = state.shot.overview;
        const phase = THREE.MathUtils.clamp((progress - cue.leadIn) / (1 - cue.leadIn), 0, 1);
        const eased = phase * phase * (3 - 2 * phase);
        focusBounds.min.fromArray(cue.from[0]).lerp(new THREE.Vector3().fromArray(cue.to[0]), eased);
        focusBounds.max.fromArray(cue.from[1]).lerp(new THREE.Vector3().fromArray(cue.to[1]), eased);
      }
      const modelCorners = boxCorners(focusBounds);
      if (state.shot.solar !== "off") focusBounds.union(solarBounds.current);
      const desiredTarget = focusBounds.getCenter(new THREE.Vector3());
      const blend = 1 - Math.exp(-dt * 7);
      if (!state.playing && viewChanged) { direction.copy(desiredDirection); target.copy(desiredTarget); }
      else if (state.playing) { direction.lerp(desiredDirection, blend).normalize(); target.lerp(desiredTarget, blend); }
      previousShot = state.shot; previousFrame = state.frame; previousBoundsVersion = boundsVersion.current;
      const corners = state.shot.solar !== "off" ? [...modelCorners, ...solarPoints.current.map(v => v.clone())] : modelCorners;
      const required = fitDistance(corners, target, direction, camera.fov, camera.aspect, state.shot.solar === "off" ? .86 : .82);
      radius = state.playing ? Math.max(required, THREE.MathUtils.lerp(radius, required * Math.max(1, distance / 1.8), blend)) : viewChanged || resized ? required : Math.max(required, radius);
      resized = false;
      camera.near = Math.max(.03, radius / 2500); camera.far = Math.max(1000, radius * 5); camera.updateProjectionMatrix();
      element.dataset.framing = state.shot.focus === state.shot.focusEnd ? state.shot.focus : "transition";
      const sun = state.solar?.hourly[state.frame?.analysis.selected_timestep ?? 0];
      if (sunMarker.current && state.frame && sun) {
        const p = state.frame.parameters, r = Math.max(p.width, p.depth) * .8;
        sunMarker.current.position.set(p.width / 2 + sun[0]*r, p.depth / 2 + sun[1]*r, sun[2]*r);
        sunMarker.current.visible = sun[2] > 0;
      }
      camera.position.copy(target).addScaledVector(direction, radius);
      camera.lookAt(target);
      const t = Math.min(1, (now - changedAt.current) / 110);
      const eased = t * t * (3 - 2 * t);
      for (const motion of transitions.current) {
        for (let i = 0; i < motion.to.length; i++) motion.attribute.array[i] = motion.from[i] + (motion.to[i] - motion.from[i]) * eased;
        motion.attribute.needsUpdate = true;
      }
      if (t === 1) transitions.current = [];
      // Expose projected frame bounds for visual QA; these describe rendered geometry only.
      let maxX = 0, maxY = 0;
      camera.updateMatrixWorld();
      for (const corner of corners) { corner.project(camera); maxX = Math.max(maxX, Math.abs(corner.x)); maxY = Math.max(maxY, Math.abs(corner.y)); }
      element.dataset.frameX = maxX.toFixed(4); element.dataset.frameY = maxY.toFixed(4);
      renderer.render(scene, camera);
      animation = requestAnimationFrame(render);
    };
    const lost = (event: Event) => { event.preventDefault(); current.current.onError("The graphics context was lost. Reload to reconnect."); };
    renderer.domElement.addEventListener("webglcontextlost", lost);
    animation = requestAnimationFrame(render);
    return () => {
      cancelAnimationFrame(animation); observer.disconnect(); window.clearTimeout(boundsTimer.current);
      renderer.domElement.removeEventListener("webglcontextlost", lost);
      disposeGroup(group); disposeGroup(sky); solarContent.current = null; content.current = null; transitions.current = []; installed.current = null;
      renderer.dispose(); renderer.domElement.remove();
    };
  }, []);

  useEffect(() => {
    const group = content.current;
    if (!group || !prepared) return;
    const frame = prepared.frame;
    if (installed.current === prepared.geometry) {
      const heatmap = group.getObjectByName("cells") as THREE.Mesh;
      const colors = heatmap.geometry.getAttribute("color") as THREE.BufferAttribute;
      colors.array.set(prepared.colors); colors.needsUpdate = true;
      return;
    }
    window.clearTimeout(boundsTimer.current);
    installed.current = prepared.geometry;
    const old = new Map<string, Float32Array>();
    group.traverse(object => {
      if (object instanceof THREE.Mesh || object instanceof THREE.Line) {
        if (object.name === "site-platform") return;
        old.set(object.name, new Float32Array(object.geometry.getAttribute("position").array));
      }
    });
    const previousBounds = new THREE.Box3();
    old.forEach(positions => previousBounds.union(new THREE.Box3().setFromBufferAttribute(new THREE.BufferAttribute(positions, 3))));
    disposeGroup(group);
    transitions.current = [];
    const { geometry, parameters: p } = frame;
        const reflectances = [p.wall_reflectance, p.floor_reflectance, p.ceiling_reflectance, p.shade_reflectance, 0.9, 0.35];
    prepared.geometry.surfaces.forEach(surface => {
      const name = surface.name, index = geometry.material_names.indexOf(name);
      const buffer = new THREE.BufferGeometry();
      buffer.setAttribute("position", new THREE.BufferAttribute(surface.positions, 3));
      buffer.setAttribute("normal", new THREE.BufferAttribute(surface.normals, 3));
      const glass = name === "glass", wall = name === "wall";
      const value = 0.3 + reflectances[index] * 0.65;
      const mesh = new THREE.Mesh(buffer, new THREE.MeshStandardMaterial({
        color: glass ? new THREE.Color("#8ebac1") : new THREE.Color().setRGB(value, value * 0.99, value * 0.97),
        // Inward-facing walls make an opaque architectural cutaway, without transparency sorting.
        side: wall ? THREE.FrontSide : THREE.DoubleSide, roughness: 0.85,
        transparent: glass, opacity: glass ? 0.1 : 1, depthWrite: !glass,
        polygonOffset: true, polygonOffsetFactor: 1, polygonOffsetUnits: 1,
      }));
      mesh.name = `surface-${name}`; group.add(mesh);
      const edgeBuffer = new THREE.BufferGeometry();
      edgeBuffer.setAttribute("position", new THREE.BufferAttribute(surface.edges, 3));
      const edges = new THREE.LineSegments(edgeBuffer,
        new THREE.LineBasicMaterial({ color: glass ? "#5b8a98" : "#8b9498", depthWrite: false, depthTest: name === "context" }));
      edges.name = `edges-${name}`; edges.renderOrder = 10; group.add(edges);
    });
    // No second floor/base at z=0: that coplanar surface caused the original flicker.
    const heat = new THREE.BufferGeometry();
    heat.setAttribute("position", new THREE.BufferAttribute(prepared.geometry.cells, 3));
    heat.setAttribute("color", new THREE.BufferAttribute(prepared.colors, 3));
    const heatmap = new THREE.Mesh(heat, new THREE.MeshBasicMaterial({ vertexColors: true, side: THREE.DoubleSide, toneMapped: false }));
    heatmap.name = "cells"; group.add(heatmap);
    if (geometry.context_present) {
      const site = new THREE.Box3(new THREE.Vector3().fromArray(prepared.geometry.bounds, 0), new THREE.Vector3().fromArray(prepared.geometry.bounds, 3));
      const size = site.getSize(new THREE.Vector3()), center = site.getCenter(new THREE.Vector3());
      const ground = new THREE.Mesh(new THREE.BoxGeometry(size.x + 1.2, size.y + 1.2, .12), new THREE.MeshStandardMaterial({ color: "#e2e4d9", roughness: 1 }));
      ground.position.set(center.x, center.y, -.11); ground.name = "site-platform"; group.add(ground);
    }
    const nextBounds = new THREE.Box3(new THREE.Vector3().fromArray(prepared.geometry.bounds, 0), new THREE.Vector3().fromArray(prepared.geometry.bounds, 3));
    if (geometry.context_present) { nextBounds.expandByVector(new THREE.Vector3(.6, .6, 0)); nextBounds.min.z = -.17; }
    // The union covers the whole transition, including a jump to many room instances.
    bounds.current = nextBounds.clone().union(previousBounds);
    boundsVersion.current += 1;
    changedAt.current = performance.now();
    group.traverse(object => {
      if (!(object instanceof THREE.Mesh || object instanceof THREE.Line)) return;
      const attribute = object.geometry.getAttribute("position") as THREE.BufferAttribute;
      const from = old.get(object.name);
      if (from && from.length === attribute.array.length) {
        transitions.current.push({ attribute, from, to: new Float32Array(attribute.array) });
        // Disable stale frustum bounds while vertex positions transition.
        object.frustumCulled = false;
      }
    });
    // Release the old extent after the positional transition; colors are never interpolated.
    boundsTimer.current = window.setTimeout(() => { bounds.current = nextBounds; boundsVersion.current += 1; }, 140);
  }, [prepared]);
  useEffect(() => {
    const group = solarContent.current;
    if (!group) return;
    disposeGroup(group); sunMarker.current = null; solarBounds.current.makeEmpty(); solarPoints.current = [];
    if (!solar || !frame || shot.solar === "off") return;
    const p = frame.parameters, r = Math.max(p.width, p.depth) * .8;
    const center = new THREE.Vector3(p.width / 2, p.depth / 2, 0);
    const line = (vectors: number[][], color: string, opacity: number) => {
      if (vectors.length < 2) return;
      const points = vectors.map(v => new THREE.Vector3().fromArray(v).multiplyScalar(r).add(center));
      points.forEach(v => solarBounds.current.expandByPoint(v));
      solarPoints.current.push(...points);
      group.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(points), new THREE.LineBasicMaterial({ color, transparent: true, opacity, depthWrite: false })));
    };
    const horizon = Array.from({ length: 97 }, (_, i) => [Math.cos(i / 96 * Math.PI * 2), Math.sin(i / 96 * Math.PI * 2), .003]);
    line(horizon, "#c8baa0", .5);
    if (shot.solar === "year") {
      solar.monthly_paths.forEach(path => line(path, "#b98b47", .36));
      // The noon analemma is continuous at Gothenburg throughout the year.
      line([...solar.analemmas[2], solar.analemmas[2][0]], "#e28b10", 1);
    } else {
      const day = Math.floor(frame.analysis.selected_timestep / 24);
      line(solar.hourly.slice(day * 24, day * 24 + 24).filter(v => v[2] > 0), "#dc9b36", .8);
    }
    const marker = new THREE.Mesh(new THREE.SphereGeometry(r * .035, 20, 12), new THREE.MeshBasicMaterial({ color: "#ffb526", toneMapped: false }));
    marker.name = "sun"; group.add(marker); sunMarker.current = marker;
    solarBounds.current.expandByScalar(r * .06);
    boundsVersion.current += 1;
    return () => { disposeGroup(group); sunMarker.current = null; };
  }, [solar, shot.solar, frame?.parameters.width, frame?.parameters.depth, Math.floor((frame?.analysis.selected_timestep ?? 0) / 24)]);
  return <div className="demo-scene" ref={container} aria-label="Live parametric rooms with individually colored sensor cells" />;
}
