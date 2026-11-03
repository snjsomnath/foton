# Foton report

Status: **passed**

```json
{
  "scene": "plan_t_triangle",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_t_triangle",
    "category": "form",
    "question": "How does a triangle opening illuminate a T-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "t",
    "window_profile": "triangle"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 54,
    "floor_area": 63.0,
    "aperture_area": 1.4400000000000002
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "8779d4fa8a3ab96026014646fac837c9ff5acde7e5b74b897c08f71a322bf237",
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
      "scene_fingerprint": 12153619422812648242,
      "basis": "ReinhartMf2",
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
      "scene_fingerprint": 12153619422812648242,
      "basis": "ReinhartMf2",
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
    "ray_count": 9248,
    "command": [
      "/usr/local/radiance/bin/rcalc",
      "-e",
      "MF:2",
      "-f",
      "/usr/local/radiance/lib/reinhart.cal",
      "-e",
      "Dx=$1;Dy=$2;Dz=$3;$1=rbin"
    ],
    "calibration_sha256": "92b8c09984de7a551773530b3146ba79a51e1b003245f230b6e7b430eb6c26cd"
  },
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 262144,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "plan_t_triangle_grid",
        "bias_percent": 0.08104181010322703,
        "rms_normalized_error_percent": 1.0952511940838772,
        "absolute_error": {
          "p95": 0.0,
          "p99": 2.1606683731079102e-07,
          "maximum": 0.00016772851813584566
        },
        "worst_index": [
          26,
          364,
          0
        ],
        "passed": true
      }
    ],
    "samples_per_patch": [
      256,
      1024
    ]
  },
  "depth_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "plan_t_triangle_grid",
        "bias_percent": 0.12559783847129247,
        "rms_normalized_error_percent": 2.332175194587895,
        "absolute_error": {
          "p95": 4.07363950216677e-06,
          "p99": 4.399102181196213e-05,
          "maximum": 0.0004668179899454117
        },
        "worst_index": [
          24,
          0,
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
        "identifier": "plan_t_triangle_grid",
        "bias_percent": -0.04699603158809496,
        "rms_normalized_error_percent": 2.0995434345775434,
        "absolute_error": {
          "p95": 3.572056584744132e-06,
          "p99": 3.495172131806612e-05,
          "maximum": 0.000447811558842659
        },
        "worst_index": [
          24,
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
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_t_triangle_grid",
            "start_sensor_index": 0,
            "sensor_count": 54,
            "stages": {
              "direct": {
                "nmbe_percent": 0.17990405446623833,
                "cvrmse_percent": 101.75724682275062,
                "rms_normalized_rmse_percent": 10.107353688331747,
                "reference_energy": 2.4640716405192506,
                "candidate_energy": 2.4685046053054975,
                "relative_energy_error_percent": 0.1799040544662383,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.452318772673607e-05,
                  "maximum": 0.0008268144447356462
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 38,
                  "sky_patch_index": 410,
                  "rgb_channel": 0,
                  "reference": 0.0041383723728358746,
                  "candidate": 0.0033115579281002283
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.40797705758728353,
                "cvrmse_percent": 593.1302361988354,
                "rms_normalized_rmse_percent": 9.61231098412579,
                "reference_energy": 0.5377718956461806,
                "candidate_energy": 0.5399658816025692,
                "relative_energy_error_percent": 0.40797705758728353,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00014151565119391307,
                  "maximum": 0.0009081314783543348
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 38,
                  "sky_patch_index": 146,
                  "rgb_channel": 0,
                  "reference": -0.00040472298860549927,
                  "candidate": 0.0005034084897488356
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 135.41670807171613,
            "full": 294.54954201355577
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 120.7494999980554,
            "full": 293.6320420121774
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 124.22333401627839,
            "full": 296.59541591536254
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 132.1535420138389,
            "full": 324.16229194495827
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 8,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_t_triangle_grid",
            "start_sensor_index": 0,
            "sensor_count": 54,
            "stages": {
              "direct": {
                "nmbe_percent": 0.15607812647553268,
                "cvrmse_percent": 50.12993942524475,
                "rms_normalized_rmse_percent": 5.002465616353178,
                "reference_energy": 2.464931668018835,
                "candidate_energy": 2.468778887185181,
                "relative_energy_error_percent": 0.15607812647553268,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.7126959543675184e-05,
                  "maximum": 0.0003808585461229086
                },
                "worst": {
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "sky_patch_index": 141,
                  "rgb_channel": 0,
                  "reference": 0.0016323250019922853,
                  "candidate": 0.0012514664558693767
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.34635131199877756,
                "cvrmse_percent": 180.8785721557805,
                "rms_normalized_rmse_percent": 4.658356662182649,
                "reference_energy": 1.052424409879162,
                "candidate_energy": 1.04877932412775,
                "relative_energy_error_percent": 0.34635131199877756,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.369352614550735e-06,
                  "p95": 5.835830052092206e-06,
                  "p99": 8.110300404950976e-05,
                  "maximum": 0.0008449694141745567
                },
                "worst": {
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.020147795788943768,
                  "candidate": 0.020992765203118324
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 161.29887499846518,
            "full": 3674.06062502414
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 159.5244590425864,
            "full": 3744.6547499857843
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 160.21524998359382,
            "full": 3745.188584085554
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 160.87933303788304,
            "full": 3743.2679580524564
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 12,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_t_triangle_grid",
            "start_sensor_index": 0,
            "sensor_count": 54,
            "stages": {
              "direct": {
                "nmbe_percent": 0.07667657804397629,
                "cvrmse_percent": 48.24718949379077,
                "rms_normalized_rmse_percent": 4.812667906316806,
                "reference_energy": 2.4645658425124566,
                "candidate_energy": 2.466455587264136,
                "relative_energy_error_percent": 0.07667657804397628,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.689343040809035e-05,
                  "maximum": 0.00035351747646927834
                },
                "worst": {
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "sky_patch_index": 363,
                  "rgb_channel": 0,
                  "reference": 0.0037756895180791616,
                  "candidate": 0.00412920699454844
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.36016967144658324,
                "cvrmse_percent": 168.50841810953202,
                "rms_normalized_rmse_percent": 4.368092915186371,
                "reference_energy": 1.0582700640957405,
                "candidate_energy": 1.0544584962828694,
                "relative_energy_error_percent": 0.3601696714465833,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.387338298603936e-06,
                  "p95": 5.589485269297256e-06,
                  "p99": 7.486337563022971e-05,
                  "maximum": 0.0007956605404615402
                },
                "worst": {
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.02058369480073452,
                  "candidate": 0.02137935534119606
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 165.98729195538908,
            "full": 3994.346958003007
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 164.17533298954368,
            "full": 4017.368125030771
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 163.8926670420915,
            "full": 4029.4507909566164
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 170.82849994767457,
            "full": 4129.397416952997
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_t_triangle_grid",
            "start_sensor_index": 0,
            "sensor_count": 54,
            "stages": {
              "direct": {
                "nmbe_percent": -0.09444558731311993,
                "cvrmse_percent": 30.880818931680803,
                "rms_normalized_rmse_percent": 3.08578600872177,
                "reference_energy": 2.468007604471495,
                "candidate_energy": 2.4656766801945196,
                "relative_energy_error_percent": 0.09444558731311993,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.3850548788905144e-05,
                  "maximum": 0.00019670557230710983
                },
                "worst": {
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "sky_patch_index": 144,
                  "rgb_channel": 0,
                  "reference": 0.0017197105335071683,
                  "candidate": 0.0015230049612000585
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.3732219221796649,
                "cvrmse_percent": 99.4919207378072,
                "rms_normalized_rmse_percent": 2.561669744716779,
                "reference_energy": 1.05141567573013,
                "candidate_energy": 1.0553397895251884,
                "relative_energy_error_percent": 0.3732219221796649,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.6402400433435105e-06,
                  "p95": 4.24209520133445e-06,
                  "p99": 4.889536648988724e-05,
                  "maximum": 0.0003638952039182186
                },
                "worst": {
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.010705339722335339,
                  "candidate": 0.011069234926253557
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 240.2456250274554,
            "full": 7164.78350001853
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 234.79875002522022,
            "full": 7247.477957978845
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 240.39016698952764,
            "full": 7161.5708329482
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 236.56250000931323,
            "full": 7238.804708002135
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 6403.995541972108,
      "worker_pool_size": 12,
      "invocation_count": 4
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_t_triangle/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 25954.89500008989,
      "worker_pool_size": 12,
      "invocation_count": 4
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      54,
      578,
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
        "identifier": "plan_t_triangle_grid",
        "full_identifier": "plan_t_triangle_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": -0.019618141410175684,
            "cvrmse_percent": 5.937641252381443,
            "rms_normalized_rmse_percent": 0.5930918488087343,
            "reference_energy": 2.467010401789466,
            "candidate_energy": 2.466526420200239,
            "relative_energy_error_percent": 0.019618141410175684,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.230517566204071e-07,
              "maximum": 8.148001506924629e-05
            },
            "worst": {
              "global_sensor_index": 26,
              "local_sensor_index": 26,
              "sky_patch_index": 451,
              "rgb_channel": 0,
              "reference": 0.004618953447788954,
              "candidate": 0.0045374734327197075,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.4055376062685028,
            "cvrmse_percent": 92.54723904168962,
            "rms_normalized_rmse_percent": 2.385949184169124,
            "reference_energy": 1.0532094595339334,
            "candidate_energy": 1.0384062045074067,
            "relative_energy_error_percent": 1.405537606268503,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.152821821255202e-06,
              "p95": 4.935464858135674e-06,
              "p99": 2.0752777345478535e-05,
              "maximum": 0.0007691783830523491
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015577347949147224,
              "candidate": 0.014808169566094875,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.4342693700389034,
            "cvrmse_percent": 27.62833595347771,
            "rms_normalized_rmse_percent": 2.3807154421328285,
            "reference_energy": 3.5202198613233993,
            "candidate_energy": 3.5049326247076458,
            "relative_energy_error_percent": 0.4342693700389034,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.15093677979894e-06,
              "p95": 4.902702130493708e-06,
              "p99": 2.061217492155265e-05,
              "maximum": 0.0007691783830523491
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015577347949147224,
              "candidate": 0.014808169566094875,
              "position": [
                6.5,
                3.5,
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
      54,
      578,
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
        "identifier": "plan_t_triangle_grid",
        "full_identifier": "plan_t_triangle_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": -0.019618141410175684,
            "cvrmse_percent": 5.937641252381443,
            "rms_normalized_rmse_percent": 0.5930918488087343,
            "reference_energy": 2.467010401789466,
            "candidate_energy": 2.466526420200239,
            "relative_energy_error_percent": 0.019618141410175684,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.230517566204071e-07,
              "maximum": 8.148001506924629e-05
            },
            "worst": {
              "global_sensor_index": 26,
              "local_sensor_index": 26,
              "sky_patch_index": 451,
              "rgb_channel": 0,
              "reference": 0.004618953447788954,
              "candidate": 0.0045374734327197075,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 92.95971862015745,
            "cvrmse_percent": 1775.5584232011884,
            "rms_normalized_rmse_percent": 28.777540521479835,
            "reference_energy": 0.538146620410199,
            "candidate_energy": 1.0384062045074067,
            "relative_energy_error_percent": 92.95971862015743,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.83999996908824e-06,
              "p95": 2.158554457309947e-05,
              "p99": 7.209600880742073e-05,
              "maximum": 0.00678885355591774
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.016653547063469887,
              "candidate": 0.023442400619387627,
              "position": [
                6.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 16.630598628159653,
            "cvrmse_percent": 317.9394862056627,
            "rms_normalized_rmse_percent": 28.77595377856777,
            "reference_energy": 3.005157022199665,
            "candidate_energy": 3.5049326247076458,
            "relative_energy_error_percent": 16.630598628159653,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.83999996908824e-06,
              "p95": 2.1682704755221494e-05,
              "p99": 7.119996007531881e-05,
              "maximum": 0.00678885355591774
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.016653547063469887,
              "candidate": 0.023442400619387627,
              "position": [
                6.5,
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
      "bias_percent": 0.014777333739146173,
      "rms_normalized_error_percent": 0.13252634233729202,
      "absolute_error": {
        "p95": 0.03626317701278494,
        "p99": 0.042836704083277936,
        "maximum": 0.043960959676262235
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.074574437259305,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.13252634233729202
    },
    "overcast": {
      "bias_percent": 0.011456360167661201,
      "rms_normalized_error_percent": 0.11189766266546905,
      "absolute_error": {
        "p95": 0.023235893249511703,
        "p99": 0.027140483856201172,
        "maximum": 0.02758932113647461
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.970133662223816,
      "reference_fraction_of_uniform": 0.6407825350761414,
      "rms_normalized_to_uniform_percent": 0.07630072955665285
    },
    "horizon": {
      "bias_percent": 0.2633229897541829,
      "rms_normalized_error_percent": 0.9789558221527296,
      "absolute_error": {
        "p95": 0.01752998953884074,
        "p99": 0.01908476974878635,
        "maximum": 0.0202154165883206
      },
      "worst_index": [
        26
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3632661353740149,
      "reference_fraction_of_uniform": 0.11815168010628249,
      "rms_normalized_to_uniform_percent": 0.06818144467529733
    },
    "north": {
      "bias_percent": -90.81647063959632,
      "rms_normalized_error_percent": 100.29878051686137,
      "absolute_error": {
        "p95": 6.175143244035986e-05,
        "p99": 0.00016628925257464278,
        "maximum": 0.00021640337945427746
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.1123310287075583e-05,
      "reference_fraction_of_uniform": 3.617837364799925e-06,
      "rms_normalized_to_uniform_percent": 0.00033809970679923173
    },
    "east": {
      "bias_percent": -0.09862140233293751,
      "rms_normalized_error_percent": 0.23864943278838713,
      "absolute_error": {
        "p95": 0.009285502508282625,
        "p99": 0.020933458805084213,
        "maximum": 0.027530431747436523
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.47579169273376465,
      "reference_fraction_of_uniform": 0.15475042164325714,
      "rms_normalized_to_uniform_percent": 0.04700128257520366
    },
    "south": {
      "bias_percent": 0.04539126741448998,
      "rms_normalized_error_percent": 0.16449847491318026,
      "absolute_error": {
        "p95": 0.02749295234680176,
        "p99": 0.03951008796691892,
        "maximum": 0.052165985107421875
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.285184621810913,
      "reference_fraction_of_uniform": 0.7432523369789124,
      "rms_normalized_to_uniform_percent": 0.11493826852433174
    },
    "west": {
      "bias_percent": -0.15360999555736107,
      "rms_normalized_error_percent": 0.2214795764003437,
      "absolute_error": {
        "p95": 0.010391446948051443,
        "p99": 0.020427043139934528,
        "maximum": 0.025702476501464844
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.48550334572792053,
      "reference_fraction_of_uniform": 0.15790912508964539,
      "rms_normalized_to_uniform_percent": 0.044241554378005886
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
        "identifier": "plan_t_triangle_grid",
        "sensor_count": 54,
        "illuminance": {
          "nmbe_percent": -0.029163319723761596,
          "cvrmse_percent": 3.3167420166637553,
          "absolute_error_percentiles_lux": {
            "p50": 0.3354121446609497,
            "p90": 5.477584743499756,
            "p95": 11.13925800323486,
            "p99": 37.10395385742185
          },
          "maximum_absolute_error_lux": 370.353515625,
          "worst": {
            "sensor_index": 38,
            "position": [
              6.5,
              0.5,
              0.75
            ],
            "hour_of_year": 2723.5,
            "foton_lux": 33070.49609375,
            "radiance_lux": 32700.142578125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.058257229832572324,
            "maximum_error_percentage_points": 1.312876712328766,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.20018693801558063,
            "maximum_error_percentage_points": 0.8322628450421163,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.20386352105530262,
            "maximum_error_percentage_points": 2.7417808219178,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.20820649416539883,
            "maximum_error_percentage_points": 2.7417808219178106,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.006392694063926911,
            "maximum_error_percentage_points": 0.22273972602739178,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 11.11111111111111,
          "radiance_percent": 11.11111111111111,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.0,
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
            "identifier": "plan_t_triangle_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_t_triangle_grid",
            "maximum_error_percentage_points": 0.004881361869916501,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_t_triangle_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_t_triangle_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_t_triangle_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
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
      "study_preparation_seconds": 0.009207749972119927,
      "weather_seconds": 0.173789499909617,
      "metric_reduction_seconds": 0.15771308296825737,
      "write_seconds": 0.0407695829635486,
      "total_seconds": 0.37246187508571893,
      "cold_end_to_end_seconds": 0.38166962505783886,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.01902274996973574,
      "engine_upload_seconds": 0.000916875,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.1050361666129902,
      "engine_annual_reduction_seconds": 0.002244791714474559,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.1050361666129902
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.009207749972119927,
      "weather_seconds": 0.11345099995378405,
      "metric_reduction_seconds": 0.04572795797139406,
      "write_seconds": 0.027447375003248453,
      "total_seconds": 0.18681137496605515,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.18681137496605515,
      "raw_export_seconds": 0.014891083003021777,
      "engine_upload_seconds": 7.1458e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.002315833349712193,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01222141704056412,
      "full": 0.09491045807953924
    }
  },
  "elapsed_seconds": 99.19409408303909,
  "result_class": "passed"
}
```
