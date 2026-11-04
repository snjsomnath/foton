# Foton report

Status: **passed**

```json
{
  "scene": "teaching_classroom",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_classroom",
    "category": "teaching",
    "question": "How is a 9 x 7 m classroom with three windows lit?",
    "interactions": [
      "multiple_bounces",
      "room",
      "side_glazing",
      "window"
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
    "sensors": 63,
    "floor_area": 63.0,
    "aperture_area": 11.520000000000001
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "1117390f074e007a8e2a1d3ef56e38192ce3d1b0eb04f25432af6a12a830d54e",
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
      "scene_fingerprint": 117564074192331588,
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 117564074192331588,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.2)",
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
    "model_sha256": "498a85b8f85c453dbf933ad47ef2d37922a017b4fcfa2c57d17b809b2104a50a",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "ea42e09dbe931b70ba70272788b8827813b1766f826a508ce4884363a557779a",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00047375215217471123,
          "p95": 4.024847876280543e-05,
          "p99": 0.00014926279429346287
        },
        "bias_percent": -0.07611121373907904,
        "identifier": "teaching_classroom_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.045527656388712,
        "worst_index": [
          26,
          99,
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
          "maximum": 0.0007091537117958069,
          "p95": 9.435423999093451e-05,
          "p99": 0.00019641279242932797
        },
        "bias_percent": 0.03961431622652311,
        "identifier": "teaching_classroom_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8077835194151125,
        "worst_index": [
          45,
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
          "maximum": 0.0007577352225780487,
          "p95": 7.808515802025771e-05,
          "p99": 0.00015426180791109796
        },
        "bias_percent": 0.01848926586111719,
        "identifier": "teaching_classroom_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.69308629185713,
        "worst_index": [
          31,
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
            "identifier": "teaching_classroom_grid",
            "sensor_count": 63,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0008360249921679497,
                  "p50": 0.0,
                  "p90": 8.759832635405474e-05,
                  "p95": 0.0001762048341333866,
                  "p99": 0.000324590338859707
                },
                "candidate_energy": 23.06057320746004,
                "cvrmse_percent": 8.2420766561156,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.03766581936473143,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 23.051890524015107,
                "relative_energy_error_percent": 0.03766581936473143,
                "rms_normalized_rmse_percent": 2.4217418657981846,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.014815425034612417,
                  "global_sensor_index": 40,
                  "local_sensor_index": 40,
                  "reference": 0.015651450026780367,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0017448663711547852,
                  "p50": 0.0,
                  "p90": 0.00012968291957804473,
                  "p95": 0.0002684237639186892,
                  "p99": 0.0005225053417962024
                },
                "candidate_energy": 8.686829279748679,
                "cvrmse_percent": 36.18503228294486,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.05016411663685454,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.691189138004997,
                "relative_energy_error_percent": 0.05016411663685456,
                "rms_normalized_rmse_percent": 2.5593870643891314,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05625571124255657,
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "reference": 0.05451084487140179,
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.91683303378522,
            "full": 355.9795409673825
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.26787493843585,
            "full": 361.9728749617934
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.2712910892442,
            "full": 353.4755000146106
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.04116698540747,
            "full": 366.64675001520663
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
            "identifier": "teaching_classroom_grid",
            "sensor_count": 63,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005007577128708363,
                  "p50": 0.0,
                  "p90": 5.070574115961794e-05,
                  "p95": 0.0001158111030235883,
                  "p99": 0.00023306508926907536
                },
                "candidate_energy": 23.046613552334748,
                "cvrmse_percent": 5.847525579770162,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.02035404722551921,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 23.05130542592724,
                "relative_energy_error_percent": 0.020354047225519208,
                "rms_normalized_rmse_percent": 1.719104811596207,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007669153623282909,
                  "global_sensor_index": 45,
                  "local_sensor_index": 45,
                  "reference": 0.007168395910412073,
                  "rgb_channel": 0,
                  "sky_patch_index": 48
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011929944157600403,
                  "p50": 3.5245001583916746e-07,
                  "p90": 9.204558446072071e-05,
                  "p95": 0.00018384740687906728,
                  "p99": 0.00036523488699458534
                },
                "candidate_energy": 15.41039262681262,
                "cvrmse_percent": 14.483034913850414,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.12553423588677598,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 15.391071562731558,
                "relative_energy_error_percent": 0.125534235886776,
                "rms_normalized_rmse_percent": 1.4644067127438305,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.049372145906090736,
                  "global_sensor_index": 44,
                  "local_sensor_index": 44,
                  "reference": 0.05056514032185078,
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 210.41933400556445,
            "full": 4188.836166984402
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 212.42266602348536,
            "full": 4120.5650409683585
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 211.08404197730124,
            "full": 4209.281084011309
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 208.55658303480595,
            "full": 4203.063874971122
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
            "identifier": "teaching_classroom_grid",
            "sensor_count": 63,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00039740954525768757,
                  "p50": 0.0,
                  "p90": 6.263244431465868e-05,
                  "p95": 0.00011670627282001075,
                  "p99": 0.0002350111841224134
                },
                "candidate_energy": 23.062058358995273,
                "cvrmse_percent": 5.895792979137754,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.045476729230869484,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 23.072551000540443,
                "relative_energy_error_percent": 0.045476729230869484,
                "rms_normalized_rmse_percent": 1.7341394645548929,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002458049450069666,
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "reference": 0.0028554589953273535,
                  "rgb_channel": 0,
                  "sky_patch_index": 15
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011787600815296173,
                  "p50": 3.559992052259986e-07,
                  "p90": 9.459377615712587e-05,
                  "p95": 0.00018659085617400676,
                  "p99": 0.0003775157919153567
                },
                "candidate_energy": 15.407253488556819,
                "cvrmse_percent": 15.063974703612919,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1252274859601201,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 15.387983503675208,
                "relative_energy_error_percent": 0.1252274859601201,
                "rms_normalized_rmse_percent": 1.5222116526146736,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06789384037256241,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.06907260045409203,
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 201.96199999190867,
            "full": 4312.350791995414
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 203.01375002600253,
            "full": 4302.952250000089
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 203.41287506744266,
            "full": 4337.56579097826
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 203.16608296707273,
            "full": 4308.404708979651
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
            "identifier": "teaching_classroom_grid",
            "sensor_count": 63,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002988399937748909,
                  "p50": 0.0,
                  "p90": 3.262314130552113e-05,
                  "p95": 5.881581455469126e-05,
                  "p99": 0.00012502096593379968
                },
                "candidate_energy": 23.05523271553875,
                "cvrmse_percent": 3.189024751251244,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.015668472022775968,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 23.051620878770564,
                "relative_energy_error_percent": 0.015668472022775968,
                "rms_normalized_rmse_percent": 0.9374103018826835,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.018299175426363945,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.018000335432589054,
                  "rgb_channel": 0,
                  "sky_patch_index": 118
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008264407515525818,
                  "p50": 2.634864983974694e-07,
                  "p90": 5.412034224718814e-05,
                  "p95": 0.00010592621983960242,
                  "p99": 0.00020699718967080063
                },
                "candidate_energy": 15.422007902293384,
                "cvrmse_percent": 8.928369871056537,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.044107813872876316,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 15.415208590780047,
                "relative_energy_error_percent": 0.044107813872876316,
                "rms_normalized_rmse_percent": 0.9034655293355869,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07128603011369705,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.07045958936214447,
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 334.42479092627764,
            "full": 7579.328499967232
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 333.2110419869423,
            "full": 7705.848833080381
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 325.0803330447525,
            "full": 7842.846208019182
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
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "63",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 349.3308749748394,
            "full": 7610.369292087853
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
    "/Users/ssanjay/GitHub/foton-release-0.3.2/validation/results/2026-11-04-architectural-v4-metal-0.3.2-release/teaching_classroom/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2257.149750017561,
      "invocation_count": 4,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_classroom/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 8617.552249925211,
      "invocation_count": 4,
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
      63,
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
        "identifier": "teaching_classroom_grid",
        "full_identifier": "teaching_classroom_grid",
        "start_sensor_index": 0,
        "sensor_count": 63,
        "stages": {
          "direct": {
            "nmbe_percent": 0.01266871125203931,
            "cvrmse_percent": 1.9996825692834805,
            "rms_normalized_rmse_percent": 0.5879454999976449,
            "reference_energy": 23.06347363085615,
            "candidate_energy": 23.066395475735135,
            "relative_energy_error_percent": 0.012668711252039312,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.249399691820145e-06,
              "p95": 2.6832130970433354e-05,
              "p99": 8.811010047793388e-05,
              "maximum": 0.00021480349823832512
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 39,
              "sky_patch_index": 76,
              "rgb_channel": 0,
              "reference": 0.0013871249975636601,
              "candidate": 0.001172321499325335,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.3437169081845861,
            "cvrmse_percent": 24.22929684042165,
            "rms_normalized_rmse_percent": 2.4499126473776163,
            "reference_energy": 15.408561418905123,
            "candidate_energy": 15.201513973811288,
            "relative_energy_error_percent": 1.343716908184586,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.145002613611723e-06,
              "p90": 5.7888460287358615e-05,
              "p95": 9.001243161037552e-05,
              "p99": 0.00022370199672877756,
              "maximum": 0.00294281542301178
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07032512873411179,
              "candidate": 0.0673823133111,
              "position": [
                4.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5305817588043555,
            "cvrmse_percent": 9.689886794320204,
            "rms_normalized_rmse_percent": 2.4463103809108224,
            "reference_energy": 38.472035049761274,
            "candidate_energy": 38.26790944954642,
            "relative_energy_error_percent": 0.5305817588043555,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.1541147273419483e-06,
              "p90": 5.788885318906978e-05,
              "p95": 8.792467997409394e-05,
              "p99": 0.0002128504496067757,
              "maximum": 0.00294281542301178
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07032512873411179,
              "candidate": 0.0673823133111,
              "position": [
                4.5,
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
      63,
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
        "identifier": "teaching_classroom_grid",
        "full_identifier": "teaching_classroom_grid",
        "start_sensor_index": 0,
        "sensor_count": 63,
        "stages": {
          "direct": {
            "nmbe_percent": 0.01266871125203931,
            "cvrmse_percent": 1.9996825692834805,
            "rms_normalized_rmse_percent": 0.5879454999976449,
            "reference_energy": 23.06347363085615,
            "candidate_energy": 23.066395475735135,
            "relative_energy_error_percent": 0.012668711252039312,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.249399691820145e-06,
              "p95": 2.6832130970433354e-05,
              "p99": 8.811010047793388e-05,
              "maximum": 0.00021480349823832512
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 39,
              "sky_patch_index": 76,
              "rgb_channel": 0,
              "reference": 0.0013871249975636601,
              "candidate": 0.001172321499325335,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 75.09699475455544,
            "cvrmse_percent": 381.28451888641507,
            "rms_normalized_rmse_percent": 26.934016206347398,
            "reference_energy": 8.681767494136729,
            "candidate_energy": 15.201513973811288,
            "relative_energy_error_percent": 75.09699475455545,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.500000053056283e-07,
              "p90": 0.000514858664246276,
              "p95": 0.0006674926320556531,
              "p99": 0.0010184820345602928,
              "maximum": 0.017484840005636215
            },
            "worst": {
              "global_sensor_index": 60,
              "local_sensor_index": 60,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03969316929578781,
              "candidate": 0.057178009301424026,
              "position": [
                8.5,
                2.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.546916934325242,
            "cvrmse_percent": 104.27497432196593,
            "rms_normalized_rmse_percent": 26.934102951355435,
            "reference_energy": 31.74524112499288,
            "candidate_energy": 38.26790944954642,
            "relative_energy_error_percent": 20.54691693432524,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.500000053056283e-07,
              "p90": 0.0005156330182217063,
              "p95": 0.0006692829134408374,
              "p99": 0.0010009312839247286,
              "maximum": 0.017484840005636215
            },
            "worst": {
              "global_sensor_index": 60,
              "local_sensor_index": 60,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03969316929578781,
              "candidate": 0.057178009301424026,
              "position": [
                8.5,
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
      "bias_percent": 0.15623589452553835,
      "rms_normalized_error_percent": 0.2374141971369134,
      "absolute_error": {
        "p95": 0.16415433812138894,
        "p99": 0.20661615568269598,
        "maximum": 0.2103198275536613
      },
      "worst_index": [
        7
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 26.724942288480342,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2374141971369134
    },
    "overcast": {
      "bias_percent": 0.1358520142328262,
      "rms_normalized_error_percent": 0.17869870386904843,
      "absolute_error": {
        "p95": 0.08221502304077148,
        "p99": 0.1276633071899415,
        "maximum": 0.15065574645996094
      },
      "worst_index": [
        26
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 17.2152099609375,
      "reference_fraction_of_uniform": 0.644162654876709,
      "rms_normalized_to_uniform_percent": 0.1250088987847618
    },
    "horizon": {
      "bias_percent": 1.0187523462624473,
      "rms_normalized_error_percent": 2.2200654887169056,
      "absolute_error": {
        "p95": 0.12866159563026586,
        "p99": 0.15688391218295816,
        "maximum": 0.18230035800553956
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.4065141985950778,
      "reference_fraction_of_uniform": 0.09004749842368767,
      "rms_normalized_to_uniform_percent": 0.15302985191606971
    },
    "north": {
      "bias_percent": -29.92046264878796,
      "rms_normalized_error_percent": 139.79601416523315,
      "absolute_error": {
        "p95": 8.948107661126415e-05,
        "p99": 0.00019508587973177843,
        "maximum": 0.0003373752551851794
      },
      "worst_index": [
        62
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.875263999158051e-05,
      "reference_fraction_of_uniform": 1.0758727739812457e-06,
      "rms_normalized_to_uniform_percent": 0.00015034168425191778
    },
    "east": {
      "bias_percent": 0.04340626110653493,
      "rms_normalized_error_percent": 0.303709787550891,
      "absolute_error": {
        "p95": 0.0467120885848999,
        "p99": 0.04825870513916016,
        "maximum": 0.04892921447753906
      },
      "worst_index": [
        26
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.272243499755859,
      "reference_fraction_of_uniform": 0.1972780078649521,
      "rms_normalized_to_uniform_percent": 0.06457352953903218
    },
    "south": {
      "bias_percent": 0.17932755546666382,
      "rms_normalized_error_percent": 0.3239368836094743,
      "absolute_error": {
        "p95": 0.16163806915283202,
        "p99": 0.1798056316375733,
        "maximum": 0.19431352615356445
      },
      "worst_index": [
        7
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 18.420686721801758,
      "reference_fraction_of_uniform": 0.6892694234848022,
      "rms_normalized_to_uniform_percent": 0.2064550016470904
    },
    "west": {
      "bias_percent": 0.16076520506482292,
      "rms_normalized_error_percent": 0.3049911963494008,
      "absolute_error": {
        "p95": 0.04339730739593506,
        "p99": 0.04860215187072754,
        "maximum": 0.048955440521240234
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.1261887550354,
      "reference_fraction_of_uniform": 0.1918129026889801,
      "rms_normalized_to_uniform_percent": 0.0626473637198631
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
        "identifier": "teaching_classroom_grid",
        "sensor_count": 63,
        "illuminance": {
          "nmbe_percent": 0.054802501776256916,
          "cvrmse_percent": 1.0952847724677481,
          "absolute_error_percentiles_lux": {
            "p50": 4.162109375,
            "p90": 36.58891601562503,
            "p95": 54.635888671874994,
            "p99": 105.80455078124999
          },
          "maximum_absolute_error_lux": 427.0244140625,
          "worst": {
            "sensor_index": 10,
            "position": [
              1.5,
              3.5,
              0.75
            ],
            "hour_of_year": 1859.5,
            "foton_lux": 6350.20458984375,
            "radiance_lux": 5923.18017578125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.10979995651228472,
            "maximum_error_percentage_points": 0.5469863013698557,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.05082350903632073,
            "maximum_error_percentage_points": 0.31508555159730633,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.05293759512937569,
            "maximum_error_percentage_points": 0.2969863013698628,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.07745161991737333,
            "maximum_error_percentage_points": 0.29876712328767496,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.08229180256577488,
            "maximum_error_percentage_points": 0.2779452054794511,
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
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_classroom_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_classroom_grid",
            "maximum_error_percentage_points": 0.004886023116441152,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_classroom_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_classroom_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_classroom_grid",
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
      "study_preparation_seconds": 0.00806458294391632,
      "weather_seconds": 0.07540958398021758,
      "metric_reduction_seconds": 0.0530439579160884,
      "write_seconds": 0.011715458938851953,
      "total_seconds": 0.14031375001650304,
      "cold_end_to_end_seconds": 0.14837833296041936,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0019507500110194087,
      "engine_upload_seconds": 0.000280875,
      "engine_acceleration_structure_seconds": 0.003951042,
      "engine_tracing_seconds": 0.02331737510394305,
      "engine_annual_reduction_seconds": 0.0006559999892488122,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.02331737510394305
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.00806458294391632,
      "weather_seconds": 0.07519812497776002,
      "metric_reduction_seconds": 0.01471637503709644,
      "write_seconds": 0.01029629202093929,
      "total_seconds": 0.10035449999850243,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.10035449999850243,
      "raw_export_seconds": 0.0020517499651759863,
      "engine_upload_seconds": 5.5792e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0006273334147408605,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.0252018750179559,
      "full": 0.02887524990364909
    }
  },
  "elapsed_seconds": 0.8171570829581469,
  "result_class": "passed"
}
```
