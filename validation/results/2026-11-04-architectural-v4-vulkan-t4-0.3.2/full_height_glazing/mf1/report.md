# Foton report

Status: **passed**

```json
{
  "scene": "full_height_glazing",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "full_height_glazing",
    "category": "openings",
    "question": "Is large near-floor glazing represented without edge leaks?",
    "interactions": [
      "large_opening",
      "near_floor_glazing"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 15.119999999999997
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "0b3cb1cf003e05c34b9b13a8887150c8fe4908650f44806f15d633716df94b01",
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
      "scene_fingerprint": 3561854793510213323,
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
      "scene_fingerprint": 3561854793510213323,
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
    "model_sha256": "46520d6fd4c8133405a90893ea02d78dd010a6597b14eea6bcd67adda76a9002",
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
          "maximum": 0.0005638124421238899,
          "p95": 3.0665786471217854e-05,
          "p99": 0.00017638364806771278
        },
        "bias_percent": 0.01960222721521616,
        "identifier": "full_height_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9464788874835877,
        "worst_index": [
          10,
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
          "maximum": 0.0006998777389526367,
          "p95": 0.00010871121194213601,
          "p99": 0.0002113133668899536
        },
        "bias_percent": 0.016589518387359652,
        "identifier": "full_height_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.5136755985601399,
        "worst_index": [
          14,
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
          "maximum": 0.0007534250617027283,
          "p95": 8.824095129966729e-05,
          "p99": 0.0001756753772497177
        },
        "bias_percent": -0.004254369388448938,
        "identifier": "full_height_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.4455246101672897,
        "worst_index": [
          25,
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
            "identifier": "full_height_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0009066499769687653,
                  "p50": 0.0,
                  "p90": 0.00017084088176488876,
                  "p95": 0.0002833101898431778,
                  "p99": 0.0005600047297775745
                },
                "candidate_energy": 19.679379012295612,
                "cvrmse_percent": 9.62570707041616,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.022949257700401137,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 19.6748637771052,
                "relative_energy_error_percent": 0.022949257700401134,
                "rms_normalized_rmse_percent": 3.3633643335679455,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.014338510110974312,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.013431860134005547,
                  "rgb_channel": 0,
                  "sky_patch_index": 74
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0016556084156036377,
                  "p50": 0.0,
                  "p90": 0.00022456562146544456,
                  "p95": 0.00038387351596611534,
                  "p99": 0.0007296986877918243
                },
                "candidate_energy": 10.007232497174414,
                "cvrmse_percent": 25.234072386146636,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.0941344453380324,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 10.016661626037472,
                "relative_energy_error_percent": 0.0941344453380324,
                "rms_normalized_rmse_percent": 2.091815580728213,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.09507275745272636,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.09672836586833,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 124.39516698941588,
            "full": 245.14183402061462
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.82958398666233,
            "full": 249.19391598086804
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.85258301906288,
            "full": 262.5702080549672
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.38033302593976,
            "full": 270.27912496123463
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
            "identifier": "full_height_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004099099896848202,
                  "p50": 0.0,
                  "p90": 7.034442387521267e-05,
                  "p95": 0.00013764144387096167,
                  "p99": 0.00025452463887631893
                },
                "candidate_energy": 19.67940698999155,
                "cvrmse_percent": 4.369703618787216,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.04825946641516411,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 19.66991439426056,
                "relative_energy_error_percent": 0.04825946641516411,
                "rms_normalized_rmse_percent": 1.5267731471422088,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013352565001696348,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.013762474991381168,
                  "rgb_channel": 0,
                  "sky_patch_index": 72
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001006104052066803,
                  "p50": 6.076043064240366e-07,
                  "p90": 0.00011572430958040059,
                  "p95": 0.00020959594985470162,
                  "p99": 0.0004293409874662757
                },
                "candidate_energy": 17.107032322451186,
                "cvrmse_percent": 8.52352194418359,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.02746890259189946,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 17.11173272764593,
                "relative_energy_error_percent": 0.027468902591899456,
                "rms_normalized_rmse_percent": 0.938108093488113,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.12723354995250702,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.12622744590044022,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 163.6353749781847,
            "full": 2144.5534999947995
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 172.70683404058218,
            "full": 2125.4309999058023
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 166.56920802779496,
            "full": 2124.547957908362
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 164.4388750428334,
            "full": 2160.2558749727905
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
            "identifier": "full_height_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005227294750511646,
                  "p50": 0.0,
                  "p90": 6.587989628314972e-05,
                  "p95": 0.00011624890612438314,
                  "p99": 0.00023161526769399643
                },
                "candidate_energy": 19.68463618729038,
                "cvrmse_percent": 4.021398415733388,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.0187996082511452,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 19.688337517614855,
                "relative_energy_error_percent": 0.0187996082511452,
                "rms_normalized_rmse_percent": 1.4058021869080712,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013308110181242228,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.013830839656293392,
                  "rgb_channel": 0,
                  "sky_patch_index": 74
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010709986090660095,
                  "p50": 5.683747872353706e-07,
                  "p90": 0.00011433055624365807,
                  "p95": 0.00019341912993695582,
                  "p99": 0.0003805849701166153
                },
                "candidate_energy": 17.09228603145676,
                "cvrmse_percent": 8.161601378081649,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.1328991429975178,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 17.1150317619922,
                "relative_energy_error_percent": 0.1328991429975178,
                "rms_normalized_rmse_percent": 0.8977598914295514,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.12799584865570068,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.12692485004663467,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 163.61291601788253,
            "full": 2202.5567919481546
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 160.33445799257606,
            "full": 2205.552125000395
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 172.57204197812825,
            "full": 2171.503624995239
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 178.50224999710917,
            "full": 2203.7384998984635
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
            "identifier": "full_height_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002431003376841545,
                  "p50": 0.0,
                  "p90": 3.456044942140579e-05,
                  "p95": 6.902054883539677e-05,
                  "p99": 0.00013945088721811771
                },
                "candidate_energy": 19.67819241547477,
                "cvrmse_percent": 2.39829726169793,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.023534687434852118,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 19.68282470674785,
                "relative_energy_error_percent": 0.02353468743485212,
                "rms_normalized_rmse_percent": 0.8380820960322464,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007500046631321311,
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "reference": 0.0077431469690054655,
                  "rgb_channel": 0,
                  "sky_patch_index": 45
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007763504981994629,
                  "p50": 3.918105164757435e-07,
                  "p90": 7.023301441222429e-05,
                  "p95": 0.00011914253118447957,
                  "p99": 0.0002438077935948968
                },
                "candidate_energy": 17.105825600292146,
                "cvrmse_percent": 5.127891268028807,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.02625768634838687,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 17.110318374024008,
                "relative_energy_error_percent": 0.02625768634838687,
                "rms_normalized_rmse_percent": 0.5643192418104221,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.12069414928555489,
                  "global_sensor_index": 35,
                  "local_sensor_index": 35,
                  "reference": 0.12147049978375435,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 249.37604099977762,
            "full": 3755.054625100456
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 259.77341597899795,
            "full": 3860.612374963239
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 252.0070830360055,
            "full": 3822.029083967209
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 256.52691698633134,
            "full": 3879.3719169916585
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
    "/content/suite-vulkan-0.3.2/full_height_glazing/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 789.8560839239508,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2817.3257500166073,
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
        "identifier": "full_height_glazing_grid",
        "full_identifier": "full_height_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.03354333392336586,
            "cvrmse_percent": 1.7924127752189054,
            "rms_normalized_rmse_percent": 0.6263868005810274,
            "reference_energy": 19.680670154411928,
            "candidate_energy": 19.674068601503677,
            "relative_energy_error_percent": 0.03354333392336586,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.39651820063591e-06,
              "p95": 1.9963830709457397e-05,
              "p99": 0.00010360404849052429,
              "maximum": 0.00034218328073620796
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 131,
              "rgb_channel": 0,
              "reference": 0.005899978801608086,
              "candidate": 0.005557795520871878,
              "position": [
                0.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.280801204206024,
            "cvrmse_percent": 22.24070331854907,
            "rms_normalized_rmse_percent": 2.4472832494258148,
            "reference_energy": 17.107910305850226,
            "candidate_energy": 16.88879198463841,
            "relative_energy_error_percent": 1.280801204206024,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.531468683424464e-06,
              "p90": 7.861433550715446e-05,
              "p95": 0.00011869350855704372,
              "p99": 0.0002904576249420643,
              "maximum": 0.004635870456695557
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.1382702738046646,
              "candidate": 0.13363440334796906,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.6135596190341787,
            "cvrmse_percent": 10.322314905185458,
            "rms_normalized_rmse_percent": 2.4424680449373732,
            "reference_energy": 36.78858046026215,
            "candidate_energy": 36.56286058614209,
            "relative_energy_error_percent": 0.6135596190341787,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.531468683424464e-06,
              "p90": 7.548835128545761e-05,
              "p95": 0.00011282463092356883,
              "p99": 0.00027213338762521744,
              "maximum": 0.004635870456695557
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.1382702738046646,
              "candidate": 0.13363440334796906,
              "position": [
                2.5,
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
        "identifier": "full_height_glazing_grid",
        "full_identifier": "full_height_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.03354333392336586,
            "cvrmse_percent": 1.7924127752189054,
            "rms_normalized_rmse_percent": 0.6263868005810274,
            "reference_energy": 19.680670154411928,
            "candidate_energy": 19.674068601503677,
            "relative_energy_error_percent": 0.03354333392336586,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.39651820063591e-06,
              "p95": 1.9963830709457397e-05,
              "p99": 0.00010360404849052429,
              "maximum": 0.00034218328073620796
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 131,
              "rgb_channel": 0,
              "reference": 0.005899978801608086,
              "candidate": 0.005557795520871878,
              "position": [
                0.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 68.74620105492441,
            "cvrmse_percent": 359.1329394855229,
            "rms_normalized_rmse_percent": 29.76317600495111,
            "reference_energy": 10.008398339670684,
            "candidate_energy": 16.88879198463841,
            "relative_energy_error_percent": 68.74620105492441,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.501351732713374e-06,
              "p90": 0.0009124715234065661,
              "p95": 0.0011653506517177441,
              "p99": 0.001799614168703556,
              "maximum": 0.03169644996523857
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04838379845023155,
              "candidate": 0.08008024841547012,
              "position": [
                2.5,
                5.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 23.152602761617477,
            "cvrmse_percent": 121.06179081838728,
            "rms_normalized_rmse_percent": 29.76206876519169,
            "reference_energy": 29.689068494082612,
            "candidate_energy": 36.56286058614209,
            "relative_energy_error_percent": 23.152602761617477,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.4727938832947984e-06,
              "p90": 0.0009105256758630276,
              "p95": 0.0011635669099177902,
              "p99": 0.0017997203394770622,
              "maximum": 0.03169644996523857
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04838379845023155,
              "candidate": 0.08008024841547012,
              "position": [
                2.5,
                5.5,
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
      "bias_percent": 0.11467193581567567,
      "rms_normalized_error_percent": 0.24200850220356335,
      "absolute_error": {
        "p95": 0.23776807938807387,
        "p99": 0.3077014749697487,
        "maximum": 0.31297713314340037
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 41.90507306474095,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.24200850220356335
    },
    "overcast": {
      "bias_percent": 0.07541088206825464,
      "rms_normalized_error_percent": 0.1922152429689021,
      "absolute_error": {
        "p95": 0.12667417526245117,
        "p99": 0.1491396903991699,
        "maximum": 0.15195083618164062
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 27.075416564941406,
      "reference_fraction_of_uniform": 0.6461130976676941,
      "rms_normalized_to_uniform_percent": 0.1319632521672619
    },
    "horizon": {
      "bias_percent": 1.1398189035041062,
      "rms_normalized_error_percent": 1.9264226428995899,
      "absolute_error": {
        "p95": 0.1644660354020845,
        "p99": 0.18542261193180073,
        "maximum": 0.18989136174127896
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.8050126399850033,
      "reference_fraction_of_uniform": 0.0908007637668708,
      "rms_normalized_to_uniform_percent": 0.14250608348909796
    },
    "north": {
      "bias_percent": 10.966833072033605,
      "rms_normalized_error_percent": 171.86486652658985,
      "absolute_error": {
        "p95": 0.00027181077894056216,
        "p99": 0.0004268111646524628,
        "maximum": 0.0004914909950457513
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 4.838158201891929e-05,
      "reference_fraction_of_uniform": 1.1545519100764068e-06,
      "rms_normalized_to_uniform_percent": 0.0002234102904722409
    },
    "east": {
      "bias_percent": -0.08992195394056794,
      "rms_normalized_error_percent": 0.36063199726798273,
      "absolute_error": {
        "p95": 0.08884692192077637,
        "p99": 0.12104043960571288,
        "maximum": 0.12163925170898438
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.206242561340332,
      "reference_fraction_of_uniform": 0.1958293467760086,
      "rms_normalized_to_uniform_percent": 0.07697716210641177
    },
    "south": {
      "bias_percent": 0.15491625207240423,
      "rms_normalized_error_percent": 0.3245128750284108,
      "absolute_error": {
        "p95": 0.22806620597839355,
        "p99": 0.2889015197753906,
        "maximum": 0.302001953125
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 28.92231559753418,
      "reference_fraction_of_uniform": 0.6901865005493164,
      "rms_normalized_to_uniform_percent": 0.20930238613340413
    },
    "west": {
      "bias_percent": 0.1545686459067002,
      "rms_normalized_error_percent": 0.27743734731848635,
      "absolute_error": {
        "p95": 0.05826163291931152,
        "p99": 0.06259064674377442,
        "maximum": 0.0634307861328125
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.937900066375732,
      "reference_fraction_of_uniform": 0.1894257664680481,
      "rms_normalized_to_uniform_percent": 0.056777530643641924
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
        "identifier": "full_height_glazing_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.0056063430519074494,
          "cvrmse_percent": 0.9293144238085278,
          "absolute_error_percentiles_lux": {
            "p50": 6.11016845703125,
            "p90": 50.81814575195314,
            "p95": 75.81067504882796,
            "p99": 139.35113037109363
          },
          "maximum_absolute_error_lux": 472.380859375,
          "worst": {
            "sensor_index": 4,
            "position": [
              0.5,
              1.5,
              0.75
            ],
            "hour_of_year": 6081.5,
            "foton_lux": 25585.177734375,
            "radiance_lux": 26057.55859375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.04663622526636067,
            "maximum_error_percentage_points": 0.24232876712328277,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.02359433425315258,
            "maximum_error_percentage_points": 0.12036808793413911,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.015650684931507057,
            "maximum_error_percentage_points": 0.1086301369863012,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.151723744292238,
            "maximum_error_percentage_points": 0.4135616438356209,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.16029299847793027,
            "maximum_error_percentage_points": 0.4347945205479462,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
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
            "identifier": "full_height_glazing_grid",
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "full_height_glazing_grid",
            "maximum_error_percentage_points": 0.004757598458894563,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "full_height_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "full_height_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "full_height_glazing_grid",
            "maximum_error_percentage_points": 0.004794520547953596,
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
      "study_preparation_seconds": 0.3675553610000861,
      "weather_seconds": 0.22845819299982395,
      "metric_reduction_seconds": 0.1646549080001023,
      "write_seconds": 0.012328400000114925,
      "total_seconds": 0.4058068060003279,
      "cold_end_to_end_seconds": 0.773362167000414,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0013909939998484333,
      "engine_upload_seconds": 0.013700354,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.018921218,
      "engine_annual_reduction_seconds": 0.005965651,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.018921218
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3675553610000861,
      "weather_seconds": 0.2271944600001916,
      "metric_reduction_seconds": 0.15036321299976407,
      "write_seconds": 0.011500613999942289,
      "total_seconds": 0.38933818600025916,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.38933818600025916,
      "raw_export_seconds": 0.001491126000018994,
      "engine_upload_seconds": 0.015188034,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 6.400000000000002e-08,
      "engine_annual_reduction_seconds": 0.005906635,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013670662000095035,
      "full": 0.027464060000056634
    }
  },
  "elapsed_seconds": 2.8606031159997656,
  "result_class": "passed"
}
```
