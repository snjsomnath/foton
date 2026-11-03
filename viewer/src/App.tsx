import { useCallback, useEffect, useRef, useState } from "react";
import { fetchStatus, normalizeAnalysisResult, sessionSocketUrl, uploadWeather } from "./api";
import { METRICS } from "./metrics";
import { SceneView } from "./SceneView";
import type {
  AnalysisQuality,
  AnalysisResult,
  GeometryPayload,
  MetricMode,
  RoomParameters,
  ServerMessage,
  StatusPayload,
  WeatherSummary,
} from "./types";

const DEFAULT_PARAMETERS: RoomParameters = {
  width: 6,
  depth: 9,
  height: 3,
  window_width: 3,
  window_height: 1.5,
  sill_height: 1,
  window_offset: 0,
  glazing_enabled: true,
  glazing_transmittance: 0.6,
  overhang_depth: 0.75,
  left_fin_depth: 0.5,
  right_fin_depth: 0.5,
  wall_reflectance: 0.7,
  floor_reflectance: 0.2,
  ceiling_reflectance: 0.8,
  shade_reflectance: 0.5,
  sensor_spacing: 0.5,
  workplane_height: 0.75,
};

interface NumericControl {
  key: keyof RoomParameters;
  label: string;
  minimum: number;
  maximum: number;
  step: number;
  unit?: string;
}

const GEOMETRY_CONTROLS: NumericControl[] = [
  { key: "width", label: "Room width", minimum: 2, maximum: 15, step: 0.1, unit: "m" },
  { key: "depth", label: "Room depth", minimum: 2, maximum: 20, step: 0.1, unit: "m" },
  { key: "height", label: "Room height", minimum: 2.2, maximum: 6, step: 0.1, unit: "m" },
  { key: "window_width", label: "Window width", minimum: 0.5, maximum: 10, step: 0.1, unit: "m" },
  { key: "window_height", label: "Window height", minimum: 0.5, maximum: 4, step: 0.1, unit: "m" },
  { key: "sill_height", label: "Sill height", minimum: 0.1, maximum: 2.5, step: 0.05, unit: "m" },
  { key: "window_offset", label: "Window offset", minimum: -4, maximum: 4, step: 0.05, unit: "m" },
  { key: "overhang_depth", label: "Overhang", minimum: 0, maximum: 3, step: 0.05, unit: "m" },
  { key: "left_fin_depth", label: "Left fin", minimum: 0, maximum: 2, step: 0.05, unit: "m" },
  { key: "right_fin_depth", label: "Right fin", minimum: 0, maximum: 2, step: 0.05, unit: "m" },
];

const MATERIAL_CONTROLS: NumericControl[] = [
  { key: "wall_reflectance", label: "Walls", minimum: 0, maximum: 0.95, step: 0.01 },
  { key: "floor_reflectance", label: "Floor", minimum: 0, maximum: 0.95, step: 0.01 },
  { key: "ceiling_reflectance", label: "Ceiling", minimum: 0, maximum: 0.95, step: 0.01 },
  { key: "glazing_transmittance", label: "Glass τᵥ", minimum: 0, maximum: 1, step: 0.01 },
];

const GRID_CONTROLS: NumericControl[] = [
  { key: "sensor_spacing", label: "Grid spacing", minimum: 0.2, maximum: 2, step: 0.05, unit: "m" },
  { key: "workplane_height", label: "Workplane", minimum: 0.1, maximum: 2, step: 0.05, unit: "m" },
];

function NumberControl({
  control,
  parameters,
  onChange,
}: {
  control: NumericControl;
  parameters: RoomParameters;
  onChange: (key: keyof RoomParameters, value: number) => void;
}) {
  const value = parameters[control.key] as number;
  return (
    <label className="parameter-control">
      <span>
        {control.label}
        <output>
          {value.toFixed(control.step < 0.1 ? 2 : 1)}
          {control.unit && <small>{control.unit}</small>}
        </output>
      </span>
      <input
        type="range"
        min={control.minimum}
        max={control.maximum}
        step={control.step}
        value={value}
        onChange={(event) => onChange(control.key, Number(event.target.value))}
      />
    </label>
  );
}

