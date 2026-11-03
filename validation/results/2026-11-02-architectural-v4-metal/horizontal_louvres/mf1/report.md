# Foton report

Status: **passed**

```json
{
  "scene": "horizontal_louvres",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "horizontal_louvres",
    "category": "shading",
    "question": "Do repeated tilted horizontal blades preserve narrow sky gaps?",
    "interactions": [
      "louvres",
      "tilted_shades",
      "small_gaps"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 4,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "44c599f3f66d8a5f3ca3739bc87bb1812de7cc68285081bad8e2c115504224c4",
  "weather_sha256": "98246499f5e0508387c41d22a6f492c76a8ec52c17ceb31712069871a196bcee",
  "gpu_executed": true,
  "candidate": {
    "capabilities": {
      "name": "Metal device: Apple M4 Pro (GPU direct, diffuse, glass, and annual reduction)",
      "hardware_acceleration": true,
      "supports_ray_tracing": true,
      "supports_async_jobs": true
    },
    "direct": {
      "metric_label": "static_sDA300_50",
      "solver_version": "0.2.0",
      "scene_fingerprint": 5344297347170131480,
      "basis": "Tregenza",
      "quality": "Final",
      "glazing_model": "radiance_thin_glass_non_refracting",
      "schedule_timestep_count": 1,
      "direct_sample_count": 256,
      "convergence": 1.0,
      "transport_backend": "metal",
      "used_reference_fallback": false
    },
    "full": {
      "metric_label": "static_sDA300_50",
      "solver_version": "0.2.0",
      "scene_fingerprint": 5344297347170131480,
      "basis": "Tregenza",
      "quality": "Final",
      "glazing_model": "radiance_thin_glass_non_refracting",
      "schedule_timestep_count": 1,
      "direct_sample_count": 256,
      "convergence": 1.0,
      "transport_backend": "metal",
      "used_reference_fallback": false
    }
  },
  "sky_bin_audit": {
    "passed": true,
    "ray_count": 2336,
    "command": [
      "/usr/local/radiance/bin/rcalc",
      "-e",
      "MF:1",
      "-f",
      "/usr/local/radiance/lib/reinhart.cal",
      "-e",
      "Dx=$1;Dy=$2;Dz=$3;$1=rbin"
    ],
    "calibration_sha256": "92b8c09984de7a551773530b3146ba79a51e1b003245f230b6e7b430eb6c26cd"
  },
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 16384,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "horizontal_louvres_grid",
        "bias_percent": -0.2582693261780377,
        "rms_normalized_error_percent": 2.667403777748573,
        "absolute_error": {
          "p95": 1.1700756294885472e-05,
          "p99": 8.456280920654535e-05,
          "maximum": 0.00025503640063107014
        },
        "worst_index": [
          28,
          76,
          0
        ],
        "passed": true
      }
    ],
    "samples_per_patch": [
      1024,
      4096
    ]
  },
  "depth_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "horizontal_louvres_grid",
        "bias_percent": 0.10147853035139233,
        "rms_normalized_error_percent": 2.0794188532286833,
        "absolute_error": {
          "p95": 3.17845206154743e-05,
          "p99": 0.00010330835357308388,
          "maximum": 0.0003204816021025181
        },
        "worst_index": [
          22,
          45,
          0
        ],
        "passed": true
      }
    ]
  },
  "sample_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "horizontal_louvres_grid",
        "bias_percent": -0.05512395874477734,
        "rms_normalized_error_percent": 1.7926881144882483,
        "absolute_error": {
          "p95": 2.7720350772142343e-05,
          "p99": 9.351968765258789e-05,
          "maximum": 0.000310627743601799
        },
        "worst_index": [
          17,
          0,
          0
        ],
        "passed": true
      }
    ]
  },
  "oracle_levels": [
    {
      "samples": 20000,
      "material_bounces": 1,
      "repeatability": {
        "schema_version": 1,
        "run_count": 12,
        "half_run_count": 6,
        "oracle_stable": false,
        "gates": {
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "horizontal_louvres_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.9521262006791411,
                "cvrmse_percent": 29.174812888829866,
                "rms_normalized_rmse_percent": 6.455897043332807,
                "reference_energy": 2.2506635809186264,
                "candidate_energy": 2.272092738561696,
                "relative_energy_error_percent": 0.9521262006791413,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.700310006834709e-05,
                  "p99": 0.00022025825455784798,
                  "maximum": 0.0005630792778295776
                },
                "worst": {
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "sky_patch_index": 45,
                  "rgb_channel": 0,
                  "reference": 0.0008762450500701865,
                  "candidate": 0.001439324327899764
                },
                "passed": false,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -3.1410902744041564,
                "cvrmse_percent": 116.1846864467047,
                "rms_normalized_rmse_percent": 6.918517521461407,
                "reference_energy": 0.7950996447567178,
                "candidate_energy": 0.7701248471434425,
                "relative_energy_error_percent": 3.141090274404156,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.0179236293576347e-05,
                  "p95": 8.325936669279985e-05,
                  "p99": 0.0003195171205637356,
                  "maximum": 0.0007414673455059528
                },
                "worst": {
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "sky_patch_index": 44,
                  "rgb_channel": 0,
                  "reference": 0.00038518127985298634,
                  "candidate": -0.0003562860656529665
                },
                "passed": false,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "2",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 121.34070799220353,
            "full": 249.04958403203636
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "2",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 102.25941694807261,
            "full": 231.87287501059473
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "2",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 103.8945410400629,
            "full": 239.24062494188547
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "2",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 112.32920805923641,
            "full": 228.9023749763146
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "2",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 102.48258302453905,
            "full": 224.22191698569804
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "2",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 103.29341690521687,
            "full": 226.74154199194163
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "2",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 119.2059590248391,
            "full": 249.5519999647513
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "2",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 110.9337080270052,
            "full": 269.2513751098886
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "2",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 107.2139999596402,
            "full": 235.427042003721
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "2",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 108.77299995627254,
            "full": 236.13254202064127
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "2",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 103.96449989639223,
            "full": 237.48504102695733
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "2",
              "-ad",
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 109.24270807299763,
            "full": 238.1460421020165
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 8,
      "repeatability": {
        "schema_version": 1,
        "run_count": 8,
        "half_run_count": 4,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "horizontal_louvres_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.06555706150998494,
                "cvrmse_percent": 17.185194924987584,
                "rms_normalized_rmse_percent": 3.7988383919043875,
                "reference_energy": 2.2645619177110348,
                "candidate_energy": 2.2660464979603603,
                "relative_energy_error_percent": 0.06555706150998494,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.6329784486733408e-05,
                  "p99": 0.00013344973558560014,
                  "maximum": 0.0004178360104560852
                },
                "worst": {
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "sky_patch_index": 45,
                  "rgb_channel": 0,
                  "reference": 0.0037244142149575055,
                  "candidate": 0.004142250225413591
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.058031644460800696,
                "cvrmse_percent": 37.54599456475165,
                "rms_normalized_rmse_percent": 3.766413090529529,
                "reference_energy": 1.5698518201385472,
                "candidate_energy": 1.5707628309653714,
                "relative_energy_error_percent": 0.058031644460800696,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 9.169328905045404e-07,
                  "p90": 1.475500175729394e-05,
                  "p95": 5.4810923757031506e-05,
                  "p99": 0.00018328297301195562,
                  "maximum": 0.0005515141529031098
                },
                "worst": {
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "sky_patch_index": 43,
                  "rgb_channel": 0,
                  "reference": -0.00016956415493041277,
                  "candidate": 0.000381949997972697
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "9",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 137.6556670293212,
            "full": 2446.556416922249
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "9",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 133.03929194808006,
            "full": 2784.0471250237897
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "9",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 134.23766696359962,
            "full": 2432.187374914065
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "9",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 134.3269580975175,
            "full": 2417.4311669776216
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "9",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 133.87337501626462,
            "full": 2422.5116670131683
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "9",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 137.5678749755025,
            "full": 2449.4620410259813
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "9",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 137.7040419029072,
            "full": 2434.7494159592316
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "9",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 138.3793749846518,
            "full": 2400.2920840866864
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 12,
      "repeatability": {
        "schema_version": 1,
        "run_count": 8,
        "half_run_count": 4,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "horizontal_louvres_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.16919936863277035,
                "cvrmse_percent": 17.686760614547733,
                "rms_normalized_rmse_percent": 3.915518860211621,
                "reference_energy": 2.263379633448949,
                "candidate_energy": 2.267209257498507,
                "relative_energy_error_percent": 0.16919936863277035,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3572066493215916e-05,
                  "p99": 0.00013536401093006134,
                  "maximum": 0.0004360488383099437
                },
                "worst": {
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "sky_patch_index": 48,
                  "rgb_channel": 0,
                  "reference": 0.003951430204324424,
                  "candidate": 0.004387479042634368
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.1583973352060675,
                "cvrmse_percent": 39.91369317633485,
                "rms_normalized_rmse_percent": 4.015270575180698,
                "reference_energy": 1.5754571459281639,
                "candidate_energy": 1.5729616637917,
                "relative_energy_error_percent": 0.15839733520606752,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 8.995714892989781e-07,
                  "p90": 1.4778617696720175e-05,
                  "p95": 5.4634532716590755e-05,
                  "p99": 0.0002140310825780034,
                  "maximum": 0.0005575267132371664
                },
                "worst": {
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "sky_patch_index": 43,
                  "rgb_channel": 0,
                  "reference": 0.0004973744507879019,
                  "candidate": -6.0152262449264526e-05
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "13",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 138.02083302289248,
            "full": 2578.772541950457
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "13",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 137.13712501339614,
            "full": 2571.35429198388
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "13",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 140.88437508326024,
            "full": 2560.00891700387
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "13",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 150.04958398640156,
            "full": 2580.882875015959
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "13",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 138.87370796874166,
            "full": 2604.287334019318
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "13",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 137.02058303169906,
            "full": 2593.5937500325963
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "13",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 134.15216596331447,
            "full": 2632.4391670059413
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "13",
              "-ad",
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 134.5881250454113,
            "full": 2581.419291906059
          }
        }
      ]
    },
    {
      "samples": 80000,
      "material_bounces": 12,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "horizontal_louvres_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.050457685858107545,
                "cvrmse_percent": 13.506625602273367,
                "rms_normalized_rmse_percent": 2.9865892614509897,
                "reference_energy": 2.265958993386448,
                "candidate_energy": 2.2671023438570046,
                "relative_energy_error_percent": 0.05045768585810755,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3065505229169495e-05,
                  "p99": 0.00010534707689657807,
                  "maximum": 0.00026767957024276257
                },
                "worst": {
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "sky_patch_index": 42,
                  "rgb_channel": 0,
                  "reference": 0.0034312770003452897,
                  "candidate": 0.003163597430102527
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.37662712574631446,
                "cvrmse_percent": 29.90362692500265,
                "rms_normalized_rmse_percent": 3.0022082954152682,
                "reference_energy": 1.573820398831188,
                "candidate_energy": 1.567892964298661,
                "relative_energy_error_percent": 0.3766271257463145,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 8.792492565135035e-07,
                  "p90": 1.444858753529843e-05,
                  "p95": 4.181655240245161e-05,
                  "p99": 0.00015575287397950888,
                  "maximum": 0.0004732112865895033
                },
                "worst": {
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "sky_patch_index": 46,
                  "rgb_channel": 0,
                  "reference": -7.315422408282757e-05,
                  "candidate": 0.0004000570625066757
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "13",
              "-ad",
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 199.0408330457285,
            "full": 4524.805624969304
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "13",
              "-ad",
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 189.25825005862862,
            "full": 4475.8625839604065
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "13",
              "-ad",
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 192.1433329116553,
            "full": 4502.1383339772
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "1",
              "-ad",
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
              "-ab",
              "13",
              "-ad",
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 193.6611250275746,
            "full": 4579.684666940011
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 782.8529169782996,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 2743.2542080059648,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/direct_4096/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/horizontal_louvres/mf1/direct_4096/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 4096,
      "elapsed_ms": 10444.046374992467,
      "worker_pool_size": 12,
      "invocation_count": 3
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      36,
      146,
      3
    ],
    "gates": {
      "direct": {
        "absolute_nmbe_percent": 2.0,
        "rms_normalized_rmse_percent": 5.0
      },
      "indirect": {
        "absolute_nmbe_percent": 3.0,
        "rms_normalized_rmse_percent": 10.0
      },
      "full": {
        "absolute_nmbe_percent": 5.0,
        "rms_normalized_rmse_percent": 10.0
      }
    },
    "grids": [
      {
        "identifier": "horizontal_louvres_grid",
        "full_identifier": "horizontal_louvres_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.31585086502326987,
            "cvrmse_percent": 10.419867609543624,
            "rms_normalized_rmse_percent": 2.3047036415254367,
            "reference_energy": 2.261935572213133,
            "candidate_energy": 2.2690799152842374,
            "relative_energy_error_percent": 0.3158508650232699,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.1272134725004422e-05,
              "p99": 8.066999725997448e-05,
              "maximum": 0.0002716449089348316
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 95,
              "rgb_channel": 0,
              "reference": 0.0045145913027226925,
              "candidate": 0.004786236211657524,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 1.3137225508783013,
            "cvrmse_percent": 57.58494493907727,
            "rms_normalized_rmse_percent": 5.7871438765312035,
            "reference_energy": 1.5754517910527621,
            "candidate_energy": 1.5961488565100383,
            "relative_energy_error_percent": 1.3137225508783013,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.8052094311069595e-06,
              "p90": 4.8770642024464905e-05,
              "p95": 7.686430471949279e-05,
              "p99": 0.0001913309097290039,
              "maximum": 0.0011698435992002487
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.005670516286045313,
              "candidate": 0.006840359885245562,
              "position": [
                0.5,
                5.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.7255303124958801,
            "cvrmse_percent": 23.956912894586413,
            "rms_normalized_rmse_percent": 5.864307034575808,
            "reference_energy": 3.8373873632658952,
            "candidate_energy": 3.8652287717942757,
            "relative_energy_error_percent": 0.7255303124958801,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.809472900684341e-06,
              "p90": 4.91653845529072e-05,
              "p95": 7.92503647971898e-05,
              "p99": 0.0001987377181649208,
              "maximum": 0.0011698435992002487
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.005670516286045313,
              "candidate": 0.006840359885245562,
              "position": [
                0.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      }
    ]
  },
  "one_bounce_diagnostic": {
    "schema_version": 1,
    "passed": false,
    "matrix_shape": [
      36,
      146,
      3
    ],
    "gates": {
      "direct": {
        "absolute_nmbe_percent": 2.0,
        "rms_normalized_rmse_percent": 5.0
      },
      "indirect": {
        "absolute_nmbe_percent": 3.0,
        "rms_normalized_rmse_percent": 10.0
      },
      "full": {
        "absolute_nmbe_percent": 5.0,
        "rms_normalized_rmse_percent": 10.0
      }
    },
    "grids": [
      {
        "identifier": "horizontal_louvres_grid",
        "full_identifier": "horizontal_louvres_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.31585086502326987,
            "cvrmse_percent": 10.419867609543624,
            "rms_normalized_rmse_percent": 2.3047036415254367,
            "reference_energy": 2.261935572213133,
            "candidate_energy": 2.2690799152842374,
            "relative_energy_error_percent": 0.3158508650232699,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.1272134725004422e-05,
              "p99": 8.066999725997448e-05,
              "maximum": 0.0002716449089348316
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 95,
              "rgb_channel": 0,
              "reference": 0.0045145913027226925,
              "candidate": 0.004786236211657524,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 104.09679533451892,
            "cvrmse_percent": 471.7622364891269,
            "rms_normalized_rmse_percent": 27.684410800943706,
            "reference_energy": 0.7820548352530068,
            "candidate_energy": 1.5961488565100383,
            "relative_energy_error_percent": 104.09679533451892,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.3083849757531425e-06,
              "p90": 0.00011651265253931342,
              "p95": 0.00019204583368264116,
              "p99": 0.0004406122025102377,
              "maximum": 0.0037394571118056774
            },
            "worst": {
              "global_sensor_index": 2,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0039478628896176815,
              "candidate": 0.007687320001423359,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 26.979006317294743,
            "cvrmse_percent": 121.41042378817994,
            "rms_normalized_rmse_percent": 27.731551028043167,
            "reference_energy": 3.04399040746614,
            "candidate_energy": 3.8652287717942757,
            "relative_energy_error_percent": 26.97900631729474,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.330000026835478e-06,
              "p90": 0.00011666117097774986,
              "p95": 0.00019599051747718472,
              "p99": 0.0004570402670651674,
              "maximum": 0.0037394571118056774
            },
            "worst": {
              "global_sensor_index": 2,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0039478628896176815,
              "candidate": 0.007687320001423359,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      }
    ]
  },
  "controlled_skies": {
    "uniform": {
      "bias_percent": 0.6601448832427556,
      "rms_normalized_error_percent": 1.2632649359391541,
      "absolute_error": {
        "p95": 0.14390162033496634,
        "p99": 0.14923787206817266,
        "maximum": 0.15006993379833844
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 5.002892493676079,
      "rms_normalized_to_uniform_percent": 1.2632649359391541
    },
    "overcast": {
      "bias_percent": 0.5724342859295009,
      "rms_normalized_error_percent": 1.2640052867116962,
      "absolute_error": {
        "p95": 0.08288365602493286,
        "p99": 0.10613055825233456,
        "maximum": 0.1150960922241211
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.7727038860321045,
      "rms_normalized_to_uniform_percent": 0.7476501951972545
    },
    "horizon": {
      "bias_percent": 1.4395410027971192,
      "rms_normalized_error_percent": 3.9937305797534615,
      "absolute_error": {
        "p95": 0.0862116325031467,
        "p99": 0.09748742455744577,
        "maximum": 0.09888969270542214
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.9874991845641793,
      "rms_normalized_to_uniform_percent": 0.6652815141983275
    },
    "north": {
      "bias_percent": -6.4336599763532005,
      "rms_normalized_error_percent": 42.86789281964974,
      "absolute_error": {
        "p95": 0.0016762424784246832,
        "p99": 0.002746653789654372,
        "maximum": 0.0032755781430751085
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 0.0022997474297881126,
      "rms_normalized_to_uniform_percent": 0.015739022294369173
    },
    "east": {
      "bias_percent": 0.8632870266695293,
      "rms_normalized_error_percent": 2.075525210967162,
      "absolute_error": {
        "p95": 0.07288026809692383,
        "p99": 0.09405738115310666,
        "maximum": 0.10245251655578613
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.0891461372375488,
      "rms_normalized_to_uniform_percent": 0.5125828226131124
    },
    "south": {
      "bias_percent": 0.6885809014315966,
      "rms_normalized_error_percent": 1.295975406144984,
      "absolute_error": {
        "p95": 0.10852205753326416,
        "p99": 0.12203062772750853,
        "maximum": 0.12679433822631836
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.6996400356292725,
      "rms_normalized_to_uniform_percent": 0.9362541176490806
    },
    "west": {
      "bias_percent": 0.36363679694673806,
      "rms_normalized_error_percent": 1.5310514941818023,
      "absolute_error": {
        "p95": 0.043998152017593384,
        "p99": 0.0482069581747055,
        "maximum": 0.04941040277481079
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.042441725730896,
      "rms_normalized_to_uniform_percent": 0.36271166063219135
    }
  },
  "annual": {
    "schema_version": 1,
    "oracle": "converged-coefficients",
    "passed": true,
    "occupied_hours": 3650,
    "structural": {
      "sun_up_hours_match": true,
      "grid_ids_match": true,
      "grid_counts_match": true
    },
    "grids": [
      {
        "identifier": "horizontal_louvres_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.5948461674809807,
          "cvrmse_percent": 5.9349590237313485,
          "absolute_error_percentiles_lux": {
            "p50": 4.0529937744140625,
            "p90": 30.243289184570326,
            "p95": 45.21844253540036,
            "p99": 89.43567810058583
          },
          "maximum_absolute_error_lux": 435.182861328125,
          "worst": {
            "sensor_index": 2,
            "position": [
              0.5,
              3.5,
              0.75
            ],
            "hour_of_year": 6850.5,
            "foton_lux": 3160.01953125,
            "radiance_lux": 2724.836669921875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.9929375951293756,
            "maximum_error_percentage_points": 5.613561643835617,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.852070116468069,
            "maximum_error_percentage_points": 2.6528744131816566,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.6062861491628618,
            "maximum_error_percentage_points": 3.752328767123288,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.6228424657534237,
            "maximum_error_percentage_points": 3.752328767123288,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.05679223744292239,
            "maximum_error_percentage_points": 0.46780821917808346,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 16.666666666666668,
          "radiance_percent": 19.444444444444443,
          "difference_percentage_points": 2.777777777777775,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 1,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      }
    ]
  },
  "outcomes": {
    "numerical_correctness": "passed",
    "honeybee_compatibility": "passed",
    "performance": "measured"
  },
  "compatibility": {
    "official_loader": {
      "passed": true,
      "tolerance_percentage_points": 0.05,
      "maximum_error_percentage_points": 0.004913447131855264,
      "metrics": {
        "da": [
          {
            "identifier": "horizontal_louvres_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "horizontal_louvres_grid",
            "maximum_error_percentage_points": 0.004913447131855264,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "horizontal_louvres_grid",
            "maximum_error_percentage_points": 0.004794520547953596,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "horizontal_louvres_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "horizontal_louvres_grid",
            "maximum_error_percentage_points": 0.0046575342465753344,
            "passed": true
          }
        ]
      }
    },
    "stock": {
      "status": "not_applicable",
      "passed": true
    }
  },
  "darkness": {
    "required": false,
    "passed": true,
    "maximum_lux": null,
    "tolerance_lux": 1e-06
  },
  "performance": {
    "candidate_cold": {
      "study_preparation_seconds": 0.007683000061661005,
      "weather_seconds": 0.10254037496633828,
      "metric_reduction_seconds": 0.03385358292143792,
      "write_seconds": 0.03728829196188599,
      "total_seconds": 0.17390404199250042,
      "cold_end_to_end_seconds": 0.18158704205416143,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.008763625053688884,
      "engine_upload_seconds": 0.000286,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.015496250009164214,
      "engine_annual_reduction_seconds": 0.00033787498250603676,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.015496250009164214
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007683000061661005,
      "weather_seconds": 0.0989185000071302,
      "metric_reduction_seconds": 0.01265212509315461,
      "write_seconds": 0.02586016699206084,
      "total_seconds": 0.1375887499889359,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1375887499889359,
      "raw_export_seconds": 0.011401499970816076,
      "engine_upload_seconds": 5.6125e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00033837498631328344,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.016336000058799982,
      "full": 0.012382583925500512
    }
  },
  "elapsed_seconds": 82.39426929096226,
  "result_class": "passed"
}
```
