# Foton — GPU daylight simulation for teaching

## Presentation

A 72-second demonstration of live parametric daylight analysis, with additional
time when calculations are pending. Captions state what changes and what is
calculated. GPU transport time and request-to-result time remain visible with
their actual measurement scopes. No comparative performance claims are made.

Both 16:9 and square 1:1 formats use the same timeline and live calculations.
The square layout places parameter controls below the model and reserves separate
rows for captions and legends. Camera fitting follows the available scene area.

## Captions and sequence

| Time | Main captions | Demonstration |
| --- | --- | --- |
| 00–05 | **Foton** / **Interactive daylight analysis** | GPU light transport for daylight teaching. Track the window and pull back to the room. |
| 05–15 | **Window geometry** / **Shading devices** / **Multiple windows** / **Material properties** | Change window width, position and height; add openings; vary overhangs, fins, glazing transmittance and surface reflectance. |
| 15–24 | **Room dimensions** / **L-shaped room** / **Sensor grid** | Change room dimensions and floor plan, then adjust sensor spacing and workplane height. |
| 24–33 | **Context shading** / **Obstruction position** / **Combined shading** | Include one neighbouring building, move it relative to the windows, and vary its height and the overhang. Keep the room visible in front of the obstruction. |
| 33–41 | **Hourly daylight** | Gothenburg weather on 21 June, from 07:30 to 18:30 in EPW standard time. Show the corresponding sun position and daily path. |
| 41–51 | **Seasonal sun paths** / **Daylight factor** / **Daylight autonomy** / **Spatial daylight autonomy** | Show monthly paths and the sun's position at noon through the year. Explain each metric in the supporting caption. |
| 51–65 | **Multiple-zone analysis** / **16 zones** / **64 zones** / **256 zones** / **1,024 zones** | Add native room instances with independent sensor grids. Widen before each increase so 16, 64, 256 and 1,024 zones are visible as they appear. Finish with all 24,576 sensor cells. |
| 65–72 | **Open-source daylight simulation** | Fast GPU light transport for parametric daylight teaching. Display the source repository and MIT licence. |

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
