# Foton cinematic demo

```sh
pip install -e ".[viewer]"   # once, from the repository root
cd viewer
npm install                  # once
npm run dev:demo
```

Open http://127.0.0.1:5173/demo.html. The original viewer remains at `/`.
The same Python service prepares `epw/gothenburg.epw` through Radiance
`gendaymtx` (or `RADIANCE_BIN`). Native Metal or Vulkan transport is required;
CPU fallback pauses the film. Weather, solar paths, and the initial GPU result
finish before playback is enabled.

## The film

[The caption script](SCRIPT.md) describes the **54.5-second** edit. Live solver
waits extend the duration. The story follows one room through 104 authored shots:

- Track an opening, pull back, and sweep the façade as visible sliders drive
  window position, size, multiple openings, glazing, shades, and reflectances.
- Stretch the room and retract its north-east corner into a true L. Its floor,
  ceiling, boundary walls, and clipped sensor cells match the physical footprint.
- Raise and move a nearby building. It is opaque native
  transport geometry and affects computed daylight.
- Follow hourly Gothenburg sun positions, then monthly sun paths and the noon
  analemma. Inspect illuminance, daylight factor, daylight autonomy, and static sDA.
- Close on the install line and the Grasshopper and Python routes.

Captions use plain, descriptive language suitable for a research-group post.
The square layout moves parameter tracks below the model and separates captions,
legends and timing readouts. Changing format preserves the current shot and
results, and refits the camera to the new scene area.

The green number is measured **GPU transport time**, with elapsed change-to-result
or cached hour-selection time below. These measurements include their stated
scope only. Preview and final sample counts remain visible. The footer labels
each result as live preview (64 samples, 1 bounce, used while sliders move) or
final quality (262,144 samples, 8 bounces, used where a chapter settles).

## Recording and interaction

1. Select **16:9** for 1920×1080 or **Square 1:1** for 1080×1080 in the Format control.
   The selected composition fits within other window sizes without stretching.
   Open `/demo.html?format=square` to start in square mode; format changes update the URL.
2. Wait for **LIVE GPU**, select **Fullscreen** and **Clean capture**.
3. Start your screen recorder and press **Space**. No audio or video export is included.
4. Playback ends on the closing card. **C** or **Escape** restores controls.

| Action | Shortcut |
| --- | --- |
| Play / pause | Space |
| Restart and play | R |
| Clean capture | C |
| Fullscreen | F |
| Previous / next chapter | Left / right arrow |
| Restore controls | Escape |

Shortcuts apply when focus is on the stage; focused controls retain their usual
keyboard behavior. Loop is off by default. Switching tabs pauses playback.
Clean capture hides controls and cursor while retaining captions, legends,
parameter tracks, solar guides, and measurements. Pause to experiment with the
visible sliders; resume restores the authored parameters. Slider readouts describe
the displayed, solved model. Errors restore controls; retry reconnects in a paused state.

## Authoring and implementation

Edit `SCRIPT.md` and `author_storyboard.py`, then run:

```sh
python src/demo/author_storyboard.py
```

The generated `storyboard.json` contains captions, durations, complete target
variations, metric/quality gates, selected weather indices, camera start/end
poses, framing subjects, and solar/slider cues. `timeline.ts` expands parameter
overrides against the original defaults. Camera tuples contain azimuth,
elevation, and a distance factor relative to the measured perspective fit
(1.8 means the fitted distance). Camera keyframes connect continuously and ease independently of geometry.
Close-ups frame a façade or first zone; overview shots fit the full subject.
Shots may also carry authored overview bounds (used for multi-zone scenes),
which stay fixed during calculation waits. A shallow display platform grounds the context
model without participating in transport.
Near/far clipping planes adapt to camera distance. The camera reads the playback
clock on every animation frame, independently of React text updates. Short
parameter beats use continuous angular motion instead of restarting easing.
The renderer uses one pixel per CSS pixel to avoid Retina supersampling while
the GPU is also calculating transport.

A Web Worker prepares triangle buffers, normals, edges and sensor colors.
The current scene remains visible until matching prepared buffers are ready.
Hour, metric and refinement updates reuse the geometry and only upload new colors.
Worker responses carry request and geometry IDs so superseded jobs cannot replace
the displayed frame. Playback waits for both the solver and display preparation.

Requests are sequential, capped at **four scene changes per second**. Geometry
and analysis publish atomically after revision, quality, timestep, sensor-ID, and
backend checks. Settled chapter endpoints refine where specified: preview is
64 samples / 1 bounce; final is 262,144 indirect samples (the `final` preset at the MF:2 sky) / 8 bounces. Selected hours reuse
completed coefficients through `select_timestep`. Solver holds preserve story
progress and gentle camera motion. Superseded results cannot overwrite the frame.

`POST /api/demo/weather` uses the existing weather store. The demo-only
`GET /api/demo/solar/{weather_id}` derives paths from Ladybug at the loaded EPW
latitude, longitude, timezone, and north rotation. Markers use index + 0.5 hours,
matching WEA hourly midpoints in EPW standard time. Monthly paths use each month's
21st; the noon analemma samples every day of the non-leap year.

The architectural cutaway and studio illumination are presentation choices;
visually hidden ceilings remain in transport. Solar guides explain weather input,
not a physically rendered sky. Exact per-cell result colors are never interpolated.
Small gaps separate cells. Geometry positions ease for 110 ms when topology is
compatible. Opaque cutaway walls, separate depth layers, and a single floor avoid
coplanar flicker. Native room instances share geometry but have independent sensors;
context is a separate mesh without sensors. The demo caps scenes at 30,000 sensors.

## Checks

```sh
npm test
npm run build
cd ..
PYTHONPATH=python .venv/bin/python -m pytest tests/python/test_viewer*.py
```

Both `index.html` and `demo.html` build into `viewer/dist`. The Python service
serves them at http://127.0.0.1:8000. The original viewer uses its existing scene
and session contracts; these extensions are isolated to demo requests.
