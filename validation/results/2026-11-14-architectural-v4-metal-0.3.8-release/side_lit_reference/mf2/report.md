# Foton report

Status: **passed**

```json
{
  "scene": "side_lit_reference",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "side_lit_reference",
    "category": "controls",
    "question": "What is the clear-glazed south-facing reference room?",
    "interactions": [
      "side_glazing",
      "baseline"
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
    "aperture_area": 2.999999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "6a286c9e183235228e936476ca38eee785b2c4fe24c9568fce8a4fc6d8fcee94",
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
      "scene_fingerprint": 7066839344617655963,
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
      "scene_fingerprint": 7066839344617655963,
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
    "model_sha256": "b89a1ff2bb9c4d64b45a1cb2fbbd56afe2de174bd64068c5cfefb7b5b10947bb",
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
          "maximum": 0.00014028436271473765,
          "p95": 3.259629011154175e-08,
          "p99": 7.011898560449481e-06
        },
        "bias_percent": -0.02574736435175291,
        "identifier": "side_lit_reference_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7597631247218805,
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
          "maximum": 0.0004994533956050873,
          "p95": 2.2038992028683424e-05,
          "p99": 0.00010130438022315502
        },
        "bias_percent": 0.06178381109020613,
        "identifier": "side_lit_reference_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.7675208558303503,
        "worst_index": [
          16,
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
          "maximum": 0.0005503185093402863,
          "p95": 1.7326638044323772e-05,
          "p99": 8.410215377807617e-05
        },
        "bias_percent": -0.0072632368204568615,
        "identifier": "side_lit_reference_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.466303077756913,
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
            "identifier": "side_lit_reference_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005466556176543236,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.376488919253461e-05,
                  "p99": 0.00018082500901073217
                },
                "candidate_energy": 6.02459423160326,
                "cvrmse_percent": 32.70391905144069,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.08478592826178444,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.0194905506632495,
                "relative_energy_error_percent": 0.08478592826178444,
                "rms_normalized_rmse_percent": 6.286360055841596,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004715425428003073,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.004168769810348749,
                  "rgb_channel": 0,
                  "sky_patch_index": 515
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009075472480617464,
                  "p50": 0.0,
                  "p90": 5.657923838953145e-06,
                  "p95": 5.2890271035721526e-05,
                  "p99": 0.00033195604919455945
                },
                "candidate_energy": 2.077930987911447,
                "cvrmse_percent": 181.59808711172937,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.2602678577149875,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.072536840675866,
                "relative_energy_error_percent": 0.26026785771498745,
                "rms_normalized_rmse_percent": 6.817459622643136,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00013072631554678082,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.0007768209325149655,
                  "rgb_channel": 0,
                  "sky_patch_index": 89
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 113.87666594237089,
            "full": 231.3800830161199
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 102.3728339932859,
            "full": 215.28825000859797
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.29387498274446,
            "full": 229.59812497720122
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 115.0924590183422,
            "full": 228.0554169556126
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
            "identifier": "side_lit_reference_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00029326175717869774,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2754784367862158e-05,
                  "p99": 0.00013723256415687501
                },
                "candidate_energy": 6.017036546610143,
                "cvrmse_percent": 24.734326800199067,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.021888291321411027,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.015719808333415,
                "relative_energy_error_percent": 0.021888291321411023,
                "rms_normalized_rmse_percent": 4.770017688944099,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.000248177551839035,
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "reference": 0.0005414393090177327,
                  "rgb_channel": 0,
                  "sky_patch_index": 37
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005887942388653755,
                  "p50": 2.361497308811522e-08,
                  "p90": 1.3763741378625181e-05,
                  "p95": 3.603792174544651e-05,
                  "p99": 0.00020251100067980587
                },
                "candidate_energy": 3.8199396093422138,
                "cvrmse_percent": 60.26008739931526,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.20568764734948095,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8120985934307434,
                "relative_energy_error_percent": 0.20568764734948092,
                "rms_normalized_rmse_percent": 3.229570181055109,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.01890381518751383,
                  "global_sensor_index": 35,
                  "local_sensor_index": 35,
                  "reference": 0.019492609426379204,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.37870800308883,
            "full": 2265.921249985695
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.82125006522983,
            "full": 2284.5329999690875
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.77554192207754,
            "full": 2228.0696659581736
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.3167500346899,
            "full": 2246.6107920045033
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
            "identifier": "side_lit_reference_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004390920512378216,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1899802959524095e-05,
                  "p99": 0.00011471693869680166
                },
                "candidate_energy": 6.013045393427092,
                "cvrmse_percent": 22.043718392506193,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.09966808112327497,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.019044459541874,
                "relative_energy_error_percent": 0.09966808112327495,
                "rms_normalized_rmse_percent": 4.2487878880569765,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0034432074753567576,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.0038822995265945792,
                  "rgb_channel": 0,
                  "sky_patch_index": 317
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006700429366901517,
                  "p50": 2.0786027121744155e-08,
                  "p90": 1.3074670459900518e-05,
                  "p95": 3.49029760400299e-05,
                  "p99": 0.00018299708608537912
                },
                "candidate_energy": 3.826153964434287,
                "cvrmse_percent": 56.62621069502465,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.19518697308812571,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.818700358792654,
                "relative_energy_error_percent": 0.1951869730881257,
                "rms_normalized_rmse_percent": 3.037234337248458,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00040186860132962465,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": -0.00026817433536052704,
                  "rgb_channel": 0,
                  "sky_patch_index": 267
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.24337500613183,
            "full": 2459.3838750151917
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.94591699540615,
            "full": 2412.469125003554
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.1386250294745,
            "full": 2428.3172499854118
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.92287493217736,
            "full": 2403.0927079729736
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
            "identifier": "side_lit_reference_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002219754969701171,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1314812581986189e-05,
                  "p99": 7.008458487689495e-05
                },
                "candidate_energy": 6.015612187395163,
                "cvrmse_percent": 14.80124444613194,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.003946738962017926,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.0153747762551575,
                "relative_energy_error_percent": 0.003946738962017926,
                "rms_normalized_rmse_percent": 2.8535105889166554,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0016105370013974607,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.0018325124983675778,
                  "rgb_channel": 0,
                  "sky_patch_index": 150
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007361499592661858,
                  "p50": 3.36913643650405e-08,
                  "p90": 9.277163553633743e-06,
                  "p95": 2.3209209757624194e-05,
                  "p99": 0.00012405649613356218
                },
                "candidate_energy": 3.824475994561009,
                "cvrmse_percent": 39.73846944909462,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.11580796047907915,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8200520701693073,
                "relative_energy_error_percent": 0.11580796047907917,
                "rms_normalized_rmse_percent": 2.131316719961453,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.026034359820187092,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.026770509779453278,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 200.61354106292129,
            "full": 4261.957417009398
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 200.62683301512152,
            "full": 4339.72054196056
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 201.62462501320988,
            "full": 4234.305290970951
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 203.0127499019727,
            "full": 4284.828916075639
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
    "/Users/ssanjay/GitHub/foton-0.3.8/validation/results/2026-11-14-architectural-v4-metal-0.3.8-release/side_lit_reference/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2550.4249579971656,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/side_lit_reference/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10842.784250038676,
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
        "identifier": "side_lit_reference_grid",
        "full_identifier": "side_lit_reference_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.02545918042736604,
            "cvrmse_percent": 2.1862248649500637,
            "rms_normalized_rmse_percent": 0.4217274666145703,
            "reference_energy": 6.016160269848569,
            "candidate_energy": 6.014628604750669,
            "relative_energy_error_percent": 0.02545918042736604,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.1525920601561666e-08,
              "p99": 6.127869710326195e-06,
              "maximum": 5.9494748711586e-05
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052893467247486,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.0089793526077442,
            "cvrmse_percent": 42.9023511802112,
            "rms_normalized_rmse_percent": 2.300679199330832,
            "reference_energy": 3.821597242870835,
            "candidate_energy": 3.7830381157504416,
            "relative_energy_error_percent": 1.0089793526077442,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.0025586379924807e-05,
              "p95": 1.6746187611715868e-05,
              "p99": 4.402897320687771e-05,
              "maximum": 0.0009939242154359818
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.028719404712319374,
              "candidate": 0.027725480496883392,
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
            "nmbe_percent": -0.40751962189004703,
            "cvrmse_percent": 16.64666630786758,
            "rms_normalized_rmse_percent": 2.2980181002983655,
            "reference_energy": 9.837757512719405,
            "candidate_energy": 9.79766672050111,
            "relative_energy_error_percent": 0.40751962189004703,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 9.965045319404464e-06,
              "p95": 1.65355704666581e-05,
              "p99": 4.369881935417652e-05,
              "maximum": 0.0009939242154359818
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.028719404712319374,
              "candidate": 0.027725480496883392,
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
        "identifier": "side_lit_reference_grid",
        "full_identifier": "side_lit_reference_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.02545918042736604,
            "cvrmse_percent": 2.1862248649500637,
            "rms_normalized_rmse_percent": 0.4217274666145703,
            "reference_energy": 6.016160269848569,
            "candidate_energy": 6.014628604750669,
            "relative_energy_error_percent": 0.02545918042736604,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.1525920601561666e-08,
              "p99": 6.127869710326195e-06,
              "maximum": 5.9494748711586e-05
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052893467247486,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.77929737129759,
            "cvrmse_percent": 857.2935955681705,
            "rms_normalized_rmse_percent": 32.25754257378812,
            "reference_energy": 2.081116040416477,
            "candidate_energy": 3.7830381157504416,
            "relative_energy_error_percent": 81.7792973712976,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.7199998991563916e-05,
              "p95": 8.006000280147418e-05,
              "p99": 0.0001792238326743245,
              "maximum": 0.007678337395191193
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.013023372739553452,
              "candidate": 0.020701710134744644,
              "position": [
                5.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.999535462072007,
            "cvrmse_percent": 220.3289034913123,
            "rms_normalized_rmse_percent": 32.25639551719592,
            "reference_energy": 8.097276310265046,
            "candidate_energy": 9.79766672050111,
            "relative_energy_error_percent": 20.99953546207201,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.71869990380947e-05,
              "p95": 8.001504465937614e-05,
              "p99": 0.00017921184189617634,
              "maximum": 0.007678337395191193
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.013023372739553452,
              "candidate": 0.020701710134744644,
              "position": [
                5.5,
                3.5,
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
      "bias_percent": 0.18675345927689246,
      "rms_normalized_error_percent": 0.18191664044113537,
      "absolute_error": {
        "p95": 0.07324313112005032,
        "p99": 0.10547329414054861,
        "maximum": 0.11999824106645152
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 12.024353571444472,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.18191664044113537
    },
    "overcast": {
      "bias_percent": 0.12458081991398547,
      "rms_normalized_error_percent": 0.12168050811811446,
      "absolute_error": {
        "p95": 0.0326518714427948,
        "p99": 0.04611491560935972,
        "maximum": 0.05013298988342285
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.696842670440674,
      "reference_fraction_of_uniform": 0.6401044726371765,
      "rms_normalized_to_uniform_percent": 0.0865397303136915
    },
    "horizon": {
      "bias_percent": 1.0801835018587749,
      "rms_normalized_error_percent": 1.8228710055691926,
      "absolute_error": {
        "p95": 0.06416256037666379,
        "p99": 0.07469985978628857,
        "maximum": 0.07546137759834792
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.4436392327850354,
      "reference_fraction_of_uniform": 0.12005961270245753,
      "rms_normalized_to_uniform_percent": 0.1283125437904371
    },
    "north": {
      "bias_percent": -91.65497755917998,
      "rms_normalized_error_percent": 99.88032759651966,
      "absolute_error": {
        "p95": 0.00013233710975057988,
        "p99": 0.00021347398287616657,
        "maximum": 0.00024381418188568205
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.94310923689045e-05,
      "reference_fraction_of_uniform": 1.6159780216185027e-06,
      "rms_normalized_to_uniform_percent": 0.0002494634300685491
    },
    "east": {
      "bias_percent": 0.07312711663228325,
      "rms_normalized_error_percent": 0.2310327790104682,
      "absolute_error": {
        "p95": 0.016511499881744385,
        "p99": 0.033382737636566136,
        "maximum": 0.03992486000061035
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.274726152420044,
      "reference_fraction_of_uniform": 0.18917657434940338,
      "rms_normalized_to_uniform_percent": 0.046445059080392224
    },
    "south": {
      "bias_percent": 0.25214939239593814,
      "rms_normalized_error_percent": 0.25719184314243465,
      "absolute_error": {
        "p95": 0.07386022806167603,
        "p99": 0.09997520446777339,
        "maximum": 0.11348319053649902
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.363171577453613,
      "reference_fraction_of_uniform": 0.6955193877220154,
      "rms_normalized_to_uniform_percent": 0.16799846020950246
    },
    "west": {
      "bias_percent": 0.1257053358308658,
      "rms_normalized_error_percent": 0.1397665268436639,
      "absolute_error": {
        "p95": 0.010986000299453735,
        "p99": 0.017206078767776488,
        "maximum": 0.01745128631591797
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.3024981021881104,
      "reference_fraction_of_uniform": 0.19148622453212738,
      "rms_normalized_to_uniform_percent": 0.028321659209325844
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
        "identifier": "side_lit_reference_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.06039879953315105,
          "cvrmse_percent": 1.76811691771078,
          "absolute_error_percentiles_lux": {
            "p50": 1.9923095703125,
            "p90": 23.359838867187502,
            "p95": 36.91520996093749,
            "p99": 81.2048144531249
          },
          "maximum_absolute_error_lux": 322.75537109375,
          "worst": {
            "sensor_index": 16,
            "position": [
              2.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5243.5,
            "foton_lux": 8341.197265625,
            "radiance_lux": 8018.44189453125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.28866438356164337,
            "maximum_error_percentage_points": 1.5639726027397245,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.11417821836116776,
            "maximum_error_percentage_points": 0.7075816450598182,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.0898211567732119,
            "maximum_error_percentage_points": 0.4639726027397266,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.08653729071537342,
            "maximum_error_percentage_points": 0.43890410958904624,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.020563165905631724,
            "maximum_error_percentage_points": 0.08506849315068499,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 55.55555555555556,
          "radiance_percent": 55.55555555555556,
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
            "identifier": "side_lit_reference_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "side_lit_reference_grid",
            "maximum_error_percentage_points": 0.004924282962321058,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "side_lit_reference_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "side_lit_reference_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "side_lit_reference_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
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
      "study_preparation_seconds": 0.007084124954417348,
      "weather_seconds": 0.1016802079975605,
      "metric_reduction_seconds": 0.11723650014027953,
      "write_seconds": 0.02192183304578066,
      "total_seconds": 0.24094375013373792,
      "cold_end_to_end_seconds": 0.24802787508815527,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.004577917046844959,
      "engine_upload_seconds": 0.001051375,
      "engine_acceleration_structure_seconds": 0.003627583,
      "engine_tracing_seconds": 0.05626670829951763,
      "engine_annual_reduction_seconds": 0.0014592499937862158,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.05626670829951763
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007084124954417348,
      "weather_seconds": 0.08124662493355572,
      "metric_reduction_seconds": 0.05360912485048175,
      "write_seconds": 0.015877582831308246,
      "total_seconds": 0.1508964579552412,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1508964579552412,
      "raw_export_seconds": 0.0054349161218851805,
      "engine_upload_seconds": 5.6e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.005002791760489345,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.020297749899327755,
      "full": 0.050745584070682526
    }
  },
  "elapsed_seconds": 1.361764166969806,
  "result_class": "passed"
}
```
