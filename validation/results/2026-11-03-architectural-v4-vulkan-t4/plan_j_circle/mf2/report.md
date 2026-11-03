# Foton report

Status: **passed**

```json
{
  "scene": "plan_j_circle",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_j_circle",
    "category": "form",
    "question": "How does a circle opening illuminate a J-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "j",
    "window_profile": "circle"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 47,
    "floor_area": 63.0,
    "aperture_area": 1.4400000000000004
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "3865d080b901bf599bffb3bf7de309dce602b41d4c6645bff82e2aaa84bea99e",
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
      "scene_fingerprint": 13821501161281504296,
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
      "scene_fingerprint": 13821501161281504296,
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
    "model_sha256": "97326f2cf68a492c424b8398e6c749cd606364cab75a497c8f9f9c413b3b0031",
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
          "maximum": 0.0001864732475951314,
          "p95": 0.0,
          "p99": 5.005276761949062e-06
        },
        "bias_percent": 0.027496474479277295,
        "identifier": "plan_j_circle_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.2639429751878328,
        "worst_index": [
          20,
          491,
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
          "maximum": 0.00048467516899108887,
          "p95": 6.345158908516169e-06,
          "p99": 4.624275607056916e-05
        },
        "bias_percent": 0.017125463304002886,
        "identifier": "plan_j_circle_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.3798378390057278,
        "worst_index": [
          19,
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
          "maximum": 0.00028661638498306274,
          "p95": 5.407830030890182e-06,
          "p99": 3.84058803319931e-05
        },
        "bias_percent": 0.06127870421582474,
        "identifier": "plan_j_circle_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.965355250997834,
        "worst_index": [
          8,
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
            "identifier": "plan_j_circle_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00037089246325194836,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 8.310499833896756e-05
                },
                "candidate_energy": 2.674548380944543,
                "cvrmse_percent": 49.79018022707447,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.09060359355292417,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.6721273375524106,
                "relative_energy_error_percent": 0.09060359355292417,
                "rms_normalized_rmse_percent": 5.480173924482248,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003828397369943559,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.003457504906691611,
                  "rgb_channel": 0,
                  "sky_patch_index": 366
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007440745830535889,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.978624363298877e-07,
                  "p99": 0.00012149856775067747
                },
                "candidate_energy": 0.6683020745641954,
                "cvrmse_percent": 331.25039575299996,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.9996817846850885,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6750504307579206,
                "relative_energy_error_percent": 0.9996817846850885,
                "rms_normalized_rmse_percent": 7.130417666838674,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.01512044994160533,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.01586452452465892,
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.78816597629339,
            "full": 279.04837497044355
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 122.06595903262496,
            "full": 285.16070800833404
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.75191701296717,
            "full": 283.96870801225305
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 131.90070795826614,
            "full": 297.1671250415966
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
            "identifier": "plan_j_circle_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003074305132031441,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.0353020671755075e-05
                },
                "candidate_energy": 2.6754259603635546,
                "cvrmse_percent": 39.45048221484317,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.07241756819464297,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.6734898840036294,
                "relative_energy_error_percent": 0.07241756819464297,
                "rms_normalized_rmse_percent": 4.343647990639272,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003067508456297219,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.003374938969500363,
                  "rgb_channel": 0,
                  "sky_patch_index": 402
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00041651749052107334,
                  "p50": 0.0,
                  "p90": 4.705519586423179e-06,
                  "p95": 8.967231451606494e-06,
                  "p99": 8.634596633783076e-05
                },
                "candidate_energy": 1.318724619458422,
                "cvrmse_percent": 117.99090503631001,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.06978259893072905,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3196455023866598,
                "relative_energy_error_percent": 0.06978259893072905,
                "rms_normalized_rmse_percent": 4.202316619244818,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0002856425126083195,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": -0.00013087497791275382,
                  "rgb_channel": 0,
                  "sky_patch_index": 153
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.55795799102634,
            "full": 3200.0829169992357
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 160.48962494824082,
            "full": 3208.1309999339283
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.3175419792533,
            "full": 3214.568916009739
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.33987495675683,
            "full": 3207.8996249474585
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
            "identifier": "plan_j_circle_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003619004273787141,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.760703399777412e-05
                },
                "candidate_energy": 2.6764674535347694,
                "cvrmse_percent": 42.254050048882206,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.16432159699558055,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.672076654503144,
                "relative_energy_error_percent": 0.16432159699558055,
                "rms_normalized_rmse_percent": 4.6536252993640606,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003053914522752166,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.00341581495013088,
                  "rgb_channel": 0,
                  "sky_patch_index": 262
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005688214441761374,
                  "p50": 0.0,
                  "p90": 4.705205356003717e-06,
                  "p95": 8.795482472123695e-06,
                  "p99": 0.00010169058805331588
                },
                "candidate_energy": 1.3178278443921094,
                "cvrmse_percent": 136.64616322373985,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.33684683337342564,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3222819091312878,
                "relative_energy_error_percent": 0.33684683337342564,
                "rms_normalized_rmse_percent": 4.885462980650272,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00014962698332965374,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.0004191944608464837,
                  "rgb_channel": 0,
                  "sky_patch_index": 312
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 164.88908301107585,
            "full": 3418.7697909073904
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 161.04929195716977,
            "full": 3522.1677919616923
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 169.4563750643283,
            "full": 3421.68958298862
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.91233302559704,
            "full": 3410.2606249507517
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
            "identifier": "plan_j_circle_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00019608857110142708,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.357790410518646e-05
                },
                "candidate_energy": 2.6761766589797844,
                "cvrmse_percent": 22.595142842329857,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.015300968878528233,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.675767240667028,
                "relative_energy_error_percent": 0.015300968878528231,
                "rms_normalized_rmse_percent": 2.490499875569523,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004036600003018975,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.003840511431917548,
                  "rgb_channel": 0,
                  "sky_patch_index": 358
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003159473417326808,
                  "p50": 0.0,
                  "p90": 3.356845809321385e-06,
                  "p95": 6.330025826173369e-06,
                  "p99": 5.256524309515953e-05
                },
                "candidate_energy": 1.3199886244593557,
                "cvrmse_percent": 68.70276218377978,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.12318575757590501,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3216166679640367,
                "relative_energy_error_percent": 0.12318575757590501,
                "rms_normalized_rmse_percent": 2.450869094004088,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00013107509585097432,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.00018487224588170648,
                  "rgb_channel": 0,
                  "sky_patch_index": 96
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 229.84683292452246,
            "full": 6087.471417034976
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 238.2550840266049,
            "full": 6063.990540918894
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 225.2177499467507,
            "full": 6074.608750059269
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 238.91908291261643,
            "full": 5999.535624985583
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/plan_j_circle/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4666.46962496452,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_circle/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 18611.91433307249,
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
        "identifier": "plan_j_circle_grid",
        "full_identifier": "plan_j_circle_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": 0.007175970266852143,
            "cvrmse_percent": 5.761453693293547,
            "rms_normalized_rmse_percent": 0.6352078768636911,
            "reference_energy": 2.6754475958042576,
            "candidate_energy": 2.6756395851282377,
            "relative_energy_error_percent": 0.007175970266852143,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.2451343940920196e-06,
              "maximum": 8.632848039269447e-05
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 446,
              "rgb_channel": 0,
              "reference": 0.0022769891656935215,
              "candidate": 0.002363317646086216,
              "position": [
                4.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.8765520865150185,
            "cvrmse_percent": 49.963272186895416,
            "rms_normalized_rmse_percent": 1.782592595276828,
            "reference_energy": 1.3213269918962105,
            "candidate_energy": 1.3097448725790581,
            "relative_energy_error_percent": 0.8765520865150185,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.226244072924601e-06,
              "p95": 7.48149432183709e-06,
              "p99": 2.256082370877266e-05,
              "maximum": 0.00033208727836608887
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01760740764439106,
              "candidate": 0.01727532036602497,
              "position": [
                3.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.28498304678537084,
            "cvrmse_percent": 16.394306526750885,
            "rms_normalized_rmse_percent": 1.7692680064532489,
            "reference_energy": 3.996774587700468,
            "candidate_energy": 3.985384457707296,
            "relative_energy_error_percent": 0.28498304678537084,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.220288246870041e-06,
              "p95": 7.4856216087937355e-06,
              "p99": 2.214871346950531e-05,
              "maximum": 0.00033208727836608887
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01760740764439106,
              "candidate": 0.01727532036602497,
              "position": [
                3.5,
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
        "identifier": "plan_j_circle_grid",
        "full_identifier": "plan_j_circle_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": 0.007175970266852143,
            "cvrmse_percent": 5.761453693293547,
            "rms_normalized_rmse_percent": 0.6352078768636911,
            "reference_energy": 2.6754475958042576,
            "candidate_energy": 2.6756395851282377,
            "relative_energy_error_percent": 0.007175970266852143,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.2451343940920196e-06,
              "maximum": 8.632848039269447e-05
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 446,
              "rgb_channel": 0,
              "reference": 0.0022769891656935215,
              "candidate": 0.002363317646086216,
              "position": [
                4.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 95.61086832814084,
            "cvrmse_percent": 1208.4342447913632,
            "rms_normalized_rmse_percent": 25.87765511896693,
            "reference_energy": 0.6695665142603104,
            "candidate_energy": 1.3097448725790581,
            "relative_energy_error_percent": 95.61086832814084,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.7070000467356294e-05,
              "p95": 2.8599999495781958e-05,
              "p99": 7.565162377431989e-05,
              "maximum": 0.0043781828135252
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015492487698793411,
              "candidate": 0.01987067051231861,
              "position": [
                4.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 19.144025303688984,
            "cvrmse_percent": 241.88881138315148,
            "rms_normalized_rmse_percent": 25.877475447693268,
            "reference_energy": 3.345014110064568,
            "candidate_energy": 3.985384457707296,
            "relative_energy_error_percent": 19.144025303688988,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.7020000086631626e-05,
              "p95": 2.8656556423811708e-05,
              "p99": 7.543014362454414e-05,
              "maximum": 0.0043781828135252
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015492487698793411,
              "candidate": 0.01987067051231861,
              "position": [
                4.5,
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
      "bias_percent": 0.14989467772030482,
      "rms_normalized_error_percent": 0.1847057469432879,
      "absolute_error": {
        "p95": 0.04557401847756294,
        "p99": 0.06252738501086469,
        "maximum": 0.06299783912285406
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.929474016506801,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.1847057469432879
    },
    "overcast": {
      "bias_percent": 0.10422803023691554,
      "rms_normalized_error_percent": 0.13489617176682697,
      "absolute_error": {
        "p95": 0.02121288776397703,
        "p99": 0.03569347381591797,
        "maximum": 0.037407875061035156
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.6159849166870117,
      "reference_fraction_of_uniform": 0.6657341122627258,
      "rms_normalized_to_uniform_percent": 0.09916900666939976
    },
    "horizon": {
      "bias_percent": 0.7011233281615558,
      "rms_normalized_error_percent": 2.736469672679071,
      "absolute_error": {
        "p95": 0.023047194077414356,
        "p99": 0.02447579572798145,
        "maximum": 0.025085456948292117
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.32585460287062085,
      "reference_fraction_of_uniform": 0.08292575583953014,
      "rms_normalized_to_uniform_percent": 0.09828718138389664
    },
    "north": {
      "bias_percent": -98.03657171178475,
      "rms_normalized_error_percent": 99.98304002700408,
      "absolute_error": {
        "p95": 8.611229059169986e-05,
        "p99": 0.00013401138159679246,
        "maximum": 0.00015059890574775636
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.3890846275899094e-05,
      "reference_fraction_of_uniform": 3.5350394682609476e-06,
      "rms_normalized_to_uniform_percent": 0.00030684105174870024
    },
    "east": {
      "bias_percent": 0.1215157192167621,
      "rms_normalized_error_percent": 0.34680082485216845,
      "absolute_error": {
        "p95": 0.01888564825057981,
        "p99": 0.026536227464675897,
        "maximum": 0.029840469360351562
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.8414868116378784,
      "reference_fraction_of_uniform": 0.2141474336385727,
      "rms_normalized_to_uniform_percent": 0.0695402738635276
    },
    "south": {
      "bias_percent": 0.2045420532586785,
      "rms_normalized_error_percent": 0.21794306862441953,
      "absolute_error": {
        "p95": 0.03968529701232909,
        "p99": 0.048642950057983386,
        "maximum": 0.05475807189941406
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.5426297187805176,
      "reference_fraction_of_uniform": 0.6470661759376526,
      "rms_normalized_to_uniform_percent": 0.1425033767460495
    },
    "west": {
      "bias_percent": 0.11923235389870006,
      "rms_normalized_error_percent": 0.20930646996817026,
      "absolute_error": {
        "p95": 0.008911013603210447,
        "p99": 0.014435721635818473,
        "maximum": 0.01843172311782837
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.8223587870597839,
      "reference_fraction_of_uniform": 0.2092795968055725,
      "rms_normalized_to_uniform_percent": 0.04198453929347713
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
        "identifier": "plan_j_circle_grid",
        "sensor_count": 47,
        "illuminance": {
          "nmbe_percent": 0.09007763249511695,
          "cvrmse_percent": 2.771210389529437,
          "absolute_error_percentiles_lux": {
            "p50": 0.6302719116210938,
            "p90": 10.149491119384772,
            "p95": 17.050973510742182,
            "p99": 41.16795776367196
          },
          "maximum_absolute_error_lux": 273.7578125,
          "worst": {
            "sensor_index": 15,
            "position": [
              3.5,
              1.5,
              0.75
            ],
            "hour_of_year": 7090.5,
            "foton_lux": 10970.4833984375,
            "radiance_lux": 10696.7255859375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.11842320023316805,
            "maximum_error_percentage_points": 0.5213698630136989,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1824044121977097,
            "maximum_error_percentage_points": 0.65278943365578,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.3763334304867387,
            "maximum_error_percentage_points": 1.728219178082199,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.3753482949577371,
            "maximum_error_percentage_points": 1.7282191780821918,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0074526377149519,
            "maximum_error_percentage_points": 0.08643835616438444,
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
      "maximum_error_percentage_points": 0.004894049657536925,
      "metrics": {
        "da": [
          {
            "identifier": "plan_j_circle_grid",
            "maximum_error_percentage_points": 0.00438356164384146,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_j_circle_grid",
            "maximum_error_percentage_points": 0.004894049657536925,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_j_circle_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_j_circle_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_j_circle_grid",
            "maximum_error_percentage_points": 0.00479452054794538,
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
      "study_preparation_seconds": 0.47201414400115027,
      "weather_seconds": 0.27630237699850113,
      "metric_reduction_seconds": 1.4458937659983349,
      "write_seconds": 0.04108475999964867,
      "total_seconds": 1.7636727280005289,
      "cold_end_to_end_seconds": 2.235686872001679,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.028327664000244113,
      "engine_upload_seconds": 0.04747528,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.056982587,
      "engine_annual_reduction_seconds": 0.058774984,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.056982587
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.47201414400115027,
      "weather_seconds": 0.24474668699986069,
      "metric_reduction_seconds": 1.3935699140020006,
      "write_seconds": 0.022474802000942873,
      "total_seconds": 1.6610937419973197,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 1.6610937419973197,
      "raw_export_seconds": 0.009747033000166994,
      "engine_upload_seconds": 0.05204711,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 7.4e-08,
      "engine_annual_reduction_seconds": 0.053670972,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02317256900278153,
      "full": 0.0781088309995539
    }
  },
  "elapsed_seconds": 6.507733393002127,
  "result_class": "passed"
}
```
