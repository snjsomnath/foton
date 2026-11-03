# Foton report

Status: **passed**

```json
{
  "scene": "plan_i_distributed",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_i_distributed",
    "category": "form",
    "question": "How does a distributed opening illuminate a I-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "i",
    "window_profile": "distributed"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 12,
    "shades": 0,
    "sensors": 74,
    "floor_area": 90.0,
    "aperture_area": 14.399999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "866ca4a3ef8dd207bb87e8300e19721a4e5021db43a21942b4162f00265ee545",
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
      "scene_fingerprint": 16343183456666100934,
      "basis": "Tregenza",
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
      "scene_fingerprint": 16343183456666100934,
      "basis": "Tregenza",
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
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "plan_i_distributed_grid",
        "bias_percent": 0.09946762968961857,
        "rms_normalized_error_percent": 1.592207671185183,
        "absolute_error": {
          "p95": 5.021854303777218e-05,
          "p99": 0.00017416622722521424,
          "maximum": 0.0006667673587799072
        },
        "worst_index": [
          70,
          129,
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
        "identifier": "plan_i_distributed_grid",
        "bias_percent": 0.013576275130760929,
        "rms_normalized_error_percent": 1.0693101680118828,
        "absolute_error": {
          "p95": 8.018918742891401e-05,
          "p99": 0.00017492007464170456,
          "maximum": 0.0008347779512405396
        },
        "worst_index": [
          58,
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
        "identifier": "plan_i_distributed_grid",
        "bias_percent": 0.02922593892597605,
        "rms_normalized_error_percent": 0.8437425630563632,
        "absolute_error": {
          "p95": 6.439327262341976e-05,
          "p99": 0.00013884156942367554,
          "maximum": 0.0004875548183917999
        },
        "worst_index": [
          13,
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_i_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 74,
            "stages": {
              "direct": {
                "nmbe_percent": -0.06065941676949259,
                "cvrmse_percent": 12.792894874179431,
                "rms_normalized_rmse_percent": 3.4525077926843255,
                "reference_energy": 20.503696606543137,
                "candidate_energy": 20.491259183765422,
                "relative_energy_error_percent": 0.060659416769492595,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.886249270290136e-05,
                  "p95": 0.00018473598174750805,
                  "p99": 0.0003990876430179924,
                  "maximum": 0.0008851776365190744
                },
                "worst": {
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "sky_patch_index": 45,
                  "rgb_channel": 0,
                  "reference": 0.006111323134973645,
                  "candidate": 0.00699650077149272
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.02066272099335294,
                "cvrmse_percent": 60.61749923327831,
                "rms_normalized_rmse_percent": 3.90632778483319,
                "reference_energy": 6.5928078682637725,
                "candidate_energy": 6.59417012175922,
                "relative_energy_error_percent": 0.020662720993352944,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.091763341624755e-06,
                  "p90": 0.00013793344260193408,
                  "p95": 0.0002712684217840433,
                  "p99": 0.0005819601938128471,
                  "maximum": 0.001334572210907936
                },
                "worst": {
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "sky_patch_index": 45,
                  "rgb_channel": 0,
                  "reference": 0.001104316208511591,
                  "candidate": -0.00023025600239634514
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 155.5868329014629,
            "full": 430.1961660385132
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 169.05791591852903,
            "full": 422.54904098808765
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 159.28508306387812,
            "full": 422.06124996300787
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 158.64216710906476,
            "full": 423.5446249367669
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_i_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 74,
            "stages": {
              "direct": {
                "nmbe_percent": -0.011499003370351056,
                "cvrmse_percent": 6.632914557601628,
                "rms_normalized_rmse_percent": 1.7896494844399915,
                "reference_energy": 20.49220354488571,
                "candidate_energy": 20.489847145709426,
                "relative_energy_error_percent": 0.011499003370351054,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.5930035412311554e-05,
                  "p95": 9.412341023562476e-05,
                  "p99": 0.000201299786567688,
                  "maximum": 0.0004573296755552292
                },
                "worst": {
                  "global_sensor_index": 42,
                  "local_sensor_index": 42,
                  "sky_patch_index": 78,
                  "rgb_channel": 0,
                  "reference": 0.007492608856409788,
                  "candidate": 0.007949938531965017
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.01855553493634198,
                "cvrmse_percent": 18.73755904087168,
                "rms_normalized_rmse_percent": 1.8389047659707107,
                "reference_energy": 12.676051268472598,
                "candidate_energy": 12.678403377594268,
                "relative_energy_error_percent": 0.01855553493634198,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.271595829166472e-05,
                  "p90": 7.912764704087749e-05,
                  "p95": 0.00015579303726553917,
                  "p99": 0.00033156340941786766,
                  "maximum": 0.0010457132011651993
                },
                "worst": {
                  "global_sensor_index": 46,
                  "local_sensor_index": 46,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0386218186467886,
                  "candidate": 0.0375761054456234
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 226.37725004460663,
            "full": 5313.629874959588
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 224.79487501550466,
            "full": 5251.083084032871
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 237.35449998639524,
            "full": 5217.737583909184
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 231.14733304828405,
            "full": 5231.300792074762
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_i_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 74,
            "stages": {
              "direct": {
                "nmbe_percent": -0.0638023749376602,
                "cvrmse_percent": 6.8561643638287615,
                "rms_normalized_rmse_percent": 1.8497910099116024,
                "reference_energy": 20.50114598845179,
                "candidate_energy": 20.48806577042172,
                "relative_energy_error_percent": 0.06380237493766018,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.569953307509422e-05,
                  "p95": 9.42545011639595e-05,
                  "p99": 0.0002086655586026609,
                  "maximum": 0.0004456997849047184
                },
                "worst": {
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "sky_patch_index": 81,
                  "rgb_channel": 0,
                  "reference": 0.013084080070257187,
                  "candidate": 0.013529779855161905
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.0494654752714196,
                "cvrmse_percent": 18.439845795179863,
                "rms_normalized_rmse_percent": 1.8100520391346042,
                "reference_energy": 12.67501486348361,
                "candidate_energy": 12.681284619826556,
                "relative_energy_error_percent": 0.04946547527141959,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.2957044418726582e-05,
                  "p90": 8.166464976966381e-05,
                  "p95": 0.000157771457452327,
                  "p99": 0.00032040243968367577,
                  "maximum": 0.0009960546158254147
                },
                "worst": {
                  "global_sensor_index": 67,
                  "local_sensor_index": 67,
                  "sky_patch_index": 67,
                  "rgb_channel": 0,
                  "reference": -0.00038788001984357834,
                  "candidate": 0.0006081745959818363
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 236.63358390331268,
            "full": 5550.575541099533
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 235.7779999729246,
            "full": 5520.722124958411
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 233.96483401302248,
            "full": 5522.96595799271
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 234.62579096667469,
            "full": 5537.189834052697
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_i_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 74,
            "stages": {
              "direct": {
                "nmbe_percent": -0.01372902192377117,
                "cvrmse_percent": 3.7375699196543635,
                "rms_normalized_rmse_percent": 1.0082368644001445,
                "reference_energy": 20.493734641270088,
                "candidate_energy": 20.490921051948188,
                "relative_energy_error_percent": 0.013729021923771168,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.343550295336172e-05,
                  "p95": 5.560927093029022e-05,
                  "p99": 0.00011555803939700127,
                  "maximum": 0.00023642205633223057
                },
                "worst": {
                  "global_sensor_index": 69,
                  "local_sensor_index": 69,
                  "sky_patch_index": 44,
                  "rgb_channel": 0,
                  "reference": 0.005510661052539945,
                  "candidate": 0.005274238996207714
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.03017785759028311,
                "cvrmse_percent": 11.228642001387888,
                "rms_normalized_rmse_percent": 1.1031326316674985,
                "reference_energy": 12.688208381395391,
                "candidate_energy": 12.692037410851487,
                "relative_energy_error_percent": 0.030177857590283113,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 9.111350664170459e-06,
                  "p90": 4.832854028791189e-05,
                  "p95": 8.69468494784087e-05,
                  "p99": 0.0001916330074891448,
                  "maximum": 0.0007097255438566208
                },
                "worst": {
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03547171503305435,
                  "candidate": 0.03476198948919773
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 379.13562497124076,
            "full": 9634.729832992889
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 379.0997079340741,
            "full": 9633.022667025216
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 372.52454191911966,
            "full": 9672.310041962191
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 382.7131250873208,
            "full": 9678.980958997272
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 2942.1013749670237,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 11539.838209049776,
      "worker_pool_size": 12,
      "invocation_count": 5
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      74,
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
        "identifier": "plan_i_distributed_grid",
        "full_identifier": "plan_i_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": -0.22682611873526873,
            "cvrmse_percent": 3.5755896852946134,
            "rms_normalized_rmse_percent": 0.9643071481849371,
            "reference_energy": 20.498682697023206,
            "candidate_energy": 20.45218633066969,
            "relative_energy_error_percent": 0.2268261187352687,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.3103301171213388e-05,
              "p95": 3.8043130189180374e-05,
              "p99": 0.00011351401917636395,
              "maximum": 0.00037631718441843987
            },
            "worst": {
              "global_sensor_index": 48,
              "local_sensor_index": 48,
              "sky_patch_index": 133,
              "rgb_channel": 0,
              "reference": 0.006344357039779425,
              "candidate": 0.0067206742241978645,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.3548482463185965,
            "cvrmse_percent": 15.434259658183977,
            "rms_normalized_rmse_percent": 1.5160480692045981,
            "reference_energy": 12.683768000574254,
            "candidate_energy": 12.638759872257097,
            "relative_energy_error_percent": 0.35484824631859657,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.7138325347332284e-05,
              "p90": 5.609169602394104e-05,
              "p95": 7.77812092565e-05,
              "p99": 0.0001654946245253086,
              "maximum": 0.0019363872706890106
            },
            "worst": {
              "global_sensor_index": 61,
              "local_sensor_index": 61,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03845026716589928,
              "candidate": 0.036513879895210266,
              "position": [
                9.5,
                9.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.27576171363767954,
            "cvrmse_percent": 5.692860015579335,
            "rms_normalized_rmse_percent": 1.4629107870107023,
            "reference_energy": 33.18245069759746,
            "candidate_energy": 33.09094620292679,
            "relative_energy_error_percent": 0.27576171363767954,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.6904447875276674e-05,
              "p90": 5.246519867796451e-05,
              "p95": 7.063379598548636e-05,
              "p99": 0.00014094921061769128,
              "maximum": 0.0019363872706890106
            },
            "worst": {
              "global_sensor_index": 61,
              "local_sensor_index": 61,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03845026716589928,
              "candidate": 0.036513879895210266,
              "position": [
                9.5,
                9.5,
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
        "identifier": "plan_i_distributed_grid",
        "full_identifier": "plan_i_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": -0.22682611873526873,
            "cvrmse_percent": 3.5755896852946134,
            "rms_normalized_rmse_percent": 0.9643071481849371,
            "reference_energy": 20.498682697023206,
            "candidate_energy": 20.45218633066969,
            "relative_energy_error_percent": 0.2268261187352687,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.3103301171213388e-05,
              "p95": 3.8043130189180374e-05,
              "p99": 0.00011351401917636395,
              "maximum": 0.00037631718441843987
            },
            "worst": {
              "global_sensor_index": 48,
              "local_sensor_index": 48,
              "sky_patch_index": 133,
              "rgb_channel": 0,
              "reference": 0.006344357039779425,
              "candidate": 0.0067206742241978645,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 91.72049406633137,
            "cvrmse_percent": 528.5508356194712,
            "rms_normalized_rmse_percent": 34.071457754339136,
            "reference_energy": 6.5922842176091745,
            "candidate_energy": 12.638759872257097,
            "relative_energy_error_percent": 91.72049406633137,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 9.215928685080144e-05,
              "p90": 0.00019659940153360367,
              "p95": 0.0002411299938103184,
              "p99": 0.00044302036985754967,
              "maximum": 0.015497766435146332
            },
            "worst": {
              "global_sensor_index": 73,
              "local_sensor_index": 73,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.018420904874801636,
              "candidate": 0.03391867130994797,
              "position": [
                11.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 22.147527281699556,
            "cvrmse_percent": 128.57969587555434,
            "rms_normalized_rmse_percent": 34.061590903490135,
            "reference_energy": 27.090966914632382,
            "candidate_energy": 33.09094620292679,
            "relative_energy_error_percent": 22.14752728169955,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 9.166018935502507e-05,
              "p90": 0.00019409999367780983,
              "p95": 0.00023593055084347725,
              "p99": 0.000413249246776104,
              "maximum": 0.015497766435146332
            },
            "worst": {
              "global_sensor_index": 73,
              "local_sensor_index": 73,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.018420904874801636,
              "candidate": 0.03391867130994797,
              "position": [
                11.5,
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
      "bias_percent": -0.08527626173714699,
      "rms_normalized_error_percent": 0.31036378155486716,
      "absolute_error": {
        "p95": 0.17147270896928343,
        "p99": 0.20071741384539782,
        "maximum": 0.20426850353430126
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 19.91668079551897,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.31036378155486716
    },
    "overcast": {
      "bias_percent": -0.034970160062854645,
      "rms_normalized_error_percent": 0.26760984129548365,
      "absolute_error": {
        "p95": 0.09932332038879393,
        "p99": 0.11298362731933592,
        "maximum": 0.11541748046875
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 12.838888168334961,
      "reference_fraction_of_uniform": 0.6446298956871033,
      "rms_normalized_to_uniform_percent": 0.18348392272733408
    },
    "horizon": {
      "bias_percent": -0.727178956239571,
      "rms_normalized_error_percent": 1.715358939548863,
      "absolute_error": {
        "p95": 0.07990831522948379,
        "p99": 0.0948916027531808,
        "maximum": 0.12956827295239526
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.1534886961049677,
      "reference_fraction_of_uniform": 0.10812487874934856,
      "rms_normalized_to_uniform_percent": 0.14877299798496116
    },
    "north": {
      "bias_percent": -0.13567993475840318,
      "rms_normalized_error_percent": 0.48588068407564705,
      "absolute_error": {
        "p95": 0.0600001811981201,
        "p99": 0.08442167043685903,
        "maximum": 0.10394001007080078
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.720008850097656,
      "reference_fraction_of_uniform": 0.23698772490024567,
      "rms_normalized_to_uniform_percent": 0.12793857812386922
    },
    "east": {
      "bias_percent": -0.24353765289100052,
      "rms_normalized_error_percent": 0.3753709198051981,
      "absolute_error": {
        "p95": 0.07725341320037837,
        "p99": 0.09215713500976562,
        "maximum": 0.09225320816040039
      },
      "worst_index": [
        56
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.662489891052246,
      "reference_fraction_of_uniform": 0.28430891036987305,
      "rms_normalized_to_uniform_percent": 0.1379676689158334
    },
    "south": {
      "bias_percent": 0.04892617118023337,
      "rms_normalized_error_percent": 0.3111673974587054,
      "absolute_error": {
        "p95": 0.05388748645782468,
        "p99": 0.06339128494262689,
        "maximum": 0.0758209228515625
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.427553176879883,
      "reference_fraction_of_uniform": 0.27251294255256653,
      "rms_normalized_to_uniform_percent": 0.10611660846721417
    },
    "west": {
      "bias_percent": -0.11848231759641491,
      "rms_normalized_error_percent": 0.41555042711547885,
      "absolute_error": {
        "p95": 0.07431192398071286,
        "p99": 0.12144665479660033,
        "maximum": 0.123291015625
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.569372177124023,
      "reference_fraction_of_uniform": 0.2796335518360138,
      "rms_normalized_to_uniform_percent": 0.15170913290297944
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
        "identifier": "plan_i_distributed_grid",
        "sensor_count": 74,
        "illuminance": {
          "nmbe_percent": -0.08492428420320126,
          "cvrmse_percent": 1.5229342992253148,
          "absolute_error_percentiles_lux": {
            "p50": 4.83599853515625,
            "p90": 28.1793212890625,
            "p95": 40.07625122070312,
            "p99": 71.31556762695311
          },
          "maximum_absolute_error_lux": 293.09765625,
          "worst": {
            "sensor_index": 0,
            "position": [
              0.5,
              11.5,
              0.75
            ],
            "hour_of_year": 2725.5,
            "foton_lux": 21809.8046875,
            "radiance_lux": 21516.70703125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.15027582376897494,
            "maximum_error_percentage_points": 0.6005479452054772,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.07445231732447616,
            "maximum_error_percentage_points": 0.29924003696875445,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.06997963717141796,
            "maximum_error_percentage_points": 0.40767123287671225,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.08185671973343149,
            "maximum_error_percentage_points": 0.4076712328767229,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.028200666419844585,
            "maximum_error_percentage_points": 0.2457534246575328,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.0,
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
            "identifier": "plan_i_distributed_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_i_distributed_grid",
            "maximum_error_percentage_points": 0.004997859589039422,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_i_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_i_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_i_distributed_grid",
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
      "study_preparation_seconds": 0.009434125036932528,
      "weather_seconds": 0.11402670806273818,
      "metric_reduction_seconds": 0.07341895799618214,
      "write_seconds": 0.028916958021000028,
      "total_seconds": 0.2165707079693675,
      "cold_end_to_end_seconds": 0.22600483300630003,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.012591624981723726,
      "engine_upload_seconds": 0.000307917,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.05223295837640762,
      "engine_annual_reduction_seconds": 0.0006263749673962593,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.05223295837640762
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.009434125036932528,
      "weather_seconds": 0.11307550000492483,
      "metric_reduction_seconds": 0.013222791953012347,
      "write_seconds": 0.02784274995792657,
      "total_seconds": 0.15430699998978525,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.15430699998978525,
      "raw_export_seconds": 0.00981616706121713,
      "engine_upload_seconds": 6.3291e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.000808583339676261,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.019287165952846408,
      "full": 0.04430741700343788
    }
  },
  "elapsed_seconds": 104.28464204201009,
  "result_class": "passed"
}
```
