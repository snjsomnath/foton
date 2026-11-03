import { useEffect, useRef, useState } from 'react';
import type { MetricMode } from '../types';
import type { DemoFrame } from './session';
import type { PreparedGeometry, PreparedScene, PrepareRequest, PrepareResponse } from './scenePreparation';

/** Publish geometry and colors together, after worker preparation has completed. */
export function usePreparedScene(frame: DemoFrame | null, metric: MetricMode, onError: (message: string) => void) {
  const [scene, setScene] = useState<PreparedScene | null>(null);
  const worker = useRef<Worker | null>(null);
  const request = useRef({id: 0, key: 0, frame, metric});
  const submitted = useRef<DemoFrame['geometry'] | null>(null);
  const cache = useRef<{ key: number; geometry: PreparedGeometry } | null>(null);
  useEffect(() => {
    const active = new Worker(new URL('./scene.worker.ts', import.meta.url), {type: 'module'});
    worker.current = active; submitted.current = null; cache.current = null;
    active.onmessage = ({data}: MessageEvent<PrepareResponse>) => {
      const pending = request.current;
      if (data.key !== pending.key) return;
      if (data.geometry) cache.current = {key: data.key, geometry: data.geometry};
      if (data.id !== pending.id) return;
      if (data.error) { onError(`Could not prepare the display: ${data.error}`); return; }
      if (pending.frame && data.colors && cache.current?.key === data.key) {
        setScene({frame: pending.frame, metric: pending.metric, geometry: cache.current.geometry, colors: data.colors});
      }
    };
    active.onerror = () => onError('The display preparation worker failed. Reload to restart it.');
    return () => { active.terminate(); worker.current = null; };
  }, [onError]);
  useEffect(() => {
    if (!frame) { request.current.id += 1; setScene(null); return; }
    if (!worker.current) return;
    const geometryChanged = submitted.current !== frame.geometry;
    const key = request.current.key + (geometryChanged ? 1 : 0);
    request.current = {id: request.current.id + 1, key, frame, metric};
    submitted.current = frame.geometry;
    const message: PrepareRequest = {id: request.current.id, key, metric,
      frame: {analysis: frame.analysis, parameters: frame.parameters, responseMs: frame.responseMs},
      ...(geometryChanged ? {geometry: frame.geometry} : {})};
    worker.current.postMessage(message);
  }, [frame, metric, onError]);
  return {scene, ready: Boolean(scene && scene.frame === frame && scene.metric === metric)};
}
