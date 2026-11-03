# Foton report

Status: **passed**

```json
{
  "scene": "deep_overhang",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "deep_overhang",
    "category": "shading",
    "question": "How does a deep overhang exclude high sky while retaining low sky?",
    "interactions": [
      "overhang",
      "zenith_mask"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 1,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "e14c9e2853456bd9e4ed486d703a1f0fd146df69460c72548256ccdf1a88b06f",
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
      "scene_fingerprint": 8376055839539751168,
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 8376055839539751168,
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
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 65536,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "f41d5b79791c377f3bbce5814ee683a2c4a6d398ab9ab54476f2d72c65ba3d6f",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "42ebbd5873d9863a0ad3aca60e92d9e55c1ae842623c6cc1f4949849ae92cd10",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0006440107244998217,
          "p95": 2.089736517518757e-06,
          "p99": 7.056444883346558e-05
        },
        "bias_percent": -0.020058718769192418,
        "identifier": "deep_overhang_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.9436860472227417,
        "worst_index": [
          17,
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
          "maximum": 0.0005135089159011841,
          "p95": 3.0634006907348356e-05,
          "p99": 0.0001262035220861435
        },
        "bias_percent": 0.19243563927492713,
        "identifier": "deep_overhang_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.986411746454722,
        "worst_index": [
          28,
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
          "maximum": 0.00039223022758960724,
          "p95": 2.7597261941991708e-05,
          "p99": 0.00011592032387852669
        },
        "bias_percent": -0.10536803791154487,
        "identifier": "deep_overhang_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8305436251050663,
        "worst_index": [
          2,
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
            "identifier": "deep_overhang_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007996660424396396,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.315963597036869e-05,
                  "p99": 0.00023613101802766323
                },
                "candidate_energy": 2.910404684706009,
                "cvrmse_percent": 23.313413017283892,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0199418626204821,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.9098244115193665,
                "relative_energy_error_percent": 0.019941862620482097,
                "rms_normalized_rmse_percent": 4.18009005932245,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0018362830160185695,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.002635949058458209,
                  "rgb_channel": 0,
                  "sky_patch_index": 17
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0016784099861979485,
                  "p50": 0.0,
                  "p90": 9.328319947599084e-06,
                  "p95": 7.904918938947956e-05,
                  "p99": 0.0003574064467102289
                },
                "candidate_energy": 2.425090051147947,
                "cvrmse_percent": 46.6026569303043,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.0655978382767464,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4235002873488156,
                "relative_energy_error_percent": 0.06559783827674641,
                "rms_normalized_rmse_percent": 3.258847024165198,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.021060979925096035,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.022739389911293983,
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 117.80554102733731,
            "full": 227.3503749165684
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.09712501335889,
            "full": 226.78995796013623
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 109.62979192845523,
            "full": 222.00408298522234
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 115.15495798084885,
            "full": 230.56937498040497
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
            "identifier": "deep_overhang_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003707695286720991,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.293694597028661e-05,
                  "p99": 0.00016604410484433174
                },
                "candidate_energy": 2.9104043254792487,
                "cvrmse_percent": 15.843296853201952,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.361612463732878,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.8999178610556555,
                "relative_energy_error_percent": 0.361612463732878,
                "rms_normalized_rmse_percent": 2.8386110985499617,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007705903612077236,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.007335134083405137,
                  "rgb_channel": 0,
                  "sky_patch_index": 45
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006909742951393127,
                  "p50": 1.217182941104511e-07,
                  "p90": 1.9506981516315136e-05,
                  "p95": 5.9454498114064315e-05,
                  "p99": 0.00026381155475974083
                },
                "candidate_energy": 3.804625851555244,
                "cvrmse_percent": 20.67985846180064,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.3766198869338481,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8190089989290037,
                "relative_energy_error_percent": 0.37661988693384807,
                "rms_normalized_rmse_percent": 1.816822369199825,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.060271721333265305,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.06096269562840462,
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.71412502601743,
            "full": 2251.0237080277875
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 131.96720799896866,
            "full": 2256.433374946937
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.26641596015543,
            "full": 2265.389167005196
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.31704197824,
            "full": 2254.7389999963343
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
            "identifier": "deep_overhang_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004921900108456612,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2784174325352067e-05,
                  "p99": 0.00014958041720092297
                },
                "candidate_energy": 2.9041537337980117,
                "cvrmse_percent": 15.382519066225667,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.13806797044062455,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.9001495561660704,
                "relative_energy_error_percent": 0.13806797044062458,
                "rms_normalized_rmse_percent": 2.7558155023125606,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0060189515352249146,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.005526761524379253,
                  "rgb_channel": 0,
                  "sky_patch_index": 71
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005748150870203972,
                  "p50": 1.227526453817518e-07,
                  "p90": 1.8750479284790345e-05,
                  "p95": 5.04910741256025e-05,
                  "p99": 0.00024621450575068593
                },
                "candidate_energy": 3.8265973348084508,
                "cvrmse_percent": 18.94545002532002,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.060352631343016154,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8289081816477832,
                "relative_energy_error_percent": 0.060352631343016154,
                "rms_normalized_rmse_percent": 1.6679938457564254,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.023476354777812958,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.02290153969079256,
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.2449580002576,
            "full": 2396.8274580547586
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.70387503691018,
            "full": 2412.219666992314
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.55658400524408,
            "full": 2487.5300840940326
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.26891692448407,
            "full": 2421.121041988954
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
            "identifier": "deep_overhang_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00022031599655747414,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1633499525487423e-05,
                  "p99": 8.435547351837158e-05
                },
                "candidate_energy": 2.9057321729660543,
                "cvrmse_percent": 8.762612973409613,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.09318685568423209,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.9030269334471086,
                "relative_energy_error_percent": 0.0931868556842321,
                "rms_normalized_rmse_percent": 1.571934463161363,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007697375025600195,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.007477059029042721,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007869042456150055,
                  "p50": 9.374660692174075e-08,
                  "p90": 1.328060170635581e-05,
                  "p95": 3.48672663676552e-05,
                  "p99": 0.0001560045056976378
                },
                "candidate_energy": 3.8189466952172886,
                "cvrmse_percent": 13.337154362715811,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.026873142380273562,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8179206999516246,
                "relative_energy_error_percent": 0.026873142380273562,
                "rms_normalized_rmse_percent": 1.1726084793596803,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.036801934242248535,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.03601502999663353,
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 193.54470807593316,
            "full": 4309.699708013795
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 191.96533295325935,
            "full": 4369.824082939886
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 195.96383394673467,
            "full": 4383.879750035703
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 185.51979097537696,
            "full": 4362.198041984811
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/deep_overhang/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 815.4467080021277,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2745.955375023186,
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
      36,
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
        "identifier": "deep_overhang_grid",
        "full_identifier": "deep_overhang_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.02810067885430365,
            "cvrmse_percent": 6.782113410631054,
            "rms_normalized_rmse_percent": 1.2163948776269204,
            "reference_energy": 2.9035105443081193,
            "candidate_energy": 2.9026946381345624,
            "relative_energy_error_percent": 0.02810067885430365,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.3928511179983578e-06,
              "p99": 4.784793418366462e-05,
              "maximum": 0.0003419344429858029
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 94,
              "rgb_channel": 0,
              "reference": 0.0008694861899130046,
              "candidate": 0.0012114206328988075,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.1058719903696193,
            "cvrmse_percent": 24.016678112666174,
            "rms_normalized_rmse_percent": 2.1100163152107045,
            "reference_energy": 3.819302690714066,
            "candidate_energy": 3.777066092030026,
            "relative_energy_error_percent": 1.1058719903696193,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.1730485855186998e-07,
              "p90": 2.6236652047373354e-05,
              "p95": 4.3107090459670806e-05,
              "p99": 0.00012906017946079373,
              "maximum": 0.0012224502861499786
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0286770798265934,
              "candidate": 0.02745462954044342,
              "position": [
                3.5,
                3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.6403941825026002,
            "cvrmse_percent": 13.549940982752572,
            "rms_normalized_rmse_percent": 2.0954497330717077,
            "reference_energy": 6.722813235022185,
            "candidate_energy": 6.679760730164588,
            "relative_energy_error_percent": 0.6403941825026002,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.1730485855186998e-07,
              "p90": 2.6365259145677555e-05,
              "p95": 4.341400563134798e-05,
              "p99": 0.00011482462286949158,
              "maximum": 0.0012224502861499786
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0286770798265934,
              "candidate": 0.02745462954044342,
              "position": [
                3.5,
                3.5,
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
      36,
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
        "identifier": "deep_overhang_grid",
        "full_identifier": "deep_overhang_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.02810067885430365,
            "cvrmse_percent": 6.782113410631054,
            "rms_normalized_rmse_percent": 1.2163948776269204,
            "reference_energy": 2.9035105443081193,
            "candidate_energy": 2.9026946381345624,
            "relative_energy_error_percent": 0.02810067885430365,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.3928511179983578e-06,
              "p99": 4.784793418366462e-05,
              "maximum": 0.0003419344429858029
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 94,
              "rgb_channel": 0,
              "reference": 0.0008694861899130046,
              "candidate": 0.0012114206328988075,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 55.37732463210865,
            "cvrmse_percent": 412.0878290703418,
            "rms_normalized_rmse_percent": 28.91435938976067,
            "reference_energy": 2.430899168184993,
            "candidate_energy": 3.777066092030026,
            "relative_energy_error_percent": 55.37732463210865,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0001322699972661212,
              "p95": 0.00019537270127329944,
              "p99": 0.0004910221323370934,
              "maximum": 0.008789248764514923
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017275461927056313,
              "candidate": 0.026064710691571236,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 25.220241604627454,
            "cvrmse_percent": 187.77104159472816,
            "rms_normalized_rmse_percent": 28.91157998945549,
            "reference_energy": 5.3344097124931125,
            "candidate_energy": 6.679760730164588,
            "relative_energy_error_percent": 25.220241604627457,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00013114999455865473,
              "p95": 0.00019168437866028397,
              "p99": 0.0005037062801420689,
              "maximum": 0.008789248764514923
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017275461927056313,
              "candidate": 0.026064710691571236,
              "position": [
                5.5,
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
      "bias_percent": 0.30067733249121487,
      "rms_normalized_error_percent": 0.31925012993050667,
      "absolute_error": {
        "p95": 0.06101080465341224,
        "p99": 0.07810209414522859,
        "maximum": 0.08493614897527246
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.012044921453725,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.31925012993050667
    },
    "overcast": {
      "bias_percent": 0.23559590555377266,
      "rms_normalized_error_percent": 0.2700106941974322,
      "absolute_error": {
        "p95": 0.027581408619880676,
        "p99": 0.034864252805709824,
        "maximum": 0.037990450859069824
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.316098928451538,
      "reference_fraction_of_uniform": 0.5515758991241455,
      "rms_normalized_to_uniform_percent": 0.1654795816516433
    },
    "horizon": {
      "bias_percent": 1.096419184705247,
      "rms_normalized_error_percent": 2.0952140561891794,
      "absolute_error": {
        "p95": 0.04568407652184331,
        "p99": 0.06788861058558505,
        "maximum": 0.07558707727214209
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.055065252216303,
      "reference_fraction_of_uniform": 0.17549191098877984,
      "rms_normalized_to_uniform_percent": 0.22658919110677708
    },
    "north": {
      "bias_percent": -40.98065178064155,
      "rms_normalized_error_percent": 133.5734144073202,
      "absolute_error": {
        "p95": 8.678954873175826e-05,
        "p99": 0.00010638923658916609,
        "maximum": 0.00010878987632167991
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.1243442713748664e-05,
      "reference_fraction_of_uniform": 1.8701528006204171e-06,
      "rms_normalized_to_uniform_percent": 0.00030086589775527706
    },
    "east": {
      "bias_percent": 0.23430070437644396,
      "rms_normalized_error_percent": 0.5584358071497694,
      "absolute_error": {
        "p95": 0.025618553161621094,
        "p99": 0.040979230403900134,
        "maximum": 0.044228553771972656
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.4367196559906006,
      "reference_fraction_of_uniform": 0.23897354304790497,
      "rms_normalized_to_uniform_percent": 0.1380946107929312
    },
    "south": {
      "bias_percent": 0.3646675286848587,
      "rms_normalized_error_percent": 0.3900029256365029,
      "absolute_error": {
        "p95": 0.0578790009021759,
        "p99": 0.06859409809112547,
        "maximum": 0.07315361499786377
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.413371562957764,
      "reference_fraction_of_uniform": 0.7340882420539856,
      "rms_normalized_to_uniform_percent": 0.27611678358049896
    },
    "west": {
      "bias_percent": 0.19997319704048686,
      "rms_normalized_error_percent": 0.45904879836463325,
      "absolute_error": {
        "p95": 0.020200543105602264,
        "p99": 0.02703350335359572,
        "maximum": 0.03063201904296875
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.368071436882019,
      "reference_fraction_of_uniform": 0.22755509614944458,
      "rms_normalized_to_uniform_percent": 0.11016231986252004
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
        "identifier": "deep_overhang_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.07875489138132188,
          "cvrmse_percent": 2.396632122868503,
          "absolute_error_percentiles_lux": {
            "p50": 1.9369583129882812,
            "p90": 15.19235534667969,
            "p95": 23.53510894775389,
            "p99": 51.986397705078105
          },
          "maximum_absolute_error_lux": 229.8193359375,
          "worst": {
            "sensor_index": 17,
            "position": [
              2.5,
              0.5,
              0.75
            ],
            "hour_of_year": 2961.5,
            "foton_lux": 13330.1884765625,
            "radiance_lux": 13100.369140625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.6375494672754942,
            "maximum_error_percentage_points": 1.6724657534246532,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.2869237643653207,
            "maximum_error_percentage_points": 1.2323380532193227,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.16213470319634707,
            "maximum_error_percentage_points": 0.7086301369863008,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.16691400304414059,
            "maximum_error_percentage_points": 0.7086301369863008,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.022713089802131044,
            "maximum_error_percentage_points": 0.14123287671232987,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 27.77777777777778,
          "radiance_percent": 27.77777777777778,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.7777777777777777,
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
            "identifier": "deep_overhang_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "deep_overhang_grid",
            "maximum_error_percentage_points": 0.004415667808210344,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "deep_overhang_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "deep_overhang_grid",
            "maximum_error_percentage_points": 0.004794520547953596,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "deep_overhang_grid",
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
      "study_preparation_seconds": 0.44127437899805955,
      "weather_seconds": 0.4168349129977287,
      "metric_reduction_seconds": 0.24144332600189955,
      "write_seconds": 0.028696923996903934,
      "total_seconds": 0.6873751550010638,
      "cold_end_to_end_seconds": 1.1286495339991234,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.016150687999470392,
      "engine_upload_seconds": 0.017091731,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.012597461,
      "engine_annual_reduction_seconds": 0.007346089,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.012597461
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.44127437899805955,
      "weather_seconds": 0.23077227400062839,
      "metric_reduction_seconds": 0.1800955309990968,
      "write_seconds": 0.020902008000120986,
      "total_seconds": 0.43203843999799574,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.43203843999799574,
      "raw_export_seconds": 0.008535745000699535,
      "engine_upload_seconds": 0.014692593,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.9e-08,
      "engine_annual_reduction_seconds": 0.007113529,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.014735734999703709,
      "full": 0.024495729001500877
    }
  },
  "elapsed_seconds": 2.9593955740019737,
  "result_class": "passed"
}
```
