# Foton report

Status: **passed**

```json
{
  "scene": "plan_i_small_center",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_i_small_center",
    "category": "form",
    "question": "How does a small center opening illuminate a I-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "i",
    "window_profile": "small_center"
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
  "model_sha256": "a1738cbaa77f8e1b9329af0ba1c28be13720060ee5a99ba88c8642f4f1b7a1c1",
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
      "scene_fingerprint": 7091735636442897822,
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
      "scene_fingerprint": 7091735636442897822,
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
    "model_sha256": "774f46a962163c7751703394a6151c3f5b5f7c2d58b635ce0fcf1f0bdbd7a391",
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
          "maximum": 0.0004480518400669098,
          "p95": 0.0,
          "p99": 2.3753498680889606e-05
        },
        "bias_percent": 0.03807326023088201,
        "identifier": "plan_i_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.2242998162428593,
        "worst_index": [
          52,
          76,
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
          "maximum": 0.0004177754744887352,
          "p95": 1.0262556315865368e-05,
          "p99": 5.960301496088505e-05
        },
        "bias_percent": 0.11598910159881469,
        "identifier": "plan_i_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.309950265428258,
        "worst_index": [
          57,
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
          "maximum": 0.0002517346292734146,
          "p95": 8.460941899102181e-06,
          "p99": 4.9332622438669205e-05
        },
        "bias_percent": 0.021833251320619692,
        "identifier": "plan_i_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0755730775008159,
        "worst_index": [
          57,
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
            "identifier": "plan_i_small_center_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000539303757250309,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.479728760197759e-05
                },
                "candidate_energy": 2.88523308353615,
                "cvrmse_percent": 28.15663001193639,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.24287153973469286,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.8782426512916572,
                "relative_energy_error_percent": 0.24287153973469286,
                "rms_normalized_rmse_percent": 2.740084565560633,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.018070894293487072,
                  "global_sensor_index": 48,
                  "local_sensor_index": 48,
                  "reference": 0.017531590536236763,
                  "rgb_channel": 0,
                  "sky_patch_index": 119
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009521548636257648,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 5.725714800064452e-06,
                  "p99": 0.00018538511358201504
                },
                "candidate_energy": 0.7148545196466785,
                "cvrmse_percent": 179.46327676244434,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.26570379914316383,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.7167589754752157,
                "relative_energy_error_percent": 0.26570379914316383,
                "rms_normalized_rmse_percent": 3.990806023344676,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.01290410989895463,
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "reference": 0.011951955035328865,
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.5104170339182,
            "full": 399.8824170557782
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.22170796710998,
            "full": 389.3166669877246
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.66833299957216,
            "full": 401.7611249582842
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.92004196997732,
            "full": 405.5166660109535
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
            "identifier": "plan_i_small_center_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00036670209374278784,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.404705345630646e-05
                },
                "candidate_energy": 2.8874653657703675,
                "cvrmse_percent": 17.48440539171495,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.06559048152834873,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.885572704738479,
                "relative_energy_error_percent": 0.06559048152834873,
                "rms_normalized_rmse_percent": 1.7054422481953906,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003738390631042421,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.003371688537299633,
                  "rgb_channel": 0,
                  "sky_patch_index": 72
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004233682993799448,
                  "p50": 0.0,
                  "p90": 6.540661161125172e-06,
                  "p95": 1.4361350622493774e-05,
                  "p99": 0.00010738801211118698
                },
                "candidate_energy": 1.3521019809877508,
                "cvrmse_percent": 57.56821941416165,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1722073432142584,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3497775649039276,
                "relative_energy_error_percent": 0.17220734321425843,
                "rms_normalized_rmse_percent": 2.2555070358525406,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00030781025998294353,
                  "global_sensor_index": 35,
                  "local_sensor_index": 35,
                  "reference": -0.00011555803939700127,
                  "rgb_channel": 0,
                  "sky_patch_index": 45
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 202.85845804028213,
            "full": 5461.321459035389
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 202.67279096879065,
            "full": 5362.443707999773
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 213.74316606670618,
            "full": 5341.89075010363
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 198.6489159753546,
            "full": 5261.580792022869
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
            "identifier": "plan_i_small_center_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005107654724270105,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.968597881495953e-05
                },
                "candidate_energy": 2.8882137872374187,
                "cvrmse_percent": 19.153333284888678,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.04770361581371212,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.88683666176712,
                "relative_energy_error_percent": 0.04770361581371212,
                "rms_normalized_rmse_percent": 1.8674267046563333,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.006475338013842702,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.0069861034862697124,
                  "rgb_channel": 0,
                  "sky_patch_index": 43
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007608854211866856,
                  "p50": 0.0,
                  "p90": 6.862538612040225e-06,
                  "p95": 1.4946945157134905e-05,
                  "p99": 0.0001256334944628179
                },
                "candidate_energy": 1.352316493196419,
                "cvrmse_percent": 63.665572121919766,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.37308422249210593,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3573806663015482,
                "relative_energy_error_percent": 0.37308422249210604,
                "rms_normalized_rmse_percent": 2.5084628648483402,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00047368300147354603,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": -0.00028720241971313953,
                  "rgb_channel": 0,
                  "sky_patch_index": 43
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 199.24187497235835,
            "full": 5902.792125009
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 203.16137501504272,
            "full": 5807.813166989945
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 191.42625003587455,
            "full": 5619.554458069615
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 190.3447089716792,
            "full": 5637.118167011067
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
            "identifier": "plan_i_small_center_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000296745914965868,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.6101817386224866e-05
                },
                "candidate_energy": 2.888024040010805,
                "cvrmse_percent": 11.023654855259984,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.13506962605834535,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.8841284584868845,
                "relative_energy_error_percent": 0.13506962605834535,
                "rms_normalized_rmse_percent": 1.0750904967293893,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.008469503372907639,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.008766249287873507,
                  "rgb_channel": 0,
                  "sky_patch_index": 70
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00036559090949594975,
                  "p50": 0.0,
                  "p90": 4.619754690793343e-06,
                  "p95": 9.911434972309507e-06,
                  "p99": 5.9463316574692726e-05
                },
                "candidate_energy": 1.3564894800815708,
                "cvrmse_percent": 35.64534169784288,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.10815131754712283,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3579581296905694,
                "relative_energy_error_percent": 0.10815131754712283,
                "rms_normalized_rmse_percent": 1.4042377029791386,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00012725242413580418,
                  "global_sensor_index": 48,
                  "local_sensor_index": 48,
                  "reference": 0.00023833848536014557,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 299.510334036313,
            "full": 9944.97970805969
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 299.12037507165223,
            "full": 10028.553750016727
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 313.6614999966696,
            "full": 10125.543124973774
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 303.1811659457162,
            "full": 10154.599583009258
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
    "/content/suite-vulkan-0.3.2/plan_i_small_center/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 3405.3697501076385,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_small_center/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 12794.380167033523,
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
        "identifier": "plan_i_small_center_grid",
        "full_identifier": "plan_i_small_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": -0.01701533165005492,
            "cvrmse_percent": 6.987334212295248,
            "rms_normalized_rmse_percent": 0.6815773718330558,
            "reference_energy": 2.885622123187204,
            "candidate_energy": 2.8851311250127765,
            "relative_energy_error_percent": 0.017015331650054925,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.551362220197916e-05,
              "maximum": 0.0002165650948882103
            },
            "worst": {
              "global_sensor_index": 48,
              "local_sensor_index": 48,
              "sky_patch_index": 121,
              "rgb_channel": 0,
              "reference": 0.006629771552979946,
              "candidate": 0.006413206458091736,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.647643053889849,
            "cvrmse_percent": 49.755377127045584,
            "rms_normalized_rmse_percent": 1.9597682289157168,
            "reference_energy": 1.3576779324825683,
            "candidate_energy": 1.335308246333824,
            "relative_energy_error_percent": 1.647643053889849,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.0990185728587676e-05,
              "p95": 2.025472349487245e-05,
              "p99": 5.9735539252869785e-05,
              "maximum": 0.000800522044301033
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015785671770572662,
              "candidate": 0.01498514972627163,
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
            "nmbe_percent": -0.5387477676160618,
            "cvrmse_percent": 15.82397933895889,
            "rms_normalized_rmse_percent": 1.9479929533188758,
            "reference_energy": 4.243300055669772,
            "candidate_energy": 4.2204393713466,
            "relative_energy_error_percent": 0.5387477676160619,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.0960787676594919e-05,
              "p95": 2.0412509911693633e-05,
              "p99": 5.936413072049618e-05,
              "maximum": 0.000800522044301033
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015785671770572662,
              "candidate": 0.01498514972627163,
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
        "identifier": "plan_i_small_center_grid",
        "full_identifier": "plan_i_small_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": -0.01701533165005492,
            "cvrmse_percent": 6.987334212295248,
            "rms_normalized_rmse_percent": 0.6815773718330558,
            "reference_energy": 2.885622123187204,
            "candidate_energy": 2.8851311250127765,
            "relative_energy_error_percent": 0.017015331650054925,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.551362220197916e-05,
              "maximum": 0.0002165650948882103
            },
            "worst": {
              "global_sensor_index": 48,
              "local_sensor_index": 48,
              "sky_patch_index": 121,
              "rgb_channel": 0,
              "reference": 0.006629771552979946,
              "candidate": 0.006413206458091736,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 87.56371193601953,
            "cvrmse_percent": 607.1048032606482,
            "rms_normalized_rmse_percent": 13.412233978313328,
            "reference_energy": 0.7119224889243583,
            "candidate_energy": 1.335308246333824,
            "relative_energy_error_percent": 87.56371193601953,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.145300113123085e-05,
              "p95": 8.232000254793093e-05,
              "p99": 0.00019192881882190704,
              "maximum": 0.0029371213167905807
            },
            "worst": {
              "global_sensor_index": 53,
              "local_sensor_index": 53,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.008071888238191605,
              "candidate": 0.011009009554982185,
              "position": [
                7.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 17.314441553775,
            "cvrmse_percent": 120.04887102601973,
            "rms_normalized_rmse_percent": 13.40198132819547,
            "reference_energy": 3.5975446121115624,
            "candidate_energy": 4.2204393713466,
            "relative_energy_error_percent": 17.314441553775,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.147000072407536e-05,
              "p95": 8.304999937536195e-05,
              "p99": 0.00018440885469317436,
              "maximum": 0.0029371213167905807
            },
            "worst": {
              "global_sensor_index": 53,
              "local_sensor_index": 53,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.008071888238191605,
              "candidate": 0.011009009554982185,
              "position": [
                7.5,
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
      "bias_percent": -0.009834649707738207,
      "rms_normalized_error_percent": 0.2742724621963996,
      "absolute_error": {
        "p95": 0.050833540635493085,
        "p99": 0.06628611878408637,
        "maximum": 0.07166842032755572
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.6558319860500177,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2742724621963996
    },
    "overcast": {
      "bias_percent": 0.015036546913220521,
      "rms_normalized_error_percent": 0.2143881204981686,
      "absolute_error": {
        "p95": 0.032206279039382904,
        "p99": 0.03910972118377684,
        "maximum": 0.04196023941040039
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.7570551633834839,
      "reference_fraction_of_uniform": 0.661583662033081,
      "rms_normalized_to_uniform_percent": 0.15602785346907444
    },
    "horizon": {
      "bias_percent": -0.3574318445146808,
      "rms_normalized_error_percent": 3.395175036407934,
      "absolute_error": {
        "p95": 0.023257095812400454,
        "p99": 0.0283812992293079,
        "maximum": 0.029817995181959434
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.20989215905458333,
      "reference_fraction_of_uniform": 0.07903066163712903,
      "rms_normalized_to_uniform_percent": 0.12328762624996112
    },
    "north": {
      "bias_percent": -91.82867112200663,
      "rms_normalized_error_percent": 102.32045992975699,
      "absolute_error": {
        "p95": 0.00010130398077308199,
        "p99": 0.0001848935865564261,
        "maximum": 0.0003856565454043448
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.8694261598284356e-05,
      "reference_fraction_of_uniform": 7.038947387627559e-06,
      "rms_normalized_to_uniform_percent": 0.0006651840647881052
    },
    "east": {
      "bias_percent": -0.06182118498957407,
      "rms_normalized_error_percent": 0.31146547770463867,
      "absolute_error": {
        "p95": 0.0163938283920288,
        "p99": 0.01981008291244506,
        "maximum": 0.021378755569458008
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.49523550271987915,
      "reference_fraction_of_uniform": 0.18647094070911407,
      "rms_normalized_to_uniform_percent": 0.07290745904635323
    },
    "south": {
      "bias_percent": -0.027292553447969232,
      "rms_normalized_error_percent": 0.36172518855741576,
      "absolute_error": {
        "p95": 0.044847020506858785,
        "p99": 0.05536512374877927,
        "maximum": 0.06034421920776367
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.804378867149353,
      "reference_fraction_of_uniform": 0.6794024705886841,
      "rms_normalized_to_uniform_percent": 0.2337461583957127
    },
    "west": {
      "bias_percent": -0.11964500463545746,
      "rms_normalized_error_percent": 0.33175787101247556,
      "absolute_error": {
        "p95": 0.01272554881870746,
        "p99": 0.021996842920780163,
        "maximum": 0.025362253189086914
      },
      "worst_index": [
        53
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.48639246821403503,
      "reference_fraction_of_uniform": 0.18314127624034882,
      "rms_normalized_to_uniform_percent": 0.07409847129327052
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
        "identifier": "plan_i_small_center_grid",
        "sensor_count": 74,
        "illuminance": {
          "nmbe_percent": -0.11823353722956097,
          "cvrmse_percent": 3.135023910166652,
          "absolute_error_percentiles_lux": {
            "p50": 0.5098508596420288,
            "p90": 8.177210807800297,
            "p95": 14.523790359497069,
            "p99": 32.7678189086914
          },
          "maximum_absolute_error_lux": 183.7373046875,
          "worst": {
            "sensor_index": 35,
            "position": [
              5.5,
              1.5,
              0.75
            ],
            "hour_of_year": 6850.5,
            "foton_lux": 15030.6611328125,
            "radiance_lux": 14846.923828125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.1308830062939653,
            "maximum_error_percentage_points": 1.343287671232872,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.3015112331036173,
            "maximum_error_percentage_points": 1.76959598665362,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.40914291003332043,
            "maximum_error_percentage_points": 3.8041095890411043,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.40965568308034067,
            "maximum_error_percentage_points": 3.8041095890410936,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.004333580155497946,
            "maximum_error_percentage_points": 0.07849315068493112,
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
      "maximum_error_percentage_points": 0.004931506849315426,
      "metrics": {
        "da": [
          {
            "identifier": "plan_i_small_center_grid",
            "maximum_error_percentage_points": 0.0046575342465753344,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_i_small_center_grid",
            "maximum_error_percentage_points": 0.004842679794521132,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_i_small_center_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_i_small_center_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_i_small_center_grid",
            "maximum_error_percentage_points": 0.004109589041095596,
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
      "study_preparation_seconds": 0.3714222839998911,
      "weather_seconds": 0.2308594380001523,
      "metric_reduction_seconds": 0.2593731370002388,
      "write_seconds": 0.012352145000022574,
      "total_seconds": 0.5029567550000138,
      "cold_end_to_end_seconds": 0.8743790389999049,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0020620899999812536,
      "engine_upload_seconds": 0.013564649,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.019010576,
      "engine_annual_reduction_seconds": 0.009772377,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.019010576
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3714222839998911,
      "weather_seconds": 0.21351035699990462,
      "metric_reduction_seconds": 0.2607765150000887,
      "write_seconds": 0.013476354999966134,
      "total_seconds": 0.488041162999707,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.488041162999707,
      "raw_export_seconds": 0.002345047999824601,
      "engine_upload_seconds": 0.013990024,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.6e-08,
      "engine_annual_reduction_seconds": 0.009804291,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01538204999997106,
      "full": 0.033185889000378666
    }
  },
  "elapsed_seconds": 3.2558898840002257,
  "result_class": "passed"
}
```
