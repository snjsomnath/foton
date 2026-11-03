# Foton report

Status: **passed**

```json
{
  "scene": "narrow_corridor",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "narrow_corridor",
    "category": "form",
    "question": "How far does end-window light travel down a narrow corridor?",
    "interactions": [
      "deep_plan",
      "end_lighting"
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
    "sensors": 45,
    "floor_area": 45.0,
    "aperture_area": 2.25
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "0869e36331f5eac8811a54081b274717729df90e070f6e2425a13c1c8432a316",
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
      "scene_fingerprint": 5183289922802089606,
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
      "scene_fingerprint": 5183289922802089606,
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
    "model_sha256": "55d7393c4716e2de0b6677f76405ebedef14938aceaeb5d992fc1fe2ab6611ba",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "aacc5410b5d2cd34f7c6c118153bdac841d4f624754306ee7858e0232dee3360",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0002872161567211151,
          "p95": 0.0,
          "p99": 4.209324251860373e-05
        },
        "bias_percent": 0.07981862569839938,
        "identifier": "narrow_corridor_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9681082596260756,
        "worst_index": [
          28,
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
          "maximum": 0.0004007341340184212,
          "p95": 2.4460925487801433e-05,
          "p99": 0.00011668498395010829
        },
        "bias_percent": 0.023750568634087983,
        "identifier": "narrow_corridor_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.162115904126053,
        "worst_index": [
          29,
          45,
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
          "maximum": 0.0003727581351995468,
          "p95": 1.82838921318762e-05,
          "p99": 9.346557082608336e-05
        },
        "bias_percent": 0.0020678572646373457,
        "identifier": "narrow_corridor_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8866237077396546,
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
            "identifier": "narrow_corridor_grid",
            "sensor_count": 45,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006402297876775265,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00023212829270050845
                },
                "candidate_energy": 3.889556817654011,
                "cvrmse_percent": 21.018726434921437,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.10524385990258403,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8936546500990517,
                "relative_energy_error_percent": 0.10524385990258403,
                "rms_normalized_rmse_percent": 3.042488179413563,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.012796205002814531,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.012155975215137005,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009480370208621025,
                  "p50": 0.0,
                  "p90": 5.571912606683344e-06,
                  "p95": 3.174154699081555e-05,
                  "p99": 0.000280072680616284
                },
                "candidate_energy": 1.3302153232591962,
                "cvrmse_percent": 81.41909183312357,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.310469841845276,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3343581027504552,
                "relative_energy_error_percent": 0.310469841845276,
                "rms_normalized_rmse_percent": 3.2542244923173276,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0006076670251786709,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.0003403699956834316,
                  "rgb_channel": 0,
                  "sky_patch_index": 72
                }
              }
            },
            "start_sensor_index": 0
          }
        ],
        "half_run_count": 4,
        "oracle_stable": true,
        "run_count": 8,
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 117.77608294505626,
            "full": 252.43583298288286
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 117.90779209695756,
            "full": 248.413166962564
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 106.14312498364598,
            "full": 262.03195797279477
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.19554194435477,
            "full": 264.4777500536293
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 107.15362499468029,
            "full": 245.7404169254005
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 111.29245802294463,
            "full": 244.5699580712244
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 112.73370799608529,
            "full": 249.22112503554672
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.28941697441041,
            "full": 244.69591700471938
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
            "identifier": "narrow_corridor_grid",
            "sensor_count": 45,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00032096030190587044,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00011761553752876353
                },
                "candidate_energy": 3.8964804056859066,
                "cvrmse_percent": 11.270392213233219,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.07830966153518841,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8934314726775483,
                "relative_energy_error_percent": 0.07830966153518841,
                "rms_normalized_rmse_percent": 1.6323858795178998,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013403845019638538,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.013724805321544409,
                  "rgb_channel": 0,
                  "sky_patch_index": 73
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005226451903581619,
                  "p50": 5.2988447407642525e-08,
                  "p90": 1.3327756460057612e-05,
                  "p95": 3.9995560655370355e-05,
                  "p99": 0.00019026489200768963
                },
                "candidate_energy": 2.4542921923071113,
                "cvrmse_percent": 28.468389119556036,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.06349932499534289,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.455851641522365,
                "relative_energy_error_percent": 0.06349932499534289,
                "rms_normalized_rmse_percent": 1.7700114802103804,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0007536248303949833,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.00023097964003682137,
                  "rgb_channel": 0,
                  "sky_patch_index": 73
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.5757909938693,
            "full": 2816.909792018123
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 163.37641701102257,
            "full": 2938.721250044182
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.45045796129853,
            "full": 2906.9610000588
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 160.61316605191678,
            "full": 2888.535249978304
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
            "identifier": "narrow_corridor_grid",
            "sensor_count": 45,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00038132723420858383,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0001358289679046718
                },
                "candidate_energy": 3.8900810552013354,
                "cvrmse_percent": 11.94846466071262,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.09496828664888647,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8937789103183604,
                "relative_energy_error_percent": 0.09496828664888647,
                "rms_normalized_rmse_percent": 1.731454862721388,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.009941396303474903,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.00956006906926632,
                  "rgb_channel": 0,
                  "sky_patch_index": 70
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006737280637025833,
                  "p50": 5.9461054746634545e-08,
                  "p90": 1.414862981619083e-05,
                  "p95": 3.6248849937692285e-05,
                  "p99": 0.00019556965562514948
                },
                "candidate_energy": 2.4575912538456883,
                "cvrmse_percent": 30.810243862002004,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.16369585842744408,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4616208251867064,
                "relative_energy_error_percent": 0.1636958584274441,
                "rms_normalized_rmse_percent": 1.9198322083961918,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03774626553058624,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.038419993594288826,
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.1651670075953,
            "full": 3019.579333020374
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.7176250498742,
            "full": 3112.878500018269
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.29891695082188,
            "full": 3102.696374990046
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.7210420370102,
            "full": 3049.7794579714537
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
            "identifier": "narrow_corridor_grid",
            "sensor_count": 45,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001987200230360031,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.981761078350246e-05
                },
                "candidate_energy": 3.895506567616394,
                "cvrmse_percent": 6.333315465995742,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.02363340734874727,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.896427426182072,
                "relative_energy_error_percent": 0.023633407348747266,
                "rms_normalized_rmse_percent": 0.918089338611781,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.010540639981627464,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.010739360004663467,
                  "rgb_channel": 0,
                  "sky_patch_index": 95
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00044858455657958984,
                  "p50": 5.000000058430487e-08,
                  "p90": 9.610177949070944e-06,
                  "p95": 2.5825807824730873e-05,
                  "p99": 0.00011308185567031613
                },
                "candidate_energy": 2.4567098204276903,
                "cvrmse_percent": 17.45341596086442,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.08224713210908362,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4546909075540846,
                "relative_energy_error_percent": 0.08224713210908362,
                "rms_normalized_rmse_percent": 1.0863847717281276,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.029916689731180668,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.029468105174601078,
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 220.0014169793576,
            "full": 5430.176583002321
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 213.2679169299081,
            "full": 5469.378708046861
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 258.4439170313999,
            "full": 5437.27187498007
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
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "45",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 212.02958305366337,
            "full": 5356.374750030227
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/narrow_corridor/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1312.097332905978,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/narrow_corridor/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4918.543874984607,
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
      45,
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
        "identifier": "narrow_corridor_grid",
        "full_identifier": "narrow_corridor_grid",
        "start_sensor_index": 0,
        "sensor_count": 45,
        "stages": {
          "direct": {
            "nmbe_percent": 0.016663876710048063,
            "cvrmse_percent": 4.520869877219876,
            "rms_normalized_rmse_percent": 0.6550319683737041,
            "reference_energy": 3.8941401394013155,
            "candidate_energy": 3.894789054113062,
            "relative_energy_error_percent": 0.016663876710048063,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.8954707086086264e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 29,
              "local_sensor_index": 29,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -2.10434393282289,
            "cvrmse_percent": 32.08931890637765,
            "rms_normalized_rmse_percent": 1.9989963768785943,
            "reference_energy": 2.457527225374683,
            "candidate_energy": 2.4058124003100403,
            "relative_energy_error_percent": 2.1043439328228906,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.2499999968440534e-07,
              "p90": 2.130178763763991e-05,
              "p95": 3.982191992690787e-05,
              "p99": 0.00010276477842126025,
              "maximum": 0.0011138413101434708
            },
            "worst": {
              "global_sensor_index": 42,
              "local_sensor_index": 42,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02973458170890808,
              "candidate": 0.02862074039876461,
              "position": [
                2.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.8039764587813465,
            "cvrmse_percent": 12.353422569542518,
            "rms_normalized_rmse_percent": 1.9889699119997857,
            "reference_energy": 6.351667364775999,
            "candidate_energy": 6.300601454423102,
            "relative_energy_error_percent": 0.8039764587813464,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.2499999968440534e-07,
              "p90": 2.10433836400626e-05,
              "p95": 3.859773278236389e-05,
              "p99": 9.91133623756466e-05,
              "maximum": 0.0011138413101434708
            },
            "worst": {
              "global_sensor_index": 42,
              "local_sensor_index": 42,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02973458170890808,
              "candidate": 0.02862074039876461,
              "position": [
                2.5,
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
      45,
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
        "identifier": "narrow_corridor_grid",
        "full_identifier": "narrow_corridor_grid",
        "start_sensor_index": 0,
        "sensor_count": 45,
        "stages": {
          "direct": {
            "nmbe_percent": 0.016663876710048063,
            "cvrmse_percent": 4.520869877219876,
            "rms_normalized_rmse_percent": 0.6550319683737041,
            "reference_energy": 3.8941401394013155,
            "candidate_energy": 3.894789054113062,
            "relative_energy_error_percent": 0.016663876710048063,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.8954707086086264e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 29,
              "local_sensor_index": 29,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 80.92185171053683,
            "cvrmse_percent": 631.6342507095051,
            "rms_normalized_rmse_percent": 25.165794091695993,
            "reference_energy": 1.3297522535637007,
            "candidate_energy": 2.4058124003100403,
            "relative_energy_error_percent": 80.92185171053683,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00011462714410299695,
              "p95": 0.00020896000205539167,
              "p99": 0.0003867233695927997,
              "maximum": 0.010505326092243195
            },
            "worst": {
              "global_sensor_index": 43,
              "local_sensor_index": 43,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025278892368078232,
              "candidate": 0.035784218460321426,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.61124120604175,
            "cvrmse_percent": 160.80576081458742,
            "rms_normalized_rmse_percent": 25.169237422518663,
            "reference_energy": 5.223892392965016,
            "candidate_energy": 6.300601454423102,
            "relative_energy_error_percent": 20.61124120604175,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00011414458376748392,
              "p95": 0.00020944990683346987,
              "p99": 0.00037541771074756867,
              "maximum": 0.010505326092243195
            },
            "worst": {
              "global_sensor_index": 43,
              "local_sensor_index": 43,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025278892368078232,
              "candidate": 0.035784218460321426,
              "position": [
                2.5,
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
      "bias_percent": -0.25910475617255735,
      "rms_normalized_error_percent": 0.2166549671835596,
      "absolute_error": {
        "p95": 0.07154312017239127,
        "p99": 0.10810427484564177,
        "maximum": 0.11588790128702087
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.338248752039419,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2166549671835596
    },
    "overcast": {
      "bias_percent": -0.22413157255858399,
      "rms_normalized_error_percent": 0.1834229188501937,
      "absolute_error": {
        "p95": 0.04326572418212891,
        "p99": 0.06799472808837892,
        "maximum": 0.0698699951171875
      },
      "worst_index": [
        43
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.068698406219482,
      "reference_fraction_of_uniform": 0.6419278383255005,
      "rms_normalized_to_uniform_percent": 0.1287164509673788
    },
    "horizon": {
      "bias_percent": 0.0648695702405435,
      "rms_normalized_error_percent": 1.5935015198493072,
      "absolute_error": {
        "p95": 0.025503950735540105,
        "p99": 0.032775525527882175,
        "maximum": 0.035313273745239515
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.6407610617124805,
      "reference_fraction_of_uniform": 0.1010943380072148,
      "rms_normalized_to_uniform_percent": 0.09064172931787529
    },
    "north": {
      "bias_percent": -94.69732935555584,
      "rms_normalized_error_percent": 100.55171068613636,
      "absolute_error": {
        "p95": 4.976229174644684e-05,
        "p99": 0.00012592368409968934,
        "maximum": 0.0001657224929658696
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.4956969607737847e-05,
      "reference_fraction_of_uniform": 2.3597954168508295e-06,
      "rms_normalized_to_uniform_percent": 0.0002103146990583229
    },
    "east": {
      "bias_percent": -0.3068048146062537,
      "rms_normalized_error_percent": 0.3053627725686483,
      "absolute_error": {
        "p95": 0.023828676342964154,
        "p99": 0.03553750038146974,
        "maximum": 0.037866950035095215
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.2506612539291382,
      "reference_fraction_of_uniform": 0.19731968641281128,
      "rms_normalized_to_uniform_percent": 0.07388755005896913
    },
    "south": {
      "bias_percent": -0.3078843799970744,
      "rms_normalized_error_percent": 0.2619491991422603,
      "absolute_error": {
        "p95": 0.0526261806488037,
        "p99": 0.07610796928405769,
        "maximum": 0.09211540222167969
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.424683570861816,
      "reference_fraction_of_uniform": 0.6980924606323242,
      "rms_normalized_to_uniform_percent": 0.16906741628976513
    },
    "west": {
      "bias_percent": -0.2855063770998584,
      "rms_normalized_error_percent": 0.4376711005870846,
      "absolute_error": {
        "p95": 0.027603602409362788,
        "p99": 0.05743075132370001,
        "maximum": 0.0688161849975586
      },
      "worst_index": [
        43
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.196332573890686,
      "reference_fraction_of_uniform": 0.18874812126159668,
      "rms_normalized_to_uniform_percent": 0.10010130897580853
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
        "identifier": "narrow_corridor_grid",
        "sensor_count": 45,
        "illuminance": {
          "nmbe_percent": -0.3288661846960232,
          "cvrmse_percent": 2.372340085391576,
          "absolute_error_percentiles_lux": {
            "p50": 1.2170677185058594,
            "p90": 13.756253051757815,
            "p95": 23.72403564453121,
            "p99": 53.892770996093944
          },
          "maximum_absolute_error_lux": 432.150390625,
          "worst": {
            "sensor_index": 43,
            "position": [
              2.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5150.5,
            "foton_lux": 4038.36474609375,
            "radiance_lux": 4470.51513671875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.23837747336377488,
            "maximum_error_percentage_points": 1.7005479452054786,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.3840206243176939,
            "maximum_error_percentage_points": 1.9905560772331725,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.5767153729071528,
            "maximum_error_percentage_points": 3.0184931506849324,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.5818203957382034,
            "maximum_error_percentage_points": 3.0184931506849324,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.014602739726027478,
            "maximum_error_percentage_points": 0.16534246575342593,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 26.666666666666668,
          "radiance_percent": 26.666666666666668,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.2222222222222223,
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
      "maximum_error_percentage_points": 0.004909032534246904,
      "metrics": {
        "da": [
          {
            "identifier": "narrow_corridor_grid",
            "maximum_error_percentage_points": 0.0046575342465753344,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "narrow_corridor_grid",
            "maximum_error_percentage_points": 0.004909032534246904,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "narrow_corridor_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "narrow_corridor_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "narrow_corridor_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
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
      "study_preparation_seconds": 0.005828666966408491,
      "weather_seconds": 0.09047716704662889,
      "metric_reduction_seconds": 0.039279457996599376,
      "write_seconds": 0.04260995797812939,
      "total_seconds": 0.17266612499952316,
      "cold_end_to_end_seconds": 0.17849479196593165,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.01696745806839317,
      "engine_upload_seconds": 0.00029120799999999994,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.02000654162839055,
      "engine_annual_reduction_seconds": 0.0004153749905526638,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.02000654162839055
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.005828666966408491,
      "weather_seconds": 0.09273804200347513,
      "metric_reduction_seconds": 0.012179624987766147,
      "write_seconds": 0.030702040996402502,
      "total_seconds": 0.1357645420357585,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1357645420357585,
      "raw_export_seconds": 0.016793624963611364,
      "engine_upload_seconds": 4.9625e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0004451250424608588,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.011616083094850183,
      "full": 0.026608083047904074
    }
  },
  "elapsed_seconds": 0.7112213339423761,
  "result_class": "passed"
}
```
