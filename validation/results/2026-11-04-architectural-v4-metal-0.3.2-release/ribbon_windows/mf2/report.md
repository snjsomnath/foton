# Foton report

Status: **passed**

```json
{
  "scene": "ribbon_windows",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "ribbon_windows",
    "category": "openings",
    "question": "Do separated ribbon openings retain their opaque mullion gaps?",
    "interactions": [
      "multiple_openings",
      "punched_faces",
      "mullion_gaps"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 3,
    "shades": 0,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 6.3
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "e2f63b96f5f88d47a824f6386e62a194f10df73cfd4f832cf77733e9f11cd49b",
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 6460232368099317047,
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 6460232368099317047,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.2)",
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
    "model_sha256": "9ca4013b3ed6a7c3b8b266ec42c5c237aa34f86744b49045e25cf8c225529e17",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "42ebbd5873d9863a0ad3aca60e92d9e55c1ae842623c6cc1f4949849ae92cd10",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00014028436271473765,
          "p95": 2.0007137209177017e-06,
          "p99": 1.5360768884420395e-05
        },
        "bias_percent": -0.04104282735490409,
        "identifier": "ribbon_windows_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7543363782339135,
        "worst_index": [
          11,
          543,
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
          "maximum": 0.0006311200559139252,
          "p95": 5.4704491049051285e-05,
          "p99": 0.00012675859034061432
        },
        "bias_percent": 0.0667185928119295,
        "identifier": "ribbon_windows_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.2558245850301812,
        "worst_index": [
          28,
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
          "maximum": 0.0005621872842311859,
          "p95": 4.590745083987713e-05,
          "p99": 0.00010241457493975759
        },
        "bias_percent": 0.011155233695881957,
        "identifier": "ribbon_windows_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0703269038352847,
        "worst_index": [
          17,
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
            "identifier": "ribbon_windows_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004729859356302768,
                  "p50": 0.0,
                  "p90": 4.258459666743878e-05,
                  "p95": 0.00011459499364718795,
                  "p99": 0.0002726379898376763
                },
                "candidate_energy": 11.974888652579011,
                "cvrmse_percent": 27.061999435778663,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.015340498806019112,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.976725942079156,
                "relative_energy_error_percent": 0.015340498806019112,
                "rms_normalized_rmse_percent": 7.338375150690736,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0010873934952542186,
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "reference": 0.0006144075596239418,
                  "rgb_channel": 0,
                  "sky_patch_index": 91
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013381801545619965,
                  "p50": 0.0,
                  "p90": 4.6943918277975273e-05,
                  "p95": 0.00015935348346829414,
                  "p99": 0.0003735740319825709
                },
                "candidate_energy": 4.294657422055929,
                "cvrmse_percent": 109.18522193297244,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.2181985467666444,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.304048793976513,
                "relative_energy_error_percent": 0.21819854676664438,
                "rms_normalized_rmse_percent": 4.720434944797492,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0316455103456974,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.0329836905002594,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          }
        ],
        "half_run_count": 4,
        "oracle_stable": true,
        "run_count": 8,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 124.86829096451402,
            "full": 246.09050003346056
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.20216607581824,
            "full": 264.24787496216595
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.66833295486867,
            "full": 241.41145800240338
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.167958015576,
            "full": 249.71166590694338
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.59266700595617,
            "full": 259.43529210053384
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.78254197351635,
            "full": 245.36404199898243
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.836874935776,
            "full": 244.33291691821069
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.114417091012,
            "full": 243.38925001211464
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
            "identifier": "ribbon_windows_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00044110382441431284,
                  "p50": 0.0,
                  "p90": 2.2943393560126424e-05,
                  "p95": 7.007952081039548e-05,
                  "p99": 0.00017840147484093904
                },
                "candidate_energy": 11.974256022516329,
                "cvrmse_percent": 18.010164051412907,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.03731879874343266,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.978726339290915,
                "relative_energy_error_percent": 0.03731879874343266,
                "rms_normalized_rmse_percent": 4.8812948609413835,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004150356398895383,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.00370925257448107,
                  "rgb_channel": 0,
                  "sky_patch_index": 363
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010748058557510376,
                  "p50": 5.000000058430487e-08,
                  "p90": 3.7236054959066826e-05,
                  "p95": 0.00010712991934269667,
                  "p99": 0.00024981697788462043
                },
                "candidate_energy": 7.698964058256497,
                "cvrmse_percent": 42.2536898074401,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1429231913152542,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.687976157384806,
                "relative_energy_error_percent": 0.1429231913152542,
                "rms_normalized_rmse_percent": 2.4313325318665377,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05073380470275879,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.04965899884700775,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 175.22687499877065,
            "full": 2384.0235840762034
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 177.17116698622704,
            "full": 2344.602750032209
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 165.0515419896692,
            "full": 2315.372582990676
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 162.91058401111513,
            "full": 2272.038625087589
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
            "identifier": "ribbon_windows_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00039645505603402853,
                  "p50": 0.0,
                  "p90": 2.2868817904964092e-05,
                  "p95": 6.989019311731681e-05,
                  "p99": 0.00017557106912136078
                },
                "candidate_energy": 11.978263230394532,
                "cvrmse_percent": 17.27491176626928,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.01845914727840082,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.976052553215595,
                "relative_energy_error_percent": 0.018459147278400822,
                "rms_normalized_rmse_percent": 4.681842302417351,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0036023034481331706,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.003998758504167199,
                  "rgb_channel": 0,
                  "sky_patch_index": 405
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010872390121221542,
                  "p50": 5.000000058430487e-08,
                  "p90": 3.9351497616735296e-05,
                  "p95": 0.00011269387323409319,
                  "p99": 0.0002562931040301919
                },
                "candidate_energy": 7.698783513856416,
                "cvrmse_percent": 43.17115604289996,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.18522966404357147,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.713070408261082,
                "relative_energy_error_percent": 0.18522966404357147,
                "rms_normalized_rmse_percent": 2.4879874748920896,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04972240515053272,
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "reference": 0.05080964416265488,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 166.92600003443658,
            "full": 2490.4322921065614
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 160.55470798164606,
            "full": 2439.657749957405
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 173.94629097543657,
            "full": 2464.8248750017956
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 162.37695794552565,
            "full": 2432.024082983844
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
            "identifier": "ribbon_windows_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00020556990057229996,
                  "p50": 0.0,
                  "p90": 1.1580050340853647e-05,
                  "p95": 4.071451257914305e-05,
                  "p99": 9.758071973919868e-05
                },
                "candidate_energy": 11.978547271836078,
                "cvrmse_percent": 9.841924798149341,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.023661413104849125,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.975713648757392,
                "relative_energy_error_percent": 0.02366141310484913,
                "rms_normalized_rmse_percent": 2.668921466937878,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002358378958888352,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.002152809058316052,
                  "rgb_channel": 0,
                  "sky_patch_index": 207
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000571124255657196,
                  "p50": 4.9999993478877514e-08,
                  "p90": 2.3051748030411725e-05,
                  "p95": 6.188949919305742e-05,
                  "p99": 0.00014355091843754053
                },
                "candidate_energy": 7.7089224614713565,
                "cvrmse_percent": 24.488236278364887,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.02004492222485071,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.707377523641167,
                "relative_energy_error_percent": 0.02004492222485071,
                "rms_normalized_rmse_percent": 1.4108693726507524,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06109756417572498,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.06052643992006779,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 255.82949991803616,
            "full": 4218.462500022724
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 254.0749169420451,
            "full": 4251.036209054291
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 255.0291660008952,
            "full": 4294.633999932557
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 256.82195799890906,
            "full": 4307.689458015375
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
    "/Users/ssanjay/GitHub/foton-release-0.3.2/validation/results/2026-11-04-architectural-v4-metal-0.3.2-release/ribbon_windows/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2561.5634999703616,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/ribbon_windows/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10766.120584099554,
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
        "identifier": "ribbon_windows_grid",
        "full_identifier": "ribbon_windows_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.03326701579726625,
            "cvrmse_percent": 1.5333370162924467,
            "rms_normalized_rmse_percent": 0.4159521874241875,
            "reference_energy": 11.975549641100315,
            "candidate_energy": 11.9715657331094,
            "relative_energy_error_percent": 0.03326701579726625,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.514570951461792e-08,
              "p95": 1.3638054952025414e-06,
              "p99": 1.2270873412489891e-05,
              "maximum": 5.9494748711586e-05
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052893467247486,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.2905113429648822,
            "cvrmse_percent": 41.84673215984112,
            "rms_normalized_rmse_percent": 2.4102876764501393,
            "reference_energy": 7.709730859118835,
            "candidate_energy": 7.610235907869843,
            "relative_energy_error_percent": 1.2905113429648822,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.000000058430487e-08,
              "p90": 1.6857193259056698e-05,
              "p95": 2.994472743012011e-05,
              "p99": 6.472982931882143e-05,
              "maximum": 0.001979835331439972
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.060682155191898346,
              "candidate": 0.058702319860458374,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5256661658377423,
            "cvrmse_percent": 16.38428772950898,
            "rms_normalized_rmse_percent": 2.40955745983755,
            "reference_energy": 19.68528050021915,
            "candidate_energy": 19.581801640979243,
            "relative_energy_error_percent": 0.5256661658377423,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.000000058430487e-08,
              "p90": 1.6844330821186346e-05,
              "p95": 2.9477043426595628e-05,
              "p99": 6.467319326475263e-05,
              "maximum": 0.001979835331439972
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.060682155191898346,
              "candidate": 0.058702319860458374,
              "position": [
                1.5,
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
        "identifier": "ribbon_windows_grid",
        "full_identifier": "ribbon_windows_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.03326701579726625,
            "cvrmse_percent": 1.5333370162924467,
            "rms_normalized_rmse_percent": 0.4159521874241875,
            "reference_energy": 11.975549641100315,
            "candidate_energy": 11.9715657331094,
            "relative_energy_error_percent": 0.03326701579726625,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.514570951461792e-08,
              "p95": 1.3638054952025414e-06,
              "p99": 1.2270873412489891e-05,
              "maximum": 5.9494748711586e-05
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052893467247486,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 76.99825214497798,
            "cvrmse_percent": 822.0467128049669,
            "rms_normalized_rmse_percent": 35.54496243413716,
            "reference_energy": 4.299610767702019,
            "candidate_energy": 7.610235907869843,
            "relative_energy_error_percent": 76.99825214497798,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00010801400130731062,
              "p95": 0.00014597526751458645,
              "p99": 0.00024067307822406292,
              "maximum": 0.01507648080587387
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.040461860597133636,
              "candidate": 0.05553834140300751,
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
            "nmbe_percent": 20.317103789579424,
            "cvrmse_percent": 217.16684775704886,
            "rms_normalized_rmse_percent": 35.544403132610285,
            "reference_energy": 16.275160408802336,
            "candidate_energy": 19.581801640979243,
            "relative_energy_error_percent": 20.317103789579413,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00010775849204947013,
              "p95": 0.0001454702578485012,
              "p99": 0.00023893883917480707,
              "maximum": 0.01507648080587387
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.040461860597133636,
              "candidate": 0.05553834140300751,
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
      "bias_percent": 0.0430799848430471,
      "rms_normalized_error_percent": 0.19135771480759226,
      "absolute_error": {
        "p95": 0.1335805423574945,
        "p99": 0.15429941830092028,
        "maximum": 0.15871749997153373
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 24.161883681632975,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.19135771480759226
    },
    "overcast": {
      "bias_percent": 0.003623370809250685,
      "rms_normalized_error_percent": 0.1356833949461434,
      "absolute_error": {
        "p95": 0.05739396810531616,
        "p99": 0.08377399444580072,
        "maximum": 0.0972442626953125
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.57344913482666,
      "reference_fraction_of_uniform": 0.6445461511611938,
      "rms_normalized_to_uniform_percent": 0.09434011086365844
    },
    "horizon": {
      "bias_percent": 0.8718806696972496,
      "rms_normalized_error_percent": 1.665290292288557,
      "absolute_error": {
        "p95": 0.1184071914267617,
        "p99": 0.1393713979155769,
        "maximum": 0.150140719460516
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.8267966448662323,
      "reference_fraction_of_uniform": 0.116994050716959,
      "rms_normalized_to_uniform_percent": 0.14323629112804317
    },
    "north": {
      "bias_percent": -85.74786345519192,
      "rms_normalized_error_percent": 96.68556129812063,
      "absolute_error": {
        "p95": 0.00016036676208841527,
        "p99": 0.0001796302688489959,
        "maximum": 0.00018504034960642457
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.4619859686936252e-05,
      "reference_fraction_of_uniform": 1.0189544354943791e-06,
      "rms_normalized_to_uniform_percent": 0.00016312594216810107
    },
    "east": {
      "bias_percent": -0.19963991640404918,
      "rms_normalized_error_percent": 0.28864091706103134,
      "absolute_error": {
        "p95": 0.038792967796325684,
        "p99": 0.06066362857818602,
        "maximum": 0.06469058990478516
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.233143329620361,
      "reference_fraction_of_uniform": 0.1751992255449295,
      "rms_normalized_to_uniform_percent": 0.057040860295697875
    },
    "south": {
      "bias_percent": 0.07146119069370795,
      "rms_normalized_error_percent": 0.263508083811154,
      "absolute_error": {
        "p95": 0.12846839427947998,
        "p99": 0.13998360633850096,
        "maximum": 0.14304542541503906
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 16.98445701599121,
      "reference_fraction_of_uniform": 0.7029442191123962,
      "rms_normalized_to_uniform_percent": 0.17182263353468227
    },
    "west": {
      "bias_percent": 0.20134085906780383,
      "rms_normalized_error_percent": 0.2097703632426389,
      "absolute_error": {
        "p95": 0.028011322021484375,
        "p99": 0.030027168989181514,
        "maximum": 0.03080451488494873
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.273641109466553,
      "reference_fraction_of_uniform": 0.17687532305717468,
      "rms_normalized_to_uniform_percent": 0.04169988289282032
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
        "identifier": "ribbon_windows_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.055080588008374363,
          "cvrmse_percent": 1.2581551833933413,
          "absolute_error_percentiles_lux": {
            "p50": 3.552490234375,
            "p90": 36.47188720703126,
            "p95": 56.8461425781249,
            "p99": 115.14434570312451
          },
          "maximum_absolute_error_lux": 357.5703125,
          "worst": {
            "sensor_index": 5,
            "position": [
              0.5,
              0.5,
              0.75
            ],
            "hour_of_year": 5843.5,
            "foton_lux": 34002.6875,
            "radiance_lux": 33645.1171875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.08741248097412363,
            "maximum_error_percentage_points": 0.3808219178082197,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.04498827461359135,
            "maximum_error_percentage_points": 0.19487209842623088,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.042100456621004735,
            "maximum_error_percentage_points": 0.27643835616438395,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.08201293759513047,
            "maximum_error_percentage_points": 0.41054794520547944,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.061879756468798064,
            "maximum_error_percentage_points": 0.4141095890410966,
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
      "maximum_error_percentage_points": 0.004984482020546466,
      "metrics": {
        "da": [
          {
            "identifier": "ribbon_windows_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "ribbon_windows_grid",
            "maximum_error_percentage_points": 0.004984482020546466,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "ribbon_windows_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "ribbon_windows_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "ribbon_windows_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
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
      "study_preparation_seconds": 0.009769291034899652,
      "weather_seconds": 0.08347279101144522,
      "metric_reduction_seconds": 0.11685054190456867,
      "write_seconds": 0.015935166971758008,
      "total_seconds": 0.21639175002928823,
      "cold_end_to_end_seconds": 0.22616104106418788,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.00357504200655967,
      "engine_upload_seconds": 0.000778125,
      "engine_acceleration_structure_seconds": 0.003387167,
      "engine_tracing_seconds": 0.0563143331091851,
      "engine_annual_reduction_seconds": 0.0023095833603292704,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0563143331091851
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.009769291034899652,
      "weather_seconds": 0.07930733298417181,
      "metric_reduction_seconds": 0.04904295806773007,
      "write_seconds": 0.0296061250846833,
      "total_seconds": 0.15810124995186925,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.15810124995186925,
      "raw_export_seconds": 0.008968167006969452,
      "engine_upload_seconds": 5.7e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0017578750848770142,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.018831958062946796,
      "full": 0.06479120801668614
    }
  },
  "elapsed_seconds": 1.361991957994178,
  "result_class": "passed"
}
```
