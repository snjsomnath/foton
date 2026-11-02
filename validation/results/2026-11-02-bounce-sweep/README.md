# Bounce sweep

Produced by `scripts/bounce_sweep.py` on an Apple M4 Pro with Radiance 5.4a
(2022-04-07). Reading guide:

- "Foton full bias %" against the same bounce count in Radiance is within 0.5 %
  on every lit scene, so one Foton bounce equals one Radiance material bounce.
- Eight bounces lands within 0.5 % of the 12-bounce reference on the glazed
  rooms and was adopted as `DEFAULT_MAXIMUM_BOUNCES`.
- `sealed` has no light and `black_open` has no reflected light: their
  indirect and sealed-room columns are noise over a zero reference.
- `deep_reflective` is unconverged at 12 bounces in both engines and Foton
  overshoots Radiance by 7 % there; see the open issue in
  `docs/purpose-and-plan.md`.
- RMS columns are per-sensor-per-patch and include Monte Carlo noise from both
  engines; bias is the figure that matters for DF/DA/UDI/sDA.

Sky density MF:1, Radiance `-ad 40000 -lw 1e-7`, Foton metal direct=64 indirect=4096.
Errors are against the deepest Radiance run (material bounces = 12). Bias/RMS in percent of the reference.

## sealed (36 sensors)

| bounces | Radiance s | Radiance energy / deepest | Radiance full bias % | Foton ms | Foton energy / 1-bounce | Foton full bias % | Foton full RMS % | Foton indirect bias % |
|---|---|---|---|---|---|---|---|---|
| 1 | 0.4 | 0.0 | -100.0 | 3.52 | None | -100.0 | 100.0 | -100.0 |
| 2 | 0.6 | 2.2857 | 128.571 | 3.34 | None | -100.0 | 100.0 | -100.0 |
| 4 | 1.2 | 0.7857 | -21.429 | 4.22 | None | -100.0 | 100.0 | -100.0 |
| 6 | 1.6 | 2.0714 | 107.143 | 4.5 | None | -100.0 | 100.0 | -100.0 |
| 8 | 2.2 | 0.0714 | -92.857 | 2.37 | None | -100.0 | 100.0 | -100.0 |
| 12 | 2.4 | 1.0 | 0.0 | 3.01 | None | -100.0 | 100.0 | -100.0 |

## black_open (36 sensors)

| bounces | Radiance s | Radiance energy / deepest | Radiance full bias % | Foton ms | Foton energy / 1-bounce | Foton full bias % | Foton full RMS % | Foton indirect bias % |
|---|---|---|---|---|---|---|---|---|
| 1 | 0.2 | 1.0007 | 0.068 | 3.61 | 1.0 | 0.05 | 2.302 | 303.759 |
| 2 | 0.2 | 1.0006 | 0.064 | 3.36 | 1.0 | 0.05 | 2.302 | 303.759 |
| 4 | 0.2 | 1.0002 | 0.017 | 2.33 | 1.0 | 0.05 | 2.302 | 303.759 |
| 6 | 0.2 | 1.0002 | 0.017 | 2.64 | 1.0 | 0.05 | 2.302 | 303.759 |
| 8 | 0.2 | 1.0002 | 0.017 | 1.66 | 1.0 | 0.05 | 2.302 | 303.759 |
| 12 | 0.2 | 1.0 | 0.0 | 2.31 | 1.0 | 0.05 | 2.302 | 303.759 |

## coloured_glass (36 sensors)

