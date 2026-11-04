# Foton report

Status: **passed**

```json
{
  "scene": "overhang_fins",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "overhang_fins",
    "category": "shading",
    "question": "How do combined overhangs and side fins mask the sky?",
    "interactions": [
      "overhang",
      "fins",
      "combined_shading"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 3,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "df9dbebb8d4ad815f971ce2c31cce6016c2a538a7773fe49ac40ddc0571e23e9",
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 11874334619688306964,
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 11874334619688306964,
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/12f3d0b2-7d1e-44d9-9264-d1e29a27929b/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "63186ed5b1112348f9a3b7bac09c1e2d528e643020c661591154d0f9ef548f74",
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
          "maximum": 0.0005986811593174934,
          "p95": 0.0,
          "p99": 6.160326302051544e-05
        },
        "bias_percent": -0.04662117912984425,
        "identifier": "overhang_fins_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.8559240210599814,
        "worst_index": [
          23,
          99,
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
          "maximum": 0.0007945038378238678,
          "p95": 2.7022726317227272e-05,
          "p99": 0.00011834502220153809
        },
        "bias_percent": 0.0670976966987206,
        "identifier": "overhang_fins_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0482322236811104,
        "worst_index": [
          23,
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
          "maximum": 0.0006159618496894836,
          "p95": 2.3417422926286195e-05,
          "p99": 0.00010319985449314117
        },
        "bias_percent": 0.06000568721204395,
        "identifier": "overhang_fins_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9336014155280367,
        "worst_index": [
          23,
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
            "identifier": "overhang_fins_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0008484437130391598,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0003718833904713392
                },
                "candidate_energy": 2.3475809137562464,
                "cvrmse_percent": 40.96017614749917,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.032045344274537195,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.346828864367126,
                "relative_energy_error_percent": 0.032045344274537195,
                "rms_normalized_rmse_percent": 6.061366830658882,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005936879198998213,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.006785322912037373,
                  "rgb_channel": 0,
                  "sky_patch_index": 70
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013201646506786346,
                  "p50": 0.0,
                  "p90": 1.6385605704272166e-05,
                  "p95": 4.888631710855392e-05,
                  "p99": 0.00046716746874153614
                },
                "candidate_energy": 2.0551667948127204,
                "cvrmse_percent": 62.935840622673574,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.058397459173474386,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0539673300797006,
                "relative_energy_error_percent": 0.05839745917347438,
                "rms_normalized_rmse_percent": 4.194832552263411,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03353067487478256,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.03221051022410393,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 106.72441695351154,
            "full": 225.36966705229133
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 111.22058297041804,
            "full": 242.90341697633266
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 104.87229202408344,
            "full": 228.28666598070413
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 109.35362498275936,
            "full": 231.07429104857147
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
            "identifier": "overhang_fins_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003035524860024452,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0001294771209359169
                },
                "candidate_energy": 2.3478437198118627,
                "cvrmse_percent": 14.098025200144328,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.15412034632377963,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.3442307832101505,
                "relative_energy_error_percent": 0.15412034632377963,
                "rms_normalized_rmse_percent": 2.0915628822157033,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003959073452278972,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.0036555209662765265,
                  "rgb_channel": 0,
                  "sky_patch_index": 45
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005880948156118393,
                  "p50": 4.1173183262799284e-07,
                  "p90": 2.1465599274961278e-05,
                  "p95": 4.446621205715926e-05,
                  "p99": 0.00022873049601912498
                },
                "candidate_energy": 3.330545985499594,
                "cvrmse_percent": 20.313069471295325,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.0923786466703248,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.333625543661885,
                "relative_energy_error_percent": 0.09237864667032482,
                "rms_normalized_rmse_percent": 1.7409901618709767,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02131824567914009,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.02190634049475193,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 131.38216699007899,
            "full": 2496.3141250191256
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.92016692645848,
            "full": 2398.814791929908
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.04087501578033,
            "full": 2424.7002500342205
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.63666704390198,
            "full": 2419.2919170018286
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
            "identifier": "overhang_fins_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004354706034064293,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00012616883032023907
                },
                "candidate_energy": 2.351150442063954,
                "cvrmse_percent": 16.260123904770573,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.19004923531518592,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.3466905745717668,
                "relative_energy_error_percent": 0.19004923531518594,
                "rms_normalized_rmse_percent": 2.4100009984060664,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007254725089296699,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.006819254485890269,
                  "rgb_channel": 0,
                  "sky_patch_index": 44
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007961206138134003,
                  "p50": 4.352437059651493e-07,
                  "p90": 2.139112984878011e-05,
                  "p95": 4.3831376569869424e-05,
                  "p99": 0.0002223204355686903
                },
                "candidate_energy": 3.325609105105322,
                "cvrmse_percent": 20.1325037545524,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.44325593528698237,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.3404156959408375,
                "relative_energy_error_percent": 0.44325593528698237,
                "rms_normalized_rmse_percent": 1.722652314460582,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06167631037533283,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.06247243098914623,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.02941710874438,
            "full": 2602.453042054549
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.40716596879065,
            "full": 2552.8293329989538
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.5332499584183,
            "full": 2524.183291941881
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.0149579383433,
            "full": 2585.395250003785
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
            "identifier": "overhang_fins_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002228455850854516,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 8.008850272744894e-05
                },
                "candidate_energy": 2.348099722848019,
                "cvrmse_percent": 10.364170197780018,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.08474396204970837,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.3461115349791726,
                "relative_energy_error_percent": 0.08474396204970837,
                "rms_normalized_rmse_percent": 1.5374655406035573,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0020066919969394803,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.002229537582024932,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005868393927812576,
                  "p50": 3.516023525662604e-07,
                  "p90": 1.4911849575582892e-05,
                  "p95": 2.9817580980306954e-05,
                  "p99": 0.00013580030645243824
                },
                "candidate_energy": 3.3341076903041973,
                "cvrmse_percent": 12.707600861979172,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.2470735797683865,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.3423657931182085,
                "relative_energy_error_percent": 0.2470735797683865,
                "rms_normalized_rmse_percent": 1.0884879571574233,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06190529465675354,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0624921340495348,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 200.91649994719774,
            "full": 4544.358541024849
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 199.86150006297976,
            "full": 4647.4210830638185
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 203.31133296713233,
            "full": 4633.617833023891
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 189.56699990667403,
            "full": 4474.825666053221
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
    "/Users/ssanjay/GitHub/foton-release-0.3.2/validation/results/2026-11-04-architectural-v4-metal-0.3.2-release/overhang_fins/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 737.0437911013141,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2645.0687079923227,
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
        "identifier": "overhang_fins_grid",
        "full_identifier": "overhang_fins_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.018984217025436026,
            "cvrmse_percent": 5.753852221027571,
            "rms_normalized_rmse_percent": 0.8524568892001334,
            "reference_energy": 2.3463134934900154,
            "candidate_energy": 2.345868064244314,
            "relative_energy_error_percent": 0.018984217025436026,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.5930570447817445e-05,
              "maximum": 0.00018672272562980652
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 99,
              "rgb_channel": 0,
              "reference": 0.009291455149650574,
              "candidate": 0.00947817787528038,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.8816842806553566,
            "cvrmse_percent": 23.555004343039606,
            "rms_normalized_rmse_percent": 2.0182313198616115,
            "reference_energy": 3.3390288936241905,
            "candidate_energy": 3.3095892007425656,
            "relative_energy_error_percent": 0.8816842806553566,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.985493771731853e-07,
              "p90": 2.500554546713829e-05,
              "p95": 4.001636370958294e-05,
              "p99": 0.00011282972991466522,
              "maximum": 0.0013053491711616516
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03033461980521679,
              "candidate": 0.029029270634055138,
              "position": [
                3.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5256521083947492,
            "cvrmse_percent": 13.772265357639235,
            "rms_normalized_rmse_percent": 2.009229665870323,
            "reference_energy": 5.685342387114206,
            "candidate_energy": 5.65545726498688,
            "relative_energy_error_percent": 0.5256521083947493,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.999131644784939e-07,
              "p90": 2.4674460291862488e-05,
              "p95": 3.903851993527489e-05,
              "p99": 0.00010425788059365004,
              "maximum": 0.0013053491711616516
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03033461980521679,
              "candidate": 0.029029270634055138,
              "position": [
                3.5,
                2.5,
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
        "identifier": "overhang_fins_grid",
        "full_identifier": "overhang_fins_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.018984217025436026,
            "cvrmse_percent": 5.753852221027571,
            "rms_normalized_rmse_percent": 0.8524568892001334,
            "reference_energy": 2.3463134934900154,
            "candidate_energy": 2.345868064244314,
            "relative_energy_error_percent": 0.018984217025436026,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.5930570447817445e-05,
              "maximum": 0.00018672272562980652
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 99,
              "rgb_channel": 0,
              "reference": 0.009291455149650574,
              "candidate": 0.00947817787528038,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 61.01464654658805,
            "cvrmse_percent": 456.8285473958075,
            "rms_normalized_rmse_percent": 30.467188053117514,
            "reference_energy": 2.0554584764342962,
            "candidate_energy": 3.3095892007425656,
            "relative_energy_error_percent": 61.01464654658803,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00012894790233985987,
              "p95": 0.00019460117291600904,
              "p99": 0.0004189256578683853,
              "maximum": 0.010297413915395737
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05186210572719574,
              "candidate": 0.062159519642591476,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 28.481377582222308,
            "cvrmse_percent": 213.32239692973405,
            "rms_normalized_rmse_percent": 30.46733203013904,
            "reference_energy": 4.401771969924312,
            "candidate_energy": 5.65545726498688,
            "relative_energy_error_percent": 28.481377582222304,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00012904999312013388,
              "p95": 0.0001966961557627654,
              "p99": 0.0004235359374433756,
              "maximum": 0.010297413915395737
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05186210572719574,
              "candidate": 0.062159519642591476,
              "position": [
                2.5,
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
      "bias_percent": 0.25960423433233737,
      "rms_normalized_error_percent": 0.39542633576413283,
      "absolute_error": {
        "p95": 0.06673962131558042,
        "p99": 0.07070109262568133,
        "maximum": 0.07264062620996148
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.038626528474941,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.39542633576413283
    },
    "overcast": {
      "bias_percent": 0.16563937912331547,
      "rms_normalized_error_percent": 0.33497514838658826,
      "absolute_error": {
        "p95": 0.0335434228181839,
        "p99": 0.04374256432056426,
        "maximum": 0.04566001892089844
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.845956802368164,
      "reference_fraction_of_uniform": 0.5648278594017029,
      "rms_normalized_to_uniform_percent": 0.2077780816075664
    },
    "horizon": {
      "bias_percent": 1.5766016917573926,
      "rms_normalized_error_percent": 3.0266001337890547,
      "absolute_error": {
        "p95": 0.04544129131038983,
        "p99": 0.07518687278691265,
        "maximum": 0.08341192078165616
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.7385528606055904,
      "reference_fraction_of_uniform": 0.14657821063573268,
      "rms_normalized_to_uniform_percent": 0.3038443592697712
    },
    "north": {
      "bias_percent": 1.7160989533442461,
      "rms_normalized_error_percent": 106.25773554426918,
      "absolute_error": {
        "p95": 0.001000654681774904,
        "p99": 0.001872715519857591,
        "maximum": 0.002338901162147522
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 0.0003389642806723714,
      "reference_fraction_of_uniform": 6.727314757881686e-05,
      "rms_normalized_to_uniform_percent": 0.006483065729403529
    },
    "east": {
      "bias_percent": 0.12923438332902115,
      "rms_normalized_error_percent": 0.6008079088115882,
      "absolute_error": {
        "p95": 0.017292000353336334,
        "p99": 0.019076722860336303,
        "maximum": 0.01909470558166504
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.8710235357284546,
      "reference_fraction_of_uniform": 0.1728692352771759,
      "rms_normalized_to_uniform_percent": 0.11116976263570438
    },
    "south": {
      "bias_percent": 0.3184355106040588,
      "rms_normalized_error_percent": 0.44250986889779803,
      "absolute_error": {
        "p95": 0.054041504859924316,
        "p99": 0.07234706878662107,
        "maximum": 0.07652640342712402
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.090353012084961,
      "reference_fraction_of_uniform": 0.811799168586731,
      "rms_normalized_to_uniform_percent": 0.3525909434530164
    },
    "west": {
      "bias_percent": 0.16278896577316765,
      "rms_normalized_error_percent": 0.5161674301446086,
      "absolute_error": {
        "p95": 0.015059471130371094,
        "p99": 0.015455326437950135,
        "maximum": 0.015482842922210693
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.8682579398155212,
      "reference_fraction_of_uniform": 0.17232035100460052,
      "rms_normalized_to_uniform_percent": 0.09653368043700203
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
        "identifier": "overhang_fins_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.0542186530021406,
          "cvrmse_percent": 2.5821128156066897,
          "absolute_error_percentiles_lux": {
            "p50": 1.6288871765136719,
            "p90": 14.739544677734377,
            "p95": 22.373745727539056,
            "p99": 44.72924163818357
          },
          "maximum_absolute_error_lux": 305.861328125,
          "worst": {
            "sensor_index": 23,
            "position": [
              3.5,
              0.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 7972.19921875,
            "radiance_lux": 7666.337890625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.430814307458143,
            "maximum_error_percentage_points": 1.3456164383561635,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.28906838329876855,
            "maximum_error_percentage_points": 1.2514463769491329,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.25546803652968086,
            "maximum_error_percentage_points": 1.4256164383561654,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.25788051750380486,
            "maximum_error_percentage_points": 1.4256164383561654,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.011267123287671288,
            "maximum_error_percentage_points": 0.08671232876712409,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 22.22222222222222,
          "radiance_percent": 22.22222222222222,
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
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "overhang_fins_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "overhang_fins_grid",
            "maximum_error_percentage_points": 0.004880136986294303,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "overhang_fins_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "overhang_fins_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "overhang_fins_grid",
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
      "study_preparation_seconds": 0.008945874986238778,
      "weather_seconds": 0.08004499995149672,
      "metric_reduction_seconds": 0.039995084051042795,
      "write_seconds": 0.01682716596405953,
      "total_seconds": 0.13702829100657254,
      "cold_end_to_end_seconds": 0.14597416599281132,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0023401669459417462,
      "engine_upload_seconds": 0.000239958,
      "engine_acceleration_structure_seconds": 0.003391292,
      "engine_tracing_seconds": 0.014461333281360567,
      "engine_annual_reduction_seconds": 0.0003884166944772005,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.014461333281360567
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.008945874986238778,
      "weather_seconds": 0.07397399994079024,
      "metric_reduction_seconds": 0.01636208302807063,
      "write_seconds": 0.010554875014349818,
      "total_seconds": 0.1010692500276491,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1010692500276491,
      "raw_export_seconds": 0.0014968749601393938,
      "engine_upload_seconds": 3.5041e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00040062505286186934,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.018196041928604245,
      "full": 0.019881083047948778
    }
  },
  "elapsed_seconds": 0.7479254170320928,
  "result_class": "passed"
}
```
