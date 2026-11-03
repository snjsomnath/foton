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
  "model_sha256": "5fae8375393857b137fbb30ad6012c757816cf3a1634cbfc3ee68515235e95a1",
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
      "scene_fingerprint": 117564074192331588,
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
      "scene_fingerprint": 117564074192331588,
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
    "/content/suite-vulkan-0.3.1/teaching_classroom/mf1/oracle/scene.rad"
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
            "nmbe_percent": 0.012666495349177086,
            "cvrmse_percent": 1.9996831036392382,
            "rms_normalized_rmse_percent": 0.5879456571086125,
            "reference_energy": 23.06347363085615,
            "candidate_energy": 23.066394964670963,
            "relative_energy_error_percent": 0.012666495349177085,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.248934030532837e-06,
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
            "nmbe_percent": -1.3438438449542933,
            "cvrmse_percent": 24.229624777617964,
            "rms_normalized_rmse_percent": 2.4499458063045996,
            "reference_energy": 15.408561418905123,
            "candidate_energy": 15.201494414681164,
            "relative_energy_error_percent": 1.3438438449542933,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.145002613611723e-06,
              "p90": 5.7888460287358615e-05,
              "p95": 9.001243161037552e-05,
              "p99": 0.00022370210499502688,
              "maximum": 0.0029428377747535706
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07032512873411179,
              "candidate": 0.06738229095935822,
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
            "nmbe_percent": -0.5306339270722152,
            "cvrmse_percent": 9.69001644141336,
            "rms_normalized_rmse_percent": 2.4463431116368435,
            "reference_energy": 38.472035049761274,
            "candidate_energy": 38.26788937935213,
            "relative_energy_error_percent": 0.5306339270722152,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.1541147273419483e-06,
              "p90": 5.7885496062226593e-05,
              "p95": 8.792467997409394e-05,
              "p99": 0.00021285041701048557,
              "maximum": 0.0029428377747535706
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07032512873411179,
              "candidate": 0.06738229095935822,
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
            "nmbe_percent": 0.012666495349177086,
            "cvrmse_percent": 1.9996831036392382,
            "rms_normalized_rmse_percent": 0.5879456571086125,
            "reference_energy": 23.06347363085615,
            "candidate_energy": 23.066394964670963,
            "relative_energy_error_percent": 0.012666495349177085,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.248934030532837e-06,
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
            "nmbe_percent": 75.09676946483032,
            "cvrmse_percent": 381.28267143738736,
            "rms_normalized_rmse_percent": 26.93388570217115,
            "reference_energy": 8.681767494136729,
            "candidate_energy": 15.201494414681164,
            "relative_energy_error_percent": 75.09676946483032,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.500000053056283e-07,
              "p90": 0.000514858664246276,
              "p95": 0.0006674926728010159,
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
            "nmbe_percent": 20.546853711638676,
            "cvrmse_percent": 104.27446795217796,
            "rms_normalized_rmse_percent": 26.933972156636095,
            "reference_energy": 31.74524112499288,
            "candidate_energy": 38.26788937935213,
            "relative_energy_error_percent": 20.546853711638676,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.500000053056283e-07,
              "p90": 0.0005156330182217063,
              "p95": 0.0006692828377708782,
              "p99": 0.0010009317006915808,
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
      "bias_percent": 0.15620726564482962,
      "rms_normalized_error_percent": 0.23743771089971188,
      "absolute_error": {
        "p95": 0.16430082489901512,
        "p99": 0.20661516711171254,
        "maximum": 0.21031964000857428
      },
      "worst_index": [
        7
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 26.724942288480342,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.23743771089971188
    },
    "overcast": {
      "bias_percent": 0.1358321841540763,
      "rms_normalized_error_percent": 0.17871183821156017,
      "absolute_error": {
        "p95": 0.08221523761749266,
        "p99": 0.1276633071899415,
        "maximum": 0.15065574645996094
      },
      "worst_index": [
        26
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 17.215211868286133,
      "reference_fraction_of_uniform": 0.6441627144813538,
      "rms_normalized_to_uniform_percent": 0.12501809465044744
    },
    "horizon": {
      "bias_percent": 1.0184473186142273,
      "rms_normalized_error_percent": 2.219978835073397,
      "absolute_error": {
        "p95": 0.1286614205881861,
        "p99": 0.15688321534877397,
        "maximum": 0.1822985242313706
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.4065141985950778,
      "reference_fraction_of_uniform": 0.09004749842368767,
      "rms_normalized_to_uniform_percent": 0.1530238788516257
    },
    "north": {
      "bias_percent": -29.920463710052875,
      "rms_normalized_error_percent": 139.79601290789563,
      "absolute_error": {
        "p95": 8.948108243203023e-05,
        "p99": 0.00019508588424287213,
        "maximum": 0.0003373752551851794
      },
      "worst_index": [
        62
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.8752638172591105e-05,
      "reference_fraction_of_uniform": 1.0758727739812457e-06,
      "rms_normalized_to_uniform_percent": 0.00015034168425191778
    },
    "east": {
      "bias_percent": 0.043398436374692734,
      "rms_normalized_error_percent": 0.3037123720756519,
      "absolute_error": {
        "p95": 0.04671926498413086,
        "p99": 0.048260250091552735,
        "maximum": 0.04893016815185547
      },
      "worst_index": [
        26
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.272243499755859,
      "reference_fraction_of_uniform": 0.1972780078649521,
      "rms_normalized_to_uniform_percent": 0.0645740841938396
    },
    "south": {
      "bias_percent": 0.17929098501664656,
      "rms_normalized_error_percent": 0.3239466088971183,
      "absolute_error": {
        "p95": 0.16163721084594726,
        "p99": 0.17980504035949713,
        "maximum": 0.19431352615356445
      },
      "worst_index": [
        7
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 18.42068862915039,
      "reference_fraction_of_uniform": 0.6892695426940918,
      "rms_normalized_to_uniform_percent": 0.20646120134007803
    },
    "west": {
      "bias_percent": 0.16071330570045914,
      "rms_normalized_error_percent": 0.30501262724194267,
      "absolute_error": {
        "p95": 0.04339730739593506,
        "p99": 0.048600993156433105,
        "maximum": 0.04895472526550293
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.1261887550354,
      "reference_fraction_of_uniform": 0.1918129026889801,
      "rms_normalized_to_uniform_percent": 0.06265176467249393
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
          "nmbe_percent": 0.05477550553291812,
          "cvrmse_percent": 1.0952784230218011,
          "absolute_error_percentiles_lux": {
            "p50": 4.16229248046875,
            "p90": 36.585693359375,
            "p95": 54.63571777343749,
            "p99": 105.80451660156248
          },
          "maximum_absolute_error_lux": 427.02392578125,
          "worst": {
            "sensor_index": 10,
            "position": [
              1.5,
              3.5,
              0.75
            ],
            "hour_of_year": 1859.5,
            "foton_lux": 6350.2041015625,
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
      "study_preparation_seconds": 0.4161891929979902,
      "weather_seconds": 0.38741560699418187,
      "metric_reduction_seconds": 0.4569818870004383,
      "write_seconds": 0.07507903699297458,
      "total_seconds": 0.9199681300015072,
      "cold_end_to_end_seconds": 1.3361573229994974,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0459329160003108,
      "engine_upload_seconds": 0.015112536999999999,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.026225478,
      "engine_annual_reduction_seconds": 0.012020289,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.026225478
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.4161891929979902,
      "weather_seconds": 0.38709374199970625,
      "metric_reduction_seconds": 0.4078255819986225,
      "write_seconds": 0.03186124200146878,
      "total_seconds": 0.8271052180061815,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.8271052180061815,
      "raw_export_seconds": 0.011432726998464204,
      "engine_upload_seconds": 0.015612416,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 8.7e-08,
      "engine_annual_reduction_seconds": 0.010278116,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.015946839994285256,
      "full": 0.03576569400320295
    }
  },
  "elapsed_seconds": 4.07669304600131,
  "result_class": "passed"
}
```
