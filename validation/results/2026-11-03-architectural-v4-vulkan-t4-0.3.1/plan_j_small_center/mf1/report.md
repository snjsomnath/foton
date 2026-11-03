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
  "model_sha256": "2ae2b671b0b88c8331f9a13353ed5db1e5153428c7d4bb29df07283e5b713035",
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 13205422065723597276,
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 13205422065723597276,
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
    "/content/suite-vulkan-0.3.1/plan_j_small_center/mf1/oracle/scene.rad"
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
            "nmbe_percent": 0.0005972326320423924,
            "cvrmse_percent": 6.37112072070404,
            "rms_normalized_rmse_percent": 0.7429413860383558,
            "reference_energy": 2.649741546666746,
            "candidate_energy": 2.6497573717879277,
            "relative_energy_error_percent": 0.0005972326320423924,
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
            "nmbe_percent": -0.35440042694537977,
            "cvrmse_percent": 32.520288100321295,
            "rms_normalized_rmse_percent": 1.5965644740545044,
            "reference_energy": 1.3206803242511302,
            "candidate_energy": 1.3159998275434006,
            "relative_energy_error_percent": 0.35440042694537977,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.0217620882713163e-07,
              "p90": 1.6856123693287373e-05,
              "p95": 2.8815644327551126e-05,
              "p99": 8.376722689718008e-05,
              "maximum": 0.000461445190012455
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015589434653520584,
              "candidate": 0.015127989463508129,
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
            "nmbe_percent": -0.11748554028264456,
            "cvrmse_percent": 10.48984350432954,
            "rms_normalized_rmse_percent": 1.5482462359820608,
            "reference_energy": 3.9704218709178765,
            "candidate_energy": 3.9657571993313283,
            "relative_energy_error_percent": 0.11748554028264459,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.0217620882713163e-07,
              "p90": 1.6650596535328077e-05,
              "p95": 2.784037496894598e-05,
              "p99": 7.445644587278366e-05,
              "maximum": 0.000461445190012455
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015589434653520584,
              "candidate": 0.015127989463508129,
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
            "nmbe_percent": 0.0005972326320423924,
            "cvrmse_percent": 6.37112072070404,
            "rms_normalized_rmse_percent": 0.7429413860383558,
            "reference_energy": 2.649741546666746,
            "candidate_energy": 2.6497573717879277,
            "relative_energy_error_percent": 0.0005972326320423924,
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
            "nmbe_percent": 95.54289076317657,
            "cvrmse_percent": 623.7854253855053,
            "rms_normalized_rmse_percent": 16.90608894605297,
            "reference_energy": 0.6729980427348892,
            "candidate_energy": 1.3159998275434006,
            "relative_energy_error_percent": 95.54289076317656,
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
            "nmbe_percent": 19.352031437573135,
            "cvrmse_percent": 126.34428182295471,
            "rms_normalized_rmse_percent": 16.9062007684553,
            "reference_energy": 3.3227395894016354,
            "candidate_energy": 3.9657571993313283,
            "relative_energy_error_percent": 19.35203143757313,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.985606205489603e-05,
              "p95": 0.0001116599960369058,
              "p99": 0.00024621468037366867,
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
      "bias_percent": 0.11107420945256515,
      "rms_normalized_error_percent": 0.26800703631503486,
      "absolute_error": {
        "p95": 0.06324327049125499,
        "p99": 0.07215065353219147,
        "maximum": 0.07301305018016535
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.8981558254079967,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.26800703631503486
    },
    "overcast": {
      "bias_percent": 0.0506160551450217,
      "rms_normalized_error_percent": 0.20676191817078413,
      "absolute_error": {
        "p95": 0.03296204209327697,
        "p99": 0.04384476661682128,
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
      "rms_normalized_to_uniform_percent": 0.1507375798111592
    },
    "horizon": {
      "bias_percent": 1.1786646291971157,
      "rms_normalized_error_percent": 3.676522237595906,
      "absolute_error": {
        "p95": 0.028380354255077754,
        "p99": 0.037856608125292894,
        "maximum": 0.04384520031949535
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.2789330503404766,
      "reference_fraction_of_uniform": 0.07155513089610326,
      "rms_normalized_to_uniform_percent": 0.12140249718885814
    },
    "north": {
      "bias_percent": -54.082362444005476,
      "rms_normalized_error_percent": 114.07749064563122,
      "absolute_error": {
        "p95": 0.00010816527153565371,
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
      "bias_percent": 0.20299539734068933,
      "rms_normalized_error_percent": 0.49261453571360786,
      "absolute_error": {
        "p95": 0.022645950317382802,
        "p99": 0.035526551008224466,
        "maximum": 0.04469114542007446
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.8997640609741211,
      "reference_fraction_of_uniform": 0.23081786930561066,
      "rms_normalized_to_uniform_percent": 0.10849505006864983
    },
    "south": {
      "bias_percent": 0.1814601166158613,
      "rms_normalized_error_percent": 0.31294108658284076,
      "absolute_error": {
        "p95": 0.04619852304458615,
        "p99": 0.05706476211547851,
        "maximum": 0.062079429626464844
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.4988298416137695,
      "reference_fraction_of_uniform": 0.6410287022590637,
      "rms_normalized_to_uniform_percent": 0.20304212416385783
    },
    "west": {
      "bias_percent": -0.02371886292341881,
      "rms_normalized_error_percent": 0.47506053136437537,
      "absolute_error": {
        "p95": 0.022024446725845317,
        "p99": 0.027797346115112302,
        "maximum": 0.028766632080078125
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.8342487215995789,
      "reference_fraction_of_uniform": 0.21401111781597137,
      "rms_normalized_to_uniform_percent": 0.09852676189085248
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
          "nmbe_percent": 0.10601762719902413,
          "cvrmse_percent": 2.6248035496998643,
          "absolute_error_percentiles_lux": {
            "p50": 0.9061355590820312,
            "p90": 11.387103271484378,
            "p95": 18.781533813476557,
            "p99": 39.13577514648438
          },
          "maximum_absolute_error_lux": 193.93994140625,
          "worst": {
            "sensor_index": 21,
            "position": [
              6.5,
              1.5,
              0.75
            ],
            "hour_of_year": 6086.5,
            "foton_lux": 6180.70703125,
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
            "mean_absolute_error_percentage_points": 0.375990767331499,
            "maximum_error_percentage_points": 1.3214528712127702,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.4898396968813762,
            "maximum_error_percentage_points": 2.683561643835617,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.4917196152725151,
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
      "study_preparation_seconds": 0.3911536750019877,
      "weather_seconds": 0.22951776500121923,
      "metric_reduction_seconds": 0.18850406200363068,
      "write_seconds": 0.04292382299900055,
      "total_seconds": 0.461329798999941,
      "cold_end_to_end_seconds": 0.8524834740019287,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.03053371900023194,
      "engine_upload_seconds": 0.01450038,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.01473156,
      "engine_annual_reduction_seconds": 0.007941237,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.01473156
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3911536750019877,
      "weather_seconds": 0.2346442050038604,
      "metric_reduction_seconds": 0.3447042080006213,
      "write_seconds": 0.03302387699659448,
      "total_seconds": 0.6127386929947534,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.6127386929947534,
      "raw_export_seconds": 0.012246827005583327,
      "engine_upload_seconds": 0.014831479,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.5e-08,
      "engine_annual_reduction_seconds": 0.008644862,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.014332936996652279,
      "full": 0.026554857999144588
    }
  },
  "elapsed_seconds": 3.2193499479981256,
  "result_class": "passed"
}
```
