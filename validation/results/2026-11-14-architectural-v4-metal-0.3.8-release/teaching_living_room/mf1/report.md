# Foton report

Status: **passed**

```json
{
  "scene": "teaching_living_room",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_living_room",
    "category": "teaching",
    "question": "How is a 5 x 4.5 m living room with a tall window lit?",
    "interactions": [
      "multiple_bounces",
      "room",
      "side_glazing",
      "window"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 20,
    "floor_area": 22.5,
    "aperture_area": 4.800000000000001
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "5cbce9dd528c353afdd05285cc73a60fe2a28dfa58791e0d9fa817ddcc884ba5",
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
      "solver_version": "0.3.8",
      "scene_fingerprint": 5011208731090707716,
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
      "solver_version": "0.3.8",
      "scene_fingerprint": 5011208731090707716,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.8)",
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/52e717d2-b26e-4bbc-9536-f9b0a23834d6/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "59ff7b6ed290a327e1a4a6f5e8eaf4153d34bbea3bab25ed8c13123f0b99cc89",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "7b1607c11eb2f886cb1b00285cf77b48f28c7f9f5caae4c4b229203928ac8536",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0007540034130215645,
          "p95": 9.847903857007378e-06,
          "p99": 0.00012934557162225246
        },
        "bias_percent": -0.07151979699695074,
        "identifier": "teaching_living_room_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3445794157223598,
        "worst_index": [
          11,
          134,
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
          "maximum": 0.0005691051483154297,
          "p95": 7.758773863315516e-05,
          "p99": 0.00018400885164737701
        },
        "bias_percent": 0.05244877139929739,
        "identifier": "teaching_living_room_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7286831490939246,
        "worst_index": [
          14,
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
          "maximum": 0.0005918219685554504,
          "p95": 5.802227533422404e-05,
          "p99": 0.00014698365703225136
        },
        "bias_percent": 0.057616443538339286,
        "identifier": "teaching_living_room_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.625221826439159,
        "worst_index": [
          14,
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
            "identifier": "teaching_living_room_grid",
            "sensor_count": 20,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005757301114499569,
                  "p50": 0.0,
                  "p90": 4.140045493841194e-05,
                  "p95": 0.00013074162416160107,
                  "p99": 0.000322242034599185
                },
                "candidate_energy": 6.346959275120753,
                "cvrmse_percent": 7.94968022077245,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.03392321607142246,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.34480691256249,
                "relative_energy_error_percent": 0.03392321607142245,
                "rms_normalized_rmse_percent": 2.1521578954067855,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.014982820022851229,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.015558550134301186,
                  "rgb_channel": 0,
                  "sky_patch_index": 98
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008639153093099594,
                  "p50": 0.0,
                  "p90": 5.001898389309682e-05,
                  "p95": 0.00016837089206091967,
                  "p99": 0.00043570250272750854
                },
                "candidate_energy": 2.872774396719393,
                "cvrmse_percent": 25.838130682025188,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.3462365844252137,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.8827555510767695,
                "relative_energy_error_percent": 0.3462365844252137,
                "rms_normalized_rmse_percent": 1.8937830310724582,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05418418534100056,
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "reference": 0.055048100650310516,
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.4206659719348,
            "full": 181.99108296539634
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 112.45191702619195,
            "full": 178.42837504576892
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.05316697992384,
            "full": 180.5519589688629
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.77724996116012,
            "full": 195.98587497603148
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
            "identifier": "teaching_living_room_grid",
            "sensor_count": 20,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003356124507263303,
                  "p50": 0.0,
                  "p90": 2.082099672406912e-05,
                  "p95": 8.855147752910828e-05,
                  "p99": 0.00022652896586805582
                },
                "candidate_energy": 6.345127997990858,
                "cvrmse_percent": 5.853214724201751,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.024144238679849876,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.343596384938792,
                "relative_energy_error_percent": 0.024144238679849873,
                "rms_normalized_rmse_percent": 1.5856469036103238,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0027412205236032605,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.003076832974329591,
                  "rgb_channel": 0,
                  "sky_patch_index": 75
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009018238633871078,
                  "p50": 3.094392013736069e-07,
                  "p90": 5.625015473924579e-05,
                  "p95": 0.00013163434923626444,
                  "p99": 0.00035334553103893995
                },
                "candidate_energy": 5.0491949670736105,
                "cvrmse_percent": 12.7744856869077,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.0005713056492316585,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.0492238135745,
                "relative_energy_error_percent": 0.0005713056492316584,
                "rms_normalized_rmse_percent": 1.3103100128109793,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05887229926884174,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.057970475405454636,
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.8200410446152,
            "full": 1392.671333043836
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.23112496640533,
            "full": 1453.4369590692222
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.76575007289648,
            "full": 1422.3873750306666
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 241.96237500291318,
            "full": 1432.216874905862
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
            "identifier": "teaching_living_room_grid",
            "sensor_count": 20,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003519193269312382,
                  "p50": 0.0,
                  "p90": 2.1679594647139337e-05,
                  "p95": 8.34008445963254e-05,
                  "p99": 0.00024469010531902313
                },
                "candidate_energy": 6.348148878900247,
                "cvrmse_percent": 5.59838067675047,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.049891844890192515,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.344983249698998,
                "relative_energy_error_percent": 0.04989184489019252,
                "rms_normalized_rmse_percent": 1.5166975000446776,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.012415370438247919,
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "reference": 0.012767289765179157,
                  "rgb_channel": 0,
                  "sky_patch_index": 70
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009273607283830643,
                  "p50": 3.818853429038427e-07,
                  "p90": 6.291580211836858e-05,
                  "p95": 0.00014953484060242753,
                  "p99": 0.0003291703760623932
                },
                "candidate_energy": 5.047678245711772,
                "cvrmse_percent": 12.598795712608496,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.20967981304896974,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.058284447083903,
                "relative_energy_error_percent": 0.20967981304896977,
                "rms_normalized_rmse_percent": 1.2935453185996435,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05797953903675079,
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "reference": 0.05890689976513386,
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.71129202097654,
            "full": 1496.8351669376716
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 126.51008402463049,
            "full": 1486.8534579873085
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.63437506370246,
            "full": 1475.8660000516102
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.89054199960083,
            "full": 1476.609249948524
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
            "identifier": "teaching_living_room_grid",
            "sensor_count": 20,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002019740641117096,
                  "p50": 0.0,
                  "p90": 1.1378922499716322e-05,
                  "p95": 5.406763521023088e-05,
                  "p99": 0.00012413947843015194
                },
                "candidate_energy": 6.346225434510416,
                "cvrmse_percent": 3.3261945256226464,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.011451460651394239,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.345498782214236,
                "relative_energy_error_percent": 0.011451460651394237,
                "rms_normalized_rmse_percent": 0.901638407006047,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007368935039266944,
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "reference": 0.007166960975155234,
                  "rgb_channel": 0,
                  "sky_patch_index": 43
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009486563503742218,
                  "p50": 3.0163570841068577e-07,
                  "p90": 3.668846911750742e-05,
                  "p95": 8.445698185823796e-05,
                  "p99": 0.00018397439271211624
                },
                "candidate_energy": 5.056239034536759,
                "cvrmse_percent": 7.776994474279908,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.15853328843731318,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.06426758447369,
                "relative_energy_error_percent": 0.1585332884373132,
                "rms_normalized_rmse_percent": 0.7991347568660464,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06949449703097343,
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "reference": 0.07044315338134766,
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 190.3982920339331,
            "full": 2593.171500018798
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 174.02595898602158,
            "full": 2615.9967080457136
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 179.22091693617404,
            "full": 2624.6729579288512
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
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "20",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 172.04345809295774,
            "full": 2588.5677080368623
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
    "/Users/ssanjay/GitHub/foton-0.3.8/validation/results/2026-11-14-architectural-v4-metal-0.3.8-release/teaching_living_room/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 468.68512500077486,
      "invocation_count": 2,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_living_room/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1372.52791703213,
      "invocation_count": 2,
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
      20,
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
        "identifier": "teaching_living_room_grid",
        "full_identifier": "teaching_living_room_grid",
        "start_sensor_index": 0,
        "sensor_count": 20,
        "stages": {
          "direct": {
            "nmbe_percent": 0.05157910077126447,
            "cvrmse_percent": 1.9383485945756473,
            "rms_normalized_rmse_percent": 0.5252373475133134,
            "reference_energy": 6.344794687406647,
            "candidate_energy": 6.348067275452195,
            "relative_energy_error_percent": 0.051579100771264465,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.7960555851459622e-07,
              "p95": 8.088909089565258e-06,
              "p99": 7.439218461513519e-05,
              "maximum": 0.0001857280731201172
            },
            "worst": {
              "global_sensor_index": 2,
              "local_sensor_index": 2,
              "sky_patch_index": 70,
              "rgb_channel": 0,
              "reference": 0.010556221939623356,
              "candidate": 0.010741950012743473,
              "position": [
                0.5,
                1.6875,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.304944677569344,
            "cvrmse_percent": 22.124923959870372,
            "rms_normalized_rmse_percent": 2.2737195081111223,
            "reference_energy": 5.061320709441306,
            "candidate_energy": 4.995273274228737,
            "relative_energy_error_percent": 1.304944677569344,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.1713168746041447e-06,
              "p90": 5.4289495164994255e-05,
              "p95": 8.0383734893985e-05,
              "p99": 0.0001944291580002755,
              "maximum": 0.002871997654438019
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06692522764205933,
              "candidate": 0.06405322998762131,
              "position": [
                1.5,
                0.5625,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5503613191952241,
            "cvrmse_percent": 9.783381086456691,
            "rms_normalized_rmse_percent": 2.2657812356262053,
            "reference_energy": 11.406115396847953,
            "candidate_energy": 11.343340549680931,
            "relative_energy_error_percent": 0.5503613191952241,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.1713168746041447e-06,
              "p90": 5.198625731281936e-05,
              "p95": 7.699965499341472e-05,
              "p99": 0.00017375219613313675,
              "maximum": 0.002871997654438019
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06692522764205933,
              "candidate": 0.06405322998762131,
              "position": [
                1.5,
                0.5625,
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
      20,
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
        "identifier": "teaching_living_room_grid",
        "full_identifier": "teaching_living_room_grid",
        "start_sensor_index": 0,
        "sensor_count": 20,
        "stages": {
          "direct": {
            "nmbe_percent": 0.05157910077126447,
            "cvrmse_percent": 1.9383485945756473,
            "rms_normalized_rmse_percent": 0.5252373475133134,
            "reference_energy": 6.344794687406647,
            "candidate_energy": 6.348067275452195,
            "relative_energy_error_percent": 0.051579100771264465,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.7960555851459622e-07,
              "p95": 8.088909089565258e-06,
              "p99": 7.439218461513519e-05,
              "maximum": 0.0001857280731201172
            },
            "worst": {
              "global_sensor_index": 2,
              "local_sensor_index": 2,
              "sky_patch_index": 70,
              "rgb_channel": 0,
              "reference": 0.010556221939623356,
              "candidate": 0.010741950012743473,
              "position": [
                0.5,
                1.6875,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 73.51607035180469,
            "cvrmse_percent": 387.67995322542384,
            "rms_normalized_rmse_percent": 28.410999780352817,
            "reference_energy": 2.8788533904097733,
            "candidate_energy": 4.995273274228737,
            "relative_energy_error_percent": 73.51607035180469,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.3505841423011589e-07,
              "p90": 0.000497136800549925,
              "p95": 0.0006409402143617624,
              "p99": 0.0010353541001677513,
              "maximum": 0.01757672242820263
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.029928086325526237,
              "candidate": 0.04750480875372887,
              "position": [
                3.5,
                3.9375,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 22.981064043006292,
            "cvrmse_percent": 121.01756326065912,
            "rms_normalized_rmse_percent": 28.414809734236954,
            "reference_energy": 9.22364807781642,
            "candidate_energy": 11.343340549680931,
            "relative_energy_error_percent": 22.981064043006295,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.3505841423011589e-07,
              "p90": 0.000495331430784063,
              "p95": 0.0006407847191439929,
              "p99": 0.0010096356272697449,
              "maximum": 0.01757672242820263
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.029928086325526237,
              "candidate": 0.04750480875372887,
              "position": [
                3.5,
                3.9375,
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
      "bias_percent": 0.15434640802669197,
      "rms_normalized_error_percent": 0.2700040343672333,
      "absolute_error": {
        "p95": 0.2029302661566795,
        "p99": 0.23755228424935274,
        "maximum": 0.24620778877252114
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 23.722997335783653,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2700040343672333
    },
    "overcast": {
      "bias_percent": 0.11070826866497707,
      "rms_normalized_error_percent": 0.20155853865744622,
      "absolute_error": {
        "p95": 0.08040914535522464,
        "p99": 0.11362058639526362,
        "maximum": 0.12192344665527344
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.343339920043945,
      "reference_fraction_of_uniform": 0.646770715713501,
      "rms_normalized_to_uniform_percent": 0.14001960050383347
    },
    "horizon": {
      "bias_percent": 1.1692027115182995,
      "rms_normalized_error_percent": 2.4150350470728217,
      "absolute_error": {
        "p95": 0.10906537433766327,
        "p99": 0.14537759867132477,
        "maximum": 0.1544556547547402
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.1033970510277262,
      "reference_fraction_of_uniform": 0.08866489429035902,
      "rms_normalized_to_uniform_percent": 0.16055996813851292
    },
    "north": {
      "bias_percent": -74.2985671865249,
      "rms_normalized_error_percent": 96.35890454629372,
      "absolute_error": {
        "p95": 0.00012182323507659043,
        "p99": 0.0003484023035525748,
        "maximum": 0.0004050470706715714
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 4.3159499909961596e-05,
      "reference_fraction_of_uniform": 1.81931056886242e-06,
      "rms_normalized_to_uniform_percent": 0.000295792915484616
    },
    "east": {
      "bias_percent": -0.061848103847150185,
      "rms_normalized_error_percent": 0.26287314887443597,
      "absolute_error": {
        "p95": 0.03330849409103394,
        "p99": 0.036026284694671624,
        "maximum": 0.036705732345581055
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.652248859405518,
      "reference_fraction_of_uniform": 0.19610711932182312,
      "rms_normalized_to_uniform_percent": 0.057920985436610534
    },
    "south": {
      "bias_percent": 0.2058669800576119,
      "rms_normalized_error_percent": 0.35818412855354165,
      "absolute_error": {
        "p95": 0.19350214004516603,
        "p99": 0.21566194534301755,
        "maximum": 0.22120189666748047
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 16.359933853149414,
      "reference_fraction_of_uniform": 0.6896233558654785,
      "rms_normalized_to_uniform_percent": 0.23475421830066712
    },
    "west": {
      "bias_percent": 0.25454475588222314,
      "rms_normalized_error_percent": 0.346021554290151,
      "absolute_error": {
        "p95": 0.0473682999610901,
        "p99": 0.05566735506057738,
        "maximum": 0.05774211883544922
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.515198230743408,
      "reference_fraction_of_uniform": 0.19032999873161316,
      "rms_normalized_to_uniform_percent": 0.07299318661321803
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
        "identifier": "teaching_living_room_grid",
        "sensor_count": 20,
        "illuminance": {
          "nmbe_percent": 0.022142585970885312,
          "cvrmse_percent": 1.1275934384772497,
          "absolute_error_percentiles_lux": {
            "p50": 4.185089111328125,
            "p90": 36.20239257812504,
            "p95": 52.669085693359385,
            "p99": 96.48178710937482
          },
          "maximum_absolute_error_lux": 257.87890625,
          "worst": {
            "sensor_index": 6,
            "position": [
              1.5,
              1.6875,
              0.75
            ],
            "hour_of_year": 2603.5,
            "foton_lux": 22129.025390625,
            "radiance_lux": 21871.146484375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.10519863013698796,
            "maximum_error_percentage_points": 0.5235616438356203,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.04903151979784966,
            "maximum_error_percentage_points": 0.20714456839112927,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.036746575342465615,
            "maximum_error_percentage_points": 0.16013698630137085,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.07290410958904267,
            "maximum_error_percentage_points": 0.2461643835616485,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.07389726027397303,
            "maximum_error_percentage_points": 0.22041095890410922,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 5.0,
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
            "identifier": "teaching_living_room_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_living_room_grid",
            "maximum_error_percentage_points": 0.004805222602726644,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_living_room_grid",
            "maximum_error_percentage_points": 0.00438356164384146,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_living_room_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_living_room_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
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
      "study_preparation_seconds": 0.009942833101376891,
      "weather_seconds": 0.07723774993792176,
      "metric_reduction_seconds": 0.043411332881078124,
      "write_seconds": 0.02965166699141264,
      "total_seconds": 0.15040770801715553,
      "cold_end_to_end_seconds": 0.16035054111853242,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0018775002099573612,
      "engine_upload_seconds": 0.000295209,
      "engine_acceleration_structure_seconds": 0.003592125,
      "engine_tracing_seconds": 0.021650791633874178,
      "engine_annual_reduction_seconds": 0.00020187487825751305,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.021650791633874178
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.009942833101376891,
      "weather_seconds": 0.07285150000825524,
      "metric_reduction_seconds": 0.013909332919865847,
      "write_seconds": 0.018185375025495887,
      "total_seconds": 0.10535145900212228,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.10535145900212228,
      "raw_export_seconds": 0.0016504998784512281,
      "engine_upload_seconds": 4.9792e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0008019166998565197,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.014211875153705478,
      "full": 0.015510624973103404
    }
  },
  "elapsed_seconds": 0.7019812089856714,
  "result_class": "passed"
}
```
