# Foton report

Status: **passed**

```json
{
  "scene": "plan_j_offset_high",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_j_offset_high",
    "category": "form",
    "question": "How does a offset high opening illuminate a J-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "j",
    "window_profile": "offset_high"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 47,
    "floor_area": 63.0,
    "aperture_area": 1.4399999999999988
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "6207839f9f82470b121056bc024482d03b9080e0503ac18090fced61a5ba387b",
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
      "scene_fingerprint": 4509496220527033930,
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
      "scene_fingerprint": 4509496220527033930,
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
    "model_sha256": "791bdcd857c7f3bd3aebf9cd2cb2ca8a301fb7c700c4a5b3fa8987eaef21ebd8",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "23633e9e91bc013f4a3a6d776a0b95fe8d48adfbd13e89c51c834683d9ee6bfe",
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
          "p99": 5.681905895471573e-05
        },
        "bias_percent": -0.008361844674369533,
        "identifier": "plan_j_offset_high_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.225288390834748,
        "worst_index": [
          45,
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
          "maximum": 0.00049634650349617,
          "p95": 1.601697294972837e-05,
          "p99": 6.592459976673126e-05
        },
        "bias_percent": 0.05317885129432206,
        "identifier": "plan_j_offset_high_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3258173956154964,
        "worst_index": [
          34,
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
          "maximum": 0.0002076420933008194,
          "p95": 1.3956858310848475e-05,
          "p99": 5.304533988237381e-05
        },
        "bias_percent": -0.15809312255624863,
        "identifier": "plan_j_offset_high_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9647611455199184,
        "worst_index": [
          33,
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
            "identifier": "plan_j_offset_high_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007199281826615334,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00018148746312363073
                },
                "candidate_energy": 1.6172240940522897,
                "cvrmse_percent": 44.20313061765461,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.5549461179216524,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.6262488991860664,
                "relative_energy_error_percent": 0.5549461179216524,
                "rms_normalized_rmse_percent": 4.305612907134543,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00414624996483326,
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "reference": 0.004866178147494793,
                  "rgb_channel": 0,
                  "sky_patch_index": 71
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009940355084836483,
                  "p50": 0.0,
                  "p90": 1.0643449968483765e-05,
                  "p95": 2.945401138276793e-05,
                  "p99": 0.0002280152402818203
                },
                "candidate_energy": 0.833014938341023,
                "cvrmse_percent": 121.51231068019602,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.8539430592506021,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.8259616957679441,
                "relative_energy_error_percent": 0.8539430592506021,
                "rms_normalized_rmse_percent": 4.778417188322922,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0006350204348564148,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": -0.0003590150736272335,
                  "rgb_channel": 0,
                  "sky_patch_index": 71
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.66266709007323,
            "full": 282.4939169222489
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 119.82954200357199,
            "full": 277.258540969342
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 119.4332919549197,
            "full": 279.8029159894213
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.34629203844815,
            "full": 275.3507500747219
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
            "identifier": "plan_j_offset_high_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003421446308493614,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.852042861282825e-05
                },
                "candidate_energy": 1.6206773960277587,
                "cvrmse_percent": 19.088556201078116,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.1928864387406874,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.617557347266029,
                "relative_energy_error_percent": 0.19288643874068737,
                "rms_normalized_rmse_percent": 1.8573247163499804,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0051988475024700165,
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "reference": 0.004856702871620655,
                  "rgb_channel": 0,
                  "sky_patch_index": 72
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005023898556828499,
                  "p50": 6.016439257905404e-08,
                  "p90": 1.2102582331863232e-05,
                  "p95": 2.4439708795398474e-05,
                  "p99": 0.00011009280569851398
                },
                "candidate_energy": 1.4496379006128883,
                "cvrmse_percent": 34.28102665200676,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.6705070171829746,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.459423437169523,
                "relative_energy_error_percent": 0.6705070171829746,
                "rms_normalized_rmse_percent": 2.0776526601472707,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.011092345230281353,
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "reference": 0.011594735085964203,
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 159.98112491797656,
            "full": 3101.1729170568287
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 164.57704198546708,
            "full": 3106.8027920555323
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.62616600841284,
            "full": 3071.306874975562
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.65654204692692,
            "full": 3050.7802499923855
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
            "identifier": "plan_j_offset_high_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00036615412682294846,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.984204082982615e-05
                },
                "candidate_energy": 1.6164309717264587,
                "cvrmse_percent": 19.740414232029167,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.2990969636367898,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.6212801714914349,
                "relative_energy_error_percent": 0.2990969636367898,
                "rms_normalized_rmse_percent": 1.9222984914791779,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004993967479094863,
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "reference": 0.005360121605917811,
                  "rgb_channel": 0,
                  "sky_patch_index": 72
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006531288381665945,
                  "p50": 5.430801763850468e-08,
                  "p90": 1.0720705176936463e-05,
                  "p95": 2.211337414337322e-05,
                  "p99": 0.00011828821152448654
                },
                "candidate_energy": 1.4636359374796548,
                "cvrmse_percent": 38.63341414914206,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.9948732679570147,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.4492180544614115,
                "relative_energy_error_percent": 0.9948732679570148,
                "rms_normalized_rmse_percent": 2.3350134091556156,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.007080188486725092,
                  "global_sensor_index": 30,
                  "local_sensor_index": 30,
                  "reference": 0.0077333173248916864,
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 163.85241702664644,
            "full": 3309.362209052779
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 159.36879196669906,
            "full": 3290.5334999086335
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.04120802506804,
            "full": 3248.88354097493
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 166.90675006248057,
            "full": 3329.248541034758
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
            "identifier": "plan_j_offset_high_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00012847647303715348,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.145968705415726e-05
                },
                "candidate_energy": 1.6185072523021518,
                "cvrmse_percent": 10.25835881323385,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.069142393358687,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.6173889508716002,
                "relative_energy_error_percent": 0.069142393358687,
                "rms_normalized_rmse_percent": 0.9969248545212162,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001189975009765476,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.0013184514828026295,
                  "rgb_channel": 0,
                  "sky_patch_index": 45
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00030834879726171494,
                  "p50": 5.6330458519937565e-08,
                  "p90": 8.362994776689447e-06,
                  "p95": 1.699965650914237e-05,
                  "p99": 7.515450124628842e-05
                },
                "candidate_energy": 1.4531252554362482,
                "cvrmse_percent": 22.419784030114084,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.0898991789401394,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.451820081103648,
                "relative_energy_error_percent": 0.08989917894013938,
                "rms_normalized_rmse_percent": 1.3558395677332362,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0009288790170103312,
                  "global_sensor_index": 44,
                  "local_sensor_index": 44,
                  "reference": 0.0006205302197486162,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 236.59387498628348,
            "full": 5776.984750060365
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 228.57729194220155,
            "full": 5751.082208007574
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 229.1280839126557,
            "full": 5778.910625027493
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 230.44779198244214,
            "full": 5736.680250032805
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
    "/content/suite-vulkan-0.3.3/plan_j_offset_high/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1309.4630419509485,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4713.977874955162,
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
      47,
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
        "identifier": "plan_j_offset_high_grid",
        "full_identifier": "plan_j_offset_high_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": -0.08332383596246025,
            "cvrmse_percent": 11.841861994851172,
            "rms_normalized_rmse_percent": 1.1524032742268329,
            "reference_energy": 1.6212123638360936,
            "candidate_energy": 1.6198615075054477,
            "relative_energy_error_percent": 0.08332383596246025,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.08914459310472e-05,
              "maximum": 0.0003807060420513153
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 45,
              "sky_patch_index": 119,
              "rgb_channel": 0,
              "reference": 0.006609765347093344,
              "candidate": 0.006229059305042028,
              "position": [
                8.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.7408689454771622,
            "cvrmse_percent": 46.50067011807438,
            "rms_normalized_rmse_percent": 2.8088026978842615,
            "reference_energy": 1.4492083946469858,
            "candidate_energy": 1.4239795757493283,
            "relative_energy_error_percent": 1.740868945477162,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.1069228378346452e-07,
              "p90": 1.7724305507726967e-05,
              "p95": 3.081774048041552e-05,
              "p99": 9.177470928989351e-05,
              "maximum": 0.001013355329632759
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 45,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.024006765335798264,
              "candidate": 0.022993410006165504,
              "position": [
                8.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.8656688225829644,
            "cvrmse_percent": 21.58313795516348,
            "rms_normalized_rmse_percent": 2.762127115202739,
            "reference_energy": 3.0704207584830794,
            "candidate_energy": 3.043841083254776,
            "relative_energy_error_percent": 0.8656688225829645,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.1069228378346452e-07,
              "p90": 1.77074452949455e-05,
              "p95": 3.0239636544138193e-05,
              "p99": 8.848411380313337e-05,
              "maximum": 0.001013355329632759
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 45,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.024006765335798264,
              "candidate": 0.022993410006165504,
              "position": [
                8.5,
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
      47,
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
        "identifier": "plan_j_offset_high_grid",
        "full_identifier": "plan_j_offset_high_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": -0.08332383596246025,
            "cvrmse_percent": 11.841861994851172,
            "rms_normalized_rmse_percent": 1.1524032742268329,
            "reference_energy": 1.6212123638360936,
            "candidate_energy": 1.6198615075054477,
            "relative_energy_error_percent": 0.08332383596246025,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.08914459310472e-05,
              "maximum": 0.0003807060420513153
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 45,
              "sky_patch_index": 119,
              "rgb_channel": 0,
              "reference": 0.006609765347093344,
              "candidate": 0.006229059305042028,
              "position": [
                8.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 71.5612304332088,
            "cvrmse_percent": 499.27750505902725,
            "rms_normalized_rmse_percent": 19.809250942479093,
            "reference_energy": 0.8300124522035901,
            "candidate_energy": 1.4239795757493283,
            "relative_energy_error_percent": 71.5612304332088,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.9130001318408176e-05,
              "p95": 0.00010950417345156893,
              "p99": 0.00028927624225616455,
              "maximum": 0.0060012489557266235
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 46,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.020604681223630905,
              "candidate": 0.02660593017935753,
              "position": [
                8.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 24.17633271894463,
            "cvrmse_percent": 168.93732716323623,
            "rms_normalized_rmse_percent": 19.794758600756218,
            "reference_energy": 2.4512248160396837,
            "candidate_energy": 3.043841083254776,
            "relative_energy_error_percent": 24.17633271894463,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.9710000641644e-05,
              "p95": 0.0001102609730878612,
              "p99": 0.00027748243883252144,
              "maximum": 0.0060012489557266235
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 46,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.020604681223630905,
              "candidate": 0.02660593017935753,
              "position": [
                8.5,
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
      "bias_percent": 0.10949470570033344,
      "rms_normalized_error_percent": 0.5253404534045818,
      "absolute_error": {
        "p95": 0.05308062092516637,
        "p99": 0.06633971152467354,
        "maximum": 0.07714413572543677
      },
      "worst_index": [
        45
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.7733958026697714,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.5253404534045818
    },
    "overcast": {
      "bias_percent": 0.08587928334094842,
      "rms_normalized_error_percent": 0.39372589982302564,
      "absolute_error": {
        "p95": 0.032638478279113765,
        "p99": 0.039698359966278074,
        "maximum": 0.04232978820800781
      },
      "worst_index": [
        45
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.9115614891052246,
      "reference_fraction_of_uniform": 0.6892494559288025,
      "rms_normalized_to_uniform_percent": 0.29884365590402595
    },
    "horizon": {
      "bias_percent": 0.06655705837947164,
      "rms_normalized_error_percent": 6.204639114032835,
      "absolute_error": {
        "p95": 0.026769232585434104,
        "p99": 0.034504299942698526,
        "maximum": 0.04013102918634681
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.21641106935332566,
      "reference_fraction_of_uniform": 0.07803107985704763,
      "rms_normalized_to_uniform_percent": 0.2844640504543818
    },
    "north": {
      "bias_percent": -22.551886191889608,
      "rms_normalized_error_percent": 164.39564766966774,
      "absolute_error": {
        "p95": 8.750230699661186e-05,
        "p99": 0.00015049915202780534,
        "maximum": 0.00018332859326619655
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.1499375432322267e-05,
      "reference_fraction_of_uniform": 4.1463158595433924e-06,
      "rms_normalized_to_uniform_percent": 0.0007292291655876356
    },
    "east": {
      "bias_percent": 0.6539314462164841,
      "rms_normalized_error_percent": 0.9483886026948984,
      "absolute_error": {
        "p95": 0.021484509110450734,
        "p99": 0.025446871519088744,
        "maximum": 0.026904940605163574
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5763893723487854,
      "reference_fraction_of_uniform": 0.20782802999019623,
      "rms_normalized_to_uniform_percent": 0.20466726599855
    },
    "south": {
      "bias_percent": 0.08855222034725566,
      "rms_normalized_error_percent": 0.6383056781862211,
      "absolute_error": {
        "p95": 0.04054372310638425,
        "p99": 0.05800299644470214,
        "maximum": 0.06316089630126953
      },
      "worst_index": [
        45
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.8123008012771606,
      "reference_fraction_of_uniform": 0.6534591317176819,
      "rms_normalized_to_uniform_percent": 0.40253328157122487
    },
    "west": {
      "bias_percent": -0.6035241412945752,
      "rms_normalized_error_percent": 1.317873493192622,
      "absolute_error": {
        "p95": 0.02235167324542999,
        "p99": 0.0417625272274017,
        "maximum": 0.0571444034576416
      },
      "worst_index": [
        45
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3645612895488739,
      "reference_fraction_of_uniform": 0.13144943118095398,
      "rms_normalized_to_uniform_percent": 0.22897945639071737
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
        "identifier": "plan_j_offset_high_grid",
        "sensor_count": 47,
        "illuminance": {
          "nmbe_percent": -0.05077842096984584,
          "cvrmse_percent": 4.551178810919429,
          "absolute_error_percentiles_lux": {
            "p50": 1.1832027435302734,
            "p90": 12.171036148071291,
            "p95": 20.04587249755851,
            "p99": 47.00926147460938
          },
          "maximum_absolute_error_lux": 233.3154296875,
          "worst": {
            "sensor_index": 42,
            "position": [
              8.5,
              4.5,
              0.75
            ],
            "hour_of_year": 1116.5,
            "foton_lux": 8804.5654296875,
            "radiance_lux": 9037.880859375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2036374234916927,
            "maximum_error_percentage_points": 1.8678082191780874,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.4303427307294601,
            "maximum_error_percentage_points": 1.997254080394086,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.5547303993004948,
            "maximum_error_percentage_points": 3.584657534246574,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.5511425240454679,
            "maximum_error_percentage_points": 3.584657534246576,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.010897697464296143,
            "maximum_error_percentage_points": 0.1139726027397252,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 12.76595744680851,
          "radiance_percent": 12.76595744680851,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.127659574468085,
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
      "maximum_error_percentage_points": 0.004957994434931834,
      "metrics": {
        "da": [
          {
            "identifier": "plan_j_offset_high_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_j_offset_high_grid",
            "maximum_error_percentage_points": 0.004957994434931834,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_j_offset_high_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_j_offset_high_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_j_offset_high_grid",
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
      "study_preparation_seconds": 0.3579403410001305,
      "weather_seconds": 0.21641445000000203,
      "metric_reduction_seconds": 0.18811030899996695,
      "write_seconds": 0.012692308999930901,
      "total_seconds": 0.4175746899998103,
      "cold_end_to_end_seconds": 0.7755150309999408,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0017383990000325866,
      "engine_upload_seconds": 0.014507147,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.014858601,
      "engine_annual_reduction_seconds": 0.010475345,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.014858601
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3579403410001305,
      "weather_seconds": 0.23013787999980195,
      "metric_reduction_seconds": 0.17111191899994083,
      "write_seconds": 0.014480806999927154,
      "total_seconds": 0.4159884279999915,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.4159884279999915,
      "raw_export_seconds": 0.0018580579999252222,
      "engine_upload_seconds": 0.013897269,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 1.35e-07,
      "engine_annual_reduction_seconds": 0.010567484,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013774101000080918,
      "full": 0.023557922000009057
    }
  },
  "elapsed_seconds": 2.8434099030000652,
  "result_class": "passed"
}
```
