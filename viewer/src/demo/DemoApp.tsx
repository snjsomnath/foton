import { useCallback, useEffect, useRef, useState } from "react";
import { fetchStatus, sessionSocketUrl } from "../api";
import { METRICS } from "../metrics";
import type { ServerMessage, WeatherSummary } from "../types";
import { DemoScene } from "./DemoScene";
import { DemoSession } from "./session";
import { CHAPTERS, PlaybackClock, SHOTS, type SolarDiagram, type DemoParameters } from "./timeline";

import { usePreparedScene } from "./usePreparedScene";
import { ParameterSliders } from "./ParameterSliders";

export default function DemoApp() {
  const clock = useRef(new PlaybackClock());
  const session = useRef<DemoSession | null>(null);
  const stage = useRef<HTMLDivElement>(null);
  const displayed = useRef<{ frame: unknown; metric: string } | null>(null);
  const [attempt, setAttempt] = useState(0);
  const [setup, setSetup] = useState("Preparing Gothenburg weather");
  const [error, setError] = useState<string | null>(null);
  const [clean, setClean] = useState(false);
  const [format, setFormat] = useState(() => new URLSearchParams(window.location.search).get("format") === "square" ? "square" : "wide");
  const [loop, setLoop] = useState(false);
  const [solar, setSolar] = useState<SolarDiagram | null>(null);
  const custom = useRef(false);
  const [, redraw] = useState(0);
  const refresh = useCallback(() => redraw((value) => value + 1), []);
  const fail = useCallback((message: string) => {
    clock.current.playing = false;
    setClean(false);
    setError(message);
    refresh();
  }, [refresh]);

  useEffect(() => {
    const abort = new AbortController();
    let socket: WebSocket | null = null;
    let disposed = false;
    session.current = null;
    setError(null);
    setSetup("Preparing Gothenburg weather");
    const initialize = async () => {
      const status = await fetchStatus();
      if (disposed) return;
      if (!status.engine.available) throw new Error(status.engine.error ?? "The native GPU engine is unavailable.");
      if (status.engine.capabilities?.hardware_acceleration === false) throw new Error("This teaser requires native Metal or Vulkan GPU transport. The service is using the CPU reference backend.");
      const response = await fetch("/api/demo/weather", { method: "POST", signal: abort.signal });
      if (!response.ok) {
        const body = await response.json().catch(() => null);
        throw new Error(body?.detail ?? "Could not prepare the demo weather.");
      }
      const weather = await response.json() as WeatherSummary;
      if (disposed) return;
      if (!weather.annual_metrics_available || weather.timestep_count !== 8760) throw new Error("The teaser requires a complete annual EPW dataset.");
      setSetup("Preparing solar paths");
      const solarResponse = await fetch(`/api/demo/solar/${encodeURIComponent(weather.weather_id)}`, { signal: abort.signal });
      if (!solarResponse.ok) throw new Error("Could not prepare the Gothenburg solar diagram. Retry weather setup.");
      const solarData = await solarResponse.json() as SolarDiagram;
      if (disposed) return;
      setSolar(solarData);
      setSetup("Connecting to the GPU");
      socket = new WebSocket(sessionSocketUrl());
      const active = new DemoSession((message) => {
        if (socket?.readyState === WebSocket.OPEN) socket.send(JSON.stringify(message));
      }, weather.weather_id);
      session.current = active;
      socket.onmessage = (event) => {
        if (disposed) return;
        try {
          const message = JSON.parse(event.data) as ServerMessage;
          if (message.type === "connected") {
            active.request(SHOTS[clock.current.index]); setSetup("");
          } else if (message.type === "error" && message.client_revision === undefined) {
            active.fail(message.message);
          } else { active.receive(message); }
          if (active.error) fail(active.error);
          refresh();
        } catch (reason) { fail(String(reason)); }
      };
      socket.onclose = () => { if (!disposed) fail("The local GPU service disconnected. Retry to reconnect."); };
      socket.onerror = () => { if (!disposed) fail("Could not connect to the local GPU service. Check that the backend is running."); };
    };
    void initialize().catch((reason) => { if (!disposed) fail(String(reason)); });
    return () => { disposed = true; abort.abort(); socket?.close(); session.current = null; };
  }, [attempt, fail, refresh]);

  useEffect(() => {
    let handle = 0;
    let previous = performance.now();
    let lastPaint = 0;
    const tick = (now: number) => {
      const active = session.current;
      active?.pump(now);
      if (active?.error && clock.current.playing) fail(active.error);
      if (clock.current.tick((now - previous) / 1000, Boolean(active?.ready && displayed.current?.frame === active.frame && displayed.current?.metric === SHOTS[clock.current.index].metric))) {
        active?.request(SHOTS[clock.current.index]);
      }
      previous = now;
      if (now - lastPaint > 80) { refresh(); lastPaint = now; }
      handle = requestAnimationFrame(tick);
    };
    handle = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(handle);
  }, [fail, refresh]);

  const jump = useCallback((index: number) => {
    if (error || setup) return;
    custom.current = false; clock.current.jump(index); session.current?.request(SHOTS[index]); refresh();
  }, [error, setup, refresh]);
  const play = useCallback(() => {
    if (error || setup || !session.current?.frame) return;
    if (clock.current.ended) jump(0);
    if (!clock.current.playing && custom.current) {
      custom.current = false; session.current?.request(SHOTS[clock.current.index]);
    }
    clock.current.playing = !clock.current.playing;
    refresh();
  }, [error, setup, jump, refresh]);
  const restart = useCallback(() => {
    if (error || setup) return;
    custom.current = false; clock.current.restart(); session.current?.request(SHOTS[0]); refresh();
  }, [error, setup, refresh]);
  const fullscreen = useCallback(() => {
    const operation = document.fullscreenElement ? document.exitFullscreen() : stage.current?.parentElement?.requestFullscreen();
    void operation?.catch(() => fail("Fullscreen is unavailable in this browser. Use the browser’s fullscreen command."));
  }, [fail]);
  useEffect(() => {
    const key = (event: KeyboardEvent) => {
      if (event.target instanceof HTMLElement && /INPUT|SELECT|BUTTON|A/.test(event.target.tagName)) return;
      if (event.code === "Space") { event.preventDefault(); play(); }
      if (event.key.toLowerCase() === "r") restart();
      if (event.key.toLowerCase() === "c") setClean((value) => !value);
      if (event.key.toLowerCase() === "f") fullscreen();
      if (event.key === "Escape") setClean(false);
      if (event.key === "ArrowRight" || event.key === "ArrowLeft") {
        event.preventDefault();
        const chapter = CHAPTERS.filter((item) => item.index <= clock.current.index).length - 1;
        jump(CHAPTERS[Math.max(0, Math.min(CHAPTERS.length - 1, chapter + (event.key === "ArrowRight" ? 1 : -1)))].index);
      }
    };
    window.addEventListener("keydown", key);
    const visibility = () => { if (document.hidden) { clock.current.playing = false; refresh(); } };
    document.addEventListener("visibilitychange", visibility);
    return () => { window.removeEventListener("keydown", key); document.removeEventListener("visibilitychange", visibility); };
  }, [play, restart, fullscreen, jump, refresh]);

  const changeParameter = (key: keyof DemoParameters, value: number) => {
    const current = session.current?.frame;
    if (!current || clock.current.playing || error) return;
    custom.current = true;
    session.current?.request({ ...SHOTS[clock.current.index], quality: "preview", parameters: { ...current.parameters, [key]: value } });
    refresh();
  };
  const active = session.current;
  const shot = SHOTS[clock.current.index];
  const prepared = usePreparedScene(active?.frame ?? null, shot.metric, fail);
  const frame = prepared.scene?.frame ?? null;
  displayed.current = frame ? {frame, metric: prepared.scene!.metric} : null;
  const playback = useCallback(() => {
    const current = clock.current, shot = SHOTS[current.index];
    return {shot, playing: current.playing, progress: current.elapsed / shot.duration};
  }, []);
  const analysis = frame?.analysis;
  const p = frame?.parameters;
  const chapter = CHAPTERS.findIndex((item) => item.name === shot.chapter);
  const closing = chapter === CHAPTERS.length - 1;
  const displayMetric = prepared.scene?.metric ?? shot.metric;
  const metric = METRICS[displayMetric];
  const ready = Boolean(active?.ready && prepared.ready);
  const displayError = error ?? active?.error;
  const stat = analysis ? displayMetric === "illuminance" ? analysis.summary.mean_lux : displayMetric === "df"
    ? analysis.summary.mean_df_percent : displayMetric === "sda" ? analysis.summary.room_sda_percent
    : analysis.daylight_autonomy_percent.reduce((sum, value) => sum + value, 0) / analysis.daylight_autonomy_percent.length : 0;
  const statLabel = displayMetric === "sda" ? "Room area meeting target" : displayMetric === "da" ? "Mean daylight autonomy" : `Mean ${metric.label.toLowerCase()}`;
  return <main className={`demo-shell format-${format} ${clean && !displayError ? "capture" : ""}`}>
    <div className="demo-stage" ref={stage}>
      <header className="demo-header">
        <div className="demo-identity"><a className="demo-wordmark" href="/">foton<span> / </span><small>Daylight simulation</small></a><div className="demo-affiliation">SBE - Computational Sustainable Design Group<br /><strong>Chalmers - Department of Architecture and Civil Engineering</strong></div></div>
        <div className="demo-edition">GPU LIGHT TRANSPORT <span>—</span> OPEN SOURCE</div>
      </header>
      <DemoScene prepared={prepared.scene} shot={shot} playback={playback} solar={solar} onError={fail} />
      <div className={`demo-copy ${closing ? "closing" : ""}`} key={`${shot.title}-${shot.caption}`}>
        <p className="demo-eyebrow"><span>{String(chapter + 1).padStart(2, "0")}</span> / {shot.chapter}</p>
        <h1>{shot.title}</h1>
        <p className="demo-caption">{shot.caption}</p>
        {closing && <a className="demo-repository" href="https://github.com/snjsomnath/foton" target="_blank" rel="noreferrer">github.com/snjsomnath/foton <span>↗</span></a>}
        <p className="demo-detail">{shot.detail}</p>
      </div>
      <div className="demo-speed"><strong>{analysis ? analysis.timings_ms.tracing_ms.toFixed(2) : "—"}<small>ms</small></strong><span>GPU LIGHT TRANSPORT</span>
        <div>{frame?.responseMs ? `${Math.round(frame.responseMs)} ms ${active?.operation === "hour" ? "hour selection" : "change → result"}` : "Live computation"}</div></div>
      {p && <><div className="demo-model-count"><strong>{p.room_count.toLocaleString()}</strong> {p.room_count === 1 ? "zone" : "zones"}<span>{frame!.geometry.sensor_ids.length.toLocaleString()} sensor cells · {p.window_count} {p.window_count === 1 ? "window" : "windows"} / zone</span></div>
        <ParameterSliders parameters={p} keys={shot.sliders} playing={clock.current.playing} onChange={changeParameter} /></>}
      {shot.solar !== "off" && analysis && <aside className="demo-solar-readout"><span>GOTHENBURG · 57.66° N</span>
        <strong>{new Date(Date.UTC(2025, 0, 1, analysis.selected_timestep)).toLocaleDateString('en-GB', { day: 'numeric', month: 'short', timeZone: 'UTC' })} <em>{String(analysis.selected_timestep % 24).padStart(2, '0')}:30</em></strong>
        <small>EPW standard time · sun {solar?.hourly[analysis.selected_timestep]?.[3].toFixed(1)}° above horizon</small>
        {shot.solar === "day" ? <div className="sun-time-track"><i style={{ left: `${(analysis.selected_timestep % 24 - 6) / 14 * 100}%` }} /><span>06:00</span><span>12:00</span><span>20:00</span></div>
          : <><div className="demo-months">{'JFMAMJJASOND'.split('').map((m, i) => <span key={i} className={new Date(Date.UTC(2025, 0, 1, analysis.selected_timestep)).getUTCMonth() === i ? 'active' : ''}>{m}</span>)}</div><small>Monthly sun paths · noon analemma</small></>}
      </aside>}
      <div className="demo-result-reading"><strong>{analysis ? stat.toFixed(displayMetric === "illuminance" ? 0 : 1) : "—"} {displayMetric === "illuminance" ? "lux" : "%"}</strong><span>{statLabel}</span></div>
      <div className="demo-map-label"><span>{metric.label}</span><div className={`demo-colorbar ${displayMetric === "sda" ? "binary" : ""}`} /><div className="demo-scale"><span>{displayMetric === "sda" ? "Below target" : `0 ${metric.unit}`}</span><span>{displayMetric === "sda" ? "Meets target" : `${metric.maximum} ${metric.unit}`}</span></div></div>
      <footer className="demo-footer"><span className="demo-live"><i className={!ready ? "busy" : ""} />{setup || (!ready ? (active?.ready && !prepared.ready ? "Preparing display" : active?.phase) ?? "Preparing" : "LIVE GPU")}</span>
        <span>{analysis ? `${analysis.transport_backend.toUpperCase()} · ${analysis.sample_count.toLocaleString()} samples · ${analysis.bounce_count} ${analysis.bounce_count === 1 ? "bounce" : "bounces"}` : "Native Metal / Vulkan"}</span>
        <span>{analysis ? `${analysis.timings_ms.tracing_ms.toFixed(2)} ms transport${active?.operation === "hour" ? " · hour from cached coefficients" : ""}` : "Preparing live analysis"}</span>
      </footer>
      {(setup || (!frame && !displayError)) && <div className="demo-preparing" role="status"><span className="demo-spinner" /><strong>{setup || active?.phase}</strong><span>Preparing weather and live GPU calculations.</span></div>}
      {displayError && <div className="demo-error" role="alert"><span>PLAYBACK PAUSED</span><h2>Analysis unavailable</h2><p>{displayError}</p><button onClick={() => { clock.current.playing = false; setAttempt((value) => value + 1); }}>Retry connection</button></div>}
      <div className="demo-controls">
        <div className="demo-control-top"><button className="demo-play" onClick={play} disabled={!!displayError || !!setup || !frame}>{clock.current.playing ? "Pause" : clock.current.ended ? "Replay" : "Play film"}</button>
          <button onClick={restart} disabled={!!displayError || !!setup}>Restart</button>
          <label className="demo-loop"><input type="checkbox" checked={loop} onChange={(event) => { setLoop(event.target.checked); clock.current.loop = event.target.checked; }} />Loop</label>
          <label className="demo-format">Format <select aria-label="Capture format" value={format} onChange={event => {
            const value = event.target.value;
            setFormat(value);
            const url = new URL(window.location.href);
            if (value === "square") url.searchParams.set("format", "square"); else url.searchParams.delete("format");
            window.history.replaceState(null, "", url);
          }}><option value="wide">16:9</option><option value="square">Square 1:1</option></select></label>
          <span className="demo-control-spacer" /><span className="demo-key-hint">SPACE play · R restart · C clean · F fullscreen</span>
          <button onClick={() => { setClean(true); (document.activeElement as HTMLElement)?.blur(); }} disabled={!!displayError}>Clean capture</button><button onClick={fullscreen}>Fullscreen</button></div>
        <nav aria-label="Film chapters">{CHAPTERS.map((item, index) => <button key={item.name} className={index === chapter ? "active" : ""} onClick={() => jump(item.index)} disabled={!!setup || !!displayError}><small>{String(index + 1).padStart(2, "0")}</small>{item.name}</button>)}</nav>
        <div className="demo-progress"><span style={{ width: `${clock.current.progress * 100}%` }} /></div>
      </div>
    </div>
  </main>;
}
