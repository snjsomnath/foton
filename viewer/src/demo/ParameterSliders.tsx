import type { DemoParameters } from './timeline';

const LABELS: Partial<Record<keyof DemoParameters, [string, number, number, string]>> = {
  width: ['Room width', 6, 16, 'm'], depth: ['Room depth', 6, 18, 'm'], height: ['Room height', 3, 5, 'm'],
  window_width: ['Opening width', .5, 5, 'm'], window_offset: ['Opening position', -2, 2, 'm'],
  window_height: ['Opening height', .5, 2.5, 'm'], overhang_depth: ['Overhang', 0, 2.5, 'm'],
  glazing_transmittance: ['Glass transmission', .1, .9, ''], wall_reflectance: ['Wall reflectance', .1, .95, ''],
  floor_reflectance: ['Floor reflectance', .1, .8, ''], notch_width: ['L · cut width', 0, 9, 'm'],
  notch_depth: ['L · cut depth', 0, 10, 'm'], context_height: ['Neighbour height', 0, 15, 'm'],
  context_offset: ['Neighbour position', -15, 18, 'm'], context_distance: ['Neighbour distance', 1, 15, 'm'],
  sensor_spacing: ['Sensor spacing', .4, 1.5, 'm'], workplane_height: ['Sensor height', .2, 1.5, 'm'],
};
export function sliderRange(key: keyof DemoParameters, p: DemoParameters) {
  const [label, start, stop, unit] = LABELS[key] ?? [key, 0, 1, ''];
  let min = start, max = stop;
  const span = p.window_count * p.window_width + (p.window_count - 1) * p.window_gap;
  if (key === 'window_width') max = (p.width - .1 - 2 * Math.abs(p.window_offset) - (p.window_count - 1) * p.window_gap) / p.window_count;
  if (key === 'window_offset') { max = (p.width - span) / 2 - .051; min = -max; }
  if (key === 'window_height') max = p.height - p.sill_height - .051;
  if (key === 'width') min = Math.max(min, span + 2 * Math.abs(p.window_offset) + .11, p.notch_width + .51);
  if (key === 'depth') min = Math.max(min, p.notch_depth + .51);
  if (key === 'height') min = Math.max(min, p.sill_height + p.window_height + .051);
  if (key === 'notch_width') max = Math.min(max, p.width - .51);
  if (key === 'notch_depth') max = Math.min(max, p.depth - .51);
  return { label, min, max, unit };
}
export function ParameterSliders({ parameters: p, keys, playing, onChange }: {
  parameters: DemoParameters; keys: (keyof DemoParameters)[]; playing: boolean;
  onChange: (key: keyof DemoParameters, value: number) => void;
}) {
  if (!keys.length) return null;
  return <aside className="demo-sliders"><div className="slider-heading">{playing ? 'LIVE DESIGN PARAMETERS' : 'TRY A LIVE CHANGE'}</div>
    {keys.map(key => {
      const { label, min, max, unit } = sliderRange(key, p);
      const value = Number(p[key]);
      return <label key={key}><span>{label}<output>{value.toFixed(2)} <small>{unit}</small></output></span>
        <input aria-label={label} type="range" min={min} max={max} step="0.01" value={value} disabled={playing}
          style={{ '--fill': `${Math.max(0, Math.min(100, (value-min)/(max-min)*100))}%` } as React.CSSProperties}
          onChange={event => onChange(key, Number(event.target.value))} /></label>;
    })}</aside>;
}
