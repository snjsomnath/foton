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
  "model_sha256": "b635f844f4ed78cc8f0fa2f6bfd606740ccc0d232de9a77b382c46e0f04b8dcd",
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
      "scene_fingerprint": 16343183456666100934,
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/plan_i_distributed/mf2/oracle/scene.rad"
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
            "nmbe_percent": -0.19053075061132035,
            "cvrmse_percent": 3.3212726339166148,
            "rms_normalized_rmse_percent": 0.8241110877153055,
            "reference_energy": 20.49178116281636,
            "candidate_energy": 20.452738018353216,
            "relative_energy_error_percent": 0.19053075061132038,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.069320417940617e-08,
              "p95": 3.552937414497137e-06,
              "p99": 2.1630035917041986e-05,
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
            "nmbe_percent": -0.259976410007693,
            "cvrmse_percent": 20.289353279263,
            "rms_normalized_rmse_percent": 1.1621823587554192,
            "reference_energy": 12.686264957307813,
            "candidate_energy": 12.653283661107741,
            "relative_energy_error_percent": 0.259976410007686,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.62875891571457e-06,
              "p90": 1.6897298337426037e-05,
              "p95": 2.632569521665573e-05,
              "p99": 5.9963479088765026e-05,
              "maximum": 0.0010898448526859283
            },
            "worst": {
              "global_sensor_index": 29,
              "local_sensor_index": 29,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.042233824729919434,
              "candidate": 0.041143979877233505,
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
            "nmbe_percent": -0.2170846360344575,
            "cvrmse_percent": 7.632660333133437,
            "rms_normalized_rmse_percent": 1.1434022422598675,
            "reference_energy": 33.17804612012417,
            "candidate_energy": 33.10602167946095,
            "relative_energy_error_percent": 0.21708463603447087,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.606405582308071e-06,
              "p90": 1.655913729337044e-05,
              "p95": 2.5490975531283766e-05,
              "p99": 5.719142500311246e-05,
              "maximum": 0.0010898448526859283
            },
            "worst": {
              "global_sensor_index": 29,
              "local_sensor_index": 29,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.042233824729919434,
              "candidate": 0.041143979877233505,
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
            "nmbe_percent": -0.19053075061132035,
            "cvrmse_percent": 3.3212726339166148,
            "rms_normalized_rmse_percent": 0.8241110877153055,
            "reference_energy": 20.49178116281636,
            "candidate_energy": 20.452738018353216,
            "relative_energy_error_percent": 0.19053075061132038,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.069320417940617e-08,
              "p95": 3.552937414497137e-06,
              "p99": 2.1630035917041986e-05,
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
            "nmbe_percent": 91.02382662002837,
            "cvrmse_percent": 1043.075162493467,
            "rms_normalized_rmse_percent": 43.55447060148428,
            "reference_energy": 6.623929530150599,
            "candidate_energy": 12.653283661107741,
            "relative_energy_error_percent": 91.02382662002837,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.3442918973159976e-05,
              "p90": 5.470118958328385e-05,
              "p95": 7.284502498805523e-05,
              "p99": 0.000158010935410859,
              "maximum": 0.015380783006548882
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025052698329091072,
              "candidate": 0.040433481335639954,
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
            "nmbe_percent": 22.091661377873134,
            "cvrmse_percent": 254.78971341398545,
            "rms_normalized_rmse_percent": 43.55161993805918,
            "reference_energy": 27.11571069296696,
            "candidate_energy": 33.10602167946095,
            "relative_energy_error_percent": 22.091661377873113,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.3287014300876763e-05,
              "p90": 5.426777079264866e-05,
              "p95": 7.245430606417358e-05,
              "p99": 0.00015575327233818844,
              "maximum": 0.015380783006548882
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025052698329091072,
              "candidate": 0.040433481335639954,
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
      "bias_percent": -0.07489518499714455,
      "rms_normalized_error_percent": 0.20703757870962516,
      "absolute_error": {
        "p95": 0.10519435390940542,
        "p99": 0.13641031794229622,
        "maximum": 0.14201689827400088
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 19.91360571464649,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.20703757870962516
    },
    "overcast": {
      "bias_percent": -0.028036840051385195,
      "rms_normalized_error_percent": 0.15752787482662098,
      "absolute_error": {
        "p95": 0.05680193901062011,
        "p99": 0.06735763549804684,
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
      "rms_normalized_to_uniform_percent": 0.10877428264331135
    },
    "horizon": {
      "bias_percent": -0.6773790441853628,
      "rms_normalized_error_percent": 1.5212271182417438,
      "absolute_error": {
        "p95": 0.05091038905223928,
        "p99": 0.06551659819898493,
        "maximum": 0.07119410425876316
      },
      "worst_index": [
        36
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.834115278681746,
      "reference_fraction_of_uniform": 0.09210362527830664,
      "rms_normalized_to_uniform_percent": 0.11087930225933472
    },
    "north": {
      "bias_percent": -0.07917527819654795,
      "rms_normalized_error_percent": 0.2965703424399001,
      "absolute_error": {
        "p95": 0.0397878527641296,
        "p99": 0.05253396749496456,
        "maximum": 0.058696746826171875
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.684465408325195,
      "reference_fraction_of_uniform": 0.2352394312620163,
      "rms_normalized_to_uniform_percent": 0.07752309583939285
    },
    "east": {
      "bias_percent": -0.10001043629230418,
      "rms_normalized_error_percent": 0.26985861557362395,
      "absolute_error": {
        "p95": 0.044631671905517575,
        "p99": 0.06687089920043922,
        "maximum": 0.10985040664672852
      },
      "worst_index": [
        56
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.560754776000977,
      "reference_fraction_of_uniform": 0.27924397587776184,
      "rms_normalized_to_uniform_percent": 0.09911340172878547
    },
    "south": {
      "bias_percent": -0.0009111784512018248,
      "rms_normalized_error_percent": 0.2269469434538825,
      "absolute_error": {
        "p95": 0.03881370425224303,
        "p99": 0.05219976902008056,
        "maximum": 0.05336761474609375
      },
      "worst_index": [
        48
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.406895160675049,
      "reference_fraction_of_uniform": 0.27151763439178467,
      "rms_normalized_to_uniform_percent": 0.0772563519503063
    },
    "west": {
      "bias_percent": -0.22158994739785567,
      "rms_normalized_error_percent": 0.31710167966414976,
      "absolute_error": {
        "p95": 0.061282444000244095,
        "p99": 0.10797727584838866,
        "maximum": 0.10978317260742188
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.588310241699219,
      "reference_fraction_of_uniform": 0.2806277275085449,
      "rms_normalized_to_uniform_percent": 0.11669157836970503
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
          "nmbe_percent": -0.06109511706212988,
          "cvrmse_percent": 1.7066774214597868,
          "absolute_error_percentiles_lux": {
            "p50": 4.348663330078125,
            "p90": 28.439379882812517,
            "p95": 42.634765625,
            "p99": 87.47235961914058
          },
          "maximum_absolute_error_lux": 326.8291015625,
          "worst": {
            "sensor_index": 56,
            "position": [
              8.5,
              9.5,
              0.75
            ],
            "hour_of_year": 4445.5,
            "foton_lux": 5048.9892578125,
            "radiance_lux": 5375.818359375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.1390984820436878,
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
      "study_preparation_seconds": 0.00824937503784895,
      "weather_seconds": 0.10113541595637798,
      "metric_reduction_seconds": 0.21720020903740078,
      "write_seconds": 0.03470866696443409,
      "total_seconds": 0.35317129199393094,
      "cold_end_to_end_seconds": 0.3614206670317799,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.021228417055681348,
      "engine_upload_seconds": 0.000951625,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.16012887528631836,
      "engine_annual_reduction_seconds": 0.0032235000981017947,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.16012887528631836
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.00824937503784895,
      "weather_seconds": 0.09753704199101776,
      "metric_reduction_seconds": 0.047312375041656196,
      "write_seconds": 0.03508162498474121,
      "total_seconds": 0.180126833030954,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.180126833030954,
      "raw_export_seconds": 0.01578575000166893,
      "engine_upload_seconds": 7.6209e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0033157499274238944,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.023046332993544638,
      "full": 0.16338741697836667
    }
  },
  "elapsed_seconds": 1.8012218340300024,
  "result_class": "passed"
}
```
