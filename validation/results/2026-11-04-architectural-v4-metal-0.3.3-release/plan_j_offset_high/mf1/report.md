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
  "model_sha256": "14d5fb689c1144e0f38a14cc3ae3674bad5f223fe019d5c5b38c72d380fed3e7",
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
      "scene_fingerprint": 4509496220527033930,
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
      "scene_fingerprint": 4509496220527033930,
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
    "/Users/ssanjay/GitHub/foton-0.3.3/validation/results/2026-11-04-architectural-v4-metal-0.3.3-release/plan_j_offset_high/mf1/oracle/scene.rad"
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
            "nmbe_percent": -0.08332272754528318,
            "cvrmse_percent": 11.841864329070516,
            "rms_normalized_rmse_percent": 1.152403501383847,
            "reference_energy": 1.6212123638360936,
            "candidate_energy": 1.619861525475244,
            "relative_energy_error_percent": 0.08332272754528318,
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
            "nmbe_percent": -1.736832216540871,
            "cvrmse_percent": 46.49120798184102,
            "rms_normalized_rmse_percent": 2.808231151846053,
            "reference_energy": 1.4492083946469858,
            "candidate_energy": 1.4240380763639422,
            "relative_energy_error_percent": 1.7368322165408707,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.1069228378346452e-07,
              "p90": 1.77074452949455e-05,
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
            "nmbe_percent": -0.8637629409786757,
            "cvrmse_percent": 21.578596649587745,
            "rms_normalized_rmse_percent": 2.7615459363539907,
            "reference_energy": 3.0704207584830794,
            "candidate_energy": 3.043899601839186,
            "relative_energy_error_percent": 0.8637629409786757,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.1069228378346452e-07,
              "p90": 1.7700111129670404e-05,
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
            "nmbe_percent": -0.08332272754528318,
            "cvrmse_percent": 11.841864329070516,
            "rms_normalized_rmse_percent": 1.152403501383847,
            "reference_energy": 1.6212123638360936,
            "candidate_energy": 1.619861525475244,
            "relative_energy_error_percent": 0.08332272754528318,
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
            "nmbe_percent": 71.56827859428864,
            "cvrmse_percent": 499.28543857233416,
            "rms_normalized_rmse_percent": 19.809565711228654,
            "reference_energy": 0.8300124522035901,
            "candidate_energy": 1.4240380763639422,
            "relative_energy_error_percent": 71.56827859428863,
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
            "nmbe_percent": 24.17872003911319,
            "cvrmse_percent": 168.9400164506487,
            "rms_normalized_rmse_percent": 19.795073710483784,
            "reference_energy": 2.4512248160396837,
            "candidate_energy": 3.043899601839186,
            "relative_energy_error_percent": 24.178720039113195,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.9710000641644e-05,
              "p95": 0.0001102609730878612,
              "p99": 0.00027748249704018235,
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
      "bias_percent": 0.11114201789091317,
      "rms_normalized_error_percent": 0.5258150765473621,
      "absolute_error": {
        "p95": 0.05308074387138899,
        "p99": 0.06633941447409786,
        "maximum": 0.07714356788059717
      },
      "worst_index": [
        45
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.7733958026697714,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.5258150765473621
    },
    "overcast": {
      "bias_percent": 0.08734540318776628,
      "rms_normalized_error_percent": 0.3942390956600515,
      "absolute_error": {
        "p95": 0.03263862133026123,
        "p99": 0.03969727516174316,
        "maximum": 0.042327880859375
      },
      "worst_index": [
        45
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.9115614891052246,
      "reference_fraction_of_uniform": 0.6892494559288025,
      "rms_normalized_to_uniform_percent": 0.29923315157475694
    },
    "horizon": {
      "bias_percent": 0.06655744571848876,
      "rms_normalized_error_percent": 6.204639413172713,
      "absolute_error": {
        "p95": 0.026769232585434104,
        "p99": 0.034504311195403654,
        "maximum": 0.04013105002468964
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.21641106935332566,
      "reference_fraction_of_uniform": 0.07803107985704763,
      "rms_normalized_to_uniform_percent": 0.2844640641690459
    },
    "north": {
      "bias_percent": -22.551887831354694,
      "rms_normalized_error_percent": 164.39564053999086,
      "absolute_error": {
        "p95": 8.750230699661186e-05,
        "p99": 0.00015049914475184773,
        "maximum": 0.00018332858599023893
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.1499375432322267e-05,
      "reference_fraction_of_uniform": 4.1463158595433924e-06,
      "rms_normalized_to_uniform_percent": 0.0007292290969231595
    },
    "east": {
      "bias_percent": 0.6600579459311917,
      "rms_normalized_error_percent": 0.9513957391964591,
      "absolute_error": {
        "p95": 0.021484526991844166,
        "p99": 0.025446860194206236,
        "maximum": 0.026904970407485962
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5763893723487854,
      "reference_fraction_of_uniform": 0.20782802999019623,
      "rms_normalized_to_uniform_percent": 0.2053162320906033
    },
    "south": {
      "bias_percent": 0.08975616543097155,
      "rms_normalized_error_percent": 0.6386031669206952,
      "absolute_error": {
        "p95": 0.04054372310638425,
        "p99": 0.05800248146057128,
        "maximum": 0.06315994262695312
      },
      "worst_index": [
        45
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.8123008012771606,
      "reference_fraction_of_uniform": 0.6534591317176819,
      "rms_normalized_to_uniform_percent": 0.4027208751174854
    },
    "west": {
      "bias_percent": -0.6035193239533279,
      "rms_normalized_error_percent": 1.3178745645210963,
      "absolute_error": {
        "p95": 0.02235165387392044,
        "p99": 0.041762628555297825,
        "maximum": 0.0571446418762207
      },
      "worst_index": [
        45
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3645612895488739,
      "reference_fraction_of_uniform": 0.13144943118095398,
      "rms_normalized_to_uniform_percent": 0.22897964974988239
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
          "nmbe_percent": -0.048712095528542505,
          "cvrmse_percent": 4.55227836834476,
          "absolute_error_percentiles_lux": {
            "p50": 1.1832542419433594,
            "p90": 12.16963043212891,
            "p95": 20.06829299926757,
            "p99": 47.08709228515629
          },
          "maximum_absolute_error_lux": 233.31640625,
          "worst": {
            "sensor_index": 42,
            "position": [
              8.5,
              4.5,
              0.75
            ],
            "hour_of_year": 1116.5,
            "foton_lux": 8804.564453125,
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
            "mean_absolute_error_percentage_points": 0.43204485838903456,
            "maximum_error_percentage_points": 1.997254080394086,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.5570708248324098,
            "maximum_error_percentage_points": 3.584657534246574,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.5534829495773829,
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
      "study_preparation_seconds": 0.0063367499969899654,
      "weather_seconds": 0.07659045793116093,
      "metric_reduction_seconds": 0.04201458301395178,
      "write_seconds": 0.01058745791669935,
      "total_seconds": 0.12930729100480676,
      "cold_end_to_end_seconds": 0.13564404100179672,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0020080000394955277,
      "engine_upload_seconds": 0.000286375,
      "engine_acceleration_structure_seconds": 0.002897583,
      "engine_tracing_seconds": 0.014716541627421975,
      "engine_annual_reduction_seconds": 0.0004928749985992908,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.014716541627421975
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.0063367499969899654,
      "weather_seconds": 0.07343345799017698,
      "metric_reduction_seconds": 0.012947667040862143,
      "write_seconds": 0.010874417028389871,
      "total_seconds": 0.09737054200377315,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.09737054200377315,
      "raw_export_seconds": 0.001866583013907075,
      "engine_upload_seconds": 4.4792e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00046387501060962677,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013861499959602952,
      "full": 0.015946042025461793
    }
  },
  "elapsed_seconds": 0.7128530000336468,
  "result_class": "passed"
}
```
