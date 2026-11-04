# Foton report

Status: **passed**

```json
{
  "scene": "plan_j_arch",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_j_arch",
    "category": "form",
    "question": "How does a arch opening illuminate a J-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "j",
    "window_profile": "arch"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 47,
    "floor_area": 63.0,
    "aperture_area": 1.4399999999999993
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "2bb0188a6ec6b8449a6b81198334a2c8c00cb3629cd36aa30598c17924e6ec8f",
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 7022943515965175511,
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 7022943515965175511,
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
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "8f67e2fba4dc52ea33fa016c8090a16426051ba296d29b703aca8b7c617de0fd",
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
          "maximum": 0.0001537444768473506,
          "p95": 0.0,
          "p99": 3.0859519029036164e-06
        },
        "bias_percent": -0.059277503336345516,
        "identifier": "plan_j_arch_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9828131727044833,
        "worst_index": [
          13,
          259,
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
          "maximum": 0.000319894403219223,
          "p95": 6.3123079598881304e-06,
          "p99": 4.775350680574775e-05
        },
        "bias_percent": 0.005429919493964415,
        "identifier": "plan_j_arch_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.354921386227561,
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
          "maximum": 0.00021893717348575592,
          "p95": 5.428808435681276e-06,
          "p99": 3.9135804399847984e-05
        },
        "bias_percent": 0.0363026440609212,
        "identifier": "plan_j_arch_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.9502689236175363,
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
            "identifier": "plan_j_arch_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00036004194043925963,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.819125312380493e-05
                },
                "candidate_energy": 2.64203203579018,
                "cvrmse_percent": 48.204798371817,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.018292865425740438,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.642515427581202,
                "relative_energy_error_percent": 0.018292865425740438,
                "rms_normalized_rmse_percent": 5.357626596239264,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 4.5056618546368554e-05,
                  "global_sensor_index": 42,
                  "local_sensor_index": 42,
                  "reference": 0.0004050985589856282,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007596143987029791,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.683499016915448e-08,
                  "p99": 0.00012783694546669722
                },
                "candidate_energy": 0.6481062796506194,
                "cvrmse_percent": 322.73912003723063,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.11002067987917705,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6473940123567274,
                "relative_energy_error_percent": 0.11002067987917705,
                "rms_normalized_rmse_percent": 6.8482334800534055,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0005357414484024048,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.0002238729503005743,
                  "rgb_channel": 0,
                  "sky_patch_index": 360
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.63133301958442,
            "full": 271.0724580101669
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.98879204131663,
            "full": 271.9592920038849
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.63462495524436,
            "full": 275.41354205459356
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.03770903497934,
            "full": 281.93404199555516
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
            "identifier": "plan_j_arch_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00031886587385088205,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.837838736828417e-05
                },
                "candidate_energy": 2.642640212159222,
                "cvrmse_percent": 43.501428066821575,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.029338597178840294,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.641865125991899,
                "relative_energy_error_percent": 0.02933859717884029,
                "rms_normalized_rmse_percent": 4.83264712327737,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0039290073327720165,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.0036101414589211345,
                  "rgb_channel": 0,
                  "sky_patch_index": 406
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004123940598219633,
                  "p50": 0.0,
                  "p90": 4.669296458814642e-06,
                  "p95": 9.075521575141465e-06,
                  "p99": 9.554240386933088e-05
                },
                "candidate_energy": 1.3073473748975601,
                "cvrmse_percent": 127.78085531591623,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.017951935423754065,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3075821111937742,
                "relative_energy_error_percent": 0.017951935423754065,
                "rms_normalized_rmse_percent": 4.592402937475945,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00016957102343440056,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": -0.00024282303638756275,
                  "rgb_channel": 0,
                  "sky_patch_index": 212
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 167.99362492747605,
            "full": 3115.514958044514
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.1454580835998,
            "full": 3139.975666999817
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.2152920048684,
            "full": 3161.6949170129374
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.2154999440536,
            "full": 3152.346624992788
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
            "identifier": "plan_j_arch_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00032059510704129934,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.329347161226906e-05
                },
                "candidate_energy": 2.6382717574165326,
                "cvrmse_percent": 41.68537293529424,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.037192049015697067,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.6392533498160446,
                "relative_energy_error_percent": 0.037192049015697067,
                "rms_normalized_rmse_percent": 4.6288519410598346,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0037153029115870595,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.004035898018628359,
                  "rgb_channel": 0,
                  "sky_patch_index": 357
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00042749522253870964,
                  "p50": 0.0,
                  "p90": 4.605051231010293e-06,
                  "p95": 9.01828934729565e-06,
                  "p99": 8.820428047329187e-05
                },
                "candidate_energy": 1.3110716844050607,
                "cvrmse_percent": 119.56245690000426,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.01489212058307279,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3112669598618893,
                "relative_energy_error_percent": 0.01489212058307279,
                "rms_normalized_rmse_percent": 4.294725939637107,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.013924019876867533,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.014351515099406242,
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
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.15904100518674,
            "full": 3460.148875019513
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.9759579570964,
            "full": 3386.0833330545574
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.5640419246629,
            "full": 3383.1942909164354
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.932666009292,
            "full": 3425.3980830544606
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
            "identifier": "plan_j_arch_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001685109455138445,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.402956645004451e-05
                },
                "candidate_energy": 2.641150035916553,
                "cvrmse_percent": 23.85334334968362,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.046458447106569434,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.639923568421864,
                "relative_energy_error_percent": 0.046458447106569434,
                "rms_normalized_rmse_percent": 2.6490941626490647,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004473546985536814,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.004305036040022969,
                  "rgb_channel": 0,
                  "sky_patch_index": 455
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003196652978658676,
                  "p50": 0.0,
                  "p90": 3.376659606146859e-06,
                  "p95": 6.094351419960731e-06,
                  "p99": 5.121808499097824e-05
                },
                "candidate_energy": 1.3095999191522338,
                "cvrmse_percent": 74.87975405946545,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.1873517362941066,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3120580827514559,
                "relative_energy_error_percent": 0.1873517362941066,
                "rms_normalized_rmse_percent": 2.693782019737891,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.01948222517967224,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.01980189047753811,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 224.85054098069668,
            "full": 5964.617665973492
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 227.6804590364918,
            "full": 5990.158958011307
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 223.59208308625966,
            "full": 5965.131875011139
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 229.7887080349028,
            "full": 6255.63566701021
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
    "/content/suite-vulkan-0.3.3/plan_j_arch/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4674.697124981321,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_arch/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 19082.010292098857,
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
        "identifier": "plan_j_arch_grid",
        "full_identifier": "plan_j_arch_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": 0.016171834130001683,
            "cvrmse_percent": 4.920795508718875,
            "rms_normalized_rmse_percent": 0.546965648047772,
            "reference_energy": 2.640393018370048,
            "candidate_energy": 2.640820018349359,
            "relative_energy_error_percent": 0.016171834130001686,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.984823029488325e-06,
              "maximum": 8.414627518504858e-05
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 456,
              "rgb_channel": 0,
              "reference": 0.0014747396344318986,
              "candidate": 0.0015588859096169472,
              "position": [
                4.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.8431617781694825,
            "cvrmse_percent": 47.992720457582124,
            "rms_normalized_rmse_percent": 1.7268721341117892,
            "reference_energy": 1.3109727902819195,
            "candidate_energy": 1.2999191687920604,
            "relative_energy_error_percent": 0.8431617781694823,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.122317477595061e-06,
              "p95": 7.273440587596269e-06,
              "p99": 2.3605447495356202e-05,
              "maximum": 0.00029001152142882347
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.007878361269831657,
              "candidate": 0.007588349748402834,
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
            "nmbe_percent": -0.2689354017104657,
            "cvrmse_percent": 15.870531248142841,
            "rms_normalized_rmse_percent": 1.7211940544452626,
            "reference_energy": 3.9513658086519676,
            "candidate_energy": 3.9407391871414195,
            "relative_energy_error_percent": 0.26893540171046576,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.1216226236429065e-06,
              "p95": 7.331780579988845e-06,
              "p99": 2.415041672065854e-05,
              "maximum": 0.00029001152142882347
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.007878361269831657,
              "candidate": 0.007588349748402834,
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
      47,
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
        "identifier": "plan_j_arch_grid",
        "full_identifier": "plan_j_arch_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": 0.016171834130001683,
            "cvrmse_percent": 4.920795508718875,
            "rms_normalized_rmse_percent": 0.546965648047772,
            "reference_energy": 2.640393018370048,
            "candidate_energy": 2.640820018349359,
            "relative_energy_error_percent": 0.016171834130001686,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.984823029488325e-06,
              "maximum": 8.414627518504858e-05
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 456,
              "rgb_channel": 0,
              "reference": 0.0014747396344318986,
              "candidate": 0.0015588859096169472,
              "position": [
                4.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 100.10120318087715,
            "cvrmse_percent": 1298.0471508770995,
            "rms_normalized_rmse_percent": 27.657567915663694,
            "reference_energy": 0.6496308608484611,
            "candidate_energy": 1.2999191687920604,
            "relative_energy_error_percent": 100.10120318087712,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.6980000509647653e-05,
              "p95": 2.8479998945840634e-05,
              "p99": 7.488403934985399e-05,
              "maximum": 0.004463815130293369
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01275226566940546,
              "candidate": 0.01721608079969883,
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
            "nmbe_percent": 19.77843723363725,
            "cvrmse_percent": 256.26532169106605,
            "rms_normalized_rmse_percent": 27.65322338869687,
            "reference_energy": 3.2900238792185093,
            "candidate_energy": 3.9407391871414195,
            "relative_energy_error_percent": 19.778437233637245,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.7020000086631626e-05,
              "p95": 2.843999936885666e-05,
              "p99": 7.227555033750832e-05,
              "maximum": 0.004463815130293369
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01275226566940546,
              "candidate": 0.01721608079969883,
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
      "bias_percent": 0.11834777086922423,
      "rms_normalized_error_percent": 0.1412401135591952,
      "absolute_error": {
        "p95": 0.027901125230661673,
        "p99": 0.051132911518881684,
        "maximum": 0.052817113023607476
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.878554086564787,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.1412401135591952
    },
    "overcast": {
      "bias_percent": 0.09288092211535369,
      "rms_normalized_error_percent": 0.10339796618549353,
      "absolute_error": {
        "p95": 0.020069557428359953,
        "p99": 0.024935717582702632,
        "maximum": 0.026387453079223633
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.5412914752960205,
      "reference_fraction_of_uniform": 0.6552162170410156,
      "rms_normalized_to_uniform_percent": 0.0745940379060855
    },
    "horizon": {
      "bias_percent": 0.13088631299445203,
      "rms_normalized_error_percent": 1.7899701867050837,
      "absolute_error": {
        "p95": 0.01792664464273899,
        "p99": 0.021214636619942735,
        "maximum": 0.02262415764262332
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3640879982806721,
      "reference_fraction_of_uniform": 0.09387209515573437,
      "rms_normalized_to_uniform_percent": 0.07730666015510974
    },
    "north": {
      "bias_percent": -93.88236791237301,
      "rms_normalized_error_percent": 100.10645080821467,
      "absolute_error": {
        "p95": 1.3903105627832682e-05,
        "p99": 7.308063202799523e-05,
        "maximum": 0.0001155732388724573
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 4.898541646980448e-06,
      "reference_fraction_of_uniform": 1.2629814136744244e-06,
      "rms_normalized_to_uniform_percent": 0.00015743739630214094
    },
    "east": {
      "bias_percent": 0.13668214148786229,
      "rms_normalized_error_percent": 0.2547695733052197,
      "absolute_error": {
        "p95": 0.01279138326644897,
        "p99": 0.018666146397590632,
        "maximum": 0.021828293800354004
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.842197835445404,
      "reference_fraction_of_uniform": 0.21714220941066742,
      "rms_normalized_to_uniform_percent": 0.05232730160235049
    },
    "south": {
      "bias_percent": 0.14870656689171186,
      "rms_normalized_error_percent": 0.17077737465410806,
      "absolute_error": {
        "p95": 0.024494254589080795,
        "p99": 0.04426108360290527,
        "maximum": 0.04905223846435547
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.5358030796051025,
      "reference_fraction_of_uniform": 0.6538011431694031,
      "rms_normalized_to_uniform_percent": 0.11296356457575031
    },
    "west": {
      "bias_percent": 0.056245730302763294,
      "rms_normalized_error_percent": 0.2255780847292133,
      "absolute_error": {
        "p95": 0.012011174857616415,
        "p99": 0.0150101763010025,
        "maximum": 0.015574455261230469
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.8256312608718872,
      "reference_fraction_of_uniform": 0.21287089586257935,
      "rms_normalized_to_uniform_percent": 0.04637908118243931
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
        "identifier": "plan_j_arch_grid",
        "sensor_count": 47,
        "illuminance": {
          "nmbe_percent": 0.11041253663032816,
          "cvrmse_percent": 2.810247989898766,
          "absolute_error_percentiles_lux": {
            "p50": 0.6298351287841797,
            "p90": 10.390597534179689,
            "p95": 17.132995605468743,
            "p99": 40.5167626953125
          },
          "maximum_absolute_error_lux": 239.234375,
          "worst": {
            "sensor_index": 16,
            "position": [
              3.5,
              0.5,
              0.75
            ],
            "hour_of_year": 2961.5,
            "foton_lux": 29130.9140625,
            "radiance_lux": 28891.6796875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.10913436315942912,
            "maximum_error_percentage_points": 0.6027397260273979,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1718624409257362,
            "maximum_error_percentage_points": 0.6020283958057533,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.46322063538326996,
            "maximum_error_percentage_points": 2.1669863013698603,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.4572835907898563,
            "maximum_error_percentage_points": 2.166986301369862,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.007653745263771518,
            "maximum_error_percentage_points": 0.08369863013698642,
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
      "maximum_error_percentage_points": 0.004985819777395761,
      "metrics": {
        "da": [
          {
            "identifier": "plan_j_arch_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_j_arch_grid",
            "maximum_error_percentage_points": 0.004985819777395761,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_j_arch_grid",
            "maximum_error_percentage_points": 0.004794520547953596,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_j_arch_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_j_arch_grid",
            "maximum_error_percentage_points": 0.00479452054794538,
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
      "study_preparation_seconds": 0.3560407079999095,
      "weather_seconds": 0.2542179900001429,
      "metric_reduction_seconds": 1.2498655670001426,
      "write_seconds": 0.011467436999964775,
      "total_seconds": 1.5158923649998997,
      "cold_end_to_end_seconds": 1.8719330729998092,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.001697271000011824,
      "engine_upload_seconds": 0.044289164,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.040479083,
      "engine_annual_reduction_seconds": 0.053263301,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.040479083
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3560407079999095,
      "weather_seconds": 0.22676527100020394,
      "metric_reduction_seconds": 1.160480661000065,
      "write_seconds": 0.012351987999863923,
      "total_seconds": 1.3998650129999533,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 1.3998650129999533,
      "raw_export_seconds": 0.0017020949999277946,
      "engine_upload_seconds": 0.044147161,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 1.32e-07,
      "engine_annual_reduction_seconds": 0.051726338,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01909586099986882,
      "full": 0.06061708000015642
    }
  },
  "elapsed_seconds": 6.294998079999914,
  "result_class": "passed"
}
```