export default function App() {
  const [parameters, setParameters] = useState(DEFAULT_PARAMETERS);
  const [geometry, setGeometry] = useState<GeometryPayload | null>(null);
  const [analysis, setAnalysis] = useState<AnalysisResult | null>(null);
  const [metric, setMetric] = useState<MetricMode>("illuminance");
  const [weather, setWeather] = useState<WeatherSummary | null>(null);
  const [status, setStatus] = useState<StatusPayload | null>(null);
  const [connected, setConnected] = useState(false);
  const [phase, setPhase] = useState("Connecting");
  const [progress, setProgress] = useState(0);
  const [error, setError] = useState<string | null>(null);
  const [selectedTimestep, setSelectedTimestep] = useState(12);
  const [uploading, setUploading] = useState(false);
  const socketRef = useRef<WebSocket | null>(null);
  const revisionRef = useRef(0);
  const weatherRef = useRef<WeatherSummary | null>(null);
  const selectedTimestepRef = useRef(selectedTimestep);
  const finalTimerRef = useRef<number | null>(null);
  const sceneReadyRef = useRef(false);

  useEffect(() => {
    weatherRef.current = weather;
  }, [weather]);
  useEffect(() => {
    selectedTimestepRef.current = selectedTimestep;
  }, [selectedTimestep]);

  const send = useCallback((message: object) => {
    const socket = socketRef.current;
    if (socket?.readyState === WebSocket.OPEN) {
      socket.send(JSON.stringify(message));
    }
  }, []);

  const requestAnalysis = useCallback(
    (quality: AnalysisQuality, revision = revisionRef.current) => {
      const activeWeather = weatherRef.current;
      if (!activeWeather) return;
      send({
        type: "analyze",
        client_revision: revision,
        weather_id: activeWeather.weather_id,
        quality,
        selected_timestep: selectedTimestepRef.current,
      });
    },
    [send],
  );

  const scheduleAnalyses = useCallback(
    (revision: number) => {
      if (!weatherRef.current) return;
      requestAnalysis("preview", revision);
      if (finalTimerRef.current) window.clearTimeout(finalTimerRef.current);
      if (!weatherRef.current.annual_metrics_available) return;
      finalTimerRef.current = window.setTimeout(() => {
        if (revision === revisionRef.current) requestAnalysis("final", revision);
      }, 500);
    },
    [requestAnalysis],
  );

  useEffect(() => {
    void fetchStatus()
      .then((payload) => {
        setStatus(payload);
        setWeather(payload.initial_weather);
        weatherRef.current = payload.initial_weather;
        const initialTimestep = Math.min(
          12,
          payload.initial_weather.timestep_count - 1,
        );
        setSelectedTimestep(initialTimestep);
        selectedTimestepRef.current = initialTimestep;
        if (sceneReadyRef.current) {
          scheduleAnalyses(revisionRef.current);
        }
      })
      .catch((reason) => setError(String(reason)));
    const socket = new WebSocket(sessionSocketUrl());
    socketRef.current = socket;
    socket.onopen = () => setPhase("Connected");
    socket.onclose = () => {
      setConnected(false);
      setPhase("Disconnected");
    };
    socket.onerror = () => setError("The local viewer WebSocket failed.");
    socket.onmessage = (event) => {
      const message = JSON.parse(event.data) as ServerMessage;
      if (message.type === "connected") {
        setConnected(true);
        setPhase("Ready");
        return;
      }
      if ("client_revision" in message && message.client_revision !== undefined) {
        if (message.client_revision !== revisionRef.current) return;
      }
      if (message.type === "scene") {
        sceneReadyRef.current = true;
        setGeometry(message.geometry);
        setError(null);
        if (weatherRef.current) {
          scheduleAnalyses(message.client_revision);
        } else {
          setPhase("Preparing demo sky");
        }
      } else if (message.type === "analysis_started") {
        setPhase(message.quality === "preview" ? "Previewing" : "Refining");
        setProgress(0);
      } else if (message.type === "analysis_progress") {
        setProgress(message.progress);
      } else if (message.type === "analysis_result") {
        const normalized = normalizeAnalysisResult(message);
        setAnalysis(normalized);
        setPhase(normalized.quality === "final" ? "Final" : "Preview");
        setProgress(1);
        if (normalized.selected_timestep !== selectedTimestepRef.current) {
          send({
            type: "select_timestep",
            client_revision: revisionRef.current,
            selected_timestep: selectedTimestepRef.current,
          });
        }
      } else if (message.type === "error") {
        setError(message.message);
        setPhase("Needs attention");
      }
    };
    return () => {
      if (finalTimerRef.current) window.clearTimeout(finalTimerRef.current);
      socket.close();
    };
  }, [scheduleAnalyses, send]);

  useEffect(() => {
    if (!connected) return;
    const timeout = window.setTimeout(() => {
      revisionRef.current += 1;
      setAnalysis(null);
      setPhase("Updating scene");
      send({
        type: "set_scene",
        client_revision: revisionRef.current,
        parameters,
      });
    }, 100);
    return () => window.clearTimeout(timeout);
  }, [connected, parameters, send]);

  const updateParameter = (key: keyof RoomParameters, value: number | boolean) => {
    setParameters((current) => ({ ...current, [key]: value }));
  };

  const onWeather = async (file: File | undefined) => {
    if (!file) return;
    setUploading(true);
    setError(null);
    try {
      const uploaded = await uploadWeather(file, 0);
      setAnalysis(null);
      setWeather(uploaded);
      weatherRef.current = uploaded;
      setSelectedTimestep(Math.min(12, uploaded.timestep_count - 1));
      selectedTimestepRef.current = Math.min(12, uploaded.timestep_count - 1);
      scheduleAnalyses(revisionRef.current);
    } catch (reason) {
      setError(reason instanceof Error ? reason.message : String(reason));
    } finally {
      setUploading(false);
    }
  };

  const onTimestep = (value: number) => {
    setSelectedTimestep(value);
    selectedTimestepRef.current = value;
    if (analysis) {
      send({
        type: "select_timestep",
        client_revision: revisionRef.current,
        selected_timestep: value,
      });
    }
  };

  const gpuTime =
    (analysis?.timings_ms.tracing_ms ?? 0) +
    (analysis?.timings_ms.annual_reduction_ms ?? 0);
  const location = weather?.location.city
    ? `${weather.location.city}${weather.location.country ? `, ${weather.location.country}` : ""}`
    : "Preparing sky";
  const annualMetricsAvailable = weather?.annual_metrics_available ?? false;
  const roomSda =
    analysis?.annual_metrics_available
      ? analysis.summary.room_sda_percent
      : null;

  return (
    <main className="app-shell">
      <header className="topbar">
        <div className="brand">
          <div className="brand-mark"><span /></div>
          <div>
            <strong>Foton</strong>
            <small>Metal spatial analysis</small>
          </div>
        </div>
        <div className="runtime">
          <span className={`status-dot ${phase.toLowerCase().replaceAll(" ", "-")}`} />
          <div>
            <strong>{phase}</strong>
            <small>
              {status?.engine.available ? "Native Metal" : status?.engine.error ?? "Checking GPU"}
            </small>
          </div>
          {(phase === "Previewing" || phase === "Refining") && (
            <div className="progress-ring" style={{ "--progress": `${progress * 360}deg` } as React.CSSProperties} />
          )}
        </div>
      </header>

      <section className="workspace">
        <aside className="controls-panel">
          <section className="weather-card">
            <div>
              <span className="eyebrow">Climate</span>
              <strong>{location}</strong>
              <small>
                {annualMetricsAvailable
                  ? `${weather?.occupied_hours.toFixed(0)} occupied hours`
                  : "10,000 lux overcast demo"}
              </small>
            </div>
            <label className="upload-button">
              {uploading ? "Processing…" : annualMetricsAvailable ? "Replace EPW" : "Load EPW"}
              <input
                type="file"
                accept=".epw"
                disabled={uploading}
                onChange={(event) => void onWeather(event.target.files?.[0])}
              />
            </label>
          </section>

          {error && <div className="error-banner">{error}</div>}

          <div className="control-scroll">
            <ControlSection title="Room & aperture" controls={GEOMETRY_CONTROLS} parameters={parameters} onChange={updateParameter} />
            <section className="control-section">
              <div className="section-heading">
                <span>Envelope</span>
                <label className="toggle">
                  <input
                    type="checkbox"
                    checked={parameters.glazing_enabled}
                    onChange={(event) => updateParameter("glazing_enabled", event.target.checked)}
                  />
                  <span />
                  Glass
                </label>
              </div>
              {MATERIAL_CONTROLS.map((control) => (
                <NumberControl key={control.key} control={control} parameters={parameters} onChange={updateParameter} />
              ))}
            </section>
            <ControlSection title="Sensor grid" controls={GRID_CONTROLS} parameters={parameters} onChange={updateParameter} />
          </div>
        </aside>

        <section className="viewport-panel">
          <SceneView geometry={geometry} analysis={analysis} metric={metric} />
          <div className="metric-tabs">
            {(Object.keys(METRICS) as MetricMode[]).map((key) => (
              <button
                key={key}
                className={metric === key ? "active" : ""}
                disabled={
                  !annualMetricsAvailable && (key === "da" || key === "sda")
                }
                title={
                  !annualMetricsAvailable && (key === "da" || key === "sda")
                    ? "Upload an EPW to calculate annual metrics"
                    : undefined
                }
                onClick={() => setMetric(key)}
              >
                {METRICS[key].label}
              </button>
            ))}
          </div>
          <div className="legend">
            <span>{METRICS[metric].minimum}</span>
            <div className={metric === "sda" ? "legend-bar binary" : "legend-bar"} />
            <span>{METRICS[metric].maximum} {METRICS[metric].unit}</span>
          </div>
          <div className="orientation">
            <span className="north-arrow">N</span>
            <small>+Y</small>
          </div>
        </section>

        <aside className="results-panel">
          <div className="results-heading">
            <div>
              <span className="eyebrow">Analysis</span>
              <strong>{analysis?.selected_timestep_label ?? "Preparing spatial map"}</strong>
            </div>
            <span className={`quality-badge ${analysis?.quality ?? ""}`}>
              {analysis?.quality ?? "idle"}
            </span>
          </div>

          <div className="metric-card primary">
            <span>Spatial daylight autonomy</span>
            <strong>
              {roomSda === null ? "EPW" : roomSda.toFixed(1)}
              {roomSda !== null && <small>%</small>}
            </strong>
            <div className="bar-track">
              <span style={{ width: `${roomSda ?? 0}%` }} />
            </div>
            <small>
              {roomSda === null
                ? "Upload EPW for annual sDA"
                : <>sDA<sub>300,50%</sub> · 08:00–18:00</>}
            </small>
          </div>

          <div className="metric-grid">
            <MetricCard label="Mean illuminance" value={analysis ? analysis.summary.mean_lux.toFixed(0) : "—"} unit="lux" />
            <MetricCard label="Mean daylight factor" value={analysis ? analysis.summary.mean_df_percent.toFixed(2) : "—"} unit="%" />
            <MetricCard label="Sensor points" value={geometry ? String(geometry.sensor_ids.length) : "—"} unit="" />
            <MetricCard label="GPU compute" value={analysis ? gpuTime.toFixed(1) : "—"} unit="ms" />
          </div>

          <section className="hour-control">
            <div>
              <span>Selected hour</span>
              <strong>{analysis?.selected_timestep_label ?? `Hour ${selectedTimestep + 1}`}</strong>
            </div>
            <input
              type="range"
              min={0}
              max={(weather?.timestep_count ?? 8760) - 1}
              value={selectedTimestep}
              disabled={!weather || weather.timestep_count <= 1}
              onChange={(event) => onTimestep(Number(event.target.value))}
            />
            <div className="hour-bounds"><span>Jan</span><span>Dec</span></div>
          </section>

          <section className="run-details">
            <div><span>Samples</span><strong>{analysis?.sample_count.toLocaleString() ?? "—"}</strong></div>
            <div><span>Diffuse bounces</span><strong>{analysis?.bounce_count ?? "—"}</strong></div>
            <div><span>Total latency</span><strong>{analysis ? `${analysis.total_latency_ms.toFixed(1)} ms` : "—"}</strong></div>
            <div><span>Backend</span><strong>{analysis?.transport_backend ?? "—"}</strong></div>
          </section>

          <p className="research-note">
            Static daylight metrics for design exploration. Not a certification report.
          </p>
        </aside>
      </section>
    </main>
  );
}

function ControlSection({
  title,
  controls,
  parameters,
  onChange,
}: {
  title: string;
  controls: NumericControl[];
  parameters: RoomParameters;
  onChange: (key: keyof RoomParameters, value: number) => void;
}) {
  return (
    <section className="control-section">
      <div className="section-heading"><span>{title}</span></div>
      {controls.map((control) => (
        <NumberControl key={control.key} control={control} parameters={parameters} onChange={onChange} />
      ))}
    </section>
  );
}

function MetricCard({ label, value, unit }: { label: string; value: string; unit: string }) {
  return (
    <div className="metric-card">
      <span>{label}</span>
      <strong>{value}<small>{unit}</small></strong>
    </div>
  );
}
