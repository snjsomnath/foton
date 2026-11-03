# Foton report

Status: **passed**

```json
{
  "scene": "asymmetric_fins",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "asymmetric_fins",
    "category": "shading",
    "question": "Do unequal fins produce different east and west sky masks?",
    "interactions": [
      "fins",
      "asymmetric_shading"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 2,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "f20c51722c12af91dc382c20bfbe03a93fc78f378112a5153c61ef44f767afac",
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
      "scene_fingerprint": 12247094324704974908,
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 12247094324704974908,
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
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 262144,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/foton-references-corpus4-2026-11-03",
    "model_sha256": "f804216acbb9232aa7fda96d823b626095bdd036a0e10dce3b34a7ee3a194380",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "42ebbd5873d9863a0ad3aca60e92d9e55c1ae842623c6cc1f4949849ae92cd10",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00014028436271473765,
          "p95": 2.7939677238464355e-09,
          "p99": 1.0647345334291458e-05
        },
        "bias_percent": -0.04724060476740068,
        "identifier": "asymmetric_fins_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.028605338271547,
        "worst_index": [
          17,
          543,
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
          "maximum": 0.0005720555782318115,
          "p95": 1.7019898223225027e-05,
          "p99": 9.092548862099648e-05
        },
        "bias_percent": 0.13352170313935088,
        "identifier": "asymmetric_fins_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.902485671439498,
        "worst_index": [
          32,
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
          "maximum": 0.0004382450133562088,
          "p95": 1.4317265595309436e-05,
          "p99": 7.437798194587231e-05
        },
        "bias_percent": -0.09011184492061225,
        "identifier": "asymmetric_fins_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.5112442925163778,
        "worst_index": [
          28,
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
            "identifier": "asymmetric_fins_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00042352247692178935,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0001407706949976273
                },
                "candidate_energy": 4.716016478079837,
                "cvrmse_percent": 33.88614329680694,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.009789962912651027,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.715554827011147,
                "relative_energy_error_percent": 0.009789962912651027,
                "rms_normalized_rmse_percent": 5.750905584678759,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001177260754047893,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.0007537382771261036,
                  "rgb_channel": 0,
                  "sky_patch_index": 89
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009009183631860651,
                  "p50": 0.0,
                  "p90": 9.063345078175193e-06,
                  "p95": 2.5923502107616514e-05,
                  "p99": 0.00022682399139739573
                },
                "candidate_energy": 1.7890672051663188,
                "cvrmse_percent": 152.23995996213827,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.38700144654451557,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.782170180786789,
                "relative_energy_error_percent": 0.38700144654451557,
                "rms_normalized_rmse_percent": 5.7047374204819405,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00041835159208858386,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.00048256677109748125,
                  "rgb_channel": 0,
                  "sky_patch_index": 89
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 122.82712501473725,
            "full": 236.0922920051962
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 109.32575003243983,
            "full": 228.5524590406567
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 108.73800003901124,
            "full": 232.2159999748692
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 108.85516600683331,
            "full": 231.0570830013603
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.50554197654128,
            "full": 236.13962507806718
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.91916701197624,
            "full": 237.12195793632418
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.72987500019372,
            "full": 229.9557919614017
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 106.48175003007054,
            "full": 233.67554205469787
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
            "identifier": "asymmetric_fins_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004204880679026246,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00011693051783367991
                },
                "candidate_energy": 4.721063958580089,
                "cvrmse_percent": 28.009931528505867,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0503259739920065,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.718689232264296,
                "relative_energy_error_percent": 0.0503259739920065,
                "rms_normalized_rmse_percent": 4.758862210789661,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003667863900773227,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.004088351968675852,
                  "rgb_channel": 0,
                  "sky_patch_index": 362
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006517898291349411,
                  "p50": 6.393028684215096e-07,
                  "p90": 1.2732047889585383e-05,
                  "p95": 2.51532410402433e-05,
                  "p99": 0.00018251698929816484
                },
                "candidate_energy": 3.2508666536947572,
                "cvrmse_percent": 63.87471945023136,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.11000906295529359,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.2544468401680042,
                "relative_energy_error_percent": 0.11000906295529359,
                "rms_normalized_rmse_percent": 3.414009071812483,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.024281149730086327,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.023629359900951385,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.36795803904533,
            "full": 2309.025041991845
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.77425001375377,
            "full": 2372.680624946952
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.34900008887053,
            "full": 2373.3250410296023
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.5373749807477,
            "full": 2392.4898749683052
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
            "identifier": "asymmetric_fins_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00048400857485830784,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.6007106751203537e-09,
                  "p99": 0.00011746180825866759
                },
                "candidate_energy": 4.719047567589314,
                "cvrmse_percent": 28.74432417205321,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.05324535451010916,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.721561579790887,
                "relative_energy_error_percent": 0.053245354510109165,
                "rms_normalized_rmse_percent": 4.884741383384886,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003690067445859313,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.004174076020717621,
                  "rgb_channel": 0,
                  "sky_patch_index": 363
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006279544904828072,
                  "p50": 6.247108679247049e-07,
                  "p90": 1.2552631187645605e-05,
                  "p95": 2.447699080221355e-05,
                  "p99": 0.00018087762873619795
                },
                "candidate_energy": 3.266132988853471,
                "cvrmse_percent": 63.0292878654842,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.19997459715688667,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.259614587712825,
                "relative_energy_error_percent": 0.1999745971568867,
                "rms_normalized_rmse_percent": 3.3731672916392803,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.017804745584726334,
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "reference": 0.01843270007520914,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.22462493833154,
            "full": 2521.804541000165
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.56725007947534,
            "full": 2512.053625076078
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.89337494503707,
            "full": 2480.8850419940427
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.7361249960959,
            "full": 2477.4657080415636
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
            "identifier": "asymmetric_fins_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002637164434418082,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.752088665962219e-09,
                  "p99": 5.865003913640976e-05
                },
                "candidate_energy": 4.717979205353004,
                "cvrmse_percent": 14.802579331626337,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.02445546646699481,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.719133291412618,
                "relative_energy_error_percent": 0.024455466466994806,
                "rms_normalized_rmse_percent": 2.5158311577777237,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001240812533069402,
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "reference": 0.0015045289765112102,
                  "rgb_channel": 0,
                  "sky_patch_index": 155
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004923492670059204,
                  "p50": 5.087959227267902e-07,
                  "p90": 8.885536408342895e-06,
                  "p95": 1.681637149886228e-05,
                  "p99": 9.546952787786722e-05
                },
                "candidate_energy": 3.258376111513897,
                "cvrmse_percent": 36.534174682280266,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.05820771980744626,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.256480588417407,
                "relative_energy_error_percent": 0.05820771980744627,
                "rms_normalized_rmse_percent": 1.9569658014511817,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.022810104303061962,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.02231775503605604,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 191.36241695377976,
            "full": 4356.674707960337
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 207.06441707443446,
            "full": 4339.595083030872
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 225.45408294536173,
            "full": 4415.18479201477
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 206.10449998639524,
            "full": 4358.658375102095
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/asymmetric_fins/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2647.2778749885038,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/asymmetric_fins/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10866.442750091664,
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
        "identifier": "asymmetric_fins_grid",
        "full_identifier": "asymmetric_fins_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.022270189409765433,
            "cvrmse_percent": 3.132803836963575,
            "rms_normalized_rmse_percent": 0.5324561238667606,
            "reference_energy": 4.720191229616262,
            "candidate_energy": 4.719140034088923,
            "relative_energy_error_percent": 0.022270189409765433,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.862645149230957e-09,
              "p99": 7.471186108887196e-06,
              "maximum": 6.395229138433933e-05
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 354,
              "rgb_channel": 0,
              "reference": 0.002199798822402954,
              "candidate": 0.0022637511137872934,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.862870604734312,
            "cvrmse_percent": 39.26090676606739,
            "rms_normalized_rmse_percent": 2.1024140540293996,
            "reference_energy": 3.2557933540660873,
            "candidate_energy": 3.2277000702629577,
            "relative_energy_error_percent": 0.862870604734312,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.930710938490847e-07,
              "p90": 8.80703446455304e-06,
              "p95": 1.46778274938697e-05,
              "p99": 4.221312701702118e-05,
              "maximum": 0.0008215121924877167
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026623792946338654,
              "candidate": 0.025802280753850937,
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
            "nmbe_percent": -0.3654029044902298,
            "cvrmse_percent": 16.009402262978334,
            "rms_normalized_rmse_percent": 2.1001993315177727,
            "reference_energy": 7.975984583682349,
            "candidate_energy": 7.946840104351881,
            "relative_energy_error_percent": 0.3654029044902298,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.916587835803512e-07,
              "p90": 8.7594891738263e-06,
              "p95": 1.4510704204440117e-05,
              "p99": 4.1942461393773556e-05,
              "maximum": 0.0008215121924877167
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026623792946338654,
              "candidate": 0.025802280753850937,
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
        "identifier": "asymmetric_fins_grid",
        "full_identifier": "asymmetric_fins_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.022270189409765433,
            "cvrmse_percent": 3.132803836963575,
            "rms_normalized_rmse_percent": 0.5324561238667606,
            "reference_energy": 4.720191229616262,
            "candidate_energy": 4.719140034088923,
            "relative_energy_error_percent": 0.022270189409765433,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.862645149230957e-09,
              "p99": 7.471186108887196e-06,
              "maximum": 6.395229138433933e-05
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 354,
              "rgb_channel": 0,
              "reference": 0.002199798822402954,
              "candidate": 0.0022637511137872934,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.20796387197338,
            "cvrmse_percent": 856.3429385873119,
            "rms_normalized_rmse_percent": 32.08000003443519,
            "reference_energy": 1.7812131438899588,
            "candidate_energy": 3.2277000702629577,
            "relative_energy_error_percent": 81.20796387197338,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.5499999790336005e-06,
              "p90": 4.830000034417026e-05,
              "p95": 6.76107665640302e-05,
              "p99": 0.00012649386189877987,
              "maximum": 0.0065872082486748695
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.013222982175648212,
              "candidate": 0.019810190424323082,
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
            "nmbe_percent": 22.232669248138674,
            "cvrmse_percent": 234.6149783161052,
            "rms_normalized_rmse_percent": 32.07994846987672,
            "reference_energy": 6.501404373506221,
            "candidate_energy": 7.946840104351881,
            "relative_energy_error_percent": 22.232669248138674,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.550442448206013e-06,
              "p90": 4.84241856611334e-05,
              "p95": 6.772999768145382e-05,
              "p99": 0.00012554400018416345,
              "maximum": 0.0065872082486748695
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.013222982175648212,
              "candidate": 0.019810190424323082,
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
      "bias_percent": 0.17690219499039733,
      "rms_normalized_error_percent": 0.20421546165469387,
      "absolute_error": {
        "p95": 0.06248734881345763,
        "p99": 0.08833147802564813,
        "maximum": 0.10112186508756205
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.632735353920111,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.20421546165469387
    },
    "overcast": {
      "bias_percent": 0.10980334719391527,
      "rms_normalized_error_percent": 0.13825843854724124,
      "absolute_error": {
        "p95": 0.033613741397857666,
        "p99": 0.042008274793624865,
        "maximum": 0.044686198234558105
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.295116424560547,
      "reference_fraction_of_uniform": 0.6535128951072693,
      "rms_normalized_to_uniform_percent": 0.10037006482404347
    },
    "horizon": {
      "bias_percent": 1.1665192050079274,
      "rms_normalized_error_percent": 1.9446404241226383,
      "absolute_error": {
        "p95": 0.046138209168516936,
        "p99": 0.05832540387186281,
        "maximum": 0.0626492006406909
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.0585209008943783,
      "reference_fraction_of_uniform": 0.10988788355569279,
      "rms_normalized_to_uniform_percent": 0.1336687278297293
    },
    "north": {
      "bias_percent": -1.7193442770661347,
      "rms_normalized_error_percent": 6.991882976261403,
      "absolute_error": {
        "p95": 0.0014862681273370981,
        "p99": 0.0019995154347270724,
        "maximum": 0.0020445045083761215
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 0.006268875673413277,
      "reference_fraction_of_uniform": 0.0006507887155748904,
      "rms_normalized_to_uniform_percent": 0.0042002816644012226
    },
    "east": {
      "bias_percent": -0.037326346248925765,
      "rms_normalized_error_percent": 0.2435756697951426,
      "absolute_error": {
        "p95": 0.010292530059814453,
        "p99": 0.014430809020996088,
        "maximum": 0.015863418579101562
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.2908544540405273,
      "reference_fraction_of_uniform": 0.1340070515871048,
      "rms_normalized_to_uniform_percent": 0.036478721942930475
    },
    "south": {
      "bias_percent": 0.2705239035724303,
      "rms_normalized_error_percent": 0.2860049539229244,
      "absolute_error": {
        "p95": 0.06302177906036377,
        "p99": 0.0840289711952209,
        "maximum": 0.09454464912414551
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.799983978271484,
      "reference_fraction_of_uniform": 0.7059245109558105,
      "rms_normalized_to_uniform_percent": 0.1896164901333684
    },
    "west": {
      "bias_percent": 0.10145698840735899,
      "rms_normalized_error_percent": 0.22941964271053455,
      "absolute_error": {
        "p95": 0.014627635478973389,
        "p99": 0.023710262775421133,
        "maximum": 0.02647542953491211
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.9485564231872559,
      "reference_fraction_of_uniform": 0.20228485763072968,
      "rms_normalized_to_uniform_percent": 0.05044691219766087
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
        "identifier": "asymmetric_fins_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.06200313590263245,
          "cvrmse_percent": 2.092870827129619,
          "absolute_error_percentiles_lux": {
            "p50": 1.9444580078125,
            "p90": 21.14348754882814,
            "p95": 33.45242004394531,
            "p99": 73.27224609374986
          },
          "maximum_absolute_error_lux": 493.728515625,
          "worst": {
            "sensor_index": 10,
            "position": [
              1.5,
              1.5,
              0.75
            ],
            "hour_of_year": 2674.5,
            "foton_lux": 18121.4921875,
            "radiance_lux": 18615.220703125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.352838660578385,
            "maximum_error_percentage_points": 0.9846575342465798,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.15142632053412836,
            "maximum_error_percentage_points": 0.776556111138639,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.13772070015220653,
            "maximum_error_percentage_points": 0.7368493150684898,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.14613013698630203,
            "maximum_error_percentage_points": 0.8184931506849296,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.032127092846271056,
            "maximum_error_percentage_points": 0.16684931506848955,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 41.666666666666664,
          "radiance_percent": 38.888888888888886,
          "difference_percentage_points": 2.7777777777777786,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 1,
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
      "maximum_error_percentage_points": 0.004988227739715967,
      "metrics": {
        "da": [
          {
            "identifier": "asymmetric_fins_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "asymmetric_fins_grid",
            "maximum_error_percentage_points": 0.004988227739715967,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "asymmetric_fins_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "asymmetric_fins_grid",
            "maximum_error_percentage_points": 0.004794520547942938,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "asymmetric_fins_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
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
      "study_preparation_seconds": 0.005904417019337416,
      "weather_seconds": 0.09496220899745822,
      "metric_reduction_seconds": 0.12603120796848089,
      "write_seconds": 0.04789304197765887,
      "total_seconds": 0.2690411669900641,
      "cold_end_to_end_seconds": 0.2749455840094015,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.010719042038545012,
      "engine_upload_seconds": 0.000804709,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.07502250000834465,
      "engine_annual_reduction_seconds": 0.0015107500366866589,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.07502250000834465
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.005904417019337416,
      "weather_seconds": 0.10342879104427993,
      "metric_reduction_seconds": 0.045596082927659154,
      "write_seconds": 0.03958262503147125,
      "total_seconds": 0.18902358307968825,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.18902358307968825,
      "raw_export_seconds": 0.013474583043716848,
      "engine_upload_seconds": 7.7042e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0014483750564977527,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.018670749966986477,
      "full": 0.08168900001328439
    }
  },
  "elapsed_seconds": 1.272502167033963,
  "result_class": "passed"
}
```
