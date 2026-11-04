# Frequently asked questions

## Is Foton a replacement for Radiance?

No. Foton speeds up one part of a Radiance-style annual daylight study: the
ray tracing that links the sky to the sensors. It handles matte surfaces,
ordinary glazing and shading devices. For glossy materials, complex glazing
systems, glare or compliance work, use Radiance.

## Do I need Radiance installed?

No, from version 0.3.2. Foton builds its own annual sky from the weather file.
Radiance is only needed to reproduce the validation results.

## How close are the results to Radiance?

On a typical room, daylight autonomy is within 0.2 percentage points of
Radiance run until its results stop changing. 204 of 212 test cases pass
every check. The [accuracy section of the README](../README.md#accuracy) has
the full table, and [accuracy notes](purpose-and-plan.md) explain the eight
cases that do not pass.

## Which computers does it run on?

- macOS on Apple silicon, using Metal
- Windows and Linux with an NVIDIA, AMD or Intel GPU that supports Vulkan 1.3
  ray tracing
- Any other computer, using the CPU. This gives the same answer, but slower.

`foton-honeybee capabilities` tells you which one Foton will use. See
[installation](installation.md) for details.

## Why is the default 8 bounces when Honeybee's recipe uses 2?

Light bouncing around a room adds a lot to the illuminance at the back of
the room. With 2 bounces, Honeybee's standard recipe reads about 15 % lower
than converged Radiance on the test rooms. Foton defaults to 8 bounces,
which agrees with converged Radiance, and is still fast.

## Can I use Foton for certification or compliance?

Not yet. Foton is checked against Radiance on a set of test models, but it has
not been reviewed for any standard. Its sDA is labelled `static_sDA300_50`
because it does not include the full LM-83 procedure (dynamic blinds and ASE).

## Can I use it from Grasshopper?

Yes. Download `foton-grasshopper-<version>.zip` from the
[releases page](https://github.com/snjsomnath/foton/releases) and follow the
[Grasshopper quickstart](grasshopper-quickstart.md). The results work with
Honeybee's metric components and Ladybug's heatmap.

## How do I cite Foton?

Use GitHub's **Cite this repository** button, or the details in
[CITATION.cff](../CITATION.cff).
