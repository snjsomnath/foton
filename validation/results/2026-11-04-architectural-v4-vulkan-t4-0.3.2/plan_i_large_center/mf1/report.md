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
  "model_sha256": "e12dc7fdd9aa2e521832437a62c3513a11901e2f35fdd646f6d9a964eb03ba8f",
  "weather_sha256": "98246499f5e0508387c41d22a6f492c76a8ec52c17ceb31712069871a196bcee",
  "gpu_executed": true,
  "candidate": {
    "capabilities": {
      "name": "Vulkan device: Tesla T4",
      "hardware_acceleration": true,
      "supports_ray_tracing": true,
      "supports_async_jobs": true
    },
    "direct": {
      "metric_label": "static_sDA300_50",
      "solver_version": "0.3.2",
      "scene_fingerprint": 5535031717744390830,
      "basis": "Tregenza",
      "quality": "Final",
      "glazing_model": "radiance_thin_glass_non_refracting",
      "schedule_timestep_count": 1,
      "direct_sample_count": 256,
      "convergence": 1.0,
      "transport_backend": "vulkan",
      "used_reference_fallback": false
    },
    "full": {
      "metric_label": "static_sDA300_50",
      "solver_version": "0.3.2",
      "scene_fingerprint": 5535031717744390830,
      "basis": "Tregenza",
      "quality": "Final",
      "glazing_model": "radiance_thin_glass_non_refracting",
      "schedule_timestep_count": 1,
      "direct_sample_count": 256,
      "convergence": 1.0,
      "transport_backend": "vulkan",
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.2)",
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
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "ff3bdf8b69a3bb177bf3b66e048fc97558de09792f5dd7355f696f08fee5c827",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "274288e18ebb896ca8da417745929f291321088f610eaef564604626c7d101ce",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00037325965240597725,
          "p95": 0.0,
          "p99": 4.025897942483425e-05
        },
        "bias_percent": -0.11873487137665646,
        "identifier": "plan_i_large_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.015976769220981,
        "worst_index": [
          36,
          135,
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
          "maximum": 0.00045307353138923645,
          "p95": 2.1524872863665223e-05,
          "p99": 0.00010549696162343025
        },
        "bias_percent": 0.049691870962604606,
        "identifier": "plan_i_large_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9927347705816938,
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
          "maximum": 0.000436246395111084,
          "p95": 1.904543023556471e-05,
          "p99": 8.842442184686661e-05
        },
        "bias_percent": -0.03343530807638633,
        "identifier": "plan_i_large_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8209649588946059,
        "worst_index": [
          52,
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
            "identifier": "plan_i_large_center_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006895801052451134,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00018761854153126478
                },
                "candidate_energy": 7.069508329152995,
                "cvrmse_percent": 17.263655791355568,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.06669400459505197,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.074226414042641,
                "relative_energy_error_percent": 0.06669400459505197,
                "rms_normalized_rmse_percent": 2.5653022853447442,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.014935445040464401,
                  "global_sensor_index": 48,
                  "local_sensor_index": 48,
                  "reference": 0.014245864935219288,
                  "rgb_channel": 0,
                  "sky_patch_index": 99
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010818252339959145,
                  "p50": 0.0,
                  "p90": 1.517992131994106e-08,
                  "p95": 2.875472273444757e-05,
                  "p99": 0.00029641506262123585
                },
                "candidate_energy": 2.4076157543880754,
                "cvrmse_percent": 82.3506153630171,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.8503827368355985,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.3873144444782497,
                "relative_energy_error_percent": 0.8503827368355985,
                "rms_normalized_rmse_percent": 3.069490433661699,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0009238799102604389,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.00015794532373547554,
                  "rgb_channel": 0,
                  "sky_patch_index": 94
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
          "timings_ms": {
            "direct": 164.345333003439,
            "full": 403.36379199288785
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
          "timings_ms": {
            "direct": 157.22545806784183,
            "full": 389.1253749607131
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
          "timings_ms": {
            "direct": 156.7528749583289,
            "full": 392.50679104588926
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
          "timings_ms": {
            "direct": 149.4527499889955,
            "full": 385.3840410010889
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
            "identifier": "plan_i_large_center_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004657772369682789,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00012966268695890903
                },
                "candidate_energy": 7.069501470108207,
                "cvrmse_percent": 10.788268719647474,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.027873637392347345,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.071472546724181,
                "relative_energy_error_percent": 0.02787363739234735,
                "rms_normalized_rmse_percent": 1.606052227524775,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007296706549823284,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.007762483786791563,
                  "rgb_channel": 0,
                  "sky_patch_index": 46
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007118303328752518,
                  "p50": 2.3305185337108014e-08,
                  "p90": 1.3962115190224722e-05,
                  "p95": 3.6971745430491865e-05,
                  "p99": 0.00019781698938459158
                },
                "candidate_energy": 4.3736471072273915,
                "cvrmse_percent": 28.474780973886347,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.27760474544930364,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.361539267246879,
                "relative_energy_error_percent": 0.2776047454493037,
                "rms_normalized_rmse_percent": 1.6851808818501992,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04351074434816837,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.04279891401529312,
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
          "timings_ms": {
            "direct": 203.37433402892202,
            "full": 5207.8407920198515
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
          "timings_ms": {
            "direct": 213.49591703619808,
            "full": 5200.984040973708
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
          "timings_ms": {
            "direct": 210.29474993702024,
            "full": 5146.713875001296
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
          "timings_ms": {
            "direct": 208.06758396793157,
            "full": 5201.76766696386
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
            "identifier": "plan_i_large_center_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00044406892266124487,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00011569890193641186
                },
                "candidate_energy": 7.068707724903561,
                "cvrmse_percent": 10.081448124719268,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.032122902705114025,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.066437779970784,
                "relative_energy_error_percent": 0.03212290270511403,
                "rms_normalized_rmse_percent": 1.499258604807882,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0033461529528722167,
                  "global_sensor_index": 43,
                  "local_sensor_index": 43,
                  "reference": 0.002902084030210972,
                  "rgb_channel": 0,
                  "sky_patch_index": 46
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011080149561166763,
                  "p50": 2.2105787422788126e-08,
                  "p90": 1.3578683137893677e-05,
                  "p95": 3.2653872040100396e-05,
                  "p99": 0.00019535375759005547
                },
                "candidate_energy": 4.378100318018447,
                "cvrmse_percent": 27.214493040890137,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.08728792225830255,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.374282098061332,
                "relative_energy_error_percent": 0.08728792225830255,
                "rms_normalized_rmse_percent": 1.6146105037506229,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04477431997656822,
                  "global_sensor_index": 46,
                  "local_sensor_index": 46,
                  "reference": 0.0458823349326849,
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
          "timings_ms": {
            "direct": 204.83750000130385,
            "full": 5598.126542055979
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
          "timings_ms": {
            "direct": 201.5820420347154,
            "full": 5635.271291946992
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
          "timings_ms": {
            "direct": 209.08466703258455,
            "full": 5602.614999981597
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
          "timings_ms": {
            "direct": 202.25062500685453,
            "full": 5670.1162500539795
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
            "identifier": "plan_i_large_center_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00021984195336699486,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.03808618709445e-05
                },
                "candidate_energy": 7.070437460174844,
                "cvrmse_percent": 6.098403420815433,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.001685894244789072,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.070318262086175,
                "relative_energy_error_percent": 0.001685894244789072,
                "rms_normalized_rmse_percent": 0.9072497482105268,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007638790411874652,
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "reference": 0.007418948458507657,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005417186766862869,
                  "p50": 2.6020151366878963e-08,
                  "p90": 9.489798685535789e-06,
                  "p95": 2.3204804165288806e-05,
                  "p99": 0.0001176029909402132
                },
                "candidate_energy": 4.370672314453785,
                "cvrmse_percent": 17.752620578723935,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.05093218767678929,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.3684473686414265,
                "relative_energy_error_percent": 0.05093218767678929,
                "rms_normalized_rmse_percent": 1.0514374465328102,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04329877346754074,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.042757054790854454,
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
          "timings_ms": {
            "direct": 311.3709590397775,
            "full": 9959.839249961078
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
          "timings_ms": {
            "direct": 323.96591699216515,
            "full": 9937.597166048363
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
          "timings_ms": {
            "direct": 318.12491710297763,
            "full": 10004.121417063288
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
          "timings_ms": {
            "direct": 319.92383394390345,
            "full": 9936.464000027627
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
    "/content/suite-vulkan-0.3.2/plan_i_large_center/mf1/oracle/scene.rad"
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
      "elapsed_ms": 3114.5894579822198,
      "invocation_count": 5,
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
      "elapsed_ms": 11239.008250064217,
      "invocation_count": 5,
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
            "nmbe_percent": 0.018541353747290688,
            "cvrmse_percent": 3.6334913515302034,
            "rms_normalized_rmse_percent": 0.540623521994138,
            "reference_energy": 7.070178507836317,
            "candidate_energy": 7.07148941464402,
            "relative_energy_error_percent": 0.018541353747290684,
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
            "nmbe_percent": -1.322200126897973,
            "cvrmse_percent": 40.83762034365982,
            "rms_normalized_rmse_percent": 2.4198461450743927,
            "reference_energy": 4.369759187201387,
            "candidate_energy": 4.311982225683074,
            "relative_energy_error_percent": 1.322200126897973,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.164036226939061e-08,
              "p90": 2.0013389530504355e-05,
              "p95": 3.7721572880400345e-05,
              "p99": 9.550899267196655e-05,
              "maximum": 0.0017855986952781677
            },
            "worst": {
              "global_sensor_index": 47,
              "local_sensor_index": 47,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04995117709040642,
              "candidate": 0.04816557839512825,
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
            "nmbe_percent": -0.49358708251621836,
            "cvrmse_percent": 15.60659917241811,
            "rms_normalized_rmse_percent": 2.4210388492626,
            "reference_energy": 11.439937695037704,
            "candidate_energy": 11.383471640327095,
            "relative_energy_error_percent": 0.4935870825162184,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.206899006931053e-08,
              "p90": 1.9770421204157174e-05,
              "p95": 3.714286140166223e-05,
              "p99": 9.483238682150841e-05,
              "maximum": 0.0017855986952781677
            },
            "worst": {
              "global_sensor_index": 47,
              "local_sensor_index": 47,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04995117709040642,
              "candidate": 0.04816557839512825,
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
            "nmbe_percent": 0.018541353747290688,
            "cvrmse_percent": 3.6334913515302034,
            "rms_normalized_rmse_percent": 0.540623521994138,
            "reference_energy": 7.070178507836317,
            "candidate_energy": 7.07148941464402,
            "relative_energy_error_percent": 0.018541353747290684,
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
            "nmbe_percent": 79.72928374344531,
            "cvrmse_percent": 518.5300548724764,
            "rms_normalized_rmse_percent": 19.423544615116576,
            "reference_energy": 2.3991539585937574,
            "candidate_energy": 4.311982225683074,
            "relative_energy_error_percent": 79.72928374344531,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0001403399946866557,
              "p95": 0.0002588900097180158,
              "p99": 0.0004919939674437046,
              "maximum": 0.008403236046433449
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.018552694469690323,
              "candidate": 0.02695593051612377,
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
            "nmbe_percent": 20.21408774782039,
            "cvrmse_percent": 131.40202012412917,
            "rms_normalized_rmse_percent": 19.427541347290713,
            "reference_energy": 9.469332466430075,
            "candidate_energy": 11.383471640327095,
            "relative_energy_error_percent": 20.21408774782039,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00014115863041297416,
              "p95": 0.0002606031484901905,
              "p99": 0.000494025181978941,
              "maximum": 0.008403236046433449
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.018552694469690323,
              "candidate": 0.02695593051612377,
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
      "bias_percent": 0.2736884992443878,
      "rms_normalized_error_percent": 0.2103910492466818,
      "absolute_error": {
        "p95": 0.07206768666027798,
        "p99": 0.11611776360580353,
        "maximum": 0.12385600714687683
      },
      "worst_index": [
        52
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.748248618532154,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2103910492466818
    },
    "overcast": {
      "bias_percent": 0.22843104959520172,
      "rms_normalized_error_percent": 0.18968374646711794,
      "absolute_error": {
        "p95": 0.04829542636871337,
        "p99": 0.08540008544921872,
        "maximum": 0.09056854248046875
      },
      "worst_index": [
        52
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.420450210571289,
      "reference_fraction_of_uniform": 0.6550514698028564,
      "rms_normalized_to_uniform_percent": 0.13408315488232378
    },
    "horizon": {
      "bias_percent": 0.812663611597345,
      "rms_normalized_error_percent": 1.6834102157906894,
      "absolute_error": {
        "p95": 0.03359419715794578,
        "p99": 0.037115752488694635,
        "maximum": 0.03902380531662897
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.6084884705711688,
      "reference_fraction_of_uniform": 0.09016983590381178,
      "rms_normalized_to_uniform_percent": 0.08433266270492282
    },
    "north": {
      "bias_percent": -83.04662583134333,
      "rms_normalized_error_percent": 90.28101865234365,
      "absolute_error": {
        "p95": 0.00010837621161954283,
        "p99": 0.0003110664425912545,
        "maximum": 0.0003294545676908456
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
      "bias_percent": 0.16453511649334263,
      "rms_normalized_error_percent": 0.28697504902298965,
      "absolute_error": {
        "p95": 0.0240170270204544,
        "p99": 0.03741589426994322,
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
      "rms_normalized_to_uniform_percent": 0.0637706409689622
    },
    "south": {
      "bias_percent": 0.3149522770398891,
      "rms_normalized_error_percent": 0.23556112888946518,
      "absolute_error": {
        "p95": 0.05882131457328793,
        "p99": 0.0657846641540527,
        "maximum": 0.07245826721191406
      },
      "worst_index": [
        52
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.517848014831543,
      "reference_fraction_of_uniform": 0.669484555721283,
      "rms_normalized_to_uniform_percent": 0.15040589527919523
    },
    "west": {
      "bias_percent": 0.3799410540951016,
      "rms_normalized_error_percent": 0.3896617592393433,
      "absolute_error": {
        "p95": 0.03445438742637634,
        "p99": 0.04363111376762387,
        "maximum": 0.04876136779785156
      },
      "worst_index": [
        52
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3249398469924927,
      "reference_fraction_of_uniform": 0.19633832573890686,
      "rms_normalized_to_uniform_percent": 0.08295908164426602
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
          "nmbe_percent": 0.1394353066393417,
          "cvrmse_percent": 2.1236282156474635,
          "absolute_error_percentiles_lux": {
            "p50": 0.7745258808135986,
            "p90": 13.471030426025395,
            "p95": 23.945585632324217,
            "p99": 55.30172912597655
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
      "maximum_error_percentage_points": 0.004952375856163371,
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
            "maximum_error_percentage_points": 0.004952375856163371,
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
      "study_preparation_seconds": 0.3758399299999837,
      "weather_seconds": 0.24408794800001488,
      "metric_reduction_seconds": 0.25940961900005277,
      "write_seconds": 0.012916233999931137,
      "total_seconds": 0.5167814619999263,
      "cold_end_to_end_seconds": 0.89262139199991,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.002255033999972511,
      "engine_upload_seconds": 0.014001185,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.02069404,
      "engine_annual_reduction_seconds": 0.009856161,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.02069404
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3758399299999837,
      "weather_seconds": 0.2346327499999461,
      "metric_reduction_seconds": 0.24583442299990566,
      "write_seconds": 0.013980087000163621,
      "total_seconds": 0.49476818500033914,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.49476818500033914,
      "raw_export_seconds": 0.0025251459996979975,
      "engine_upload_seconds": 0.014062995,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.4e-08,
      "engine_annual_reduction_seconds": 0.010700173,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.0143982340000548,
      "full": 0.03078368699971179
    }
  },
  "elapsed_seconds": 3.4064842559996578,
  "result_class": "passed"
}
```
