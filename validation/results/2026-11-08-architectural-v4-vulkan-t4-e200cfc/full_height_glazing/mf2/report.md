# Foton report

Status: **passed**

```json
{
  "scene": "full_height_glazing",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "full_height_glazing",
    "category": "openings",
    "question": "Is large near-floor glazing represented without edge leaks?",
    "interactions": [
      "large_opening",
      "near_floor_glazing"
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
    "aperture_area": 15.119999999999997
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "cf6065add0a7b3a721193d8e74b7067a296d35bd85105f8b7d5c4378ccf52473",
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
      "scene_fingerprint": 3561854793510213323,
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
      "scene_fingerprint": 3561854793510213323,
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
    "model_sha256": "46520d6fd4c8133405a90893ea02d78dd010a6597b14eea6bcd67adda76a9002",
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
          "maximum": 0.00013487995602190495,
          "p95": 2.3329630494117737e-07,
          "p99": 1.83905940502882e-05
        },
        "bias_percent": 0.03677204259932399,
        "identifier": "full_height_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.5486334346969537,
        "worst_index": [
          3,
          309,
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
          "maximum": 0.0006342381238937378,
          "p95": 7.913948502391577e-05,
          "p99": 0.0001499920035712421
        },
        "bias_percent": 0.027150952568931238,
        "identifier": "full_height_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7345157045963514,
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
          "maximum": 0.0007528960704803467,
          "p95": 6.329407915472984e-05,
          "p99": 0.0001207430032081902
        },
        "bias_percent": -0.024213671722531502,
        "identifier": "full_height_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.6160916911076786,
        "worst_index": [
          8,
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
            "identifier": "full_height_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006423312006518245,
                  "p50": 0.0,
                  "p90": 4.735146649181843e-05,
                  "p95": 0.0001283779856748879,
                  "p99": 0.00023247292847372591
                },
                "candidate_energy": 19.691736579785356,
                "cvrmse_percent": 16.226219845396123,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.02238818393556855,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 19.696146189222418,
                "relative_energy_error_percent": 0.02238818393556855,
                "rms_normalized_rmse_percent": 5.477919323005418,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004103224142454565,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.00346089294180274,
                  "rgb_channel": 0,
                  "sky_patch_index": 365
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0016327425837516785,
                  "p50": 0.0,
                  "p90": 0.00012132018455304216,
                  "p95": 0.0002466419246047735,
                  "p99": 0.00047991418978199363
                },
                "candidate_energy": 10.011864426884216,
                "cvrmse_percent": 65.62094926231839,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.34354355328123637,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 9.977587069733126,
                "relative_energy_error_percent": 0.34354355328123637,
                "rms_normalized_rmse_percent": 2.989563286839691,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.057770781219005585,
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "reference": 0.056138038635253906,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.38712495937943,
            "full": 264.86166601534933
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.46633308194578,
            "full": 264.85416607465595
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.39516704156995,
            "full": 262.1452499879524
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 126.6875839792192,
            "full": 267.6012919982895
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
            "identifier": "full_height_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003405285533517599,
                  "p50": 0.0,
                  "p90": 4.690792411565782e-05,
                  "p95": 0.00010261754505336285,
                  "p99": 0.00018045853357762098
                },
                "candidate_energy": 19.68087399599699,
                "cvrmse_percent": 12.484138547337679,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.012031586217604676,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 19.678506359538005,
                "relative_energy_error_percent": 0.012031586217604676,
                "rms_normalized_rmse_percent": 4.216944347793101,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0028013414703309536,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.0031418700236827135,
                  "rgb_channel": 0,
                  "sky_patch_index": 321
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010184012353420258,
                  "p50": 7.273180635536391e-08,
                  "p90": 7.199205283541252e-05,
                  "p95": 0.00014662405010312796,
                  "p99": 0.0002730514243012294
                },
                "candidate_energy": 17.089626634888837,
                "cvrmse_percent": 22.355477905902607,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.14353529069043586,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 17.114191539464326,
                "relative_energy_error_percent": 0.14353529069043586,
                "rms_normalized_rmse_percent": 1.3195197231574363,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.10373640060424805,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.10271799936890602,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 180.98549998831004,
            "full": 2150.6425829138607
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 178.12541709281504,
            "full": 2172.9369579115883
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 179.13508298806846,
            "full": 2149.6895420132205
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 188.5455830488354,
            "full": 2171.1195840034634
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
            "identifier": "full_height_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004346615169197321,
                  "p50": 0.0,
                  "p90": 4.6664499677717686e-05,
                  "p95": 0.00010503167868591845,
                  "p99": 0.0001996280552702956
                },
                "candidate_energy": 19.678944489815876,
                "cvrmse_percent": 13.321609845961138,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.03318056775943492,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 19.67241707014,
                "relative_energy_error_percent": 0.03318056775943492,
                "rms_normalized_rmse_percent": 4.499863565450577,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0036922264844179153,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.0041268880013376474,
                  "rgb_channel": 0,
                  "sky_patch_index": 358
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0012849979102611542,
                  "p50": 7.191377449089487e-08,
                  "p90": 7.546491106040791e-05,
                  "p95": 0.00015189393889158964,
                  "p99": 0.00028842015308327973
                },
                "candidate_energy": 17.100222520642838,
                "cvrmse_percent": 23.346451116326197,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.1830831650620367,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 17.13158757339759,
                "relative_energy_error_percent": 0.1830831650620367,
                "rms_normalized_rmse_percent": 1.3790452090430325,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.11101280152797699,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.11229779943823814,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 190.879917005077,
            "full": 2278.1937080435455
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 189.40087500959635,
            "full": 2240.9284580498934
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 181.98970903176814,
            "full": 2240.6839169561863
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 178.21745795663446,
            "full": 2285.928125027567
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
            "identifier": "full_height_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00022625294514000416,
                  "p50": 0.0,
                  "p90": 2.3205913021229227e-05,
                  "p95": 5.301600322127342e-05,
                  "p99": 0.0001024985103867948
                },
                "candidate_energy": 19.678977700991254,
                "cvrmse_percent": 6.810964089749381,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.015911241306716638,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 19.67584702949125,
                "relative_energy_error_percent": 0.015911241306716638,
                "rms_normalized_rmse_percent": 2.302299209596612,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00407403102144599,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.004300283966585994,
                  "rgb_channel": 0,
                  "sky_patch_index": 487
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010089501738548279,
                  "p50": 5.000000768973223e-08,
                  "p90": 4.1414023144170825e-05,
                  "p95": 8.316256571561098e-05,
                  "p99": 0.0001535741612315178
                },
                "candidate_energy": 17.110875215375277,
                "cvrmse_percent": 13.208119831042858,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.06561916187851585,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 17.099654565365363,
                "relative_energy_error_percent": 0.06561916187851585,
                "rms_normalized_rmse_percent": 0.779501575026566,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.1277182474732399,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.12670929729938507,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 280.97754099871963,
            "full": 3947.6535000139847
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 280.8071250328794,
            "full": 3919.79325003922
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 273.76337500754744,
            "full": 3898.5311669530347
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 286.13262495491654,
            "full": 4075.1302499556914
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
    "/content/suite-vulkan/full_height_glazing/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2641.1858749343082,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/full_height_glazing/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10350.489667034708,
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
        "identifier": "full_height_glazing_grid",
        "full_identifier": "full_height_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.03344188487030071,
            "cvrmse_percent": 0.9198089386492369,
            "rms_normalized_rmse_percent": 0.31092930559491244,
            "reference_energy": 19.680874874620713,
            "candidate_energy": 19.674293219103674,
            "relative_energy_error_percent": 0.03344188487030071,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.236345946788788e-08,
              "p95": 3.257300704717636e-07,
              "p99": 1.2091128155589104e-05,
              "maximum": 5.990988574922085e-05
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 360,
              "rgb_channel": 0,
              "reference": 0.0007348036160692573,
              "candidate": 0.0006748937303200364,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.2233203823291776,
            "cvrmse_percent": 42.84520068051874,
            "rms_normalized_rmse_percent": 2.5285147443469795,
            "reference_energy": 17.101802350445787,
            "candidate_energy": 16.892592516547136,
            "relative_energy_error_percent": 1.2233203823291618,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.2404444760250044e-07,
              "p90": 2.3622988373972474e-05,
              "p95": 3.910501254722476e-05,
              "p99": 7.723201997578144e-05,
              "maximum": 0.00465787947177887
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.13818517327308655,
              "candidate": 0.13352729380130768,
              "position": [
                3.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5866660767928975,
            "cvrmse_percent": 19.917655973181503,
            "rms_normalized_rmse_percent": 2.528150880402436,
            "reference_energy": 36.7826772250665,
            "candidate_energy": 36.566885735650814,
            "relative_energy_error_percent": 0.5866660767928806,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.2322863085501012e-07,
              "p90": 2.3646696354262536e-05,
              "p95": 3.840867429971695e-05,
              "p99": 7.643969729542732e-05,
              "maximum": 0.00465787947177887
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.13818517327308655,
              "candidate": 0.13352729380130768,
              "position": [
                3.5,
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
        "identifier": "full_height_glazing_grid",
        "full_identifier": "full_height_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.03344188487030071,
            "cvrmse_percent": 0.9198089386492369,
            "rms_normalized_rmse_percent": 0.31092930559491244,
            "reference_energy": 19.680874874620713,
            "candidate_energy": 19.674293219103674,
            "relative_energy_error_percent": 0.03344188487030071,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.236345946788788e-08,
              "p95": 3.257300704717636e-07,
              "p99": 1.2091128155589104e-05,
              "maximum": 5.990988574922085e-05
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 360,
              "rgb_channel": 0,
              "reference": 0.0007348036160692573,
              "candidate": 0.0006748937303200364,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 68.79439646395412,
            "cvrmse_percent": 702.8593682884223,
            "rms_normalized_rmse_percent": 32.120703812362486,
            "reference_energy": 10.007792243360717,
            "candidate_energy": 16.892592516547136,
            "relative_energy_error_percent": 68.79439646395413,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00022794441320002118,
              "p95": 0.0003136160667054355,
              "p99": 0.00047706475015729666,
              "maximum": 0.03127076476812363
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04920830577611923,
              "candidate": 0.08047907054424286,
              "position": [
                3.5,
                5.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 23.16782558925818,
            "cvrmse_percent": 236.92340911849334,
            "rms_normalized_rmse_percent": 32.1201087662902,
            "reference_energy": 29.688667117981428,
            "candidate_energy": 36.566885735650814,
            "relative_energy_error_percent": 23.1678255892582,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002276710547448603,
              "p95": 0.0003131583798676729,
              "p99": 0.0004770922241732478,
              "maximum": 0.03127076476812363
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04920830577611923,
              "candidate": 0.08047907054424286,
              "position": [
                3.5,
                5.5,
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
      "bias_percent": 0.150053150804471,
      "rms_normalized_error_percent": 0.21929118033320896,
      "absolute_error": {
        "p95": 0.29016749492385685,
        "p99": 0.31015803448954016,
        "maximum": 0.3198747754669782
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 41.89725913918019,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.21929118033320896
    },
    "overcast": {
      "bias_percent": 0.09623718711522487,
      "rms_normalized_error_percent": 0.14448297877712032,
      "absolute_error": {
        "p95": 0.10498106479644775,
        "p99": 0.12353105545043941,
        "maximum": 0.13350391387939453
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 27.146848678588867,
      "reference_fraction_of_uniform": 0.6479385495185852,
      "rms_normalized_to_uniform_percent": 0.09974702608790352
    },
    "horizon": {
      "bias_percent": 0.9688072751463287,
      "rms_normalized_error_percent": 1.7375702039009968,
      "absolute_error": {
        "p95": 0.21719347644487086,
        "p99": 0.26467800084899623,
        "maximum": 0.2683905129797841
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.91365289382185,
      "reference_fraction_of_uniform": 0.11727862382355345,
      "rms_normalized_to_uniform_percent": 0.16479260594391268
    },
    "north": {
      "bias_percent": -52.246261805188,
      "rms_normalized_error_percent": 92.22795486748586,
      "absolute_error": {
        "p95": 6.923926031277006e-05,
        "p99": 0.0001376722353640502,
        "maximum": 0.00015449574172521352
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.0270463210181333e-05,
      "reference_fraction_of_uniform": 4.838136078433308e-07,
      "rms_normalized_to_uniform_percent": 6.687753941688028e-05
    },
    "east": {
      "bias_percent": -0.03887527824641525,
      "rms_normalized_error_percent": 0.23887824908820074,
      "absolute_error": {
        "p95": 0.05001193284988403,
        "p99": 0.0827109336853027,
        "maximum": 0.08955955505371094
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.593806743621826,
      "reference_fraction_of_uniform": 0.18124829232692719,
      "rms_normalized_to_uniform_percent": 0.0477363324478859
    },
    "south": {
      "bias_percent": 0.19810962174584212,
      "rms_normalized_error_percent": 0.32072163653514113,
      "absolute_error": {
        "p95": 0.2894287109375,
        "p99": 0.2978220462799072,
        "maximum": 0.3019733428955078
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 29.12405776977539,
      "reference_fraction_of_uniform": 0.6951304078102112,
      "rms_normalized_to_uniform_percent": 0.2077802075494508
    },
    "west": {
      "bias_percent": 0.18363636537632208,
      "rms_normalized_error_percent": 0.2010730039348219,
      "absolute_error": {
        "p95": 0.036010026931762695,
        "p99": 0.04742792844772338,
        "maximum": 0.05003237724304199
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.678269386291504,
      "reference_fraction_of_uniform": 0.18326424062252045,
      "rms_normalized_to_uniform_percent": 0.0404643670700243
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
        "identifier": "full_height_glazing_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.0023346921741234194,
          "cvrmse_percent": 0.9565645360772947,
          "absolute_error_percentiles_lux": {
            "p50": 5.38189697265625,
            "p90": 49.818432617187504,
            "p95": 76.29791259765624,
            "p99": 150.07385742187418
          },
          "maximum_absolute_error_lux": 533.775390625,
          "worst": {
            "sensor_index": 12,
            "position": [
              2.5,
              5.5,
              0.75
            ],
            "hour_of_year": 8604.5,
            "foton_lux": 8266.046875,
            "radiance_lux": 7732.271484375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.0463318112633182,
            "maximum_error_percentage_points": 0.30452054794521644,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.019473085102848446,
            "maximum_error_percentage_points": 0.12988959257995703,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.01911339421613414,
            "maximum_error_percentage_points": 0.14123287671232987,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.1184208523592089,
            "maximum_error_percentage_points": 0.7686301369863031,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.12817351598173504,
            "maximum_error_percentage_points": 0.7908219178082199,
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
      "maximum_error_percentage_points": 0.004992241010270959,
      "metrics": {
        "da": [
          {
            "identifier": "full_height_glazing_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "full_height_glazing_grid",
            "maximum_error_percentage_points": 0.004992241010270959,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "full_height_glazing_grid",
            "maximum_error_percentage_points": 0.0045205479452086195,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "full_height_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "full_height_glazing_grid",
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
      "study_preparation_seconds": 0.39817926900013845,
      "weather_seconds": 0.27189773899999636,
      "metric_reduction_seconds": 0.3233576960001301,
      "write_seconds": 0.013230351000402152,
      "total_seconds": 0.6088683289999608,
      "cold_end_to_end_seconds": 1.0070475980000992,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0015974530001585663,
      "engine_upload_seconds": 0.065200782,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.031457622,
      "engine_annual_reduction_seconds": 0.00880867,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.031457622
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.39817926900013845,
      "weather_seconds": 0.2702839829998993,
      "metric_reduction_seconds": 0.3138277940001899,
      "write_seconds": 0.011946873999931995,
      "total_seconds": 0.5963648460001423,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.5963648460001423,
      "raw_export_seconds": 0.0014151440000205184,
      "engine_upload_seconds": 0.06543987,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 8.8e-08,
      "engine_annual_reduction_seconds": 0.00849445,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.029260999000143784,
      "full": 0.056700306000038836
    }
  },
  "elapsed_seconds": 4.575936404000004,
  "result_class": "passed"
}
```
