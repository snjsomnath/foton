# Foton report

Status: **passed**

```json
{
  "scene": "plan_i_large_center",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_i_large_center",
    "category": "form",
    "question": "How does a large center opening illuminate a I-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "i",
    "window_profile": "large_center"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 74,
    "floor_area": 90.0,
    "aperture_area": 4.800000000000001
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "ff3bdf8b69a3bb177bf3b66e048fc97558de09792f5dd7355f696f08fee5c827",
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 5535031717744390830,
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 5535031717744390830,
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
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "plan_i_large_center_grid",
        "bias_percent": -0.11873487137665646,
        "rms_normalized_error_percent": 1.015976769220981,
        "absolute_error": {
          "p95": 0.0,
          "p99": 4.025897942483425e-05,
          "maximum": 0.00037325965240597725
        },
        "worst_index": [
          36,
          135,
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
        "identifier": "plan_i_large_center_grid",
        "bias_percent": 0.049691870962604606,
        "rms_normalized_error_percent": 0.9927347705816938,
        "absolute_error": {
          "p95": 2.1524872863665223e-05,
          "p99": 0.00010549696162343025,
          "maximum": 0.00045307353138923645
        },
        "worst_index": [
          35,
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
        "identifier": "plan_i_large_center_grid",
        "bias_percent": -0.03343530807638633,
        "rms_normalized_error_percent": 0.8209649588946059,
        "absolute_error": {
          "p95": 1.904543023556471e-05,
          "p99": 8.842442184686661e-05,
          "maximum": 0.000436246395111084
        },
        "worst_index": [
          52,
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_i_large_center_grid",
            "start_sensor_index": 0,
            "sensor_count": 74,
            "stages": {
              "direct": {
                "nmbe_percent": -0.06669400459505197,
                "cvrmse_percent": 17.263655791355568,
                "rms_normalized_rmse_percent": 2.5653022853447442,
                "reference_energy": 7.074226414042641,
                "candidate_energy": 7.069508329152995,
                "relative_energy_error_percent": 0.06669400459505197,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00018761854153126478,
                  "maximum": 0.0006895801052451134
                },
                "worst": {
                  "global_sensor_index": 48,
                  "local_sensor_index": 48,
                  "sky_patch_index": 99,
                  "rgb_channel": 0,
                  "reference": 0.014245864935219288,
                  "candidate": 0.014935445040464401
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.8503827368355985,
                "cvrmse_percent": 82.3506153630171,
                "rms_normalized_rmse_percent": 3.069490433661699,
                "reference_energy": 2.3873144444782497,
                "candidate_energy": 2.4076157543880754,
                "relative_energy_error_percent": 0.8503827368355985,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.517992131994106e-08,
                  "p95": 2.875472273444757e-05,
                  "p99": 0.00029641506262123585,
                  "maximum": 0.0010818252339959145
                },
                "worst": {
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "sky_patch_index": 94,
                  "rgb_channel": 0,
                  "reference": 0.00015794532373547554,
                  "candidate": -0.0009238799102604389
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 164.345333003439,
            "full": 403.36379199288785
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 157.22545806784183,
            "full": 389.1253749607131
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 156.7528749583289,
            "full": 392.50679104588926
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 149.4527499889955,
            "full": 385.3840410010889
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_i_large_center_grid",
            "start_sensor_index": 0,
            "sensor_count": 74,
            "stages": {
              "direct": {
                "nmbe_percent": -0.027873637392347345,
                "cvrmse_percent": 10.788268719647474,
                "rms_normalized_rmse_percent": 1.606052227524775,
                "reference_energy": 7.071472546724181,
                "candidate_energy": 7.069501470108207,
                "relative_energy_error_percent": 0.02787363739234735,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00012966268695890903,
                  "maximum": 0.0004657772369682789
                },
                "worst": {
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "sky_patch_index": 46,
                  "rgb_channel": 0,
                  "reference": 0.007762483786791563,
                  "candidate": 0.007296706549823284
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.27760474544930364,
                "cvrmse_percent": 28.474780973886347,
                "rms_normalized_rmse_percent": 1.6851808818501992,
                "reference_energy": 4.361539267246879,
                "candidate_energy": 4.3736471072273915,
                "relative_energy_error_percent": 0.2776047454493037,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.3305185337108014e-08,
                  "p90": 1.3962115190224722e-05,
                  "p95": 3.6971745430491865e-05,
                  "p99": 0.00019781698938459158,
                  "maximum": 0.0007118303328752518
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04279891401529312,
                  "candidate": 0.04351074434816837
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 203.37433402892202,
            "full": 5207.8407920198515
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 213.49591703619808,
            "full": 5200.984040973708
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 210.29474993702024,
            "full": 5146.713875001296
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 208.06758396793157,
            "full": 5201.76766696386
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_i_large_center_grid",
            "start_sensor_index": 0,
            "sensor_count": 74,
            "stages": {
              "direct": {
                "nmbe_percent": 0.032122902705114025,
                "cvrmse_percent": 10.081448124719268,
                "rms_normalized_rmse_percent": 1.499258604807882,
                "reference_energy": 7.066437779970784,
                "candidate_energy": 7.068707724903561,
                "relative_energy_error_percent": 0.03212290270511403,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00011569890193641186,
                  "maximum": 0.00044406892266124487
                },
                "worst": {
                  "global_sensor_index": 43,
                  "local_sensor_index": 43,
                  "sky_patch_index": 46,
                  "rgb_channel": 0,
                  "reference": 0.002902084030210972,
                  "candidate": 0.0033461529528722167
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.08728792225830255,
                "cvrmse_percent": 27.214493040890137,
                "rms_normalized_rmse_percent": 1.6146105037506229,
                "reference_energy": 4.374282098061332,
                "candidate_energy": 4.378100318018447,
                "relative_energy_error_percent": 0.08728792225830255,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.2105787422788126e-08,
                  "p90": 1.3578683137893677e-05,
                  "p95": 3.2653872040100396e-05,
                  "p99": 0.00019535375759005547,
                  "maximum": 0.0011080149561166763
                },
                "worst": {
                  "global_sensor_index": 46,
                  "local_sensor_index": 46,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0458823349326849,
                  "candidate": 0.04477431997656822
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 204.83750000130385,
            "full": 5598.126542055979
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 201.5820420347154,
            "full": 5635.271291946992
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 209.08466703258455,
            "full": 5602.614999981597
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 202.25062500685453,
            "full": 5670.1162500539795
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
            "identifier": "plan_i_large_center_grid",
            "start_sensor_index": 0,
            "sensor_count": 74,
            "stages": {
              "direct": {
                "nmbe_percent": 0.001685894244789072,
                "cvrmse_percent": 6.098403420815433,
                "rms_normalized_rmse_percent": 0.9072497482105268,
                "reference_energy": 7.070318262086175,
                "candidate_energy": 7.070437460174844,
                "relative_energy_error_percent": 0.001685894244789072,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.03808618709445e-05,
                  "maximum": 0.00021984195336699486
                },
                "worst": {
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "sky_patch_index": 47,
                  "rgb_channel": 0,
                  "reference": 0.007418948458507657,
                  "candidate": 0.007638790411874652
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.05093218767678929,
                "cvrmse_percent": 17.752620578723935,
                "rms_normalized_rmse_percent": 1.0514374465328102,
                "reference_energy": 4.3684473686414265,
                "candidate_energy": 4.370672314453785,
                "relative_energy_error_percent": 0.05093218767678929,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.6020151366878963e-08,
                  "p90": 9.489798685535789e-06,
                  "p95": 2.3204804165288806e-05,
                  "p99": 0.0001176029909402132,
                  "maximum": 0.0005417186766862869
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.042757054790854454,
                  "candidate": 0.04329877346754074
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 311.3709590397775,
            "full": 9959.839249961078
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 323.96591699216515,
            "full": 9937.597166048363
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 318.12491710297763,
            "full": 10004.121417063288
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 319.92383394390345,
            "full": 9936.464000027627
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 3114.5894579822198,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_large_center/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 11239.008250064217,
      "worker_pool_size": 12,
      "invocation_count": 5
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      74,
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
        "identifier": "plan_i_large_center_grid",
        "full_identifier": "plan_i_large_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": 0.018542996044857252,
            "cvrmse_percent": 3.633492723168646,
            "rms_normalized_rmse_percent": 0.5406237260788416,
            "reference_energy": 7.070178507836317,
            "candidate_energy": 7.07148953075739,
            "relative_energy_error_percent": 0.01854299604485725,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.3727770894765854e-05,
              "maximum": 0.0002558249980211258
            },
            "worst": {
              "global_sensor_index": 53,
              "local_sensor_index": 53,
              "sky_patch_index": 134,
              "rgb_channel": 0,
              "reference": 0.006629856303334236,
              "candidate": 0.00637403130531311,
              "position": [
                7.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.3222261432100537,
            "cvrmse_percent": 40.8376442984604,
            "rms_normalized_rmse_percent": 2.419847564523698,
            "reference_energy": 4.369759187201387,
            "candidate_energy": 4.311981088832887,
            "relative_energy_error_percent": 1.322226143210054,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.164036226939061e-08,
              "p90": 2.0013389530504355e-05,
              "p95": 3.7721572880400345e-05,
              "p99": 9.550899267196655e-05,
              "maximum": 0.0017855875194072723
            },
            "worst": {
              "global_sensor_index": 47,
              "local_sensor_index": 47,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04995117709040642,
              "candidate": 0.048165589570999146,
              "position": [
                6.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.49359600508944335,
            "cvrmse_percent": 15.606636746915182,
            "rms_normalized_rmse_percent": 2.4210446781633204,
            "reference_energy": 11.439937695037704,
            "candidate_energy": 11.383470619590277,
            "relative_energy_error_percent": 0.4935960050894434,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.206899006931053e-08,
              "p90": 1.9770421204157174e-05,
              "p95": 3.714286140166223e-05,
              "p99": 9.483238682150841e-05,
              "maximum": 0.0017855875194072723
            },
            "worst": {
              "global_sensor_index": 47,
              "local_sensor_index": 47,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04995117709040642,
              "candidate": 0.048165589570999146,
              "position": [
                6.5,
                1.5,
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
      74,
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
        "identifier": "plan_i_large_center_grid",
        "full_identifier": "plan_i_large_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": 0.018542996044857252,
            "cvrmse_percent": 3.633492723168646,
            "rms_normalized_rmse_percent": 0.5406237260788416,
            "reference_energy": 7.070178507836317,
            "candidate_energy": 7.07148953075739,
            "relative_energy_error_percent": 0.01854299604485725,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.3727770894765854e-05,
              "maximum": 0.0002558249980211258
            },
            "worst": {
              "global_sensor_index": 53,
              "local_sensor_index": 53,
              "sky_patch_index": 134,
              "rgb_channel": 0,
              "reference": 0.006629856303334236,
              "candidate": 0.00637403130531311,
              "position": [
                7.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 79.72923635798331,
            "cvrmse_percent": 518.5286581888524,
            "rms_normalized_rmse_percent": 19.42349229694055,
            "reference_energy": 2.3991539585937574,
            "candidate_energy": 4.311981088832887,
            "relative_energy_error_percent": 79.72923635798331,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0001403399946866557,
              "p95": 0.0002588900097180158,
              "p99": 0.0004919939674437046,
              "maximum": 0.008403245359659195
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.018552694469690323,
              "candidate": 0.026955939829349518,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.214076968424678,
            "cvrmse_percent": 131.40167258880217,
            "rms_normalized_rmse_percent": 19.427489964846757,
            "reference_energy": 9.469332466430075,
            "candidate_energy": 11.383470619590277,
            "relative_energy_error_percent": 20.214076968424678,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00014115863041297416,
              "p95": 0.0002606031484901905,
              "p99": 0.0004940256476402283,
              "maximum": 0.008403245359659195
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.018552694469690323,
              "candidate": 0.026955939829349518,
              "position": [
                3.5,
                0.5,
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
      "bias_percent": 0.273690634998617,
      "rms_normalized_error_percent": 0.21039183888571816,
      "absolute_error": {
        "p95": 0.07206787107961236,
        "p99": 0.11611905474952376,
        "maximum": 0.12385650726710651
      },
      "worst_index": [
        52
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.748248618532154,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.21039183888571816
    },
    "overcast": {
      "bias_percent": 0.22844004050221003,
      "rms_normalized_error_percent": 0.18968161393597552,
      "absolute_error": {
        "p95": 0.04829511642456054,
        "p99": 0.08539957046508787,
        "maximum": 0.09056663513183594
      },
      "worst_index": [
        52
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.420449733734131,
      "reference_fraction_of_uniform": 0.6550514101982117,
      "rms_normalized_to_uniform_percent": 0.1340816430270227
    },
    "horizon": {
      "bias_percent": 0.8126701484329311,
      "rms_normalized_error_percent": 1.6834131023912464,
      "absolute_error": {
        "p95": 0.0335941737148101,
        "p99": 0.037115763741399764,
        "maximum": 0.039023846993314626
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.6084884705711688,
      "reference_fraction_of_uniform": 0.09016983590381178,
      "rms_normalized_to_uniform_percent": 0.08433280731299805
    },
    "north": {
      "bias_percent": -83.04662540064682,
      "rms_normalized_error_percent": 90.2810178838159,
      "absolute_error": {
        "p95": 0.00010837621130121968,
        "p99": 0.00031106644062674595,
        "maximum": 0.00032945456041488796
      },
      "worst_index": [
        53
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.3690752641414292e-05,
      "reference_fraction_of_uniform": 3.510652049953933e-06,
      "rms_normalized_to_uniform_percent": 0.0003662806635382775
    },
    "east": {
      "bias_percent": 0.16457115638804654,
      "rms_normalized_error_percent": 0.28701704647894,
      "absolute_error": {
        "p95": 0.0240173578262329,
        "p99": 0.037417112588882424,
        "maximum": 0.04093170166015625
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3604003190994263,
      "reference_fraction_of_uniform": 0.20159310102462769,
      "rms_normalized_to_uniform_percent": 0.06377997479903019
    },
    "south": {
      "bias_percent": 0.3149269108704849,
      "rms_normalized_error_percent": 0.23556104224156862,
      "absolute_error": {
        "p95": 0.05882139205932614,
        "p99": 0.06578405857086178,
        "maximum": 0.07245731353759766
      },
      "worst_index": [
        52
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.517848014831543,
      "reference_fraction_of_uniform": 0.669484555721283,
      "rms_normalized_to_uniform_percent": 0.1504058416673051
    },
    "west": {
      "bias_percent": 0.3799403695158668,
      "rms_normalized_error_percent": 0.3896629680527571,
      "absolute_error": {
        "p95": 0.034454554319381714,
        "p99": 0.04363145828247068,
        "maximum": 0.04876232147216797
      },
      "worst_index": [
        52
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3249398469924927,
      "reference_fraction_of_uniform": 0.19633832573890686,
      "rms_normalized_to_uniform_percent": 0.08295933898133855
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
        "identifier": "plan_i_large_center_grid",
        "sensor_count": 74,
        "illuminance": {
          "nmbe_percent": 0.13941466659693477,
          "cvrmse_percent": 2.12366656673326,
          "absolute_error_percentiles_lux": {
            "p50": 0.7745223045349121,
            "p90": 13.471163940429689,
            "p95": 23.945580291748044,
            "p99": 55.301771240234366
          },
          "maximum_absolute_error_lux": 304.2255859375,
          "worst": {
            "sensor_index": 47,
            "position": [
              6.5,
              1.5,
              0.75
            ],
            "hour_of_year": 4451.5,
            "foton_lux": 5980.228515625,
            "radiance_lux": 5676.0029296875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.25716216216216214,
            "maximum_error_percentage_points": 1.754520547945205,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.26528804667983774,
            "maximum_error_percentage_points": 1.1795467767922219,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.39463161791928913,
            "maximum_error_percentage_points": 4.521232876712318,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.4027156608663455,
            "maximum_error_percentage_points": 4.521232876712329,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.017482413920770094,
            "maximum_error_percentage_points": 0.19287671232876846,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 22.972972972972972,
          "radiance_percent": 22.972972972972972,
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
      "maximum_error_percentage_points": 0.004955720248290163,
      "metrics": {
        "da": [
          {
            "identifier": "plan_i_large_center_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_i_large_center_grid",
            "maximum_error_percentage_points": 0.004955720248290163,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_i_large_center_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_i_large_center_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_i_large_center_grid",
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
      "study_preparation_seconds": 0.008104166015982628,
      "weather_seconds": 0.116832833038643,
      "metric_reduction_seconds": 0.06620241701602936,
      "write_seconds": 0.03862816595938057,
      "total_seconds": 0.2218388329492882,
      "cold_end_to_end_seconds": 0.22994299896527082,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.02430858404841274,
      "engine_upload_seconds": 0.000307833,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.04691654164344072,
      "engine_annual_reduction_seconds": 0.0006227083504199982,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.04691654164344072
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.008104166015982628,
      "weather_seconds": 0.12852575001306832,
      "metric_reduction_seconds": 0.013118666945956647,
      "write_seconds": 0.029117458034306765,
      "total_seconds": 0.17094395798631012,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.17094395798631012,
      "raw_export_seconds": 0.010582415969111025,
      "engine_upload_seconds": 5.2958e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0006570833502337337,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013941959012299776,
      "full": 0.0403814580058679
    }
  },
  "elapsed_seconds": 104.95328749995679,
  "result_class": "passed"
}
```
