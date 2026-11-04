# Foton — GPU daylight simulation for teaching

## Presentation

A 54.5-second demonstration of live parametric daylight analysis, with additional
time when calculations are pending. Captions state what changes and what is
calculated. GPU transport time and request-to-result time remain visible with
their actual measurement scopes. No comparative performance claims are made.

Both 16:9 and square 1:1 formats use the same timeline and live calculations.
The square layout places parameter controls below the model and reserves separate
rows for captions and legends. Camera fitting follows the available scene area.

## Captions and sequence

| Time | Main captions | Demonstration |
| --- | --- | --- |
| 00–04 | **Foton** / **Interactive daylight analysis** | Annual daylight analysis on the GPU. Track the window and pull back to the room. |
| 04–14 | **Window geometry** / **Shading devices** / **Multiple windows** / **Material properties** | Change window width, position and height; add openings; vary overhangs, fins, glazing transmittance and surface reflectance. |
| 14–23 | **Room dimensions** / **L-shaped room** / **Sensor grid** | Change room dimensions and floor plan, then adjust sensor spacing and workplane height. |
| 23–29 | **Context shading** / **Combined shading** | Include one neighbouring building, then move it and vary its height and the overhang. Keep the room visible in front of the obstruction. |
| 29–35 | **Hourly daylight** | Gothenburg weather on 21 June, from 07:30 to 18:30 in EPW standard time. Show the corresponding sun position and daily path. |
| 35–49.5 | **Seasonal sun paths** / **Daylight factor** / **Daylight autonomy** / **Spatial daylight autonomy** | Show monthly paths and the sun's position at noon through the year. Hold each metric long enough to read its explanation. |
| 49.5–54.5 | **Daylight analysis for Grasshopper and Python** | Install line, Grasshopper toggle, MIT licence and the source repository. |

## Camera and result presentation

- Every camera move starts at the preceding endpoint. Close shots frame an opening
  or the first zone; overview shots contain the complete subject.
- During playback, slider values describe the displayed solver frame. Pause to
  edit them; resume restores the authored state.
- Geometry and matching results appear together. Result colors remain constant
  within each sensor cell, without interpolation between measured values.
- Solar positions use the EPW location, timezone and hourly midpoints. The monthly
  paths use each month's 21st; the noon analemma samples every day of the year.
- The cutaway, studio lighting and context platform are display choices. Hidden
  ceilings and the neighbouring building remain in the transport calculation.
- GPU requests remain sequential. Slow calculations hold the timeline while gentle
  camera movement continues. All displayed timings come from the running system.
