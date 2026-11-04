# Foton report

Status: **passed**

```json
{
  "scene": "balcony_above",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "balcony_above",
    "category": "shading",
    "question": "How does an upper balcony slab shade a full-width facade?",
    "interactions": [
      "balcony",
      "overhang",
      "context_occlusion"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 6,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "3c6a68488ae59d5a4c9abc56fc3d25409f982fc5d32ea999787ddbde2413c276",
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
      "scene_fingerprint": 9723977500591765372,
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 9723977500591765372,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.3)",
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/12f3d0b2-7d1e-44d9-9264-d1e29a27929b/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "f86339d7b5aabcd354a29792e78084a9654ae1dc1ac7a6382fc4f2d8bfa4ff93",
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
          "maximum": 0.0001479843631386757,
          "p95": 0.0,
          "p99": 7.0536480052396655e-06
        },
        "bias_percent": 0.007772835741710868,
        "identifier": "balcony_above_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1504613225770217,
        "worst_index": [
          11,
          258,
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
          "maximum": 0.0005377717316150665,
          "p95": 1.53389701154083e-05,
          "p99": 8.985551539808512e-05
        },
        "bias_percent": 0.09528290936879161,
        "identifier": "balcony_above_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.360994229524615,
        "worst_index": [
          15,
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
          "maximum": 0.00040490925312042236,
          "p95": 1.252072979696095e-05,
          "p99": 7.370091043412685e-05
        },
        "bias_percent": -0.0537245398091957,
        "identifier": "balcony_above_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0892802299213071,
        "worst_index": [
          3,
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
            "identifier": "balcony_above_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00042117451084777713,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00014122296124696732
                },
                "candidate_energy": 3.404064759850371,
                "cvrmse_percent": 49.59170310797679,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.12777034897673376,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.3997209245608246,
                "relative_energy_error_percent": 0.12777034897673376,
                "rms_normalized_rmse_percent": 8.476480441507752,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001030085957609117,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.0014512604684568942,
                  "rgb_channel": 0,
                  "sky_patch_index": 211
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006790030747652054,
                  "p50": 0.0,
                  "p90": 1.5411438312185714e-06,
                  "p95": 2.0902585674775764e-05,
                  "p99": 0.00024167884839698672
                },
                "candidate_energy": 2.438907978120163,
                "cvrmse_percent": 111.66744017856963,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.07414203136634952,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4407175757107105,
                "relative_energy_error_percent": 0.07414203136634952,
                "rms_normalized_rmse_percent": 4.31189434142641,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05575949884951115,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.05508049577474594,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 106.52287502307445,
            "full": 234.81187492143363
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 107.5090829981491,
            "full": 238.97512501571327
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 106.96541704237461,
            "full": 237.75816708803177
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 103.54579205159098,
            "full": 239.6665420383215
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
            "identifier": "balcony_above_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002925597655121237,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00011656509013846517
                },
                "candidate_energy": 3.39957772350499,
                "cvrmse_percent": 38.11359734187398,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.011140886981250729,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.399199022583616,
                "relative_energy_error_percent": 0.01114088698125073,
                "rms_normalized_rmse_percent": 6.531835933598115,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0011704990174621344,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.0008779392519500107,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008985036984086037,
                  "p50": 0.0,
                  "p90": 9.361853517475552e-06,
                  "p95": 2.3488162696594372e-05,
                  "p99": 0.00018005704623647034
                },
                "candidate_energy": 3.9295506342888054,
                "cvrmse_percent": 52.157499771869155,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.016665706206681494,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.930205630812555,
                "relative_energy_error_percent": 0.016665706206681494,
                "rms_normalized_rmse_percent": 2.5050069891426627,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.031176619231700897,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.030278115533292294,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.24183290731162,
            "full": 2374.176000012085
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.00229201558977,
            "full": 2298.320374917239
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.89495804160833,
            "full": 2373.1909579364583
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.7058329479769,
            "full": 2302.474749973044
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
            "identifier": "balcony_above_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003622912336140871,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00010020955232903361
                },
                "candidate_energy": 3.397278146588178,
                "cvrmse_percent": 34.91113757368732,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.2206637899721201,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.4047912880851072,
                "relative_energy_error_percent": 0.22066378997212016,
                "rms_normalized_rmse_percent": 5.984362165271537,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004128150641918182,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0037658594083040953,
                  "rgb_channel": 0,
                  "sky_patch_index": 313
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005463585257530212,
                  "p50": 0.0,
                  "p90": 9.484223892286551e-06,
                  "p95": 2.274631151522044e-05,
                  "p99": 0.00016681448323652148
                },
                "candidate_energy": 3.9371642148961605,
                "cvrmse_percent": 48.10561340390338,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.09909850044822929,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.93326640686832,
                "relative_energy_error_percent": 0.0990985004482293,
                "rms_normalized_rmse_percent": 2.306103730863966,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03458845056593418,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.0351348090916872,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 137.4344170326367,
            "full": 2497.398208011873
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.12054201681167,
            "full": 2507.722958107479
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 131.35270902421325,
            "full": 2530.192582984455
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.94354095868766,
            "full": 2458.81337497849
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
            "identifier": "balcony_above_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001703790039755404,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.003307109698653e-05
                },
                "candidate_energy": 3.3975003447158088,
                "cvrmse_percent": 22.688909961273886,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.14263577322313425,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.402353317678262,
                "relative_energy_error_percent": 0.14263577322313425,
                "rms_normalized_rmse_percent": 3.8942816932697184,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001661509508267045,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.0014911305042915046,
                  "rgb_channel": 0,
                  "sky_patch_index": 159
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000569639727473259,
                  "p50": 0.0,
                  "p90": 6.502378528239234e-06,
                  "p95": 1.466976391384378e-05,
                  "p99": 0.0001004009391181171
                },
                "candidate_energy": 3.9334266721451883,
                "cvrmse_percent": 31.901117053754945,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.05315474977407346,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.931336979810794,
                "relative_energy_error_percent": 0.05315474977407345,
                "rms_normalized_rmse_percent": 1.5308766546824346,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04421105980873108,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.04478069953620434,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 191.02866703178734,
            "full": 4333.819332998246
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 188.94208304118365,
            "full": 4370.315667008981
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 188.9527920866385,
            "full": 4292.443375103176
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 192.3467080341652,
            "full": 4388.285666005686
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
    "/Users/ssanjay/GitHub/foton-0.3.3/validation/results/2026-11-04-architectural-v4-metal-0.3.3-release/balcony_above/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2696.1840839358047,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10531.303207972087,
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
        "identifier": "balcony_above_grid",
        "full_identifier": "balcony_above_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.0251594979050582,
            "cvrmse_percent": 3.395081783887871,
            "rms_normalized_rmse_percent": 0.5831204642381814,
            "reference_energy": 3.402104158160455,
            "candidate_energy": 3.4012482058360547,
            "relative_energy_error_percent": 0.0251594979050582,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 5.023321136832237e-06,
              "maximum": 6.313773337751627e-05
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 260,
              "rgb_channel": 0,
              "reference": 0.001303136465139687,
              "candidate": 0.0013662741985172033,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.9418580088563032,
            "cvrmse_percent": 39.52323556418123,
            "rms_normalized_rmse_percent": 1.8979130396008703,
            "reference_energy": 3.9302045076396457,
            "candidate_energy": 3.8931875617200102,
            "relative_energy_error_percent": 0.9418580088563033,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.3537485150155044e-06,
              "p95": 1.3582110113929957e-05,
              "p99": 4.265968163963407e-05,
              "maximum": 0.00105198472738266
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.031038634479045868,
              "candidate": 0.029986649751663208,
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
            "nmbe_percent": -0.5165207845202332,
            "cvrmse_percent": 21.15790108658028,
            "rms_normalized_rmse_percent": 1.895492153061864,
            "reference_energy": 7.332308665800101,
            "candidate_energy": 7.294435767556065,
            "relative_energy_error_percent": 0.5165207845202332,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.365611600107516e-06,
              "p95": 1.366477954434231e-05,
              "p99": 4.212337080389261e-05,
              "maximum": 0.00105198472738266
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.031038634479045868,
              "candidate": 0.029986649751663208,
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
        "identifier": "balcony_above_grid",
        "full_identifier": "balcony_above_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.0251594979050582,
            "cvrmse_percent": 3.395081783887871,
            "rms_normalized_rmse_percent": 0.5831204642381814,
            "reference_energy": 3.402104158160455,
            "candidate_energy": 3.4012482058360547,
            "relative_energy_error_percent": 0.0251594979050582,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 5.023321136832237e-06,
              "maximum": 6.313773337751627e-05
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 260,
              "rgb_channel": 0,
              "reference": 0.001303136465139687,
              "candidate": 0.0013662741985172033,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 59.58293295698125,
            "cvrmse_percent": 811.4868647432235,
            "rms_normalized_rmse_percent": 31.292003364416576,
            "reference_energy": 2.439601459618176,
            "candidate_energy": 3.8931875617200102,
            "relative_energy_error_percent": 59.58293295698127,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.478399896470373e-05,
              "p95": 6.758903691661544e-05,
              "p99": 0.00017095584917115048,
              "maximum": 0.009204953908920288
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05541999638080597,
              "candidate": 0.06462495028972626,
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
            "nmbe_percent": 24.868253294999988,
            "cvrmse_percent": 338.8958767745087,
            "rms_normalized_rmse_percent": 31.29240496565668,
            "reference_energy": 5.841705617778631,
            "candidate_energy": 7.294435767556065,
            "relative_energy_error_percent": 24.86825329499999,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.4701297156279913e-05,
              "p95": 6.724805280100554e-05,
              "p99": 0.00017344584921374917,
              "maximum": 0.009204953908920288
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05541999638080597,
              "candidate": 0.06462495028972626,
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
      "bias_percent": 0.291307335442136,
      "rms_normalized_error_percent": 0.37434197117193424,
      "absolute_error": {
        "p95": 0.08841293278512108,
        "p99": 0.11593103833805428,
        "maximum": 0.12517281154656867
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.112511114158955,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.37434197117193424
    },
    "overcast": {
      "bias_percent": 0.23299277681772756,
      "rms_normalized_error_percent": 0.2800699175762824,
      "absolute_error": {
        "p95": 0.03833529353141785,
        "p99": 0.045731127262115465,
        "maximum": 0.04858875274658203
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.8433756828308105,
      "reference_fraction_of_uniform": 0.5403683185577393,
      "rms_normalized_to_uniform_percent": 0.1646874048823159
    },
    "horizon": {
      "bias_percent": 0.9937143582016952,
      "rms_normalized_error_percent": 1.9892000509742502,
      "absolute_error": {
        "p95": 0.06003207620038664,
        "p99": 0.08851987253495122,
        "maximum": 0.0993364243511321
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.4544831689190454,
      "reference_fraction_of_uniform": 0.20449643530589212,
      "rms_normalized_to_uniform_percent": 0.2787452253880942
    },
    "north": {
      "bias_percent": 14.903666110450317,
      "rms_normalized_error_percent": 41.98380158778689,
      "absolute_error": {
        "p95": 0.0002577754930825904,
        "p99": 0.00034306454526813454,
        "maximum": 0.0003770958246605005
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 9.506462083663791e-05,
      "reference_fraction_of_uniform": 1.3365830454858951e-05,
      "rms_normalized_to_uniform_percent": 0.0009438094809536534
    },
    "east": {
      "bias_percent": 0.06729715270473019,
      "rms_normalized_error_percent": 0.4843002826318043,
      "absolute_error": {
        "p95": 0.025492727756500244,
        "p99": 0.031485557556152344,
        "maximum": 0.03185272216796875
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3710042238235474,
      "reference_fraction_of_uniform": 0.19275951385498047,
      "rms_normalized_to_uniform_percent": 0.10239258642249299
    },
    "south": {
      "bias_percent": 0.3213864974721751,
      "rms_normalized_error_percent": 0.4360201254916866,
      "absolute_error": {
        "p95": 0.08290088176727295,
        "p99": 0.11310799121856686,
        "maximum": 0.12178325653076172
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.658870697021484,
      "reference_fraction_of_uniform": 0.7956220507621765,
      "rms_normalized_to_uniform_percent": 0.3420781727950934
    },
    "west": {
      "bias_percent": 0.27172024212944496,
      "rms_normalized_error_percent": 0.36767845442181485,
      "absolute_error": {
        "p95": 0.01763763278722763,
        "p99": 0.02108685970306396,
        "maximum": 0.022069692611694336
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3976463079452515,
      "reference_fraction_of_uniform": 0.1965053230524063,
      "rms_normalized_to_uniform_percent": 0.0790889281223069
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
        "identifier": "balcony_above_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.07351534429707202,
          "cvrmse_percent": 2.346130625147185,
          "absolute_error_percentiles_lux": {
            "p50": 1.541961669921875,
            "p90": 13.067358398437502,
            "p95": 23.223252868652295,
            "p99": 62.033203125
          },
          "maximum_absolute_error_lux": 298.240234375,
          "worst": {
            "sensor_index": 17,
            "position": [
              2.5,
              0.5,
              0.75
            ],
            "hour_of_year": 5844.5,
            "foton_lux": 25602.65234375,
            "radiance_lux": 25900.892578125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.3683828006088279,
            "maximum_error_percentage_points": 1.6420547945205506,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.19253492185656226,
            "maximum_error_percentage_points": 0.8677006444701973,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.10015981735159812,
            "maximum_error_percentage_points": 0.5235616438356168,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.11741628614916205,
            "maximum_error_percentage_points": 0.49191780821918485,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.03321156773211588,
            "maximum_error_percentage_points": 0.11178082191780803,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 36.111111111111114,
          "radiance_percent": 36.111111111111114,
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
      "maximum_error_percentage_points": 0.004997859589039422,
      "metrics": {
        "da": [
          {
            "identifier": "balcony_above_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "balcony_above_grid",
            "maximum_error_percentage_points": 0.004997859589039422,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "balcony_above_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "balcony_above_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "balcony_above_grid",
            "maximum_error_percentage_points": 0.0046575342465753344,
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
      "study_preparation_seconds": 0.007982583018019795,
      "weather_seconds": 0.08554004202596843,
      "metric_reduction_seconds": 0.11028675001580268,
      "write_seconds": 0.010139749967493117,
      "total_seconds": 0.20612533402163535,
      "cold_end_to_end_seconds": 0.21410791703965515,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.002160041010938585,
      "engine_upload_seconds": 0.000853666,
      "engine_acceleration_structure_seconds": 0.0032413750000000003,
      "engine_tracing_seconds": 0.048511500004678965,
      "engine_annual_reduction_seconds": 0.0015500417212024331,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.048511500004678965
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007982583018019795,
      "weather_seconds": 0.08056925004348159,
      "metric_reduction_seconds": 0.047232207958586514,
      "write_seconds": 0.010466917068697512,
      "total_seconds": 0.13844400004018098,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.13844400004018098,
      "raw_export_seconds": 0.0016871660482138395,
      "engine_upload_seconds": 5.7375e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0016060000052675605,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.022181291948072612,
      "full": 0.059893583063967526
    }
  },
  "elapsed_seconds": 1.2633990830508992,
  "result_class": "passed"
}
```
