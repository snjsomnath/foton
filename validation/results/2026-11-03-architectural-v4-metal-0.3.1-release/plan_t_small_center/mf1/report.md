# Foton report

Status: **passed**

```json
{
  "scene": "plan_t_small_center",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_t_small_center",
    "category": "form",
    "question": "How does a small center opening illuminate a T-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "t",
    "window_profile": "small_center"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 54,
    "floor_area": 63.0,
    "aperture_area": 1.4399999999999993
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "676c57b4f4f9f92b56e9ac5b6f4bda3c9af52e50cdce388a0218fd331fc71a47",
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 7077756305093146598,
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 7077756305093146598,
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
    "maximum_samples": 65536,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/refbundle/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "36f62ce5f70cb040065dba1add956594cc902554565f4c4a0b72ef16f23bc13c",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "ac3c34594b2170933cb2e75470e0a8f06dd50696589dcbda19cdd379ce27d048",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00043346919119358063,
          "p95": 0.0,
          "p99": 2.0692517282442725e-05
        },
        "bias_percent": 0.13572691866453915,
        "identifier": "plan_t_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0391215787378878,
        "worst_index": [
          26,
          132,
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
          "maximum": 0.00034443195909261703,
          "p95": 9.79998912953306e-06,
          "p99": 6.543817464262464e-05
        },
        "bias_percent": -0.06565706585926727,
        "identifier": "plan_t_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1975528357935754,
        "worst_index": [
          35,
          0,
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
          "maximum": 0.00023163435980677605,
          "p95": 8.554481610190123e-06,
          "p99": 5.8012343943119604e-05
        },
        "bias_percent": 0.00894326531655726,
        "identifier": "plan_t_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.868418531845953,
        "worst_index": [
          37,
          49,
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
            "identifier": "plan_t_small_center_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007954593747854233,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.524091263301746e-05
                },
                "candidate_energy": 2.424933885667997,
                "cvrmse_percent": 33.718731964216126,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.06517669913036726,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4265154083150264,
                "relative_energy_error_percent": 0.06517669913036726,
                "rms_normalized_rmse_percent": 3.3658193362063997,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.015739809721708298,
                  "global_sensor_index": 38,
                  "local_sensor_index": 38,
                  "reference": 0.014944350346922874,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010654203360900283,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1019154953828547e-05,
                  "p99": 0.00026247910223901297
                },
                "candidate_energy": 0.5721424681506697,
                "cvrmse_percent": 226.59499320947356,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.007205717100224453,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.5721836980892476,
                "relative_energy_error_percent": 0.007205717100224452,
                "rms_normalized_rmse_percent": 4.802433846897593,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0004628598690032959,
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "reference": 0.0006025604670867324,
                  "rgb_channel": 0,
                  "sky_patch_index": 73
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.47854095324874,
            "full": 309.06604207120836
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.3681670781225,
            "full": 306.75054097082466
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.35183298960328,
            "full": 291.6784998960793
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 125.29691692907363,
            "full": 289.83749996405095
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
            "identifier": "plan_t_small_center_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00037426967173814774,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.04159471206369e-05
                },
                "candidate_energy": 2.4253669078607345,
                "cvrmse_percent": 16.470299348351848,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.08927355793275966,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.427534053880663,
                "relative_energy_error_percent": 0.08927355793275966,
                "rms_normalized_rmse_percent": 1.6457139704569488,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.01795506477355957,
                  "global_sensor_index": 38,
                  "local_sensor_index": 38,
                  "reference": 0.017580795101821423,
                  "rgb_channel": 0,
                  "sky_patch_index": 119
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009443145245313644,
                  "p50": 0.0,
                  "p90": 5.7117304095299914e-06,
                  "p95": 1.4525590813718736e-05,
                  "p99": 0.00011944870580919233
                },
                "candidate_energy": 1.091269756960088,
                "cvrmse_percent": 65.9512862769721,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.7469515148691781,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.0994823570820316,
                "relative_energy_error_percent": 0.7469515148691781,
                "rms_normalized_rmse_percent": 2.4284458197080583,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.024052745662629604,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.02499706018716097,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 167.6587499678135,
            "full": 3742.7144169341773
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 161.47158294916153,
            "full": 3647.0015830127522
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 160.25854100007564,
            "full": 3716.728665982373
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 169.3918340606615,
            "full": 3677.682499983348
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
            "identifier": "plan_t_small_center_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00042106950422748923,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.985565181821593e-05
                },
                "candidate_energy": 2.4255910411193327,
                "cvrmse_percent": 17.58542748926421,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.023045539833572205,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4250321793624607,
                "relative_energy_error_percent": 0.023045539833572205,
                "rms_normalized_rmse_percent": 1.7538555797705708,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002222639974206686,
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "reference": 0.0018015704699791968,
                  "rgb_channel": 0,
                  "sky_patch_index": 17
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007435674197040498,
                  "p50": 0.0,
                  "p90": 5.300156772136688e-06,
                  "p95": 1.4155282769934274e-05,
                  "p99": 0.00013821717468090556
                },
                "candidate_energy": 1.0942850316572255,
                "cvrmse_percent": 65.90659512139852,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.01507438661009152,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.0941200997634084,
                "relative_energy_error_percent": 0.015074386610091518,
                "rms_normalized_rmse_percent": 2.425759900442269,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00020648946519941092,
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "reference": 0.0005370779545046389,
                  "rgb_channel": 0,
                  "sky_patch_index": 17
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 163.28195901587605,
            "full": 3947.84883398097
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 165.39295797701925,
            "full": 3992.7806250052527
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 163.84233394637704,
            "full": 3933.8991249678656
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 164.03012501541525,
            "full": 3996.227749972604
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
            "identifier": "plan_t_small_center_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00022873259149491787,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.5240022807556694e-05
                },
                "candidate_energy": 2.4247478656925523,
                "cvrmse_percent": 8.991747679800033,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.017827302893537466,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.425180209914288,
                "relative_energy_error_percent": 0.017827302893537463,
                "rms_normalized_rmse_percent": 0.8974713146240492,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00371081056073308,
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "reference": 0.003482077969238162,
                  "rgb_channel": 0,
                  "sky_patch_index": 72
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00031722523272037506,
                  "p50": 7.105427357601002e-15,
                  "p90": 3.813154762610793e-06,
                  "p95": 9.042189049068838e-06,
                  "p99": 6.963745327084345e-05
                },
                "candidate_energy": 1.0954006911156107,
                "cvrmse_percent": 31.81167752589387,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.09792158091302874,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.0943291067538858,
                "relative_energy_error_percent": 0.09792158091302874,
                "rms_normalized_rmse_percent": 1.1692704233945852,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.020626519806683064,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.02094374503940344,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 243.93283296376467,
            "full": 7193.326374981552
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 233.28170797321945,
            "full": 6959.274166030809
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 238.6056249961257,
            "full": 7029.656416038051
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 241.2617920199409,
            "full": 7090.655124979094
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/suite-0.3.1/run/plan_t_small_center/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1667.434124974534,
      "invocation_count": 4,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_small_center/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 6708.069875021465,
      "invocation_count": 4,
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
      54,
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
        "identifier": "plan_t_small_center_grid",
        "full_identifier": "plan_t_small_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": -0.051096950471465744,
            "cvrmse_percent": 5.808873894179545,
            "rms_normalized_rmse_percent": 0.5797006092934287,
            "reference_energy": 2.425289561786485,
            "candidate_energy": 2.4240503127803095,
            "relative_energy_error_percent": 0.051096950471465744,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.125816634157726e-05,
              "maximum": 0.0002165650948882103
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 121,
              "rgb_channel": 0,
              "reference": 0.006629771552979946,
              "candidate": 0.006413206458091736,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.640220745632949,
            "cvrmse_percent": 49.61512816051051,
            "rms_normalized_rmse_percent": 1.8242094908301447,
            "reference_energy": 1.0945393793893015,
            "candidate_energy": 1.076586517419436,
            "relative_energy_error_percent": 1.640220745632949,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.4761308559106965e-08,
              "p90": 9.234197932528332e-06,
              "p95": 2.066443266812712e-05,
              "p99": 5.805788394354822e-05,
              "maximum": 0.000728844664990902
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015338774770498276,
              "candidate": 0.014609930105507374,
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
            "nmbe_percent": -0.5452569229012039,
            "cvrmse_percent": 15.296304248848426,
            "rms_normalized_rmse_percent": 1.8085781234025915,
            "reference_energy": 3.5198289411757866,
            "candidate_energy": 3.5006368301997455,
            "relative_energy_error_percent": 0.545256922901204,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.4761308559106965e-08,
              "p90": 9.205456990457606e-06,
              "p95": 2.044536086032167e-05,
              "p99": 5.877137169591175e-05,
              "maximum": 0.000728844664990902
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015338774770498276,
              "candidate": 0.014609930105507374,
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
        "identifier": "plan_t_small_center_grid",
        "full_identifier": "plan_t_small_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": -0.051096950471465744,
            "cvrmse_percent": 5.808873894179545,
            "rms_normalized_rmse_percent": 0.5797006092934287,
            "reference_energy": 2.425289561786485,
            "candidate_energy": 2.4240503127803095,
            "relative_energy_error_percent": 0.051096950471465744,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.125816634157726e-05,
              "maximum": 0.0002165650948882103
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 121,
              "rgb_channel": 0,
              "reference": 0.006629771552979946,
              "candidate": 0.006413206458091736,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 88.0178100139579,
            "cvrmse_percent": 855.2104528172259,
            "rms_normalized_rmse_percent": 18.181492252017524,
            "reference_energy": 0.5725981583018722,
            "candidate_energy": 1.076586517419436,
            "relative_energy_error_percent": 88.0178100139579,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.359000038472004e-05,
              "p95": 9.375810623168945e-05,
              "p99": 0.00023310285701882177,
              "maximum": 0.006504707038402557
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0176383126527071,
              "candidate": 0.024143019691109657,
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
            "nmbe_percent": 16.77011139351712,
            "cvrmse_percent": 163.3167070017975,
            "rms_normalized_rmse_percent": 18.178270252941633,
            "reference_energy": 2.9978877200883574,
            "candidate_energy": 3.5006368301997455,
            "relative_energy_error_percent": 16.770111393517116,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.387999822734855e-05,
              "p95": 9.256090561393648e-05,
              "p99": 0.0002270550525281599,
              "maximum": 0.006504707038402557
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0176383126527071,
              "candidate": 0.024143019691109657,
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
      "bias_percent": 0.00544536149789479,
      "rms_normalized_error_percent": 0.23644247792339398,
      "absolute_error": {
        "p95": 0.0440545072714866,
        "p99": 0.09333616918451015,
        "maximum": 0.10424718706291003
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.0756738614096544,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.23644247792339398
    },
    "overcast": {
      "bias_percent": -0.03989572938360608,
      "rms_normalized_error_percent": 0.18300570508788347,
      "absolute_error": {
        "p95": 0.02858431637287129,
        "p99": 0.04949607133865355,
        "maximum": 0.05639934539794922
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.0610949993133545,
      "reference_fraction_of_uniform": 0.6701279282569885,
      "rms_normalized_to_uniform_percent": 0.13274535731006767
    },
    "horizon": {
      "bias_percent": 0.4927004805564456,
      "rms_normalized_error_percent": 2.711431747868891,
      "absolute_error": {
        "p95": 0.0229603918203587,
        "p99": 0.02947144895048991,
        "maximum": 0.03042732161352299
      },
      "worst_index": [
        39
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.2387636656579376,
      "reference_fraction_of_uniform": 0.07762970861562889,
      "rms_normalized_to_uniform_percent": 0.10573557309972571
    },
    "north": {
      "bias_percent": -100.0,
      "rms_normalized_error_percent": 100.0,
      "absolute_error": {
        "p95": 2.7629864507616667e-05,
        "p99": 6.753540357749439e-05,
        "maximum": 8.644447370897979e-05
      },
      "worst_index": [
        37
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 6.187060080264928e-06,
      "reference_fraction_of_uniform": 2.011611286434345e-06,
      "rms_normalized_to_uniform_percent": 0.00015646011552645012
    },
    "east": {
      "bias_percent": 0.16294317488042834,
      "rms_normalized_error_percent": 0.24095855018721607,
      "absolute_error": {
        "p95": 0.010849505662918089,
        "p99": 0.01864883542060852,
        "maximum": 0.019678115844726562
      },
      "worst_index": [
        26
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.48922425508499146,
      "reference_fraction_of_uniform": 0.159062460064888,
      "rms_normalized_to_uniform_percent": 0.05445982560699648
    },
    "south": {
      "bias_percent": 0.06204128091433723,
      "rms_normalized_error_percent": 0.2925848526704502,
      "absolute_error": {
        "p95": 0.039365121722221244,
        "p99": 0.07214189529418943,
        "maximum": 0.08005619049072266
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.1821179389953613,
      "reference_fraction_of_uniform": 0.7094764113426208,
      "rms_normalized_to_uniform_percent": 0.18944646613379354
    },
    "west": {
      "bias_percent": -0.4404583158654088,
      "rms_normalized_error_percent": 0.49700129867609116,
      "absolute_error": {
        "p95": 0.02791736721992487,
        "p99": 0.04311706900596618,
        "maximum": 0.045371174812316895
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.48162898421287537,
      "reference_fraction_of_uniform": 0.15659299492835999,
      "rms_normalized_to_uniform_percent": 0.10703525307518212
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
        "identifier": "plan_t_small_center_grid",
        "sensor_count": 54,
        "illuminance": {
          "nmbe_percent": -0.11523970337138117,
          "cvrmse_percent": 2.5843139271235978,
          "absolute_error_percentiles_lux": {
            "p50": 0.4277939796447754,
            "p90": 6.344718170166017,
            "p95": 12.16848526000975,
            "p99": 32.60495025634765
          },
          "maximum_absolute_error_lux": 195.556640625,
          "worst": {
            "sensor_index": 25,
            "position": [
              5.5,
              1.5,
              0.75
            ],
            "hour_of_year": 1954.5,
            "foton_lux": 18330.25,
            "radiance_lux": 18134.693359375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.1399518011161845,
            "maximum_error_percentage_points": 2.273698630136984,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.2616596078600055,
            "maximum_error_percentage_points": 1.1763879865053823,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.28541856925418635,
            "maximum_error_percentage_points": 4.600958904109589,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.28435312024353127,
            "maximum_error_percentage_points": 4.600958904109589,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.004923896499239045,
            "maximum_error_percentage_points": 0.056027397260274725,
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
      "maximum_error_percentage_points": 0.004932062854505537,
      "metrics": {
        "da": [
          {
            "identifier": "plan_t_small_center_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_t_small_center_grid",
            "maximum_error_percentage_points": 0.004932062854505537,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_t_small_center_grid",
            "maximum_error_percentage_points": 0.004520547945205511,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_t_small_center_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_t_small_center_grid",
            "maximum_error_percentage_points": 0.004383561643835243,
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
      "study_preparation_seconds": 0.006452583009377122,
      "weather_seconds": 0.09561187494546175,
      "metric_reduction_seconds": 0.044058125000447035,
      "write_seconds": 0.05192150000948459,
      "total_seconds": 0.191740290960297,
      "cold_end_to_end_seconds": 0.1981928739696741,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.027507666032761335,
      "engine_upload_seconds": 0.000316125,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.022983208298683167,
      "engine_annual_reduction_seconds": 0.00046799995470792055,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.022983208298683167
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006452583009377122,
      "weather_seconds": 0.09426079189870507,
      "metric_reduction_seconds": 0.01324775000102818,
      "write_seconds": 0.0334580410271883,
      "total_seconds": 0.14112024998757988,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14112024998757988,
      "raw_export_seconds": 0.013373957946896553,
      "engine_upload_seconds": 5.8e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0004935832694172859,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.0092827919870615,
      "full": 0.024214250035583973
    }
  },
  "elapsed_seconds": 0.7462041670223698,
  "result_class": "passed"
}
```
