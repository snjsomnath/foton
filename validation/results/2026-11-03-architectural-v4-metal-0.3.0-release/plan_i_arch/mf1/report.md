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
  "model_sha256": "12a5f3f112f0a318b25ea951f34a144e0fdc5bf055b28b6aef77641038418813",
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
      "scene_fingerprint": 5547156972887524777,
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
      "scene_fingerprint": 5547156972887524777,
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/foton-references-corpus4-2026-11-03",
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/plan_i_arch/mf1/oracle/scene.rad"
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
            "nmbe_percent": 0.03977234400479781,
            "cvrmse_percent": 8.954201771439525,
            "rms_normalized_rmse_percent": 0.8810950922952137,
            "reference_energy": 2.8764198793951437,
            "candidate_energy": 2.877563899004599,
            "relative_energy_error_percent": 0.03977234400479781,
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
            "nmbe_percent": -1.5023371328667237,
            "cvrmse_percent": 55.96345916862188,
            "rms_normalized_rmse_percent": 2.2091736403815587,
            "reference_energy": 1.3439884321503097,
            "candidate_energy": 1.3237971948726823,
            "relative_energy_error_percent": 1.5023371328667237,
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
            "nmbe_percent": -0.4513122016195904,
            "cvrmse_percent": 17.288341388163726,
            "rms_normalized_rmse_percent": 2.143075989077763,
            "reference_energy": 4.220408311545453,
            "candidate_energy": 4.201361093877281,
            "relative_energy_error_percent": 0.4513122016195904,
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
            "nmbe_percent": 0.03977234400479781,
            "cvrmse_percent": 8.954201771439525,
            "rms_normalized_rmse_percent": 0.8810950922952137,
            "reference_energy": 2.8764198793951437,
            "candidate_energy": 2.877563899004599,
            "relative_energy_error_percent": 0.03977234400479781,
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
            "nmbe_percent": 88.3476745508524,
            "cvrmse_percent": 603.6454123775814,
            "rms_normalized_rmse_percent": 13.321324365162893,
            "reference_energy": 0.7028476449361563,
            "candidate_energy": 1.3237971948726823,
            "relative_energy_error_percent": 88.34767455085242,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.2243918869644403e-05,
              "p95": 8.415999764110893e-05,
              "p99": 0.00018960607121698558,
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
            "nmbe_percent": 17.380471432132044,
            "cvrmse_percent": 118.46821952560713,
            "rms_normalized_rmse_percent": 13.313747809809215,
            "reference_energy": 3.5792675243313,
            "candidate_energy": 4.201361093877281,
            "relative_energy_error_percent": 17.380471432132044,
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
      "bias_percent": 0.05450253584494539,
      "rms_normalized_error_percent": 0.21826008344679484,
      "absolute_error": {
        "p95": 0.03717933514439245,
        "p99": 0.05016894280569272,
        "maximum": 0.07061404381323655
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.644048165938102,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.21826008344679484
    },
    "overcast": {
      "bias_percent": 0.0698241256417691,
      "rms_normalized_error_percent": 0.19995608064565287,
      "absolute_error": {
        "p95": 0.025311951339244836,
        "p99": 0.040010654926299995,
        "maximum": 0.05001044273376465
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.7269335985183716,
      "reference_fraction_of_uniform": 0.6531400084495544,
      "rms_normalized_to_uniform_percent": 0.1426266126671268
    },
    "horizon": {
      "bias_percent": 0.09149979103510261,
      "rms_normalized_error_percent": 2.6266382424039385,
      "absolute_error": {
        "p95": 0.02036615603419471,
        "p99": 0.027900872556746937,
        "maximum": 0.03102448925837681
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.23401454890873047,
      "reference_fraction_of_uniform": 0.08850615957886783,
      "rms_normalized_to_uniform_percent": 0.1080208161428728
    },
    "north": {
      "bias_percent": -88.44640710314451,
      "rms_normalized_error_percent": 102.68559252960893,
      "absolute_error": {
        "p95": 9.040095319505777e-05,
        "p99": 0.00021769288854556996,
        "maximum": 0.00038891867734491825
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.3221598237578291e-05,
      "reference_fraction_of_uniform": 5.000513283448527e-06,
      "rms_normalized_to_uniform_percent": 0.000609948506005057
    },
    "east": {
      "bias_percent": -0.08117137192966713,
      "rms_normalized_error_percent": 0.3181553822150725,
      "absolute_error": {
        "p95": 0.012787748873233784,
        "p99": 0.02240536153316495,
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
      "rms_normalized_to_uniform_percent": 0.07508439897860525
    },
    "south": {
      "bias_percent": 0.07075195485752012,
      "rms_normalized_error_percent": 0.2516402022833672,
      "absolute_error": {
        "p95": 0.027402973175048827,
        "p99": 0.03939469099044793,
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
      "rms_normalized_to_uniform_percent": 0.1654732525311666
    },
    "west": {
      "bias_percent": 0.007445311501980384,
      "rms_normalized_error_percent": 0.28237137879903584,
      "absolute_error": {
        "p95": 0.011582016944885245,
        "p99": 0.01932207882404327,
        "maximum": 0.020063817501068115
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.4893185794353485,
      "reference_fraction_of_uniform": 0.1850641667842865,
      "rms_normalized_to_uniform_percent": 0.06386189111528731
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
          "nmbe_percent": -0.01640916793493558,
          "cvrmse_percent": 3.3316018886323886,
          "absolute_error_percentiles_lux": {
            "p50": 0.4625861644744873,
            "p90": 7.826435685157788,
            "p95": 14.185988426208493,
            "p99": 33.93403884887695
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
      "study_preparation_seconds": 0.007555958000011742,
      "weather_seconds": 0.09589199989568442,
      "metric_reduction_seconds": 0.05343916697893292,
      "write_seconds": 0.036253083031624556,
      "total_seconds": 0.1857877499423921,
      "cold_end_to_end_seconds": 0.19334370794240385,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.01244470791425556,
      "engine_upload_seconds": 0.000421833,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.03165687492582947,
      "engine_annual_reduction_seconds": 0.0006783750141039491,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.03165687492582947
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007555958000011742,
      "weather_seconds": 0.09897137503139675,
      "metric_reduction_seconds": 0.013515167054720223,
      "write_seconds": 0.04254458309151232,
      "total_seconds": 0.1551808329531923,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1551808329531923,
      "raw_export_seconds": 0.023530457983724773,
      "engine_upload_seconds": 5.175e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0006108749657869339,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.017642750055529177,
      "full": 0.03586400009226054
    }
  },
  "elapsed_seconds": 0.8533562499796972,
  "result_class": "passed"
}
```
