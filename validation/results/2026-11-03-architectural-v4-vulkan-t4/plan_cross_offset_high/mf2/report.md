# Foton report

Status: **passed**

```json
{
  "scene": "plan_cross_offset_high",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_cross_offset_high",
    "category": "form",
    "question": "How does a offset high opening illuminate a CROSS-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "cross",
    "window_profile": "offset_high"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 44,
    "floor_area": 63.0,
    "aperture_area": 1.440000000000001
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "46127d4301be9f0ba3fe0e179c900badb6730acae0e0b5b6b86fa4a49bc3d138",
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 6430983599904955441,
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 6430983599904955441,
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
    "maximum_samples": 262144,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "00693eaa3820d6d920cafe9291ce4da327de69ca4a85a1b98c3050de0f3d4143",
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
          "maximum": 0.00021733436733484268,
          "p95": 0.0,
          "p99": 1.5203841030597687e-07
        },
        "bias_percent": 0.0728320494484127,
        "identifier": "plan_cross_offset_high_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3582579008068842,
        "worst_index": [
          33,
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
          "maximum": 0.00038101524114608765,
          "p95": 6.255440894165076e-06,
          "p99": 2.8284135623835027e-05
        },
        "bias_percent": 0.022921365310441002,
        "identifier": "plan_cross_offset_high_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.8164771394137051,
        "worst_index": [
          32,
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
          "maximum": 0.0002372507005929947,
          "p95": 5.303617172103259e-06,
          "p99": 2.3761735064908862e-05
        },
        "bias_percent": 0.07105828880028113,
        "identifier": "plan_cross_offset_high_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.4928877831279432,
        "worst_index": [
          32,
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
            "identifier": "plan_cross_offset_high_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004915326135233045,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.508420195430517e-05
                },
                "candidate_energy": 1.296854255895596,
                "cvrmse_percent": 86.05519762561948,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.43612457958088097,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.2912229153844237,
                "relative_energy_error_percent": 0.4361245795808809,
                "rms_normalized_rmse_percent": 6.954641161659147,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003712197416462004,
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "reference": 0.004203730029985309,
                  "rgb_channel": 0,
                  "sky_patch_index": 362
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000740797899197787,
                  "p50": 0.0,
                  "p90": 1.4604787565986044e-06,
                  "p95": 5.8946950503013795e-06,
                  "p99": 5.244674684945494e-05
                },
                "candidate_energy": 0.6515248723224598,
                "cvrmse_percent": 251.79765316669398,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.7891167990208958,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6464238332613199,
                "relative_energy_error_percent": 0.7891167990208958,
                "rms_normalized_rmse_percent": 6.066955072874302,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0004114216426387429,
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "reference": -0.0003293762565590441,
                  "rgb_channel": 0,
                  "sky_patch_index": 362
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.53562493808568,
            "full": 267.98175007570535
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 113.86970803141594,
            "full": 277.2378330118954
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.00425001233816,
            "full": 268.5368329985067
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 113.45554096624255,
            "full": 266.3487079553306
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.41083308961242,
            "full": 284.90541595965624
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.2504169838503,
            "full": 270.55545803159475
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 119.42933301907033,
            "full": 288.1332909455523
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 125.21641701459885,
            "full": 274.0029999986291
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
            "identifier": "plan_cross_offset_high_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000356371165253222,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.1023486624471843e-05
                },
                "candidate_energy": 1.297080768149499,
                "cvrmse_percent": 57.33044051809935,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.03197024479245983,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.296666220784573,
                "relative_energy_error_percent": 0.031970244792459836,
                "rms_normalized_rmse_percent": 4.657663569278483,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0037561164936050773,
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "reference": 0.004112487658858299,
                  "rgb_channel": 0,
                  "sky_patch_index": 360
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00044733850518241525,
                  "p50": 0.0,
                  "p90": 4.3724280658352654e-06,
                  "p95": 8.765257689447026e-06,
                  "p99": 4.612607881426811e-05
                },
                "candidate_energy": 1.1760821343170846,
                "cvrmse_percent": 102.89766409003327,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.23498936323764724,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1788523118582326,
                "relative_energy_error_percent": 0.23498936323764727,
                "rms_normalized_rmse_percent": 3.4903597001315045,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0002150799846276641,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.00023225852055475116,
                  "rgb_channel": 0,
                  "sky_patch_index": 148
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.02029205486178,
            "full": 3133.8087080512196
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.02195797953755,
            "full": 3202.8719160007313
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.4014580110088,
            "full": 3187.472084071487
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.5395830180496,
            "full": 3209.773874958046
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
            "identifier": "plan_cross_offset_high_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002998885465785861,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.061088162008673e-05
                },
                "candidate_energy": 1.296604446109086,
                "cvrmse_percent": 58.46686294942624,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.09325665712106322,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.2978147447556694,
                "relative_energy_error_percent": 0.09325665712106322,
                "rms_normalized_rmse_percent": 4.758885319359878,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0035862245131284,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.003886113059706986,
                  "rgb_channel": 0,
                  "sky_patch_index": 357
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004299851134419441,
                  "p50": 0.0,
                  "p90": 4.246944115493534e-06,
                  "p95": 8.909030839276966e-06,
                  "p99": 4.9044117531593656e-05
                },
                "candidate_energy": 1.1831218411224995,
                "cvrmse_percent": 101.19454136346947,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.9253074798992126,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1722746956784214,
                "relative_energy_error_percent": 0.9253074798992127,
                "rms_normalized_rmse_percent": 3.4229135688652517,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.030966955237090588,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.030536970123648643,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.11812499444932,
            "full": 3376.321666990407
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 159.6979999449104,
            "full": 3377.561041037552
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.26104094088078,
            "full": 3291.700958041474
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.35020795464516,
            "full": 3370.29662495479
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
            "identifier": "plan_cross_offset_high_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00015019800048321486,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.1418480426073074e-05
                },
                "candidate_energy": 1.2968545349513079,
                "cvrmse_percent": 33.69591543514127,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.04845631874554197,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.2962264313400738,
                "relative_energy_error_percent": 0.04845631874554197,
                "rms_normalized_rmse_percent": 2.735628511437314,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001526989508420229,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.0016771875089034438,
                  "rgb_channel": 0,
                  "sky_patch_index": 148
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003674700856208801,
                  "p50": 0.0,
                  "p90": 3.062301004774781e-06,
                  "p95": 6.416154974431265e-06,
                  "p99": 3.2458956411574036e-05
                },
                "candidate_energy": 1.1818787792303382,
                "cvrmse_percent": 59.6328707429018,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.29748599489764105,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1783732837435856,
                "relative_energy_error_percent": 0.297485994897641,
                "rms_normalized_rmse_percent": 2.0212021882516096,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02808395028114319,
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "reference": 0.02771648019552231,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 215.9367089625448,
            "full": 6057.924250024371
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 223.33575005177408,
            "full": 5966.895000077784
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 220.8839589729905,
            "full": 5987.639625091106
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 222.84633398521692,
            "full": 6079.374375054613
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/plan_cross_offset_high/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4295.269708964042,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_offset_high/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 16622.68866598606,
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
        "identifier": "plan_cross_offset_high_grid",
        "full_identifier": "plan_cross_offset_high_grid",
        "start_sensor_index": 0,
        "sensor_count": 44,
        "stages": {
          "direct": {
            "nmbe_percent": -0.05550359015850934,
            "cvrmse_percent": 7.828857327926221,
            "rms_normalized_rmse_percent": 0.6365606719147577,
            "reference_energy": 1.297497490088631,
            "candidate_energy": 1.2967773323994152,
            "relative_energy_error_percent": 0.05550359015850934,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.329769242554903e-07,
              "maximum": 6.128521636128426e-05
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 447,
              "rgb_channel": 0,
              "reference": 0.0024364946875721216,
              "candidate": 0.0023752094712108374,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.960733506119812,
            "cvrmse_percent": 81.16551306840553,
            "rms_normalized_rmse_percent": 2.752449970280265,
            "reference_energy": 1.1791690098028162,
            "candidate_energy": 1.1560486479338312,
            "relative_energy_error_percent": 1.960733506119812,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.8149902934492275e-06,
              "p95": 7.150578312575817e-06,
              "p99": 2.0504114218056202e-05,
              "maximum": 0.0008039567619562149
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.023747526109218597,
              "candidate": 0.022943569347262383,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.9626051613830808,
            "cvrmse_percent": 38.58400295573654,
            "rms_normalized_rmse_percent": 2.748189339950949,
            "reference_energy": 2.476666499891447,
            "candidate_energy": 2.4528259803332464,
            "relative_energy_error_percent": 0.9626051613830809,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.821926156888367e-06,
              "p95": 7.141963578760624e-06,
              "p99": 2.0273728296160698e-05,
              "maximum": 0.0008039567619562149
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.023747526109218597,
              "candidate": 0.022943569347262383,
              "position": [
                5.5,
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
        "identifier": "plan_cross_offset_high_grid",
        "full_identifier": "plan_cross_offset_high_grid",
        "start_sensor_index": 0,
        "sensor_count": 44,
        "stages": {
          "direct": {
            "nmbe_percent": -0.05550359015850934,
            "cvrmse_percent": 7.828857327926221,
            "rms_normalized_rmse_percent": 0.6365606719147577,
            "reference_energy": 1.297497490088631,
            "candidate_energy": 1.2967773323994152,
            "relative_energy_error_percent": 0.05550359015850934,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.329769242554903e-07,
              "maximum": 6.128521636128426e-05
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 447,
              "rgb_channel": 0,
              "reference": 0.0024364946875721216,
              "candidate": 0.0023752094712108374,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 79.08923166867685,
            "cvrmse_percent": 1306.2545145641081,
            "rms_normalized_rmse_percent": 31.374931738327923,
            "reference_energy": 0.6455154434257517,
            "candidate_energy": 1.1560486479338312,
            "relative_energy_error_percent": 79.08923166867685,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2290000086068176e-05,
              "p95": 2.542233960411977e-05,
              "p99": 5.673139821738005e-05,
              "maximum": 0.0076643601059913635
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022502049803733826,
              "candidate": 0.03016640990972519,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 26.238273457951227,
            "cvrmse_percent": 433.9337273298647,
            "rms_normalized_rmse_percent": 31.372378540059167,
            "reference_energy": 1.9430129335143826,
            "candidate_energy": 2.4528259803332464,
            "relative_energy_error_percent": 26.238273457951223,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.228955125043285e-05,
              "p95": 2.542233960411977e-05,
              "p99": 5.7115350500680506e-05,
              "maximum": 0.0076643601059913635
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022502049803733826,
              "candidate": 0.03016640990972519,
              "position": [
                6.5,
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
      "bias_percent": -0.21060112116498672,
      "rms_normalized_error_percent": 0.39889189827664867,
      "absolute_error": {
        "p95": 0.0405246725444458,
        "p99": 0.0634736799451049,
        "maximum": 0.06731740250472207
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.400571453587056,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.39889189827664867
    },
    "overcast": {
      "bias_percent": -0.21209776830771274,
      "rms_normalized_error_percent": 0.32114621980535546,
      "absolute_error": {
        "p95": 0.02862420082092286,
        "p99": 0.03982330799102783,
        "maximum": 0.04351997375488281
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.6283107995986938,
      "reference_fraction_of_uniform": 0.6783013343811035,
      "rms_normalized_to_uniform_percent": 0.24334099997660014
    },
    "horizon": {
      "bias_percent": -0.21201558218250788,
      "rms_normalized_error_percent": 2.8904816143390426,
      "absolute_error": {
        "p95": 0.012601640227734134,
        "p99": 0.026366767486608496,
        "maximum": 0.035731264886258995
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.21940352031426122,
      "reference_fraction_of_uniform": 0.09139637147080847,
      "rms_normalized_to_uniform_percent": 0.1693977995706698
    },
    "north": {
      "bias_percent": -99.27903753521397,
      "rms_normalized_error_percent": 99.98318560564495,
      "absolute_error": {
        "p95": 6.289131779340097e-05,
        "p99": 0.0002702411432255759,
        "maximum": 0.0004052102449350059
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.7597045371076092e-05,
      "reference_fraction_of_uniform": 7.33035722078057e-06,
      "rms_normalized_to_uniform_percent": 0.001310741355748225
    },
    "east": {
      "bias_percent": -0.2477969152317417,
      "rms_normalized_error_percent": 0.6231115063385285,
      "absolute_error": {
        "p95": 0.014686131477355965,
        "p99": 0.026090888977050787,
        "maximum": 0.03255128860473633
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5087056756019592,
      "reference_fraction_of_uniform": 0.21191024780273438,
      "rms_normalized_to_uniform_percent": 0.14580596540964638
    },
    "south": {
      "bias_percent": -0.2026936980705527,
      "rms_normalized_error_percent": 0.4466559143619914,
      "absolute_error": {
        "p95": 0.029457163810729985,
        "p99": 0.045471303462982185,
        "maximum": 0.057196617126464844
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.6672821044921875,
      "reference_fraction_of_uniform": 0.6945355534553528,
      "rms_normalized_to_uniform_percent": 0.283874973468735
    },
    "west": {
      "bias_percent": -0.5440477578625952,
      "rms_normalized_error_percent": 0.9519702329799525,
      "absolute_error": {
        "p95": 0.010914638638496404,
        "p99": 0.013784146904945374,
        "maximum": 0.01400899887084961
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.19048739969730377,
      "reference_fraction_of_uniform": 0.07935085892677307,
      "rms_normalized_to_uniform_percent": 0.08776472496662863
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
        "identifier": "plan_cross_offset_high_grid",
        "sensor_count": 44,
        "illuminance": {
          "nmbe_percent": -0.37781159533753267,
          "cvrmse_percent": 4.9246129097036535,
          "absolute_error_percentiles_lux": {
            "p50": 0.6542661190032959,
            "p90": 8.856377410888673,
            "p95": 15.871914672851556,
            "p99": 42.47813674926758
          },
          "maximum_absolute_error_lux": 304.6015625,
          "worst": {
            "sensor_index": 31,
            "position": [
              6.5,
              2.5,
              0.75
            ],
            "hour_of_year": 1356.5,
            "foton_lux": 17708.900390625,
            "radiance_lux": 18013.501953125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.1178518057285177,
            "maximum_error_percentage_points": 1.2858904109589062,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.19776903846959398,
            "maximum_error_percentage_points": 1.1106452162106848,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.3805635118306352,
            "maximum_error_percentage_points": 2.5210958904109617,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.38298256537982545,
            "maximum_error_percentage_points": 2.521917808219179,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.004828767123287638,
            "maximum_error_percentage_points": 0.05863013698630137,
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
      "maximum_error_percentage_points": 0.004931506849315426,
      "metrics": {
        "da": [
          {
            "identifier": "plan_cross_offset_high_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_cross_offset_high_grid",
            "maximum_error_percentage_points": 0.00488287938784282,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_cross_offset_high_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_cross_offset_high_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_cross_offset_high_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
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
      "study_preparation_seconds": 0.35869415100023616,
      "weather_seconds": 0.25255855900104507,
      "metric_reduction_seconds": 1.655814140001894,
      "write_seconds": 0.05392690900043817,
      "total_seconds": 1.9627292769982887,
      "cold_end_to_end_seconds": 2.321423427998525,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.03278675899855443,
      "engine_upload_seconds": 0.045925704,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.040059545,
      "engine_annual_reduction_seconds": 0.034375749,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.040059545
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.35869415100023616,
      "weather_seconds": 0.450556179999694,
      "metric_reduction_seconds": 1.899321258002601,
      "write_seconds": 0.022119113000371726,
      "total_seconds": 2.372356948999368,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 2.372356948999368,
      "raw_export_seconds": 0.009524039000098128,
      "engine_upload_seconds": 0.054750659,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 8.6e-08,
      "engine_annual_reduction_seconds": 0.039800782,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.018755788001726614,
      "full": 0.059169577001739526
    }
  },
  "elapsed_seconds": 7.0343263579998165,
  "result_class": "passed"
}
```
