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
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "f7263bcb09550d25ca0a3ee28648a78e2990ce269e7ccae77e8b5b118d37a29d",
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
      "scene_fingerprint": 6409402939110902228,
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
      "scene_fingerprint": 6409402939110902228,
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
          "maximum": 0.0006659128703176975,
          "p95": 0.0,
          "p99": 2.932638381025754e-06
        },
        "bias_percent": -0.18031469745560588,
        "identifier": "plan_i_offset_high_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.289597941580846,
        "worst_index": [
          72,
          119,
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
          "maximum": 0.00037905387580394745,
          "p95": 7.271089998539537e-06,
          "p99": 3.2133422791957855e-05
        },
        "bias_percent": 0.05964662544213941,
        "identifier": "plan_i_offset_high_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0252499380235267,
        "worst_index": [
          72,
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
          "maximum": 0.0001931833103299141,
          "p95": 6.1348237068159506e-06,
          "p99": 2.9032351449131966e-05
        },
        "bias_percent": 0.03851125843722787,
        "identifier": "plan_i_offset_high_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8468914134048595,
        "worst_index": [
          72,
          98,
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
            "identifier": "plan_i_offset_high_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003953399136662483,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.715045750141144e-06
                },
                "candidate_energy": 1.1235875731485976,
                "cvrmse_percent": 40.81204755424,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.049240747749518234,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1230345825226777,
                "relative_energy_error_percent": 0.049240747749518234,
                "rms_normalized_rmse_percent": 2.4703378114275516,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.01503336988389492,
                  "global_sensor_index": 72,
                  "local_sensor_index": 72,
                  "reference": 0.015428709797561169,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009050215594470501,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.0342730092816055e-05,
                  "p99": 8.120588609017432e-05
                },
                "candidate_energy": 0.6322700869165487,
                "cvrmse_percent": 126.12058181138208,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1107305726322945,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6315707450140167,
                "relative_energy_error_percent": 0.11073057263229448,
                "rms_normalized_rmse_percent": 3.3544153606178733,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0004738220013678074,
                  "global_sensor_index": 72,
                  "local_sensor_index": 72,
                  "reference": 0.0004311995580792427,
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 158.5843750508502,
            "full": 396.8380839796737
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.01854197867215,
            "full": 386.55979093164206
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.64249992650002,
            "full": 406.38850000686944
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.37412490788847,
            "full": 383.4789580432698
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
            "identifier": "plan_i_offset_high_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00024524983018636703,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.928173100575805e-06
                },
                "candidate_energy": 1.1230084537642142,
                "cvrmse_percent": 21.57751731020885,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.11569126368856435,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1217107324429207,
                "relative_energy_error_percent": 0.11569126368856433,
                "rms_normalized_rmse_percent": 1.3063280607202041,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.015098805073648691,
                  "global_sensor_index": 72,
                  "local_sensor_index": 72,
                  "reference": 0.015344054903835058,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003444547764956951,
                  "p50": 0.0,
                  "p90": 4.170121883362299e-06,
                  "p95": 1.0185076007473981e-05,
                  "p99": 5.245333886705339e-05
                },
                "candidate_energy": 1.1479931532318624,
                "cvrmse_percent": 40.67173974262275,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1948384717102865,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1457607704572474,
                "relative_energy_error_percent": 0.19483847171028654,
                "rms_normalized_rmse_percent": 1.6528717357321148,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00027849990874528885,
                  "global_sensor_index": 62,
                  "local_sensor_index": 62,
                  "reference": -6.595486775040627e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 70
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 206.30254200659692,
            "full": 5156.998582999222
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 198.714290978387,
            "full": 5276.639625080861
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 196.89116696827114,
            "full": 5262.243374949321
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 202.60312501341105,
            "full": 5293.240417027846
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
            "identifier": "plan_i_offset_high_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00038569746538996696,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.0524963727220893e-06
                },
                "candidate_energy": 1.122246267412379,
                "cvrmse_percent": 24.82599706736234,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.06112755536422055,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1215606847838444,
                "relative_energy_error_percent": 0.06112755536422055,
                "rms_normalized_rmse_percent": 1.5023563127130461,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.008678138721734285,
                  "global_sensor_index": 72,
                  "local_sensor_index": 72,
                  "reference": 0.009063836187124252,
                  "rgb_channel": 0,
                  "sky_patch_index": 74
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00035857781767845154,
                  "p50": 0.0,
                  "p90": 4.579445430863416e-06,
                  "p95": 1.054262975230813e-05,
                  "p99": 5.223031621426344e-05
                },
                "candidate_energy": 1.1509490127408384,
                "cvrmse_percent": 38.308805576849736,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.3946910831988027,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.146424178731749,
                "relative_energy_error_percent": 0.3946910831988027,
                "rms_normalized_rmse_percent": 1.5572187266267756,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0002933540381491184,
                  "global_sensor_index": 67,
                  "local_sensor_index": 67,
                  "reference": -6.522377952933311e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 72
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 217.90037490427494,
            "full": 5626.449708011933
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 208.18366704043,
            "full": 5623.250207980163
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 207.14254199992865,
            "full": 5767.9730410454795
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 207.14633399620652,
            "full": 5662.799083045684
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
            "identifier": "plan_i_offset_high_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002457038499414921,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.0396565762202954e-06
                },
                "candidate_energy": 1.1228240324103353,
                "cvrmse_percent": 15.282755475481759,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.03830631780797346,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.12325430977603,
                "relative_energy_error_percent": 0.03830631780797345,
                "rms_normalized_rmse_percent": 0.9258073784101297,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.010229209903627634,
                  "global_sensor_index": 68,
                  "local_sensor_index": 68,
                  "reference": 0.009983506053686142,
                  "rgb_channel": 0,
                  "sky_patch_index": 116
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000317474827170372,
                  "p50": 0.0,
                  "p90": 3.19364062306704e-06,
                  "p95": 7.333175744861364e-06,
                  "p99": 3.471071249805391e-05
                },
                "candidate_energy": 1.1473809997955158,
                "cvrmse_percent": 26.852156875459585,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.1817105180583887,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.149469707155312,
                "relative_energy_error_percent": 0.18171051805838864,
                "rms_normalized_rmse_percent": 1.0934739135757876,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.029958264902234077,
                  "global_sensor_index": 73,
                  "local_sensor_index": 73,
                  "reference": 0.029640790075063705,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 318.84016597177833,
            "full": 9865.063249948435
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 314.6102500613779,
            "full": 10169.098041951656
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 308.90325002837926,
            "full": 10005.875666975044
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 307.95670906081796,
            "full": 9978.239958989434
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
    "/content/suite-vulkan-0.3.3/plan_i_offset_high/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 3110.081958002411,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_high/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 11585.951791028492,
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
        "identifier": "plan_i_offset_high_grid",
        "full_identifier": "plan_i_offset_high_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": -0.015665813617560444,
            "cvrmse_percent": 19.7429935989164,
            "rms_normalized_rmse_percent": 1.196859824505401,
            "reference_energy": 1.1239262149721299,
            "candidate_energy": 1.1237501427860934,
            "relative_energy_error_percent": 0.015665813617560444,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.5009272829047404e-06,
              "maximum": 0.0003807060420513153
            },
            "worst": {
              "global_sensor_index": 72,
              "local_sensor_index": 72,
              "sky_patch_index": 119,
              "rgb_channel": 0,
              "reference": 0.006609765347093344,
              "candidate": 0.006229059305042028,
              "position": [
                11.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.64507294549482,
            "cvrmse_percent": 51.46147705742791,
            "rms_normalized_rmse_percent": 2.0906976626089224,
            "reference_energy": 1.1475383017978888,
            "candidate_energy": 1.1401358426738,
            "relative_energy_error_percent": 0.64507294549482,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.998154615052044e-06,
              "p95": 1.7272936020162888e-05,
              "p99": 5.636624700855464e-05,
              "maximum": 0.0006758514791727066
            },
            "worst": {
              "global_sensor_index": 63,
              "local_sensor_index": 63,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.019257551059126854,
              "candidate": 0.018581699579954147,
              "position": [
                9.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.33364075265863485,
            "cvrmse_percent": 24.940880143344167,
            "rms_normalized_rmse_percent": 2.005670231408023,
            "reference_energy": 2.2714645167700187,
            "candidate_energy": 2.2638859854598934,
            "relative_energy_error_percent": 0.33364075265863485,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.930631909403019e-06,
              "p95": 1.72489344549831e-05,
              "p99": 5.550324567593634e-05,
              "maximum": 0.0006758514791727066
            },
            "worst": {
              "global_sensor_index": 63,
              "local_sensor_index": 63,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.019257551059126854,
              "candidate": 0.018581699579954147,
              "position": [
                9.5,
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
        "identifier": "plan_i_offset_high_grid",
        "full_identifier": "plan_i_offset_high_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": -0.015665813617560444,
            "cvrmse_percent": 19.7429935989164,
            "rms_normalized_rmse_percent": 1.196859824505401,
            "reference_energy": 1.1239262149721299,
            "candidate_energy": 1.1237501427860934,
            "relative_energy_error_percent": 0.015665813617560444,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.5009272829047404e-06,
              "maximum": 0.0003807060420513153
            },
            "worst": {
              "global_sensor_index": 72,
              "local_sensor_index": 72,
              "sky_patch_index": 119,
              "rgb_channel": 0,
              "reference": 0.006609765347093344,
              "candidate": 0.006229059305042028,
              "position": [
                11.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 80.59975947976776,
            "cvrmse_percent": 972.9715582135987,
            "rms_normalized_rmse_percent": 25.89199065304104,
            "reference_energy": 0.631305294070188,
            "candidate_energy": 1.1401358426738,
            "relative_energy_error_percent": 80.59975947976774,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.0389999917824753e-05,
              "p95": 5.660182796418667e-05,
              "p99": 0.00020845411927439272,
              "maximum": 0.00800633430480957
            },
            "worst": {
              "global_sensor_index": 72,
              "local_sensor_index": 72,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01910039596259594,
              "candidate": 0.02710673026740551,
              "position": [
                11.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 28.97933826946312,
            "cvrmse_percent": 349.9097836223047,
            "rms_normalized_rmse_percent": 25.889064487696682,
            "reference_energy": 1.7552315090423178,
            "candidate_energy": 2.2638859854598934,
            "relative_energy_error_percent": 28.979338269463128,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.0218620193190873e-05,
              "p95": 5.616999987978488e-05,
              "p99": 0.00020845411927439272,
              "maximum": 0.00800633430480957
            },
            "worst": {
              "global_sensor_index": 72,
              "local_sensor_index": 72,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01910039596259594,
              "candidate": 0.02710673026740551,
              "position": [
                11.5,
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
      "bias_percent": 0.39907970275259186,
      "rms_normalized_error_percent": 0.6383501804233976,
      "absolute_error": {
        "p95": 0.05283571892851308,
        "p99": 0.11062939376398022,
        "maximum": 0.11504474668751641
      },
      "worst_index": [
        73
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.283116646151937,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.6383501804233976
    },
    "overcast": {
      "bias_percent": 0.3190608390060368,
      "rms_normalized_error_percent": 0.5105721298857337,
      "absolute_error": {
        "p95": 0.03424856662750234,
        "p99": 0.0664388465881347,
        "maximum": 0.077392578125
      },
      "worst_index": [
        73
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.9286069869995117,
      "reference_fraction_of_uniform": 0.7237120270729065,
      "rms_normalized_to_uniform_percent": 0.391868593516438
    },
    "horizon": {
      "bias_percent": 2.232809387007007,
      "rms_normalized_error_percent": 6.6562996954149805,
      "absolute_error": {
        "p95": 0.022106057319171514,
        "p99": 0.04440778641402689,
        "maximum": 0.06193236175818273
      },
      "worst_index": [
        72
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.07889387072251076,
      "reference_fraction_of_uniform": 0.06148612517740554,
      "rms_normalized_to_uniform_percent": 0.2729883676905071
    },
    "north": {
      "bias_percent": -81.10891725770702,
      "rms_normalized_error_percent": 114.09063080961951,
      "absolute_error": {
        "p95": 0.00010534076391195393,
        "p99": 0.00021924346011473954,
        "maximum": 0.0002538150001782924
      },
      "worst_index": [
        55
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.558527219458483e-05,
      "reference_fraction_of_uniform": 1.2146418157499284e-05,
      "rms_normalized_to_uniform_percent": 0.0012199451751688344
    },
    "east": {
      "bias_percent": 0.35000480105192877,
      "rms_normalized_error_percent": 0.7682649330350312,
      "absolute_error": {
        "p95": 0.015853523835539816,
        "p99": 0.022673500180244437,
        "maximum": 0.024471521377563477
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3314265310764313,
      "reference_fraction_of_uniform": 0.25829803943634033,
      "rms_normalized_to_uniform_percent": 0.17452955320474198
    },
    "south": {
      "bias_percent": 0.502880144450891,
      "rms_normalized_error_percent": 0.7329517481638896,
      "absolute_error": {
        "p95": 0.04797232747077942,
        "p99": 0.07409740447998042,
        "maximum": 0.08279132843017578
      },
      "worst_index": [
        72
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.7374936938285828,
      "reference_fraction_of_uniform": 0.5747674107551575,
      "rms_normalized_to_uniform_percent": 0.4392693730768475
    },
    "west": {
      "bias_percent": 0.21225746382822736,
      "rms_normalized_error_percent": 1.1048544804855054,
      "absolute_error": {
        "p95": 0.015259630978107426,
        "p99": 0.03247160106897347,
        "maximum": 0.04619550704956055
      },
      "worst_index": [
        73
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.17418140172958374,
      "reference_fraction_of_uniform": 0.13574868440628052,
      "rms_normalized_to_uniform_percent": 0.19207115990619403
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
          "nmbe_percent": 0.14848731978178437,
          "cvrmse_percent": 7.45315154991954,
          "absolute_error_percentiles_lux": {
            "p50": 0.20261549949645996,
            "p90": 5.848812103271488,
            "p95": 11.753464508056627,
            "p99": 36.18303710937499
          },
          "maximum_absolute_error_lux": 224.35302734375,
          "worst": {
            "sensor_index": 72,
            "position": [
              11.5,
              1.5,
              0.75
            ],
            "hour_of_year": 4451.5,
            "foton_lux": 4906.81396484375,
            "radiance_lux": 4682.4609375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.06695298037763804,
            "maximum_error_percentage_points": 1.4265753424657532,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.16245788036920555,
            "maximum_error_percentage_points": 0.9381732356317265,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.21508515364679726,
            "maximum_error_percentage_points": 3.7309589041095848,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.21358015549796427,
            "maximum_error_percentage_points": 3.730958904109589,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.008143280266567961,
            "maximum_error_percentage_points": 0.21602739726027487,
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
      "maximum_error_percentage_points": 0.004934216852057471,
      "metrics": {
        "da": [
          {
            "identifier": "plan_i_offset_high_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_i_offset_high_grid",
            "maximum_error_percentage_points": 0.004934216852057471,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_i_offset_high_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
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
            "maximum_error_percentage_points": 0.004246575342465642,
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
      "study_preparation_seconds": 0.3782930390000274,
      "weather_seconds": 0.2250193020001916,
      "metric_reduction_seconds": 0.26360146899992287,
      "write_seconds": 0.012768801999982315,
      "total_seconds": 0.5017126760001247,
      "cold_end_to_end_seconds": 0.8800057150001521,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0022139590000733733,
      "engine_upload_seconds": 0.013848909,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.020492135,
      "engine_annual_reduction_seconds": 0.016205998000000003,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.020492135
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3782930390000274,
      "weather_seconds": 0.22751368800004457,
      "metric_reduction_seconds": 0.2420732670000234,
      "write_seconds": 0.012919704999831083,
      "total_seconds": 0.48276988599991455,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.48276988599991455,
      "raw_export_seconds": 0.0023869169999670703,
      "engine_upload_seconds": 0.01383751,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 1.32e-07,
      "engine_annual_reduction_seconds": 0.016592311,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.014622815999928207,
      "full": 0.030957916000033947
    }
  },
  "elapsed_seconds": 3.1583962909999173,
  "result_class": "passed"
}
```
