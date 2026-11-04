# Foton report

Status: **passed**

```json
{
  "scene": "teaching_obstruction30",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_obstruction30",
    "category": "teaching",
    "question": "How does a 30 degree obstruction angle reduce sky access?",
    "interactions": [
      "multiple_bounces",
      "obstruction",
      "side_glazing"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 6,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 4.499999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "85eea1d5c0dbdb5ec7c49137c913011feacc5685acdf87d6102bfcfc4fd930fa",
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
      "scene_fingerprint": 16536123132161339720,
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
      "scene_fingerprint": 16536123132161339720,
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
    "model_sha256": "2f9e103febe9b48f5fa9c64e24766f5f42fbbe20ec5fc9c103349d9b90e28cae",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "42ebbd5873d9863a0ad3aca60e92d9e55c1ae842623c6cc1f4949849ae92cd10",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00029224716126918793,
          "p95": 4.12575900554657e-07,
          "p99": 0.00013335076801013201
        },
        "bias_percent": -0.2141990698903249,
        "identifier": "teaching_obstruction30_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.2974127623121974,
        "worst_index": [
          17,
          121,
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
          "maximum": 0.0006466172635555267,
          "p95": 4.2564532486721865e-05,
          "p99": 0.00012212898582220078
        },
        "bias_percent": 0.09504229798769098,
        "identifier": "teaching_obstruction30_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7952599562739783,
        "worst_index": [
          5,
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
          "maximum": 0.0005340911448001862,
          "p95": 3.445749171078205e-05,
          "p99": 0.00010180938988924026
        },
        "bias_percent": -0.02631811809215449,
        "identifier": "teaching_obstruction30_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7042289015007868,
        "worst_index": [
          23,
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
            "identifier": "teaching_obstruction30_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000916650053113699,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.247195415198675e-07,
                  "p99": 0.0003482755273580551
                },
                "candidate_energy": 5.0702037090668455,
                "cvrmse_percent": 19.734825238333034,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.05622345830271112,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.073055956567259,
                "relative_energy_error_percent": 0.056223458302711124,
                "rms_normalized_rmse_percent": 3.394929925122913,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0036176550202071667,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.004534305073320866,
                  "rgb_channel": 0,
                  "sky_patch_index": 41
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001739494502544403,
                  "p50": 9.117798072111327e-07,
                  "p90": 5.560260979109444e-05,
                  "p95": 9.640927892178201e-05,
                  "p99": 0.000491174403578043
                },
                "candidate_energy": 3.159602244800837,
                "cvrmse_percent": 45.6729659047799,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.12910576931176584,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.1555282757445866,
                "relative_energy_error_percent": 0.12910576931176584,
                "rms_normalized_rmse_percent": 3.0867067072437258,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.046185195446014404,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.04792468994855881,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 105.63004098366946,
            "full": 234.50583405792713
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 101.00662498734891,
            "full": 235.711041954346
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 113.86520799715072,
            "full": 220.3356659738347
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 107.16374998446554,
            "full": 222.81145805027336
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
            "identifier": "teaching_obstruction30_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00033130450174212456,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.07521191239357e-06,
                  "p99": 0.00013953856250736862
                },
                "candidate_energy": 5.070027616765401,
                "cvrmse_percent": 7.415396395516687,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.009032724035578595,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.069569696524923,
                "relative_energy_error_percent": 0.009032724035578595,
                "rms_normalized_rmse_percent": 1.2745522849023259,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.015167319681495428,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.014836015179753304,
                  "rgb_channel": 0,
                  "sky_patch_index": 98
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008640754967927933,
                  "p50": 7.101720257196575e-06,
                  "p90": 3.5708661016542464e-05,
                  "p95": 5.762716646131587e-05,
                  "p99": 0.00023578922264277935
                },
                "candidate_energy": 5.084026001882865,
                "cvrmse_percent": 15.2865066050429,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.08832183213599884,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.088520276219434,
                "relative_energy_error_percent": 0.08832183213599884,
                "rms_normalized_rmse_percent": 1.36877664290894,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.029310420155525208,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.028446344658732414,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.56874999590218,
            "full": 2176.7129169311374
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.57858299463987,
            "full": 2178.1109999865294
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.6276659918949,
            "full": 2205.0292500061914
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.59412501752377,
            "full": 2192.747208988294
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
            "identifier": "teaching_obstruction30_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00040851463563740253,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 8.30506905913353e-07,
                  "p99": 0.00012460449943318963
                },
                "candidate_energy": 5.070020306291553,
                "cvrmse_percent": 7.274614181491905,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.0014851017167087006,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.070095602368383,
                "relative_energy_error_percent": 0.0014851017167087008,
                "rms_normalized_rmse_percent": 1.2511264368981891,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.006812608567997813,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.007221123203635216,
                  "rgb_channel": 0,
                  "sky_patch_index": 99
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006463266909122467,
                  "p50": 7.151543613304057e-06,
                  "p90": 3.596480382839218e-05,
                  "p95": 5.93684409977867e-05,
                  "p99": 0.00022410042583942413
                },
                "candidate_energy": 5.091838741050019,
                "cvrmse_percent": 13.659605272695718,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.1501221071142358,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.099494209209052,
                "relative_energy_error_percent": 0.15012210711423576,
                "rms_normalized_rmse_percent": 1.2253498285983428,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.056076060980558395,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.05542973428964615,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.55333301238716,
            "full": 2296.338582993485
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.11983400490135,
            "full": 2329.0539589943364
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 129.07899997662753,
            "full": 2442.4172500148416
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.73499993700534,
            "full": 2334.254042012617
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
            "identifier": "teaching_obstruction30_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00019469019025564194,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.475936293601807e-07,
                  "p99": 7.472513243556023e-05
                },
                "candidate_energy": 5.0685279804092715,
                "cvrmse_percent": 4.301375585837968,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.026579794819467602,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.069875542926184,
                "relative_energy_error_percent": 0.0265797948194676,
                "rms_normalized_rmse_percent": 0.7394601437867272,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.01380795007571578,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.014002640265971422,
                  "rgb_channel": 0,
                  "sky_patch_index": 134
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010605249553918839,
                  "p50": 5.06146352563519e-06,
                  "p90": 2.5457149604335427e-05,
                  "p95": 3.9210795512189975e-05,
                  "p99": 0.0001328052021563053
                },
                "candidate_energy": 5.097838016219441,
                "cvrmse_percent": 10.721617307242315,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.15681394415999947,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.089856411628286,
                "relative_energy_error_percent": 0.15681394415999947,
                "rms_normalized_rmse_percent": 0.9605874757006662,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05147680453956127,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.052537329494953156,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 199.55812499392778,
            "full": 4084.70100001432
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 185.4301249841228,
            "full": 4074.1473749512807
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 197.80270801857114,
            "full": 4146.60666603595
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 192.21474998630583,
            "full": 4063.031749916263
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
    "/Users/ssanjay/GitHub/foton-0.3.3/validation/results/2026-11-04-architectural-v4-metal-0.3.3-release/teaching_obstruction30/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 768.1852920213714,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction30/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2760.874083964154,
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
        "identifier": "teaching_obstruction30_grid",
        "full_identifier": "teaching_obstruction30_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.18712955930342395,
            "cvrmse_percent": 4.83698174035112,
            "rms_normalized_rmse_percent": 0.8320721092586214,
            "reference_energy": 5.07558257445271,
            "candidate_energy": 5.066084659149055,
            "relative_energy_error_percent": 0.18712955930342395,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.880130290985107e-07,
              "p99": 8.323788642883301e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.3006805979601634,
            "cvrmse_percent": 24.730243977520804,
            "rms_normalized_rmse_percent": 2.214011224983349,
            "reference_energy": 5.087466417564942,
            "candidate_energy": 5.021294728943936,
            "relative_energy_error_percent": 1.3006805979601637,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 8.132985385600477e-06,
              "p90": 3.307254519313574e-05,
              "p95": 4.819457899429835e-05,
              "p99": 0.0001290483633056283,
              "maximum": 0.0020107589662075043
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04923363775014877,
              "candidate": 0.04722287878394127,
              "position": [
                3.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.7445561266515001,
            "cvrmse_percent": 12.321417056497914,
            "rms_normalized_rmse_percent": 2.203609007955048,
            "reference_energy": 10.163048992017652,
            "candidate_energy": 10.087379388092991,
            "relative_energy_error_percent": 0.7445561266515,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 8.081007393911932e-06,
              "p90": 3.2901712984312326e-05,
              "p95": 4.759442526847122e-05,
              "p99": 0.00011783884838223457,
              "maximum": 0.0020107589662075043
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04923363775014877,
              "candidate": 0.04722287878394127,
              "position": [
                3.5,
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
        "identifier": "teaching_obstruction30_grid",
        "full_identifier": "teaching_obstruction30_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.18712955930342395,
            "cvrmse_percent": 4.83698174035112,
            "rms_normalized_rmse_percent": 0.8320721092586214,
            "reference_energy": 5.07558257445271,
            "candidate_energy": 5.066084659149055,
            "relative_energy_error_percent": 0.18712955930342395,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.880130290985107e-07,
              "p99": 8.323788642883301e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 59.22357885463252,
            "cvrmse_percent": 392.2128226154689,
            "rms_normalized_rmse_percent": 26.518823571449087,
            "reference_energy": 3.153612527154827,
            "candidate_energy": 5.021294728943936,
            "relative_energy_error_percent": 59.223578854632514,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.546550194892916e-05,
              "p90": 0.00018523000471759588,
              "p95": 0.00027051600336562803,
              "p99": 0.0004761422678711824,
              "maximum": 0.011001555249094963
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02444622479379177,
              "candidate": 0.035447780042886734,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 22.580389254867292,
            "cvrmse_percent": 150.26826666088843,
            "rms_normalized_rmse_percent": 26.512383288523417,
            "reference_energy": 8.229195101607537,
            "candidate_energy": 10.087379388092991,
            "relative_energy_error_percent": 22.58038925486729,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5351348085678183e-05,
              "p90": 0.0001842399942688644,
              "p95": 0.000266959995497018,
              "p99": 0.0004472886212170124,
              "maximum": 0.011001555249094963
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02444622479379177,
              "candidate": 0.035447780042886734,
              "position": [
                0.5,
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
      "bias_percent": -0.003138303795467626,
      "rms_normalized_error_percent": 0.19386028152890328,
      "absolute_error": {
        "p95": 0.0864682297784718,
        "p99": 0.0890033447233037,
        "maximum": 0.09034304780838909
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.541103155830344,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.19386028152890328
    },
    "overcast": {
      "bias_percent": 0.006201380287964278,
      "rms_normalized_error_percent": 0.1880177490301624,
      "absolute_error": {
        "p95": 0.05746126174926758,
        "p99": 0.06844081878662107,
        "maximum": 0.073486328125
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.74970817565918,
      "reference_fraction_of_uniform": 0.7351894974708557,
      "rms_normalized_to_uniform_percent": 0.1440256228505473
    },
    "horizon": {
      "bias_percent": -0.14178085683886635,
      "rms_normalized_error_percent": 2.807919780358558,
      "absolute_error": {
        "p95": 0.022387442463391097,
        "p99": 0.029152301662619565,
        "maximum": 0.029434220906386366
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3285779149962254,
      "reference_fraction_of_uniform": 0.031171112751561217,
      "rms_normalized_to_uniform_percent": 0.055509658769576434
    },
    "north": {
      "bias_percent": 0.3770158842787355,
      "rms_normalized_error_percent": 1.3990598835434374,
      "absolute_error": {
        "p95": 0.01959879696369171,
        "p99": 0.02108325660228729,
        "maximum": 0.02125680446624756
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5986044406890869,
      "reference_fraction_of_uniform": 0.0567876473069191,
      "rms_normalized_to_uniform_percent": 0.047307065029470824
    },
    "east": {
      "bias_percent": 0.07224400899142996,
      "rms_normalized_error_percent": 0.32543597196597,
      "absolute_error": {
        "p95": 0.02468140423297882,
        "p99": 0.031106385588645924,
        "maximum": 0.03381061553955078
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.1856656074523926,
      "reference_fraction_of_uniform": 0.20734694600105286,
      "rms_normalized_to_uniform_percent": 0.07331665590319114
    },
    "south": {
      "bias_percent": -0.032089444010311836,
      "rms_normalized_error_percent": 0.17313618705953326,
      "absolute_error": {
        "p95": 0.0316452831029892,
        "p99": 0.036805889010429374,
        "maximum": 0.039447784423828125
      },
      "worst_index": [
        29
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.50840425491333,
      "reference_fraction_of_uniform": 0.5225642919540405,
      "rms_normalized_to_uniform_percent": 0.09143032260434282
    },
    "west": {
      "bias_percent": -0.24155161258019303,
      "rms_normalized_error_percent": 0.37821622404225536,
      "absolute_error": {
        "p95": 0.031041257083415985,
        "p99": 0.04533927440643308,
        "maximum": 0.051480770111083984
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.1174135208129883,
      "reference_fraction_of_uniform": 0.20087209343910217,
      "rms_normalized_to_uniform_percent": 0.08106688378069153
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
        "identifier": "teaching_obstruction30_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.13091190172409475,
          "cvrmse_percent": 1.8954095619691211,
          "absolute_error_percentiles_lux": {
            "p50": 2.0386199951171875,
            "p90": 23.552990722656258,
            "p95": 36.99172363281244,
            "p99": 75.31396179199214
          },
          "maximum_absolute_error_lux": 416.64453125,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 5156.45068359375,
            "radiance_lux": 5573.09521484375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.3858599695585994,
            "maximum_error_percentage_points": 2.0049315068493136,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.23705705723420165,
            "maximum_error_percentage_points": 1.169922056990103,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.2347640791476414,
            "maximum_error_percentage_points": 1.2087671232876716,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.2399429223744295,
            "maximum_error_percentage_points": 1.2087671232876716,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.01628614916286141,
            "maximum_error_percentage_points": 0.16013698630136908,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 27.77777777777778,
          "radiance_percent": 27.77777777777778,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.7777777777777777,
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
      "maximum_error_percentage_points": 0.0049684289383549185,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_obstruction30_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_obstruction30_grid",
            "maximum_error_percentage_points": 0.0049684289383549185,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_obstruction30_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_obstruction30_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_obstruction30_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
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
      "study_preparation_seconds": 0.00651208299677819,
      "weather_seconds": 0.07541045802645385,
      "metric_reduction_seconds": 0.03522141696885228,
      "write_seconds": 0.00963049998972565,
      "total_seconds": 0.12040070910006762,
      "cold_end_to_end_seconds": 0.1269127920968458,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0013308339985087514,
      "engine_upload_seconds": 0.000276042,
      "engine_acceleration_structure_seconds": 0.003076042,
      "engine_tracing_seconds": 0.014001291594468057,
      "engine_annual_reduction_seconds": 0.0003461666638031602,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.014001291594468057
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.00651208299677819,
      "weather_seconds": 0.07393424992915243,
      "metric_reduction_seconds": 0.012688667047768831,
      "write_seconds": 0.009901832905597985,
      "total_seconds": 0.09662720805499703,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.09662720805499703,
      "raw_export_seconds": 0.0017858329229056835,
      "engine_upload_seconds": 3.5375e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0003658750792965293,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.019532541977241635,
      "full": 0.01700666605029255
    }
  },
  "elapsed_seconds": 0.670413792016916,
  "result_class": "passed"
}
```
