# Foton report

Status: **passed**

```json
{
  "scene": "plan_i_offset_high",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_i_offset_high",
    "category": "form",
    "question": "How does a offset high opening illuminate a I-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "i",
    "window_profile": "offset_high"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 74,
    "floor_area": 90.0,
    "aperture_area": 1.4399999999999988
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "2c01f4cbbaf58c3498c0b160a5dd5078a3dd02b8470d04c87b9bdc8581942edd",
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 6409402939110902228,
      "basis": "ReinhartMf2",
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 6409402939110902228,
      "basis": "ReinhartMf2",
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
  "reference_source": {
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "292b7c5f83b55d544c8fd1bd9022c51d67ac087a02b36fb594c3872732937a49",
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
          "maximum": 0.00021733436733484268,
          "p95": 0.0,
          "p99": 0.0
        },
        "bias_percent": -0.04025754578607849,
        "identifier": "plan_i_offset_high_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.2851339553167704,
        "worst_index": [
          68,
          447,
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
          "maximum": 0.000629933550953865,
          "p95": 3.334404027555138e-06,
          "p99": 1.419842428731549e-05
        },
        "bias_percent": 0.13720939335519272,
        "identifier": "plan_i_offset_high_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.5478941322995856,
        "worst_index": [
          67,
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
          "maximum": 0.000420641154050827,
          "p95": 2.828352080541663e-06,
          "p99": 1.1659913434414293e-05
        },
        "bias_percent": 0.09463707720490196,
        "identifier": "plan_i_offset_high_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3799962618549932,
        "worst_index": [
          67,
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "plan_i_offset_high_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007945054676383734,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 1.1188033383227776,
                "cvrmse_percent": 106.37702413366296,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.11679549793898512,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1201115782180295,
                "relative_energy_error_percent": 0.11679549793898512,
                "rms_normalized_rmse_percent": 5.803462582964005,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0030345754930749536,
                  "global_sensor_index": 67,
                  "local_sensor_index": 67,
                  "reference": 0.003829080960713327,
                  "rgb_channel": 0,
                  "sky_patch_index": 356
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000841952976770699,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.9758451748639345e-06,
                  "p99": 2.8445522207222478e-05
                },
                "candidate_energy": 0.6414746658023596,
                "cvrmse_percent": 291.3086081235623,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.6354650289792351,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6374240588222442,
                "relative_energy_error_percent": 0.635465028979235,
                "rms_normalized_rmse_percent": 5.234698498413692,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0006331660551950336,
                  "global_sensor_index": 67,
                  "local_sensor_index": 67,
                  "reference": -0.00020878692157566547,
                  "rgb_channel": 0,
                  "sky_patch_index": 356
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 167.71924996282905,
            "full": 403.50416698493063
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 162.47675009071827,
            "full": 383.650750038214
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.78925001621246,
            "full": 405.8931670151651
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 145.5112500116229,
            "full": 396.60829096101224
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "plan_i_offset_high_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002692140405997634,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 1.122793157100432,
                "cvrmse_percent": 71.86573004817329,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.138855399564717,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1212362600115284,
                "relative_energy_error_percent": 0.138855399564717,
                "rms_normalized_rmse_percent": 3.9160002555225213,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0037547569954767823,
                  "global_sensor_index": 72,
                  "local_sensor_index": 72,
                  "reference": 0.004023971036076546,
                  "rgb_channel": 0,
                  "sky_patch_index": 362
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005506742745637894,
                  "p50": 0.0,
                  "p90": 2.003801455430221e-06,
                  "p95": 4.776328040634326e-06,
                  "p99": 2.0951148644599816e-05
                },
                "candidate_energy": 1.1444090350511864,
                "cvrmse_percent": 120.68735040945009,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.2614678773121812,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1474091413772314,
                "relative_energy_error_percent": 0.2614678773121812,
                "rms_normalized_rmse_percent": 2.979909093756531,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.029594100080430508,
                  "global_sensor_index": 73,
                  "local_sensor_index": 73,
                  "reference": 0.030144774354994297,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 209.15141701698303,
            "full": 5261.60595798865
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 210.01570799853653,
            "full": 5329.756750026718
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 205.86141699459404,
            "full": 5276.279165991582
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 209.43737507332116,
            "full": 5241.314332932234
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "plan_i_offset_high_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003391013015061617,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 1.1227182542452283,
                "cvrmse_percent": 66.89532510366604,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.27416369962479703,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.119648584263814,
                "relative_energy_error_percent": 0.2741636996247971,
                "rms_normalized_rmse_percent": 3.647013996507825,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00396987737622112,
                  "global_sensor_index": 72,
                  "local_sensor_index": 72,
                  "reference": 0.0036307760747149587,
                  "rgb_channel": 0,
                  "sky_patch_index": 313
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004255963722243905,
                  "p50": 0.0,
                  "p90": 2.0254218888737796e-06,
                  "p95": 4.739972979450613e-06,
                  "p99": 2.1487875164894265e-05
                },
                "candidate_energy": 1.1494088100962898,
                "cvrmse_percent": 100.14702048792718,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.07708903005893246,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1502955617876829,
                "relative_energy_error_percent": 0.07708903005893246,
                "rms_normalized_rmse_percent": 2.472852058333756,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00016032846178859472,
                  "global_sensor_index": 72,
                  "local_sensor_index": 72,
                  "reference": 0.0002652679104357958,
                  "rgb_channel": 0,
                  "sky_patch_index": 313
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 205.0287500023842,
            "full": 5517.214625026099
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 202.9564999975264,
            "full": 5590.769125032239
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 207.5479170307517,
            "full": 5660.294249886647
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 205.01487492583692,
            "full": 5613.92195802182
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "plan_i_offset_high_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001366993528790772,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 1.1231720831449366,
                "cvrmse_percent": 34.81669190355547,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.15771717217209077,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1214034373548998,
                "relative_energy_error_percent": 0.15771717217209077,
                "rms_normalized_rmse_percent": 1.9011924374010643,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0003175051388097927,
                  "global_sensor_index": 46,
                  "local_sensor_index": 46,
                  "reference": 0.0004542044916888699,
                  "rgb_channel": 0,
                  "sky_patch_index": 140
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00043462030589580536,
                  "p50": 0.0,
                  "p90": 1.411179937349516e-06,
                  "p95": 3.4564816360216355e-06,
                  "p99": 1.4613410348829364e-05
                },
                "candidate_energy": 1.1487817362123138,
                "cvrmse_percent": 64.68369048114855,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.36692642275425374,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1530124435252525,
                "relative_energy_error_percent": 0.3669264227542538,
                "rms_normalized_rmse_percent": 1.5990005879615568,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.028815599158406258,
                  "global_sensor_index": 68,
                  "local_sensor_index": 68,
                  "reference": 0.029250219464302063,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 323.72970797587186,
            "full": 10038.00375002902
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 346.7484579887241,
            "full": 10182.615124969743
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 320.65604196395725,
            "full": 9969.648791011423
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 317.9860420059413,
            "full": 10234.688458032906
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/plan_i_offset_high/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 12205.507208011113,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 45190.48250000924,
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
        "identifier": "plan_i_offset_high_grid",
        "full_identifier": "plan_i_offset_high_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": -0.08696802400646497,
            "cvrmse_percent": 11.902271073879186,
            "rms_normalized_rmse_percent": 0.6501606820881254,
            "reference_energy": 1.1231927205457595,
            "candidate_energy": 1.1222159020309164,
            "relative_energy_error_percent": 0.08696802400646496,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 6.128521636128426e-05
            },
            "worst": {
              "global_sensor_index": 68,
              "local_sensor_index": 68,
              "sky_patch_index": 447,
              "rgb_channel": 0,
              "reference": 0.0024364946875721216,
              "candidate": 0.0023752094712108374,
              "position": [
                10.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.0294345024164908,
            "cvrmse_percent": 91.06139457900284,
            "rms_normalized_rmse_percent": 2.2486674093995433,
            "reference_energy": 1.149992126441063,
            "candidate_energy": 1.1381537107164057,
            "relative_energy_error_percent": 1.0294345024164908,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.884327986090284e-06,
              "p95": 4.246249318384798e-06,
              "p99": 1.449281444365627e-05,
              "maximum": 0.0009439680725336075
            },
            "worst": {
              "global_sensor_index": 68,
              "local_sensor_index": 68,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.029032908380031586,
              "candidate": 0.028088940307497978,
              "position": [
                10.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.563756803873098,
            "cvrmse_percent": 45.85176978558798,
            "rms_normalized_rmse_percent": 2.238138289779697,
            "reference_energy": 2.2731848469868225,
            "candidate_energy": 2.260369612747322,
            "relative_energy_error_percent": 0.563756803873098,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.8794880531913805e-06,
              "p95": 4.246249318384798e-06,
              "p99": 1.4164340518618716e-05,
              "maximum": 0.0009439680725336075
            },
            "worst": {
              "global_sensor_index": 68,
              "local_sensor_index": 68,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.029032908380031586,
              "candidate": 0.028088940307497978,
              "position": [
                10.5,
                0.5,
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
        "identifier": "plan_i_offset_high_grid",
        "full_identifier": "plan_i_offset_high_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": -0.08696802400646497,
            "cvrmse_percent": 11.902271073879186,
            "rms_normalized_rmse_percent": 0.6501606820881254,
            "reference_energy": 1.1231927205457595,
            "candidate_energy": 1.1222159020309164,
            "relative_energy_error_percent": 0.08696802400646496,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 6.128521636128426e-05
            },
            "worst": {
              "global_sensor_index": 68,
              "local_sensor_index": 68,
              "sky_patch_index": 447,
              "rgb_channel": 0,
              "reference": 0.0024364946875721216,
              "candidate": 0.0023752094712108374,
              "position": [
                10.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 79.03546708440204,
            "cvrmse_percent": 1893.3596867907625,
            "rms_normalized_rmse_percent": 33.837767884732024,
            "reference_energy": 0.6357141013740311,
            "candidate_energy": 1.1381537107164057,
            "relative_energy_error_percent": 79.03546708440206,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.640000042854808e-06,
              "p95": 1.293163495574845e-05,
              "p99": 5.0005810953735065e-05,
              "maximum": 0.008242310956120491
            },
            "worst": {
              "global_sensor_index": 73,
              "local_sensor_index": 73,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021251589059829712,
              "candidate": 0.029493900015950203,
              "position": [
                11.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 28.509912212416175,
            "cvrmse_percent": 684.2918270809541,
            "rms_normalized_rmse_percent": 33.83692761533304,
            "reference_energy": 1.7589068219197905,
            "candidate_energy": 2.260369612747322,
            "relative_energy_error_percent": 28.50991221241617,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.640000042854808e-06,
              "p95": 1.2900000001536682e-05,
              "p99": 4.9796713392425234e-05,
              "maximum": 0.008242310956120491
            },
            "worst": {
              "global_sensor_index": 73,
              "local_sensor_index": 73,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021251589059829712,
              "candidate": 0.029493900015950203,
              "position": [
                11.5,
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
      "bias_percent": 0.11031821174288008,
      "rms_normalized_error_percent": 0.25780685711051377,
      "absolute_error": {
        "p95": 0.012280339250749553,
        "p99": 0.04064921840917794,
        "maximum": 0.0765596286027943
      },
      "worst_index": [
        67
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.283264039907282,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.25780685711051377
    },
    "overcast": {
      "bias_percent": 0.007522035483715404,
      "rms_normalized_error_percent": 0.17708452950006423,
      "absolute_error": {
        "p95": 0.009866067022085182,
        "p99": 0.021793880462646416,
        "maximum": 0.03418731689453125
      },
      "worst_index": [
        67
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.9366346001625061,
      "reference_fraction_of_uniform": 0.7298845648765564,
      "rms_normalized_to_uniform_percent": 0.13714176668287464
    },
    "horizon": {
      "bias_percent": 1.9924989695724593,
      "rms_normalized_error_percent": 2.8429411259182684,
      "absolute_error": {
        "p95": 0.011547511683454758,
        "p99": 0.025335524737251192,
        "maximum": 0.03435849168217575
      },
      "worst_index": [
        72
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.10594490950483448,
      "reference_fraction_of_uniform": 0.08255893269828489,
      "rms_normalized_to_uniform_percent": 0.15721653578022687
    },
    "north": {
      "bias_percent": -97.53769648253193,
      "rms_normalized_error_percent": 99.78006096733759,
      "absolute_error": {
        "p95": 4.265515156021122e-05,
        "p99": 0.00016615086176898308,
        "maximum": 0.00020605220925062895
      },
      "worst_index": [
        27
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 9.169376426143572e-06,
      "reference_fraction_of_uniform": 7.145354629756184e-06,
      "rms_normalized_to_uniform_percent": 0.000796826127468257
    },
    "east": {
      "bias_percent": 0.4472614982500477,
      "rms_normalized_error_percent": 0.4894380090651343,
      "absolute_error": {
        "p95": 0.008595743775367723,
        "p99": 0.014932500422000877,
        "maximum": 0.016487836837768555
      },
      "worst_index": [
        67
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3134949803352356,
      "reference_fraction_of_uniform": 0.24429498612880707,
      "rms_normalized_to_uniform_percent": 0.10573172903067293
    },
    "south": {
      "bias_percent": 0.20724134307714198,
      "rms_normalized_error_percent": 0.41044214907426213,
      "absolute_error": {
        "p95": 0.0119308829307556,
        "p99": 0.03265498936176277,
        "maximum": 0.0761404037475586
      },
      "worst_index": [
        67
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.737174928188324,
      "reference_fraction_of_uniform": 0.5744530558586121,
      "rms_normalized_to_uniform_percent": 0.24468974035102284
    },
    "west": {
      "bias_percent": -0.4959660405995198,
      "rms_normalized_error_percent": 0.4502802624591488,
      "absolute_error": {
        "p95": 0.007104689627885818,
        "p99": 0.012951382994651789,
        "maximum": 0.014119446277618408
      },
      "worst_index": [
        68
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.1703772395849228,
      "reference_fraction_of_uniform": 0.1327686607837677,
      "rms_normalized_to_uniform_percent": 0.07680785773351566
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
        "identifier": "plan_i_offset_high_grid",
        "sensor_count": 74,
        "illuminance": {
          "nmbe_percent": 0.013397902281840356,
          "cvrmse_percent": 6.8925925948482805,
          "absolute_error_percentiles_lux": {
            "p50": 0.1319270133972168,
            "p90": 4.730637359619153,
            "p95": 10.07210083007812,
            "p99": 32.09521484375
          },
          "maximum_absolute_error_lux": 215.109375,
          "worst": {
            "sensor_index": 72,
            "position": [
              11.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5245.5,
            "foton_lux": 28287.232421875,
            "radiance_lux": 28502.341796875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.04004813032210303,
            "maximum_error_percentage_points": 0.7716438356164383,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.09446202984784814,
            "maximum_error_percentage_points": 0.5427003118014291,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.12805812661977067,
            "maximum_error_percentage_points": 1.8124657534246609,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.13023880044427938,
            "maximum_error_percentage_points": 1.8090410958904108,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0053572750833024586,
            "maximum_error_percentage_points": 0.11082191780821837,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 6.756756756756757,
          "radiance_percent": 6.756756756756757,
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
      "maximum_error_percentage_points": 0.004997583676690925,
      "metrics": {
        "da": [
          {
            "identifier": "plan_i_offset_high_grid",
            "maximum_error_percentage_points": 0.0046575342465753344,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_i_offset_high_grid",
            "maximum_error_percentage_points": 0.004997583676690925,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_i_offset_high_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_i_offset_high_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_i_offset_high_grid",
            "maximum_error_percentage_points": 0.004520547945205955,
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
      "study_preparation_seconds": 0.3500584780013014,
      "weather_seconds": 0.2507983469986357,
      "metric_reduction_seconds": 2.0471020250006404,
      "write_seconds": 0.03960128000107943,
      "total_seconds": 2.337819259002572,
      "cold_end_to_end_seconds": 2.6878777370038733,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.027183082998817554,
      "engine_upload_seconds": 0.046358619,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.069951913,
      "engine_annual_reduction_seconds": 0.037426002,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.069951913
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3500584780013014,
      "weather_seconds": 0.25733433999994304,
      "metric_reduction_seconds": 1.951870158998645,
      "write_seconds": 0.02405028200155357,
      "total_seconds": 2.2336182369981543,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 2.2336182369981543,
      "raw_export_seconds": 0.01085470700127189,
      "engine_upload_seconds": 0.053026497,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.3e-08,
      "engine_annual_reduction_seconds": 0.037690826,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02249057399967569,
      "full": 0.10174657900279271
    }
  },
  "elapsed_seconds": 8.049826091999421,
  "result_class": "passed"
}
```
