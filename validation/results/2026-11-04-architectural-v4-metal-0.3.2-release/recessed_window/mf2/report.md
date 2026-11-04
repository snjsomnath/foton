# Foton report

Status: **passed**

```json
{
  "scene": "recessed_window",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "recessed_window",
    "category": "shading",
    "question": "How do deep opaque window reveals screen low and oblique sky?",
    "interactions": [
      "window_reveals",
      "combined_shading"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 4,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "fe1aed8b1cc3d47bc42b1168fc324580550f6954ab1be4dbb289b20789b7b830",
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
      "scene_fingerprint": 2657174224559240176,
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
      "scene_fingerprint": 2657174224559240176,
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
    "model_sha256": "9f85cc1156e8d6eff5e896536175b2f3ac04ee1627c0d0b9a899018e0dfb7777",
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
          "maximum": 0.00011665117926895618,
          "p95": 0.0,
          "p99": 6.0914026107639074e-06
        },
        "bias_percent": 0.016382771112224324,
        "identifier": "recessed_window_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8487273647977025,
        "worst_index": [
          17,
          404,
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
          "maximum": 0.00034428946673870087,
          "p95": 1.2532807886600494e-05,
          "p99": 7.904530502855778e-05
        },
        "bias_percent": 0.12397576573688968,
        "identifier": "recessed_window_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.025770584414129,
        "worst_index": [
          8,
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
          "maximum": 0.0003719944506883621,
          "p95": 1.1000200174748898e-05,
          "p99": 6.844897870905697e-05
        },
        "bias_percent": -0.022263414158204112,
        "identifier": "recessed_window_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.7616443370806185,
        "worst_index": [
          16,
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
            "identifier": "recessed_window_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005402149399742484,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00013839802704751492
                },
                "candidate_energy": 3.26298791105728,
                "cvrmse_percent": 46.78750591741924,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.092113985641286,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.265996350466594,
                "relative_energy_error_percent": 0.092113985641286,
                "rms_normalized_rmse_percent": 7.1883649720604215,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0039382349932566285,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.00339802005328238,
                  "rgb_channel": 0,
                  "sky_patch_index": 315
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008764530066400766,
                  "p50": 0.0,
                  "p90": 5.607656930806118e-06,
                  "p95": 1.657231587159913e-05,
                  "p99": 0.0002343695960007608
                },
                "candidate_energy": 1.3939515239347031,
                "cvrmse_percent": 197.28767029268846,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.21875401096773434,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3909088550254296,
                "relative_energy_error_percent": 0.2187540109677343,
                "rms_normalized_rmse_percent": 7.3828881184381085,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.000553942983970046,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.0003225100226700306,
                  "rgb_channel": 0,
                  "sky_patch_index": 155
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 109.82308408711106,
            "full": 239.97312493156642
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 107.47741698287427,
            "full": 242.1082080109045
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.44666698016226,
            "full": 263.04154202807695
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 117.170957964845,
            "full": 232.7499999664724
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
            "identifier": "recessed_window_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004805419594049454,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00011600472498685122
                },
                "candidate_energy": 3.2660742706630117,
                "cvrmse_percent": 38.56168879768284,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.004398053665394723,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.266217920679992,
                "relative_energy_error_percent": 0.0043980536653947236,
                "rms_normalized_rmse_percent": 5.931014981102826,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0039485294837504625,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.003467987524345517,
                  "rgb_channel": 0,
                  "sky_patch_index": 317
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006953547708690166,
                  "p50": 2.451333358521879e-08,
                  "p90": 9.71092667896303e-06,
                  "p95": 1.994017293327488e-05,
                  "p99": 0.0001774114789441228
                },
                "candidate_energy": 2.5426319218909903,
                "cvrmse_percent": 77.85818737898295,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.02333814052119302,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.542038657337038,
                "relative_energy_error_percent": 0.02333814052119302,
                "rms_normalized_rmse_percent": 4.171153078934456,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.011878515128046274,
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "reference": 0.01257386989891529,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.63525004126132,
            "full": 2401.303332997486
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.77729096729308,
            "full": 2454.112667008303
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.5131670916453,
            "full": 2422.50662506558
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.2718330193311,
            "full": 2453.8828749209642
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
            "identifier": "recessed_window_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00037308246828615665,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00011289457324892282
                },
                "candidate_energy": 3.2656377087969304,
                "cvrmse_percent": 39.146266325837736,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.028944835524559995,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.2646927488503934,
                "relative_energy_error_percent": 0.028944835524559995,
                "rms_normalized_rmse_percent": 6.01316086981292,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0029946145368739963,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.0026215320685878396,
                  "rgb_channel": 0,
                  "sky_patch_index": 260
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006141730409581214,
                  "p50": 2.450420311106427e-08,
                  "p90": 9.488343437169557e-06,
                  "p95": 1.8827786334441043e-05,
                  "p99": 0.0001694645034149289
                },
                "candidate_energy": 2.5468552031236555,
                "cvrmse_percent": 77.44334920264897,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.28675340985911846,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.55417939964606,
                "relative_energy_error_percent": 0.2867534098591184,
                "rms_normalized_rmse_percent": 4.17004798224882,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0003181965439580381,
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "reference": -0.00029597649700008333,
                  "rgb_channel": 0,
                  "sky_patch_index": 95
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.5339169492945,
            "full": 2604.071500012651
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.13779203034937,
            "full": 2606.997290975414
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.6258330512792,
            "full": 2576.754792011343
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 131.81312498636544,
            "full": 2594.4290830520913
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
            "identifier": "recessed_window_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00019625143613666296,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.772369331680238e-05
                },
                "candidate_energy": 3.266157132891749,
                "cvrmse_percent": 19.84396901162812,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.015684899363530003,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.2656449197725124,
                "relative_energy_error_percent": 0.015684899363530003,
                "rms_normalized_rmse_percent": 3.053416434350673,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0038068514550104737,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.004003102891147137,
                  "rgb_channel": 0,
                  "sky_patch_index": 408
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003658253699541092,
                  "p50": 4.703974809672218e-08,
                  "p90": 6.720199053233966e-06,
                  "p95": 1.2714146578218788e-05,
                  "p99": 9.092265099752694e-05
                },
                "candidate_energy": 2.5494759019633015,
                "cvrmse_percent": 41.451141807578864,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.07766092960870725,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.547497491729466,
                "relative_energy_error_percent": 0.07766092960870725,
                "rms_normalized_rmse_percent": 2.2269334773512974,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.018580185249447823,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.018214359879493713,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 193.74245894141495,
            "full": 4575.697707943618
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 198.30150005873293,
            "full": 4504.765667021275
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 203.33395805209875,
            "full": 4563.538208953105
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 192.49300006777048,
            "full": 4585.293167037889
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
    "/Users/ssanjay/GitHub/foton-release-0.3.2/validation/results/2026-11-04-architectural-v4-metal-0.3.2-release/recessed_window/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2773.2348749414086,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/recessed_window/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10506.412541959435,
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
        "identifier": "recessed_window_grid",
        "full_identifier": "recessed_window_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.017250019829816818,
            "cvrmse_percent": 3.4046051291255948,
            "rms_normalized_rmse_percent": 0.5243186789102512,
            "reference_energy": 3.26736506296038,
            "candidate_energy": 3.267928684081653,
            "relative_energy_error_percent": 0.017250019829816818,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 4.787340003531426e-06,
              "maximum": 5.839118966832757e-05
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 415,
              "rgb_channel": 0,
              "reference": 0.0008395466138608754,
              "candidate": 0.0007811554241925478,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.9871304551644092,
            "cvrmse_percent": 44.063116277853005,
            "rms_normalized_rmse_percent": 2.365850877056425,
            "reference_energy": 2.5470226713455695,
            "candidate_energy": 2.5218802348567753,
            "relative_energy_error_percent": 0.9871304551644093,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.529403696551526e-08,
              "p90": 7.1080603447626345e-06,
              "p95": 1.2266191333765164e-05,
              "p99": 3.957119770348072e-05,
              "maximum": 0.0007553212344646454
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017631560564041138,
              "candidate": 0.016876239329576492,
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
            "nmbe_percent": -0.42272405093491694,
            "cvrmse_percent": 19.32150579501412,
            "rms_normalized_rmse_percent": 2.3682323362357565,
            "reference_energy": 5.814387734305949,
            "candidate_energy": 5.789808918938428,
            "relative_energy_error_percent": 0.42272405093491694,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.529403696551526e-08,
              "p90": 7.113911851774903e-06,
              "p95": 1.233583316206932e-05,
              "p99": 3.914994886144996e-05,
              "maximum": 0.0007553212344646454
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017631560564041138,
              "candidate": 0.016876239329576492,
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
        "identifier": "recessed_window_grid",
        "full_identifier": "recessed_window_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.017250019829816818,
            "cvrmse_percent": 3.4046051291255948,
            "rms_normalized_rmse_percent": 0.5243186789102512,
            "reference_energy": 3.26736506296038,
            "candidate_energy": 3.267928684081653,
            "relative_energy_error_percent": 0.017250019829816818,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 4.787340003531426e-06,
              "maximum": 5.839118966832757e-05
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 415,
              "rgb_channel": 0,
              "reference": 0.0008395466138608754,
              "candidate": 0.0007811554241925478,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.48804078144937,
            "cvrmse_percent": 850.8922856729962,
            "rms_normalized_rmse_percent": 31.824738177982425,
            "reference_energy": 1.3895572534686522,
            "candidate_energy": 2.5218802348567753,
            "relative_energy_error_percent": 81.48804078144936,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.0166998951463075e-05,
              "p95": 5.935209082963411e-05,
              "p99": 0.00013590382877737284,
              "maximum": 0.005040153861045837
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.007925746031105518,
              "candidate": 0.012965899892151356,
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
            "nmbe_percent": 24.326937954552424,
            "cvrmse_percent": 253.89447025294191,
            "rms_normalized_rmse_percent": 31.82482638403538,
            "reference_energy": 4.656922316429032,
            "candidate_energy": 5.789808918938428,
            "relative_energy_error_percent": 24.326937954552424,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.017999890493229e-05,
              "p95": 5.946657620370388e-05,
              "p99": 0.00013506959658116102,
              "maximum": 0.005040153861045837
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.007925746031105518,
              "candidate": 0.012965899892151356,
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
      "bias_percent": 0.2453961617730458,
      "rms_normalized_error_percent": 0.28577339134663987,
      "absolute_error": {
        "p95": 0.05677566750877239,
        "p99": 0.09442925092490073,
        "maximum": 0.11192904674318527
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.830341803337491,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.28577339134663987
    },
    "overcast": {
      "bias_percent": 0.20636355368951353,
      "rms_normalized_error_percent": 0.20982132364885178,
      "absolute_error": {
        "p95": 0.031374722719192505,
        "p99": 0.039580321311950675,
        "maximum": 0.04179048538208008
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.0272111892700195,
      "reference_fraction_of_uniform": 0.5896061062812805,
      "rms_normalized_to_uniform_percent": 0.13749315185169123
    },
    "horizon": {
      "bias_percent": 0.8768819177430114,
      "rms_normalized_error_percent": 2.170776822227396,
      "absolute_error": {
        "p95": 0.05280945863537839,
        "p99": 0.07713993507461686,
        "maximum": 0.08706643067727193
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1330189286890395,
      "reference_fraction_of_uniform": 0.16588026797361966,
      "rms_normalized_to_uniform_percent": 0.22391365634621102
    },
    "north": {
      "bias_percent": -62.70336871509916,
      "rms_normalized_error_percent": 93.54303943488603,
      "absolute_error": {
        "p95": 9.48726289848878e-05,
        "p99": 0.000157374428731316,
        "maximum": 0.000190431735063612
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.3300546672544442e-05,
      "reference_fraction_of_uniform": 3.411329544178443e-06,
      "rms_normalized_to_uniform_percent": 0.00036582231236775245
    },
    "east": {
      "bias_percent": 0.019393766603307203,
      "rms_normalized_error_percent": 0.26141361104636174,
      "absolute_error": {
        "p95": 0.010932683944702148,
        "p99": 0.013389158248901363,
        "maximum": 0.014219284057617188
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.144587755203247,
      "reference_fraction_of_uniform": 0.16757400333881378,
      "rms_normalized_to_uniform_percent": 0.048418210624440204
    },
    "south": {
      "bias_percent": 0.2981254037100478,
      "rms_normalized_error_percent": 0.34879513154185504,
      "absolute_error": {
        "p95": 0.058326125144958496,
        "p99": 0.09392791986465447,
        "maximum": 0.11125850677490234
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.35506534576416,
      "reference_fraction_of_uniform": 0.7840113043785095,
      "rms_normalized_to_uniform_percent": 0.26488465346532303
    },
    "west": {
      "bias_percent": 0.08838429191162517,
      "rms_normalized_error_percent": 0.3477248652592246,
      "absolute_error": {
        "p95": 0.016336411237716675,
        "p99": 0.01724776029586792,
        "maximum": 0.017310261726379395
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1632853746414185,
      "reference_fraction_of_uniform": 0.17031145095825195,
      "rms_normalized_to_uniform_percent": 0.06505428582197378
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
        "identifier": "recessed_window_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.11736779004774976,
          "cvrmse_percent": 2.5374257915873737,
          "absolute_error_percentiles_lux": {
            "p50": 1.4112777709960938,
            "p90": 16.632452392578124,
            "p95": 26.672998046874966,
            "p99": 62.8881115722652
          },
          "maximum_absolute_error_lux": 384.6201171875,
          "worst": {
            "sensor_index": 23,
            "position": [
              3.5,
              0.5,
              0.75
            ],
            "hour_of_year": 4934.5,
            "foton_lux": 12198.05078125,
            "radiance_lux": 12582.6708984375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.3894140030441401,
            "maximum_error_percentage_points": 2.2231506849315075,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.18711494662785297,
            "maximum_error_percentage_points": 0.8203717321673594,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.17112633181126233,
            "maximum_error_percentage_points": 1.285890410958899,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.16421613394216214,
            "maximum_error_percentage_points": 1.179452054794524,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.02007229832572312,
            "maximum_error_percentage_points": 0.10643835616438357,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 25.0,
          "radiance_percent": 25.0,
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
      "maximum_error_percentage_points": 0.004944616866438878,
      "metrics": {
        "da": [
          {
            "identifier": "recessed_window_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "recessed_window_grid",
            "maximum_error_percentage_points": 0.004944616866438878,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "recessed_window_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "recessed_window_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "recessed_window_grid",
            "maximum_error_percentage_points": 0.004794520547945602,
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
      "study_preparation_seconds": 0.006437208037823439,
      "weather_seconds": 0.0840761250583455,
      "metric_reduction_seconds": 0.12186029204167426,
      "write_seconds": 0.02481387509033084,
      "total_seconds": 0.23088579101022333,
      "cold_end_to_end_seconds": 0.23732299904804677,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.003111208090558648,
      "engine_upload_seconds": 0.000906125,
      "engine_acceleration_structure_seconds": 0.00314525,
      "engine_tracing_seconds": 0.058383041992783546,
      "engine_annual_reduction_seconds": 0.001564375008456409,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.058383041992783546
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006437208037823439,
      "weather_seconds": 0.0814960419666022,
      "metric_reduction_seconds": 0.04975391610059887,
      "write_seconds": 0.02101212495472282,
      "total_seconds": 0.1528409169986844,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1528409169986844,
      "raw_export_seconds": 0.00189362489618361,
      "engine_upload_seconds": 5.6958e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0031799583230167627,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.024541374994441867,
      "full": 0.06507162505295128
    }
  },
  "elapsed_seconds": 1.3966737920418382,
  "result_class": "passed"
}
```
