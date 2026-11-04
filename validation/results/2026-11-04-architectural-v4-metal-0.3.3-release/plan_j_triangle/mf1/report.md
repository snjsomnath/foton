# Foton report

Status: **passed**

```json
{
  "scene": "plan_j_triangle",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_j_triangle",
    "category": "form",
    "question": "How does a triangle opening illuminate a J-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "j",
    "window_profile": "triangle"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 47,
    "floor_area": 63.0,
    "aperture_area": 1.4400000000000002
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "498f48b9eea3ab71eed2d8ba462a0caf5bb4001a72b7bc07b56f18ab0382319a",
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 3946307548040165476,
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 3946307548040165476,
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
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.3)",
      "weather_id": "aff05f88fed2459a6796dca3cabd63daf743bc359ea5c7394adb01155f6785fb"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/usr/local/radiance/bin/gendaymtx",
      "weather_id": "fa596a1b71c81c8eee4f32b17ea6d10a57aabce8541ff637ac4a9c1ee69c4ac1"
    },
    "sun_up_hours_equal": true,
    "compared_hours": 4405,
    "max_relative_difference": 0.0,
    "mean_relative_difference": 0.0
  },
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 65536,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/12f3d0b2-7d1e-44d9-9264-d1e29a27929b/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "c9ebbf7b4b91e00907bab1211be1600f1ec57f56211cde6130eff108116d8a4c",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "23633e9e91bc013f4a3a6d776a0b95fe8d48adfbd13e89c51c834683d9ee6bfe",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00039337179623544216,
          "p95": 0.0,
          "p99": 5.759531632065773e-05
        },
        "bias_percent": 0.007892430975283748,
        "identifier": "plan_j_triangle_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.5562490682182268,
        "worst_index": [
          17,
          48,
          0
        ]
      }
    ],
    "passed": true,
    "samples_per_patch": [
      256,
      1024
    ]
  },
  "depth_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00039019808173179626,
          "p95": 1.4589772035833448e-05,
          "p99": 8.036778308451176e-05
        },
        "bias_percent": 0.06677899526990723,
        "identifier": "plan_j_triangle_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3379875590281078,
        "worst_index": [
          18,
          75,
          0
        ]
      }
    ],
    "passed": true
  },
  "sample_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00027792155742645264,
          "p95": 1.1991178325843066e-05,
          "p99": 6.686709821224213e-05
        },
        "bias_percent": 0.011063009978943036,
        "identifier": "plan_j_triangle_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1102230969513986,
        "worst_index": [
          15,
          0,
          0
        ]
      }
    ],
    "passed": true
  },
  "oracle_levels": [
    {
      "material_bounces": 1,
      "repeatability": {
        "gates": {
          "absolute_energy_bias_percent": 1.0,
          "rms_normalized_rmse_percent": 5.0
        },
        "grids": [
          {
            "identifier": "plan_j_triangle_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005769748240709305,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00013366993516683578
                },
                "candidate_energy": 2.6369439725185657,
                "cvrmse_percent": 19.251047115904612,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.2039441019665414,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.631577026384548,
                "relative_energy_error_percent": 0.2039441019665414,
                "rms_normalized_rmse_percent": 2.3239795139060013,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.015299810096621513,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.014722835272550583,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008561522699892521,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1604039173107594e-05,
                  "p99": 0.00022326060570776463
                },
                "candidate_energy": 0.6177805488082626,
                "cvrmse_percent": 146.8063703064862,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.19357309715746268,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.618978725097179,
                "relative_energy_error_percent": 0.19357309715746268,
                "rms_normalized_rmse_percent": 3.84733753885901,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0006980993784964085,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": -0.00015805289149284363,
                  "rgb_channel": 0,
                  "sky_patch_index": 46
                }
              }
            },
            "start_sensor_index": 0
          }
        ],
        "half_run_count": 2,
        "oracle_stable": true,
        "run_count": 4,
        "schema_version": 1
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 109.60058297496289,
            "full": 256.3389170682058
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 117.71695897914469,
            "full": 262.969792005606
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.47008303366601,
            "full": 271.51533297728747
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 111.80279206018895,
            "full": 269.8843750404194
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        }
      ],
      "samples": 20000
    },
    {
      "material_bounces": 8,
      "repeatability": {
        "gates": {
          "absolute_energy_bias_percent": 1.0,
          "rms_normalized_rmse_percent": 5.0
        },
        "grids": [
          {
            "identifier": "plan_j_triangle_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003463629400357604,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.2705013230443e-05
                },
                "candidate_energy": 2.6361456474633087,
                "cvrmse_percent": 14.79152756296051,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.04361910968085852,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.6372960125036116,
                "relative_energy_error_percent": 0.043619109680858525,
                "rms_normalized_rmse_percent": 1.7891866699736485,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0021682579535990953,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.001821895013563335,
                  "rgb_channel": 0,
                  "sky_patch_index": 14
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005721496418118477,
                  "p50": 6.095068627587352e-08,
                  "p90": 1.067334960680455e-05,
                  "p95": 2.1538551663979888e-05,
                  "p99": 0.00016246037557721138
                },
                "candidate_energy": 1.2746419662695097,
                "cvrmse_percent": 50.74866859943034,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.7500796162598873,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.2651523166278444,
                "relative_energy_error_percent": 0.7500796162598873,
                "rms_normalized_rmse_percent": 2.4924714486892925,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.000287357484921813,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.0002847921568900347,
                  "rgb_channel": 0,
                  "sky_patch_index": 50
                }
              }
            },
            "start_sensor_index": 0
          }
        ],
        "half_run_count": 2,
        "oracle_stable": true,
        "run_count": 4,
        "schema_version": 1
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.92466602195054,
            "full": 3125.453417073004
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 145.34191600978374,
            "full": 3075.1144170062616
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.55129204504192,
            "full": 3107.2310409508646
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 161.41229204367846,
            "full": 3076.6153329750523
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        }
      ],
      "samples": 40000
    },
    {
      "material_bounces": 12,
      "repeatability": {
        "gates": {
          "absolute_energy_bias_percent": 1.0,
          "rms_normalized_rmse_percent": 5.0
        },
        "grids": [
          {
            "identifier": "plan_j_triangle_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003983678761869669,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00011304544750601053
                },
                "candidate_energy": 2.6365286692844165,
                "cvrmse_percent": 16.494300718719465,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.06474743138897933,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.6348226892714592,
                "relative_energy_error_percent": 0.06474743138897932,
                "rms_normalized_rmse_percent": 1.9936829158134957,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0026211539516225457,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.002222786075435579,
                  "rgb_channel": 0,
                  "sky_patch_index": 15
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005117704859003425,
                  "p50": 6.249042883155198e-08,
                  "p90": 1.0203219062532298e-05,
                  "p95": 2.2131265723146498e-05,
                  "p99": 0.00017967703752219677
                },
                "candidate_energy": 1.2731527314552906,
                "cvrmse_percent": 53.07918512801291,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.0625431258315446,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.2739494992936642,
                "relative_energy_error_percent": 0.0625431258315446,
                "rms_normalized_rmse_percent": 2.6271384187947624,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0001441295025870204,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.0006558999884873629,
                  "rgb_channel": 0,
                  "sky_patch_index": 15
                }
              }
            },
            "start_sensor_index": 0
          }
        ],
        "half_run_count": 2,
        "oracle_stable": true,
        "run_count": 4,
        "schema_version": 1
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.2773749679327,
            "full": 3338.038207963109
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.03095894865692,
            "full": 3300.558082992211
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 145.35470900591463,
            "full": 3306.050750077702
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.3890839200467,
            "full": 3390.575999976136
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        }
      ],
      "samples": 40000
    },
    {
      "material_bounces": 12,
      "repeatability": {
        "gates": {
          "absolute_energy_bias_percent": 1.0,
          "rms_normalized_rmse_percent": 5.0
        },
        "grids": [
          {
            "identifier": "plan_j_triangle_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00018182490020990372,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.413005758076906e-05
                },
                "candidate_energy": 2.635798520010212,
                "cvrmse_percent": 9.027223006909237,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.01933862468809378,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.6352888913820607,
                "relative_energy_error_percent": 0.019338624688093775,
                "rms_normalized_rmse_percent": 1.092149351155354,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013496140018105507,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.01367796491831541,
                  "rgb_channel": 0,
                  "sky_patch_index": 72
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00034228991717100143,
                  "p50": 5.000000058430487e-08,
                  "p90": 7.042583092697896e-06,
                  "p95": 1.4457382349064574e-05,
                  "p99": 9.236740879714489e-05
                },
                "candidate_energy": 1.2721798995300446,
                "cvrmse_percent": 29.51894262404828,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.3033841370844658,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.2760512365628465,
                "relative_energy_error_percent": 0.3033841370844658,
                "rms_normalized_rmse_percent": 1.4615139237351238,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.01651623472571373,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.01617394480854273,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          }
        ],
        "half_run_count": 2,
        "oracle_stable": true,
        "run_count": 4,
        "schema_version": 1
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 214.40891700331122,
            "full": 5816.03604205884
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 222.78325003571808,
            "full": 5821.317750029266
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 221.22545808088034,
            "full": 5994.08770899754
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 212.84104196820408,
            "full": 5859.29941595532
          },
          "versions": {
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]"
          }
        }
      ],
      "samples": 80000
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton-0.3.3/validation/results/2026-11-04-architectural-v4-metal-0.3.3-release/plan_j_triangle/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1295.646750018932,
      "invocation_count": 3,
      "sample_count": 256,
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "worker_pool_size": 12
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_triangle/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4622.301792027429,
      "invocation_count": 3,
      "sample_count": 1024,
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "worker_pool_size": 12
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      47,
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
        "identifier": "plan_j_triangle_grid",
        "full_identifier": "plan_j_triangle_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": -0.05266435454164955,
            "cvrmse_percent": 7.893978596738905,
            "rms_normalized_rmse_percent": 0.9542526483726724,
            "reference_energy": 2.6350590688556963,
            "candidate_energy": 2.6336713320052922,
            "relative_energy_error_percent": 0.05266435454164955,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.205041866749525e-05,
              "maximum": 0.000261625275015831
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 50,
              "rgb_channel": 0,
              "reference": 0.005460815038532019,
              "candidate": 0.005199189763516188,
              "position": [
                6.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.40848115394815593,
            "cvrmse_percent": 33.83018374461491,
            "rms_normalized_rmse_percent": 1.673274961803046,
            "reference_energy": 1.2746001983930881,
            "candidate_energy": 1.2693936967944666,
            "relative_energy_error_percent": 0.40848115394815593,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 9.74040368362239e-08,
              "p90": 1.598987728357315e-05,
              "p95": 2.7011807105736807e-05,
              "p99": 7.547250424977392e-05,
              "maximum": 0.0006000879220664501
            },
            "worst": {
              "global_sensor_index": 2,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0063374778255820274,
              "candidate": 0.005737389903515577,
              "position": [
                0.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.16866529787558623,
            "cvrmse_percent": 10.684066141730826,
            "rms_normalized_rmse_percent": 1.6209307147228844,
            "reference_energy": 3.9096592672487844,
            "candidate_energy": 3.903065028799759,
            "relative_energy_error_percent": 0.16866529787558623,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 9.74040368362239e-08,
              "p90": 1.5724519471405074e-05,
              "p95": 2.5809742510318756e-05,
              "p99": 7.221636769827455e-05,
              "maximum": 0.0006000879220664501
            },
            "worst": {
              "global_sensor_index": 2,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0063374778255820274,
              "candidate": 0.005737389903515577,
              "position": [
                0.5,
                2.5,
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
      47,
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
        "identifier": "plan_j_triangle_grid",
        "full_identifier": "plan_j_triangle_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": -0.05266435454164955,
            "cvrmse_percent": 7.893978596738905,
            "rms_normalized_rmse_percent": 0.9542526483726724,
            "reference_energy": 2.6350590688556963,
            "candidate_energy": 2.6336713320052922,
            "relative_energy_error_percent": 0.05266435454164955,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.205041866749525e-05,
              "maximum": 0.000261625275015831
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 50,
              "rgb_channel": 0,
              "reference": 0.005460815038532019,
              "candidate": 0.005199189763516188,
              "position": [
                6.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 105.54284890775837,
            "cvrmse_percent": 702.0661398138471,
            "rms_normalized_rmse_percent": 18.350676840156336,
            "reference_energy": 0.617581055989028,
            "candidate_energy": 1.2693936967944666,
            "relative_energy_error_percent": 105.54284890775838,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.80800003465265e-05,
              "p95": 0.00010898999607888982,
              "p99": 0.00027054455131292343,
              "maximum": 0.004894617944955826
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.013781771063804626,
              "candidate": 0.018676389008760452,
              "position": [
                4.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 19.99682962117073,
            "cvrmse_percent": 133.22137420835816,
            "rms_normalized_rmse_percent": 18.339606710950733,
            "reference_energy": 3.2526401248447243,
            "candidate_energy": 3.903065028799759,
            "relative_energy_error_percent": 19.996829621170733,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.757999653927982e-05,
              "p95": 0.00011002831206496921,
              "p99": 0.0002714991569519043,
              "maximum": 0.004894617944955826
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.013781771063804626,
              "candidate": 0.018676389008760452,
              "position": [
                4.5,
                1.5,
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
      "bias_percent": -0.06780624494786379,
      "rms_normalized_error_percent": 0.2398105383710367,
      "absolute_error": {
        "p95": 0.04905665250046027,
        "p99": 0.07892360800639091,
        "maximum": 0.09892380145861157
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.8466329100502894,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2398105383710367
    },
    "overcast": {
      "bias_percent": -0.06051727960345222,
      "rms_normalized_error_percent": 0.2058084631449693,
      "absolute_error": {
        "p95": 0.0258441925048828,
        "p99": 0.04749420166015623,
        "maximum": 0.05900466442108154
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.413738489151001,
      "reference_fraction_of_uniform": 0.6274938583374023,
      "rms_normalized_to_uniform_percent": 0.14070613886658295
    },
    "horizon": {
      "bias_percent": -0.3496984501960102,
      "rms_normalized_error_percent": 1.6766707705164037,
      "absolute_error": {
        "p95": 0.01998849345802193,
        "p99": 0.02684193126327283,
        "maximum": 0.030331141459994382
      },
      "worst_index": [
        42
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3981209645921842,
      "reference_fraction_of_uniform": 0.10349855936395536,
      "rms_normalized_to_uniform_percent": 0.09407426222130405
    },
    "north": {
      "bias_percent": -67.88410201278201,
      "rms_normalized_error_percent": 105.36433014621176,
      "absolute_error": {
        "p95": 9.704245790658182e-05,
        "p99": 0.0002678519216715357,
        "maximum": 0.0003228952700737864
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.580978096171748e-05,
      "reference_fraction_of_uniform": 4.1100311136688106e-06,
      "rms_normalized_to_uniform_percent": 0.0005215878887039946
    },
    "east": {
      "bias_percent": 0.11363611037889854,
      "rms_normalized_error_percent": 0.35647064274676943,
      "absolute_error": {
        "p95": 0.019841642677783964,
        "p99": 0.028526272773742676,
        "maximum": 0.02926960587501526
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.892891526222229,
      "reference_fraction_of_uniform": 0.23212288320064545,
      "rms_normalized_to_uniform_percent": 0.08332783007404856
    },
    "south": {
      "bias_percent": -0.053798180431798175,
      "rms_normalized_error_percent": 0.24643622004438387,
      "absolute_error": {
        "p95": 0.030000193417072288,
        "p99": 0.059772610664367676,
        "maximum": 0.060126304626464844
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.6027655601501465,
      "reference_fraction_of_uniform": 0.6766347289085388,
      "rms_normalized_to_uniform_percent": 0.16710143807738273
    },
    "west": {
      "bias_percent": -0.3845000958629718,
      "rms_normalized_error_percent": 0.4372772040202221,
      "absolute_error": {
        "p95": 0.020582393556833247,
        "p99": 0.041878348588943466,
        "maximum": 0.0514984130859375
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.8271421790122986,
      "reference_fraction_of_uniform": 0.21503017842769623,
      "rms_normalized_to_uniform_percent": 0.09640192130984498
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
        "identifier": "plan_j_triangle_grid",
        "sensor_count": 47,
        "illuminance": {
          "nmbe_percent": -0.0664269291186862,
          "cvrmse_percent": 2.508829187936234,
          "absolute_error_percentiles_lux": {
            "p50": 0.9238662719726562,
            "p90": 10.813509368896485,
            "p95": 17.402947998046862,
            "p99": 36.344748535156256
          },
          "maximum_absolute_error_lux": 196.2685546875,
          "worst": {
            "sensor_index": 19,
            "position": [
              5.5,
              1.5,
              0.75
            ],
            "hour_of_year": 1861.5,
            "foton_lux": 8453.55859375,
            "radiance_lux": 8649.8271484375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.22343923054503026,
            "maximum_error_percentage_points": 2.3561643835616444,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.4032887130900714,
            "maximum_error_percentage_points": 1.5271532865569704,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.6376508306616135,
            "maximum_error_percentage_points": 3.5845205479452176,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.6360507140775286,
            "maximum_error_percentage_points": 3.584520547945205,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.007102885456135315,
            "maximum_error_percentage_points": 0.08287671232876903,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 12.76595744680851,
          "radiance_percent": 12.76595744680851,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.127659574468085,
          "ambiguous_sensor_count": 0,
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
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "plan_j_triangle_grid",
            "maximum_error_percentage_points": 0.004520547945205511,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_j_triangle_grid",
            "maximum_error_percentage_points": 0.004889271357288116,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_j_triangle_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_j_triangle_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_j_triangle_grid",
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
      "study_preparation_seconds": 0.0059244579169899225,
      "weather_seconds": 0.07746729196514934,
      "metric_reduction_seconds": 0.03592474991455674,
      "write_seconds": 0.010383750079199672,
      "total_seconds": 0.12389770802110434,
      "cold_end_to_end_seconds": 0.12982216593809426,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0020012500463053584,
      "engine_upload_seconds": 0.000239958,
      "engine_acceleration_structure_seconds": 0.002602125,
      "engine_tracing_seconds": 0.014195999945513904,
      "engine_annual_reduction_seconds": 0.000715250032953918,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.014195999945513904
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.0059244579169899225,
      "weather_seconds": 0.07331474998500198,
      "metric_reduction_seconds": 0.013673709006980062,
      "write_seconds": 0.010426082997582853,
      "total_seconds": 0.09752000006847084,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.09752000006847084,
      "raw_export_seconds": 0.0018601249903440475,
      "engine_upload_seconds": 4.0334e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0004889999981969595,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.014671459095552564,
      "full": 0.03728050005156547
    }
  },
  "elapsed_seconds": 0.7644527500960976,
  "result_class": "passed"
}
```
