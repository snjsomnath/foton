import { useEffect, useRef, useState } from "react";
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";
import {
  colorForValue,
  gridCornerValues,
  metricValueLabel,
  metricValues,
} from "./metrics";
import type {
  AnalysisResult,
  GeometryPayload,
  MetricMode,
} from "./types";

interface SceneViewProps {
  geometry: GeometryPayload | null;
  analysis: AnalysisResult | null;
  metric: MetricMode;
}

interface TooltipState {
  x: number;
  y: number;
  sensorIndex: number;
}

const MATERIAL_COLORS = ["#d7d0be", "#766b5e", "#f0eadc", "#6f7782", "#7fc7ff"];

export function SceneView({ geometry, analysis, metric }: SceneViewProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const sceneRef = useRef<THREE.Scene | null>(null);
  const cameraRef = useRef<THREE.PerspectiveCamera | null>(null);
  const rendererRef = useRef<THREE.WebGLRenderer | null>(null);
  const controlsRef = useRef<OrbitControls | null>(null);
  const contentRef = useRef<THREE.Group | null>(null);
  const sensorsRef = useRef<THREE.InstancedMesh | null>(null);
  const heatmapRef = useRef<THREE.Mesh | null>(null);
  const geometryRef = useRef<GeometryPayload | null>(geometry);
  const analysisRef = useRef<AnalysisResult | null>(analysis);
  const metricRef = useRef<MetricMode>(metric);
  const [tooltip, setTooltip] = useState<TooltipState | null>(null);

  useEffect(() => {
    geometryRef.current = geometry;
  }, [geometry]);
  useEffect(() => {
    analysisRef.current = analysis;
  }, [analysis]);
  useEffect(() => {
    metricRef.current = metric;
  }, [metric]);

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;

    const scene = new THREE.Scene();
    scene.background = new THREE.Color("#0d1117");
    scene.fog = new THREE.Fog("#0d1117", 18, 45);
    const camera = new THREE.PerspectiveCamera(38, 1, 0.05, 100);
    camera.up.set(0, 0, 1);
    camera.position.set(10, -13, 9);
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.outputColorSpace = THREE.SRGBColorSpace;
    renderer.shadowMap.enabled = true;
    container.appendChild(renderer.domElement);
    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.target.set(3, 4.5, 1.2);

    scene.add(new THREE.HemisphereLight("#d7edff", "#503b2b", 2.2));
    const key = new THREE.DirectionalLight("#fff2d2", 2.4);
    key.position.set(-6, -10, 14);
    key.castShadow = true;
    scene.add(key);
    const content = new THREE.Group();
    scene.add(content);
    const floorGrid = new THREE.GridHelper(30, 30, "#2f3a46", "#202831");
    floorGrid.rotation.x = Math.PI / 2;
    floorGrid.position.z = -0.01;
    scene.add(floorGrid);

    const raycaster = new THREE.Raycaster();
    const pointer = new THREE.Vector2();
    const onPointerMove = (event: PointerEvent) => {
      const sensors = sensorsRef.current;
      if (!sensors) {
        setTooltip(null);
        return;
      }
      const bounds = renderer.domElement.getBoundingClientRect();
      pointer.x = ((event.clientX - bounds.left) / bounds.width) * 2 - 1;
      pointer.y = -((event.clientY - bounds.top) / bounds.height) * 2 + 1;
      raycaster.setFromCamera(pointer, camera);
      const hit = raycaster.intersectObject(sensors, false)[0];
      if (hit?.instanceId !== undefined) {
        setTooltip({
          x: event.clientX - bounds.left + 14,
          y: event.clientY - bounds.top + 14,
          sensorIndex: hit.instanceId,
        });
      } else {
        setTooltip(null);
      }
    };
    renderer.domElement.addEventListener("pointermove", onPointerMove);
    renderer.domElement.addEventListener("pointerleave", () => setTooltip(null));

    const resize = () => {
      const width = container.clientWidth;
      const height = container.clientHeight;
      renderer.setSize(width, height, false);
      camera.aspect = width / Math.max(height, 1);
      camera.updateProjectionMatrix();
    };
    const observer = new ResizeObserver(resize);
    observer.observe(container);
    resize();
    let animation = 0;
    const render = () => {
      controls.update();
      renderer.render(scene, camera);
      animation = requestAnimationFrame(render);
    };
    render();

    sceneRef.current = scene;
    cameraRef.current = camera;
    rendererRef.current = renderer;
    controlsRef.current = controls;
    contentRef.current = content;
    return () => {
      cancelAnimationFrame(animation);
      observer.disconnect();
      renderer.domElement.removeEventListener("pointermove", onPointerMove);
      controls.dispose();
      renderer.dispose();
      renderer.domElement.remove();
    };
  }, []);

  useEffect(() => {
    const content = contentRef.current;
    if (!content || !geometry) return;
    while (content.children.length) {
      const child = content.children.pop();
      if (child instanceof THREE.Mesh || child instanceof THREE.LineSegments) {
        child.geometry.dispose();
        if (Array.isArray(child.material)) {
          child.material.forEach((material) => material.dispose());
        } else {
          child.material.dispose();
        }
      }
    }

    const positions = new Float32Array(geometry.vertices.flat());
    geometry.material_names.forEach((name, materialIndex) => {
      const selectedIndices = geometry.triangles
        .filter((_, index) => geometry.triangle_materials[index] === materialIndex)
        .flat();
      if (!selectedIndices.length) return;
      const buffer = new THREE.BufferGeometry();
      buffer.setAttribute("position", new THREE.BufferAttribute(positions, 3));
      buffer.setIndex(selectedIndices);
      buffer.computeVertexNormals();
      const isGlass = name === "glass";
      const opacity =
        name === "shade"
          ? 0.82
          : isGlass
            ? 0.16
            : name === "ceiling"
              ? 0.025
              : name === "floor"
                ? 0.1
                : 0.14;
      const material = new THREE.MeshStandardMaterial({
        color: MATERIAL_COLORS[materialIndex] ?? "#c8c8c8",
        side: THREE.DoubleSide,
        transparent: true,
        opacity,
        roughness: isGlass ? 0.08 : 0.78,
        metalness: 0,
        depthWrite: name === "shade",
      });
      const mesh = new THREE.Mesh(buffer, material);
      mesh.renderOrder = name === "shade" ? 3 : 1;
      mesh.castShadow = name === "shade";
      mesh.receiveShadow = true;
      content.add(mesh);
      if (!isGlass) {
        const edges = new THREE.LineSegments(
          new THREE.EdgesGeometry(buffer, 25),
          new THREE.LineBasicMaterial({
            color: "#506070",
            transparent: true,
            opacity: name === "ceiling" ? 0.42 : 0.58,
          }),
        );
        edges.renderOrder = 4;
        content.add(edges);
      }
    });

    const { columns, rows, cell_width: cellWidth, cell_depth: cellDepth } =
      geometry.grid;
    const workplaneZ = geometry.sensor_positions[0]?.[2] ?? 0.75;
    const heatmapPositions: number[] = [];
    const heatmapColors: number[] = [];
    const heatmapIndices: number[] = [];
    const mutedColor = new THREE.Color("#667789");
    for (let row = 0; row <= rows; row += 1) {
      for (let column = 0; column <= columns; column += 1) {
        heatmapPositions.push(
          column * cellWidth,
          row * cellDepth,
          workplaneZ + 0.008,
        );
        heatmapColors.push(mutedColor.r, mutedColor.g, mutedColor.b);
      }
    }
    for (let row = 0; row < rows; row += 1) {
      for (let column = 0; column < columns; column += 1) {
        const lowerLeft = row * (columns + 1) + column;
        const lowerRight = lowerLeft + 1;
        const upperLeft = lowerLeft + columns + 1;
        const upperRight = upperLeft + 1;
        heatmapIndices.push(
          lowerLeft,
          lowerRight,
          upperRight,
          lowerLeft,
          upperRight,
          upperLeft,
        );
      }
    }
    const heatmapGeometry = new THREE.BufferGeometry();
    heatmapGeometry.setAttribute(
      "position",
      new THREE.Float32BufferAttribute(heatmapPositions, 3),
    );
    heatmapGeometry.setAttribute(
      "color",
      new THREE.Float32BufferAttribute(heatmapColors, 3),
    );
    heatmapGeometry.setIndex(heatmapIndices);
    const heatmap = new THREE.Mesh(
      heatmapGeometry,
      new THREE.MeshBasicMaterial({
        vertexColors: true,
        side: THREE.DoubleSide,
        transparent: true,
        opacity: 0.96,
        depthWrite: false,
        polygonOffset: true,
        polygonOffsetFactor: -2,
      }),
    );
    heatmap.renderOrder = 5;
    heatmapRef.current = heatmap;
    content.add(heatmap);

    const markerRadius = Math.min(cellWidth, cellDepth) * 0.075;
    const marker = new THREE.CircleGeometry(markerRadius, 10);
    const sensorMaterial = new THREE.MeshBasicMaterial({
      color: "#15202a",
      side: THREE.DoubleSide,
      transparent: true,
      opacity: 0.55,
      depthWrite: false,
    });
    const sensors = new THREE.InstancedMesh(
      marker,
      sensorMaterial,
      geometry.sensor_positions.length,
    );
    const transform = new THREE.Matrix4();
    geometry.sensor_positions.forEach((position, index) => {
      transform.makeTranslation(position[0], position[1], position[2] + 0.018);
      sensors.setMatrixAt(index, transform);
    });
    sensors.instanceMatrix.needsUpdate = true;
    sensors.renderOrder = 6;
    sensorsRef.current = sensors;
    content.add(sensors);

    const camera = cameraRef.current;
    const controls = controlsRef.current;
    if (camera && controls) {
      const box = new THREE.Box3().setFromObject(content);
      const center = box.getCenter(new THREE.Vector3());
      const size = box.getSize(new THREE.Vector3());
      controls.target.copy(center);
      camera.position.set(
        center.x + Math.max(size.x, size.y) * 1.35,
        center.y - Math.max(size.x, size.y) * 1.65,
        center.z + Math.max(size.z, 2) * 2.2,
      );
      controls.update();
    }
  }, [geometry]);

  useEffect(() => {
    const heatmap = heatmapRef.current;
    if (!heatmap || !geometry) return;
    const values = metricValues(analysis, metric);
    const corners = gridCornerValues(
      values,
      geometry.grid.columns,
      geometry.grid.rows,
    );
    const colors = heatmap.geometry.getAttribute("color") as THREE.BufferAttribute;
    for (let index = 0; index < colors.count; index += 1) {
      const color = corners.length
        ? colorForValue(corners[index] ?? 0, metric)
        : new THREE.Color("#667789");
      colors.setXYZ(index, color.r, color.g, color.b);
    }
    colors.needsUpdate = true;
  }, [analysis, geometry, metric]);

  const tooltipAnalysis = analysisRef.current;
  return (
    <div className="scene-view" ref={containerRef}>
      {!geometry && (
        <div className="empty-state">
          <div className="empty-orbit" />
          <strong>Preparing parametric room</strong>
          <span>The canonical Metal scene will appear here.</span>
        </div>
      )}
      {tooltip && geometryRef.current && (
        <div
          className="sensor-tooltip"
          style={{ left: tooltip.x, top: tooltip.y }}
        >
          <strong>Sensor {geometryRef.current.sensor_ids[tooltip.sensorIndex]}</strong>
          {tooltipAnalysis ? (
            <>
              <span>
                {metricValueLabel(
                  tooltipAnalysis,
                  metricRef.current,
                  tooltip.sensorIndex,
                )}
              </span>
              <small>
                DF {tooltipAnalysis.daylight_factor_percent[tooltip.sensorIndex]?.toFixed(2)}%
                {" · "}DA {tooltipAnalysis.daylight_autonomy_percent[tooltip.sensorIndex]?.toFixed(1)}%
              </small>
            </>
          ) : (
            <span>Waiting for analysis</span>
          )}
        </div>
      )}
    </div>
  );
}
