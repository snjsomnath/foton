# Foton report

Status: **passed**

```json
{
  "scene": "context_obstruction",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "context_obstruction",
    "category": "context",
    "question": "How much sky does a neighbouring facade obstruct?",
    "interactions": [
      "external_obstruction",
      "horizon_sky"
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
    "aperture_area": 2.999999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "1144f6c4469f21d1a9d9fad2976777ad39aaa104a315c152005e2e266477974f",
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
      "scene_fingerprint": 14793621846004041752,
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
      "scene_fingerprint": 14793621846004041752,
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
    "model_sha256": "983c1c58a88e88bfc0c380a3c61201837ebb9491fa195c8f63ddfc4ac7aa881b",
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
          "maximum": 0.00021733436733484268,
          "p95": 0.0,
          "p99": 0.0
        },
        "bias_percent": 0.09782542200423092,
        "identifier": "context_obstruction_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.0392927119777826,
        "worst_index": [
          17,
          447,
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
          "maximum": 0.0005549471825361252,
          "p95": 2.1602405468001962e-05,
          "p99": 4.996047937311232e-05
        },
        "bias_percent": 0.14899372180750456,
        "identifier": "context_obstruction_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.584879659103991,
        "worst_index": [
          21,
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
          "maximum": 0.0006390698254108429,
          "p95": 1.8664050003280863e-05,
          "p99": 4.344332410255447e-05
        },
        "bias_percent": 0.10973397949553523,
        "identifier": "context_obstruction_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.5084657718732304,
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
            "identifier": "context_obstruction_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005566710606217384,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.8502957084238005,
                "cvrmse_percent": 114.15349882545026,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.36249187838111735,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.8472245881002891,
                "relative_energy_error_percent": 0.36249187838111735,
                "rms_normalized_rmse_percent": 8.062611994624406,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0019369160290807486,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.002493587089702487,
                  "rgb_channel": 0,
                  "sky_patch_index": 514
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011777393519878387,
                  "p50": 0.0,
                  "p90": 1.6520802819286474e-05,
                  "p95": 3.273648508184124e-05,
                  "p99": 9.638986193749588e-05
                },
                "candidate_energy": 1.8625461798359133,
                "cvrmse_percent": 93.33821258521283,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.04820178984081096,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.8634443933862137,
                "relative_energy_error_percent": 0.048201789840810964,
                "rms_normalized_rmse_percent": 4.487991240201911,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.040136560797691345,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.041314300149679184,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 101.61899996455759,
            "full": 219.1450409591198
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 95.72041698265821,
            "full": 225.13237490784377
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 102.2358339978382,
            "full": 219.37795798294246
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 101.93674999754876,
            "full": 223.0854999506846
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
            "identifier": "context_obstruction_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002223360352218151,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.8482811717599361,
                "cvrmse_percent": 45.290503807045646,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.006528873659911302,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.8482257921696146,
                "relative_energy_error_percent": 0.006528873659911301,
                "rms_normalized_rmse_percent": 3.1949326117525794,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0018045100150629878,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.0015821739798411727,
                  "rgb_channel": 0,
                  "sky_patch_index": 514
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008584205061197281,
                  "p50": 2.6277034521626774e-06,
                  "p90": 1.933191633725074e-05,
                  "p95": 3.0120245355647057e-05,
                  "p99": 7.736205589026213e-05
                },
                "candidate_energy": 3.0090267404198308,
                "cvrmse_percent": 41.93939770465282,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.2398233721847597,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.0018276561077784,
                "relative_energy_error_percent": 0.23982337218475971,
                "rms_normalized_rmse_percent": 2.4012863756991805,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05020786076784134,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.05106628127396107,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.98854202125221,
            "full": 2276.1518330080435
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.67741601541638,
            "full": 2294.151333044283
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 125.36591698881239,
            "full": 2330.223917029798
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 126.64512498304248,
            "full": 2301.498082932085
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
            "identifier": "context_obstruction_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00023075105855241418,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.848597415441418,
                "cvrmse_percent": 46.89588815592457,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.04921773973246938,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.8481799604360276,
                "relative_energy_error_percent": 0.04921773973246938,
                "rms_normalized_rmse_percent": 3.3090406795006215,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001887039456050843,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.002117790514603257,
                  "rgb_channel": 0,
                  "sky_patch_index": 322
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006971005350351334,
                  "p50": 2.707600629037188e-06,
                  "p90": 1.933650488581409e-05,
                  "p95": 3.153202123939991e-05,
                  "p99": 7.384706623270176e-05
                },
                "candidate_energy": 3.0144653409062947,
                "cvrmse_percent": 42.307956863000896,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.22819414501350171,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.007602168851676,
                "relative_energy_error_percent": 0.2281941450135017,
                "rms_normalized_rmse_percent": 2.419173046266888,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.051328400149941444,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.05063129961490631,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.7660829992965,
            "full": 2494.387042010203
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 124.88004192709923,
            "full": 2498.049624962732
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.753917042166,
            "full": 2428.3834589878097
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.20366704184562,
            "full": 2464.6890830481425
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
            "identifier": "context_obstruction_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001305683981627226,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.8478609130461336,
                "cvrmse_percent": 24.989043214318595,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.0064931640174940375,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.8479159696207716,
                "relative_energy_error_percent": 0.0064931640174940375,
                "rms_normalized_rmse_percent": 1.7642351475204954,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004696621326729655,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.004566052928566933,
                  "rgb_channel": 0,
                  "sky_patch_index": 515
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00044278986752033234,
                  "p50": 1.9564202489164018e-06,
                  "p90": 1.3633657135869735e-05,
                  "p95": 2.1321451640687883e-05,
                  "p99": 4.9939495511353016e-05
                },
                "candidate_energy": 3.0152314356621517,
                "cvrmse_percent": 26.45613710713426,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.035649487010214365,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.016306733539313,
                "relative_energy_error_percent": 0.035649487010214365,
                "rms_normalized_rmse_percent": 1.518287638260227,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05024580471217632,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.050688594579696655,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 184.1285830596462,
            "full": 4314.89924993366
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 188.92670806962997,
            "full": 4321.11166708637
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 184.94962505064905,
            "full": 4323.345292010345
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.92816700786352,
            "full": 4316.161625087261
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
    "/Users/ssanjay/GitHub/foton-release-0.3.2/validation/results/2026-11-04-architectural-v4-metal-0.3.2-release/context_obstruction/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2778.568167006597,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10808.369542006403,
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
        "identifier": "context_obstruction_grid",
        "full_identifier": "context_obstruction_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.08745193411055277,
            "cvrmse_percent": 12.760766885276189,
            "rms_normalized_rmse_percent": 0.9006256228910481,
            "reference_energy": 0.8487971900273692,
            "candidate_energy": 0.8480549004680142,
            "relative_energy_error_percent": 0.08745193411055277,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 6.128521636128426e-05
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 447,
              "rgb_channel": 0,
              "reference": 0.0024364946875721216,
              "candidate": 0.0023752094712108374,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.0232626183578428,
            "cvrmse_percent": 28.39280591561234,
            "rms_normalized_rmse_percent": 1.6300570668744037,
            "reference_energy": 3.0148603364134132,
            "candidate_energy": 2.9840103975951973,
            "relative_energy_error_percent": 1.0232626183578428,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.9158460418111645e-06,
              "p90": 9.481413508183327e-06,
              "p95": 1.3955634130979888e-05,
              "p99": 2.8651149477809668e-05,
              "maximum": 0.0006610676646232605
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.018303917720913887,
              "candidate": 0.017642850056290627,
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
            "nmbe_percent": -0.8176767262980944,
            "cvrmse_percent": 22.08448898954061,
            "rms_normalized_rmse_percent": 1.6248500020628613,
            "reference_energy": 3.8636575264407824,
            "candidate_energy": 3.8320652980632115,
            "relative_energy_error_percent": 0.8176767262980944,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.9146359591104556e-06,
              "p90": 9.476102968619673e-06,
              "p95": 1.3923205187893473e-05,
              "p99": 2.849928569048643e-05,
              "maximum": 0.0006610676646232605
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.018303917720913887,
              "candidate": 0.017642850056290627,
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
        "identifier": "context_obstruction_grid",
        "full_identifier": "context_obstruction_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.08745193411055277,
            "cvrmse_percent": 12.760766885276189,
            "rms_normalized_rmse_percent": 0.9006256228910481,
            "reference_energy": 0.8487971900273692,
            "candidate_energy": 0.8480549004680142,
            "relative_energy_error_percent": 0.08745193411055277,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 6.128521636128426e-05
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 447,
              "rgb_channel": 0,
              "reference": 0.0024364946875721216,
              "candidate": 0.0023752094712108374,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 60.17591228495727,
            "cvrmse_percent": 838.2152583349897,
            "rms_normalized_rmse_percent": 40.31389283676716,
            "reference_energy": 1.8629582657138624,
            "candidate_energy": 2.9840103975951973,
            "relative_energy_error_percent": 60.17591228495726,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.254638265090762e-06,
              "p90": 2.561140245234129e-05,
              "p95": 3.4468517696950585e-05,
              "p99": 7.090429062373005e-05,
              "maximum": 0.009620048105716705
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.040725432336330414,
              "candidate": 0.05034548044204712,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 41.31308521755161,
            "cvrmse_percent": 575.8240287144149,
            "rms_normalized_rmse_percent": 40.312186563629794,
            "reference_energy": 2.7117554557412316,
            "candidate_energy": 3.8320652980632115,
            "relative_energy_error_percent": 41.31308521755161,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.251424338188372e-06,
              "p90": 2.5609999283915386e-05,
              "p95": 3.443999958108179e-05,
              "p99": 6.99295342201367e-05,
              "maximum": 0.009620048105716705
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.040725432336330414,
              "candidate": 0.05034548044204712,
              "position": [
                3.5,
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
      "bias_percent": -0.3290422892601271,
      "rms_normalized_error_percent": 0.40609713972119543,
      "absolute_error": {
        "p95": 0.06515541435796934,
        "p99": 0.08381609541759148,
        "maximum": 0.08785916425259188
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.4670531520102363,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.40609713972119543
    },
    "overcast": {
      "bias_percent": -0.3437841316275054,
      "rms_normalized_error_percent": 0.38203565827864,
      "absolute_error": {
        "p95": 0.04317772388458252,
        "p99": 0.0670208692550659,
        "maximum": 0.07355690002441406
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.5516459941864014,
      "reference_fraction_of_uniform": 0.7359696626663208,
      "rms_normalized_to_uniform_percent": 0.29860778207162075
    },
    "horizon": {
      "bias_percent": -0.3272349938238022,
      "rms_normalized_error_percent": 1.8029861115539005,
      "absolute_error": {
        "p95": 0.017941089483320863,
        "p99": 0.022290347251045547,
        "maximum": 0.02394257493437363
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3052949636653108,
      "reference_fraction_of_uniform": 0.0880560378742095,
      "rms_normalized_to_uniform_percent": 0.12142075467559459
    },
    "north": {
      "bias_percent": -0.46400004234495656,
      "rms_normalized_error_percent": 0.9334205035951565,
      "absolute_error": {
        "p95": 0.035805702209472656,
        "p99": 0.04948832988739013,
        "maximum": 0.05158567428588867
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.0563234090805054,
      "reference_fraction_of_uniform": 0.3046747148036957,
      "rms_normalized_to_uniform_percent": 0.2247738383821126
    },
    "east": {
      "bias_percent": -0.3227335058156585,
      "rms_normalized_error_percent": 0.8051016854738338,
      "absolute_error": {
        "p95": 0.02778056263923645,
        "p99": 0.03423259854316711,
        "maximum": 0.03511166572570801
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.7859581708908081,
      "reference_fraction_of_uniform": 0.22669342160224915,
      "rms_normalized_to_uniform_percent": 0.17850682502820805
    },
    "south": {
      "bias_percent": -0.0796171222508306,
      "rms_normalized_error_percent": 0.22663377350820663,
      "absolute_error": {
        "p95": 0.009239166975021362,
        "p99": 0.011846548318862912,
        "maximum": 0.01262664794921875
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5935534238815308,
      "reference_fraction_of_uniform": 0.17119824886322021,
      "rms_normalized_to_uniform_percent": 0.054353167368568996
    },
    "west": {
      "bias_percent": -0.15682503275023488,
      "rms_normalized_error_percent": 0.6447077201352781,
      "absolute_error": {
        "p95": 0.020813345909118652,
        "p99": 0.033865362405776964,
        "maximum": 0.03649163246154785
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.7881231307983398,
      "reference_fraction_of_uniform": 0.22731786966323853,
      "rms_normalized_to_uniform_percent": 0.14370054927417883
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
        "identifier": "context_obstruction_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.4945825364590237,
          "cvrmse_percent": 4.538162559826498,
          "absolute_error_percentiles_lux": {
            "p50": 0.8676605224609375,
            "p90": 8.754899597167968,
            "p95": 13.841218185424797,
            "p99": 29.513538055419367
          },
          "maximum_absolute_error_lux": 218.2412109375,
          "worst": {
            "sensor_index": 23,
            "position": [
              3.5,
              0.5,
              0.75
            ],
            "hour_of_year": 3828.5,
            "foton_lux": 8503.1044921875,
            "radiance_lux": 8721.345703125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.10716894977168961,
            "maximum_error_percentage_points": 0.6531506849315036,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.23593230592628092,
            "maximum_error_percentage_points": 0.7456546992035911,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.5752397260273975,
            "maximum_error_percentage_points": 1.7232876712328675,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.5749048706240483,
            "maximum_error_percentage_points": 1.7232876712328782,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0025190258751902925,
            "maximum_error_percentage_points": 0.030958904109589014,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 5.555555555555555,
          "radiance_percent": 5.555555555555555,
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
      "maximum_error_percentage_points": 0.004931506849314982,
      "metrics": {
        "da": [
          {
            "identifier": "context_obstruction_grid",
            "maximum_error_percentage_points": 0.00438356164384146,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "context_obstruction_grid",
            "maximum_error_percentage_points": 0.004879869434930129,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "context_obstruction_grid",
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "context_obstruction_grid",
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "context_obstruction_grid",
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
      "study_preparation_seconds": 0.009898625081405044,
      "weather_seconds": 0.08548629097640514,
      "metric_reduction_seconds": 0.1330996659817174,
      "write_seconds": 0.01797812490258366,
      "total_seconds": 0.2367197909625247,
      "cold_end_to_end_seconds": 0.24661841604392976,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.002087624976411462,
      "engine_upload_seconds": 0.000889917,
      "engine_acceleration_structure_seconds": 0.003069375,
      "engine_tracing_seconds": 0.057516708271577954,
      "engine_annual_reduction_seconds": 0.0015822916757315397,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.057516708271577954
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.009898625081405044,
      "weather_seconds": 0.0792703329352662,
      "metric_reduction_seconds": 0.054263792000710964,
      "write_seconds": 0.01738666696473956,
      "total_seconds": 0.15103441604878753,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.15103441604878753,
      "raw_export_seconds": 0.0016741659492254257,
      "engine_upload_seconds": 4.3709e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0014394583413377404,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.05262020800728351,
      "full": 0.06265054107643664
    }
  },
  "elapsed_seconds": 1.392371749971062,
  "result_class": "passed"
}
```
