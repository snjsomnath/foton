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
  "model_sha256": "37f108974287fe37ce49f9960e808f6302b50110b0a62c33183c6d13a6c7ed3a",
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
      "solver_version": "0.2.0",
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
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 262144,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "plan_cross_arch_grid",
        "bias_percent": 0.0417184612529181,
        "rms_normalized_error_percent": 0.9238426291090699,
        "absolute_error": {
          "p95": 0.0,
          "p99": 5.430774763226509e-07,
          "maximum": 0.00019649998284876347
        },
        "worst_index": [
          21,
          517,
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
        "identifier": "plan_cross_arch_grid",
        "bias_percent": 0.012409068480823376,
        "rms_normalized_error_percent": 2.348324038852969,
        "absolute_error": {
          "p95": 5.413315193436574e-06,
          "p99": 4.6703265979886055e-05,
          "maximum": 0.0005058441311120987
        },
        "worst_index": [
          30,
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
        "identifier": "plan_cross_arch_grid",
        "bias_percent": 0.05123789872270178,
        "rms_normalized_error_percent": 1.7430924926816547,
        "absolute_error": {
          "p95": 4.629870090866461e-06,
          "p99": 4.1063292883336544e-05,
          "maximum": 0.00016948190750554204
        },
        "worst_index": [
          9,
          89,
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
            "identifier": "plan_cross_arch_grid",
            "start_sensor_index": 0,
            "sensor_count": 44,
            "stages": {
              "direct": {
                "nmbe_percent": -0.11749589623165778,
                "cvrmse_percent": 109.39713243335575,
                "rms_normalized_rmse_percent": 11.691945613070562,
                "reference_energy": 2.4616666446163435,
                "candidate_energy": 2.458774287330016,
                "relative_energy_error_percent": 0.11749589623165779,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00015629921108484268,
                  "maximum": 0.0010357290739193559
                },
                "worst": {
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "sky_patch_index": 151,
                  "rgb_channel": 0,
                  "reference": 0.0023537210654467344,
                  "candidate": 0.0013179919915273786
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.31587069432023,
                "cvrmse_percent": 559.6827683810347,
                "rms_normalized_rmse_percent": 10.643080757227857,
                "reference_energy": 0.5837546305691887,
                "candidate_energy": 0.5855985403738941,
                "relative_energy_error_percent": 0.31587069432023,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.919643404515227e-06,
                  "p99": 0.00018371210899204016,
                  "maximum": 0.0013179810484871268
                },
                "worst": {
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "sky_patch_index": 151,
                  "rgb_channel": 0,
                  "reference": -0.0007067785481922328,
                  "candidate": 0.000611202500294894
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 117.25033400580287,
            "full": 264.66754195280373
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 110.98945897538215,
            "full": 269.48020805139095
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 110.96874997019768,
            "full": 269.9409999186173
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 119.60350000299513,
            "full": 282.2620830265805
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
            "identifier": "plan_cross_arch_grid",
            "start_sensor_index": 0,
            "sensor_count": 44,
            "stages": {
              "direct": {
                "nmbe_percent": 0.06300310884373357,
                "cvrmse_percent": 47.050667796393796,
                "rms_normalized_rmse_percent": 5.032593947051449,
                "reference_energy": 2.4615518711916593,
                "candidate_energy": 2.463102725396311,
                "relative_energy_error_percent": 0.06300310884373357,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.056185313558672e-05,
                  "maximum": 0.00030496076215058565
                },
                "worst": {
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "sky_patch_index": 92,
                  "rgb_channel": 0,
                  "reference": 0.0005159596621524543,
                  "candidate": 0.0008209204243030399
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.13735508902383667,
                "cvrmse_percent": 152.88454936641813,
                "rms_normalized_rmse_percent": 4.594850121089236,
                "reference_energy": 1.1244621911006334,
                "candidate_energy": 1.1229176850570077,
                "relative_energy_error_percent": 0.1373550890238367,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.8497855712193996e-06,
                  "p95": 7.805446784914238e-06,
                  "p99": 0.0001007190439850092,
                  "maximum": 0.0005691088736057281
                },
                "worst": {
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.021094169467687607,
                  "candidate": 0.02052506059408188
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 148.29466701485217,
            "full": 3265.412750071846
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 155.49845900386572,
            "full": 3230.090625002049
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 152.6187090203166,
            "full": 3247.024375014007
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 157.38541691098362,
            "full": 3325.4159999778494
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
            "identifier": "plan_cross_arch_grid",
            "start_sensor_index": 0,
            "sensor_count": 44,
            "stages": {
              "direct": {
                "nmbe_percent": -0.10970527353537908,
                "cvrmse_percent": 43.24883476566012,
                "rms_normalized_rmse_percent": 4.631503670838651,
                "reference_energy": 2.4654596809177747,
                "candidate_energy": 2.4627549416309193,
                "relative_energy_error_percent": 0.10970527353537908,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.000360346864909e-05,
                  "maximum": 0.00042141834273934364
                },
                "worst": {
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "sky_patch_index": 451,
                  "rgb_channel": 0,
                  "reference": 0.004960973979905248,
                  "candidate": 0.004539555637165904
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.48933825139213144,
                "cvrmse_percent": 141.3712057742914,
                "rms_normalized_rmse_percent": 4.229731496370629,
                "reference_energy": 1.1196155542506574,
                "candidate_energy": 1.1250942614261419,
                "relative_energy_error_percent": 0.48933825139213144,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.7606309888360556e-06,
                  "p95": 7.812826879671775e-06,
                  "p99": 9.515452256891876e-05,
                  "maximum": 0.0004896149039268494
                },
                "worst": {
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.020565900020301342,
                  "candidate": 0.02105551492422819
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 150.86012508254498,
            "full": 3485.2799579966813
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 152.11870800703764,
            "full": 3490.0437920587137
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 163.72704203240573,
            "full": 3472.1798331011087
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 149.48566700331867,
            "full": 3476.6052500344813
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
            "identifier": "plan_cross_arch_grid",
            "start_sensor_index": 0,
            "sensor_count": 44,
            "stages": {
              "direct": {
                "nmbe_percent": 0.07537922940545216,
                "cvrmse_percent": 23.239170732547585,
                "rms_normalized_rmse_percent": 2.486773089749364,
                "reference_energy": 2.4624312329151508,
                "candidate_energy": 2.4642873946031614,
                "relative_energy_error_percent": 0.07537922940545218,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.427124465815723e-05,
                  "maximum": 0.00018322805408388376
                },
                "worst": {
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "sky_patch_index": 308,
                  "rgb_channel": 0,
                  "reference": 0.0035431409487500787,
                  "candidate": 0.0037263690028339624
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.24598669712685486,
                "cvrmse_percent": 79.90461393596615,
                "rms_normalized_rmse_percent": 2.4020966143740923,
                "reference_energy": 1.126325851043397,
                "candidate_energy": 1.1235552392835295,
                "relative_energy_error_percent": 0.24598669712685486,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.6391625169708277e-06,
                  "p95": 5.4787651606602594e-06,
                  "p99": 5.129725468577817e-05,
                  "maximum": 0.0003173248842358589
                },
                "worst": {
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.024349144659936428,
                  "candidate": 0.02403181977570057
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 221.44466696772724,
            "full": 6180.295667028986
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 217.574542039074,
            "full": 6286.77420807071
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 240.5199579661712,
            "full": 6243.753540911712
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 224.8219168977812,
            "full": 6351.162667036988
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 4195.87241706904,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_cross_arch/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 15974.448874942027,
      "worker_pool_size": 12,
      "invocation_count": 3
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
            "nmbe_percent": -1.9499838602282653,
            "cvrmse_percent": 80.50609672281361,
            "rms_normalized_rmse_percent": 2.419318816671245,
            "reference_energy": 1.1253264111263626,
            "candidate_energy": 1.1033827277345125,
            "relative_energy_error_percent": 1.9499838602282653,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.4501301797718043e-06,
              "p95": 6.420634235837497e-06,
              "p99": 2.3777494789101183e-05,
              "maximum": 0.0006750822067260742
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02076476253569126,
              "candidate": 0.020089680328965187,
              "position": [
                6.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.6024625545104484,
            "cvrmse_percent": 25.18340506550581,
            "rms_normalized_rmse_percent": 2.41317600941672,
            "reference_energy": 3.5882998534499357,
            "candidate_energy": 3.5666816904893466,
            "relative_energy_error_percent": 0.6024625545104484,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.4502518815315852e-06,
              "p95": 6.4421301431139e-06,
              "p99": 2.338876947760582e-05,
              "maximum": 0.0006750822067260742
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02076476253569126,
              "candidate": 0.020089680328965187,
              "position": [
                6.5,
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
            "nmbe_percent": 89.60954961146517,
            "cvrmse_percent": 1441.8888135135046,
            "rms_normalized_rmse_percent": 27.31024014272407,
            "reference_energy": 0.5819236056387922,
            "candidate_energy": 1.1033827277345125,
            "relative_energy_error_percent": 89.60954961146516,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.170999985333765e-05,
              "p95": 2.5830012646110845e-05,
              "p99": 7.963589450810105e-05,
              "maximum": 0.006191812455654144
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01733817718923092,
              "candidate": 0.023529989644885063,
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
            "nmbe_percent": 17.136364031623263,
            "cvrmse_percent": 275.5915460504128,
            "rms_normalized_rmse_percent": 27.31280324403508,
            "reference_energy": 3.0448970479623654,
            "candidate_energy": 3.5666816904893466,
            "relative_energy_error_percent": 17.13636403162326,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.168000017059967e-05,
              "p95": 2.5830012646110845e-05,
              "p99": 7.963589450810105e-05,
              "maximum": 0.006191812455654144
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01733817718923092,
              "candidate": 0.023529989644885063,
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
      "bias_percent": -0.01798702155572136,
      "rms_normalized_error_percent": 0.13306698905730877,
      "absolute_error": {
        "p95": 0.033951457621615555,
        "p99": 0.048786317931470286,
        "maximum": 0.049016903817770796
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.8253200179807973,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.13306698905730877
    },
    "overcast": {
      "bias_percent": -0.0037999857042997033,
      "rms_normalized_error_percent": 0.10963086122022926,
      "absolute_error": {
        "p95": 0.019306439161300662,
        "p99": 0.03191488027572632,
        "maximum": 0.03443717956542969
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.533971071243286,
      "reference_fraction_of_uniform": 0.6624206900596619,
      "rms_normalized_to_uniform_percent": 0.07846860938536393
    },
    "horizon": {
      "bias_percent": -0.4359264601661077,
      "rms_normalized_error_percent": 1.8867023082655479,
      "absolute_error": {
        "p95": 0.01997449661534002,
        "p99": 0.03125241998577255,
        "maximum": 0.038783567306732825
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.35408358746176405,
      "reference_fraction_of_uniform": 0.09256312826048675,
      "rms_normalized_to_uniform_percent": 0.09147139749336669
    },
    "north": {
      "bias_percent": -98.05307654333346,
      "rms_normalized_error_percent": 100.08312500577952,
      "absolute_error": {
        "p95": 9.242802570952344e-05,
        "p99": 0.0001564253552351147,
        "maximum": 0.0001596504298504442
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.3109166502545122e-05,
      "reference_fraction_of_uniform": 3.426946477702586e-06,
      "rms_normalized_to_uniform_percent": 0.0003314619924718693
    },
    "east": {
      "bias_percent": -0.08201880440212775,
      "rms_normalized_error_percent": 0.10276584990129921,
      "absolute_error": {
        "p95": 0.005889426171779634,
        "p99": 0.007654775083065033,
        "maximum": 0.007667064666748047
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5636072754859924,
      "reference_fraction_of_uniform": 0.1473359763622284,
      "rms_normalized_to_uniform_percent": 0.022003535516941997
    },
    "south": {
      "bias_percent": -0.01065179568762185,
      "rms_normalized_error_percent": 0.15673566641248773,
      "absolute_error": {
        "p95": 0.02883349657058717,
        "p99": 0.03486058712005615,
        "maximum": 0.036118507385253906
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.7611570358276367,
      "reference_fraction_of_uniform": 0.7218107581138611,
      "rms_normalized_to_uniform_percent": 0.10362921766151444
    },
    "west": {
      "bias_percent": -0.02547007005757556,
      "rms_normalized_error_percent": 0.18831855228554806,
      "absolute_error": {
        "p95": 0.01251126304268838,
        "p99": 0.016829264163970948,
        "maximum": 0.018917083740234375
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5732095241546631,
      "reference_fraction_of_uniform": 0.1498461663722992,
      "rms_normalized_to_uniform_percent": 0.040684145596099675
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
          "nmbe_percent": -0.04403754408228046,
          "cvrmse_percent": 2.76379333748134,
          "absolute_error_percentiles_lux": {
            "p50": 0.571448802947998,
            "p90": 8.0133056640625,
            "p95": 14.13858337402343,
            "p99": 39.85642578124998
          },
          "maximum_absolute_error_lux": 293.52734375,
          "worst": {
            "sensor_index": 33,
            "position": [
              6.5,
              0.5,
              0.75
            ],
            "hour_of_year": 1357.5,
            "foton_lux": 17238.3359375,
            "radiance_lux": 16944.80859375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.07518991282689962,
            "maximum_error_percentage_points": 1.1817808219178119,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.15701168313045158,
            "maximum_error_percentage_points": 0.7851469399994997,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.2687266500622672,
            "maximum_error_percentage_points": 2.0528767123287537,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.2699626400996264,
            "maximum_error_percentage_points": 2.052876712328768,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.004844333748443167,
            "maximum_error_percentage_points": 0.028493150684930413,
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
      "study_preparation_seconds": 0.007864915998652577,
      "weather_seconds": 0.12500541703775525,
      "metric_reduction_seconds": 0.13466341700404882,
      "write_seconds": 0.029588749981485307,
      "total_seconds": 0.2894099169643596,
      "cold_end_to_end_seconds": 0.29727483296301216,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.01567841600626707,
      "engine_upload_seconds": 0.000867042,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.08195104158949107,
      "engine_annual_reduction_seconds": 0.0018593750428408384,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.08195104158949107
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007864915998652577,
      "weather_seconds": 0.10920620907563716,
      "metric_reduction_seconds": 0.04501633404288441,
      "write_seconds": 0.034135624999180436,
      "total_seconds": 0.18854837503749877,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.18854837503749877,
      "raw_export_seconds": 0.011150042060762644,
      "engine_upload_seconds": 7.375e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0019615000346675515,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01711695792619139,
      "full": 0.08104624995030463
    }
  },
  "elapsed_seconds": 78.38312329200562,
  "result_class": "passed"
}
```
