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
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "f97f1714c135ee9bef3dc17d5b20ee7e2c3ada68e21e22c7a62845ea0b780b59",
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
      "scene_fingerprint": 11874334619688306964,
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 11874334619688306964,
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
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.2)",
      "weather_id": "82c544d76aea9710a570440071d4833104fdc7da7504bac286ac2afe42bdd614"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/usr/local/radiance/bin/gendaymtx",
      "weather_id": "a39080f6e203418927f730315e529393ad080464468f645476c383a744bbb720"
    },
    "sun_up_hours_equal": true,
    "compared_hours": 4405,
    "max_relative_difference": 0.0,
    "mean_relative_difference": 0.0
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
          "maximum": 7.914018351584673e-05,
          "p95": 0.0,
          "p99": 4.614703357219696e-06
        },
        "bias_percent": 0.06889876830678253,
        "identifier": "overhang_fins_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8824736846485314,
        "worst_index": [
          10,
          260,
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
          "maximum": 0.000721663236618042,
          "p95": 1.2307815268286504e-05,
          "p99": 7.540697697550058e-05
        },
        "bias_percent": 0.18102338513889116,
        "identifier": "overhang_fins_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3925828682673087,
        "worst_index": [
          17,
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
          "maximum": 0.0005025230348110199,
          "p95": 1.068211713572964e-05,
          "p99": 6.149872206151485e-05
        },
        "bias_percent": -0.052298958214880224,
        "identifier": "overhang_fins_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.157171143420004,
        "worst_index": [
          16,
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
            "identifier": "overhang_fins_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006570657715201378,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0001893083972390741
                },
                "candidate_energy": 2.341701879602624,
                "cvrmse_percent": 108.74881749417779,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.03209940401858164,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.342453793309687,
                "relative_energy_error_percent": 0.032099404018581634,
                "rms_normalized_rmse_percent": 14.666662368096368,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001220721984282136,
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "reference": 0.0005636562127619982,
                  "rgb_channel": 0,
                  "sky_patch_index": 149
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0012148283421993256,
                  "p50": 0.0,
                  "p90": 5.930238057771938e-06,
                  "p95": 2.4778579245321453e-05,
                  "p99": 0.00032114225905388594
                },
                "candidate_energy": 2.04600650053618,
                "cvrmse_percent": 181.16133866221165,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.6260367076342134,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0588959449233926,
                "relative_energy_error_percent": 0.6260367076342134,
                "rms_normalized_rmse_percent": 6.756088500924649,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.017738090828061104,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.01895291917026043,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 158.22274994570762,
            "full": 233.53699990548193
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.81920901779085,
            "full": 242.9345001000911
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 108.51074999663979,
            "full": 256.85641705058515
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 109.23633293714374,
            "full": 235.5158340651542
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
            "identifier": "overhang_fins_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002945815213024616,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.319398668594658e-05
                },
                "candidate_energy": 2.3478303832598613,
                "cvrmse_percent": 46.27154201131956,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.1606185900839448,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.3440653784982715,
                "relative_energy_error_percent": 0.16061859008394477,
                "rms_normalized_rmse_percent": 6.279505728051442,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0036302199587225914,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.003924801480025053,
                  "rgb_channel": 0,
                  "sky_patch_index": 313
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0012017246335744858,
                  "p50": 5.000000058430487e-08,
                  "p90": 1.0068112896988186e-05,
                  "p95": 1.868000157401184e-05,
                  "p99": 0.0001462365034967661
                },
                "candidate_energy": 3.3301275939337103,
                "cvrmse_percent": 54.99421349335035,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.19690593874312257,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.336697749961292,
                "relative_energy_error_percent": 0.19690593874312254,
                "rms_normalized_rmse_percent": 2.543697716813226,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06243847496807575,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.061236750334501266,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.13316701352596,
            "full": 2468.673333991319
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.56841598358005,
            "full": 2863.9911249047145
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.88412501849234,
            "full": 2522.4255000939593
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.45329200476408,
            "full": 2503.065333934501
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
            "identifier": "overhang_fins_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002584274625405669,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.09335067262873e-05
                },
                "candidate_energy": 2.3460704128356156,
                "cvrmse_percent": 44.66592558625099,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.19387877477114057,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.341530681838776,
                "relative_energy_error_percent": 0.19387877477114057,
                "rms_normalized_rmse_percent": 6.062108521284192,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0007511393923778087,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.0010095668549183756,
                  "rgb_channel": 0,
                  "sky_patch_index": 90
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007422007620334625,
                  "p50": 5.000000058430487e-08,
                  "p90": 9.539876054986974e-06,
                  "p95": 1.805433475965401e-05,
                  "p99": 0.00014113960787653923
                },
                "candidate_energy": 3.3437901968000077,
                "cvrmse_percent": 53.590073395655324,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.12251165007752725,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.3478917542309254,
                "relative_energy_error_percent": 0.12251165007752723,
                "rms_normalized_rmse_percent": 2.4807759662374713,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04068831540644169,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.039946114644408226,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.3695419691503,
            "full": 2732.374000013806
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.4558330019936,
            "full": 2846.5102090267465
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 173.8515410106629,
            "full": 3324.4439580012113
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 179.32875000406057,
            "full": 2833.5855840705335
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
            "identifier": "overhang_fins_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001919330097734928,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.8443460147827864e-05
                },
                "candidate_energy": 2.3478114956342324,
                "cvrmse_percent": 28.21615466451313,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.04460877773504384,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.3467646326153044,
                "relative_energy_error_percent": 0.04460877773504384,
                "rms_normalized_rmse_percent": 3.8346363361554903,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0016509165288880467,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.001458983519114554,
                  "rgb_channel": 0,
                  "sky_patch_index": 159
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00046356022357940674,
                  "p50": 7.44145189912615e-08,
                  "p90": 6.838244917162233e-06,
                  "p95": 1.2557021818793146e-05,
                  "p99": 8.890772005543113e-05
                },
                "candidate_energy": 3.33943448742869,
                "cvrmse_percent": 33.153845698951145,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.003395303561770754,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.3393211073401936,
                "relative_energy_error_percent": 0.003395303561770754,
                "rms_normalized_rmse_percent": 1.531029417693086,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.021335680037736893,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.0217992402613163,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 202.05520803574473,
            "full": 4900.6159589625895
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 201.30954193882644,
            "full": 4771.364915999584
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 214.2196249915287,
            "full": 4668.0265420582145
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 197.7639589458704,
            "full": 4628.92954191193
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
    "/content/suite-vulkan-0.3.2/overhang_fins/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2899.301291909069,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/overhang_fins/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 11615.04787497688,
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
        "identifier": "overhang_fins_grid",
        "full_identifier": "overhang_fins_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.045998578794981156,
            "cvrmse_percent": 3.826859696291209,
            "rms_normalized_rmse_percent": 0.5203070658130219,
            "reference_energy": 2.345814719842906,
            "candidate_energy": 2.346893761275197,
            "relative_energy_error_percent": 0.045998578794981156,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 4.009882104583085e-06,
              "maximum": 6.273412145674229e-05
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 366,
              "rgb_channel": 0,
              "reference": 0.002344720298424363,
              "candidate": 0.0024074544198811054,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.9790005309582478,
            "cvrmse_percent": 37.845400487201836,
            "rms_normalized_rmse_percent": 1.7481691057923208,
            "reference_energy": 3.3408511722699092,
            "candidate_energy": 3.308144221554862,
            "relative_energy_error_percent": 0.9790005309582478,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 9.806570844261842e-08,
              "p90": 6.73065177920765e-06,
              "p95": 1.1480948160169646e-05,
              "p99": 3.463885514065623e-05,
              "maximum": 0.0009014736860990524
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02629922330379486,
              "candidate": 0.02539774961769581,
              "position": [
                1.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5561766750992481,
            "cvrmse_percent": 22.254626886543672,
            "rms_normalized_rmse_percent": 1.749811380602285,
            "reference_energy": 5.686665892112815,
            "candidate_energy": 5.655037982830059,
            "relative_energy_error_percent": 0.5561766750992481,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 9.817108548304532e-08,
              "p90": 6.779626255593032e-06,
              "p95": 1.1509127944009379e-05,
              "p99": 3.533056587912142e-05,
              "maximum": 0.0009014736860990524
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02629922330379486,
              "candidate": 0.02539774961769581,
              "position": [
                1.5,
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
        "identifier": "overhang_fins_grid",
        "full_identifier": "overhang_fins_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.045998578794981156,
            "cvrmse_percent": 3.826859696291209,
            "rms_normalized_rmse_percent": 0.5203070658130219,
            "reference_energy": 2.345814719842906,
            "candidate_energy": 2.346893761275197,
            "relative_energy_error_percent": 0.045998578794981156,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 4.009882104583085e-06,
              "maximum": 6.273412145674229e-05
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 366,
              "rgb_channel": 0,
              "reference": 0.002344720298424363,
              "candidate": 0.0024074544198811054,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 61.47415812230558,
            "cvrmse_percent": 908.1032885944709,
            "rms_normalized_rmse_percent": 33.81039801044122,
            "reference_energy": 2.0487143330074957,
            "candidate_energy": 3.308144221554862,
            "relative_energy_error_percent": 61.47415812230559,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.251999805797823e-05,
              "p95": 4.989000080968253e-05,
              "p99": 0.0001315439585596323,
              "maximum": 0.009990360587835312
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.051890790462493896,
              "candidate": 0.06188115105032921,
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
            "nmbe_percent": 28.683595325466325,
            "cvrmse_percent": 423.3514107123404,
            "rms_normalized_rmse_percent": 33.81014087189954,
            "reference_energy": 4.394529052850402,
            "candidate_energy": 5.655037982830059,
            "relative_energy_error_percent": 28.683595325466328,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.2538619942101925e-05,
              "p95": 5.002000034437515e-05,
              "p99": 0.00013020832557231188,
              "maximum": 0.009990360587835312
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.051890790462493896,
              "candidate": 0.06188115105032921,
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
      "bias_percent": 0.24452211064534812,
      "rms_normalized_error_percent": 0.3213546324634414,
      "absolute_error": {
        "p95": 0.055062711993090874,
        "p99": 0.07170775534374342,
        "maximum": 0.07963365996582716
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.042658427783702,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.3213546324634414
    },
    "overcast": {
      "bias_percent": 0.1863148341328899,
      "rms_normalized_error_percent": 0.23804399307015803,
      "absolute_error": {
        "p95": 0.022911295294761658,
        "p99": 0.03031170964241027,
        "maximum": 0.03215992450714111
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.8415021896362305,
      "reference_fraction_of_uniform": 0.5634928941726685,
      "rms_normalized_to_uniform_percent": 0.14866445137736595
    },
    "horizon": {
      "bias_percent": 1.0794049881082732,
      "rms_normalized_error_percent": 2.188096064681042,
      "absolute_error": {
        "p95": 0.05547898175180868,
        "p99": 0.05941743038286169,
        "maximum": 0.06115478288807874
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.9928056987573842,
      "reference_fraction_of_uniform": 0.19688140947387786,
      "rms_normalized_to_uniform_percent": 0.27688132194995924
    },
    "north": {
      "bias_percent": -5.549376761252633,
      "rms_normalized_error_percent": 39.56174329420743,
      "absolute_error": {
        "p95": 0.0004226829041726887,
        "p99": 0.0004397051568957977,
        "maximum": 0.00044236736721359193
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 0.0002917590318247676,
      "reference_fraction_of_uniform": 5.785817847936414e-05,
      "rms_normalized_to_uniform_percent": 0.0021646436409421006
    },
    "east": {
      "bias_percent": 0.06823591971796743,
      "rms_normalized_error_percent": 0.5281016954403137,
      "absolute_error": {
        "p95": 0.014174699783325195,
        "p99": 0.023955917358398426,
        "maximum": 0.026644229888916016
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.7831960916519165,
      "reference_fraction_of_uniform": 0.1553141325712204,
      "rms_normalized_to_uniform_percent": 0.09009945776666721
    },
    "south": {
      "bias_percent": 0.2908858511702241,
      "rms_normalized_error_percent": 0.369684652303799,
      "absolute_error": {
        "p95": 0.05448257923126221,
        "p99": 0.07035434842109678,
        "maximum": 0.07714176177978516
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.141620635986328,
      "reference_fraction_of_uniform": 0.8213168978691101,
      "rms_normalized_to_uniform_percent": 0.2965787065271286
    },
    "west": {
      "bias_percent": 0.04473698415677175,
      "rms_normalized_error_percent": 0.31877702244991624,
      "absolute_error": {
        "p95": 0.007576420903205872,
        "p99": 0.00830324739217758,
        "maximum": 0.008653044700622559
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.8014744520187378,
      "reference_fraction_of_uniform": 0.15893886983394623,
      "rms_normalized_to_uniform_percent": 0.05539388461852211
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
          "nmbe_percent": 0.04010330942501004,
          "cvrmse_percent": 2.9609148962492022,
          "absolute_error_percentiles_lux": {
            "p50": 1.4616317749023438,
            "p90": 14.705712890625001,
            "p95": 23.63201446533199,
            "p99": 54.51300781249927
          },
          "maximum_absolute_error_lux": 334.595703125,
          "worst": {
            "sensor_index": 15,
            "position": [
              2.5,
              2.5,
              0.75
            ],
            "hour_of_year": 1356.5,
            "foton_lux": 12887.2529296875,
            "radiance_lux": 12552.6572265625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.42017123287671243,
            "maximum_error_percentage_points": 1.3935616438356178,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.2474501610912102,
            "maximum_error_percentage_points": 0.9818251831618596,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.2315525114155247,
            "maximum_error_percentage_points": 0.8524657534246529,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.22991628614916415,
            "maximum_error_percentage_points": 0.8532876712328701,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.015878995433789907,
            "maximum_error_percentage_points": 0.05821917808219179,
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
            "maximum_error_percentage_points": 0.004794520547953596,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "overhang_fins_grid",
            "maximum_error_percentage_points": 0.004784754922944501,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "overhang_fins_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "overhang_fins_grid",
            "maximum_error_percentage_points": 0.004657534246572226,
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
      "study_preparation_seconds": 0.435091747000115,
      "weather_seconds": 0.405126669000083,
      "metric_reduction_seconds": 1.7807915920000141,
      "write_seconds": 0.012129426999990756,
      "total_seconds": 2.198402786000088,
      "cold_end_to_end_seconds": 2.633494533000203,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0014267920000747836,
      "engine_upload_seconds": 0.052355308,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.034718138,
      "engine_annual_reduction_seconds": 0.019529003,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.034718138
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.435091747000115,
      "weather_seconds": 0.25425574199994116,
      "metric_reduction_seconds": 1.0045074679999288,
      "write_seconds": 0.0133646439999211,
      "total_seconds": 1.2723841990000437,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 1.2723841990000437,
      "raw_export_seconds": 0.001675292000072659,
      "engine_upload_seconds": 0.044886239,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.3e-08,
      "engine_annual_reduction_seconds": 0.017810919,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.018394618000002083,
      "full": 0.04711372899987509
    }
  },
  "elapsed_seconds": 6.673784949000037,
  "result_class": "passed"
}
```