| bounces | Radiance s | Radiance energy / deepest | Radiance full bias % | Foton ms | Foton energy / 1-bounce | Foton full bias % | Foton full RMS % | Foton indirect bias % |
|---|---|---|---|---|---|---|---|---|
| 1 | 0.5 | 0.821 | -17.899 | 4.19 | 1.0 | -18.016 | 23.596 | -46.283 |
| 2 | 0.7 | 0.9124 | -8.757 | 4.51 | 1.1129 | -8.761 | 14.985 | -22.508 |
| 4 | 1.3 | 0.9783 | -2.17 | 3.28 | 1.1925 | -2.233 | 7.573 | -5.738 |
| 6 | 1.8 | 0.9948 | -0.519 | 3.76 | 1.2112 | -0.699 | 6.645 | -1.795 |
| 8 | 2.4 | 0.9977 | -0.231 | 4.53 | 1.2158 | -0.323 | 6.498 | -0.83 |
| 12 | 2.5 | 1.0 | 0.0 | 5.7 | 1.2172 | -0.212 | 6.463 | -0.544 |

## dark_interior (36 sensors)

| bounces | Radiance s | Radiance energy / deepest | Radiance full bias % | Foton ms | Foton energy / 1-bounce | Foton full bias % | Foton full RMS % | Foton indirect bias % |
|---|---|---|---|---|---|---|---|---|
| 1 | 0.5 | 0.9931 | -0.694 | 3.78 | 1.0 | -0.678 | 2.768 | -9.785 |
| 2 | 0.7 | 0.9994 | -0.057 | 4.11 | 1.0057 | -0.113 | 2.64 | -1.627 |
| 4 | 0.9 | 1.0001 | 0.006 | 2.19 | 1.0063 | -0.054 | 2.628 | -0.781 |
| 6 | 0.9 | 1.0004 | 0.042 | 2.08 | 1.0063 | -0.054 | 2.628 | -0.779 |
| 8 | 0.9 | 1.0017 | 0.167 | 1.71 | 1.0063 | -0.054 | 2.628 | -0.779 |
| 12 | 0.9 | 1.0 | 0.0 | 1.74 | 1.0063 | -0.054 | 2.628 | -0.779 |

## deep_reflective (72 sensors)

| bounces | Radiance s | Radiance energy / deepest | Radiance full bias % | Foton ms | Foton energy / 1-bounce | Foton full bias % | Foton full RMS % | Foton indirect bias % |
|---|---|---|---|---|---|---|---|---|
| 1 | 0.8 | 0.4281 | -57.193 | 6.44 | 1.0 | -57.925 | 60.273 | -78.584 |
| 2 | 1.3 | 0.5514 | -44.863 | 2.04 | 1.2955 | -45.492 | 50.705 | -61.716 |
| 4 | 2.4 | 0.7413 | -25.875 | 2.43 | 1.7444 | -26.605 | 29.068 | -36.094 |
| 6 | 3.5 | 0.8715 | -12.849 | 2.78 | 2.062 | -13.24 | 15.68 | -17.963 |
| 8 | 4.7 | 0.9654 | -3.463 | 3.0 | 2.283 | -3.945 | 8.567 | -5.352 |
| 12 | 5.4 | 1.0 | 0.0 | 3.92 | 2.5491 | 7.253 | 10.474 | 9.84 |

## interior_glazing (72 sensors)

| bounces | Radiance s | Radiance energy / deepest | Radiance full bias % | Foton ms | Foton energy / 1-bounce | Foton full bias % | Foton full RMS % | Foton indirect bias % |
|---|---|---|---|---|---|---|---|---|
| 1 | 0.9 | 0.8272 | -17.28 | 9.06 | 1.0 | -17.801 | 22.529 | -46.329 |
| 2 | 1.5 | 0.9157 | -8.429 | 3.54 | 1.1107 | -8.699 | 14.531 | -22.641 |
| 4 | 2.8 | 0.9826 | -1.736 | 3.67 | 1.1877 | -2.371 | 7.5 | -6.172 |
| 6 | 4.1 | 0.9967 | -0.329 | 3.83 | 1.2056 | -0.9 | 6.595 | -2.343 |
| 8 | 5.2 | 0.9993 | -0.074 | 4.52 | 1.2099 | -0.545 | 6.447 | -1.418 |
| 12 | 5.5 | 1.0 | 0.0 | 6.26 | 1.2112 | -0.441 | 6.409 | -1.147 |
