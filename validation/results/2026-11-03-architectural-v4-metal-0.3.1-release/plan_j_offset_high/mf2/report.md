# Foton report

Status: **passed**

```json
{
  "scene": "plan_j_offset_high",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_j_offset_high",
    "category": "form",
    "question": "How does a offset high opening illuminate a J-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "j",
    "window_profile": "offset_high"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 47,
    "floor_area": 63.0,
    "aperture_area": 1.4399999999999988
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "14cfbcd7229b6de0a5051a83dc99913cbfe1328942a88c427468414d77f33a87",
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 4509496220527033930,
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 4509496220527033930,
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
    "maximum_samples": 262144,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/refbundle/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "791bdcd857c7f3bd3aebf9cd2cb2ca8a301fb7c700c4a5b3fa8987eaef21ebd8",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "23633e9e91bc013f4a3a6d776a0b95fe8d48adfbd13e89c51c834683d9ee6bfe",
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
          "p99": 1.9546132534742355e-06
        },
        "bias_percent": -0.04103263021909103,
        "identifier": "plan_j_offset_high_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.2118164597810421,
        "worst_index": [
          34,
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
          "maximum": 0.00025011226534843445,
          "p95": 6.650115210504737e-06,
          "p99": 3.0439594411291182e-05
        },
        "bias_percent": -0.016541250614322132,
        "identifier": "plan_j_offset_high_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.8077889686216064,
        "worst_index": [
          31,
          150,
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
          "maximum": 0.00024550221860408783,
          "p95": 5.852523827343248e-06,
          "p99": 2.6504669222049415e-05
        },
        "bias_percent": 0.2060915945631368,
        "identifier": "plan_j_offset_high_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.5365980325238984,
        "worst_index": [
          45,
          453,
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
            "identifier": "plan_j_offset_high_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005415932610048912,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.303606692701578e-05
                },
                "candidate_energy": 1.6172489919649706,
                "cvrmse_percent": 88.51061761589182,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.05764739567475814,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.6163172271776602,
                "relative_energy_error_percent": 0.057647395674758135,
                "rms_normalized_rmse_percent": 7.62249316627021,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0010831844701897353,
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "reference": 0.000541591209184844,
                  "rgb_channel": 0,
                  "sky_patch_index": 150
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006596373204956762,
                  "p50": 0.0,
                  "p90": 2.552142404965707e-06,
                  "p95": 6.219932970452646e-06,
                  "p99": 6.820674752816558e-05
                },
                "candidate_energy": 0.8371644796465585,
                "cvrmse_percent": 212.31710556387745,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.25490751921140836,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.8393039284692634,
                "relative_energy_error_percent": 0.25490751921140836,
                "rms_normalized_rmse_percent": 5.736759015472501,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0004476833710214123,
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "reference": 0.00021195394947426394,
                  "rgb_channel": 0,
                  "sky_patch_index": 150
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.66799998562783,
            "full": 273.9891249220818
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 113.37099992670119,
            "full": 270.3793750843033
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 113.08654199820012,
            "full": 284.19762500561774
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.6102499179542,
            "full": 263.03445803932846
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 115.68408296443522,
            "full": 262.8300830256194
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 112.82233300153166,
            "full": 265.0688330177218
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.37912502232939,
            "full": 271.93974994588643
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 113.45674993935972,
            "full": 273.3470000093803
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
            "identifier": "plan_j_offset_high_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00036943377926945686,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.3531285478384234e-05
                },
                "candidate_energy": 1.6173357513162046,
                "cvrmse_percent": 51.07064448058363,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.32829831661520115,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.622662926387875,
                "relative_energy_error_percent": 0.32829831661520115,
                "rms_normalized_rmse_percent": 4.408720928375697,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003714770544320345,
                  "global_sensor_index": 45,
                  "local_sensor_index": 45,
                  "reference": 0.004084204323589802,
                  "rgb_channel": 0,
                  "sky_patch_index": 364
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005041155964136124,
                  "p50": 0.0,
                  "p90": 5.059978008148391e-06,
                  "p95": 9.617030173103558e-06,
                  "p99": 4.892059223493561e-05
                },
                "candidate_energy": 1.4532603262306694,
                "cvrmse_percent": 90.59551625406078,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.3238612288376727,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.4485689729542983,
                "relative_energy_error_percent": 0.32386122883767277,
                "rms_normalized_rmse_percent": 3.4148087542110668,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.017099060118198395,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.016594944521784782,
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.61416605021805,
            "full": 3099.7259590076283
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.1005419306457,
            "full": 3074.246499920264
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 162.67670807428658,
            "full": 3118.011457961984
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 163.91558293253183,
            "full": 3100.250874995254
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
            "identifier": "plan_j_offset_high_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002988161286339164,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.345380198676139e-05
                },
                "candidate_energy": 1.6187793352098652,
                "cvrmse_percent": 49.57010396640521,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.02760153881539718,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.6183326504951765,
                "relative_energy_error_percent": 0.02760153881539718,
                "rms_normalized_rmse_percent": 4.270425956850407,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00371756951790303,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.004016385646536946,
                  "rgb_channel": 0,
                  "sky_patch_index": 406
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004921321524307132,
                  "p50": 0.0,
                  "p90": 5.0635327397685614e-06,
                  "p95": 9.752583309818874e-06,
                  "p99": 5.358550697565079e-05
                },
                "candidate_energy": 1.4496525955333261,
                "cvrmse_percent": 88.71655838850778,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.3022500258450739,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.454047454339868,
                "relative_energy_error_percent": 0.3022500258450739,
                "rms_normalized_rmse_percent": 3.3478069278387577,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00028879009187221527,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": -0.0002033420605584979,
                  "rgb_channel": 0,
                  "sky_patch_index": 308
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.65595898684114,
            "full": 3252.738874987699
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.15345898084342,
            "full": 3242.009707959369
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.0340830059722,
            "full": 3283.4678340004757
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.26208402216434,
            "full": 3262.923000031151
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
            "identifier": "plan_j_offset_high_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001642407150939107,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.1815980542451143e-05
                },
                "candidate_energy": 1.6197082841586052,
                "cvrmse_percent": 29.73956264151214,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.2563162049695401,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.6155673233067773,
                "relative_energy_error_percent": 0.25631620496954016,
                "rms_normalized_rmse_percent": 2.5615181724378524,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.000738874456146732,
                  "global_sensor_index": 41,
                  "local_sensor_index": 41,
                  "reference": 0.0005746337410528213,
                  "rgb_channel": 0,
                  "sky_patch_index": 91
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00048049446195364,
                  "p50": 0.0,
                  "p90": 3.5429152376309503e-06,
                  "p95": 6.630763891735114e-06,
                  "p99": 3.309779640403576e-05
                },
                "candidate_energy": 1.454461526192599,
                "cvrmse_percent": 54.05674053439382,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.6332506690414536,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.4637306100738563,
                "relative_energy_error_percent": 0.6332506690414536,
                "rms_normalized_rmse_percent": 2.0480984768417922,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.026349875144660473,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.026830369606614113,
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 225.38208309561014,
            "full": 5766.461624996737
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 222.89524995721877,
            "full": 5801.103917066939
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 232.23737499210984,
            "full": 5737.083957996219
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
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "47",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 228.50274993106723,
            "full": 5830.686792032793
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/suite-0.3.1/run/plan_j_offset_high/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4855.830417014658,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_offset_high/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 18739.735499955714,
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
      47,
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
        "identifier": "plan_j_offset_high_grid",
        "full_identifier": "plan_j_offset_high_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": -0.07455180027019224,
            "cvrmse_percent": 7.553587173191046,
            "rms_normalized_rmse_percent": 0.6512432693251387,
            "reference_energy": 1.6195405054554612,
            "candidate_energy": 1.6183331088525392,
            "relative_energy_error_percent": 0.07455180027019224,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.753040123730898e-06,
              "maximum": 6.128521636128426e-05
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 447,
              "rgb_channel": 0,
              "reference": 0.0024364946875721216,
              "candidate": 0.0023752094712108374,
              "position": [
                7.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -2.1541046149486873,
            "cvrmse_percent": 78.53621783001684,
            "rms_normalized_rmse_percent": 2.969124823640462,
            "reference_energy": 1.457193366250106,
            "candidate_energy": 1.4258038966989863,
            "relative_energy_error_percent": 2.154104614948687,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.377551704237703e-06,
              "p95": 7.780140094837407e-06,
              "p99": 2.156231494154781e-05,
              "maximum": 0.0009549334645271301
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026590123772621155,
              "candidate": 0.025635190308094025,
              "position": [
                7.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -1.0594632982010828,
            "cvrmse_percent": 37.13668555431603,
            "rms_normalized_rmse_percent": 2.964383320617922,
            "reference_energy": 3.0767338717055672,
            "candidate_energy": 3.0441370055515256,
            "relative_energy_error_percent": 1.0594632982010828,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.360750608611852e-06,
              "p95": 7.775152425892884e-06,
              "p99": 2.0768435206264257e-05,
              "maximum": 0.0009549334645271301
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026590123772621155,
              "candidate": 0.025635190308094025,
              "position": [
                7.5,
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
      47,
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
        "identifier": "plan_j_offset_high_grid",
        "full_identifier": "plan_j_offset_high_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": -0.07455180027019224,
            "cvrmse_percent": 7.553587173191046,
            "rms_normalized_rmse_percent": 0.6512432693251387,
            "reference_energy": 1.6195405054554612,
            "candidate_energy": 1.6183331088525392,
            "relative_energy_error_percent": 0.07455180027019224,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.753040123730898e-06,
              "maximum": 6.128521636128426e-05
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 447,
              "rgb_channel": 0,
              "reference": 0.0024364946875721216,
              "candidate": 0.0023752094712108374,
              "position": [
                7.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 70.65750636870611,
            "cvrmse_percent": 974.9703884589009,
            "rms_normalized_rmse_percent": 26.220465289137458,
            "reference_energy": 0.835476813787805,
            "candidate_energy": 1.4258038966989863,
            "relative_energy_error_percent": 70.65750636870611,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.4090000149735715e-05,
              "p95": 2.596000012999866e-05,
              "p99": 5.461927503347397e-05,
              "maximum": 0.006077263504266739
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 46,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.020569005981087685,
              "candidate": 0.026646269485354424,
              "position": [
                8.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 23.99655927844327,
            "cvrmse_percent": 331.7535432355137,
            "rms_normalized_rmse_percent": 26.217102793140597,
            "reference_energy": 2.4550173192432663,
            "candidate_energy": 3.0441370055515256,
            "relative_energy_error_percent": 23.99655927844327,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.4010000086273067e-05,
              "p95": 2.58545996985049e-05,
              "p99": 5.474916088132886e-05,
              "maximum": 0.006077263504266739
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 46,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.020569005981087685,
              "candidate": 0.026646269485354424,
              "position": [
                8.5,
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
      "bias_percent": -0.3038165586509353,
      "rms_normalized_error_percent": 0.4505424542539949,
      "absolute_error": {
        "p95": 0.04242302677950972,
        "p99": 0.0833957260897916,
        "maximum": 0.09425713566956517
      },
      "worst_index": [
        45
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.7792146268732516,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.4505424542539949
    },
    "overcast": {
      "bias_percent": -0.2696811836828515,
      "rms_normalized_error_percent": 0.3977586619959126,
      "absolute_error": {
        "p95": 0.029328227043151838,
        "p99": 0.06236066818237304,
        "maximum": 0.06380176544189453
      },
      "worst_index": [
        45
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.9274808168411255,
      "reference_fraction_of_uniform": 0.6935343742370605,
      "rms_normalized_to_uniform_percent": 0.3043819383077401
    },
    "horizon": {
      "bias_percent": -1.3167647916398313,
      "rms_normalized_error_percent": 4.229672805957662,
      "absolute_error": {
        "p95": 0.025435476246698105,
        "p99": 0.03821457320752764,
        "maximum": 0.04270128564320774
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.22885861494862825,
      "reference_fraction_of_uniform": 0.08234650636036162,
      "rms_normalized_to_uniform_percent": 0.2088052519423622
    },
    "north": {
      "bias_percent": -96.10044569836526,
      "rms_normalized_error_percent": 99.605166946098,
      "absolute_error": {
        "p95": 1.8568798805063094e-05,
        "p99": 3.700232397250146e-05,
        "maximum": 4.6216278860811144e-05
      },
      "worst_index": [
        29
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 3.568067995729507e-06,
      "reference_fraction_of_uniform": 1.283840447285911e-06,
      "rms_normalized_to_uniform_percent": 0.00016770715861540815
    },
    "east": {
      "bias_percent": 0.1419957431913966,
      "rms_normalized_error_percent": 0.4851999902951647,
      "absolute_error": {
        "p95": 0.010216805338859557,
        "p99": 0.015140613913536065,
        "maximum": 0.018362998962402344
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5414848923683167,
      "reference_fraction_of_uniform": 0.19483378529548645,
      "rms_normalized_to_uniform_percent": 0.09987954385869806
    },
    "south": {
      "bias_percent": -0.37694243775166386,
      "rms_normalized_error_percent": 0.5376019481582643,
      "absolute_error": {
        "p95": 0.03483190536499023,
        "p99": 0.055464715957641575,
        "maximum": 0.06916522979736328
      },
      "worst_index": [
        45
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.824375867843628,
      "reference_fraction_of_uniform": 0.6564357876777649,
      "rms_normalized_to_uniform_percent": 0.3387455001153425
    },
    "west": {
      "bias_percent": -0.8701207552569822,
      "rms_normalized_error_percent": 0.8924989074788933,
      "absolute_error": {
        "p95": 0.017668014764785755,
        "p99": 0.028051595687866197,
        "maximum": 0.03572845458984375
      },
      "worst_index": [
        45
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.33645662665367126,
      "reference_fraction_of_uniform": 0.1210617646574974,
      "rms_normalized_to_uniform_percent": 0.1496868384072797
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
        "identifier": "plan_j_offset_high_grid",
        "sensor_count": 47,
        "illuminance": {
          "nmbe_percent": -0.36157713467940833,
          "cvrmse_percent": 4.551995603105081,
          "absolute_error_percentiles_lux": {
            "p50": 0.877471923828125,
            "p90": 10.753773498535157,
            "p95": 18.437707519531237,
            "p99": 45.74051879882813
          },
          "maximum_absolute_error_lux": 281.3291015625,
          "worst": {
            "sensor_index": 46,
            "position": [
              8.5,
              0.5,
              0.75
            ],
            "hour_of_year": 3566.5,
            "foton_lux": 13024.1455078125,
            "radiance_lux": 13305.474609375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.18052462838822464,
            "maximum_error_percentage_points": 1.6947945205479442,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.2550268189420248,
            "maximum_error_percentage_points": 1.0402724713427354,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.42903526668609643,
            "maximum_error_percentage_points": 2.549999999999997,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.4262459924220346,
            "maximum_error_percentage_points": 2.549999999999997,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.01183619935878752,
            "maximum_error_percentage_points": 0.1693150684931508,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 12.76595744680851,
          "radiance_percent": 12.76595744680851,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.127659574468085,
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
      "maximum_error_percentage_points": 0.004964415667807032,
      "metrics": {
        "da": [
          {
            "identifier": "plan_j_offset_high_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_j_offset_high_grid",
            "maximum_error_percentage_points": 0.004964415667807032,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_j_offset_high_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_j_offset_high_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_j_offset_high_grid",
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
      "study_preparation_seconds": 0.00672962493263185,
      "weather_seconds": 0.0985542080597952,
      "metric_reduction_seconds": 0.13788545806892216,
      "write_seconds": 0.04325799993239343,
      "total_seconds": 0.2798662499990314,
      "cold_end_to_end_seconds": 0.2865958749316633,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.02322375006042421,
      "engine_upload_seconds": 0.000922542,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.08120191667694598,
      "engine_annual_reduction_seconds": 0.0020643749739974737,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.08120191667694598
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.00672962493263185,
      "weather_seconds": 0.10377241589594632,
      "metric_reduction_seconds": 0.04869708395563066,
      "write_seconds": 0.02857720898464322,
      "total_seconds": 0.18154508306179196,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.18154508306179196,
      "raw_export_seconds": 0.00996250007301569,
      "engine_upload_seconds": 8.9166e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0020252916729077697,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.011470207944512367,
      "full": 0.08450962498318404
    }
  },
  "elapsed_seconds": 1.379083542036824,
  "result_class": "passed"
}
```
