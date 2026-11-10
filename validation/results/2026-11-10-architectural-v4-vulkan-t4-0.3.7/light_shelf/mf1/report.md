# Foton report

Status: **passed**

```json
{
  "scene": "light_shelf",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "light_shelf",
    "category": "shading",
    "question": "Does a shelf block direct light and reflect light toward the ceiling?",
    "interactions": [
      "interior_shades",
      "exterior_shades",
      "shelf_reflection"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 2,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "b59cde3c05ed3b21b9262be28088ed99e4dbbc97772f5af68671453aceb138a5",
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 16584052180798691258,
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 16584052180798691258,
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
      "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/rcalc",
      "-e",
      "MF:1",
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.7)",
      "weather_id": "aff05f88fed2459a6796dca3cabd63daf743bc359ea5c7394adb01155f6785fb"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/gendaymtx",
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
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "da4bd6ca1d5da08752852b4c5a39e6ffc366f224c734a4f7ca46d2eaa89a5d0f",
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
          "maximum": 0.0006487497594207525,
          "p95": 1.819421231630201e-06,
          "p99": 6.817118264734745e-05
        },
        "bias_percent": 0.14096737470786652,
        "identifier": "light_shelf_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.1079347641335846,
        "worst_index": [
          4,
          70,
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
          "maximum": 0.000567261129617691,
          "p95": 3.852244408335535e-05,
          "p99": 0.00012510479427874088
        },
        "bias_percent": 0.20432191035875516,
        "identifier": "light_shelf_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.4799349692993243,
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
          "maximum": 0.0005790591239929199,
          "p95": 3.0259840423241202e-05,
          "p99": 9.92750283330679e-05
        },
        "bias_percent": -0.05944780624932982,
        "identifier": "light_shelf_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.4061871381486413,
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
          "rms_normalized_rmse_percent": 5.0
        },
        "grids": [
          {
            "identifier": "light_shelf_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006091694813221693,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.558109943289289e-06,
                  "p99": 0.00016904104268178344
                },
                "candidate_energy": 2.0056075447664625,
                "cvrmse_percent": 26.991448802734322,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.29327676539834907,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.011506826924233,
                "relative_energy_error_percent": 0.29327676539834907,
                "rms_normalized_rmse_percent": 4.1458542786854675,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005519788013771176,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.006128957495093346,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0025793984532356262,
                  "p50": 0.0,
                  "p90": 9.433069863007404e-06,
                  "p95": 5.1443954725982484e-05,
                  "p99": 0.0003626500547397882
                },
                "candidate_energy": 3.5297621893439555,
                "cvrmse_percent": 35.62456159944033,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.5924266713271342,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.5089740909392724,
                "relative_energy_error_percent": 0.5924266713271342,
                "rms_normalized_rmse_percent": 1.5140685944768906,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.24305369704961777,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.24047429859638214,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 111.6436249576509,
            "full": 250.96829200629145
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 103.81783405318856,
            "full": 220.74233298189938
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 105.63887504395097,
            "full": 242.27879103273153
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 101.89095791429281,
            "full": 225.0156659865752
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
            "identifier": "light_shelf_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00032666599145159125,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.0941873663105e-05,
                  "p99": 0.00013909232802689075
                },
                "candidate_energy": 2.017945850781871,
                "cvrmse_percent": 18.86718061486626,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.11100275740467588,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0201883155168616,
                "relative_energy_error_percent": 0.11100275740467588,
                "rms_normalized_rmse_percent": 2.9110344334629996,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0016793709946796298,
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "reference": 0.0013527050032280385,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009163320064544678,
                  "p50": 3.675042989925714e-06,
                  "p90": 3.3669355616439134e-05,
                  "p95": 5.9668804624379805e-05,
                  "p99": 0.00024341046810150146
                },
                "candidate_energy": 5.576002279765948,
                "cvrmse_percent": 13.937845764635668,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.04915288961011135,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.578744393839482,
                "relative_energy_error_percent": 0.049152889610111355,
                "rms_normalized_rmse_percent": 0.8462674835932861,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07429954782128334,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.07521587982773781,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.8333340138197,
            "full": 2432.211457984522
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 131.26433407887816,
            "full": 2416.504167020321
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.9388750018552,
            "full": 2430.4212919669226
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.86445804219693,
            "full": 2402.748416061513
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
            "identifier": "light_shelf_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005056937225162983,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.0199988921376626e-05,
                  "p99": 0.00016389205120503902
                },
                "candidate_energy": 2.0173182816315602,
                "cvrmse_percent": 24.611030247972025,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.09301626097487939,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.019196462682885,
                "relative_energy_error_percent": 0.0930162609748794,
                "rms_normalized_rmse_percent": 3.7934937376269944,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007256207522004843,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.007761901244521141,
                  "rgb_channel": 0,
                  "sky_patch_index": 48
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013386905193328857,
                  "p50": 3.5332182051206473e-06,
                  "p90": 3.17761496262392e-05,
                  "p95": 6.072399410186331e-05,
                  "p99": 0.0002728131366893649
                },
                "candidate_energy": 5.595629832989918,
                "cvrmse_percent": 15.747629444396269,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.06887197912358176,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.591778664355566,
                "relative_energy_error_percent": 0.06887197912358177,
                "rms_normalized_rmse_percent": 0.957810762280413,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.2595038563013077,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.26084254682064056,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 129.55504201818258,
            "full": 2636.4161670207977
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.50887498259544,
            "full": 2613.1177499191836
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.22279197908938,
            "full": 2566.2160840583965
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.99999999254942,
            "full": 2710.0739589659497
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
            "identifier": "light_shelf_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00024259602651000023,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.0227030770693053e-05,
                  "p99": 6.55630137771368e-05
                },
                "candidate_energy": 2.018946809530462,
                "cvrmse_percent": 10.527143964005727,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.009474453570870253,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0191381118333993,
                "relative_energy_error_percent": 0.009474453570870253,
                "rms_normalized_rmse_percent": 1.6260887284451864,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00767394551075995,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0074313494842499495,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013559013605117798,
                  "p50": 2.72998902062227e-06,
                  "p90": 2.3172055080067366e-05,
                  "p95": 4.033907753182571e-05,
                  "p99": 0.0001399400644004345
                },
                "candidate_energy": 5.59095213286162,
                "cvrmse_percent": 10.934445491242677,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.09159485595069702,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.585835794611903,
                "relative_energy_error_percent": 0.09159485595069702,
                "rms_normalized_rmse_percent": 0.665520400021435,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.2589161992073059,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.2602721005678177,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 193.27045790851116,
            "full": 4605.693417019211
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 182.90124996565282,
            "full": 4735.633583972231
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 184.29883406497538,
            "full": 4612.132792011835
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 195.61079191043973,
            "full": 4607.332209008746
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
    "/content/suite-vulkan-0.3.7/light_shelf/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 800.924125011079,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/light_shelf/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2783.378417021595,
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
        "identifier": "light_shelf_grid",
        "full_identifier": "light_shelf_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.1147824774010304,
            "cvrmse_percent": 6.940975383154455,
            "rms_normalized_rmse_percent": 1.0712061379532898,
            "reference_energy": 2.017501687460026,
            "candidate_energy": 2.015185949041552,
            "relative_energy_error_percent": 0.1147824774010304,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 8.02241993369518e-07,
              "p99": 4.02433070121333e-05,
              "maximum": 0.00020708958618342876
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 76,
              "rgb_channel": 0,
              "reference": 0.003619827562943101,
              "candidate": 0.003412737976759672,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.4526493019192561,
            "cvrmse_percent": 31.566044545745203,
            "rms_normalized_rmse_percent": 1.9228027987625962,
            "reference_energy": 5.5899347371464145,
            "candidate_energy": 5.508732589209515,
            "relative_energy_error_percent": 1.4526493019192561,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.326013135549147e-06,
              "p90": 4.5617009163834155e-05,
              "p95": 6.464103025791699e-05,
              "p99": 0.0001374548301100731,
              "maximum": 0.004379838705062866
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.2603074312210083,
              "candidate": 0.25592759251594543,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -1.0978453409775852,
            "cvrmse_percent": 23.16965097388175,
            "rms_normalized_rmse_percent": 1.9207271104398231,
            "reference_energy": 7.6074364246064405,
            "candidate_energy": 7.523918538251067,
            "relative_energy_error_percent": 1.0978453409775855,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.30037538940087e-06,
              "p90": 4.524012911133468e-05,
              "p95": 6.580490735359488e-05,
              "p99": 0.00013401079922914505,
              "maximum": 0.004379838705062866
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.2603074312210083,
              "candidate": 0.25592759251594543,
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
  "one_bounce_diagnostic": {
    "schema_version": 1,
    "passed": false,
    "matrix_shape": [
      36,
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
        "identifier": "light_shelf_grid",
        "full_identifier": "light_shelf_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.1147824774010304,
            "cvrmse_percent": 6.940975383154455,
            "rms_normalized_rmse_percent": 1.0712061379532898,
            "reference_energy": 2.017501687460026,
            "candidate_energy": 2.015185949041552,
            "relative_energy_error_percent": 0.1147824774010304,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 8.02241993369518e-07,
              "p99": 4.02433070121333e-05,
              "maximum": 0.00020708958618342876
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 76,
              "rgb_channel": 0,
              "reference": 0.003619827562943101,
              "candidate": 0.003412737976759672,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 56.92500902489355,
            "cvrmse_percent": 305.8007754802101,
            "rms_normalized_rmse_percent": 12.965833480521328,
            "reference_energy": 3.510423624277534,
            "candidate_energy": 5.508732589209515,
            "relative_energy_error_percent": 56.92500902489354,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5004999770317227e-05,
              "p90": 0.00023555064399261028,
              "p95": 0.00031649550364818416,
              "p99": 0.0005816100165247917,
              "maximum": 0.0142669677734375
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.24166062474250793,
              "candidate": 0.25592759251594543,
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
            "nmbe_percent": 36.10745648598711,
            "cvrmse_percent": 194.16174110338426,
            "rms_normalized_rmse_percent": 12.963675548270626,
            "reference_energy": 5.52792531173756,
            "candidate_energy": 7.523918538251067,
            "relative_energy_error_percent": 36.107456485987115,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5114999516517855e-05,
              "p90": 0.00023506245997850783,
              "p95": 0.00031700550607638434,
              "p99": 0.0005713102873414755,
              "maximum": 0.0142669677734375
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.24166062474250793,
              "candidate": 0.25592759251594543,
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
      "bias_percent": -0.3634769162952394,
      "rms_normalized_error_percent": 0.6121192381907333,
      "absolute_error": {
        "p95": 0.0993719774203079,
        "p99": 0.1087336277299041,
        "maximum": 0.11307658087867622
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.645958787207698,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.6121192381907333
    },
    "overcast": {
      "bias_percent": -0.5031581879974637,
      "rms_normalized_error_percent": 0.6699394896329599,
      "absolute_error": {
        "p95": 0.07269695401191711,
        "p99": 0.07358286380767823,
        "maximum": 0.07372188568115234
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.166271924972534,
      "reference_fraction_of_uniform": 0.560803234577179,
      "rms_normalized_to_uniform_percent": 0.38764017605750745
    },
    "horizon": {
      "bias_percent": 0.5729300495341931,
      "rms_normalized_error_percent": 2.4794277924236425,
      "absolute_error": {
        "p95": 0.054129832307127757,
        "p99": 0.0771146551351834,
        "maximum": 0.08451390683743254
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.037010996646046,
      "reference_fraction_of_uniform": 0.1836731431684638,
      "rms_normalized_to_uniform_percent": 0.3263183720988148
    },
    "north": {
      "bias_percent": -8.27442925209433,
      "rms_normalized_error_percent": 19.255663218594382,
      "absolute_error": {
        "p95": 0.003829183930065483,
        "p99": 0.004394103307276963,
        "maximum": 0.004555979743599892
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": true,
      "reference_mean": 0.010277451016008854,
      "reference_fraction_of_uniform": 0.0018203197978436947,
      "rms_normalized_to_uniform_percent": 0.02437554655290631
    },
    "east": {
      "bias_percent": -1.0487688752436528,
      "rms_normalized_error_percent": 1.545854817351155,
      "absolute_error": {
        "p95": 0.06061902642250061,
        "p99": 0.06399698257446289,
        "maximum": 0.06561517715454102
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.2427830696105957,
      "reference_fraction_of_uniform": 0.22011904418468475,
      "rms_normalized_to_uniform_percent": 0.3459695642258865
    },
    "south": {
      "bias_percent": -0.07283183731312837,
      "rms_normalized_error_percent": 0.5729720426102266,
      "absolute_error": {
        "p95": 0.07804954051971436,
        "p99": 0.09314635992050169,
        "maximum": 0.09958100318908691
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.139016151428223,
      "reference_fraction_of_uniform": 0.7330935597419739,
      "rms_normalized_to_uniform_percent": 0.43401941479796413
    },
    "west": {
      "bias_percent": -0.26675460555115993,
      "rms_normalized_error_percent": 0.7998925396008943,
      "absolute_error": {
        "p95": 0.032480545341968536,
        "p99": 0.035242876410484306,
        "maximum": 0.03662055730819702
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1937410831451416,
      "reference_fraction_of_uniform": 0.2114328294992447,
      "rms_normalized_to_uniform_percent": 0.17650688786682708
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
        "identifier": "light_shelf_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.5007356737279147,
          "cvrmse_percent": 4.062818983039243,
          "absolute_error_percentiles_lux": {
            "p50": 3.8717041015625,
            "p90": 30.67608032226564,
            "p95": 44.21891174316397,
            "p99": 76.3592596435545
          },
          "maximum_absolute_error_lux": 272.46240234375,
          "worst": {
            "sensor_index": 34,
            "position": [
              5.5,
              1.5,
              0.75
            ],
            "hour_of_year": 6086.5,
            "foton_lux": 4586.47021484375,
            "radiance_lux": 4858.9326171875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.7667427701674282,
            "maximum_error_percentage_points": 3.315616438356166,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.31122114657734873,
            "maximum_error_percentage_points": 1.3111883220389373,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.27895357686453554,
            "maximum_error_percentage_points": 1.3458904109589014,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.28774733637747374,
            "maximum_error_percentage_points": 1.3458904109589014,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.026122526636225257,
            "maximum_error_percentage_points": 0.19260273972602704,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 36.111111111111114,
          "radiance_percent": 38.888888888888886,
          "difference_percentage_points": 2.7777777777777715,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 1,
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
            "identifier": "light_shelf_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "light_shelf_grid",
            "maximum_error_percentage_points": 0.00491598886986111,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "light_shelf_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "light_shelf_grid",
            "maximum_error_percentage_points": 0.004794520547942938,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "light_shelf_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
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
      "study_preparation_seconds": 0.3850174970000353,
      "weather_seconds": 0.23308441200015295,
      "metric_reduction_seconds": 0.08792020199985018,
      "write_seconds": 0.012321515000166983,
      "total_seconds": 0.33366128199986633,
      "cold_end_to_end_seconds": 0.7186787789999016,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.001444462000108615,
      "engine_upload_seconds": 0.023851867,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.010162381,
      "engine_annual_reduction_seconds": 0.006216483,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.010162381
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3850174970000353,
      "weather_seconds": 0.23019681999994646,
      "metric_reduction_seconds": 0.07927951700003177,
      "write_seconds": 0.01304921399992054,
      "total_seconds": 0.3227871399999458,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.3227871399999458,
      "raw_export_seconds": 0.0018719160000273405,
      "engine_upload_seconds": 0.024280912,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 8.2e-08,
      "engine_annual_reduction_seconds": 0.00640852,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.023889958000154365,
      "full": 0.030056732000048214
    }
  },
  "elapsed_seconds": 2.7379889589999493,
  "result_class": "passed"
}
```
