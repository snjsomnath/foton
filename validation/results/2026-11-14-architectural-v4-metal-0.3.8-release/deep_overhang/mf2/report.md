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
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "a9b1e16161ff99a0990870c59037a9f7b6341b2d197dacb71da39ee677e8d4ea",
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
      "solver_version": "0.3.8",
      "scene_fingerprint": 8376055839539751168,
      "basis": "ReinhartMf2",
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
      "solver_version": "0.3.8",
      "scene_fingerprint": 8376055839539751168,
      "basis": "ReinhartMf2",
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.8)",
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/52e717d2-b26e-4bbc-9536-f9b0a23834d6/scratchpad/refx/foton-references-corpus4-2026-11-03",
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
          "maximum": 0.00011488376185297966,
          "p95": 0.0,
          "p99": 7.125257980078459e-06
        },
        "bias_percent": 0.014153360126348354,
        "identifier": "deep_overhang_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.194300789050525,
        "worst_index": [
          17,
          363,
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
          "maximum": 0.0005521029233932495,
          "p95": 1.2128453818149865e-05,
          "p99": 8.626654744148254e-05
        },
        "bias_percent": -0.016037336140242536,
        "identifier": "deep_overhang_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3113238909906249,
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
          "maximum": 0.000395236536860466,
          "p95": 1.0327477866667323e-05,
          "p99": 7.252476643770933e-05
        },
        "bias_percent": -0.027272551562409618,
        "identifier": "deep_overhang_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0900356957334103,
        "worst_index": [
          32,
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
            "identifier": "deep_overhang_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00041646696627140045,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0001352669787593186
                },
                "candidate_energy": 2.8982551782573864,
                "cvrmse_percent": 49.49725909235405,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.14890417685098617,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.902577236999605,
                "relative_energy_error_percent": 0.14890417685098617,
                "rms_normalized_rmse_percent": 7.924665538860594,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0017582729924470186,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.002174739958718419,
                  "rgb_channel": 0,
                  "sky_patch_index": 214
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007313545793294907,
                  "p50": 0.0,
                  "p90": 8.521692507202564e-09,
                  "p95": 1.5842932498344453e-05,
                  "p99": 0.00022606796119362116
                },
                "candidate_energy": 2.441651870074228,
                "cvrmse_percent": 106.02058514797689,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.41008040612271107,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.451705835320645,
                "relative_energy_error_percent": 0.41008040612271107,
                "rms_normalized_rmse_percent": 4.098934669971256,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.010395980440080166,
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "reference": 0.011127335019409657,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 108.17312495782971,
            "full": 224.00641604326665
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 102.07983397413045,
            "full": 228.9537088945508
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 103.59941702336073,
            "full": 234.39445800613612
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 102.4155409540981,
            "full": 225.20954196806997
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
            "identifier": "deep_overhang_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00031395949190482497,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.344024874735624e-05
                },
                "candidate_energy": 2.901372792915936,
                "cvrmse_percent": 37.22410470136494,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.315904318974711,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.910567401042499,
                "relative_energy_error_percent": 0.315904318974711,
                "rms_normalized_rmse_percent": 5.968876598318029,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0018361425027251244,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.0015221830108202994,
                  "rgb_channel": 0,
                  "sky_patch_index": 145
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000814264640212059,
                  "p50": 0.0,
                  "p90": 8.123859333863955e-06,
                  "p95": 1.8473586351319682e-05,
                  "p99": 0.00015423954755533487
                },
                "candidate_energy": 3.819829316968516,
                "cvrmse_percent": 48.05501207912552,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.10737155742908763,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8157323057644916,
                "relative_energy_error_percent": 0.10737155742908762,
                "rms_normalized_rmse_percent": 2.2392222285970154,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06015392020344734,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0609681848436594,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.4782078936696,
            "full": 2265.016542049125
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 126.81458296719939,
            "full": 2265.1239169063047
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 131.63633306976408,
            "full": 2258.431291906163
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.59495796915144,
            "full": 2296.5739580104128
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
            "identifier": "deep_overhang_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003235503099858761,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00010890304110944271
                },
                "candidate_energy": 2.9080562188423755,
                "cvrmse_percent": 42.950491220757314,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.11205772012362347,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.9048011648828833,
                "relative_energy_error_percent": 0.11205772012362347,
                "rms_normalized_rmse_percent": 6.886144308832058,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0009464116883464158,
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "reference": 0.0012699619983322918,
                  "rgb_channel": 0,
                  "sky_patch_index": 87
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008246749639511108,
                  "p50": 0.0,
                  "p90": 8.164403413957191e-06,
                  "p95": 1.8524497136240825e-05,
                  "p99": 0.0001562461256980896
                },
                "candidate_energy": 3.8107694985511387,
                "cvrmse_percent": 50.560032872856645,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.28648910051874815,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8217183049473427,
                "relative_energy_error_percent": 0.2864891005187482,
                "rms_normalized_rmse_percent": 2.3597567251610005,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03601142019033432,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.03683609515428543,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 126.40549999196082,
            "full": 2442.0216670259833
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.3497499320656,
            "full": 2471.1912909988314
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.29975004307926,
            "full": 2407.279666978866
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 128.61379201058298,
            "full": 2391.083416994661
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
            "identifier": "deep_overhang_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00018379942048341036,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.8031437220051885e-05
                },
                "candidate_energy": 2.898478159903334,
                "cvrmse_percent": 23.87266488881644,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.19935922100475495,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.904268086135744,
                "relative_energy_error_percent": 0.19935922100475498,
                "rms_normalized_rmse_percent": 3.828570319587345,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0018250229768455029,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0016412235563620925,
                  "rgb_channel": 0,
                  "sky_patch_index": 155
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00034199468791484833,
                  "p50": 0.0,
                  "p90": 5.83328094307948e-06,
                  "p95": 1.2522679753601551e-05,
                  "p99": 8.865118434187025e-05
                },
                "candidate_energy": 3.819000490179107,
                "cvrmse_percent": 28.44772038828941,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.02437297189629117,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8199315210151816,
                "relative_energy_error_percent": 0.024372971896291163,
                "rms_normalized_rmse_percent": 1.3269910391916786,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06045673042535782,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.06079872511327267,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 185.010917019099,
            "full": 4278.908958076499
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 184.50537498574704,
            "full": 4239.605666021816
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 187.41462496109307,
            "full": 4620.951583026908
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 184.54270903021097,
            "full": 4279.319082968868
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
    "/Users/ssanjay/GitHub/foton-0.3.8/validation/results/2026-11-14-architectural-v4-metal-0.3.8-release/deep_overhang/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2667.9067090153694,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/deep_overhang/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10519.746082951315,
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
        "identifier": "deep_overhang_grid",
        "full_identifier": "deep_overhang_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.020034282966355035,
            "cvrmse_percent": 4.20204007098521,
            "rms_normalized_rmse_percent": 0.6741605782197672,
            "reference_energy": 2.9040415096833385,
            "candidate_energy": 2.903459705789828,
            "relative_energy_error_percent": 0.020034282966355035,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 5.2675441111205146e-06,
              "maximum": 6.88477884978056e-05
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 412,
              "rgb_channel": 0,
              "reference": 0.00318742822855711,
              "candidate": 0.0031185804400593042,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.9998577405184604,
            "cvrmse_percent": 42.44364941684539,
            "rms_normalized_rmse_percent": 1.9798155894256824,
            "reference_energy": 3.81679763079649,
            "candidate_energy": 3.778635084245046,
            "relative_energy_error_percent": 0.9998577405184603,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.80326993460767e-06,
              "p95": 1.216347300214693e-05,
              "p99": 4.101777449250221e-05,
              "maximum": 0.0011230409145355225
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03242862969636917,
              "candidate": 0.03130558878183365,
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
            "nmbe_percent": -0.5764808476310023,
            "cvrmse_percent": 24.088063518940107,
            "rms_normalized_rmse_percent": 1.9785101186061238,
            "reference_energy": 6.720839140479828,
            "candidate_energy": 6.682094790034874,
            "relative_energy_error_percent": 0.5764808476310022,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.802245479775607e-06,
              "p95": 1.2079533917130902e-05,
              "p99": 4.091043956577778e-05,
              "maximum": 0.0011230409145355225
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03242862969636917,
              "candidate": 0.03130558878183365,
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
        "identifier": "deep_overhang_grid",
        "full_identifier": "deep_overhang_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.020034282966355035,
            "cvrmse_percent": 4.20204007098521,
            "rms_normalized_rmse_percent": 0.6741605782197672,
            "reference_energy": 2.9040415096833385,
            "candidate_energy": 2.903459705789828,
            "relative_energy_error_percent": 0.020034282966355035,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 5.2675441111205146e-06,
              "maximum": 6.88477884978056e-05
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 412,
              "rgb_channel": 0,
              "reference": 0.00318742822855711,
              "candidate": 0.0031185804400593042,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 54.668533358193216,
            "cvrmse_percent": 807.8547035624719,
            "rms_normalized_rmse_percent": 31.126716761003483,
            "reference_energy": 2.4430535430850657,
            "candidate_energy": 3.778635084245046,
            "relative_energy_error_percent": 54.668533358193216,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.338731294206813e-05,
              "p95": 4.94699997943826e-05,
              "p99": 0.00013768469216302037,
              "maximum": 0.00868326798081398
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017525171861052513,
              "candidate": 0.026208439841866493,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 24.96682262222527,
            "cvrmse_percent": 369.0967807892386,
            "rms_normalized_rmse_percent": 31.12613755607383,
            "reference_energy": 5.347095052768404,
            "candidate_energy": 6.682094790034874,
            "relative_energy_error_percent": 24.966822622225266,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.334399989398671e-05,
              "p95": 4.926000110572204e-05,
              "p99": 0.00013663622667081654,
              "maximum": 0.00868326798081398
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017525171861052513,
              "candidate": 0.026208439841866493,
              "position": [
                0.5,
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
      "bias_percent": 0.4050428958219295,
      "rms_normalized_error_percent": 0.31792288334620156,
      "absolute_error": {
        "p95": 0.055984872939810026,
        "p99": 0.10176723332797931,
        "maximum": 0.11633254400969095
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.005870511405461,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.31792288334620156
    },
    "overcast": {
      "bias_percent": 0.3208235628250225,
      "rms_normalized_error_percent": 0.22248237564572187,
      "absolute_error": {
        "p95": 0.024915024638175964,
        "p99": 0.03713061511516569,
        "maximum": 0.04266560077667236
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.2907943725585938,
      "reference_fraction_of_uniform": 0.5479296445846558,
      "rms_normalized_to_uniform_percent": 0.13663737614730914
    },
    "horizon": {
      "bias_percent": 1.3785278327855017,
      "rms_normalized_error_percent": 2.1609403111781504,
      "absolute_error": {
        "p95": 0.07005095864255739,
        "p99": 0.09910330953879161,
        "maximum": 0.10808797105262036
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3594082047336158,
      "reference_fraction_of_uniform": 0.2263465724330934,
      "rms_normalized_to_uniform_percent": 0.2888392102930869
    },
    "north": {
      "bias_percent": -92.72337163887303,
      "rms_normalized_error_percent": 99.55677367918481,
      "absolute_error": {
        "p95": 0.00010902896747211344,
        "p99": 0.0002773296442938996,
        "maximum": 0.0003653128104019743
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.999313462874852e-05,
      "reference_fraction_of_uniform": 3.328932052681921e-06,
      "rms_normalized_to_uniform_percent": 0.0006259640912429918
    },
    "east": {
      "bias_percent": 0.2960895874158923,
      "rms_normalized_error_percent": 0.3652970836955249,
      "absolute_error": {
        "p95": 0.01686495542526245,
        "p99": 0.028051495552062978,
        "maximum": 0.030620813369750977
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3273721933364868,
      "reference_fraction_of_uniform": 0.22101245820522308,
      "rms_normalized_to_uniform_percent": 0.08531972521256888
    },
    "south": {
      "bias_percent": 0.45835383906263805,
      "rms_normalized_error_percent": 0.3998396797025491,
      "absolute_error": {
        "p95": 0.05509266257286072,
        "p99": 0.0992270410060882,
        "maximum": 0.11364388465881348
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.476278305053711,
      "reference_fraction_of_uniform": 0.7453171610832214,
      "rms_normalized_to_uniform_percent": 0.2865082008993096
    },
    "west": {
      "bias_percent": 0.3110288466707544,
      "rms_normalized_error_percent": 0.3228204275386322,
      "absolute_error": {
        "p95": 0.01337914913892746,
        "p99": 0.01804413646459579,
        "maximum": 0.01923966407775879
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3467143774032593,
      "reference_fraction_of_uniform": 0.2242330014705658,
      "rms_normalized_to_uniform_percent": 0.07639256358623532
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
          "nmbe_percent": 0.08644212083471914,
          "cvrmse_percent": 2.3202489319932984,
          "absolute_error_percentiles_lux": {
            "p50": 1.4927978515625,
            "p90": 13.97310180664063,
            "p95": 21.59528961181639,
            "p99": 50.40359954833961
          },
          "maximum_absolute_error_lux": 343.497802734375,
          "worst": {
            "sensor_index": 18,
            "position": [
              3.5,
              5.5,
              0.75
            ],
            "hour_of_year": 8604.5,
            "foton_lux": 3515.520263671875,
            "radiance_lux": 3172.0224609375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.3576598173515975,
            "maximum_error_percentage_points": 1.8638356164383572,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1844378179506718,
            "maximum_error_percentage_points": 1.2201761953689783,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.13208143074581466,
            "maximum_error_percentage_points": 0.9556164383561594,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.13507610350075971,
            "maximum_error_percentage_points": 0.8804109589041076,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.019482496194824707,
            "maximum_error_percentage_points": 0.08547945205479435,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 25.0,
          "radiance_percent": 25.0,
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
      "maximum_error_percentage_points": 0.004938730736299135,
      "metrics": {
        "da": [
          {
            "identifier": "deep_overhang_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "deep_overhang_grid",
            "maximum_error_percentage_points": 0.004938730736299135,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "deep_overhang_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "deep_overhang_grid",
            "maximum_error_percentage_points": 0.004383561643834355,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "deep_overhang_grid",
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
      "study_preparation_seconds": 0.007070374907925725,
      "weather_seconds": 0.08198812510818243,
      "metric_reduction_seconds": 0.11913574999198318,
      "write_seconds": 0.019274875055998564,
      "total_seconds": 0.220511042047292,
      "cold_end_to_end_seconds": 0.22758141695521772,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0022495840676128864,
      "engine_upload_seconds": 0.000913584,
      "engine_acceleration_structure_seconds": 0.003671042,
      "engine_tracing_seconds": 0.05892124981619418,
      "engine_annual_reduction_seconds": 0.001614291686564684,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.05892124981619418
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007070374907925725,
      "weather_seconds": 0.07634949986822903,
      "metric_reduction_seconds": 0.05417766701430082,
      "write_seconds": 0.017663082806393504,
      "total_seconds": 0.14829241600818932,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14829241600818932,
      "raw_export_seconds": 0.0029128328897058964,
      "engine_upload_seconds": 6.0042e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.005007208324968815,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.021730666980147362,
      "full": 0.05454929219558835
    }
  },
  "elapsed_seconds": 1.3325264579616487,
  "result_class": "passed"
}
```
