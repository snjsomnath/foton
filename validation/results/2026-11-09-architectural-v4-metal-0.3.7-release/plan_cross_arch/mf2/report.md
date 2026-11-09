# Foton report

Status: **passed**

```json
{
  "scene": "plan_cross_arch",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_cross_arch",
    "category": "form",
    "question": "How does a arch opening illuminate a CROSS-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "cross",
    "window_profile": "arch"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 44,
    "floor_area": 63.0,
    "aperture_area": 1.4399999999999993
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "2fc6086b5d4c1bcea297e7e1486ae8ec6f1f0343f8a171222ed656b2ed2cc324",
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 3167779511141355274,
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 3167779511141355274,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.7)",
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/7fb068ed-087d-41c3-b9b3-215cbbd36098/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "e726265b02d6c86805289479cffc7f97bbcb22a16d44e30f04630866d50ff191",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "9a3231f9777058abb1b3cf65cd66b5db7df4d557b41586683d412e16e4487cf8",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00019649998284876347,
          "p95": 0.0,
          "p99": 5.430774763226509e-07
        },
        "bias_percent": 0.0417184612529181,
        "identifier": "plan_cross_arch_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9238426291090699,
        "worst_index": [
          21,
          517,
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
          "maximum": 0.00032570306211709976,
          "p95": 5.25880568602588e-06,
          "p99": 4.893413279205561e-05
        },
        "bias_percent": 0.17965779397580808,
        "identifier": "plan_cross_arch_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.257691868169329,
        "worst_index": [
          30,
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
          "maximum": 0.00024180114269256592,
          "p95": 4.696310497820377e-06,
          "p99": 3.8016121834516525e-05
        },
        "bias_percent": -0.019092763529240924,
        "identifier": "plan_cross_arch_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.8156048459431118,
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "plan_cross_arch_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00048524653539061546,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.7345703933387995e-05
                },
                "candidate_energy": 2.459192869708204,
                "cvrmse_percent": 48.086202993435926,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.03313580157662661,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.460008013082188,
                "relative_energy_error_percent": 0.03313580157662661,
                "rms_normalized_rmse_percent": 5.134191830275727,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0021185160148888826,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.0016332694794982672,
                  "rgb_channel": 0,
                  "sky_patch_index": 144
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006256544729694724,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.1521465189143782e-06,
                  "p99": 0.0001325449557043612
                },
                "candidate_energy": 0.5885328958053861,
                "cvrmse_percent": 353.1341099409586,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.4359849206410959,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.5859781195658229,
                "relative_energy_error_percent": 0.4359849206410959,
                "rms_normalized_rmse_percent": 6.727274144278628,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00025556248147040606,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": -0.00037009199149906635,
                  "rgb_channel": 0,
                  "sky_patch_index": 319
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.87037510052323,
            "full": 281.9438329897821
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.93179197795689,
            "full": 283.15204102545977
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.05208295118064,
            "full": 273.06066697929054
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 122.63212504331023,
            "full": 272.7084580110386
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
            "identifier": "plan_cross_arch_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000369604560546577,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.83650141581893e-05
                },
                "candidate_energy": 2.462355304722223,
                "cvrmse_percent": 44.45652943182132,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.051072709815117946,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4610983551010577,
                "relative_energy_error_percent": 0.05107270981511794,
                "rms_normalized_rmse_percent": 4.754350828287258,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0025923314969986677,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.0029619360575452447,
                  "rgb_channel": 0,
                  "sky_patch_index": 257
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005360804498195648,
                  "p50": 0.0,
                  "p90": 3.844590537482873e-06,
                  "p95": 7.674076869079727e-06,
                  "p99": 9.483772737439722e-05
                },
                "candidate_energy": 1.1192224657885355,
                "cvrmse_percent": 146.58434495487293,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.05146790366929412,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1197988027576287,
                "relative_energy_error_percent": 0.05146790366929412,
                "rms_normalized_rmse_percent": 4.395634815625471,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02110354509204626,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.020567464642226696,
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.10487496107817,
            "full": 3333.2622080342844
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.57412500493228,
            "full": 3331.7695839796215
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 166.14516696427017,
            "full": 3300.8092500967905
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.39320800174028,
            "full": 3234.0707080438733
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
            "identifier": "plan_cross_arch_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00036294187884777784,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.70774648420047e-05
                },
                "candidate_energy": 2.4618655182621296,
                "cvrmse_percent": 41.97849596347886,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.07656651676752792,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.463751927294652,
                "relative_energy_error_percent": 0.0765665167675279,
                "rms_normalized_rmse_percent": 4.4914008969867405,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0036232270067557693,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.003986168885603547,
                  "rgb_channel": 0,
                  "sky_patch_index": 314
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006184331141412258,
                  "p50": 0.0,
                  "p90": 3.938323857255455e-06,
                  "p95": 7.982258466654457e-06,
                  "p99": 9.355496149510145e-05
                },
                "candidate_energy": 1.1248180297525856,
                "cvrmse_percent": 133.04642332527942,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.007944283201946683,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1249073955818503,
                "relative_energy_error_percent": 0.007944283201946683,
                "rms_normalized_rmse_percent": 4.000893127278385,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00027189007960259914,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": -0.00034654303453862667,
                  "rgb_channel": 0,
                  "sky_patch_index": 357
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 158.35275000426918,
            "full": 3516.8260419741273
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.99870793428272,
            "full": 3512.4885420082137
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 168.1037920061499,
            "full": 3576.8092080252245
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 162.9482920980081,
            "full": 3495.994291966781
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
            "identifier": "plan_cross_arch_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00017596350517123938,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.432051744312048e-05
                },
                "candidate_energy": 2.462214378651879,
                "cvrmse_percent": 24.072535859926333,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.07740732962176101,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4641217895277805,
                "relative_energy_error_percent": 0.07740732962176101,
                "rms_normalized_rmse_percent": 2.5769039021359466,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0029782154597342014,
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "reference": 0.002802251954562962,
                  "rgb_channel": 0,
                  "sky_patch_index": 317
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003451453521847725,
                  "p50": 0.0,
                  "p90": 2.7021378627978265e-06,
                  "p95": 5.645859346259385e-06,
                  "p99": 4.7352397814393044e-05
                },
                "candidate_energy": 1.122899817051458,
                "cvrmse_percent": 77.3865043271604,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.16333445531223412,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1247368999406717,
                "relative_energy_error_percent": 0.1633344553122341,
                "rms_normalized_rmse_percent": 2.3246757279639443,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.020215215161442757,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.02056036051362753,
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 225.49187496770173,
            "full": 6227.7161669917405
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 250.98587502725422,
            "full": 6162.504083942622
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 232.25087497849017,
            "full": 6154.709374997765
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 233.59566600993276,
            "full": 6118.157375021838
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub/7fb068ed-087d-41c3-b9b3-215cbbd36098/scratchpad/suite-metal-0.3.7/plan_cross_arch/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4238.449792028405,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_arch/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 16765.7832079567,
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
      44,
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
        "identifier": "plan_cross_arch_grid",
        "full_identifier": "plan_cross_arch_grid",
        "start_sensor_index": 0,
        "sensor_count": 44,
        "stages": {
          "direct": {
            "nmbe_percent": 0.013216562780059352,
            "cvrmse_percent": 3.687777062731175,
            "rms_normalized_rmse_percent": 0.3947583360449308,
            "reference_energy": 2.462973442323573,
            "candidate_energy": 2.463298962754834,
            "relative_energy_error_percent": 0.01321656278005935,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.974128048866987e-07,
              "maximum": 5.561765283346176e-05
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 265,
              "rgb_channel": 0,
              "reference": 0.00033255162998102605,
              "candidate": 0.0003881692828144878,
              "position": [
                6.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.8354131504505207,
            "cvrmse_percent": 75.10434011255143,
            "rms_normalized_rmse_percent": 2.2579373182951628,
            "reference_energy": 1.1240130103390502,
            "candidate_energy": 1.1033827277345125,
            "relative_energy_error_percent": 1.8354131504505207,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.4255899663548917e-06,
              "p95": 6.443555292889869e-06,
              "p99": 2.4036038666963577e-05,
              "maximum": 0.0006130654364824295
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.024143055081367493,
              "candidate": 0.023529989644885063,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5660674340769971,
            "cvrmse_percent": 23.4874240553645,
            "rms_normalized_rmse_percent": 2.2534121620642122,
            "reference_energy": 3.5869864526626234,
            "candidate_energy": 3.5666816904893466,
            "relative_energy_error_percent": 0.5660674340769971,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.4363597478659358e-06,
              "p95": 6.460963049903512e-06,
              "p99": 2.4563283659517765e-05,
              "maximum": 0.0006130654364824295
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.024143055081367493,
              "candidate": 0.023529989644885063,
              "position": [
                5.5,
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
      44,
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
        "identifier": "plan_cross_arch_grid",
        "full_identifier": "plan_cross_arch_grid",
        "start_sensor_index": 0,
        "sensor_count": 44,
        "stages": {
          "direct": {
            "nmbe_percent": 0.013216562780059352,
            "cvrmse_percent": 3.687777062731175,
            "rms_normalized_rmse_percent": 0.3947583360449308,
            "reference_energy": 2.462973442323573,
            "candidate_energy": 2.463298962754834,
            "relative_energy_error_percent": 0.01321656278005935,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.974128048866987e-07,
              "maximum": 5.561765283346176e-05
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 265,
              "rgb_channel": 0,
              "reference": 0.00033255162998102605,
              "candidate": 0.0003881692828144878,
              "position": [
                6.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 88.9734223344453,
            "cvrmse_percent": 1445.2111143252262,
            "rms_normalized_rmse_percent": 27.49911879780315,
            "reference_energy": 0.5838824921007912,
            "candidate_energy": 1.1033827277345125,
            "relative_energy_error_percent": 88.97342233444532,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.1649999578366987e-05,
              "p95": 2.5499999537714757e-05,
              "p99": 7.974961772561073e-05,
              "maximum": 0.006550023332238197
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017125116661190987,
              "candidate": 0.023675139993429184,
              "position": [
                6.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 17.061054649542914,
            "cvrmse_percent": 276.94498047640565,
            "rms_normalized_rmse_percent": 27.49840153626455,
            "reference_energy": 3.0468559344243644,
            "candidate_energy": 3.5666816904893466,
            "relative_energy_error_percent": 17.06105464954291,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.1670000276353676e-05,
              "p95": 2.5390009795955848e-05,
              "p99": 7.698498666286469e-05,
              "maximum": 0.006550023332238197
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017125116661190987,
              "candidate": 0.023675139993429184,
              "position": [
                6.5,
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
      "bias_percent": -0.011593351957806084,
      "rms_normalized_error_percent": 0.10128844308854262,
      "absolute_error": {
        "p95": 0.020177822083392166,
        "p99": 0.03573368370070949,
        "maximum": 0.046059130642523094
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.825075411299672,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.10128844308854262
    },
    "overcast": {
      "bias_percent": -0.030376801210234464,
      "rms_normalized_error_percent": 0.08810394060146295,
      "absolute_error": {
        "p95": 0.015219861268997196,
        "p99": 0.026731321811676027,
        "maximum": 0.030842065811157227
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.534644603729248,
      "reference_fraction_of_uniform": 0.6626391410827637,
      "rms_normalized_to_uniform_percent": 0.06306868043214735
    },
    "horizon": {
      "bias_percent": 0.16445871855628136,
      "rms_normalized_error_percent": 1.4995240029261485,
      "absolute_error": {
        "p95": 0.01596921084522757,
        "p99": 0.02185005653106522,
        "maximum": 0.022570442308058714
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.35196121251299883,
      "reference_fraction_of_uniform": 0.0920141891773607,
      "rms_normalized_to_uniform_percent": 0.072132383243846
    },
    "north": {
      "bias_percent": -89.82993068182643,
      "rms_normalized_error_percent": 102.07534696263819,
      "absolute_error": {
        "p95": 1.2052555993591344e-05,
        "p99": 3.407080670513097e-05,
        "maximum": 4.575530329020694e-05
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.509574414943927e-06,
      "reference_fraction_of_uniform": 6.560849783454614e-07,
      "rms_normalized_to_uniform_percent": 6.973973957399734e-05
    },
    "east": {
      "bias_percent": -0.13480570160852293,
      "rms_normalized_error_percent": 0.100263022465697,
      "absolute_error": {
        "p95": 0.00432717464864254,
        "p99": 0.00591808021068573,
        "maximum": 0.006350278854370117
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5639050602912903,
      "reference_fraction_of_uniform": 0.14742325246334076,
      "rms_normalized_to_uniform_percent": 0.021464904975650508
    },
    "south": {
      "bias_percent": 0.022018162976714592,
      "rms_normalized_error_percent": 0.12187182024585227,
      "absolute_error": {
        "p95": 0.01804647445678711,
        "p99": 0.026162146031856542,
        "maximum": 0.03143596649169922
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.7602548599243164,
      "reference_fraction_of_uniform": 0.721621036529541,
      "rms_normalized_to_uniform_percent": 0.08055004835887856
    },
    "west": {
      "bias_percent": 0.02864611431683212,
      "rms_normalized_error_percent": 0.1355126791252608,
      "absolute_error": {
        "p95": 0.0065848529338836705,
        "p99": 0.012404110431671143,
        "maximum": 0.012637138366699219
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.572899341583252,
      "reference_fraction_of_uniform": 0.14977465569972992,
      "rms_normalized_to_uniform_percent": 0.029314751550957086
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
        "identifier": "plan_cross_arch_grid",
        "sensor_count": 44,
        "illuminance": {
          "nmbe_percent": -0.04902706995070425,
          "cvrmse_percent": 2.8273869794129456,
          "absolute_error_percentiles_lux": {
            "p50": 0.5681991577148438,
            "p90": 7.839753723144536,
            "p95": 14.041660308837887,
            "p99": 38.58696197509763
          },
          "maximum_absolute_error_lux": 321.8359375,
          "worst": {
            "sensor_index": 21,
            "position": [
              5.5,
              0.5,
              0.75
            ],
            "hour_of_year": 2722.5,
            "foton_lux": 36617.0078125,
            "radiance_lux": 36295.171875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.07699564134495684,
            "maximum_error_percentage_points": 1.0995890410958893,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.15763828323289591,
            "maximum_error_percentage_points": 0.7447971321295981,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.24324719800747163,
            "maximum_error_percentage_points": 1.4761643835616525,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.2489476961394776,
            "maximum_error_percentage_points": 1.4761643835616436,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.006849315068493148,
            "maximum_error_percentage_points": 0.05534246575342472,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 13.636363636363637,
          "radiance_percent": 13.636363636363637,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.272727272727273,
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
      "maximum_error_percentage_points": 0.004931506849310097,
      "metrics": {
        "da": [
          {
            "identifier": "plan_cross_arch_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_cross_arch_grid",
            "maximum_error_percentage_points": 0.00463880565068564,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_cross_arch_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_cross_arch_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_cross_arch_grid",
            "maximum_error_percentage_points": 0.00438356164384146,
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
      "study_preparation_seconds": 0.007707667071372271,
      "weather_seconds": 0.08201108314096928,
      "metric_reduction_seconds": 0.11849083402194083,
      "write_seconds": 0.024831291055306792,
      "total_seconds": 0.225476416060701,
      "cold_end_to_end_seconds": 0.23318408313207328,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0035115829668939114,
      "engine_upload_seconds": 0.000732125,
      "engine_acceleration_structure_seconds": 0.003555375,
      "engine_tracing_seconds": 0.05220604152418673,
      "engine_annual_reduction_seconds": 0.0019648747984319925,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.05220604152418673
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007707667071372271,
      "weather_seconds": 0.07791958283632994,
      "metric_reduction_seconds": 0.04667212488129735,
      "write_seconds": 0.020200375001877546,
      "total_seconds": 0.14488870790228248,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14488870790228248,
      "raw_export_seconds": 0.002899582963436842,
      "engine_upload_seconds": 5.2875e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.001962249865755439,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01948462496511638,
      "full": 0.059899582993239164
    }
  },
  "elapsed_seconds": 1.3866912920493633,
  "result_class": "passed"
}
```
