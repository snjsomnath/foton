# Foton report

Status: **passed**

```json
{
  "scene": "teaching_overhang050",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_overhang050",
    "category": "teaching",
    "question": "What does a 0.5 m overhang remove from the base room?",
    "interactions": [
      "multiple_bounces",
      "overhang",
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
    "shades": 1,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 4.499999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "adebcef3d5f4d5b5e1255df8b70d555be35566d6f749eefa504713f4697ca8d0",
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
      "scene_fingerprint": 14403547847970506616,
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 14403547847970506616,
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/12f3d0b2-7d1e-44d9-9264-d1e29a27929b/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "cb5086441c7e0fc253688640734dc38c6624544ccc07c8794637a12c71c58cea",
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
          "maximum": 0.00017850683070719242,
          "p95": 8.393544703722e-08,
          "p99": 1.2253760360181332e-05
        },
        "bias_percent": -0.007443887076704275,
        "identifier": "teaching_overhang050_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9699699184146368,
        "worst_index": [
          17,
          454,
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
          "maximum": 0.0005898512899875641,
          "p95": 3.327452577650547e-05,
          "p99": 0.00011610088404268026
        },
        "bias_percent": -0.006044899545977756,
        "identifier": "teaching_overhang050_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3107509634131045,
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
          "maximum": 0.0004492923617362976,
          "p95": 2.7412082999944687e-05,
          "p99": 9.379500988870859e-05
        },
        "bias_percent": 0.009602841242917423,
        "identifier": "teaching_overhang050_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0726328916887473,
        "worst_index": [
          10,
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
            "identifier": "teaching_overhang050_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006125950312707573,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.608905874192715e-05,
                  "p99": 0.0001874992740340531
                },
                "candidate_energy": 6.670849885797907,
                "cvrmse_percent": 32.06265543268341,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.021572595721910403,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.669411120699806,
                "relative_energy_error_percent": 0.0215725957219104,
                "rms_normalized_rmse_percent": 6.857995831256872,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0013185254647396505,
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "reference": 0.0007059304334688932,
                  "rgb_channel": 0,
                  "sky_patch_index": 93
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0018800590187311172,
                  "p50": 0.0,
                  "p90": 5.79337856834174e-06,
                  "p95": 9.024247992783785e-05,
                  "p99": 0.0003180405983584933
                },
                "candidate_energy": 3.34613994630962,
                "cvrmse_percent": 113.86455576147685,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.16088173615056087,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.3407652651503312,
                "relative_energy_error_percent": 0.16088173615056087,
                "rms_normalized_rmse_percent": 4.615882600269748,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.037394680082798004,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.03927473910152912,
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 122.46341700665653,
            "full": 248.35595802869648
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 115.54649996105582,
            "full": 244.5228750584647
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 117.02033295296133,
            "full": 244.04150003101677
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.74358297791332,
            "full": 240.54095894098282
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
            "identifier": "teaching_overhang050_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005165874608792365,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.1108462028205395e-05,
                  "p99": 0.00015347707085311413
                },
                "candidate_energy": 6.665122717094164,
                "cvrmse_percent": 26.702901544880923,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.09518301741074531,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.671472826235913,
                "relative_energy_error_percent": 0.09518301741074532,
                "rms_normalized_rmse_percent": 5.716167230196359,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0008682335028424859,
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "reference": 0.0013848209637217224,
                  "rgb_channel": 0,
                  "sky_patch_index": 90
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006943735061213374,
                  "p50": 0.0,
                  "p90": 1.6109794796648286e-05,
                  "p95": 5.910199251957238e-05,
                  "p99": 0.00022979630739428103
                },
                "candidate_energy": 5.619932353268215,
                "cvrmse_percent": 47.21358161698992,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.14897907972828908,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.611572284520449,
                "relative_energy_error_percent": 0.14897907972828905,
                "rms_normalized_rmse_percent": 2.450407239469578,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0005099630216136575,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": -0.00018441048450767994,
                  "rgb_channel": 0,
                  "sky_patch_index": 90
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.81804191786796,
            "full": 2287.0843750424683
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.96870802901685,
            "full": 2257.445332943462
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.96820893045515,
            "full": 2313.0851249443367
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 164.44083396345377,
            "full": 2258.589292061515
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
            "identifier": "teaching_overhang050_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004307443741708994,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.350870585767552e-05,
                  "p99": 0.00013734656386077404
                },
                "candidate_energy": 6.671702339148396,
                "cvrmse_percent": 23.433360420927745,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.016915334091796273,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.67057398927227,
                "relative_energy_error_percent": 0.016915334091796273,
                "rms_normalized_rmse_percent": 5.01779487391923,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003342422074638307,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.0037731664488092065,
                  "rgb_channel": 0,
                  "sky_patch_index": 318
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001038750633597374,
                  "p50": 0.0,
                  "p90": 1.588220438861754e-05,
                  "p95": 6.07239780947566e-05,
                  "p99": 0.00021181406918913126
                },
                "candidate_energy": 5.615491724190974,
                "cvrmse_percent": 46.135818823074494,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1184688526294543,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.608846987519119,
                "relative_energy_error_percent": 0.1184688526294543,
                "rms_normalized_rmse_percent": 2.3923868500397023,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.049179330468177795,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.04814057983458042,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.96808296442032,
            "full": 2419.7845419403166
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.91729199048132,
            "full": 2356.7717500263825
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.4644169518724,
            "full": 2426.9726669881493
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.34104204177856,
            "full": 2406.7362090572715
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
            "identifier": "teaching_overhang050_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002324667584616691,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3054657503962517e-05,
                  "p99": 8.214905392378569e-05
                },
                "candidate_energy": 6.671459683630019,
                "cvrmse_percent": 14.199519555036572,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.04995082114272979,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.674793797941675,
                "relative_energy_error_percent": 0.04995082114272979,
                "rms_normalized_rmse_percent": 3.0420384748065867,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.000801766145741567,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.001034232904203236,
                  "rgb_channel": 0,
                  "sky_patch_index": 210
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000646321102976799,
                  "p50": 0.0,
                  "p90": 1.0801268763316416e-05,
                  "p95": 3.570890112314373e-05,
                  "p99": 0.0001284503232454881
                },
                "candidate_energy": 5.613220585806822,
                "cvrmse_percent": 27.921407655750365,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.06632448385461667,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.6095001138095135,
                "relative_energy_error_percent": 0.06632448385461667,
                "rms_normalized_rmse_percent": 1.449738676532438,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04006914608180523,
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "reference": 0.03942282497882843,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 209.09250003751367,
            "full": 4253.204790991731
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 214.13229196332395,
            "full": 4287.584333913401
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 213.25850009452552,
            "full": 4259.0603329008445
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 216.3896249840036,
            "full": 4254.242000053637
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
    "/Users/ssanjay/GitHub/foton-0.3.3/validation/results/2026-11-04-architectural-v4-metal-0.3.3-release/teaching_overhang050/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2681.340332957916,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang050/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10481.660749996081,
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
        "identifier": "teaching_overhang050_grid",
        "full_identifier": "teaching_overhang050_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.013053845176376111,
            "cvrmse_percent": 2.481913875070816,
            "rms_normalized_rmse_percent": 0.5318368866319579,
            "reference_energy": 6.671203007665099,
            "candidate_energy": 6.672073856177121,
            "relative_energy_error_percent": 0.013053845176376111,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 6.309710443019867e-08,
              "p99": 9.739771485328674e-06,
              "maximum": 0.00012166961096227169
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 454,
              "rgb_channel": 0,
              "reference": 0.0028337687253952026,
              "candidate": 0.002712099114432931,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.046210746487288,
            "cvrmse_percent": 40.78288356654696,
            "rms_normalized_rmse_percent": 2.1178969104042125,
            "reference_energy": 5.613284060209921,
            "candidate_energy": 5.554557279141147,
            "relative_energy_error_percent": 1.046210746487288,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.0854628089873605e-05,
              "p95": 1.9630882889032364e-05,
              "p99": 5.2667448471765965e-05,
              "maximum": 0.001541774719953537
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04491521418094635,
              "candidate": 0.04337343946099281,
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
            "nmbe_percent": -0.4709674261292521,
            "cvrmse_percent": 18.607437869720968,
            "rms_normalized_rmse_percent": 2.114722919007349,
            "reference_energy": 12.28448706787502,
            "candidate_energy": 12.22663113531827,
            "relative_energy_error_percent": 0.47096742612923764,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.079477688108457e-05,
              "p95": 1.9622966647148132e-05,
              "p99": 5.1690818509086967e-05,
              "maximum": 0.001541774719953537
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04491521418094635,
              "candidate": 0.04337343946099281,
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
      36,
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
        "identifier": "teaching_overhang050_grid",
        "full_identifier": "teaching_overhang050_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.013053845176376111,
            "cvrmse_percent": 2.481913875070816,
            "rms_normalized_rmse_percent": 0.5318368866319579,
            "reference_energy": 6.671203007665099,
            "candidate_energy": 6.672073856177121,
            "relative_energy_error_percent": 0.013053845176376111,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 6.309710443019867e-08,
              "p99": 9.739771485328674e-06,
              "maximum": 0.00012166961096227169
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 454,
              "rgb_channel": 0,
              "reference": 0.0028337687253952026,
              "candidate": 0.002712099114432931,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 66.1856836516116,
            "cvrmse_percent": 808.2176290928104,
            "rms_normalized_rmse_percent": 32.762169808229054,
            "reference_energy": 3.3423801359361445,
            "candidate_energy": 5.554557279141147,
            "relative_energy_error_percent": 66.1856836516116,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.765537095816405e-05,
              "p95": 9.644000238040462e-05,
              "p99": 0.00020226649940013885,
              "maximum": 0.012165181338787079
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.020108778029680252,
              "candidate": 0.03227395936846733,
              "position": [
                0.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 22.100460544247635,
            "cvrmse_percent": 269.77248619920766,
            "rms_normalized_rmse_percent": 32.76239625483259,
            "reference_energy": 10.013583143601243,
            "candidate_energy": 12.22663113531827,
            "relative_energy_error_percent": 22.10046054424765,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.770191539544612e-05,
              "p95": 9.666522964835167e-05,
              "p99": 0.00020216801203787327,
              "maximum": 0.012165181338787079
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.020108778029680252,
              "candidate": 0.03227395936846733,
              "position": [
                0.5,
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
      "bias_percent": 0.20116185385031907,
      "rms_normalized_error_percent": 0.22540395277096015,
      "absolute_error": {
        "p95": 0.10251346025191954,
        "p99": 0.13078288772591085,
        "maximum": 0.1391074020279346
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 13.487250695558442,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.22540395277096015
    },
    "overcast": {
      "bias_percent": 0.1540216343651505,
      "rms_normalized_error_percent": 0.15207572078694706,
      "absolute_error": {
        "p95": 0.0355089008808136,
        "p99": 0.049346834421157816,
        "maximum": 0.05440974235534668
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.046287536621094,
      "reference_fraction_of_uniform": 0.5965847373008728,
      "rms_normalized_to_uniform_percent": 0.09948236071880287
    },
    "horizon": {
      "bias_percent": 0.9166969038359136,
      "rms_normalized_error_percent": 1.998979155047518,
      "absolute_error": {
        "p95": 0.10544031219748806,
        "p99": 0.12425091031031642,
        "maximum": 0.12685514768863015
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.096498906925109,
      "reference_fraction_of_uniform": 0.1554430146104957,
      "rms_normalized_to_uniform_percent": 0.20310395497753025
    },
    "north": {
      "bias_percent": -90.5966204146588,
      "rms_normalized_error_percent": 99.62218721701215,
      "absolute_error": {
        "p95": 4.180675636789033e-05,
        "p99": 0.00012321990873545002,
        "maximum": 0.00016233603201953883
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.215917473018635e-05,
      "reference_fraction_of_uniform": 9.015310524773668e-07,
      "rms_normalized_to_uniform_percent": 0.00014505235790840927
    },
    "east": {
      "bias_percent": 0.08857365637011587,
      "rms_normalized_error_percent": 0.25612316159630083,
      "absolute_error": {
        "p95": 0.024850577116012573,
        "p99": 0.0356600522994995,
        "maximum": 0.03838157653808594
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.598822832107544,
      "reference_fraction_of_uniform": 0.19268737733364105,
      "rms_normalized_to_uniform_percent": 0.0562332071993321
    },
    "south": {
      "bias_percent": 0.2401345517024984,
      "rms_normalized_error_percent": 0.29531606152426587,
      "absolute_error": {
        "p95": 0.10131311416625977,
        "p99": 0.12973437309265134,
        "maximum": 0.13832902908325195
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.035910606384277,
      "reference_fraction_of_uniform": 0.7441035509109497,
      "rms_normalized_to_uniform_percent": 0.20677700398181456
    },
    "west": {
      "bias_percent": 0.12568964364586266,
      "rms_normalized_error_percent": 0.2531111311601164,
      "absolute_error": {
        "p95": 0.023010313510894775,
        "p99": 0.033007168769836406,
        "maximum": 0.03727579116821289
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.633699893951416,
      "reference_fraction_of_uniform": 0.195273295044899,
      "rms_normalized_to_uniform_percent": 0.05601614578168132
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
        "identifier": "teaching_overhang050_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.04328917851359377,
          "cvrmse_percent": 1.6657367181856095,
          "absolute_error_percentiles_lux": {
            "p50": 2.2937469482421875,
            "p90": 24.474700927734382,
            "p95": 39.101095581054636,
            "p99": 88.25258605956957
          },
          "maximum_absolute_error_lux": 343.40625,
          "worst": {
            "sensor_index": 21,
            "position": [
              3.5,
              2.5,
              0.75
            ],
            "hour_of_year": 1356.5,
            "foton_lux": 16659.990234375,
            "radiance_lux": 16316.583984375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2703234398782336,
            "maximum_error_percentage_points": 1.2024657534246543,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.09057427597992332,
            "maximum_error_percentage_points": 0.43518179425377923,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.06504566210045651,
            "maximum_error_percentage_points": 0.46808219178081956,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.08056697108067093,
            "maximum_error_percentage_points": 0.4369863013698563,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.04398021308980215,
            "maximum_error_percentage_points": 0.16643835616438452,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 91.66666666666667,
          "radiance_percent": 86.11111111111111,
          "difference_percentage_points": 5.555555555555557,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 2,
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
            "identifier": "teaching_overhang050_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_overhang050_grid",
            "maximum_error_percentage_points": 0.004894584760265275,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_overhang050_grid",
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_overhang050_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_overhang050_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
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
      "study_preparation_seconds": 0.006069332943297923,
      "weather_seconds": 0.08233054203446954,
      "metric_reduction_seconds": 0.10894933401141316,
      "write_seconds": 0.010648625087924302,
      "total_seconds": 0.20205487497150898,
      "cold_end_to_end_seconds": 0.2081242079148069,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.001592333079315722,
      "engine_upload_seconds": 0.000728917,
      "engine_acceleration_structure_seconds": 0.002834083,
      "engine_tracing_seconds": 0.051219791639596224,
      "engine_annual_reduction_seconds": 0.00180116668343544,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.051219791639596224
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006069332943297923,
      "weather_seconds": 0.08033645793329924,
      "metric_reduction_seconds": 0.04619974992237985,
      "write_seconds": 0.009983542026020586,
      "total_seconds": 0.13662437500897795,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.13662437500897795,
      "raw_export_seconds": 0.0018737079808488488,
      "engine_upload_seconds": 5.4709e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0015777916414663196,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.020824374980293214,
      "full": 0.06232062494382262
    }
  },
  "elapsed_seconds": 1.2768566249869764,
  "result_class": "passed"
}
```
