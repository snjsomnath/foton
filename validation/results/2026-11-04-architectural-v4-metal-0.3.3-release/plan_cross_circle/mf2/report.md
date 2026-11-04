# Foton report

Status: **passed**

```json
{
  "scene": "plan_cross_circle",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_cross_circle",
    "category": "form",
    "question": "How does a circle opening illuminate a CROSS-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "cross",
    "window_profile": "circle"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 44,
    "floor_area": 63.0,
    "aperture_area": 1.44
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "019804f64d96a27c30d5737ddc3241a33ffe75140139f96c715faad87d065b08",
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
      "scene_fingerprint": 13351775639006016543,
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
      "scene_fingerprint": 13351775639006016543,
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
    "model_sha256": "142d088ac90f3a8f0330de530b77818a9e232543a4418489967bd291fca5ff69",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "9a3231f9777058abb1b3cf65cd66b5db7df4d557b41586683d412e16e4487cf8",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00017749506514519453,
          "p95": 0.0,
          "p99": 2.1212472347542644e-06
        },
        "bias_percent": 0.02100480878777493,
        "identifier": "plan_cross_circle_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3803222545004314,
        "worst_index": [
          33,
          485,
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
          "maximum": 0.0003413008525967598,
          "p95": 5.588748535956256e-06,
          "p99": 4.284386523067951e-05
        },
        "bias_percent": 0.1960840827952767,
        "identifier": "plan_cross_circle_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.042150811259087,
        "worst_index": [
          18,
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
          "maximum": 0.00032405275851488113,
          "p95": 4.889353476755787e-06,
          "p99": 3.806597669608891e-05
        },
        "bias_percent": -0.2127587419079376,
        "identifier": "plan_cross_circle_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.8717567042649124,
        "worst_index": [
          18,
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
            "identifier": "plan_cross_circle_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005411030142568052,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 8.299248293042183e-05
                },
                "candidate_energy": 2.392608289729651,
                "cvrmse_percent": 69.25392544914281,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.13811953040289068,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.389308188479845,
                "relative_energy_error_percent": 0.13811953040289066,
                "rms_normalized_rmse_percent": 7.20370702470474,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0013881329796276987,
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "reference": 0.0019292359938845038,
                  "rgb_channel": 0,
                  "sky_patch_index": 151
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010391650721430779,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.9111070034559816e-06,
                  "p99": 0.00012861128197982907
                },
                "candidate_energy": 0.5980738847852507,
                "cvrmse_percent": 401.8650570074842,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.3809193027656658,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.5958043510055528,
                "relative_energy_error_percent": 0.3809193027656658,
                "rms_normalized_rmse_percent": 7.818552880622185,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.017664114944636822,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.016624949872493744,
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.88287495821714,
            "full": 277.2949159843847
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.68820795603096,
            "full": 268.8293749233708
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.43033400550485,
            "full": 284.7423750208691
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.18620799668133,
            "full": 276.14591701421887
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.21062498167157,
            "full": 298.94729203078896
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.18949998915195,
            "full": 276.70299995224923
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 112.52475006040186,
            "full": 276.9343330292031
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 117.45154194068164,
            "full": 266.79212506860495
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
            "identifier": "plan_cross_circle_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00053962561651133,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.703836748376489e-05
                },
                "candidate_energy": 2.3923541575413765,
                "cvrmse_percent": 48.362938111025116,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.037160137330059,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.3932434901089437,
                "relative_energy_error_percent": 0.037160137330059,
                "rms_normalized_rmse_percent": 5.043703752065338,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0007510009163524956,
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "reference": 0.0012906265328638256,
                  "rgb_channel": 0,
                  "sky_patch_index": 92
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007381738978438079,
                  "p50": 0.0,
                  "p90": 3.8052800519494667e-06,
                  "p95": 8.08846425570664e-06,
                  "p99": 9.446809417568147e-05
                },
                "candidate_energy": 1.1302237483596969,
                "cvrmse_percent": 151.87921079126414,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.07221062579841282,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1294081956338111,
                "relative_energy_error_percent": 0.07221062579841282,
                "rms_normalized_rmse_percent": 4.588107510039747,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00033572211395949125,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": -0.0004024517838843167,
                  "rgb_channel": 0,
                  "sky_patch_index": 92
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 160.2907080668956,
            "full": 3262.854833039455
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 158.21287501603365,
            "full": 3266.475167009048
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.4077500263229,
            "full": 3252.191000035964
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 160.2438340196386,
            "full": 3299.330374924466
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
            "identifier": "plan_cross_circle_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00036394689232110977,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.694358358392492e-05
                },
                "candidate_energy": 2.3935453859667177,
                "cvrmse_percent": 42.60657503316757,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.16434993767243777,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.38961805019062,
                "relative_energy_error_percent": 0.16434993767243777,
                "rms_normalized_rmse_percent": 4.4375554031400215,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00476099899969995,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.0043970521073788404,
                  "rgb_channel": 0,
                  "sky_patch_index": 454
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00044333399273455143,
                  "p50": 0.0,
                  "p90": 3.8175776069238054e-06,
                  "p95": 7.827489753253758e-06,
                  "p99": 8.397380588576198e-05
                },
                "candidate_energy": 1.137135022961072,
                "cvrmse_percent": 134.647911224501,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.14144350252183288,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1387457047707166,
                "relative_energy_error_percent": 0.14144350252183285,
                "rms_normalized_rmse_percent": 4.088385937472941,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00016837799921631813,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": -0.0002749559935182333,
                  "rgb_channel": 0,
                  "sky_patch_index": 453
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 171.00225004833192,
            "full": 3513.4464589646086
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.3126249667257,
            "full": 3498.848333954811
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 163.4647079044953,
            "full": 3591.198042035103
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.03175000008196,
            "full": 3490.677708061412
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
            "identifier": "plan_cross_circle_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002115695970132947,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.2845884561538696e-05
                },
                "candidate_energy": 2.3918844669233295,
                "cvrmse_percent": 24.464588466021613,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.10167774282278308,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.389454923091762,
                "relative_energy_error_percent": 0.1016777428227831,
                "rms_normalized_rmse_percent": 2.5492407824794854,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003639993956312537,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.003851563553325832,
                  "rgb_channel": 0,
                  "sky_patch_index": 310
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00025639263913035393,
                  "p50": 0.0,
                  "p90": 2.685304934857413e-06,
                  "p95": 5.601548764389008e-06,
                  "p99": 4.658696707338095e-05
                },
                "candidate_energy": 1.129995927221998,
                "cvrmse_percent": 73.06066858582646,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.2378575280853121,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.132690115932622,
                "relative_energy_error_percent": 0.2378575280853121,
                "rms_normalized_rmse_percent": 2.210559048890684,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -6.713985931128263e-05,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.0001892527798190713,
                  "rgb_channel": 0,
                  "sky_patch_index": 91
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 237.53079096786678,
            "full": 6235.67545809783
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 220.58349999133497,
            "full": 6212.476250017062
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 232.38729208242148,
            "full": 6279.108541901223
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 232.70258400589228,
            "full": 6294.366542017087
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
    "/Users/ssanjay/GitHub/foton-0.3.3/validation/results/2026-11-04-architectural-v4-metal-0.3.3-release/plan_cross_circle/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4269.286000053398,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_circle/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 16573.765292065218,
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
      44,
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
        "identifier": "plan_cross_circle_grid",
        "full_identifier": "plan_cross_circle_grid",
        "start_sensor_index": 0,
        "sensor_count": 44,
        "stages": {
          "direct": {
            "nmbe_percent": -0.030676908593965675,
            "cvrmse_percent": 6.2490568409329885,
            "rms_normalized_rmse_percent": 0.6518144767278061,
            "reference_energy": 2.3918597072370176,
            "candidate_energy": 2.3911259586209326,
            "relative_energy_error_percent": 0.030676908593965675,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.2821255950257182e-06,
              "maximum": 9.685126133263111e-05
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 485,
              "rgb_channel": 0,
              "reference": 0.001293012173846364,
              "candidate": 0.001196160912513733,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.3926785874584604,
            "cvrmse_percent": 66.99265731943198,
            "rms_normalized_rmse_percent": 2.022326344285208,
            "reference_energy": 1.1301529954494036,
            "candidate_energy": 1.1144135966762594,
            "relative_energy_error_percent": 1.3926785874584602,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.382559953024611e-06,
              "p95": 6.4117675719899125e-06,
              "p99": 2.2661173716187477e-05,
              "maximum": 0.0006802286952733994
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.020883798599243164,
              "candidate": 0.020203569903969765,
              "position": [
                6.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.4677197040392361,
            "cvrmse_percent": 21.36961259157365,
            "rms_normalized_rmse_percent": 2.0103624370261155,
            "reference_energy": 3.522012702686421,
            "candidate_energy": 3.505539555297192,
            "relative_energy_error_percent": 0.46771970403923596,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.3818596421042457e-06,
              "p95": 6.380733793776017e-06,
              "p99": 2.2432999685406685e-05,
              "maximum": 0.0006802286952733994
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.020883798599243164,
              "candidate": 0.020203569903969765,
              "position": [
                6.5,
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
      44,
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
        "identifier": "plan_cross_circle_grid",
        "full_identifier": "plan_cross_circle_grid",
        "start_sensor_index": 0,
        "sensor_count": 44,
        "stages": {
          "direct": {
            "nmbe_percent": -0.030676908593965675,
            "cvrmse_percent": 6.2490568409329885,
            "rms_normalized_rmse_percent": 0.6518144767278061,
            "reference_energy": 2.3918597072370176,
            "candidate_energy": 2.3911259586209326,
            "relative_energy_error_percent": 0.030676908593965675,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.2821255950257182e-06,
              "maximum": 9.685126133263111e-05
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 485,
              "rgb_channel": 0,
              "reference": 0.001293012173846364,
              "candidate": 0.001196160912513733,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 86.9703398799448,
            "cvrmse_percent": 1424.2439938660266,
            "rms_normalized_rmse_percent": 27.63110312774822,
            "reference_energy": 0.5960376375161074,
            "candidate_energy": 1.1144135966762594,
            "relative_energy_error_percent": 86.97033987994482,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.1590000212891027e-05,
              "p95": 2.49700005952036e-05,
              "p99": 6.130128167569637e-05,
              "maximum": 0.0065737441182136536
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01736435666680336,
              "candidate": 0.023938100785017014,
              "position": [
                6.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 17.324631699715816,
            "cvrmse_percent": 284.096330691136,
            "rms_normalized_rmse_percent": 27.62939907287337,
            "reference_energy": 2.987897344753125,
            "candidate_energy": 3.505539555297192,
            "relative_energy_error_percent": 17.324631699715816,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.1553373724382254e-05,
              "p95": 2.491202758392319e-05,
              "p99": 6.271956954151392e-05,
              "maximum": 0.0065737441182136536
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01736435666680336,
              "candidate": 0.023938100785017014,
              "position": [
                6.5,
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
      "bias_percent": -0.017703311413043186,
      "rms_normalized_error_percent": 0.12484884437361157,
      "absolute_error": {
        "p95": 0.02347311908171719,
        "p99": 0.043598274574035686,
        "maximum": 0.048635493990744294
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.741631750997095,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.12484884437361157
    },
    "overcast": {
      "bias_percent": -0.047510203327559127,
      "rms_normalized_error_percent": 0.12748783227983235,
      "absolute_error": {
        "p95": 0.024262630939483654,
        "p99": 0.035506973266601564,
        "maximum": 0.03656005859375
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.526918649673462,
      "reference_fraction_of_uniform": 0.6753520369529724,
      "rms_normalized_to_uniform_percent": 0.09406057615552989
    },
    "horizon": {
      "bias_percent": 0.6039347976802535,
      "rms_normalized_error_percent": 1.8674900433211064,
      "absolute_error": {
        "p95": 0.01916193233375057,
        "p99": 0.02562982010193624,
        "maximum": 0.027969504277420176
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.31936418073523787,
      "reference_fraction_of_uniform": 0.08535425236599822,
      "rms_normalized_to_uniform_percent": 0.08213896928818595
    },
    "north": {
      "bias_percent": -89.91527305034626,
      "rms_normalized_error_percent": 102.90620226474529,
      "absolute_error": {
        "p95": 1.310056933050419e-05,
        "p99": 2.861676979591721e-05,
        "maximum": 3.431953882682137e-05
      },
      "worst_index": [
        13
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.530811798351351e-06,
      "reference_fraction_of_uniform": 6.763925171071605e-07,
      "rms_normalized_to_uniform_percent": 6.357132172657139e-05
    },
    "east": {
      "bias_percent": -0.16907082915995691,
      "rms_normalized_error_percent": 0.18313585014702988,
      "absolute_error": {
        "p95": 0.004137082397937777,
        "p99": 0.01721107661724091,
        "maximum": 0.0267181396484375
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5671685934066772,
      "reference_fraction_of_uniform": 0.1515832245349884,
      "rms_normalized_to_uniform_percent": 0.04095084643369566
    },
    "south": {
      "bias_percent": 0.03415195975602912,
      "rms_normalized_error_percent": 0.1409041705428026,
      "absolute_error": {
        "p95": 0.020020648837089542,
        "p99": 0.02452281951904297,
        "maximum": 0.027627944946289062
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.635396718978882,
      "reference_fraction_of_uniform": 0.7043442130088806,
      "rms_normalized_to_uniform_percent": 0.08918954189186185
    },
    "west": {
      "bias_percent": 0.001590934164865883,
      "rms_normalized_error_percent": 0.08070982916306332,
      "absolute_error": {
        "p95": 0.004024217091500759,
        "p99": 0.006617419421672822,
        "maximum": 0.00811004638671875
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5732945799827576,
      "reference_fraction_of_uniform": 0.15322047472000122,
      "rms_normalized_to_uniform_percent": 0.018136872779737127
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
        "identifier": "plan_cross_circle_grid",
        "sensor_count": 44,
        "illuminance": {
          "nmbe_percent": -0.05904162060496485,
          "cvrmse_percent": 3.1283396101857264,
          "absolute_error_percentiles_lux": {
            "p50": 0.5406961441040039,
            "p90": 7.828270912170414,
            "p95": 14.20388450622558,
            "p99": 44.508466796874984
          },
          "maximum_absolute_error_lux": 323.0078125,
          "worst": {
            "sensor_index": 33,
            "position": [
              6.5,
              0.5,
              0.75
            ],
            "hour_of_year": 2726.5,
            "foton_lux": 30339.26953125,
            "radiance_lux": 30662.27734375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.07707658779576577,
            "maximum_error_percentage_points": 0.8476712328767135,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1269772837203949,
            "maximum_error_percentage_points": 0.45532108898841983,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.24422789539227943,
            "maximum_error_percentage_points": 1.6691780821917774,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.24932752179327491,
            "maximum_error_percentage_points": 1.669178082191781,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0064445828144458405,
            "maximum_error_percentage_points": 0.08109589041095866,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 13.636363636363637,
          "radiance_percent": 13.636363636363637,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.272727272727273,
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
            "identifier": "plan_cross_circle_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_cross_circle_grid",
            "maximum_error_percentage_points": 0.0047586352204618265,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_cross_circle_grid",
            "maximum_error_percentage_points": 0.00479452054794538,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_cross_circle_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_cross_circle_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
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
      "study_preparation_seconds": 0.006646291934885085,
      "weather_seconds": 0.08269837498664856,
      "metric_reduction_seconds": 0.10866400005761534,
      "write_seconds": 0.015210542012937367,
      "total_seconds": 0.20670833298936486,
      "cold_end_to_end_seconds": 0.21335462492424995,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0016344999894499779,
      "engine_upload_seconds": 0.00080025,
      "engine_acceleration_structure_seconds": 0.002700542,
      "engine_tracing_seconds": 0.050397583399899304,
      "engine_annual_reduction_seconds": 0.002335916622541845,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.050397583399899304
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006646291934885085,
      "weather_seconds": 0.07857625000178814,
      "metric_reduction_seconds": 0.047115374938584864,
      "write_seconds": 0.02104008395690471,
      "total_seconds": 0.14686154189985245,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14686154189985245,
      "raw_export_seconds": 0.0018166250083595514,
      "engine_upload_seconds": 9.5709e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.001960541703738272,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.015865791938267648,
      "full": 0.07191183301620185
    }
  },
  "elapsed_seconds": 1.3893959580454975,
  "result_class": "passed"
}
```
