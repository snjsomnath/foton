# Foton report

Status: **passed**

```json
{
  "scene": "clerestory",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "clerestory",
    "category": "openings",
    "question": "How does a high narrow opening distribute light toward the ceiling?",
    "interactions": [
      "high_glazing",
      "ceiling_reflection"
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
    "aperture_area": 2.0
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "03214a973f65ed0ef4d08e4a5ed543b6b591e1dae987c8ba4511a028044481b7",
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
      "scene_fingerprint": 10818472177728081475,
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 10818472177728081475,
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
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 262144,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "7981c357b1997edadb557c6bdd7cbe8993540223ed4dc46d0a43bb5e6cbf1e73",
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
          "maximum": 0.0001423674402758479,
          "p95": 0.0,
          "p99": 3.128760727122426e-05
        },
        "bias_percent": -0.03985531661445846,
        "identifier": "clerestory_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.465612390224671,
        "worst_index": [
          4,
          449,
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
          "maximum": 0.0005423463881015778,
          "p95": 1.412499841535464e-05,
          "p99": 6.435747491195798e-05
        },
        "bias_percent": -0.14993718720716284,
        "identifier": "clerestory_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.8004076284573183,
        "worst_index": [
          11,
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
          "maximum": 0.0003777407109737396,
          "p95": 1.2512733519542962e-05,
          "p99": 5.639600567519665e-05
        },
        "bias_percent": 0.0296652172936106,
        "identifier": "clerestory_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.4324206197738611,
        "worst_index": [
          15,
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
            "identifier": "clerestory_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005194745026528835,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00010487981489859521
                },
                "candidate_energy": 2.623286954520154,
                "cvrmse_percent": 47.21634591663869,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.3510354449410994,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.63252806111268,
                "relative_energy_error_percent": 0.3510354449410994,
                "rms_normalized_rmse_percent": 6.684131964889708,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0029235139954835176,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.003442988498136401,
                  "rgb_channel": 0,
                  "sky_patch_index": 367
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008797005284577608,
                  "p50": 0.0,
                  "p90": 5.916111149417702e-06,
                  "p95": 2.1822357666678727e-05,
                  "p99": 0.00015983886260073632
                },
                "candidate_energy": 1.6050613892177736,
                "cvrmse_percent": 128.49335914561084,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.8808713760909189,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.5910463176254623,
                "relative_energy_error_percent": 0.8808713760909188,
                "rms_normalized_rmse_percent": 5.181817287305536,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0008882534457370639,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 8.552917279303074e-06,
                  "rgb_channel": 0,
                  "sky_patch_index": 367
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 126.0595420608297,
            "full": 221.87474998645484
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 105.33754096832126,
            "full": 220.81616602372378
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 112.72125004325062,
            "full": 229.74404192063957
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.72508292272687,
            "full": 222.56391600240022
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
            "identifier": "clerestory_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00031388807110488415,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 8.943193824961782e-05
                },
                "candidate_energy": 2.633573268921282,
                "cvrmse_percent": 38.97613615797805,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.15159199310003965,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.6295870255389673,
                "relative_energy_error_percent": 0.15159199310003965,
                "rms_normalized_rmse_percent": 5.5160019146033825,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0015119899762794375,
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "reference": 0.0018258780473843217,
                  "rgb_channel": 0,
                  "sky_patch_index": 257
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005871690809726715,
                  "p50": 0.0,
                  "p90": 1.1390441068215311e-05,
                  "p95": 2.1884450688958168e-05,
                  "p99": 0.00012542546028271317
                },
                "candidate_energy": 2.7504523644087087,
                "cvrmse_percent": 57.31703484096605,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.0838084613311113,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.7527594097141375,
                "relative_energy_error_percent": 0.08380846133111132,
                "rms_normalized_rmse_percent": 3.1591432264765653,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.033353134989738464,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.03276596590876579,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.09458299167454,
            "full": 2235.0467919604853
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.08066710084677,
            "full": 2241.4967089425772
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.45808307733387,
            "full": 2237.6085000578314
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 145.65679198130965,
            "full": 2228.9762910222635
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
            "identifier": "clerestory_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003919184673577547,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.207549737766385e-05
                },
                "candidate_energy": 2.6354880090034385,
                "cvrmse_percent": 41.462939736666875,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.16963684835132586,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.639966364742122,
                "relative_energy_error_percent": 0.16963684835132586,
                "rms_normalized_rmse_percent": 5.865397707474928,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0028304335428401828,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.0032223520101979375,
                  "rgb_channel": 0,
                  "sky_patch_index": 265
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007379651069641113,
                  "p50": 0.0,
                  "p90": 1.1337750584061764e-05,
                  "p95": 2.084317384287715e-05,
                  "p99": 0.00013130990555509925
                },
                "candidate_energy": 2.7374000412026263,
                "cvrmse_percent": 61.13882304466541,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.0009183056127243285,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.737374903735244,
                "relative_energy_error_percent": 0.0009183056127243286,
                "rms_normalized_rmse_percent": 3.3387229985818707,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02888402994722128,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.02962199505418539,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.09795793611556,
            "full": 2438.555417000316
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.28175009135157,
            "full": 2419.767125044018
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.46270900405943,
            "full": 2401.920542004518
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 137.25212507415563,
            "full": 2540.978458011523
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
            "identifier": "clerestory_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00022530159913003445,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.4328396799974144e-05
                },
                "candidate_energy": 2.638102159432492,
                "cvrmse_percent": 22.84648950214163,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.03231206819452797,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.637250009410991,
                "relative_energy_error_percent": 0.03231206819452797,
                "rms_normalized_rmse_percent": 3.2382328151294355,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00359765044413507,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.0038229520432651043,
                  "rgb_channel": 0,
                  "sky_patch_index": 311
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005508707836270332,
                  "p50": 2.437545276734454e-09,
                  "p90": 7.952214218676092e-06,
                  "p95": 1.4844223187537864e-05,
                  "p99": 7.866899250075221e-05
                },
                "candidate_energy": 2.7399126356595254,
                "cvrmse_percent": 36.39661878758277,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.0642421933462755,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.738153585738857,
                "relative_energy_error_percent": 0.0642421933462755,
                "rms_normalized_rmse_percent": 1.997160308031027,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.029340720735490322,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.02878984995186329,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 190.70558296516538,
            "full": 4191.8922499753535
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 188.53074999060482,
            "full": 4194.537917035632
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.27383303828537,
            "full": 4282.431959058158
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 187.0330829406157,
            "full": 4297.948000021279
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/clerestory/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2837.8137089312077,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/clerestory/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10588.480209000409,
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
        "identifier": "clerestory_grid",
        "full_identifier": "clerestory_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.009082975179435597,
            "cvrmse_percent": 9.123210124017183,
            "rms_normalized_rmse_percent": 1.2929544896585525,
            "reference_energy": 2.6379202031350815,
            "candidate_energy": 2.6381598047723855,
            "relative_energy_error_percent": 0.009082975179435598,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.924438402056694e-05,
              "maximum": 8.170245564542711e-05
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 415,
              "rgb_channel": 0,
              "reference": 0.0004859736072830856,
              "candidate": 0.0004042711516376585,
              "position": [
                3.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.947900942666308,
            "cvrmse_percent": 67.78117405550073,
            "rms_normalized_rmse_percent": 3.7173934513201075,
            "reference_energy": 2.7387889856448915,
            "candidate_energy": 2.6854400891758736,
            "relative_energy_error_percent": 1.947900942666308,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.4999996739438757e-08,
              "p90": 9.25405984162353e-06,
              "p95": 1.539763479740941e-05,
              "p99": 3.980715700890869e-05,
              "maximum": 0.0014154687523841858
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03286643698811531,
              "candidate": 0.031450968235731125,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.9877658055700943,
            "cvrmse_percent": 34.45940770895492,
            "rms_normalized_rmse_percent": 3.7101820984558302,
            "reference_energy": 5.376709188779973,
            "candidate_energy": 5.323599893948259,
            "relative_energy_error_percent": 0.9877658055700943,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.4999996739438757e-08,
              "p90": 9.206646063830719e-06,
              "p95": 1.5177472960203886e-05,
              "p99": 3.858741547446698e-05,
              "maximum": 0.0014154687523841858
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03286643698811531,
              "candidate": 0.031450968235731125,
              "position": [
                3.5,
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
        "identifier": "clerestory_grid",
        "full_identifier": "clerestory_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.009082975179435597,
            "cvrmse_percent": 9.123210124017183,
            "rms_normalized_rmse_percent": 1.2929544896585525,
            "reference_energy": 2.6379202031350815,
            "candidate_energy": 2.6381598047723855,
            "relative_energy_error_percent": 0.009082975179435598,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.924438402056694e-05,
              "maximum": 8.170245564542711e-05
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 415,
              "rgb_channel": 0,
              "reference": 0.0004859736072830856,
              "candidate": 0.0004042711516376585,
              "position": [
                3.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 69.10393403928639,
            "cvrmse_percent": 673.6066048047503,
            "rms_normalized_rmse_percent": 27.0623933982562,
            "reference_energy": 1.5880411679553177,
            "candidate_energy": 2.6854400891758736,
            "relative_energy_error_percent": 69.10393403928639,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.792806410274363e-05,
              "p95": 5.246259388513863e-05,
              "p99": 0.00011846190318465233,
              "maximum": 0.005734255537390709
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.012850034981966019,
              "candidate": 0.018584290519356728,
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
            "nmbe_percent": 25.973699863106958,
            "cvrmse_percent": 253.1340292885152,
            "rms_normalized_rmse_percent": 27.062889506796843,
            "reference_energy": 4.225961371090399,
            "candidate_energy": 5.323599893948259,
            "relative_energy_error_percent": 25.973699863106958,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.8054476453908145e-05,
              "p95": 5.246259388513863e-05,
              "p99": 0.00011745635129045695,
              "maximum": 0.005734255537390709
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.012850034981966019,
              "candidate": 0.018584290519356728,
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
      "bias_percent": 0.24928613421182655,
      "rms_normalized_error_percent": 0.5654894940244538,
      "absolute_error": {
        "p95": 0.08573425697135284,
        "p99": 0.09649485739760796,
        "maximum": 0.09706466481845855
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.104683887807923,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.5654894940244538
    },
    "overcast": {
      "bias_percent": 0.18795209088664835,
      "rms_normalized_error_percent": 0.4291830100839732,
      "absolute_error": {
        "p95": 0.0397205650806427,
        "p99": 0.05255873203277586,
        "maximum": 0.057125091552734375
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.155035972595215,
      "reference_fraction_of_uniform": 0.6806308031082153,
      "rms_normalized_to_uniform_percent": 0.30624731222375684
    },
    "horizon": {
      "bias_percent": 1.482263426655684,
      "rms_normalized_error_percent": 3.876956827190254,
      "absolute_error": {
        "p95": 0.037835843573154684,
        "p99": 0.042952504736843145,
        "maximum": 0.045473822995369284
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.49849718155726247,
      "reference_fraction_of_uniform": 0.08165814818894143,
      "rms_normalized_to_uniform_percent": 0.30108856932477157
    },
    "north": {
      "bias_percent": -74.19450287169435,
      "rms_normalized_error_percent": 93.589217069891,
      "absolute_error": {
        "p95": 1.5281731037930513e-05,
        "p99": 5.615898762698626e-05,
        "maximum": 7.659715629415587e-05
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 5.662244802806526e-06,
      "reference_fraction_of_uniform": 9.275246384277125e-07,
      "rms_normalized_to_uniform_percent": 0.0002116712810362181
    },
    "east": {
      "bias_percent": -0.14621117007194814,
      "rms_normalized_error_percent": 0.7132339031916696,
      "absolute_error": {
        "p95": 0.02305459976196289,
        "p99": 0.032741606235504137,
        "maximum": 0.035852909088134766
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.0675854682922363,
      "reference_fraction_of_uniform": 0.17487972974777222,
      "rms_normalized_to_uniform_percent": 0.15096142568698756
    },
    "south": {
      "bias_percent": 0.3874418242972675,
      "rms_normalized_error_percent": 0.7476397125740584,
      "absolute_error": {
        "p95": 0.06533259153366089,
        "p99": 0.08945821523666378,
        "maximum": 0.09781312942504883
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.0942816734313965,
      "reference_fraction_of_uniform": 0.6706787347793579,
      "rms_normalized_to_uniform_percent": 0.4990993587811853
    },
    "west": {
      "bias_percent": -0.01230592484726252,
      "rms_normalized_error_percent": 0.5483957490342761,
      "absolute_error": {
        "p95": 0.011203810572624207,
        "p99": 0.0241023816168308,
        "maximum": 0.0305328369140625
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.0766186714172363,
      "reference_fraction_of_uniform": 0.17635944485664368,
      "rms_normalized_to_uniform_percent": 0.1162655643436181
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
        "identifier": "clerestory_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.12231090230164282,
          "cvrmse_percent": 3.5687999884486143,
          "absolute_error_percentiles_lux": {
            "p50": 1.9449691772460938,
            "p90": 21.582073974609376,
            "p95": 35.273742675781236,
            "p99": 90.50601074218746
          },
          "maximum_absolute_error_lux": 368.97265625,
          "worst": {
            "sensor_index": 22,
            "position": [
              3.5,
              1.5,
              0.75
            ],
            "hour_of_year": 2962.5,
            "foton_lux": 23201.921875,
            "radiance_lux": 23570.89453125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.4203500761035006,
            "maximum_error_percentage_points": 1.2610958904109566,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.18656660944101666,
            "maximum_error_percentage_points": 0.5546380874501011,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.15381659056316563,
            "maximum_error_percentage_points": 0.6034246575342479,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.15564307458142876,
            "maximum_error_percentage_points": 0.6063013698630186,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.027149923896499204,
            "maximum_error_percentage_points": 0.11013698630136992,
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
      "maximum_error_percentage_points": 0.004947559931508749,
      "metrics": {
        "da": [
          {
            "identifier": "clerestory_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "clerestory_grid",
            "maximum_error_percentage_points": 0.004947559931508749,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "clerestory_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "clerestory_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "clerestory_grid",
            "maximum_error_percentage_points": 0.004383561643835632,
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
      "study_preparation_seconds": 0.3700973279992468,
      "weather_seconds": 0.2534023700027319,
      "metric_reduction_seconds": 1.070466208999278,
      "write_seconds": 0.02379035199919599,
      "total_seconds": 1.3479859340004623,
      "cold_end_to_end_seconds": 1.718083261999709,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.011805809001089074,
      "engine_upload_seconds": 0.04457161999999999,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.038626132,
      "engine_annual_reduction_seconds": 0.01978044,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.038626132
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3700973279992468,
      "weather_seconds": 0.23135690200069803,
      "metric_reduction_seconds": 1.0027885210001841,
      "write_seconds": 0.02099949700277648,
      "total_seconds": 1.2554810820001876,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 1.2554810820001876,
      "raw_export_seconds": 0.008297349002532428,
      "engine_upload_seconds": 0.044932601,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.3e-08,
      "engine_annual_reduction_seconds": 0.019920221,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.018122795001545455,
      "full": 0.05168681899885996
    }
  },
  "elapsed_seconds": 5.6247750660004385,
  "result_class": "passed"
}
```
