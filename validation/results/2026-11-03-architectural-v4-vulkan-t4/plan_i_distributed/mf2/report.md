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
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "4edbaf300b270dc1dbe86fbae8f6f56e485ceeecb5e84bdd0c1a61315daabc03",
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
      "scene_fingerprint": 16343183456666100934,
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
      "scene_fingerprint": 16343183456666100934,
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
    "model_sha256": "866ca4a3ef8dd207bb87e8300e19721a4e5021db43a21942b4162f00265ee545",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "274288e18ebb896ca8da417745929f291321088f610eaef564604626c7d101ce",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00013830000534653664,
          "p95": 2.8614485927391797e-06,
          "p99": 2.3933553893585247e-05
        },
        "bias_percent": 0.0277428871487856,
        "identifier": "plan_i_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.923732058617109,
        "worst_index": [
          1,
          522,
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
          "maximum": 0.0006738603115081787,
          "p95": 4.844367504119873e-05,
          "p99": 0.00012081001186743447
        },
        "bias_percent": 0.044883483522619526,
        "identifier": "plan_i_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.5144807378299998,
        "worst_index": [
          22,
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
          "maximum": 0.0004598982632160187,
          "p95": 3.9096223190426826e-05,
          "p99": 9.593393770046547e-05
        },
        "bias_percent": 0.03603101875812208,
        "identifier": "plan_i_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.20216320123419,
        "worst_index": [
          21,
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
            "identifier": "plan_i_distributed_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007370775565505028,
                  "p50": 0.0,
                  "p90": 3.287173603894189e-05,
                  "p95": 0.00010619848035275936,
                  "p99": 0.0002840142260538414
                },
                "candidate_energy": 20.49752378308314,
                "cvrmse_percent": 35.24324147867165,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.03943248757060229,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 20.505609655061647,
                "relative_energy_error_percent": 0.03943248757060229,
                "rms_normalized_rmse_percent": 8.739495201627093,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0043192170560359955,
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "reference": 0.0035821394994854927,
                  "rgb_channel": 0,
                  "sky_patch_index": 377
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011097351089119911,
                  "p50": 0.0,
                  "p90": 4.734153480967507e-05,
                  "p95": 0.00015666408580727875,
                  "p99": 0.0004068270005518657
                },
                "candidate_energy": 6.6108316917510415,
                "cvrmse_percent": 153.83491077157143,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.10010591662155462,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.61745615689393,
                "relative_energy_error_percent": 0.10010591662155462,
                "rms_normalized_rmse_percent": 6.41090494456573,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.024488460272550583,
                  "global_sensor_index": 54,
                  "local_sensor_index": 54,
                  "reference": 0.023378725163638592,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 168.84675004985183,
            "full": 429.0554169565439
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 164.24404201097786,
            "full": 436.10208306927234
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 167.16237494256347,
            "full": 449.0234999684617
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 161.32266691420227,
            "full": 424.8636669944972
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
            "identifier": "plan_i_distributed_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004140585660934448,
                  "p50": 0.0,
                  "p90": 1.7989586922340095e-05,
                  "p95": 6.6739710746333e-05,
                  "p99": 0.00016200389909499813
                },
                "candidate_energy": 20.492057228343768,
                "cvrmse_percent": 19.573862996811872,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.0009655830542466474,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 20.492255098086428,
                "relative_energy_error_percent": 0.0009655830542466474,
                "rms_normalized_rmse_percent": 4.854809632432035,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003633544547483325,
                  "global_sensor_index": 61,
                  "local_sensor_index": 61,
                  "reference": 0.00321948598138988,
                  "rgb_channel": 0,
                  "sky_patch_index": 265
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009213685989379883,
                  "p50": 5.820854198645975e-06,
                  "p90": 3.457114871707745e-05,
                  "p95": 9.315001079812646e-05,
                  "p99": 0.00023443376703653562
                },
                "candidate_energy": 12.65888774590816,
                "cvrmse_percent": 48.90681220218651,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.002728813035276632,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.659233192713689,
                "relative_energy_error_percent": 0.0027288130352766324,
                "rms_normalized_rmse_percent": 2.800914277767937,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03673199564218521,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.0376533642411232,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 248.5575000755489,
            "full": 5284.307124908082
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 249.82500006444752,
            "full": 5425.799791933969
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 247.18087504152209,
            "full": 5240.848999936134
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 249.73616702482104,
            "full": 5457.127625006251
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
            "identifier": "plan_i_distributed_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00042238435707986355,
                  "p50": 0.0,
                  "p90": 1.808334855013527e-05,
                  "p95": 6.743364792782813e-05,
                  "p99": 0.00016103744565043615
                },
                "candidate_energy": 20.48932905446692,
                "cvrmse_percent": 19.532984309634227,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.026208248395552754,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 20.494700356444262,
                "relative_energy_error_percent": 0.02620824839555275,
                "rms_normalized_rmse_percent": 4.845362521634622,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0007981121307238936,
                  "global_sensor_index": 72,
                  "local_sensor_index": 72,
                  "reference": 0.0012204964878037572,
                  "rgb_channel": 0,
                  "sky_patch_index": 77
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009005554020404816,
                  "p50": 5.805515115753224e-06,
                  "p90": 3.6494689993560314e-05,
                  "p95": 9.500277155893855e-05,
                  "p99": 0.0002353139821934754
                },
                "candidate_energy": 12.673772566635712,
                "cvrmse_percent": 48.571561632031695,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.004873000039270182,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.674390189674632,
                "relative_energy_error_percent": 0.004873000039270182,
                "rms_normalized_rmse_percent": 2.778121060054505,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03977989964187145,
                  "global_sensor_index": 68,
                  "local_sensor_index": 68,
                  "reference": 0.040680455043911934,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 248.16804099828005,
            "full": 5612.493915949017
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 253.16545902751386,
            "full": 5629.018959007226
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 248.44420794397593,
            "full": 5649.470250005834
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 243.8357500359416,
            "full": 5688.289207988419
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
            "identifier": "plan_i_distributed_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00024782196851447225,
                  "p50": 0.0,
                  "p90": 1.0614876430281583e-05,
                  "p95": 3.493495751172304e-05,
                  "p99": 9.10492439288646e-05
                },
                "candidate_energy": 20.49852269216728,
                "cvrmse_percent": 10.924900541037982,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0012369152334328385,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 20.498269145953625,
                "relative_energy_error_percent": 0.0012369152334328383,
                "rms_normalized_rmse_percent": 2.7118070673856485,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001860811491496861,
                  "global_sensor_index": 54,
                  "local_sensor_index": 54,
                  "reference": 0.0016129895229823887,
                  "rgb_channel": 0,
                  "sky_patch_index": 206
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006296541541814804,
                  "p50": 4.1391681122604496e-06,
                  "p90": 2.2088204786996357e-05,
                  "p95": 5.3457566536962986e-05,
                  "p99": 0.00013533792080124878
                },
                "candidate_energy": 12.678901179386141,
                "cvrmse_percent": 28.65595852077571,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.011814068109131931,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.680399250390092,
                "relative_energy_error_percent": 0.011814068109131931,
                "rms_normalized_rmse_percent": 1.639871372510779,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.042625635862350464,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.043255290016531944,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 400.07895801682025,
            "full": 9832.39654195495
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 397.384834010154,
            "full": 9973.297708900645
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 393.7805419554934,
            "full": 9865.439499961212
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 408.0048749456182,
            "full": 9905.134042026475
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/plan_i_distributed/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 11358.588499948382,
      "invocation_count": 5,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_distributed/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 45579.07408406027,
      "invocation_count": 5,
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
        "identifier": "plan_i_distributed_grid",
        "full_identifier": "plan_i_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": -0.19053257679749827,
            "cvrmse_percent": 3.3218436630250876,
            "rms_normalized_rmse_percent": 0.8242527778056928,
            "reference_energy": 20.49178116281636,
            "candidate_energy": 20.45273764413514,
            "relative_energy_error_percent": 0.19053257679749824,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.069320417940617e-08,
              "p95": 3.5576777008827776e-06,
              "p99": 2.16300526517445e-05,
              "maximum": 0.00015418848488479853
            },
            "worst": {
              "global_sensor_index": 56,
              "local_sensor_index": 56,
              "sky_patch_index": 141,
              "rgb_channel": 0,
              "reference": 0.0015848726034164429,
              "candidate": 0.0014306841185316443,
              "position": [
                8.5,
                9.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.26010605750729243,
            "cvrmse_percent": 20.29056400964448,
            "rms_normalized_rmse_percent": 1.1622517098811647,
            "reference_energy": 12.686264957307813,
            "candidate_energy": 12.653267213682431,
            "relative_energy_error_percent": 0.26010605750728544,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.62875891571457e-06,
              "p90": 1.6897298337426037e-05,
              "p95": 2.632569521665573e-05,
              "p99": 5.9963479088765026e-05,
              "maximum": 0.001089785248041153
            },
            "worst": {
              "global_sensor_index": 29,
              "local_sensor_index": 29,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.042233824729919434,
              "candidate": 0.04114403948187828,
              "position": [
                5.5,
                7.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.21713533716171496,
            "cvrmse_percent": 7.633186850164164,
            "rms_normalized_rmse_percent": 1.1434811165615193,
            "reference_energy": 33.17804612012417,
            "candidate_energy": 33.10600485781757,
            "relative_energy_error_percent": 0.21713533716172834,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.606405582308071e-06,
              "p90": 1.6560954463784583e-05,
              "p95": 2.5490975531283766e-05,
              "p99": 5.719132605008891e-05,
              "maximum": 0.001089785248041153
            },
            "worst": {
              "global_sensor_index": 29,
              "local_sensor_index": 29,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.042233824729919434,
              "candidate": 0.04114403948187828,
              "position": [
                5.5,
                7.5,
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
        "identifier": "plan_i_distributed_grid",
        "full_identifier": "plan_i_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": -0.19053257679749827,
            "cvrmse_percent": 3.3218436630250876,
            "rms_normalized_rmse_percent": 0.8242527778056928,
            "reference_energy": 20.49178116281636,
            "candidate_energy": 20.45273764413514,
            "relative_energy_error_percent": 0.19053257679749824,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.069320417940617e-08,
              "p95": 3.5576777008827776e-06,
              "p99": 2.16300526517445e-05,
              "maximum": 0.00015418848488479853
            },
            "worst": {
              "global_sensor_index": 56,
              "local_sensor_index": 56,
              "sky_patch_index": 141,
              "rgb_channel": 0,
              "reference": 0.0015848726034164429,
              "candidate": 0.0014306841185316443,
              "position": [
                8.5,
                9.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 91.0235783168839,
            "cvrmse_percent": 1043.072926517914,
            "rms_normalized_rmse_percent": 43.55437723646613,
            "reference_energy": 6.623929530150599,
            "candidate_energy": 12.653267213682431,
            "relative_energy_error_percent": 91.02357831688391,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.3441160010406747e-05,
              "p90": 5.470118958328385e-05,
              "p95": 7.284502498805523e-05,
              "p99": 0.000158010935410859,
              "maximum": 0.015380742028355598
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025052698329091072,
              "candidate": 0.04043344035744667,
              "position": [
                2.5,
                11.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 22.091599341352772,
            "cvrmse_percent": 254.7892283268902,
            "rms_normalized_rmse_percent": 43.55153702133336,
            "reference_energy": 27.11571069296696,
            "candidate_energy": 33.10600485781757,
            "relative_energy_error_percent": 22.09159934135275,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.3287014300876763e-05,
              "p90": 5.426777079264866e-05,
              "p95": 7.245430606417358e-05,
              "p99": 0.00015575316465401575,
              "maximum": 0.015380742028355598
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025052698329091072,
              "candidate": 0.04043344035744667,
              "position": [
                2.5,
                11.5,
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
      "bias_percent": -0.07492962920067592,
      "rms_normalized_error_percent": 0.2070797560529515,
      "absolute_error": {
        "p95": 0.10519845834662041,
        "p99": 0.1364121897724698,
        "maximum": 0.1420168552949228
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 19.91360571464649,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2070797560529515
    },
    "overcast": {
      "bias_percent": -0.028069234690518002,
      "rms_normalized_error_percent": 0.15746801297043905,
      "absolute_error": {
        "p95": 0.05680446624755858,
        "p99": 0.06736042022705074,
        "maximum": 0.07326126098632812
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 12.929347038269043,
      "reference_fraction_of_uniform": 0.6492719650268555,
      "rms_normalized_to_uniform_percent": 0.10873294969546017
    },
    "horizon": {
      "bias_percent": -0.6775296460179665,
      "rms_normalized_error_percent": 1.5209502046096608,
      "absolute_error": {
        "p95": 0.05091041905619709,
        "p99": 0.06551666749298632,
        "maximum": 0.07119416547139545
      },
      "worst_index": [
        36
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.834115278681746,
      "reference_fraction_of_uniform": 0.09210362527830664,
      "rms_normalized_to_uniform_percent": 0.11085911856030434
    },
    "north": {
      "bias_percent": -0.07928764437984316,
      "rms_normalized_error_percent": 0.29642006298919854,
      "absolute_error": {
        "p95": 0.039788204431533775,
        "p99": 0.05253465652465817,
        "maximum": 0.05869865417480469
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.684464931488037,
      "reference_fraction_of_uniform": 0.2352394014596939,
      "rms_normalized_to_uniform_percent": 0.07748381359705392
    },
    "east": {
      "bias_percent": -0.09995103393376067,
      "rms_normalized_error_percent": 0.2698011173927547,
      "absolute_error": {
        "p95": 0.04463117122650146,
        "p99": 0.06687137603759742,
        "maximum": 0.10985088348388672
      },
      "worst_index": [
        56
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.560754776000977,
      "reference_fraction_of_uniform": 0.27924397587776184,
      "rms_normalized_to_uniform_percent": 0.09909228598368759
    },
    "south": {
      "bias_percent": -0.0009430432417941978,
      "rms_normalized_error_percent": 0.22694862835203197,
      "absolute_error": {
        "p95": 0.038813745975494376,
        "p99": 0.05220216274261474,
        "maximum": 0.053379058837890625
      },
      "worst_index": [
        48
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.406895160675049,
      "reference_fraction_of_uniform": 0.27151763439178467,
      "rms_normalized_to_uniform_percent": 0.07725692440873552
    },
    "west": {
      "bias_percent": -0.22169280290869273,
      "rms_normalized_error_percent": 0.3171248731652019,
      "absolute_error": {
        "p95": 0.06128215789794917,
        "p99": 0.107975754737854,
        "maximum": 0.10978269577026367
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.588310241699219,
      "reference_fraction_of_uniform": 0.2806277275085449,
      "rms_normalized_to_uniform_percent": 0.11670010727566942
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
          "nmbe_percent": -0.06114369750666354,
          "cvrmse_percent": 1.7066635880946084,
          "absolute_error_percentiles_lux": {
            "p50": 4.3480682373046875,
            "p90": 28.441235351562504,
            "p95": 42.63172302246093,
            "p99": 87.47224609374996
          },
          "maximum_absolute_error_lux": 326.82958984375,
          "worst": {
            "sensor_index": 56,
            "position": [
              8.5,
              9.5,
              0.75
            ],
            "hour_of_year": 4445.5,
            "foton_lux": 5048.98876953125,
            "radiance_lux": 5375.818359375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.1395038874490932,
            "maximum_error_percentage_points": 0.6847945205479391,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.06174117937921691,
            "maximum_error_percentage_points": 0.2738878634422406,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.0635560903369123,
            "maximum_error_percentage_points": 0.38753424657534197,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.07932247315808935,
            "maximum_error_percentage_points": 0.38123287671231765,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.025653461680858795,
            "maximum_error_percentage_points": 0.18931506849315127,
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
      "maximum_error_percentage_points": 0.004931506849315426,
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
            "maximum_error_percentage_points": 0.004897260273978077,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_i_distributed_grid",
            "maximum_error_percentage_points": 0.004520547945212172,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_i_distributed_grid",
            "maximum_error_percentage_points": 0.004657534246574002,
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
      "study_preparation_seconds": 0.3775910770018527,
      "weather_seconds": 0.25029080400054227,
      "metric_reduction_seconds": 2.1563526559984894,
      "write_seconds": 0.024409209996520076,
      "total_seconds": 2.431546530999185,
      "cold_end_to_end_seconds": 2.8091376080010377,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.010642407996783732,
      "engine_upload_seconds": 0.047097779,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.088662922,
      "engine_annual_reduction_seconds": 0.094006865,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.088662922
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3775910770018527,
      "weather_seconds": 0.252022639997449,
      "metric_reduction_seconds": 2.0173307929981092,
      "write_seconds": 0.025520148003124632,
      "total_seconds": 2.295136606997403,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 2.295136606997403,
      "raw_export_seconds": 0.01229041800252162,
      "engine_upload_seconds": 0.047309762,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.5e-08,
      "engine_annual_reduction_seconds": 0.076531964,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02203121699858457,
      "full": 0.10190994499862427
    }
  },
  "elapsed_seconds": 8.236375852997298,
  "result_class": "passed"
}
```
