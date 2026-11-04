# Foton report

Status: **passed**

```json
{
  "scene": "teaching_depth6",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_depth6",
    "category": "teaching",
    "question": "What is the 6 m deep teaching base room?",
    "interactions": [
      "multiple_bounces",
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
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 4.499999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "8019fb02918a395fd77f9aa888902917a5002c94993ef7a94d70707429c47dc3",
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
      "scene_fingerprint": 13295819725958684955,
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 13295819725958684955,
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
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "45487966d5ee6917d66289c4eb2bd7eb44bdf4c344478a51ff285fe2179aafd5",
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
          "maximum": 0.00029224716126918793,
          "p95": 1.1893303599208524e-05,
          "p99": 0.00012718886137008667
        },
        "bias_percent": -0.060910624560303654,
        "identifier": "teaching_depth6_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9651389221795657,
        "worst_index": [
          17,
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
          "maximum": 0.0005071628838777542,
          "p95": 7.185545691754668e-05,
          "p99": 0.00016926322132349014
        },
        "bias_percent": 0.10774159687806287,
        "identifier": "teaching_depth6_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9936433118356247,
        "worst_index": [
          12,
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
          "maximum": 0.0007013678550720215,
          "p95": 5.512269563041597e-05,
          "p99": 0.00015357788652181625
        },
        "bias_percent": -0.02945788236549324,
        "identifier": "teaching_depth6_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8634278387289157,
        "worst_index": [
          11,
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
            "identifier": "teaching_depth6_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006137789459899068,
                  "p50": 0.0,
                  "p90": 4.7497451305389404e-07,
                  "p95": 0.0001320349983870983,
                  "p99": 0.00031365850009024143
                },
                "candidate_energy": 8.951205340956221,
                "cvrmse_percent": 10.69738445858502,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.049469817338681124,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.946779385536502,
                "relative_energy_error_percent": 0.049469817338681124,
                "rms_normalized_rmse_percent": 2.6394329803374443,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002127552987076342,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.002741331933066249,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013389098457992077,
                  "p50": 0.0,
                  "p90": 5.422955291578546e-05,
                  "p95": 0.00023439667420461748,
                  "p99": 0.0005557615077123046
                },
                "candidate_energy": 3.123825450901478,
                "cvrmse_percent": 57.04513378342477,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.5596060988574041,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.106441614171132,
                "relative_energy_error_percent": 0.5596060988574042,
                "rms_normalized_rmse_percent": 3.547771258525361,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0003574248403310776,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.0009814850054681301,
                  "rgb_channel": 0,
                  "sky_patch_index": 75
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.66658299509436,
            "full": 232.5897499686107
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.5097079416737,
            "full": 224.1251670056954
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 122.28424998465925,
            "full": 238.14095801208168
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 112.60266706813127,
            "full": 251.28441595006734
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
            "identifier": "teaching_depth6_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000441601499915123,
                  "p50": 0.0,
                  "p90": 2.2673048079013824e-06,
                  "p95": 7.953586173243774e-05,
                  "p99": 0.00022361031733453274
                },
                "candidate_energy": 8.944526115647022,
                "cvrmse_percent": 7.371480852394301,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.046301535898740254,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.948669487062034,
                "relative_energy_error_percent": 0.046301535898740254,
                "rms_normalized_rmse_percent": 1.8189839059283046,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00786795187741518,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.007426350377500057,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009105689823627472,
                  "p50": 2.515128478819406e-07,
                  "p90": 4.514585452852771e-05,
                  "p95": 0.00012967926450073696,
                  "p99": 0.0003490790259093046
                },
                "candidate_energy": 5.6369192477241725,
                "cvrmse_percent": 18.862570258573346,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.15179504627772675,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.628375652298082,
                "relative_energy_error_percent": 0.15179504627772675,
                "rms_normalized_rmse_percent": 1.756049530319994,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.031861549243330956,
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "reference": 0.03095098026096821,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.02133299782872,
            "full": 2287.2082920512185
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.00400000158697,
            "full": 2222.912042052485
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.36716603208333,
            "full": 2253.3140829764307
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.14554194081575,
            "full": 2234.3273339793086
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
            "identifier": "teaching_depth6_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003939908929169178,
                  "p50": 0.0,
                  "p90": 4.4249463826417923e-07,
                  "p95": 8.700451580807566e-05,
                  "p99": 0.00020029651932418346
                },
                "candidate_energy": 8.94948533459501,
                "cvrmse_percent": 6.733028153376326,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.016789528234732672,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.94798301046103,
                "relative_energy_error_percent": 0.016789528234732672,
                "rms_normalized_rmse_percent": 1.661722691993759,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007334491470828652,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.00772848236374557,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009082648903131485,
                  "p50": 2.9503512877226967e-07,
                  "p90": 4.3277163058519363e-05,
                  "p95": 0.00012898443383164694,
                  "p99": 0.00031497469171881676
                },
                "candidate_energy": 5.652324953166701,
                "cvrmse_percent": 18.07909915993406,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.21652040309170625,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.640112957855525,
                "relative_energy_error_percent": 0.21652040309170623,
                "rms_normalized_rmse_percent": 1.6859040440506652,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04671707563102245,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.045808810740709305,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.98883303813636,
            "full": 2415.790500002913
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.81300001312047,
            "full": 2372.2569999517873
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.56583393923938,
            "full": 2406.280208961107
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.3067080155015,
            "full": 2339.7557080024853
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
            "identifier": "teaching_depth6_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002204264746978879,
                  "p50": 0.0,
                  "p90": 3.3748801797628403e-07,
                  "p95": 4.089623398613168e-05,
                  "p99": 0.00010505341924726963
                },
                "candidate_energy": 8.951278551087853,
                "cvrmse_percent": 3.417435780954114,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.03660889596674131,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.948002786056804,
                "relative_energy_error_percent": 0.036608895966741314,
                "rms_normalized_rmse_percent": 0.8435596397217046,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003466974012553692,
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "reference": 0.0036874004872515798,
                  "rgb_channel": 0,
                  "sky_patch_index": 45
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005607102066278458,
                  "p50": 2.374843788288672e-07,
                  "p90": 2.9030648875050247e-05,
                  "p95": 7.359200390055688e-05,
                  "p99": 0.0001836055889725685
                },
                "candidate_energy": 5.640107080707423,
                "cvrmse_percent": 10.905959404284788,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.032115601274259435,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.641919016923115,
                "relative_energy_error_percent": 0.032115601274259435,
                "rms_normalized_rmse_percent": 1.0162637383041422,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.043052734807133675,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.04249202460050583,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 204.01774998754263,
            "full": 4180.731583968736
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 208.05741695221514,
            "full": 4206.669416977093
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 216.94887499324977,
            "full": 4179.240499972366
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 200.67470788490027,
            "full": 4160.74641700834
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
    "/content/suite-vulkan-0.3.3/teaching_depth6/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 781.61583293695,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_depth6/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2911.998916999437,
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
        "identifier": "teaching_depth6_grid",
        "full_identifier": "teaching_depth6_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.057234207925190565,
            "cvrmse_percent": 2.4774773209699803,
            "rms_normalized_rmse_percent": 0.6117134404603434,
            "reference_energy": 8.95339652423354,
            "candidate_energy": 8.948272118650493,
            "relative_energy_error_percent": 0.057234207925190565,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2898817658424377e-07,
              "p95": 6.249168654903633e-06,
              "p99": 6.368057802319527e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
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
            "nmbe_percent": -0.9741487997668916,
            "cvrmse_percent": 22.635646349554353,
            "rms_normalized_rmse_percent": 2.108023743749927,
            "reference_energy": 5.63725720041861,
            "candidate_energy": 5.582341927060959,
            "relative_energy_error_percent": 0.9741487997668916,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 8.31612396723358e-07,
              "p90": 4.4787630031351e-05,
              "p95": 6.665831606369461e-05,
              "p99": 0.0001667328178882599,
              "maximum": 0.0018232092261314392
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04604068025946617,
              "candidate": 0.04421747103333473,
              "position": [
                3.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.41149409802834963,
            "cvrmse_percent": 8.7312532442347,
            "rms_normalized_rmse_percent": 2.10458312404893,
            "reference_energy": 14.59065372465215,
            "candidate_energy": 14.530614045711452,
            "relative_energy_error_percent": 0.4114940980283497,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 8.238484383582545e-07,
              "p90": 4.500563954934478e-05,
              "p95": 6.724883569404479e-05,
              "p99": 0.00015328312292695045,
              "maximum": 0.0018232092261314392
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04604068025946617,
              "candidate": 0.04421747103333473,
              "position": [
                3.5,
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
        "identifier": "teaching_depth6_grid",
        "full_identifier": "teaching_depth6_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.057234207925190565,
            "cvrmse_percent": 2.4774773209699803,
            "rms_normalized_rmse_percent": 0.6117134404603434,
            "reference_energy": 8.95339652423354,
            "candidate_energy": 8.948272118650493,
            "relative_energy_error_percent": 0.057234207925190565,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2898817658424377e-07,
              "p95": 6.249168654903633e-06,
              "p99": 6.368057802319527e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
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
            "nmbe_percent": 79.45443861774302,
            "cvrmse_percent": 426.3736667036872,
            "rms_normalized_rmse_percent": 26.522604572623287,
            "reference_energy": 3.110729369559891,
            "candidate_energy": 5.582341927060959,
            "relative_energy_error_percent": 79.45443861774301,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0003151900018565357,
              "p95": 0.00041337311849929347,
              "p99": 0.0007296788971871138,
              "maximum": 0.0118144191801548
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.023800920695066452,
              "candidate": 0.03561533987522125,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.444814432738493,
            "cvrmse_percent": 109.92296034988266,
            "rms_normalized_rmse_percent": 26.5184321080342,
            "reference_energy": 12.064125893793431,
            "candidate_energy": 14.530614045711452,
            "relative_energy_error_percent": 20.444814432738493,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0003166199894621968,
              "p95": 0.00041436253668507555,
              "p99": 0.0007299510762095451,
              "maximum": 0.0118144191801548
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.023800920695066452,
              "candidate": 0.03561533987522125,
              "position": [
                5.5,
                2.5,
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
      "bias_percent": 0.09470099559931627,
      "rms_normalized_error_percent": 0.2435336539503446,
      "absolute_error": {
        "p95": 0.13785387114223302,
        "p99": 0.15041695821782167,
        "maximum": 0.15529551008648745
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 17.86502188766986,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2435336539503446
    },
    "overcast": {
      "bias_percent": 0.06588694400480832,
      "rms_normalized_error_percent": 0.1974149127448928,
      "absolute_error": {
        "p95": 0.07062709331512451,
        "p99": 0.09620647430419918,
        "maximum": 0.10643768310546875
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 11.413580894470215,
      "reference_fraction_of_uniform": 0.638878583908081,
      "rms_normalized_to_uniform_percent": 0.13768664138091385
    },
    "horizon": {
      "bias_percent": 0.9550487844608022,
      "rms_normalized_error_percent": 2.5196260948701443,
      "absolute_error": {
        "p95": 0.100067131631083,
        "p99": 0.1322363301052149,
        "maximum": 0.1404582697105976
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.6677532088849756,
      "reference_fraction_of_uniform": 0.09335298995832918,
      "rms_normalized_to_uniform_percent": 0.15586784111739582
    },
    "north": {
      "bias_percent": -11.475152169341667,
      "rms_normalized_error_percent": 126.46387558507476,
      "absolute_error": {
        "p95": 6.320700401829527e-05,
        "p99": 0.00010540850355482686,
        "maximum": 0.00011420727059885394
      },
      "worst_index": [
        20
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.7719548850436695e-05,
      "reference_fraction_of_uniform": 9.918570640365942e-07,
      "rms_normalized_to_uniform_percent": 0.00011711744322283941
    },
    "east": {
      "bias_percent": -0.02131036414079078,
      "rms_normalized_error_percent": 0.28497588741887914,
      "absolute_error": {
        "p95": 0.028119266033172607,
        "p99": 0.046867084503173784,
        "maximum": 0.05684661865234375
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.6279077529907227,
      "reference_fraction_of_uniform": 0.20307321846485138,
      "rms_normalized_to_uniform_percent": 0.06485298956831584
    },
    "south": {
      "bias_percent": 0.14259728547991996,
      "rms_normalized_error_percent": 0.3188706523939541,
      "absolute_error": {
        "p95": 0.12303531169891357,
        "p99": 0.13226246833801267,
        "maximum": 0.13596248626708984
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 12.342010498046875,
      "reference_fraction_of_uniform": 0.6908477544784546,
      "rms_normalized_to_uniform_percent": 0.20449247605579712
    },
    "west": {
      "bias_percent": -0.0179534058221253,
      "rms_normalized_error_percent": 0.27540715885911804,
      "absolute_error": {
        "p95": 0.03333938121795654,
        "p99": 0.039348858594894405,
        "maximum": 0.040046095848083496
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.5070245265960693,
      "reference_fraction_of_uniform": 0.1963067501783371,
      "rms_normalized_to_uniform_percent": 0.06007347456334843
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
        "identifier": "teaching_depth6_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.012423481685107455,
          "cvrmse_percent": 1.3420937640568982,
          "absolute_error_percentiles_lux": {
            "p50": 3.1900482177734375,
            "p90": 29.739105224609375,
            "p95": 44.53720703124998,
            "p99": 85.09574096679677
          },
          "maximum_absolute_error_lux": 338.6171875,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 5829.03662109375,
            "radiance_lux": 6167.65380859375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.25547184170471876,
            "maximum_error_percentage_points": 1.7304109589041161,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.0975063340915408,
            "maximum_error_percentage_points": 0.6156071989286005,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.07425418569254176,
            "maximum_error_percentage_points": 0.4145205479452052,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.09146118721461288,
            "maximum_error_percentage_points": 0.38123287671231765,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.058066971080669855,
            "maximum_error_percentage_points": 0.16547945205479486,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
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
      "maximum_error_percentage_points": 0.004977525684935813,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_depth6_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_depth6_grid",
            "maximum_error_percentage_points": 0.004977525684935813,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_depth6_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_depth6_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_depth6_grid",
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
      "study_preparation_seconds": 0.3741241159998481,
      "weather_seconds": 0.22718011500001012,
      "metric_reduction_seconds": 0.14672343300003376,
      "write_seconds": 0.011203236000028483,
      "total_seconds": 0.3854301280000527,
      "cold_end_to_end_seconds": 0.7595542439999008,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0014105819998349034,
      "engine_upload_seconds": 0.013592878,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.009887508,
      "engine_annual_reduction_seconds": 0.00796534,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.009887508
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3741241159998481,
      "weather_seconds": 0.22430494200011708,
      "metric_reduction_seconds": 0.13701555199986615,
      "write_seconds": 0.011827342000060526,
      "total_seconds": 0.3734064360000957,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.3734064360000957,
      "raw_export_seconds": 0.0014983749999828433,
      "engine_upload_seconds": 0.013436266,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 1.24e-07,
      "engine_annual_reduction_seconds": 0.008223519,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.014443777999986196,
      "full": 0.02080332399987128
    }
  },
  "elapsed_seconds": 2.6908801889999268,
  "result_class": "passed"
}
```
