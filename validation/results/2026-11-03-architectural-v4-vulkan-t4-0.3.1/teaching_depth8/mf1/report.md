# Foton report

Status: **passed**

```json
{
  "scene": "teaching_depth8",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_depth8",
    "category": "teaching",
    "question": "How does daylight fall off in an 8 m deep room?",
    "interactions": [
      "multiple_bounces",
      "room",
      "side_glazing"
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
    "sensors": 48,
    "floor_area": 48.0,
    "aperture_area": 4.499999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "fd3aa3e47b16a54b84f5c09933909716869fdde2617d4985d5a955e34df9e8be",
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 7711455366643186943,
      "basis": "Tregenza",
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 7711455366643186943,
      "basis": "Tregenza",
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
  "reference_source": {
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "30b1c00e51d152792af875274bd2e8bdb45a29a6f3570f71ae1e408959e44f87",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "f6d6e65ba07d4bd1ed66e7715cd3ea4c7e6e299c4d91d0f82d38c8c28e87102d",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00029224716126918793,
          "p95": 4.4424086809158325e-06,
          "p99": 9.02470201253891e-05
        },
        "bias_percent": -0.05485834551319389,
        "identifier": "teaching_depth8_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9725811534349869,
        "worst_index": [
          23,
          121,
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
          "maximum": 0.0005317814648151398,
          "p95": 5.4667412769049406e-05,
          "p99": 0.00016458332538604736
        },
        "bias_percent": -0.03338614127705075,
        "identifier": "teaching_depth8_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9857583286789389,
        "worst_index": [
          5,
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
          "maximum": 0.0006092041730880737,
          "p95": 4.308100324124098e-05,
          "p99": 0.00012643681839108467
        },
        "bias_percent": 0.03558510745129561,
        "identifier": "teaching_depth8_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8619463985876945,
        "worst_index": [
          5,
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
            "identifier": "teaching_depth8_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0008633859688416123,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 8.006300777196884e-05,
                  "p99": 0.00026144098956137896
                },
                "candidate_energy": 9.139487969028778,
                "cvrmse_percent": 11.156932863817213,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.1338483941610037,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 9.127271263012517,
                "relative_energy_error_percent": 0.1338483941610037,
                "rms_normalized_rmse_percent": 2.426954279832736,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001724670990370214,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.0025880569592118263,
                  "rgb_channel": 0,
                  "sky_patch_index": 19
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011885203421115875,
                  "p50": 0.0,
                  "p90": 2.022937333094892e-05,
                  "p95": 0.00015494797844439745,
                  "p99": 0.00041897199116647243
                },
                "candidate_energy": 3.297401732885646,
                "cvrmse_percent": 54.3022960218867,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.19891571916341305,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.2908557035962076,
                "relative_energy_error_percent": 0.19891571916341305,
                "rms_normalized_rmse_percent": 3.1206674806799826,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0314846895635128,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.030296169221401215,
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 119.08945895265788,
            "full": 277.17029210180044
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 117.57083295378834,
            "full": 272.0327499555424
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.31266710255295,
            "full": 257.9660410992801
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.71533398516476,
            "full": 271.53899997938424
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
            "identifier": "teaching_depth8_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004207948222756386,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.672096110880375e-05,
                  "p99": 0.00016140297520905733
                },
                "candidate_energy": 9.13551839226966,
                "cvrmse_percent": 6.904710834020186,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.09186561586287204,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 9.143918509322248,
                "relative_energy_error_percent": 0.09186561586287202,
                "rms_normalized_rmse_percent": 1.5043962983711723,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.012888314668089151,
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "reference": 0.012467519845813513,
                  "rgb_channel": 0,
                  "sky_patch_index": 70
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007971003651618958,
                  "p50": 2.436585191389895e-07,
                  "p90": 3.346779703861107e-05,
                  "p95": 9.664427489042282e-05,
                  "p99": 0.0002514203661121428
                },
                "candidate_energy": 6.015929863135117,
                "cvrmse_percent": 17.924768451886855,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.07794945682414246,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.01124413098664,
                "relative_energy_error_percent": 0.07794945682414246,
                "rms_normalized_rmse_percent": 1.5764985296440546,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02767293993383646,
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "reference": 0.026875839568674564,
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.318666995503,
            "full": 2972.520292038098
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.36983399558812,
            "full": 2939.474332961254
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.18608304671943,
            "full": 2980.7562499772757
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.52245800103992,
            "full": 3016.9575000181794
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
            "identifier": "teaching_depth8_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003330595791339874,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.6922825276851654e-05,
                  "p99": 0.00016177096404135227
                },
                "candidate_energy": 9.143160612728934,
                "cvrmse_percent": 6.929427734787269,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.044498377776379924,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 9.14723098212744,
                "relative_energy_error_percent": 0.04449837777637993,
                "rms_normalized_rmse_percent": 1.5101922149699905,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0065046269446611404,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.006171567365527153,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000970594584941864,
                  "p50": 2.4044946300705305e-07,
                  "p90": 3.4322572173550965e-05,
                  "p95": 8.787494152784348e-05,
                  "p99": 0.00026693008840084076
                },
                "candidate_energy": 5.996329960873084,
                "cvrmse_percent": 18.54988345484137,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.22365363016434572,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.009771031950606,
                "relative_energy_error_percent": 0.22365363016434572,
                "rms_normalized_rmse_percent": 1.6309656980393847,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04293757490813732,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.043908169493079185,
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 167.69483289681375,
            "full": 3170.102750067599
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.93408309016377,
            "full": 3096.546291024424
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.41137507837266,
            "full": 3147.7368340129033
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 164.39933399669826,
            "full": 3154.884499963373
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
            "identifier": "teaching_depth8_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002067149616777897,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.4227792639285326e-05,
                  "p99": 9.389547631144524e-05
                },
                "candidate_energy": 9.141744203890994,
                "cvrmse_percent": 4.13981979808866,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.03938523428186646,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 9.145346119886199,
                "relative_energy_error_percent": 0.03938523428186646,
                "rms_normalized_rmse_percent": 0.9024081335642856,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.01389443501830101,
                  "global_sensor_index": 30,
                  "local_sensor_index": 30,
                  "reference": 0.01368772005662322,
                  "rgb_channel": 0,
                  "sky_patch_index": 73
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005113650113344193,
                  "p50": 1.604480690531318e-07,
                  "p90": 2.2744655871065345e-05,
                  "p95": 5.476502701640129e-05,
                  "p99": 0.00015830784104764462
                },
                "candidate_energy": 6.008285401366177,
                "cvrmse_percent": 11.224607761044975,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.06008928836157393,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.01189790803614,
                "relative_energy_error_percent": 0.06008928836157393,
                "rms_normalized_rmse_percent": 0.9876905891858453,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.036088693886995316,
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "reference": 0.036600058898329735,
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 233.5154169704765,
            "full": 5544.625916983932
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 232.51816700212657,
            "full": 5503.889042069204
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 234.18645898345858,
            "full": 5567.381916102022
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 231.71633400488645,
            "full": 5568.770457990468
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
    "/content/suite-vulkan-0.3.1/teaching_depth8/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1271.595707978122,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth8/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4599.713290925138,
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
      48,
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
        "identifier": "teaching_depth8_grid",
        "full_identifier": "teaching_depth8_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.04684312413452163,
            "cvrmse_percent": 2.8216093754602767,
            "rms_normalized_rmse_percent": 0.6149475812793934,
            "reference_energy": 9.146421276938781,
            "candidate_energy": 9.142136807466159,
            "relative_energy_error_percent": 0.04684312413452163,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.8442591428756714e-06,
              "p99": 5.6789256632328033e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.4168594680377598,
            "cvrmse_percent": 27.37218313874916,
            "rms_normalized_rmse_percent": 2.407126993342165,
            "reference_energy": 6.007215583534499,
            "candidate_energy": 5.922101780773751,
            "relative_energy_error_percent": 1.4168594680377598,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.913014149427909e-07,
              "p90": 3.844354578177448e-05,
              "p95": 5.9911515563726425e-05,
              "p99": 0.00015184725634753704,
              "maximum": 0.001961641013622284
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04772743210196495,
              "candidate": 0.04576579108834267,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5899459849572966,
            "cvrmse_percent": 10.85158051428259,
            "rms_normalized_rmse_percent": 2.407277855356534,
            "reference_energy": 15.15363686047328,
            "candidate_energy": 15.06423858823991,
            "relative_energy_error_percent": 0.5899459849572966,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.910711138312763e-07,
              "p90": 3.852658337564212e-05,
              "p95": 6.152514833956957e-05,
              "p99": 0.00014005322009325027,
              "maximum": 0.001961641013622284
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04772743210196495,
              "candidate": 0.04576579108834267,
              "position": [
                2.5,
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
      48,
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
        "identifier": "teaching_depth8_grid",
        "full_identifier": "teaching_depth8_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.04684312413452163,
            "cvrmse_percent": 2.8216093754602767,
            "rms_normalized_rmse_percent": 0.6149475812793934,
            "reference_energy": 9.146421276938781,
            "candidate_energy": 9.142136807466159,
            "relative_energy_error_percent": 0.04684312413452163,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.8442591428756714e-06,
              "p99": 5.6789256632328033e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 80.49206712911361,
            "cvrmse_percent": 419.197816826246,
            "rms_normalized_rmse_percent": 23.9932840877728,
            "reference_energy": 3.2810870167149346,
            "candidate_energy": 5.922101780773751,
            "relative_energy_error_percent": 80.49206712911361,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00026810301642399314,
              "p95": 0.00036502000875771046,
              "p99": 0.0006547318771481514,
              "maximum": 0.010745804756879807
            },
            "worst": {
              "global_sensor_index": 47,
              "local_sensor_index": 47,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.018309805542230606,
              "candidate": 0.029055610299110413,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.2168862195222,
            "cvrmse_percent": 110.66266058650078,
            "rms_normalized_rmse_percent": 23.990434007382362,
            "reference_energy": 12.427508293653716,
            "candidate_energy": 15.06423858823991,
            "relative_energy_error_percent": 21.2168862195222,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002670247369678691,
              "p95": 0.00036573479883372784,
              "p99": 0.0006395978853106499,
              "maximum": 0.010745804756879807
            },
            "worst": {
              "global_sensor_index": 47,
              "local_sensor_index": 47,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.018309805542230606,
              "candidate": 0.029055610299110413,
              "position": [
                5.5,
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
      "bias_percent": 0.09997336656519248,
      "rms_normalized_error_percent": 0.23115914872460275,
      "absolute_error": {
        "p95": 0.11401750548116779,
        "p99": 0.13545126979960823,
        "maximum": 0.14564252268811906
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 13.782212303866052,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.23115914872460275
    },
    "overcast": {
      "bias_percent": 0.05806773058846557,
      "rms_normalized_error_percent": 0.20122909751271903,
      "absolute_error": {
        "p95": 0.07887649536132811,
        "p99": 0.08756269931793213,
        "maximum": 0.09072113037109375
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.751080513000488,
      "reference_fraction_of_uniform": 0.6349546909332275,
      "rms_normalized_to_uniform_percent": 0.14054455946996566
    },
    "horizon": {
      "bias_percent": 1.0019803955426543,
      "rms_normalized_error_percent": 2.0792700775189417,
      "absolute_error": {
        "p95": 0.05717556768615005,
        "p99": 0.09708311211448227,
        "maximum": 0.09976404256424654
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3784120459428122,
      "reference_fraction_of_uniform": 0.10001384505999472,
      "rms_normalized_to_uniform_percent": 0.1268537628919197
    },
    "north": {
      "bias_percent": -67.27757045888049,
      "rms_normalized_error_percent": 105.77613149337316,
      "absolute_error": {
        "p95": 7.319482892853552e-05,
        "p99": 0.00023299637264244692,
        "maximum": 0.0003466516500338912
      },
      "worst_index": [
        45
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.9104663806501776e-05,
      "reference_fraction_of_uniform": 1.3861827028449625e-06,
      "rms_normalized_to_uniform_percent": 0.0002321262558531547
    },
    "east": {
      "bias_percent": 0.018721473193210443,
      "rms_normalized_error_percent": 0.3077323346886904,
      "absolute_error": {
        "p95": 0.03325265645980834,
        "p99": 0.050516829490661636,
        "maximum": 0.05692625045776367
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.782548189163208,
      "reference_fraction_of_uniform": 0.20189416408538818,
      "rms_normalized_to_uniform_percent": 0.07002132858709555
    },
    "south": {
      "bias_percent": 0.13691172002406463,
      "rms_normalized_error_percent": 0.26789636530499145,
      "absolute_error": {
        "p95": 0.08661725521087646,
        "p99": 0.09131220817565919,
        "maximum": 0.09177970886230469
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.585331916809082,
      "reference_fraction_of_uniform": 0.6954857110977173,
      "rms_normalized_to_uniform_percent": 0.1715126572180405
    },
    "west": {
      "bias_percent": 0.06482683582463232,
      "rms_normalized_error_percent": 0.3233117062856883,
      "absolute_error": {
        "p95": 0.035687598586082454,
        "p99": 0.04049477100372315,
        "maximum": 0.04360389709472656
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.6862499713897705,
      "reference_fraction_of_uniform": 0.1949070245027542,
      "rms_normalized_to_uniform_percent": 0.07059161674717136
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
        "identifier": "teaching_depth8_grid",
        "sensor_count": 48,
        "illuminance": {
          "nmbe_percent": -0.05351641658374814,
          "cvrmse_percent": 1.5512353480286607,
          "absolute_error_percentiles_lux": {
            "p50": 2.7088088989257812,
            "p90": 25.174615478515626,
            "p95": 38.42476806640623,
            "p99": 75.52334472656236
          },
          "maximum_absolute_error_lux": 388.8681640625,
          "worst": {
            "sensor_index": 30,
            "position": [
              3.5,
              1.5,
              0.75
            ],
            "hour_of_year": 2726.5,
            "foton_lux": 9992.302734375,
            "radiance_lux": 10381.1708984375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.38986586757990915,
            "maximum_error_percentage_points": 2.8510958904109565,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1589461405416516,
            "maximum_error_percentage_points": 0.6199400280871146,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.1320804794520547,
            "maximum_error_percentage_points": 0.5734246575342468,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.1352968036529699,
            "maximum_error_percentage_points": 0.5734246575342468,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.03632990867579904,
            "maximum_error_percentage_points": 0.3002739726027386,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 62.5,
          "radiance_percent": 62.5,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.0833333333333335,
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
            "identifier": "teaching_depth8_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_depth8_grid",
            "maximum_error_percentage_points": 0.004872110445205635,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_depth8_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_depth8_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_depth8_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
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
      "study_preparation_seconds": 0.3673999160018866,
      "weather_seconds": 0.22946505699655972,
      "metric_reduction_seconds": 0.1930570189942955,
      "write_seconds": 0.048506452003493905,
      "total_seconds": 0.471442431997275,
      "cold_end_to_end_seconds": 0.8388423479991616,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.036350110996863805,
      "engine_upload_seconds": 0.013939533,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.014592787,
      "engine_annual_reduction_seconds": 0.008064592,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.014592787
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3673999160018866,
      "weather_seconds": 0.2560853879986098,
      "metric_reduction_seconds": 0.31112154299626127,
      "write_seconds": 0.032005591005145106,
      "total_seconds": 0.5995303689996945,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.5995303689996945,
      "raw_export_seconds": 0.011948092003876809,
      "engine_upload_seconds": 0.015838945,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 8.9e-08,
      "engine_annual_reduction_seconds": 0.008918596,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013642643003549892,
      "full": 0.02545747499971185
    }
  },
  "elapsed_seconds": 3.268339187001402,
  "result_class": "passed"
}
```
