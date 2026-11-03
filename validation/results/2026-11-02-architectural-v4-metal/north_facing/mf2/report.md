# Foton report

Status: **passed**

```json
{
  "scene": "north_facing",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "north_facing",
    "category": "orientation",
    "question": "Is north-facing glazing assigned to the correct sky patches?",
    "interactions": [
      "north_glazing",
      "sky_patch_order"
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
    "aperture_area": 2.999999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "fedfba254fafb32ea9dc9cd12b81309ec91ce48af5909fb6c71b81d68f7cd9c9",
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 14256008842406293211,
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 14256008842406293211,
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
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 16384,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "north_facing_grid",
        "bias_percent": -0.00293816625518776,
        "rms_normalized_error_percent": 0.7961676481493521,
        "absolute_error": {
          "p95": 3.9814040064811707e-08,
          "p99": 8.134287782013416e-06,
          "maximum": 0.00011883559636771679
        },
        "worst_index": [
          7,
          341,
          0
        ],
        "passed": true
      }
    ],
    "samples_per_patch": [
      256,
      1024
    ]
  },
  "depth_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "north_facing_grid",
        "bias_percent": 0.09522902442571012,
        "rms_normalized_error_percent": 1.7469773639767783,
        "absolute_error": {
          "p95": 2.2345608158502728e-05,
          "p99": 0.0001028731931000948,
          "maximum": 0.0003822408616542816
        },
        "worst_index": [
          8,
          0,
          0
        ],
        "passed": true
      }
    ]
  },
  "sample_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "north_facing_grid",
        "bias_percent": -0.05757993711227416,
        "rms_normalized_error_percent": 1.3969178764046395,
        "absolute_error": {
          "p95": 1.8463193555362523e-05,
          "p99": 8.057616651058197e-05,
          "maximum": 0.0003849044442176819
        },
        "worst_index": [
          12,
          0,
          0
        ],
        "passed": true
      }
    ]
  },
  "oracle_levels": [
    {
      "samples": 20000,
      "material_bounces": 1,
      "repeatability": {
        "schema_version": 1,
        "run_count": 8,
        "half_run_count": 4,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "north_facing_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.019272769578318593,
                "cvrmse_percent": 32.716332551583776,
                "rms_normalized_rmse_percent": 6.3094701692338475,
                "reference_energy": 6.023027715422359,
                "candidate_energy": 6.02418851967559,
                "relative_energy_error_percent": 0.019272769578318593,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3138331016525626e-05,
                  "p99": 0.0001754812547005713,
                  "maximum": 0.0004833220737054944
                },
                "worst": {
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "sky_patch_index": 246,
                  "rgb_channel": 0,
                  "reference": 0.0031596890185028315,
                  "candidate": 0.003643011092208326
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.32601585843062053,
                "cvrmse_percent": 151.2032954493924,
                "rms_normalized_rmse_percent": 5.631705340606752,
                "reference_energy": 2.006016543362435,
                "candidate_energy": 2.012556475416538,
                "relative_energy_error_percent": 0.32601585843062053,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.154832524567664e-06,
                  "p95": 4.670699127018452e-05,
                  "p99": 0.00025789514984353445,
                  "maximum": 0.000924224965274334
                },
                "worst": {
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0159612400457263,
                  "candidate": 0.015037015080451965
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          }
        ]
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 106.7925828974694,
            "full": 214.79445905424654
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 113.33804100286216,
            "full": 224.08154199365526
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 102.50454093329608,
            "full": 215.99129203241318
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 102.9798339586705,
            "full": 209.28229193668813
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 105.65091704484075,
            "full": 241.3214580155909
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 107.97187499701977,
            "full": 215.14583297539502
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 102.11262502707541,
            "full": 213.0782500607893
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 111.3084580283612,
            "full": 213.3697080425918
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 8,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "north_facing_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.09072714181628246,
                "cvrmse_percent": 26.978451161281235,
                "rms_normalized_rmse_percent": 5.197164986934721,
                "reference_energy": 6.010577600809029,
                "candidate_energy": 6.0160308260728925,
                "relative_energy_error_percent": 0.09072714181628244,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3092157789506018e-05,
                  "p99": 0.0001408809912391007,
                  "maximum": 0.0003497386060189456
                },
                "worst": {
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "sky_patch_index": 179,
                  "rgb_channel": 0,
                  "reference": 0.0005367411067709327,
                  "candidate": 0.0008864797127898782
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.089260068333977,
                "cvrmse_percent": 62.797322608490575,
                "rms_normalized_rmse_percent": 3.381143842589907,
                "reference_energy": 3.7449840106657533,
                "candidate_energy": 3.7416412353787365,
                "relative_energy_error_percent": 0.089260068333977,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.9482578156603267e-08,
                  "p90": 1.3435072651191188e-05,
                  "p95": 3.5119010135531425e-05,
                  "p99": 0.00020360015332698822,
                  "maximum": 0.0007142601534724236
                },
                "worst": {
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.022885344922542572,
                  "candidate": 0.023599605076014996
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 136.23954099602997,
            "full": 2238.3672919822857
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 133.97095794789493,
            "full": 2273.55395804625
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 131.9304999196902,
            "full": 2223.1578750070184
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 133.41529096942395,
            "full": 2254.4911250006407
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 12,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "north_facing_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.13546284792585092,
                "cvrmse_percent": 24.104564764426474,
                "rms_normalized_rmse_percent": 4.6473122886380525,
                "reference_energy": 6.022401746113246,
                "candidate_energy": 6.014243629194425,
                "relative_energy_error_percent": 0.13546284792585095,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2496897145174444e-05,
                  "p99": 0.00013312169176060706,
                  "maximum": 0.00036651274422183633
                },
                "worst": {
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "sky_patch_index": 113,
                  "rgb_channel": 0,
                  "reference": 0.0011600549914874136,
                  "candidate": 0.0007935422472655773
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.07111012544609883,
                "cvrmse_percent": 59.9732885042929,
                "rms_normalized_rmse_percent": 3.2243194017025045,
                "reference_energy": 3.74625325887925,
                "candidate_energy": 3.7489172242711675,
                "relative_energy_error_percent": 0.07111012544609882,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.9857695932046227e-08,
                  "p90": 1.3215139324529483e-05,
                  "p95": 3.737499355338514e-05,
                  "p99": 0.0001940201036632061,
                  "maximum": 0.0005714177968911827
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 61,
                  "rgb_channel": 0,
                  "reference": 3.966648364439607e-05,
                  "candidate": 0.0006110842805355787
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 135.36070892587304,
            "full": 2496.593000018038
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 136.45570899825543,
            "full": 2430.541165987961
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 152.16754202265292,
            "full": 2442.8492499282584
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 143.07516696862876,
            "full": 2459.5944170141593
          }
        }
      ]
    },
    {
      "samples": 80000,
      "material_bounces": 12,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "north_facing_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.06234659776262754,
                "cvrmse_percent": 14.323131844096864,
                "rms_normalized_rmse_percent": 2.7601636435859005,
                "reference_energy": 6.01131818654585,
                "candidate_energy": 6.0150660389158475,
                "relative_energy_error_percent": 0.06234659776262754,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1487543815746903e-05,
                  "p99": 7.952901069074869e-05,
                  "maximum": 0.00017550104530528188
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 121,
                  "rgb_channel": 0,
                  "reference": 0.0009827322501223534,
                  "candidate": 0.0008072312048170716
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.1366899452772172,
                "cvrmse_percent": 35.41327655549626,
                "rms_normalized_rmse_percent": 1.9086992213855865,
                "reference_energy": 3.749655322422491,
                "candidate_energy": 3.7445299206141875,
                "relative_energy_error_percent": 0.13668994527721717,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.480562955042842e-08,
                  "p90": 9.306274296250202e-06,
                  "p95": 2.3539061658084393e-05,
                  "p99": 0.00011087267193943262,
                  "maximum": 0.0004586242139339447
                },
                "worst": {
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.020386824384331703,
                  "candidate": 0.01992820017039776
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          }
        ]
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 195.54941693786532,
            "full": 4254.610541975126
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 202.9994580661878,
            "full": 4179.489083006047
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 190.08620898239315,
            "full": 4252.788165933453
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 208.0828748876229,
            "full": 4259.642792050727
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 2592.8192499559373,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/north_facing/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 10967.721957946196,
      "worker_pool_size": 12,
      "invocation_count": 3
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
        "identifier": "north_facing_grid",
        "full_identifier": "north_facing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.0036633636174217632,
            "cvrmse_percent": 2.3580461345024015,
            "rms_normalized_rmse_percent": 0.4548746880656067,
            "reference_energy": 6.016047347356562,
            "candidate_energy": 6.016267737046292,
            "relative_energy_error_percent": 0.003663363617421763,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.5133991837501526e-08,
              "p99": 5.79573679715395e-06,
              "maximum": 9.540095925331116e-05
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 295,
              "rgb_channel": 0,
              "reference": 0.0028306380845606327,
              "candidate": 0.0027352371253073215,
              "position": [
                1.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.2480315500748032,
            "cvrmse_percent": 60.70849817900285,
            "rms_normalized_rmse_percent": 3.2694131314433155,
            "reference_energy": 3.7442373928352115,
            "candidate_energy": 3.753524282879141,
            "relative_energy_error_percent": 0.24803155007480324,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 3.427417177590543e-05,
              "p95": 5.131680518388748e-05,
              "p99": 9.682335394245456e-05,
              "maximum": 0.0012566102668642998
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014872239902615547,
              "candidate": 0.013615629635751247,
              "position": [
                0.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.09740781121384272,
            "cvrmse_percent": 23.272341068644316,
            "rms_normalized_rmse_percent": 3.2670779603282485,
            "reference_energy": 9.760284740191773,
            "candidate_energy": 9.769792019925433,
            "relative_energy_error_percent": 0.09740781121384272,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 3.435202524997298e-05,
              "p95": 5.119628622196615e-05,
              "p99": 9.660085197538137e-05,
              "maximum": 0.0012566102668642998
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014872239902615547,
              "candidate": 0.013615629635751247,
              "position": [
                0.5,
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
        "identifier": "north_facing_grid",
        "full_identifier": "north_facing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.0036633636174217632,
            "cvrmse_percent": 2.3580461345024015,
            "rms_normalized_rmse_percent": 0.4548746880656067,
            "reference_energy": 6.016047347356562,
            "candidate_energy": 6.016267737046292,
            "relative_energy_error_percent": 0.003663363617421763,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.5133991837501526e-08,
              "p99": 5.79573679715395e-06,
              "maximum": 9.540095925331116e-05
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 295,
              "rgb_channel": 0,
              "reference": 0.0028306380845606327,
              "candidate": 0.0027352371253073215,
              "position": [
                1.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 86.10850314679492,
            "cvrmse_percent": 945.5963494828321,
            "rms_normalized_rmse_percent": 35.35117381774825,
            "reference_energy": 2.0168472796315555,
            "candidate_energy": 3.753524282879141,
            "relative_energy_error_percent": 86.10850314679492,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.258512188424014e-05,
              "p95": 9.567976485413965e-05,
              "p99": 0.00017369375564157963,
              "maximum": 0.008737378753721714
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015470660291612148,
              "candidate": 0.024208039045333862,
              "position": [
                5.5,
                4.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.62231018320421,
            "cvrmse_percent": 237.41552442980029,
            "rms_normalized_rmse_percent": 35.351367809760156,
            "reference_energy": 8.032894626988117,
            "candidate_energy": 9.769792019925433,
            "relative_energy_error_percent": 21.62231018320421,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.255028901023252e-05,
              "p95": 9.567976485413965e-05,
              "p99": 0.00017345743253827095,
              "maximum": 0.008737378753721714
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015470660291612148,
              "candidate": 0.024208039045333862,
              "position": [
                5.5,
                4.5,
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
      "bias_percent": 0.027588624894711207,
      "rms_normalized_error_percent": 0.32066333834121874,
      "absolute_error": {
        "p95": 0.12343036966624243,
        "p99": 0.17652745206458392,
        "maximum": 0.1988068717897158
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 12.024652280469327,
      "rms_normalized_to_uniform_percent": 0.32066333834121874
    },
    "overcast": {
      "bias_percent": 0.04373987206159852,
      "rms_normalized_error_percent": 0.27792553659925445,
      "absolute_error": {
        "p95": 0.07293647527694702,
        "p99": 0.10496316552162163,
        "maximum": 0.12072908878326416
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 7.646310806274414,
      "rms_normalized_to_uniform_percent": 0.19675099111270924
    },
    "horizon": {
      "bias_percent": 0.26640286124730084,
      "rms_normalized_error_percent": 3.398528939419023,
      "absolute_error": {
        "p95": 0.08563979054719972,
        "p99": 0.13819860743580178,
        "maximum": 0.16408064005758982
      },
      "worst_index": [
        29
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.4267431226982348,
      "rms_normalized_to_uniform_percent": 0.23693952191480613
    },
    "north": {
      "bias_percent": 0.023028415375955576,
      "rms_normalized_error_percent": 0.3667561358346477,
      "absolute_error": {
        "p95": 0.09334707260131836,
        "p99": 0.13570036888122552,
        "maximum": 0.15070772171020508
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 8.388736724853516,
      "rms_normalized_to_uniform_percent": 0.24014562926195093
    },
    "east": {
      "bias_percent": 0.2756616126549759,
      "rms_normalized_error_percent": 0.5981771995240106,
      "absolute_error": {
        "p95": 0.05029940605163574,
        "p99": 0.05416839718818664,
        "maximum": 0.054934144020080566
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.318145990371704,
      "rms_normalized_to_uniform_percent": 0.1216873658550892
    },
    "south": {
      "bias_percent": -98.25507243419139,
      "rms_normalized_error_percent": 99.66531725217327,
      "absolute_error": {
        "p95": 0.00012382397653709631,
        "p99": 0.00018248982451041226,
        "maximum": 0.0001899338240036741
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 2.0018678696942516e-05,
      "rms_normalized_to_uniform_percent": 0.0002299607423013646
    },
    "west": {
      "bias_percent": -0.3098692324468305,
      "rms_normalized_error_percent": 0.7582330810300348,
      "absolute_error": {
        "p95": 0.06804296374320984,
        "p99": 0.08188789486885067,
        "maximum": 0.0883188247680664
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.327934980392456,
      "rms_normalized_to_uniform_percent": 0.15458333523027065
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
        "identifier": "north_facing_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.03164124639150113,
          "cvrmse_percent": 3.286929918391885,
          "absolute_error_percentiles_lux": {
            "p50": 1.2803688049316406,
            "p90": 5.5925933837890645,
            "p95": 10.454790496826153,
            "p99": 38.59501556396484
          },
          "maximum_absolute_error_lux": 275.6669921875,
          "worst": {
            "sensor_index": 0,
            "position": [
              0.5,
              5.5,
              0.75
            ],
            "hour_of_year": 2957.5,
            "foton_lux": 1890.1011962890625,
            "radiance_lux": 1614.4342041015625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.3588013698630129,
            "maximum_error_percentage_points": 2.2436986301369863,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.35358897592590743,
            "maximum_error_percentage_points": 0.9584905075155064,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.2577891933028924,
            "maximum_error_percentage_points": 1.2057534246575372,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.25839421613394326,
            "maximum_error_percentage_points": 1.2057534246575372,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0007952815829528163,
            "maximum_error_percentage_points": 0.028219178082191793,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 19.444444444444443,
          "radiance_percent": 22.22222222222222,
          "difference_percentage_points": 2.7777777777777786,
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
            "identifier": "north_facing_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "north_facing_grid",
            "maximum_error_percentage_points": 0.004893514554794365,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "north_facing_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "north_facing_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "north_facing_grid",
            "maximum_error_percentage_points": 0.0008219178082191914,
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
      "study_preparation_seconds": 0.00786525011062622,
      "weather_seconds": 0.11797637504059821,
      "metric_reduction_seconds": 0.06965141696855426,
      "write_seconds": 0.03235729201696813,
      "total_seconds": 0.22017691598739475,
      "cold_end_to_end_seconds": 0.22804216609802097,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.00906837498769164,
      "engine_upload_seconds": 0.000904584,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.01493545831181109,
      "engine_annual_reduction_seconds": 0.0015247499104589224,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.01493545831181109
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.00786525011062622,
      "weather_seconds": 0.1057255839696154,
      "metric_reduction_seconds": 0.04524008301086724,
      "write_seconds": 0.0333434590138495,
      "total_seconds": 0.18452070804778486,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.18452070804778486,
      "raw_export_seconds": 0.009227792033925653,
      "engine_upload_seconds": 9.4834e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.001610041712410748,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01818700006697327,
      "full": 0.011107999947853386
    }
  },
  "elapsed_seconds": 56.19357912510168,
  "result_class": "passed"
}
```
