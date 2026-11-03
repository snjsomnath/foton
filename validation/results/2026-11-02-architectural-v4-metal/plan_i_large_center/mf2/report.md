# Foton report

Status: **passed**

```json
{
  "scene": "plan_i_large_center",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_i_large_center",
    "category": "form",
    "question": "How does a large center opening illuminate a I-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "i",
    "window_profile": "large_center"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 74,
    "floor_area": 90.0,
    "aperture_area": 4.800000000000001
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "77f363e8cbcdf29db63e5d131ac6f18fe5dda22287890c75dc98898c0abaaab5",
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 5535031717744390830,
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 5535031717744390830,
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
    "maximum_samples": 16384,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "plan_i_large_center_grid",
        "bias_percent": 0.018816839041654314,
        "rms_normalized_error_percent": 0.7067205402871549,
        "absolute_error": {
          "p95": 0.0,
          "p99": 2.1905085304752904e-06,
          "maximum": 0.00013817357830703259
        },
        "worst_index": [
          23,
          356,
          0
        ],
        "passed": true
      }
    ],
    "samples_per_patch": [
      256,
      1024
    ]
  },
  "depth_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "plan_i_large_center_grid",
        "bias_percent": 0.0915023564418354,
        "rms_normalized_error_percent": 1.5895281139970123,
        "absolute_error": {
          "p95": 9.749190212460235e-06,
          "p99": 7.455108570866298e-05,
          "maximum": 0.0008640289306640625
        },
        "worst_index": [
          33,
          0,
          0
        ],
        "passed": true
      }
    ]
  },
  "sample_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "plan_i_large_center_grid",
        "bias_percent": -0.008694490023878287,
        "rms_normalized_error_percent": 1.2785547452540107,
        "absolute_error": {
          "p95": 8.340248314198107e-06,
          "p99": 5.7121616555378405e-05,
          "maximum": 0.0004452243447303772
        },
        "worst_index": [
          57,
          0,
          0
        ],
        "passed": true
      }
    ]
  },
  "oracle_levels": [
    {
      "samples": 20000,
      "material_bounces": 1,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_i_large_center_grid",
            "start_sensor_index": 0,
            "sensor_count": 74,
            "stages": {
              "direct": {
                "nmbe_percent": 0.06082823327288879,
                "cvrmse_percent": 41.950501613311964,
                "rms_normalized_rmse_percent": 5.998214032606593,
                "reference_energy": 7.066336938477889,
                "candidate_energy": 7.0706352663946745,
                "relative_energy_error_percent": 0.06082823327288879,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00012332947226241465,
                  "maximum": 0.000568011193536222
                },
                "worst": {
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "sky_patch_index": 364,
                  "rgb_channel": 0,
                  "reference": 0.00443684053607285,
                  "candidate": 0.0038688293425366282
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.7919256678559339,
                "cvrmse_percent": 214.4668311187887,
                "rms_normalized_rmse_percent": 5.241208605246963,
                "reference_energy": 2.3982847239299154,
                "candidate_energy": 2.3792920916128466,
                "relative_energy_error_percent": 0.791925667855934,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 5.845120085723465e-06,
                  "p99": 0.00020513393683359237,
                  "maximum": 0.0020892247557640076
                },
                "worst": {
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.043101999908685684,
                  "candidate": 0.04101277515292168
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 177.34508297871798,
            "full": 407.91116596665233
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 168.36591600440443,
            "full": 414.9908749386668
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 158.9752919971943,
            "full": 412.68366703297943
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 162.77337505016476,
            "full": 423.674458055757
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 8,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_i_large_center_grid",
            "start_sensor_index": 0,
            "sensor_count": 74,
            "stages": {
              "direct": {
                "nmbe_percent": -0.04514522809730594,
                "cvrmse_percent": 31.61335958669406,
                "rms_normalized_rmse_percent": 4.52622506141201,
                "reference_energy": 7.069116574811687,
                "candidate_energy": 7.065925206009524,
                "relative_energy_error_percent": 0.04514522809730594,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.188145049847682e-05,
                  "maximum": 0.0003557190066203475
                },
                "worst": {
                  "global_sensor_index": 48,
                  "local_sensor_index": 48,
                  "sky_patch_index": 362,
                  "rgb_channel": 0,
                  "reference": 0.003779050544835627,
                  "candidate": 0.004134769551455975
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.0020703821073563395,
                "cvrmse_percent": 78.28533890562652,
                "rms_normalized_rmse_percent": 2.8343940686895657,
                "reference_energy": 4.363044955104069,
                "candidate_energy": 4.3631352868061555,
                "relative_energy_error_percent": 0.0020703821073563395,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.0252145885897335e-06,
                  "p95": 1.4651612218585797e-05,
                  "p99": 0.00013481971691362945,
                  "maximum": 0.0008289702236652374
                },
                "worst": {
                  "global_sensor_index": 48,
                  "local_sensor_index": 48,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.042806150391697884,
                  "candidate": 0.04363512061536312
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 216.13212500233203,
            "full": 5425.178750068881
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 236.02149996440858,
            "full": 5388.318291050382
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 246.56841601245105,
            "full": 5882.065000012517
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 221.9006670638919,
            "full": 5481.610915972851
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 12,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_i_large_center_grid",
            "start_sensor_index": 0,
            "sensor_count": 74,
            "stages": {
              "direct": {
                "nmbe_percent": 0.04822097768143867,
                "cvrmse_percent": 31.437262477440658,
                "rms_normalized_rmse_percent": 4.500401166644781,
                "reference_energy": 7.067337947879423,
                "candidate_energy": 7.070745887333942,
                "relative_energy_error_percent": 0.048220977681438675,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.250549483113045e-05,
                  "maximum": 0.00034994748421013355
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 35,
                  "sky_patch_index": 358,
                  "rgb_channel": 0,
                  "reference": 0.0037128550466150045,
                  "candidate": 0.004062802530825138
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.03308599978955558,
                "cvrmse_percent": 80.30665471778426,
                "rms_normalized_rmse_percent": 2.9070907743378718,
                "reference_energy": 4.372751742689456,
                "candidate_energy": 4.371304974057072,
                "relative_energy_error_percent": 0.03308599978955558,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.108594106990495e-06,
                  "p95": 1.4583781535293383e-05,
                  "p99": 0.0001396145642502274,
                  "maximum": 0.0006473325192928314
                },
                "worst": {
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.043581148609519005,
                  "candidate": 0.04293381609022617
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 221.98658296838403,
            "full": 5892.956333002076
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 220.35499999765307,
            "full": 5864.246750017628
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 231.7873330321163,
            "full": 5897.385166957974
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 242.33641603495926,
            "full": 6067.370333941653
          }
        }
      ]
    },
    {
      "samples": 80000,
      "material_bounces": 12,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_i_large_center_grid",
            "start_sensor_index": 0,
            "sensor_count": 74,
            "stages": {
              "direct": {
                "nmbe_percent": -0.04920474098228758,
                "cvrmse_percent": 18.489725568799788,
                "rms_normalized_rmse_percent": 2.648456904334707,
                "reference_energy": 7.071336015069846,
                "candidate_energy": 7.067856582499644,
                "relative_energy_error_percent": 0.04920474098228758,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.316017777659035e-05,
                  "maximum": 0.00020511809270828962
                },
                "worst": {
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "sky_patch_index": 96,
                  "rgb_channel": 0,
                  "reference": 0.001163610490038991,
                  "candidate": 0.0009584923973307014
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.11966096324351892,
                "cvrmse_percent": 47.43336277300427,
                "rms_normalized_rmse_percent": 1.7143063683953739,
                "reference_energy": 4.367865905048099,
                "candidate_energy": 4.373092535463265,
                "relative_energy_error_percent": 0.11966096324351892,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.367266228655353e-06,
                  "p95": 1.0213800123892725e-05,
                  "p99": 7.510991417803109e-05,
                  "maximum": 0.0006467252969741821
                },
                "worst": {
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04347125068306923,
                  "candidate": 0.04282452538609505
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 329.21558304224163,
            "full": 10811.930291936733
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 356.23179201502353,
            "full": 10657.045083935373
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 332.538083079271,
            "full": 10587.114583933726
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 316.7038339888677,
            "full": 10278.337207972072
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 12591.315499972552,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_i_large_center/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 49143.54337495752,
      "worker_pool_size": 12,
      "invocation_count": 5
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      74,
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
        "identifier": "plan_i_large_center_grid",
        "full_identifier": "plan_i_large_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": 0.012198811956043278,
            "cvrmse_percent": 2.7677584901643457,
            "rms_normalized_rmse_percent": 0.39651594519761857,
            "reference_energy": 7.067806016531165,
            "candidate_energy": 7.0686682048965395,
            "relative_energy_error_percent": 0.012198811956043278,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.8322258256376278e-06,
              "maximum": 6.050811498425901e-05
            },
            "worst": {
              "global_sensor_index": 24,
              "local_sensor_index": 24,
              "sky_patch_index": 513,
              "rgb_channel": 0,
              "reference": 0.0003328037273604423,
              "candidate": 0.00027229561237618327,
              "position": [
                4.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.5526120136171042,
            "cvrmse_percent": 108.02576566737538,
            "rms_normalized_rmse_percent": 3.9091861051534194,
            "reference_energy": 4.372269527562411,
            "candidate_energy": 4.304385145609757,
            "relative_energy_error_percent": 1.552612013617104,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.9101426005363464e-05,
              "p95": 3.4736149245873094e-05,
              "p99": 7.984480471350371e-05,
              "maximum": 0.0024909041821956635
            },
            "worst": {
              "global_sensor_index": 47,
              "local_sensor_index": 47,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.049999453127384186,
              "candidate": 0.04750854894518852,
              "position": [
                6.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5858544668604245,
            "cvrmse_percent": 41.26424410442992,
            "rms_normalized_rmse_percent": 3.907102937467488,
            "reference_energy": 11.440075544093576,
            "candidate_energy": 11.373053350506297,
            "relative_energy_error_percent": 0.5858544668604245,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.903302108985372e-05,
              "p95": 3.445866605034098e-05,
              "p99": 7.977608183864575e-05,
              "maximum": 0.0024909041821956635
            },
            "worst": {
              "global_sensor_index": 47,
              "local_sensor_index": 47,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.049999453127384186,
              "candidate": 0.04750854894518852,
              "position": [
                6.5,
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
      74,
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
        "identifier": "plan_i_large_center_grid",
        "full_identifier": "plan_i_large_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": 0.012198811956043278,
            "cvrmse_percent": 2.7677584901643457,
            "rms_normalized_rmse_percent": 0.39651594519761857,
            "reference_energy": 7.067806016531165,
            "candidate_energy": 7.0686682048965395,
            "relative_energy_error_percent": 0.012198811956043278,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.8322258256376278e-06,
              "maximum": 6.050811498425901e-05
            },
            "worst": {
              "global_sensor_index": 24,
              "local_sensor_index": 24,
              "sky_patch_index": 513,
              "rgb_channel": 0,
              "reference": 0.0003328037273604423,
              "candidate": 0.00027229561237618327,
              "position": [
                4.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 80.13985562914674,
            "cvrmse_percent": 1031.9316729698423,
            "rms_normalized_rmse_percent": 25.190287710446746,
            "reference_energy": 2.3894685218751253,
            "candidate_energy": 4.304385145609757,
            "relative_energy_error_percent": 80.13985562914674,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.238999852328561e-05,
              "p95": 6.744797792634927e-05,
              "p99": 0.00016509345732629337,
              "maximum": 0.00987238809466362
            },
            "worst": {
              "global_sensor_index": 24,
              "local_sensor_index": 24,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.028362292796373367,
              "candidate": 0.03823468089103699,
              "position": [
                4.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.25719782501785,
            "cvrmse_percent": 260.7259614898975,
            "rms_normalized_rmse_percent": 25.190172758102886,
            "reference_energy": 9.45727453840629,
            "candidate_energy": 11.373053350506297,
            "relative_energy_error_percent": 20.257197825017855,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.237000055378303e-05,
              "p95": 6.730000313837081e-05,
              "p99": 0.00016503108199685858,
              "maximum": 0.00987238809466362
            },
            "worst": {
              "global_sensor_index": 24,
              "local_sensor_index": 24,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.028362292796373367,
              "candidate": 0.03823468089103699,
              "position": [
                4.5,
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
      "bias_percent": 0.2397144087553504,
      "rms_normalized_error_percent": 0.378724158065495,
      "absolute_error": {
        "p95": 0.13162875581578992,
        "p99": 0.15002779870441058,
        "maximum": 0.1667211548776244
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 6.74716097778374,
      "rms_normalized_to_uniform_percent": 0.378724158065495
    },
    "overcast": {
      "bias_percent": 0.194876238103593,
      "rms_normalized_error_percent": 0.33049513967238453,
      "absolute_error": {
        "p95": 0.09197430610656737,
        "p99": 0.11314049720764147,
        "maximum": 0.1371469497680664
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 4.436232089996338,
      "rms_normalized_to_uniform_percent": 0.23539353616518002
    },
    "horizon": {
      "bias_percent": 1.0433863916637176,
      "rms_normalized_error_percent": 3.726433880851845,
      "absolute_error": {
        "p95": 0.0763086059223056,
        "p99": 0.09680708358525424,
        "maximum": 0.10979349933574156
      },
      "worst_index": [
        58
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.6847504392679286,
      "rms_normalized_to_uniform_percent": 0.2181271278929658
    },
    "north": {
      "bias_percent": -97.54466050292383,
      "rms_normalized_error_percent": 99.9765111831943,
      "absolute_error": {
        "p95": 4.146620613028058e-05,
        "p99": 9.438164699531593e-05,
        "maximum": 0.00015467496996279806
      },
      "worst_index": [
        59
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 8.386129593418445e-06,
      "rms_normalized_to_uniform_percent": 0.00013117873054931177
    },
    "east": {
      "bias_percent": 0.015387460361919594,
      "rms_normalized_error_percent": 0.5186455351593388,
      "absolute_error": {
        "p95": 0.04417866766452788,
        "p99": 0.05688630819320675,
        "maximum": 0.06375432014465332
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.2707278728485107,
      "rms_normalized_to_uniform_percent": 0.10857147578521871
    },
    "south": {
      "bias_percent": 0.26597757926470733,
      "rms_normalized_error_percent": 0.43545337843871296,
      "absolute_error": {
        "p95": 0.09788868725299835,
        "p99": 0.11704648971557613,
        "maximum": 0.12357807159423828
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 4.543532371520996,
      "rms_normalized_to_uniform_percent": 0.2785670605802054
    },
    "west": {
      "bias_percent": 0.39941960386882924,
      "rms_normalized_error_percent": 0.5875048879643188,
      "absolute_error": {
        "p95": 0.04776374101638793,
        "p99": 0.07423568487167355,
        "maximum": 0.08158719539642334
      },
      "worst_index": [
        73
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.2870603799819946,
      "rms_normalized_to_uniform_percent": 0.12410926087278426
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
        "identifier": "plan_i_large_center_grid",
        "sensor_count": 74,
        "illuminance": {
          "nmbe_percent": 0.022262792951126646,
          "cvrmse_percent": 6.180672511260183,
          "absolute_error_percentiles_lux": {
            "p50": 1.6729693412780762,
            "p90": 42.491618347168,
            "p95": 74.42777862548827,
            "p99": 169.26217651367185
          },
          "maximum_absolute_error_lux": 882.616943359375,
          "worst": {
            "sensor_index": 33,
            "position": [
              5.5,
              3.5,
              0.75
            ],
            "hour_of_year": 6252.5,
            "foton_lux": 3473.279296875,
            "radiance_lux": 2590.662353515625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.5871084783413552,
            "maximum_error_percentage_points": 5.701369863013696,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.5535712058134589,
            "maximum_error_percentage_points": 2.558316616750723,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.9371566086634583,
            "maximum_error_percentage_points": 6.82671232876713,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.9501499444650129,
            "maximum_error_percentage_points": 6.8267123287671225,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.018154387263976272,
            "maximum_error_percentage_points": 0.1920547945205513,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 22.972972972972972,
          "radiance_percent": 21.62162162162162,
          "difference_percentage_points": 1.3513513513513509,
          "tolerance_percentage_points": 2.0,
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
      "maximum_error_percentage_points": 0.004962810359586456,
      "metrics": {
        "da": [
          {
            "identifier": "plan_i_large_center_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_i_large_center_grid",
            "maximum_error_percentage_points": 0.004962810359586456,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_i_large_center_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_i_large_center_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_i_large_center_grid",
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
      "study_preparation_seconds": 0.013636125018820167,
      "weather_seconds": 0.13462404208257794,
      "metric_reduction_seconds": 0.13050337496679276,
      "write_seconds": 0.03253458300605416,
      "total_seconds": 0.2978855000110343,
      "cold_end_to_end_seconds": 0.3115216250298545,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.013310707989148796,
      "engine_upload_seconds": 0.00090725,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.025643249973654747,
      "engine_annual_reduction_seconds": 0.0033203333150595427,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.025643249973654747
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.013636125018820167,
      "weather_seconds": 0.10566383297555149,
      "metric_reduction_seconds": 0.056155625032261014,
      "write_seconds": 0.031867583049461246,
      "total_seconds": 0.19387258391361684,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.19387258391361684,
      "raw_export_seconds": 0.012694958015345037,
      "engine_upload_seconds": 9.0792e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0032615000382065773,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.017836457933299243,
      "full": 0.0269032089272514
    }
  },
  "elapsed_seconds": 158.53560754202772,
  "result_class": "passed"
}
```
