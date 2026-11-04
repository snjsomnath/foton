# Foton report

Status: **passed**

```json
{
  "scene": "plan_j_small_center",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_j_small_center",
    "category": "form",
    "question": "How does a small center opening illuminate a J-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "j",
    "window_profile": "small_center"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 47,
    "floor_area": 63.0,
    "aperture_area": 1.44
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "10c685ae44a1f5160c98a333b0a6d067c420ae94a7326800dafe76930bd54233",
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
      "scene_fingerprint": 13205422065723597276,
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
      "scene_fingerprint": 13205422065723597276,
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
    "model_sha256": "dfdd5ab8ea952243a7bbae07b696295e3cdf49fcdc8567e6c84d21b26535acdd",
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
          "maximum": 0.00043346919119358063,
          "p95": 0.0,
          "p99": 4.7317633288912475e-05
        },
        "bias_percent": 0.051826255602459396,
        "identifier": "plan_j_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.2860058758761261,
        "worst_index": [
          18,
          132,
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
          "maximum": 0.0004658009856939316,
          "p95": 1.5202676877379417e-05,
          "p99": 8.782395161688328e-05
        },
        "bias_percent": 0.0695595365709805,
        "identifier": "plan_j_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3408492196044912,
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
          "maximum": 0.00029087066650390625,
          "p95": 1.3778575521428138e-05,
          "p99": 6.837630644440651e-05
        },
        "bias_percent": -0.044638483396629604,
        "identifier": "plan_j_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0819465688920515,
        "worst_index": [
          20,
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
            "identifier": "plan_j_small_center_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005483548156917095,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00012423517182469368
                },
                "candidate_energy": 2.6478254704015853,
                "cvrmse_percent": 20.53317501353546,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.05282697013918514,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.649224975688412,
                "relative_energy_error_percent": 0.052826970139185137,
                "rms_normalized_rmse_percent": 2.3933180601210777,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.012797205243259668,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.013345560058951378,
                  "rgb_channel": 0,
                  "sky_patch_index": 74
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007774750702083111,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.177929470941308e-05,
                  "p99": 0.00022374396212399006
                },
                "candidate_energy": 0.6775554017129366,
                "cvrmse_percent": 131.1775614058476,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.9960292765805091,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6708733071648112,
                "relative_energy_error_percent": 0.9960292765805091,
                "rms_normalized_rmse_percent": 3.545900767652978,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00031751999631524086,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": -0.0004599550738930702,
                  "rgb_channel": 0,
                  "sky_patch_index": 74
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.17804104834795,
            "full": 267.7702499786392
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.08491603471339,
            "full": 267.11562497075647
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.62479194719344,
            "full": 272.87904103286564
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.23024999164045,
            "full": 280.20458295941353
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
            "identifier": "plan_j_small_center_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003996801096946001,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 8.754088776186109e-05
                },
                "candidate_energy": 2.6514487108779576,
                "cvrmse_percent": 13.895181401380109,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.041335981747977715,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.652545166463824,
                "relative_energy_error_percent": 0.04133598174797772,
                "rms_normalized_rmse_percent": 1.6213721612529288,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007508092559874058,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.007108412450179458,
                  "rgb_channel": 0,
                  "sky_patch_index": 49
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000523074995726347,
                  "p50": 5.000000058430487e-08,
                  "p90": 1.0018575267167762e-05,
                  "p95": 2.0564154510793742e-05,
                  "p99": 0.00014988216571509838
                },
                "candidate_energy": 1.3220539859895517,
                "cvrmse_percent": 48.43293611568577,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.703380121858732,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3128198719742734,
                "relative_energy_error_percent": 0.703380121858732,
                "rms_normalized_rmse_percent": 2.3662436278199555,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00048730988055467606,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": -3.5765115171670914e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 74
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.3528750082478,
            "full": 3129.1845419909805
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.78212507534772,
            "full": 3140.7122920500115
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 174.70416706055403,
            "full": 3081.215125042945
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.65754200704396,
            "full": 3131.1495419358835
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
            "identifier": "plan_j_small_center_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00033051008358597755,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00010289531201124191
                },
                "candidate_energy": 2.65426165648023,
                "cvrmse_percent": 14.563703500050094,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.17832829768588,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.6495367826391885,
                "relative_energy_error_percent": 0.17832829768588,
                "rms_normalized_rmse_percent": 1.6983519797943458,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.006369198439642787,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.0066997085232287645,
                  "rgb_channel": 0,
                  "sky_patch_index": 49
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005543970037251711,
                  "p50": 5.000000058430487e-08,
                  "p90": 1.0736506737885065e-05,
                  "p95": 2.160624717362225e-05,
                  "p99": 0.00016098003834486008
                },
                "candidate_energy": 1.3180375379617644,
                "cvrmse_percent": 49.329922863766654,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.34149688301235526,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3225540187118199,
                "relative_energy_error_percent": 0.3414968830123553,
                "rms_normalized_rmse_percent": 2.4245181999154015,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -3.897445276379585e-05,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.0005154225509613752,
                  "rgb_channel": 0,
                  "sky_patch_index": 76
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.1032089414075,
            "full": 3342.9987500421703
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.7361659836024,
            "full": 3326.2081670109183
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 165.58645793702453,
            "full": 3302.0516249816865
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 191.90249999519438,
            "full": 3324.7682499932125
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
            "identifier": "plan_j_small_center_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00017340504564344883,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.247537046670914e-05
                },
                "candidate_energy": 2.651176576184298,
                "cvrmse_percent": 7.505686108156821,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.054805669312977874,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.6497243770045316,
                "relative_energy_error_percent": 0.05480566931297788,
                "rms_normalized_rmse_percent": 0.8759256681226824,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0063849755097180605,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.006211570464074612,
                  "rgb_channel": 0,
                  "sky_patch_index": 76
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00039314990863204,
                  "p50": 5.000000058430487e-08,
                  "p90": 7.3553969741624314e-06,
                  "p95": 1.4986659152782522e-05,
                  "p99": 8.389761205762625e-05
                },
                "candidate_energy": 1.3212227524046014,
                "cvrmse_percent": 27.929187939000723,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.18978104495894058,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.318720071672498,
                "relative_energy_error_percent": 0.1897810449589406,
                "rms_normalized_rmse_percent": 1.3697273905858185,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.011086125392466784,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.011479275301098824,
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
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 226.697540958412,
            "full": 5891.79562497884
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 244.498832966201,
            "full": 5851.649957941845
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 226.3607910135761,
            "full": 5928.0723329866305
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 230.65704200416803,
            "full": 5795.968084014021
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
    "/Users/ssanjay/GitHub/foton-0.3.3/validation/results/2026-11-04-architectural-v4-metal-0.3.3-release/plan_j_small_center/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1392.4251249991357,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_small_center/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4730.548624997027,
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
        "identifier": "plan_j_small_center_grid",
        "full_identifier": "plan_j_small_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": 0.0005996304312147826,
            "cvrmse_percent": 6.37111989458525,
            "rms_normalized_rmse_percent": 0.7429412897039955,
            "reference_energy": 2.649741546666746,
            "candidate_energy": 2.6497574353234086,
            "relative_energy_error_percent": 0.0005996304312147826,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.421766450628638e-05,
              "maximum": 0.0002165650948882103
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 121,
              "rgb_channel": 0,
              "reference": 0.006629771552979946,
              "candidate": 0.006413206458091736,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.3553888594678844,
            "cvrmse_percent": 32.5169995838364,
            "rms_normalized_rmse_percent": 1.5964030262660982,
            "reference_energy": 1.3206803242511302,
            "candidate_energy": 1.3159867735095574,
            "relative_energy_error_percent": 0.3553888594678844,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.0217620882713163e-07,
              "p90": 1.6856123693287373e-05,
              "p95": 2.8815644327551126e-05,
              "p99": 8.376722689718008e-05,
              "maximum": 0.0004614349454641342
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015589434653520584,
              "candidate": 0.01512799970805645,
              "position": [
                4.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.11781272209819654,
            "cvrmse_percent": 10.489868821989969,
            "rms_normalized_rmse_percent": 1.548249972736803,
            "reference_energy": 3.9704218709178765,
            "candidate_energy": 3.965744208832966,
            "relative_energy_error_percent": 0.11781272209819656,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.0217620882713163e-07,
              "p90": 1.6650596535328077e-05,
              "p95": 2.784037496894598e-05,
              "p99": 7.445644587278366e-05,
              "maximum": 0.0004614349454641342
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015589434653520584,
              "candidate": 0.01512799970805645,
              "position": [
                4.5,
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
        "identifier": "plan_j_small_center_grid",
        "full_identifier": "plan_j_small_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": 0.0005996304312147826,
            "cvrmse_percent": 6.37111989458525,
            "rms_normalized_rmse_percent": 0.7429412897039955,
            "reference_energy": 2.649741546666746,
            "candidate_energy": 2.6497574353234086,
            "relative_energy_error_percent": 0.0005996304312147826,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.421766450628638e-05,
              "maximum": 0.0002165650948882103
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 121,
              "rgb_channel": 0,
              "reference": 0.006629771552979946,
              "candidate": 0.006413206458091736,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 95.54095107940122,
            "cvrmse_percent": 623.7841420090963,
            "rms_normalized_rmse_percent": 16.906054163458126,
            "reference_energy": 0.6729980427348892,
            "candidate_energy": 1.3159867735095574,
            "relative_energy_error_percent": 95.54095107940122,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.959000165807083e-05,
              "p95": 0.00011105999874416739,
              "p99": 0.00024695100728422403,
              "maximum": 0.004617337137460709
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.013378672301769257,
              "candidate": 0.017996009439229965,
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
            "nmbe_percent": 19.351640480111293,
            "cvrmse_percent": 126.34416005985302,
            "rms_normalized_rmse_percent": 16.906184475264872,
            "reference_energy": 3.3227395894016354,
            "candidate_energy": 3.965744208832966,
            "relative_energy_error_percent": 19.351640480111293,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.985606205489603e-05,
              "p95": 0.0001116599960369058,
              "p99": 0.0002462156116962433,
              "maximum": 0.004617337137460709
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.013378672301769257,
              "candidate": 0.017996009439229965,
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
      "bias_percent": 0.11065324362278038,
      "rms_normalized_error_percent": 0.2680343216987095,
      "absolute_error": {
        "p95": 0.06324364623262833,
        "p99": 0.07215084435931773,
        "maximum": 0.07301338359365417
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.8981558254079967,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2680343216987095
    },
    "overcast": {
      "bias_percent": 0.05028326376472079,
      "rms_normalized_error_percent": 0.20684806236139291,
      "absolute_error": {
        "p95": 0.03296208381652831,
        "p99": 0.04384520530700683,
        "maximum": 0.0483393669128418
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.5807411670684814,
      "reference_fraction_of_uniform": 0.6620415449142456,
      "rms_normalized_to_uniform_percent": 0.15080038520799555
    },
    "horizon": {
      "bias_percent": 1.1786664422406434,
      "rms_normalized_error_percent": 3.6765211539947678,
      "absolute_error": {
        "p95": 0.02838036675808345,
        "p99": 0.03785658681808736,
        "maximum": 0.04384515864280969
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.2789330503404766,
      "reference_fraction_of_uniform": 0.07155513089610326,
      "rms_normalized_to_uniform_percent": 0.12140246140724834
    },
    "north": {
      "bias_percent": -54.08236239957194,
      "rms_normalized_error_percent": 114.07749064002715,
      "absolute_error": {
        "p95": 0.00010816527150154766,
        "p99": 0.00018187914276495573,
        "maximum": 0.00019770774815697223
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.2498300748120528e-05,
      "reference_fraction_of_uniform": 3.206208475603489e-06,
      "rms_normalized_to_uniform_percent": 0.00040583966680697635
    },
    "east": {
      "bias_percent": 0.20300375046341007,
      "rms_normalized_error_percent": 0.4926160585720946,
      "absolute_error": {
        "p95": 0.022645866870880115,
        "p99": 0.035526596307754496,
        "maximum": 0.04469102621078491
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.8997640609741211,
      "reference_fraction_of_uniform": 0.23081786930561066,
      "rms_normalized_to_uniform_percent": 0.10849538551242915
    },
    "south": {
      "bias_percent": 0.18071782833488048,
      "rms_normalized_error_percent": 0.3128666012207831,
      "absolute_error": {
        "p95": 0.04619885087013242,
        "p99": 0.05706548690795898,
        "maximum": 0.06207752227783203
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.4988296031951904,
      "reference_fraction_of_uniform": 0.641028642654419,
      "rms_normalized_to_uniform_percent": 0.2029937858551451
    },
    "west": {
      "bias_percent": -0.02367908030125372,
      "rms_normalized_error_percent": 0.4749412542391847,
      "absolute_error": {
        "p95": 0.022024798393249494,
        "p99": 0.027798376083374023,
        "maximum": 0.028768539428710938
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.8342487215995789,
      "reference_fraction_of_uniform": 0.21401111781597137,
      "rms_normalized_to_uniform_percent": 0.09850202506240804
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
        "identifier": "plan_j_small_center_grid",
        "sensor_count": 47,
        "illuminance": {
          "nmbe_percent": 0.10561762494618031,
          "cvrmse_percent": 2.62453650362203,
          "absolute_error_percentiles_lux": {
            "p50": 0.9064416885375977,
            "p90": 11.383594512939457,
            "p95": 18.77465209960937,
            "p99": 39.13364013671877
          },
          "maximum_absolute_error_lux": 193.9404296875,
          "worst": {
            "sensor_index": 21,
            "position": [
              6.5,
              1.5,
              0.75
            ],
            "hour_of_year": 6086.5,
            "foton_lux": 6180.70654296875,
            "radiance_lux": 6374.64697265625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.32371320314777086,
            "maximum_error_percentage_points": 3.397123287671233,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.37577800137405226,
            "maximum_error_percentage_points": 1.3214528712127702,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.4894141649664823,
            "maximum_error_percentage_points": 2.683561643835617,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.4912940833576214,
            "maximum_error_percentage_points": 2.683561643835617,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.00927134946079877,
            "maximum_error_percentage_points": 0.08671232876712764,
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
      "maximum_error_percentage_points": 0.004977391909243067,
      "metrics": {
        "da": [
          {
            "identifier": "plan_j_small_center_grid",
            "maximum_error_percentage_points": 0.004520547945205511,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_j_small_center_grid",
            "maximum_error_percentage_points": 0.004977391909243067,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_j_small_center_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_j_small_center_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_j_small_center_grid",
            "maximum_error_percentage_points": 0.004794520547945158,
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
      "study_preparation_seconds": 0.006178334006108344,
      "weather_seconds": 0.07452770799864084,
      "metric_reduction_seconds": 0.038833208032883704,
      "write_seconds": 0.011374166002497077,
      "total_seconds": 0.12489979097153991,
      "cold_end_to_end_seconds": 0.13107812497764826,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.002590458025224507,
      "engine_upload_seconds": 0.000265958,
      "engine_acceleration_structure_seconds": 0.002913042,
      "engine_tracing_seconds": 0.014916624873876572,
      "engine_annual_reduction_seconds": 0.0004493333399295807,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.014916624873876572
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006178334006108344,
      "weather_seconds": 0.07403675001114607,
      "metric_reduction_seconds": 0.013634209055453539,
      "write_seconds": 0.009843499981798232,
      "total_seconds": 0.09766774997115135,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.09766774997115135,
      "raw_export_seconds": 0.0016300830757245421,
      "engine_upload_seconds": 5.1667e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0004701249999925494,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.015599749982357025,
      "full": 0.023096291930414736
    }
  },
  "elapsed_seconds": 0.728631709003821,
  "result_class": "passed"
}
```
