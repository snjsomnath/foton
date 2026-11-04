# Foton report

Status: **passed**

```json
{
  "scene": "mixed_glazing",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "mixed_glazing",
    "category": "materials",
    "question": "Are adjacent windows with different glass properties kept distinct?",
    "interactions": [
      "multiple_openings",
      "mixed_glazing",
      "material_assignment"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 2,
    "shades": 0,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 4.799999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "41f1888ee4f34491c30675100566b6def6ec312b806ff349d49d90df2473a4ca",
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
      "scene_fingerprint": 14239135421942143921,
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
      "scene_fingerprint": 14239135421942143921,
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
    "model_sha256": "622cae5301e41c07e79497fff4373eee58a1763c09d9697e7a50086c4597855f",
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
          "maximum": 0.00041220150887966156,
          "p95": 1.7040685634128695e-05,
          "p99": 9.735627099871635e-05
        },
        "bias_percent": -0.030979363387190893,
        "identifier": "mixed_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0098569488591904,
        "worst_index": [
          35,
          134,
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
          "maximum": 0.00046147219836711884,
          "p95": 5.6040810886770476e-05,
          "p99": 0.00017804355593398213
        },
        "bias_percent": 0.07779574716997383,
        "identifier": "mixed_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.945196887935872,
        "worst_index": [
          18,
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
          "maximum": 0.000560510903596878,
          "p95": 4.6431994996964856e-05,
          "p99": 0.00014262832701206207
        },
        "bias_percent": 0.05575522166988575,
        "identifier": "mixed_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8590783716345872,
        "worst_index": [
          26,
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
            "identifier": "mixed_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0009713293984532356,
                  "p50": 0.0,
                  "p90": 1.2966571375727654e-05,
                  "p95": 7.470146156265396e-05,
                  "p99": 0.00031476409640163183
                },
                "candidate_energy": 7.915271679639773,
                "cvrmse_percent": 12.82205704105062,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.04906211500771062,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.911390184288848,
                "relative_energy_error_percent": 0.04906211500771063,
                "rms_normalized_rmse_percent": 2.755317667832583,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.019728420302271843,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.02069974970072508,
                  "rgb_channel": 0,
                  "sky_patch_index": 99
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013795588165521622,
                  "p50": 0.0,
                  "p90": 4.3594278395175934e-05,
                  "p95": 0.00014483373379334797,
                  "p99": 0.0005325200036168098
                },
                "candidate_energy": 2.877598227393456,
                "cvrmse_percent": 57.76335604170877,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.01456851306499935,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.877179065185441,
                "relative_energy_error_percent": 0.014568513064999348,
                "rms_normalized_rmse_percent": 3.4255800214686816,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0005437489598989487,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": -0.0008358098566532135,
                  "rgb_channel": 0,
                  "sky_patch_index": 95
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.14612501580268,
            "full": 232.30425000656396
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 109.28504099138081,
            "full": 228.95599994808435
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 107.49495797790587,
            "full": 236.27745802514255
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 106.12320899963379,
            "full": 237.68179106991738
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
            "identifier": "mixed_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004954901523888111,
                  "p50": 0.0,
                  "p90": 9.725335985422134e-06,
                  "p95": 5.4597023699898034e-05,
                  "p99": 0.00018486022599972785
                },
                "candidate_energy": 7.920657214652238,
                "cvrmse_percent": 6.89921255986498,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.019961514548756176,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.922238613465652,
                "relative_energy_error_percent": 0.019961514548756176,
                "rms_normalized_rmse_percent": 1.4851552848707057,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.009963999968022108,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.01045949012041092,
                  "rgb_channel": 0,
                  "sky_patch_index": 74
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00083901546895504,
                  "p50": 3.135942705512207e-07,
                  "p90": 4.4431355490814894e-05,
                  "p95": 9.922619210556128e-05,
                  "p99": 0.00033511104993522167
                },
                "candidate_energy": 5.2307216389895,
                "cvrmse_percent": 20.634383888799764,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.30101254124601706,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.215023763432608,
                "relative_energy_error_percent": 0.30101254124601706,
                "rms_normalized_rmse_percent": 1.851718618928846,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03344094008207321,
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "reference": 0.03260192461311817,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.94258393440396,
            "full": 2231.4358330331743
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.95787489693612,
            "full": 2252.7600000612438
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.60445805080235,
            "full": 2231.187375029549
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.76324999891222,
            "full": 2209.484584047459
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
            "identifier": "mixed_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005314978770911694,
                  "p50": 0.0,
                  "p90": 1.0480100172571838e-05,
                  "p95": 6.251832364796428e-05,
                  "p99": 0.0002383049577474594
                },
                "candidate_energy": 7.922846128346464,
                "cvrmse_percent": 8.847051851467585,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.08829383491830851,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.915856914709821,
                "relative_energy_error_percent": 0.08829383491830851,
                "rms_normalized_rmse_percent": 1.9024636736290725,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.010467445012181997,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.009935947135090828,
                  "rgb_channel": 0,
                  "sky_patch_index": 45
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007489146664738655,
                  "p50": 3.1401640399053576e-07,
                  "p90": 4.9476089770905674e-05,
                  "p95": 0.0001142403503763487,
                  "p99": 0.0003757013473659754
                },
                "candidate_energy": 5.238543317938699,
                "cvrmse_percent": 21.426312378359572,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.12800271670596425,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.231846412396948,
                "relative_energy_error_percent": 0.12800271670596425,
                "rms_normalized_rmse_percent": 1.9284584777692846,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0006081601604819298,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": -0.00014075450599193573,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.6261249948293,
            "full": 2348.8900419324636
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.71995807718486,
            "full": 2409.0851669898257
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.30070806480944,
            "full": 2365.854208008386
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.0498750982806,
            "full": 2369.8252079775557
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
            "identifier": "mixed_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00027792155742645264,
                  "p50": 0.0,
                  "p90": 6.760237738490105e-06,
                  "p95": 3.120179899269715e-05,
                  "p99": 0.00010874168947339058
                },
                "candidate_energy": 7.918768376669959,
                "cvrmse_percent": 4.039792762908097,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.032776455031510554,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.921364719215035,
                "relative_energy_error_percent": 0.03277645503151056,
                "rms_normalized_rmse_percent": 0.8697144951238303,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.008272173348814249,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.007994251791387796,
                  "rgb_channel": 0,
                  "sky_patch_index": 42
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000601375475525856,
                  "p50": 2.823153408826329e-07,
                  "p90": 2.8164213290438056e-05,
                  "p95": 6.220150971785187e-05,
                  "p99": 0.0001924494281411171
                },
                "candidate_energy": 5.243093525114492,
                "cvrmse_percent": 11.33913845410445,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.0488253948639823,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.240534813298915,
                "relative_energy_error_percent": 0.04882539486398229,
                "rms_normalized_rmse_percent": 1.0216579851459344,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02929084002971649,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.028689464554190636,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 223.90724997967482,
            "full": 4188.521208940074
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 213.04266701918095,
            "full": 4167.346250033006
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 214.34525004588068,
            "full": 4155.818916973658
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 210.8003330649808,
            "full": 4196.5828749816865
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
    "/content/suite-vulkan-0.3.3/mixed_glazing/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 797.4596250569448,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2761.858875048347,
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
        "identifier": "mixed_glazing_grid",
        "full_identifier": "mixed_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.04867566712373198,
            "cvrmse_percent": 3.2575318558413815,
            "rms_normalized_rmse_percent": 0.7011836700764436,
            "reference_energy": 7.925182910303647,
            "candidate_energy": 7.921325274651281,
            "relative_energy_error_percent": 0.04867566712373198,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.867332220077515e-07,
              "p95": 1.2499126023612913e-05,
              "p99": 7.228963659144938e-05,
              "maximum": 0.00035694707185029984
            },
            "worst": {
              "global_sensor_index": 29,
              "local_sensor_index": 29,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.002620032289996743,
              "candidate": 0.0022630852181464434,
              "position": [
                4.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.067029504372175,
            "cvrmse_percent": 23.409349830499377,
            "rms_normalized_rmse_percent": 2.1067946510602686,
            "reference_energy": 5.236697792293839,
            "candidate_energy": 5.180820681795257,
            "relative_energy_error_percent": 1.067029504372175,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 8.304207881337788e-07,
              "p90": 4.672398790717125e-05,
              "p95": 6.990761903580265e-05,
              "p99": 0.00016568507999181747,
              "maximum": 0.0022781454026699066
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.050664324313402176,
              "candidate": 0.04838617891073227,
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
            "nmbe_percent": -0.45384658545916823,
            "cvrmse_percent": 9.288821280708477,
            "rms_normalized_rmse_percent": 2.1011347269293292,
            "reference_energy": 13.161880702597486,
            "candidate_energy": 13.102145956446538,
            "relative_energy_error_percent": 0.45384658545916823,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 8.164497558027506e-07,
              "p90": 4.599092062562704e-05,
              "p95": 6.839910201961173e-05,
              "p99": 0.00015983730554580688,
              "maximum": 0.0022781454026699066
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.050664324313402176,
              "candidate": 0.04838617891073227,
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
        "identifier": "mixed_glazing_grid",
        "full_identifier": "mixed_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.04867566712373198,
            "cvrmse_percent": 3.2575318558413815,
            "rms_normalized_rmse_percent": 0.7011836700764436,
            "reference_energy": 7.925182910303647,
            "candidate_energy": 7.921325274651281,
            "relative_energy_error_percent": 0.04867566712373198,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.867332220077515e-07,
              "p95": 1.2499126023612913e-05,
              "p99": 7.228963659144938e-05,
              "maximum": 0.00035694707185029984
            },
            "worst": {
              "global_sensor_index": 29,
              "local_sensor_index": 29,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.002620032289996743,
              "candidate": 0.0022630852181464434,
              "position": [
                4.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 80.79756842330984,
            "cvrmse_percent": 440.79425736488287,
            "rms_normalized_rmse_percent": 26.031250747362204,
            "reference_energy": 2.8655367032731096,
            "candidate_energy": 5.180820681795257,
            "relative_energy_error_percent": 80.79756842330984,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.000291300006210804,
              "p95": 0.0003882229881128295,
              "p99": 0.0006602123739867238,
              "maximum": 0.01246073842048645
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03236372023820877,
              "candidate": 0.04482445865869522,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.420502298674982,
            "cvrmse_percent": 117.05153086519667,
            "rms_normalized_rmse_percent": 26.03038779083351,
            "reference_energy": 10.790719613576757,
            "candidate_energy": 13.102145956446538,
            "relative_energy_error_percent": 21.420502298674982,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002910562325268984,
              "p95": 0.0003879556577885521,
              "p99": 0.0006820653798058629,
              "maximum": 0.01246073842048645
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03236372023820877,
              "candidate": 0.04482445865869522,
              "position": [
                5.5,
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
      "bias_percent": 0.049116029445737876,
      "rms_normalized_error_percent": 0.2071907839758708,
      "absolute_error": {
        "p95": 0.10268671092616688,
        "p99": 0.11128764184922292,
        "maximum": 0.11286613834700798
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 16.050098057729368,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2071907839758708
    },
    "overcast": {
      "bias_percent": 0.044997641042567954,
      "rms_normalized_error_percent": 0.17704151701426452,
      "absolute_error": {
        "p95": 0.06171822547912598,
        "p99": 0.06929092407226561,
        "maximum": 0.07263946533203125
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.248738288879395,
      "reference_fraction_of_uniform": 0.6385467648506165,
      "rms_normalized_to_uniform_percent": 0.12391693615099664
    },
    "horizon": {
      "bias_percent": 0.6154678865990555,
      "rms_normalized_error_percent": 1.9208943111070642,
      "absolute_error": {
        "p95": 0.05741488347473234,
        "p99": 0.08388106880407088,
        "maximum": 0.09547770240361464
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.4921332729582557,
      "reference_fraction_of_uniform": 0.09296723718392971,
      "rms_normalized_to_uniform_percent": 0.11910231131587967
    },
    "north": {
      "bias_percent": -31.40094247942258,
      "rms_normalized_error_percent": 124.89958370424209,
      "absolute_error": {
        "p95": 4.764140794577543e-05,
        "p99": 0.000151547207860858,
        "maximum": 0.00019507889373926446
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.0086868971702643e-05,
      "reference_fraction_of_uniform": 1.2515106391219888e-06,
      "rms_normalized_to_uniform_percent": 0.0001482341074954227
    },
    "east": {
      "bias_percent": 0.21167942578495025,
      "rms_normalized_error_percent": 0.28671884309434775,
      "absolute_error": {
        "p95": 0.031793028116226196,
        "p99": 0.04170218706130979,
        "maximum": 0.04662728309631348
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.6184730529785156,
      "reference_fraction_of_uniform": 0.22544865310192108,
      "rms_normalized_to_uniform_percent": 0.06879382694128877
    },
    "south": {
      "bias_percent": 0.041604853921687585,
      "rms_normalized_error_percent": 0.2590283004676999,
      "absolute_error": {
        "p95": 0.08653223514556885,
        "p99": 0.10570294857025143,
        "maximum": 0.11345195770263672
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.986174583435059,
      "reference_fraction_of_uniform": 0.6844926476478577,
      "rms_normalized_to_uniform_percent": 0.16573020203561376
    },
    "west": {
      "bias_percent": -0.20693662601129306,
      "rms_normalized_error_percent": 0.30903884014647004,
      "absolute_error": {
        "p95": 0.03590977191925049,
        "p99": 0.05271019935607907,
        "maximum": 0.06122875213623047
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.0152151584625244,
      "reference_fraction_of_uniform": 0.18786272406578064,
      "rms_normalized_to_uniform_percent": 0.0722589271139049
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
        "identifier": "mixed_glazing_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.04745366620743521,
          "cvrmse_percent": 1.5312774804677804,
          "absolute_error_percentiles_lux": {
            "p50": 3.062042236328125,
            "p90": 29.359423828125003,
            "p95": 43.830935668945315,
            "p99": 83.96061401367174
          },
          "maximum_absolute_error_lux": 536.77099609375,
          "worst": {
            "sensor_index": 34,
            "position": [
              5.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 7646.60546875,
            "radiance_lux": 8183.37646484375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.20207001522070023,
            "maximum_error_percentage_points": 0.9871232876712313,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.08524434566361608,
            "maximum_error_percentage_points": 0.42294814789137547,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.06754946727549428,
            "maximum_error_percentage_points": 0.361095890410958,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.080011415525114,
            "maximum_error_percentage_points": 0.3030136986301386,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.06135083713850812,
            "maximum_error_percentage_points": 0.2969863013698628,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 97.22222222222223,
          "radiance_percent": 97.22222222222223,
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
      "maximum_error_percentage_points": 0.0049793985445205635,
      "metrics": {
        "da": [
          {
            "identifier": "mixed_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "mixed_glazing_grid",
            "maximum_error_percentage_points": 0.0049793985445205635,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "mixed_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "mixed_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "mixed_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
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
      "study_preparation_seconds": 0.35676822600021296,
      "weather_seconds": 0.21123538599999847,
      "metric_reduction_seconds": 0.151624073999983,
      "write_seconds": 0.011844760000030874,
      "total_seconds": 0.37504294499990465,
      "cold_end_to_end_seconds": 0.7318111710001176,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0014098169999670063,
      "engine_upload_seconds": 0.013821124,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.010951483,
      "engine_annual_reduction_seconds": 0.008402847,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.010951483
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.35676822600021296,
      "weather_seconds": 0.22946758700004466,
      "metric_reduction_seconds": 0.1366017529999226,
      "write_seconds": 0.01108229300007224,
      "total_seconds": 0.3774125489999278,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.3774125489999278,
      "raw_export_seconds": 0.001404441999966366,
      "engine_upload_seconds": 0.013636408,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 2.06e-07,
      "engine_annual_reduction_seconds": 0.008947264,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01343221000001904,
      "full": 0.019947611999896253
    }
  },
  "elapsed_seconds": 2.6500242790000357,
  "result_class": "passed"
}
```
