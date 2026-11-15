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
  "model_sha256": "a200ec296e748d86dc65462199ac02a75a25b5f8f56a373d38905fe0197e93ba",
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
      "solver_version": "0.3.8",
      "scene_fingerprint": 3561854793510213323,
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
      "solver_version": "0.3.8",
      "scene_fingerprint": 3561854793510213323,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.8)",
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/52e717d2-b26e-4bbc-9536-f9b0a23834d6/scratchpad/refx/foton-references-corpus4-2026-11-03",
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
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton-0.3.8/validation/results/2026-11-14-architectural-v4-metal-0.3.8-release/full_height_glazing/mf2/oracle/scene.rad"
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
            "nmbe_percent": -0.03344046812493129,
            "cvrmse_percent": 0.9198083336649149,
            "rms_normalized_rmse_percent": 0.31092910108792493,
            "reference_energy": 19.680874874620713,
            "candidate_energy": 19.674293497931558,
            "relative_energy_error_percent": 0.03344046812493128,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.236345946788788e-08,
              "p95": 3.257300704717636e-07,
              "p99": 1.2091128155589104e-05,
              "maximum": 5.9909827541559935e-05
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 360,
              "rgb_channel": 0,
              "reference": 0.0007348036160692573,
              "candidate": 0.0006748937885276973,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.223333028137928,
            "cvrmse_percent": 42.845794724426824,
            "rms_normalized_rmse_percent": 2.5285498019206756,
            "reference_energy": 17.101802350445787,
            "candidate_energy": 16.892590353885918,
            "relative_energy_error_percent": 1.2233330281379122,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.240589995177288e-07,
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
            "nmbe_percent": -0.5866711983160622,
            "cvrmse_percent": 19.917932844962714,
            "rms_normalized_rmse_percent": 2.5281860237766542,
            "reference_energy": 36.7826772250665,
            "candidate_energy": 36.56688385181748,
            "relative_energy_error_percent": 0.5866711983160453,
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
            "nmbe_percent": -0.03344046812493129,
            "cvrmse_percent": 0.9198083336649149,
            "rms_normalized_rmse_percent": 0.31092910108792493,
            "reference_energy": 19.680874874620713,
            "candidate_energy": 19.674293497931558,
            "relative_energy_error_percent": 0.03344046812493128,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.236345946788788e-08,
              "p95": 3.257300704717636e-07,
              "p99": 1.2091128155589104e-05,
              "maximum": 5.9909827541559935e-05
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 360,
              "rgb_channel": 0,
              "reference": 0.0007348036160692573,
              "candidate": 0.0006748937885276973,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 68.79437485418079,
            "cvrmse_percent": 702.8581148496645,
            "rms_normalized_rmse_percent": 32.12064653015654,
            "reference_energy": 10.007792243360717,
            "candidate_energy": 16.892590353885918,
            "relative_energy_error_percent": 68.7943748541808,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00022794441320002118,
              "p95": 0.0003136160084977746,
              "p99": 0.00047706475015729666,
              "maximum": 0.03127075731754303
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04920830577611923,
              "candidate": 0.08047906309366226,
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
            "nmbe_percent": 23.167819243963773,
            "cvrmse_percent": 236.92298693799353,
            "rms_normalized_rmse_percent": 32.12005153056317,
            "reference_energy": 29.688667117981428,
            "candidate_energy": 36.56688385181748,
            "relative_energy_error_percent": 23.16781924396379,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00022767119444324648,
              "p95": 0.0003131583798676729,
              "p99": 0.00047709234058856964,
              "maximum": 0.03127075731754303
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04920830577611923,
              "candidate": 0.08047906309366226,
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
      "bias_percent": 0.15006745012307718,
      "rms_normalized_error_percent": 0.21929585518352762,
      "absolute_error": {
        "p95": 0.29016810444538343,
        "p99": 0.3101598828505484,
        "maximum": 0.31987660924114536
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 41.89725913918019,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.21929585518352762
    },
    "overcast": {
      "bias_percent": 0.09623650416883639,
      "rms_normalized_error_percent": 0.14449432610907184,
      "absolute_error": {
        "p95": 0.1049877405166626,
        "p99": 0.12353889942169186,
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
      "rms_normalized_to_uniform_percent": 0.09975485620357333
    },
    "horizon": {
      "bias_percent": 0.9692038711443987,
      "rms_normalized_error_percent": 1.737640514524433,
      "absolute_error": {
        "p95": 0.21719485177549758,
        "p99": 0.2646780227292565,
        "maximum": 0.268390512979785
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.91365289382185,
      "reference_fraction_of_uniform": 0.11727862382355345,
      "rms_normalized_to_uniform_percent": 0.1647992742620247
    },
    "north": {
      "bias_percent": -52.24626255688242,
      "rms_normalized_error_percent": 92.22795461590157,
      "absolute_error": {
        "p95": 6.923925758428595e-05,
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
      "bias_percent": -0.03888162341155579,
      "rms_normalized_error_percent": 0.23884018039657515,
      "absolute_error": {
        "p95": 0.049980878829956055,
        "p99": 0.08271336555480954,
        "maximum": 0.08956432342529297
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.593806743621826,
      "reference_fraction_of_uniform": 0.18124829232692719,
      "rms_normalized_to_uniform_percent": 0.04772872461571955
    },
    "south": {
      "bias_percent": 0.19811444041065418,
      "rms_normalized_error_percent": 0.32072602125279104,
      "absolute_error": {
        "p95": 0.2894439697265625,
        "p99": 0.2978219985961914,
        "maximum": 0.3019742965698242
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 29.12405776977539,
      "reference_fraction_of_uniform": 0.6951304078102112,
      "rms_normalized_to_uniform_percent": 0.20778304704194644
    },
    "west": {
      "bias_percent": 0.18374286616051685,
      "rms_normalized_error_percent": 0.2011985600381283,
      "absolute_error": {
        "p95": 0.03601032495498657,
        "p99": 0.0474279224872589,
        "maximum": 0.05003249645233154
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.678269386291504,
      "reference_fraction_of_uniform": 0.18326424062252045,
      "rms_normalized_to_uniform_percent": 0.04048963209984347
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
          "nmbe_percent": -0.0023217696311554213,
          "cvrmse_percent": 0.9566062502294821,
          "absolute_error_percentiles_lux": {
            "p50": 5.38116455078125,
            "p90": 49.826757812500006,
            "p95": 76.29603271484372,
            "p99": 150.1589208984371
          },
          "maximum_absolute_error_lux": 533.7763671875,
          "worst": {
            "sensor_index": 12,
            "position": [
              2.5,
              5.5,
              0.75
            ],
            "hour_of_year": 8604.5,
            "foton_lux": 8266.0478515625,
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
      "study_preparation_seconds": 0.007160249864682555,
      "weather_seconds": 0.08295312500558794,
      "metric_reduction_seconds": 0.12550633307546377,
      "write_seconds": 0.019414417212828994,
      "total_seconds": 0.22800479107536376,
      "cold_end_to_end_seconds": 0.2351650409400463,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.006686999928206205,
      "engine_upload_seconds": 0.000883209,
      "engine_acceleration_structure_seconds": 0.003749542,
      "engine_tracing_seconds": 0.06041116686537862,
      "engine_annual_reduction_seconds": 0.001635166583582759,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.06041116686537862
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007160249864682555,
      "weather_seconds": 0.0777413749601692,
      "metric_reduction_seconds": 0.05449666688218713,
      "write_seconds": 0.021613958990201354,
      "total_seconds": 0.15425766701810062,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.15425766701810062,
      "raw_export_seconds": 0.009280709084123373,
      "engine_upload_seconds": 6.725e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.005025124875828624,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01772741600871086,
      "full": 0.05808654217980802
    }
  },
  "elapsed_seconds": 1.3117949170991778,
  "result_class": "passed"
}
```
