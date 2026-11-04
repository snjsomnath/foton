# Foton report

Status: **passed**

```json
{
  "scene": "plan_cross_distributed",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_cross_distributed",
    "category": "form",
    "question": "How does a distributed opening illuminate a CROSS-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "cross",
    "window_profile": "distributed"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 12,
    "shades": 0,
    "sensors": 44,
    "floor_area": 63.0,
    "aperture_area": 14.399999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "61de71c8a4a8b2891bc1854e41bf4cd54113a6fe0bc7e44e3d922958e9b3164f",
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
      "scene_fingerprint": 5695616808233762139,
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 5695616808233762139,
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
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.3)",
      "weather_id": "aff05f88fed2459a6796dca3cabd63daf743bc359ea5c7394adb01155f6785fb"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/usr/local/radiance/bin/gendaymtx",
      "weather_id": "fa596a1b71c81c8eee4f32b17ea6d10a57aabce8541ff637ac4a9c1ee69c4ac1"
    },
    "sun_up_hours_equal": true,
    "compared_hours": 4405,
    "max_relative_difference": 0.0,
    "mean_relative_difference": 0.0
  },
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 65536,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/12f3d0b2-7d1e-44d9-9264-d1e29a27929b/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "38b62f9d0082b4a71f7fe577d02d1ce5b78acd0fbe667ba5fbfd06589212d4d0",
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
          "maximum": 0.0006667673587799072,
          "p95": 6.650947034358978e-05,
          "p99": 0.00021307007409632206
        },
        "bias_percent": 0.05768782644107047,
        "identifier": "plan_cross_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.6073919207378187,
        "worst_index": [
          43,
          129,
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
          "maximum": 0.0005769021809101105,
          "p95": 9.554540156386793e-05,
          "p99": 0.0001837878953665495
        },
        "bias_percent": 0.05512470664104452,
        "identifier": "plan_cross_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8391014028138183,
        "worst_index": [
          31,
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
          "maximum": 0.000743035227060318,
          "p95": 7.916591130197048e-05,
          "p99": 0.00015183165669441223
        },
        "bias_percent": -0.0076580940473004195,
        "identifier": "plan_cross_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7516302766013643,
        "worst_index": [
          2,
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
          "rms_normalized_rmse_percent": 5.0
        },
        "grids": [
          {
            "identifier": "plan_cross_distributed_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0012246432015672326,
                  "p50": 0.0,
                  "p90": 0.00015468895435333252,
                  "p95": 0.0002665109932422638,
                  "p99": 0.00046990346163511276
                },
                "candidate_energy": 17.798483771130577,
                "cvrmse_percent": 11.736074222828394,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.15784283019187903,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 17.770434414513318,
                "relative_energy_error_percent": 0.15784283019187903,
                "rms_normalized_rmse_percent": 3.8684160945498016,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0020723689813166857,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.0008477257797494531,
                  "rgb_channel": 0,
                  "sky_patch_index": 54
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001854587346315384,
                  "p50": 1.5575260476907715e-06,
                  "p90": 0.0002291618729941547,
                  "p95": 0.0003788223257288337,
                  "p99": 0.0007498795166611671
                },
                "candidate_energy": 5.326403827901409,
                "cvrmse_percent": 60.28792236513856,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.8009247637440359,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.369408752264938,
                "relative_energy_error_percent": 0.8009247637440359,
                "rms_normalized_rmse_percent": 4.1033907925219895,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03693956136703491,
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "reference": 0.038794148713350296,
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.2435839837417,
            "full": 302.66325001139194
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.49683308135718,
            "full": 298.96975005976856
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.1408330956474,
            "full": 310.13537500984967
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.9967499738559,
            "full": 290.15779099427164
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
          "rms_normalized_rmse_percent": 5.0
        },
        "grids": [
          {
            "identifier": "plan_cross_distributed_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00043846038170158863,
                  "p50": 0.0,
                  "p90": 6.988202221691608e-05,
                  "p95": 0.00012802472338080406,
                  "p99": 0.00023566698655486107
                },
                "candidate_energy": 17.789511412415763,
                "cvrmse_percent": 5.711314151627655,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.01609091564556617,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 17.78664937766823,
                "relative_energy_error_percent": 0.01609091564556617,
                "rms_normalized_rmse_percent": 1.8831430465110648,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005870466586202383,
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "reference": 0.006308926967903972,
                  "rgb_channel": 0,
                  "sky_patch_index": 55
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013715550303459167,
                  "p50": 1.4558663679054007e-05,
                  "p90": 0.00011370099673513323,
                  "p95": 0.000189950194908306,
                  "p99": 0.00034002121537923813
                },
                "candidate_energy": 10.034353599016889,
                "cvrmse_percent": 16.254436305732238,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.026376261197833466,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 10.03700098461302,
                "relative_energy_error_percent": 0.026376261197833466,
                "rms_normalized_rmse_percent": 1.6185621489563855,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05941666476428509,
                  "global_sensor_index": 41,
                  "local_sensor_index": 41,
                  "reference": 0.05804510973393917,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.9601249927655,
            "full": 3214.647167013027
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.23529199976474,
            "full": 3239.2877500969917
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 183.586832950823,
            "full": 3219.7150830179453
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 180.65816606394947,
            "full": 3192.530208034441
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
          "rms_normalized_rmse_percent": 5.0
        },
        "grids": [
          {
            "identifier": "plan_cross_distributed_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005547835025936365,
                  "p50": 0.0,
                  "p90": 7.052708679111674e-05,
                  "p95": 0.00012743115075863898,
                  "p99": 0.0002338811755180359
                },
                "candidate_energy": 17.79050390630758,
                "cvrmse_percent": 5.817870736374647,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.03624253336317066,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 17.79695397328898,
                "relative_energy_error_percent": 0.03624253336317066,
                "rms_normalized_rmse_percent": 1.9188403788796327,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007726899581030011,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.007172116078436375,
                  "rgb_channel": 0,
                  "sky_patch_index": 32
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0014431364834308624,
                  "p50": 1.388668897561729e-05,
                  "p90": 0.00011416728375479579,
                  "p95": 0.0001933660350914579,
                  "p99": 0.00036826543509960175
                },
                "candidate_energy": 10.054134551165824,
                "cvrmse_percent": 16.65376726799562,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.17472246028728025,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 10.036598359582808,
                "relative_energy_error_percent": 0.17472246028728025,
                "rms_normalized_rmse_percent": 1.6550160402115752,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05837566405534744,
                  "global_sensor_index": 41,
                  "local_sensor_index": 41,
                  "reference": 0.059818800538778305,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 188.32558300346136,
            "full": 3329.5579999685287
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.4042499801144,
            "full": 3361.7074999492615
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 177.83620895352215,
            "full": 3364.57341699861
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 196.12291699741036,
            "full": 3407.7625840436667
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
          "rms_normalized_rmse_percent": 5.0
        },
        "grids": [
          {
            "identifier": "plan_cross_distributed_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002973731607198715,
                  "p50": 0.0,
                  "p90": 4.0499959141016006e-05,
                  "p95": 6.896854029037058e-05,
                  "p99": 0.00012633646838366985
                },
                "candidate_energy": 17.79262257188123,
                "cvrmse_percent": 3.1019788463059386,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.00234441474735832,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 17.792205448792807,
                "relative_energy_error_percent": 0.00234441474735832,
                "rms_normalized_rmse_percent": 1.023052334262872,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.008414619602262974,
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "reference": 0.008711992762982845,
                  "rgb_channel": 0,
                  "sky_patch_index": 79
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007576644420623779,
                  "p50": 9.901231351250317e-06,
                  "p90": 6.387810572050512e-05,
                  "p95": 0.00010997519711963832,
                  "p99": 0.00019381252059247345
                },
                "candidate_energy": 10.043370111188967,
                "cvrmse_percent": 9.710725204336567,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.02347871266794691,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 10.045728718970295,
                "relative_energy_error_percent": 0.023478712667946905,
                "rms_normalized_rmse_percent": 0.9665514044797475,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.052869945764541626,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.053627610206604004,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 296.49445798713714,
            "full": 5889.125292073004
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 288.72366703581065,
            "full": 6009.359874995425
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 288.0532919662073,
            "full": 5914.9324159370735
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 282.1672079153359,
            "full": 5988.905499922112
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
    "/Users/ssanjay/GitHub/foton-0.3.3/validation/results/2026-11-04-architectural-v4-metal-0.3.3-release/plan_cross_distributed/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1162.4052089173347,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_distributed/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4070.7539580762386,
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
        "identifier": "plan_cross_distributed_grid",
        "full_identifier": "plan_cross_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 44,
        "stages": {
          "direct": {
            "nmbe_percent": -0.38394965884355087,
            "cvrmse_percent": 3.4523719384958986,
            "rms_normalized_rmse_percent": 1.1384953434872815,
            "reference_energy": 17.797327991129293,
            "candidate_energy": 17.728995211024085,
            "relative_energy_error_percent": 0.3839496588435509,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.0141440220177174e-05,
              "p95": 6.292662146734074e-05,
              "p99": 0.00014853104948997498,
              "maximum": 0.0005514095537364483
            },
            "worst": {
              "global_sensor_index": 42,
              "local_sensor_index": 42,
              "sky_patch_index": 130,
              "rgb_channel": 0,
              "reference": 0.007197155151516199,
              "candidate": 0.006645745597779751,
              "position": [
                11.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.3407995545598289,
            "cvrmse_percent": 14.674606938869152,
            "rms_normalized_rmse_percent": 1.4595719744518043,
            "reference_energy": 10.039635470648989,
            "candidate_energy": 10.005420437685586,
            "relative_energy_error_percent": 0.3407995545598289,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.043621861957945e-05,
              "p90": 7.070973515510559e-05,
              "p95": 0.00010128022404387593,
              "p99": 0.00020561867859214544,
              "maximum": 0.0017219148576259613
            },
            "worst": {
              "global_sensor_index": 29,
              "local_sensor_index": 29,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.050184495747089386,
              "candidate": 0.048462580889463425,
              "position": [
                6.5,
                4.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.36838721008279146,
            "cvrmse_percent": 5.043975350627795,
            "rms_normalized_rmse_percent": 1.3910281185744937,
            "reference_energy": 27.836963461778282,
            "candidate_energy": 27.73441564870967,
            "relative_energy_error_percent": 0.3683872100827914,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.9580278603825718e-05,
              "p90": 6.494141416624188e-05,
              "p95": 8.794700261205435e-05,
              "p99": 0.000172801548615098,
              "maximum": 0.0017219148576259613
            },
            "worst": {
              "global_sensor_index": 29,
              "local_sensor_index": 29,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.050184495747089386,
              "candidate": 0.048462580889463425,
              "position": [
                6.5,
                4.5,
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
        "identifier": "plan_cross_distributed_grid",
        "full_identifier": "plan_cross_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 44,
        "stages": {
          "direct": {
            "nmbe_percent": -0.38394965884355087,
            "cvrmse_percent": 3.4523719384958986,
            "rms_normalized_rmse_percent": 1.1384953434872815,
            "reference_energy": 17.797327991129293,
            "candidate_energy": 17.728995211024085,
            "relative_energy_error_percent": 0.3839496588435509,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.0141440220177174e-05,
              "p95": 6.292662146734074e-05,
              "p99": 0.00014853104948997498,
              "maximum": 0.0005514095537364483
            },
            "worst": {
              "global_sensor_index": 42,
              "local_sensor_index": 42,
              "sky_patch_index": 130,
              "rgb_channel": 0,
              "reference": 0.007197155151516199,
              "candidate": 0.006645745597779751,
              "position": [
                11.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 87.54171357150781,
            "cvrmse_percent": 505.0634860606256,
            "rms_normalized_rmse_percent": 34.19378019541707,
            "reference_energy": 5.335037334971677,
            "candidate_energy": 10.005420437685586,
            "relative_energy_error_percent": 87.54171357150783,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0001231299975188449,
              "p90": 0.0002440999960526824,
              "p95": 0.000293554192467127,
              "p99": 0.00048667925875633955,
              "maximum": 0.019180025905370712
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0409402921795845,
              "candidate": 0.060120318084955215,
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
            "nmbe_percent": 19.894421766787783,
            "cvrmse_percent": 116.43854980424963,
            "rms_normalized_rmse_percent": 34.18066523967966,
            "reference_energy": 23.13236532610097,
            "candidate_energy": 27.73441564870967,
            "relative_energy_error_percent": 19.894421766787783,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.00012056997729814611,
              "p90": 0.0002354783209739253,
              "p95": 0.0002816470805555582,
              "p99": 0.00046966876834630966,
              "maximum": 0.019180025905370712
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0409402921795845,
              "candidate": 0.060120318084955215,
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
      "bias_percent": -0.2735581869810985,
      "rms_normalized_error_percent": 0.3054805885367142,
      "absolute_error": {
        "p95": 0.16390687590062056,
        "p99": 0.2129254964208865,
        "maximum": 0.2190885885409415
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 28.31237910023091,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.3054805885367142
    },
    "overcast": {
      "bias_percent": -0.19487471612062737,
      "rms_normalized_error_percent": 0.24076094944749113,
      "absolute_error": {
        "p95": 0.0875401020050049,
        "p99": 0.12610816955566406,
        "maximum": 0.13463783264160156
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 17.94532012939453,
      "reference_fraction_of_uniform": 0.6338329911231995,
      "rms_normalized_to_uniform_percent": 0.15708362256563727
    },
    "horizon": {
      "bias_percent": -1.2235445546926107,
      "rms_normalized_error_percent": 1.7129810237364143,
      "absolute_error": {
        "p95": 0.09960362836623173,
        "p99": 0.11373783984158242,
        "maximum": 0.11577615331809721
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.173443248679618,
      "reference_fraction_of_uniform": 0.1120867743909849,
      "rms_normalized_to_uniform_percent": 0.17402315128889298
    },
    "north": {
      "bias_percent": -0.2826630147460837,
      "rms_normalized_error_percent": 0.4188701603702839,
      "absolute_error": {
        "p95": 0.0858193874359131,
        "p99": 0.10106699943542481,
        "maximum": 0.10180473327636719
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.667699813842773,
      "reference_fraction_of_uniform": 0.27082499861717224,
      "rms_normalized_to_uniform_percent": 0.13448904500066156
    },
    "east": {
      "bias_percent": -0.3233765907299782,
      "rms_normalized_error_percent": 0.4434745141601927,
      "absolute_error": {
        "p95": 0.08005123138427735,
        "p99": 0.11169217109680177,
        "maximum": 0.12903404235839844
      },
      "worst_index": [
        36
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.829497814178467,
      "reference_fraction_of_uniform": 0.27653971314430237,
      "rms_normalized_to_uniform_percent": 0.1442332590353802
    },
    "south": {
      "bias_percent": -0.31996303622360944,
      "rms_normalized_error_percent": 0.38551024393160566,
      "absolute_error": {
        "p95": 0.08392214775085452,
        "p99": 0.10814282417297363,
        "maximum": 0.11229324340820312
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.639122486114502,
      "reference_fraction_of_uniform": 0.2698156237602234,
      "rms_normalized_to_uniform_percent": 0.12310527586853089
    },
    "west": {
      "bias_percent": -0.3607891142545508,
      "rms_normalized_error_percent": 0.41123123360184005,
      "absolute_error": {
        "p95": 0.07616236209869387,
        "p99": 0.11943489074707031,
        "maximum": 0.1248922348022461
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.657520771026611,
      "reference_fraction_of_uniform": 0.2704654633998871,
      "rms_normalized_to_uniform_percent": 0.131668490989782
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
        "identifier": "plan_cross_distributed_grid",
        "sensor_count": 44,
        "illuminance": {
          "nmbe_percent": -0.2781803858520075,
          "cvrmse_percent": 1.317848650601726,
          "absolute_error_percentiles_lux": {
            "p50": 5.9498291015625,
            "p90": 33.31676025390625,
            "p95": 47.30180664062499,
            "p99": 82.75093261718749
          },
          "maximum_absolute_error_lux": 245.05859375,
          "worst": {
            "sensor_index": 21,
            "position": [
              5.5,
              0.5,
              0.75
            ],
            "hour_of_year": 4451.5,
            "foton_lux": 39551.859375,
            "radiance_lux": 39306.80078125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.10495952677459609,
            "maximum_error_percentage_points": 0.4971232876712435,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.053188715315350195,
            "maximum_error_percentage_points": 0.24466303357243646,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.03152552926525531,
            "maximum_error_percentage_points": 0.22205479452054888,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.06641344956413339,
            "maximum_error_percentage_points": 0.18999999999999773,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.04770236612702367,
            "maximum_error_percentage_points": 0.1657534246575345,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
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
      "maximum_error_percentage_points": 0.004989833047943648,
      "metrics": {
        "da": [
          {
            "identifier": "plan_cross_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_cross_distributed_grid",
            "maximum_error_percentage_points": 0.004989833047943648,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_cross_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_cross_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_cross_distributed_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
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
      "study_preparation_seconds": 0.007676083012484014,
      "weather_seconds": 0.07569420791696757,
      "metric_reduction_seconds": 0.0368062499910593,
      "write_seconds": 0.011377000017091632,
      "total_seconds": 0.12401000002864748,
      "cold_end_to_end_seconds": 0.1316860830411315,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0015895830001682043,
      "engine_upload_seconds": 0.000327584,
      "engine_acceleration_structure_seconds": 0.002652541,
      "engine_tracing_seconds": 0.01733579149004072,
      "engine_annual_reduction_seconds": 0.00041912496089935303,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.01733579149004072
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007676083012484014,
      "weather_seconds": 0.07154187490232289,
      "metric_reduction_seconds": 0.012591250007972121,
      "write_seconds": 0.010679958038963377,
      "total_seconds": 0.0949951660586521,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.0949951660586521,
      "raw_export_seconds": 0.002300583990290761,
      "engine_upload_seconds": 4.5e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0004209582693874836,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02179208304733038,
      "full": 0.021535416948609054
    }
  },
  "elapsed_seconds": 0.7252404589671642,
  "result_class": "passed"
}
```
