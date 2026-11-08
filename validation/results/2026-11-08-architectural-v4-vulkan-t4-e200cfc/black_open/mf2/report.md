# Foton report

Status: **passed**

```json
{
  "scene": "black_open",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "black_open",
    "category": "controls",
    "question": "Is direct sky integration correct without glazing or reflections?",
    "interactions": [
      "open_aperture",
      "direct_sky"
    ],
    "room_count": 1,
    "include_glazing": false,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "4446b114543b821d9b3791e8414b96916357b212dbdec3ac8cff9cb9645ddb8e",
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
      "solver_version": "0.3.5",
      "scene_fingerprint": 17021673487271919861,
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
      "solver_version": "0.3.5",
      "scene_fingerprint": 17021673487271919861,
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
      "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/rcalc",
      "-e",
      "MF:2",
      "-f",
      "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/lib/reinhart.cal",
      "-e",
      "Dx=$1;Dy=$2;Dz=$3;$1=rbin"
    ],
    "calibration_sha256": "92b8c09984de7a551773530b3146ba79a51e1b003245f230b6e7b430eb6c26cd"
  },
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.5)",
      "weather_id": "82c544d76aea9710a570440071d4833104fdc7da7504bac286ac2afe42bdd614"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/gendaymtx",
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
    "model_sha256": "22ef95e4598ad81e217be9f93f838977f1b277a150a1fde1ced5629a765d95dd",
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
          "maximum": 0.00036029936745762825,
          "p95": 3.073364496231079e-08,
          "p99": 1.3703247532248497e-05
        },
        "bias_percent": -0.03088083916421781,
        "identifier": "black_open_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9025371677533087,
        "worst_index": [
          17,
          540,
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
          "maximum": 0.0005497788079082966,
          "p95": 3.926968201994896e-05,
          "p99": 0.0002159841824322939
        },
        "bias_percent": 0.0921149870458587,
        "identifier": "black_open_grid",
        "passed": true,
        "rms_normalized_error_percent": 3.853268272240929,
        "worst_index": [
          11,
          304,
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
          "maximum": 0.0006356062367558479,
          "p95": 2.841581590473652e-05,
          "p99": 0.00017734733410179615
        },
        "bias_percent": -0.07600316785434115,
        "identifier": "black_open_grid",
        "passed": true,
        "rms_normalized_error_percent": 3.2969246033121773,
        "worst_index": [
          11,
          304,
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
            "identifier": "black_open_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0011851487215608358,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 7.9009507317096e-05,
                  "p99": 0.00031603965908288956
                },
                "candidate_energy": 11.398762404605804,
                "cvrmse_percent": 31.14286379114621,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.06242211016429844,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.391651495359838,
                "relative_energy_error_percent": 0.06242211016429843,
                "rms_normalized_rmse_percent": 5.9169159896984285,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003950496204197407,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.002765347482636571,
                  "rgb_channel": 0,
                  "sky_patch_index": 157
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008691099938005209,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 7.9009507317096e-05,
                  "p99": 0.00031603965908288956
                },
                "candidate_energy": -0.0007110967198968865,
                "cvrmse_percent": 39899.676834899234,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": true,
                "nmbe_percent": -108.10818621230209,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.008770108397584409,
                "relative_energy_error_percent": 108.10818621230209,
                "rms_normalized_rmse_percent": 5.826558629936156,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0006320800166577101,
                  "global_sensor_index": 35,
                  "local_sensor_index": 35,
                  "reference": 0.00023702997714281082,
                  "rgb_channel": 0,
                  "sky_patch_index": 371
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.51279108505696,
            "full": 103.69312495458871
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.77804211527109,
            "full": 117.16687493026257
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 111.1600409494713,
            "full": 103.67375006899238
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 105.44558300171047,
            "full": 110.04079203121364
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
            "identifier": "black_open_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00047123897820711136,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.9269889384740964e-05,
                  "p99": 0.0001570798922330141
                },
                "candidate_energy": 11.377238219127321,
                "cvrmse_percent": 16.351511782587878,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.07139825959672483,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.385367173137638,
                "relative_energy_error_percent": 0.07139825959672483,
                "rms_normalized_rmse_percent": 3.1084999476884816,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003691371064633131,
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "reference": 0.004162610042840242,
                  "rgb_channel": 0,
                  "sky_patch_index": 205
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007068581180647016,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.926997305825353e-05,
                  "p99": 0.0002748894039541483
                },
                "candidate_energy": 0.010485105267434847,
                "cvrmse_percent": 40266.18183622211,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": true,
                "nmbe_percent": -236.922205994043,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": -0.007657709858904127,
                "relative_energy_error_percent": 236.92220599404297,
                "rms_normalized_rmse_percent": 5.147797005617404,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0003534290590323508,
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "reference": -0.0003534290590323508,
                  "rgb_channel": 0,
                  "sky_patch_index": 78
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.16787500400096,
            "full": 148.01541704218835
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.0652919653803,
            "full": 138.77058401703835
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.62499994784594,
            "full": 139.96629102621228
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.22958394140005,
            "full": 147.75241701863706
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
            "identifier": "black_open_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005105091258883476,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.9269889384740964e-05,
                  "p99": 0.00015707965940237045
                },
                "candidate_energy": 11.394674130449857,
                "cvrmse_percent": 16.541023437357683,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.02894079989163041,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.397972794948146,
                "relative_energy_error_percent": 0.028940799891630415,
                "rms_normalized_rmse_percent": 3.14808674532187,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007107852958142757,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.007618362084031105,
                  "rgb_channel": 0,
                  "sky_patch_index": 370
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005105084273964167,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.9269900298677385e-05,
                  "p99": 0.00015707965940237045
                },
                "candidate_energy": -0.004948002679157071,
                "cvrmse_percent": 149742.662422176,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": true,
                "nmbe_percent": 281.8185992367225,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": -0.001295904046855867,
                "relative_energy_error_percent": 281.8185992367225,
                "rms_normalized_rmse_percent": 3.2405003885412236,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0005105084273964167,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.0,
                  "rgb_channel": 0,
                  "sky_patch_index": 318
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.29320901539177,
            "full": 140.14266699086875
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.9559160238132,
            "full": 147.06574997399002
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.9350419845432,
            "full": 140.68816707003862
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.83437497820705,
            "full": 135.2263749577105
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
            "identifier": "black_open_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00021574448328465223,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.961301313713193e-05,
                  "p99": 9.806553134694695e-05
                },
                "candidate_energy": 11.38307140345205,
                "cvrmse_percent": 9.603765407760841,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.028421286248145706,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.386307538510664,
                "relative_energy_error_percent": 0.028421286248145702,
                "rms_normalized_rmse_percent": 1.8267879539736849,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0021182189229875803,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.001902474439702928,
                  "rgb_channel": 0,
                  "sky_patch_index": 101
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00027458398835733533,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.9612954929471016e-05,
                  "p99": 9.806593880057335e-05
                },
                "candidate_energy": -0.0002941646489489358,
                "cvrmse_percent": 355897473466.7486,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": true,
                "nmbe_percent": -89843836.66666667,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.2741809263825417e-10,
                "relative_energy_error_percent": 89843836.66666667,
                "rms_normalized_rmse_percent": 1.9466906023055768,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00027458398835733533,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.0,
                  "rgb_channel": 0,
                  "sky_patch_index": 151
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 191.48591707926244,
            "full": 188.93083301372826
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 209.97016702312976,
            "full": 198.72658397071064
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.83616700582206,
            "full": 188.98533307947218
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 197.3419999703765,
            "full": 198.39116698130965
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
    "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/oconv",
    "/content/suite-vulkan/black_open/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2861.8098340230063,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/black_open/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 11857.336750021204,
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
        "identifier": "black_open_grid",
        "full_identifier": "black_open_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.028383681892268284,
            "cvrmse_percent": 2.5976170414651207,
            "rms_normalized_rmse_percent": 0.4940581407328946,
            "reference_energy": 11.387923528768624,
            "candidate_energy": 11.384691216780084,
            "relative_energy_error_percent": 0.028383681892268284,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.958120942115784e-09,
              "p99": 1.1761672794818878e-05,
              "maximum": 0.00012795720249414444
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 514,
              "rgb_channel": 0,
              "reference": 0.005723865702748299,
              "candidate": 0.005851822905242443,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -100.0,
            "cvrmse_percent": 28674.460575016044,
            "rms_normalized_rmse_percent": 1.6197586228897736,
            "reference_energy": -0.003381181180884596,
            "candidate_energy": 0.0,
            "relative_energy_error_percent": 100.0,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.1713418643921614e-05,
              "p99": 8.485146099701524e-05,
              "maximum": 0.00019555282779037952
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 214,
              "rgb_channel": 0,
              "reference": -0.00019555282779037952,
              "candidate": 0.0,
              "position": [
                3.5,
                3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": true
          },
          "full": {
            "nmbe_percent": 0.0013076431866905942,
            "cvrmse_percent": 8.418424535870574,
            "rms_normalized_rmse_percent": 1.601153617505497,
            "reference_energy": 11.38454234758774,
            "candidate_energy": 11.384691216780084,
            "relative_energy_error_percent": 0.0013076431866905945,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.1957192327827215e-05,
              "p99": 8.380040526390076e-05,
              "maximum": 0.00019237562082707882
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 143,
              "rgb_channel": 0,
              "reference": 0.0027262254152446985,
              "candidate": 0.0029186010360717773,
              "position": [
                2.5,
                0.5,
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
        "identifier": "black_open_grid",
        "full_identifier": "black_open_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.028383681892268284,
            "cvrmse_percent": 2.5976170414651207,
            "rms_normalized_rmse_percent": 0.4940581407328946,
            "reference_energy": 11.387923528768624,
            "candidate_energy": 11.384691216780084,
            "relative_energy_error_percent": 0.028383681892268284,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.958120942115784e-09,
              "p99": 1.1761672794818878e-05,
              "maximum": 0.00012795720249414444
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 514,
              "rgb_channel": 0,
              "reference": 0.005723865702748299,
              "candidate": 0.005851822905242443,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -99.99999999999999,
            "cvrmse_percent": 39757.141914579384,
            "rms_normalized_rmse_percent": 7.489731202807409,
            "reference_energy": 0.011312930218082329,
            "candidate_energy": 0.0,
            "relative_energy_error_percent": 100.0,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 6.9386325776577e-05,
              "p99": 0.00039868986641522497,
              "maximum": 0.0010367671493440866
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 101,
              "rgb_channel": 0,
              "reference": 0.0010367671493440866,
              "candidate": 0.0,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": true
          },
          "full": {
            "nmbe_percent": -0.1275983901110841,
            "cvrmse_percent": 39.42352961932811,
            "rms_normalized_rmse_percent": 7.483542584310185,
            "reference_energy": 11.399236458986707,
            "candidate_energy": 11.384691216780084,
            "relative_energy_error_percent": 0.12759839011108412,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 6.937992293387651e-05,
              "p99": 0.00039465283043682575,
              "maximum": 0.0010367590002715588
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 101,
              "rgb_channel": 0,
              "reference": 0.002844356931746006,
              "candidate": 0.0018075979314744473,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      }
    ]
  },
  "controlled_skies": {
    "uniform": {
      "bias_percent": 0.0013076431867072044,
      "rms_normalized_error_percent": 0.05287562618529831,
      "absolute_error": {
        "p95": 0.03352650037712923,
        "p99": 0.04256217974659399,
        "maximum": 0.046126812100233394
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 18.868825017893485,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.05287562618529831
    },
    "overcast": {
      "bias_percent": 0.0035337960003826658,
      "rms_normalized_error_percent": 0.04411308339878694,
      "absolute_error": {
        "p95": 0.02639007568359375,
        "p99": 0.028881549835205078,
        "maximum": 0.0290985107421875
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 12.540216445922852,
      "reference_fraction_of_uniform": 0.6645997166633606,
      "rms_normalized_to_uniform_percent": 0.032194664899050034
    },
    "horizon": {
      "bias_percent": -0.08698611466614281,
      "rms_normalized_error_percent": 1.1714146980250504,
      "absolute_error": {
        "p95": 0.03314108228394483,
        "p99": 0.04037608458479002,
        "maximum": 0.04422982286468535
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.4221468228972491,
      "reference_fraction_of_uniform": 0.07537018450002127,
      "rms_normalized_to_uniform_percent": 0.049289809543134284
    },
    "north": {
      "bias_percent": 0.0,
      "rms_normalized_error_percent": 0.0,
      "absolute_error": {
        "p95": 0.0,
        "p99": 0.0,
        "maximum": 0.0
      },
      "worst_index": [
        0
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 0.0,
      "reference_fraction_of_uniform": 0.0,
      "rms_normalized_to_uniform_percent": 0.0
    },
    "east": {
      "bias_percent": -0.021737574714035167,
      "rms_normalized_error_percent": 0.08903073074675073,
      "absolute_error": {
        "p95": 0.014160513877868652,
        "p99": 0.02421200275421142,
        "maximum": 0.025661468505859375
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.6504533290863037,
      "reference_fraction_of_uniform": 0.19346478581428528,
      "rms_normalized_to_uniform_percent": 0.01867136787685703
    },
    "south": {
      "bias_percent": 0.004204612163143949,
      "rms_normalized_error_percent": 0.06575130938580451,
      "absolute_error": {
        "p95": 0.028114795684814453,
        "p99": 0.033734130859374996,
        "maximum": 0.03524017333984375
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 12.517106056213379,
      "reference_fraction_of_uniform": 0.6633749008178711,
      "rms_normalized_to_uniform_percent": 0.040974931549656896
    },
    "west": {
      "bias_percent": -0.012940684109322751,
      "rms_normalized_error_percent": 0.08556881388158058,
      "absolute_error": {
        "p95": 0.01556164026260376,
        "p99": 0.017611134052276607,
        "maximum": 0.018344879150390625
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.690631866455078,
      "reference_fraction_of_uniform": 0.19559414684772491,
      "rms_normalized_to_uniform_percent": 0.018055948079987616
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
        "identifier": "black_open_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.01566852865111069,
          "cvrmse_percent": 1.6396365551035372,
          "absolute_error_percentiles_lux": {
            "p50": 0.41290283203125,
            "p90": 4.633843994140628,
            "p95": 31.89453125,
            "p99": 139.8387890624996
          },
          "maximum_absolute_error_lux": 601.9296875,
          "worst": {
            "sensor_index": 17,
            "position": [
              2.5,
              0.5,
              0.75
            ],
            "hour_of_year": 3492.5,
            "foton_lux": 78752.8828125,
            "radiance_lux": 79354.8125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.0679566210045664,
            "maximum_error_percentage_points": 0.4969863013698621,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.07446399869992505,
            "maximum_error_percentage_points": 0.2717405217069242,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.09745433789954319,
            "maximum_error_percentage_points": 0.6068493150684944,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.09693302891933096,
            "maximum_error_percentage_points": 0.6057534246575358,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.024737442922374467,
            "maximum_error_percentage_points": 0.10945205479452191,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 33.333333333333336,
          "radiance_percent": 33.333333333333336,
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
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "black_open_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "black_open_grid",
            "maximum_error_percentage_points": 0.004667701198613372,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "black_open_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "black_open_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "black_open_grid",
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
      "study_preparation_seconds": 0.38607653299982303,
      "weather_seconds": 0.26472241700002996,
      "metric_reduction_seconds": 0.3248341999999411,
      "write_seconds": 0.01280662899989693,
      "total_seconds": 0.6026967939999395,
      "cold_end_to_end_seconds": 0.9887733269997625,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0016508300000168674,
      "engine_upload_seconds": 0.062901032,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.007909608,
      "engine_annual_reduction_seconds": 0.008155423,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.007909608
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.38607653299982303,
      "weather_seconds": 0.2578870449999613,
      "metric_reduction_seconds": 0.30234516600012284,
      "write_seconds": 0.012459697999929631,
      "total_seconds": 0.57306982099999,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.57306982099999,
      "raw_export_seconds": 0.0015089690000422706,
      "engine_upload_seconds": 0.063520564,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 1.45e-07,
      "engine_annual_reduction_seconds": 0.008431865,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02948294399993756,
      "full": 0.03082806299994445
    }
  },
  "elapsed_seconds": 4.4000214570000935,
  "result_class": "passed"
}
```
