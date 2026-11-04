# Foton report

Status: **passed**

```json
{
  "scene": "plan_i_arch",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_i_arch",
    "category": "form",
    "question": "How does a arch opening illuminate a I-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "i",
    "window_profile": "arch"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 74,
    "floor_area": 90.0,
    "aperture_area": 1.4399999999999993
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "9dbb68cfc4a2be16660061d78df5ea1056596acd68ff0ba664c56979725f95db",
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 5547156972887524777,
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 5547156972887524777,
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
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "a9ef6bf81d1bb39e75b9324bd5666316c60d0cceae7a81ac8f388465a9a33223",
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
          "maximum": 0.0006167888641357422,
          "p95": 0.0,
          "p99": 2.1290863514877856e-05
        },
        "bias_percent": -0.01416242129909043,
        "identifier": "plan_i_arch_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.5881895401858381,
        "worst_index": [
          48,
          133,
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
          "maximum": 0.0003351811319589615,
          "p95": 1.0133036994375288e-05,
          "p99": 6.178789772093296e-05
        },
        "bias_percent": 0.035930250837669354,
        "identifier": "plan_i_arch_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.250135536357077,
        "worst_index": [
          45,
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
          "maximum": 0.0003195563331246376,
          "p95": 8.15652310848236e-06,
          "p99": 4.8949383199214935e-05
        },
        "bias_percent": -0.0253570176859172,
        "identifier": "plan_i_arch_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.117263928803039,
        "worst_index": [
          48,
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
            "identifier": "plan_i_arch_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000688125379383564,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.15700220502913e-05
                },
                "candidate_energy": 2.880424799903267,
                "cvrmse_percent": 23.862826960405293,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.028173840154334835,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.8812365548847083,
                "relative_energy_error_percent": 0.02817384015433483,
                "rms_normalized_rmse_percent": 2.350446441731486,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.01611472014337778,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.016802845522761345,
                  "rgb_channel": 0,
                  "sky_patch_index": 116
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008981415303424001,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 5.529680038307561e-06,
                  "p99": 0.0001712911471258849
                },
                "candidate_energy": 0.7017002268221404,
                "cvrmse_percent": 175.53739196962178,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.9388657863640678,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6951734808545211,
                "relative_energy_error_percent": 0.9388657863640679,
                "rms_normalized_rmse_percent": 3.832408778126659,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0003304674755781889,
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "reference": -0.0005676740547642112,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.15766694583,
            "full": 397.23929204046726
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.50595793500543,
            "full": 405.9061660664156
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.74033397529274,
            "full": 407.77116699609905
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 181.92083307076246,
            "full": 409.90245807915926
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
            "identifier": "plan_i_arch_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00039891109918244183,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.515346467494965e-05
                },
                "candidate_energy": 2.876905150559196,
                "cvrmse_percent": 17.28187549819004,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.004517457247941418,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.8767751934697117,
                "relative_energy_error_percent": 0.004517457247941417,
                "rms_normalized_rmse_percent": 1.700028238450479,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0008217768918257207,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.0012206879910081625,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006132519338279963,
                  "p50": 0.0,
                  "p90": 6.456271876231767e-06,
                  "p95": 1.3958146155346185e-05,
                  "p99": 0.00010598867083899677
                },
                "candidate_energy": 1.3421796366099272,
                "cvrmse_percent": 57.705864803101946,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.1402735178268482,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.344065003872739,
                "relative_energy_error_percent": 0.1402735178268482,
                "rms_normalized_rmse_percent": 2.2778414777018114,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -6.739445962011814e-05,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.0005458574742078781,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 199.88654204644263,
            "full": 5579.294792027213
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 215.2009579585865,
            "full": 5419.842874980532
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 212.91970810852945,
            "full": 5637.992540956475
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 211.92562498617917,
            "full": 5594.538083998486
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
            "identifier": "plan_i_arch_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003872276283800602,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.577640306204557e-05
                },
                "candidate_energy": 2.8766880513489923,
                "cvrmse_percent": 16.633104560002533,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.06910974603916843,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.8786774980571863,
                "relative_energy_error_percent": 0.06910974603916843,
                "rms_normalized_rmse_percent": 1.6372259756772467,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00454164738766849,
                  "global_sensor_index": 57,
                  "local_sensor_index": 57,
                  "reference": 0.004928875016048551,
                  "rgb_channel": 0,
                  "sky_patch_index": 51
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004330645315349102,
                  "p50": 0.0,
                  "p90": 6.874419341329485e-06,
                  "p95": 1.4259348972700536e-05,
                  "p99": 0.00011888891458511353
                },
                "candidate_energy": 1.3453965957612368,
                "cvrmse_percent": 57.419644450675996,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.23850660797321407,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3421953711092307,
                "relative_energy_error_percent": 0.23850660797321405,
                "rms_normalized_rmse_percent": 2.2629169634314152,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 3.880029544234276e-05,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.00047186482697725296,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 202.19149999320507,
            "full": 5871.550041018054
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 214.56899994518608,
            "full": 5812.918584095314
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 206.43987506628036,
            "full": 5738.4430839447305
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 205.5383330443874,
            "full": 5712.422291981056
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
            "identifier": "plan_i_arch_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00019861944019794464,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.521749749779701e-05
                },
                "candidate_energy": 2.8769999434953206,
                "cvrmse_percent": 9.465021588896068,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.05209004689932018,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.87849935515942,
                "relative_energy_error_percent": 0.052090046899320175,
                "rms_normalized_rmse_percent": 0.9317578456874723,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.009531254880130291,
                  "global_sensor_index": 48,
                  "local_sensor_index": 48,
                  "reference": 0.009729874320328236,
                  "rgb_channel": 0,
                  "sky_patch_index": 77
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000306909903883934,
                  "p50": 0.0,
                  "p90": 4.917455953545868e-06,
                  "p95": 9.919214789988473e-06,
                  "p99": 6.649037823081017e-05
                },
                "candidate_energy": 1.3420005401208535,
                "cvrmse_percent": 35.96538285167497,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.09798499627809978,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3433167890265842,
                "relative_energy_error_percent": 0.09798499627809978,
                "rms_normalized_rmse_percent": 1.418587621982392,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -9.385496377944946e-05,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.00021305494010448456,
                  "rgb_channel": 0,
                  "sky_patch_index": 118
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 306.54037499334663,
            "full": 10686.130209011026
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 316.44062499981374,
            "full": 10288.626374909654
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 341.2981249857694,
            "full": 10387.463333900087
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 331.351333996281,
            "full": 10465.575291076675
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
    "/content/suite-vulkan-0.3.3/plan_i_arch/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 3128.7694580387324,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_arch/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10984.550416003913,
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
        "identifier": "plan_i_arch_grid",
        "full_identifier": "plan_i_arch_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": 0.03977044088985283,
            "cvrmse_percent": 8.954206721671909,
            "rms_normalized_rmse_percent": 0.8810955793989859,
            "reference_energy": 2.8764198793951437,
            "candidate_energy": 2.8775638442630225,
            "relative_energy_error_percent": 0.03977044088985283,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.6095145838335156e-05,
              "maximum": 0.00047633983194828033
            },
            "worst": {
              "global_sensor_index": 36,
              "local_sensor_index": 36,
              "sky_patch_index": 133,
              "rgb_channel": 0,
              "reference": 0.009515693411231041,
              "candidate": 0.00903935357928276,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.5022881736146894,
            "cvrmse_percent": 55.962889784687,
            "rms_normalized_rmse_percent": 2.209151163787029,
            "reference_energy": 1.3439884321503097,
            "candidate_energy": 1.3237978528793661,
            "relative_energy_error_percent": 1.5022881736146894,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.0897010724875145e-05,
              "p95": 2.0839215721935034e-05,
              "p99": 5.771587530034594e-05,
              "maximum": 0.0009848317131400108
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015416571870446205,
              "candidate": 0.014431740157306194,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.45129790762093747,
            "cvrmse_percent": 17.288156305406797,
            "rms_normalized_rmse_percent": 2.1430530460779997,
            "reference_energy": 4.220408311545453,
            "candidate_energy": 4.201361697142389,
            "relative_energy_error_percent": 0.4512979076209374,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.0797699815157102e-05,
              "p95": 2.0485730601649266e-05,
              "p99": 5.771587530034594e-05,
              "maximum": 0.0009848317131400108
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015416571870446205,
              "candidate": 0.014431740157306194,
              "position": [
                5.5,
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
        "identifier": "plan_i_arch_grid",
        "full_identifier": "plan_i_arch_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": 0.03977044088985283,
            "cvrmse_percent": 8.954206721671909,
            "rms_normalized_rmse_percent": 0.8810955793989859,
            "reference_energy": 2.8764198793951437,
            "candidate_energy": 2.8775638442630225,
            "relative_energy_error_percent": 0.03977044088985283,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.6095145838335156e-05,
              "maximum": 0.00047633983194828033
            },
            "worst": {
              "global_sensor_index": 36,
              "local_sensor_index": 36,
              "sky_patch_index": 133,
              "rgb_channel": 0,
              "reference": 0.009515693411231041,
              "candidate": 0.00903935357928276,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 88.34776817095465,
            "cvrmse_percent": 603.6460971970672,
            "rms_normalized_rmse_percent": 13.32133947784712,
            "reference_energy": 0.7028476449361563,
            "candidate_energy": 1.3237978528793661,
            "relative_energy_error_percent": 88.34776817095467,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.2243918869644403e-05,
              "p95": 8.415999764110893e-05,
              "p99": 0.00018960610032081604,
              "maximum": 0.003154638223350048
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00500769168138504,
              "candidate": 0.008162329904735088,
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
            "nmbe_percent": 17.380488286561146,
            "cvrmse_percent": 118.46835273449996,
            "rms_normalized_rmse_percent": 13.313762780149888,
            "reference_energy": 3.5792675243313,
            "candidate_energy": 4.201361697142389,
            "relative_energy_error_percent": 17.380488286561146,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.203524440526962e-05,
              "p95": 8.415999764110893e-05,
              "p99": 0.00018832118439604528,
              "maximum": 0.003154638223350048
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00500769168138504,
              "candidate": 0.008162329904735088,
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
      "bias_percent": 0.0544998874965486,
      "rms_normalized_error_percent": 0.2182607229365199,
      "absolute_error": {
        "p95": 0.03717934530308447,
        "p99": 0.05017020412453594,
        "maximum": 0.07061387710649214
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.644048165938102,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2182607229365199
    },
    "overcast": {
      "bias_percent": 0.06982538659439494,
      "rms_normalized_error_percent": 0.19995388317834334,
      "absolute_error": {
        "p95": 0.025312452018260947,
        "p99": 0.040007934570312445,
        "maximum": 0.05001068115234375
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.726933479309082,
      "reference_fraction_of_uniform": 0.6531399488449097,
      "rms_normalized_to_uniform_percent": 0.14262502940600394
    },
    "horizon": {
      "bias_percent": 0.09149670747459679,
      "rms_normalized_error_percent": 2.626638372083006,
      "absolute_error": {
        "p95": 0.020366191459377597,
        "p99": 0.027900851718404108,
        "maximum": 0.03102446842003398
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.23401454890873047,
      "reference_fraction_of_uniform": 0.08850615957886783,
      "rms_normalized_to_uniform_percent": 0.10802082147594017
    },
    "north": {
      "bias_percent": -88.4464079776975,
      "rms_normalized_error_percent": 102.68559191913252,
      "absolute_error": {
        "p95": 9.040095319505777e-05,
        "p99": 0.00021769288578070607,
        "maximum": 0.0003889187064487487
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.3221599147072993e-05,
      "reference_fraction_of_uniform": 5.0005137381958775e-06,
      "rms_normalized_to_uniform_percent": 0.000609948506005057
    },
    "east": {
      "bias_percent": -0.08117324417851533,
      "rms_normalized_error_percent": 0.31815476085081684,
      "absolute_error": {
        "p95": 0.012787665426731099,
        "p99": 0.022405405044555637,
        "maximum": 0.02765357494354248
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.49576616287231445,
      "reference_fraction_of_uniform": 0.1875026971101761,
      "rms_normalized_to_uniform_percent": 0.07508424921066119
    },
    "south": {
      "bias_percent": 0.07074773324850044,
      "rms_normalized_error_percent": 0.25164085648871154,
      "absolute_error": {
        "p95": 0.027402639389038086,
        "p99": 0.03939573526382439,
        "maximum": 0.05287504196166992
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.814223051071167,
      "reference_fraction_of_uniform": 0.6861535310745239,
      "rms_normalized_to_uniform_percent": 0.16547368043957816
    },
    "west": {
      "bias_percent": 0.007435334315406574,
      "rms_normalized_error_percent": 0.28236906108110493,
      "absolute_error": {
        "p95": 0.011580777168273918,
        "p99": 0.019322049021720883,
        "maximum": 0.020063787698745728
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.4893186390399933,
      "reference_fraction_of_uniform": 0.1850641965866089,
      "rms_normalized_to_uniform_percent": 0.06386136692748312
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
        "identifier": "plan_i_arch_grid",
        "sensor_count": 74,
        "illuminance": {
          "nmbe_percent": -0.01640919759832978,
          "cvrmse_percent": 3.331607503969912,
          "absolute_error_percentiles_lux": {
            "p50": 0.4625868797302246,
            "p90": 7.826332855224612,
            "p95": 14.185991573333736,
            "p99": 33.93405990600586
          },
          "maximum_absolute_error_lux": 233.21435546875,
          "worst": {
            "sensor_index": 34,
            "position": [
              5.5,
              2.5,
              0.75
            ],
            "hour_of_year": 1859.5,
            "foton_lux": 7261.974609375,
            "radiance_lux": 7028.76025390625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.15928915216586495,
            "maximum_error_percentage_points": 2.0308219178082183,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.30954170842019363,
            "maximum_error_percentage_points": 1.4452890288788538,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.46961495742317605,
            "maximum_error_percentage_points": 4.354246575342458,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.47069603850425795,
            "maximum_error_percentage_points": 4.354246575342465,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0036467974824140035,
            "maximum_error_percentage_points": 0.08712328767123267,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 5.405405405405405,
          "radiance_percent": 5.405405405405405,
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
      "maximum_error_percentage_points": 0.004944010695365986,
      "metrics": {
        "da": [
          {
            "identifier": "plan_i_arch_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_i_arch_grid",
            "maximum_error_percentage_points": 0.004944010695365986,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_i_arch_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_i_arch_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_i_arch_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
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
      "study_preparation_seconds": 0.365819336000186,
      "weather_seconds": 0.22933129600005486,
      "metric_reduction_seconds": 0.277745718999995,
      "write_seconds": 0.01331431300013719,
      "total_seconds": 0.5207538610000029,
      "cold_end_to_end_seconds": 0.8865731970001889,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.002326079999875219,
      "engine_upload_seconds": 0.013902523,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.021954522,
      "engine_annual_reduction_seconds": 0.014836223,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.021954522
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.365819336000186,
      "weather_seconds": 0.23676461399986692,
      "metric_reduction_seconds": 0.2497652710001148,
      "write_seconds": 0.013369490000059159,
      "total_seconds": 0.5001759950000633,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.5001759950000633,
      "raw_export_seconds": 0.002339585000072475,
      "engine_upload_seconds": 0.016103206000000002,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 2.44e-07,
      "engine_annual_reduction_seconds": 0.017468691,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.014148105000003852,
      "full": 0.03155999199998405
    }
  },
  "elapsed_seconds": 3.276606855999944,
  "result_class": "passed"
}
```
