# Foton report

Status: **passed**

```json
{
  "scene": "plan_l_large_center",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_l_large_center",
    "category": "form",
    "question": "How does a large center opening illuminate a L-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "l",
    "window_profile": "large_center"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 48,
    "floor_area": 54.0,
    "aperture_area": 4.800000000000001
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "2f3eb587d51b143fd9bd5061e74578c32d22a146c139a1133847efc3b5954e21",
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 9519076420102749743,
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 9519076420102749743,
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
    "maximum_samples": 16384,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "plan_l_large_center_grid",
        "bias_percent": -0.04277980441328652,
        "rms_normalized_error_percent": 0.9236977764085991,
        "absolute_error": {
          "p95": 4.3422915041446686e-07,
          "p99": 5.43864443898201e-05,
          "maximum": 0.00047375215217471123
        },
        "worst_index": [
          42,
          99,
          0
        ],
        "passed": true
      }
    ],
    "samples_per_patch": [
      256,
      1024
    ]
  },
  "depth_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "plan_l_large_center_grid",
        "bias_percent": 0.03850213486029847,
        "rms_normalized_error_percent": 0.7828462607706094,
        "absolute_error": {
          "p95": 3.051571547985077e-05,
          "p99": 0.0001164381392300129,
          "maximum": 0.0003107171505689621
        },
        "worst_index": [
          46,
          0,
          0
        ],
        "passed": true
      }
    ]
  },
  "sample_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "plan_l_large_center_grid",
        "bias_percent": 0.026027474063448828,
        "rms_normalized_error_percent": 0.6699265204472631,
        "absolute_error": {
          "p95": 2.7014873921871185e-05,
          "p99": 9.162910282611847e-05,
          "maximum": 0.0004173554480075836
        },
        "worst_index": [
          40,
          0,
          0
        ],
        "passed": true
      }
    ]
  },
  "oracle_levels": [
    {
      "samples": 20000,
      "material_bounces": 1,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_l_large_center_grid",
            "start_sensor_index": 0,
            "sensor_count": 48,
            "stages": {
              "direct": {
                "nmbe_percent": -0.1097211880038083,
                "cvrmse_percent": 16.36967127085902,
                "rms_normalized_rmse_percent": 2.8555619694327943,
                "reference_energy": 6.654864893032936,
                "candidate_energy": 6.647563096212252,
                "relative_energy_error_percent": 0.10972118800380828,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.6720990212634206e-05,
                  "p99": 0.0002821981906890869,
                  "maximum": 0.0006749685853719711
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "sky_patch_index": 116,
                  "rgb_channel": 0,
                  "reference": 0.015776900574564934,
                  "candidate": 0.016451869159936905
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.7246295105485849,
                "cvrmse_percent": 77.04677486695364,
                "rms_normalized_rmse_percent": 3.2383113001980153,
                "reference_energy": 2.145547770630742,
                "candidate_energy": 2.1300004983218344,
                "relative_energy_error_percent": 0.724629510548585,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.39205686133939e-06,
                  "p95": 8.315034210681915e-05,
                  "p99": 0.0004170769825577736,
                  "maximum": 0.0017904303967952728
                },
                "worst": {
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.044358450919389725,
                  "candidate": 0.04256802052259445
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 126.8791250186041,
            "full": 276.06191695667803
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 123.7243339419365,
            "full": 278.7154170218855
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 125.96391700208187,
            "full": 271.22170804068446
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 135.94558299519122,
            "full": 279.25429202150553
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 8,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_l_large_center_grid",
            "start_sensor_index": 0,
            "sensor_count": 48,
            "stages": {
              "direct": {
                "nmbe_percent": -0.011958063215362663,
                "cvrmse_percent": 8.415937608400407,
                "rms_normalized_rmse_percent": 1.4697957203208571,
                "reference_energy": 6.651992883111234,
                "candidate_energy": 6.65119743359719,
                "relative_energy_error_percent": 0.011958063215362661,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.199150185333565e-05,
                  "p99": 0.0001555299386382103,
                  "maximum": 0.00045455642975866795
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "sky_patch_index": 44,
                  "rgb_channel": 0,
                  "reference": 0.007714122999459505,
                  "candidate": 0.007259566569700837
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.045273987142610564,
                "cvrmse_percent": 22.89000464704576,
                "rms_normalized_rmse_percent": 1.5395748993238556,
                "reference_energy": 4.080526809803054,
                "candidate_energy": 4.082374226986275,
                "relative_energy_error_percent": 0.04527398714261057,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.0358002811017286e-07,
                  "p90": 2.0573700749082534e-05,
                  "p95": 5.177230923436582e-05,
                  "p99": 0.00022349203936755657,
                  "maximum": 0.0008910596370697021
                },
                "worst": {
                  "global_sensor_index": 40,
                  "local_sensor_index": 40,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0586584247648716,
                  "candidate": 0.0595494844019413
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 178.04391600657254,
            "full": 3061.171417008154
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 169.4741250248626,
            "full": 3060.3835829533637
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 163.84570894297212,
            "full": 3078.1271669548005
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 160.55033297743648,
            "full": 3047.9123330442235
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 12,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_l_large_center_grid",
            "start_sensor_index": 0,
            "sensor_count": 48,
            "stages": {
              "direct": {
                "nmbe_percent": -0.03918638100927239,
                "cvrmse_percent": 7.989968601447945,
                "rms_normalized_rmse_percent": 1.3954085210327116,
                "reference_energy": 6.654997278705196,
                "candidate_energy": 6.6523894261154055,
                "relative_energy_error_percent": 0.039186381009272395,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.038251841440797e-05,
                  "p99": 0.00013595749624073505,
                  "maximum": 0.0004480623174458742
                },
                "worst": {
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "sky_patch_index": 71,
                  "rgb_channel": 0,
                  "reference": 0.007857518969103694,
                  "candidate": 0.00740945665165782
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.021707309409102017,
                "cvrmse_percent": 21.850952954761024,
                "rms_normalized_rmse_percent": 1.469808865582302,
                "reference_energy": 4.08304161932012,
                "candidate_energy": 4.0839279377977284,
                "relative_energy_error_percent": 0.021707309409102017,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 9.855462757002442e-08,
                  "p90": 2.0849832799285777e-05,
                  "p95": 5.650783714372665e-05,
                  "p99": 0.00022291834466159344,
                  "maximum": 0.0006113047711551189
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 38,
                  "sky_patch_index": 72,
                  "rgb_channel": 0,
                  "reference": 3.9040111005306244e-05,
                  "candidate": 0.0006503448821604252
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 167.7105410490185,
            "full": 3275.285999989137
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 168.99929102510214,
            "full": 3364.4391670823097
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 174.00200001429766,
            "full": 3270.714999991469
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 161.6027910495177,
            "full": 3293.3420829940587
          }
        }
      ]
    },
    {
      "samples": 80000,
      "material_bounces": 12,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_l_large_center_grid",
            "start_sensor_index": 0,
            "sensor_count": 48,
            "stages": {
              "direct": {
                "nmbe_percent": 0.009951914277928388,
                "cvrmse_percent": 4.712430912103004,
                "rms_normalized_rmse_percent": 0.8231632603922817,
                "reference_energy": 6.652632560028451,
                "candidate_energy": 6.65329462431805,
                "relative_energy_error_percent": 0.00995191427792839,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.0734889656305313e-05,
                  "p99": 7.794646080583334e-05,
                  "maximum": 0.00018773763440549374
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 44,
                  "sky_patch_index": 77,
                  "rgb_channel": 0,
                  "reference": 0.005491448799148202,
                  "candidate": 0.005679186433553696
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.07534390917187951,
                "cvrmse_percent": 13.076590616669511,
                "rms_normalized_rmse_percent": 0.8797927103155451,
                "reference_energy": 4.085470090632484,
                "candidate_energy": 4.088548243506814,
                "relative_energy_error_percent": 0.07534390917187951,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 8.418237484875135e-08,
                  "p90": 1.4045255011296832e-05,
                  "p95": 3.33913994836621e-05,
                  "p99": 0.00012419931590557098,
                  "maximum": 0.0005500316619873047
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 38,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.06384394690394402,
                  "candidate": 0.06439397856593132
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 250.51637494470924,
            "full": 5800.163957988843
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 272.96400000341237,
            "full": 5729.11945800297
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 303.41433302965015,
            "full": 5750.092291040346
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 245.5081669613719,
            "full": 5789.192459080368
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 1385.2354170521721,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_l_large_center/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 4930.911792092957,
      "worker_pool_size": 12,
      "invocation_count": 3
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      48,
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
        "identifier": "plan_l_large_center_grid",
        "full_identifier": "plan_l_large_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": 0.05870040520822543,
            "cvrmse_percent": 2.9471831019278656,
            "rms_normalized_rmse_percent": 0.5146542009978081,
            "reference_energy": 6.652876656219178,
            "candidate_energy": 6.656781921774382,
            "relative_energy_error_percent": 0.05870040520822543,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.818422555923462e-07,
              "p99": 3.629550337791443e-05,
              "maximum": 0.0002032020129263401
            },
            "worst": {
              "global_sensor_index": 40,
              "local_sensor_index": 40,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.003940886352211237,
              "candidate": 0.004144088365137577,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.9952409923979374,
            "cvrmse_percent": 33.51720998538727,
            "rms_normalized_rmse_percent": 2.255406274662141,
            "reference_energy": 4.087096101935851,
            "candidate_energy": 4.046419646130687,
            "relative_energy_error_percent": 0.9952409923979373,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.4657899189151067e-07,
              "p90": 5.369244026951493e-05,
              "p95": 8.927873568609357e-05,
              "p99": 0.000217961409362033,
              "maximum": 0.0022345781326293945
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04642362892627716,
              "candidate": 0.044189050793647766,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.3423769415247235,
            "cvrmse_percent": 12.736647362193665,
            "rms_normalized_rmse_percent": 2.2521659022467806,
            "reference_energy": 10.739972758155028,
            "candidate_energy": 10.703201567905069,
            "relative_energy_error_percent": 0.3423769415247235,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.480965974882565e-07,
              "p90": 5.2975157450418955e-05,
              "p95": 8.913828060030937e-05,
              "p99": 0.00021438614930957556,
              "maximum": 0.0022345781326293945
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04642362892627716,
              "candidate": 0.044189050793647766,
              "position": [
                3.5,
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
      48,
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
        "identifier": "plan_l_large_center_grid",
        "full_identifier": "plan_l_large_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": 0.05870040520822543,
            "cvrmse_percent": 2.9471831019278656,
            "rms_normalized_rmse_percent": 0.5146542009978081,
            "reference_energy": 6.652876656219178,
            "candidate_energy": 6.656781921774382,
            "relative_energy_error_percent": 0.05870040520822543,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.818422555923462e-07,
              "p99": 3.629550337791443e-05,
              "maximum": 0.0002032020129263401
            },
            "worst": {
              "global_sensor_index": 40,
              "local_sensor_index": 40,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.003940886352211237,
              "candidate": 0.004144088365137577,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 89.42923343915413,
            "cvrmse_percent": 607.1399983185008,
            "rms_normalized_rmse_percent": 25.48666019801909,
            "reference_energy": 2.1361115033126197,
            "candidate_energy": 4.046419646130687,
            "relative_energy_error_percent": 89.42923343915413,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00020330499974079434,
              "p95": 0.0003315241483505815,
              "p99": 0.0006659780628979206,
              "maximum": 0.013469759374856949
            },
            "worst": {
              "global_sensor_index": 43,
              "local_sensor_index": 43,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02569841966032982,
              "candidate": 0.03916817903518677,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.779678998625982,
            "cvrmse_percent": 147.58236573192255,
            "rms_normalized_rmse_percent": 25.490215789150707,
            "reference_energy": 8.788988159531797,
            "candidate_energy": 10.703201567905069,
            "relative_energy_error_percent": 21.779678998625986,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00020334100408945236,
              "p95": 0.0003357816021889448,
              "p99": 0.0006725999992340803,
              "maximum": 0.013469759374856949
            },
            "worst": {
              "global_sensor_index": 43,
              "local_sensor_index": 43,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02569841966032982,
              "candidate": 0.03916817903518677,
              "position": [
                6.5,
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
      "bias_percent": 0.28151321145810554,
      "rms_normalized_error_percent": 0.3781577424980491,
      "absolute_error": {
        "p95": 0.15479083639089175,
        "p99": 0.24055130438369354,
        "maximum": 0.3075012092225151
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 9.86830998354832,
      "rms_normalized_to_uniform_percent": 0.3781577424980491
    },
    "overcast": {
      "bias_percent": 0.233967449376513,
      "rms_normalized_error_percent": 0.30360627495516596,
      "absolute_error": {
        "p95": 0.07551984786987304,
        "p99": 0.14803651809692395,
        "maximum": 0.20012855529785156
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 6.540656566619873,
      "rms_normalized_to_uniform_percent": 0.21495321890473043
    },
    "horizon": {
      "bias_percent": 2.198265985434603,
      "rms_normalized_error_percent": 4.3530380212164355,
      "absolute_error": {
        "p95": 0.10855952063509543,
        "p99": 0.12439517435121157,
        "maximum": 0.1344791332110038
      },
      "worst_index": [
        41
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.7492186610138146,
      "rms_normalized_to_uniform_percent": 0.219710567869509
    },
    "north": {
      "bias_percent": -81.32804825808907,
      "rms_normalized_error_percent": 121.09429082221223,
      "absolute_error": {
        "p95": 6.708052133035375e-05,
        "p99": 9.517165032775668e-05,
        "maximum": 0.0001046909792421502
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 1.2557015907077584e-05,
      "rms_normalized_to_uniform_percent": 0.00012198401923091947
    },
    "east": {
      "bias_percent": 0.3700766170282147,
      "rms_normalized_error_percent": 0.6407246039313462,
      "absolute_error": {
        "p95": 0.04861027002334595,
        "p99": 0.08826642394065859,
        "maximum": 0.0961681604385376
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.3248298168182373,
      "rms_normalized_to_uniform_percent": 0.14075815517770784
    },
    "south": {
      "bias_percent": 0.21664557167666057,
      "rms_normalized_error_percent": 0.42148695859154484,
      "absolute_error": {
        "p95": 0.12061996459960934,
        "p99": 0.1947470474243165,
        "maximum": 0.23223495483398438
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 6.407344818115234,
      "rms_normalized_to_uniform_percent": 0.2692819561435523
    },
    "west": {
      "bias_percent": 0.519429449543574,
      "rms_normalized_error_percent": 0.6210470208566569,
      "absolute_error": {
        "p95": 0.07173619270324706,
        "p99": 0.10081978201866156,
        "maximum": 0.12214255332946777
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.7790565490722656,
      "rms_normalized_to_uniform_percent": 0.12916222084246848
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
        "identifier": "plan_l_large_center_grid",
        "sensor_count": 48,
        "illuminance": {
          "nmbe_percent": 0.15399653965222987,
          "cvrmse_percent": 3.132964490075878,
          "absolute_error_percentiles_lux": {
            "p50": 2.6953659057617188,
            "p90": 34.59760284423829,
            "p95": 56.37260742187499,
            "p99": 119.80672546386694
          },
          "maximum_absolute_error_lux": 465.83203125,
          "worst": {
            "sensor_index": 41,
            "position": [
              5.5,
              0.5,
              0.75
            ],
            "hour_of_year": 4451.5,
            "foton_lux": 27557.16015625,
            "radiance_lux": 27091.328125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.34351598173515957,
            "maximum_error_percentage_points": 1.5116438356164394,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.5191445889799063,
            "maximum_error_percentage_points": 2.3215503091600063,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.7037585616438361,
            "maximum_error_percentage_points": 4.489999999999995,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.7169834474885833,
            "maximum_error_percentage_points": 4.489999999999998,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.027211757990867624,
            "maximum_error_percentage_points": 0.2426027397260313,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 31.25,
          "radiance_percent": 29.166666666666668,
          "difference_percentage_points": 2.083333333333332,
          "tolerance_percentage_points": 2.0833333333333335,
          "ambiguous_sensor_count": 1,
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
            "identifier": "plan_l_large_center_grid",
            "maximum_error_percentage_points": 0.004794520547953596,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_l_large_center_grid",
            "maximum_error_percentage_points": 0.004842947345895965,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_l_large_center_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_l_large_center_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_l_large_center_grid",
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
      "study_preparation_seconds": 0.0070405000587925315,
      "weather_seconds": 0.11282670800574124,
      "metric_reduction_seconds": 0.03845412493683398,
      "write_seconds": 0.03875366598367691,
      "total_seconds": 0.19020195794291794,
      "cold_end_to_end_seconds": 0.19724245800171047,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.011900124954991043,
      "engine_upload_seconds": 0.000348708,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.019324208376929164,
      "engine_annual_reduction_seconds": 0.000462499912828207,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.019324208376929164
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.0070405000587925315,
      "weather_seconds": 0.11039570800494403,
      "metric_reduction_seconds": 0.013786041992716491,
      "write_seconds": 0.0325919589959085,
      "total_seconds": 0.15695220895577222,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.15695220895577222,
      "raw_export_seconds": 0.011293041054159403,
      "engine_upload_seconds": 9.4666e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00065595842897892,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013763833092525601,
      "full": 0.010637832921929657
    }
  },
  "elapsed_seconds": 61.0341110000154,
  "result_class": "passed"
}
```
