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
  "model_sha256": "3de92213e911c1f4dbd6ae37c0ab3a1a62ceaafbcc51a15900431c3257131e46",
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
      "scene_fingerprint": 7091735636442897822,
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
      "scene_fingerprint": 7091735636442897822,
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/plan_i_small_center/mf1/oracle/scene.rad"
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
            "nmbe_percent": -0.017013650471947687,
            "cvrmse_percent": 6.987340380281342,
            "rms_normalized_rmse_percent": 0.6815779734873668,
            "reference_energy": 2.885622123187204,
            "candidate_energy": 2.885131173525224,
            "relative_energy_error_percent": 0.017013650471947687,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.551327295601368e-05,
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
            "nmbe_percent": -1.6477711301352322,
            "cvrmse_percent": 49.75619993323747,
            "rms_normalized_rmse_percent": 1.9598006376628017,
            "reference_energy": 1.3576779324825683,
            "candidate_energy": 1.3353065074709036,
            "relative_energy_error_percent": 1.6477711301352322,
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
            "nmbe_percent": -0.5387876033677351,
            "cvrmse_percent": 15.82422404069899,
            "rms_normalized_rmse_percent": 1.9480230770478801,
            "reference_energy": 4.243300055669772,
            "candidate_energy": 4.2204376809961275,
            "relative_energy_error_percent": 0.5387876033677351,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.0960787676594919e-05,
              "p95": 2.0412509911693633e-05,
              "p99": 5.9314421378076077e-05,
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
            "nmbe_percent": -0.017013650471947687,
            "cvrmse_percent": 6.987340380281342,
            "rms_normalized_rmse_percent": 0.6815779734873668,
            "reference_energy": 2.885622123187204,
            "candidate_energy": 2.885131173525224,
            "relative_energy_error_percent": 0.017013650471947687,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.551327295601368e-05,
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
            "nmbe_percent": 87.56346768710938,
            "cvrmse_percent": 607.1040815744267,
            "rms_normalized_rmse_percent": 13.412218034732566,
            "reference_energy": 0.7119224889243583,
            "candidate_energy": 1.3353065074709036,
            "relative_energy_error_percent": 87.56346768710938,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.145300113123085e-05,
              "p95": 8.232000254793093e-05,
              "p99": 0.0001919290516525507,
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
            "nmbe_percent": 17.31439456754814,
            "cvrmse_percent": 120.04872617295361,
            "rms_normalized_rmse_percent": 13.401965157130546,
            "reference_energy": 3.5975446121115624,
            "candidate_energy": 4.2204376809961275,
            "relative_energy_error_percent": 17.31439456754814,
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
      "bias_percent": -0.009864995640507667,
      "rms_normalized_error_percent": 0.2742660138613147,
      "absolute_error": {
        "p95": 0.05083361356969426,
        "p99": 0.0662862240698132,
        "maximum": 0.07166823278247048
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.6558319860500177,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2742660138613147
    },
    "overcast": {
      "bias_percent": 0.015005297705269949,
      "rms_normalized_error_percent": 0.2143954226284571,
      "absolute_error": {
        "p95": 0.03220636248588559,
        "p99": 0.03911006927490233,
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
      "rms_normalized_to_uniform_percent": 0.15603317404601266
    },
    "horizon": {
      "bias_percent": -0.35756659524825424,
      "rms_normalized_error_percent": 3.3949619781149174,
      "absolute_error": {
        "p95": 0.023249576296390587,
        "p99": 0.028381253593337104,
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
      "rms_normalized_to_uniform_percent": 0.12327988954981539
    },
    "north": {
      "bias_percent": -91.82867038216871,
      "rms_normalized_error_percent": 102.32046050095596,
      "absolute_error": {
        "p95": 0.00010130397822649682,
        "p99": 0.00018489357869839188,
        "maximum": 0.00038565651630051434
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.8694261598284356e-05,
      "reference_fraction_of_uniform": 7.038947387627559e-06,
      "rms_normalized_to_uniform_percent": 0.000665184021846982
    },
    "east": {
      "bias_percent": -0.06195645855155672,
      "rms_normalized_error_percent": 0.31139855062136584,
      "absolute_error": {
        "p95": 0.016393694281578056,
        "p99": 0.019811410903930654,
        "maximum": 0.021378517150878906
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.49523550271987915,
      "reference_fraction_of_uniform": 0.18647094070911407,
      "rms_normalized_to_uniform_percent": 0.07289180511751014
    },
    "south": {
      "bias_percent": -0.027304835127332925,
      "rms_normalized_error_percent": 0.3617169151334391,
      "absolute_error": {
        "p95": 0.04484698176383968,
        "p99": 0.055364775657653784,
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
      "rms_normalized_to_uniform_percent": 0.23374079384706423
    },
    "west": {
      "bias_percent": -0.11964578792546718,
      "rms_normalized_error_percent": 0.33175921628637506,
      "absolute_error": {
        "p95": 0.012725553661584846,
        "p99": 0.021996993422508222,
        "maximum": 0.025362730026245117
      },
      "worst_index": [
        53
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.48639246821403503,
      "reference_fraction_of_uniform": 0.18314127624034882,
      "rms_normalized_to_uniform_percent": 0.07409877359877838
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
          "nmbe_percent": -0.11826143157941449,
          "cvrmse_percent": 3.1350330567338176,
          "absolute_error_percentiles_lux": {
            "p50": 0.5099208354949951,
            "p90": 8.177210807800297,
            "p95": 14.523788261413573,
            "p99": 32.7678189086914
          },
          "maximum_absolute_error_lux": 183.734375,
          "worst": {
            "sensor_index": 35,
            "position": [
              5.5,
              1.5,
              0.75
            ],
            "hour_of_year": 6850.5,
            "foton_lux": 15030.658203125,
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
      "study_preparation_seconds": 0.0067647909745574,
      "weather_seconds": 0.08996358304284513,
      "metric_reduction_seconds": 0.05211624992080033,
      "write_seconds": 0.0342083340510726,
      "total_seconds": 0.17642987496219575,
      "cold_end_to_end_seconds": 0.18319466593675315,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.016737000085413456,
      "engine_upload_seconds": 0.000274958,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.031677291612140834,
      "engine_annual_reduction_seconds": 0.000606583314947784,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.031677291612140834
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.0067647909745574,
      "weather_seconds": 0.09257029101718217,
      "metric_reduction_seconds": 0.012926208903081715,
      "write_seconds": 0.03161149995867163,
      "total_seconds": 0.13724858302157372,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.13724858302157372,
      "raw_export_seconds": 0.013113624998368323,
      "engine_upload_seconds": 5.9125e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0006185000529512763,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.0139285420300439,
      "full": 0.05371979204937816
    }
  },
  "elapsed_seconds": 0.8330249170539901,
  "result_class": "passed"
}
```
