# Foton report

Status: **passed**

```json
{
  "scene": "plan_l_distributed",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_l_distributed",
    "category": "form",
    "question": "How does a distributed opening illuminate a L-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "l",
    "window_profile": "distributed"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 6,
    "shades": 0,
    "sensors": 48,
    "floor_area": 54.0,
    "aperture_area": 7.199999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "42366c3fe6521a2b59b8941896e17ac4ef4fa651260e0df490a72e1b5e812cdf",
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
      "scene_fingerprint": 16609558811435530087,
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 16609558811435530087,
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
    "model_sha256": "63500a2338c49a83abc067a45b369e227c59a944c9cd7e3b2c344bd71899e25f",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "738a59ae8fb6881ea29066a9316dfc51647b6e94d0eae23cc7b76edc5ea48e16",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0006667673587799072,
          "p95": 3.461034793872386e-05,
          "p99": 0.00014698994345963
        },
        "bias_percent": -0.004995085911255719,
        "identifier": "plan_l_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.5356954756813113,
        "worst_index": [
          28,
          129,
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
          "maximum": 0.000603262335062027,
          "p95": 7.073208689689636e-05,
          "p99": 0.0001611071638762951
        },
        "bias_percent": 0.07279806605557582,
        "identifier": "plan_l_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0064243841252927,
        "worst_index": [
          37,
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
          "maximum": 0.0004483535885810852,
          "p95": 5.4809264838695526e-05,
          "p99": 0.00013165734708309174
        },
        "bias_percent": 0.005380863565933173,
        "identifier": "plan_l_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8453509095643211,
        "worst_index": [
          45,
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
            "identifier": "plan_l_distributed_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0008034715428948402,
                  "p50": 0.0,
                  "p90": 4.511650186032062e-05,
                  "p95": 0.00012678717030212283,
                  "p99": 0.0003162113716825843
                },
                "candidate_energy": 11.713607592351494,
                "cvrmse_percent": 10.596146468560553,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.024359610076210455,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.716461676730674,
                "relative_energy_error_percent": 0.024359610076210455,
                "rms_normalized_rmse_percent": 2.668976766435072,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0018434114754199982,
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "reference": 0.0026468830183148384,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008407249115407467,
                  "p50": 0.0,
                  "p90": 8.591048535890915e-05,
                  "p95": 0.00019646203145384789,
                  "p99": 0.00045555876567959785
                },
                "candidate_energy": 3.447879398045437,
                "cvrmse_percent": 56.628658559487775,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.5973441424400031,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.427405989131721,
                "relative_energy_error_percent": 0.5973441424400031,
                "rms_normalized_rmse_percent": 3.269251226307216,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.000596845056861639,
                  "global_sensor_index": 46,
                  "local_sensor_index": 46,
                  "reference": 0.00024387985467910767,
                  "rgb_channel": 0,
                  "sky_patch_index": 89
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 131.86925009358674,
            "full": 308.43283399008214
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.67762506846339,
            "full": 308.01620800048113
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 131.27904199063778,
            "full": 294.84541597776115
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.35541607718915,
            "full": 297.70708398427814
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
            "identifier": "plan_l_distributed_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003943436313420534,
                  "p50": 0.0,
                  "p90": 2.7949898503720796e-05,
                  "p95": 8.797759073786438e-05,
                  "p99": 0.00018523144535720348
                },
                "candidate_energy": 11.716702623043432,
                "cvrmse_percent": 6.795997989037608,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0003761006540146438,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.716658556613972,
                "relative_energy_error_percent": 0.00037610065401464385,
                "rms_normalized_rmse_percent": 1.7118571116015608,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007776195649057627,
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "reference": 0.007381852017715573,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006728209555149078,
                  "p50": 8.587832780904137e-06,
                  "p90": 6.067794747650653e-05,
                  "p95": 0.0001281052827835083,
                  "p99": 0.00030040042474865913
                },
                "candidate_energy": 6.62782299242205,
                "cvrmse_percent": 20.107585720579333,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.016913797665310832,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.6267021654259075,
                "relative_energy_error_percent": 0.016913797665310832,
                "rms_normalized_rmse_percent": 1.8279984416955497,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04607096500694752,
                  "global_sensor_index": 42,
                  "local_sensor_index": 42,
                  "reference": 0.04539814405143261,
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 184.83225000090897,
            "full": 3152.7293749386445
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 178.1276250258088,
            "full": 3214.8442920297384
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 181.06187507510185,
            "full": 3158.2454580347985
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 191.57083297614008,
            "full": 3230.399874970317
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
            "identifier": "plan_l_distributed_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005151554942131042,
                  "p50": 0.0,
                  "p90": 2.5467824889347148e-05,
                  "p95": 8.6270272731781e-05,
                  "p99": 0.00018449639901518822
                },
                "candidate_energy": 11.719746892283347,
                "cvrmse_percent": 6.8067170045528185,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.05381167403071035,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.713443692145958,
                "relative_energy_error_percent": 0.05381167403071036,
                "rms_normalized_rmse_percent": 1.7139116954669424,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0022931559942662716,
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "reference": 0.0017780005000531673,
                  "rgb_channel": 0,
                  "sky_patch_index": 15
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009332001209259033,
                  "p50": 8.570439604227431e-06,
                  "p90": 5.822092643938965e-05,
                  "p95": 0.0001274824608117342,
                  "p99": 0.00030376948416233063
                },
                "candidate_energy": 6.6337468178364105,
                "cvrmse_percent": 20.87293962032657,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.20925013105080525,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.64765704892309,
                "relative_energy_error_percent": 0.20925013105080525,
                "rms_normalized_rmse_percent": 1.9002396040013334,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03914499469101429,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.04007819481194019,
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 177.52562498208135,
            "full": 3336.9022080441937
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 179.156459053047,
            "full": 3387.0008749654517
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 180.9554579667747,
            "full": 3383.920709020458
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 179.49466698337346,
            "full": 3400.690917042084
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
            "identifier": "plan_l_distributed_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00022945948876440525,
                  "p50": 0.0,
                  "p90": 2.0812448929064004e-05,
                  "p95": 4.682585131376982e-05,
                  "p99": 0.00010548019781708717
                },
                "candidate_energy": 11.718982585207158,
                "cvrmse_percent": 3.924434790647536,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.012025168401952164,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.720391982080372,
                "relative_energy_error_percent": 0.012025168401952164,
                "rms_normalized_rmse_percent": 0.9888340216340092,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0015729590086266398,
                  "global_sensor_index": 43,
                  "local_sensor_index": 43,
                  "reference": 0.001802418497391045,
                  "rgb_channel": 0,
                  "sky_patch_index": 84
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005116220563650131,
                  "p50": 6.0009542721672915e-06,
                  "p90": 3.8316191057674595e-05,
                  "p95": 8.134898962453008e-05,
                  "p99": 0.00018307939171791077
                },
                "candidate_energy": 6.639712229228227,
                "cvrmse_percent": 12.798103988939122,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.033582684375814055,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.637483184199979,
                "relative_energy_error_percent": 0.033582684375814055,
                "rms_normalized_rmse_percent": 1.1650516962861286,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03897932358086109,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.039490945637226105,
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 268.9622089965269,
            "full": 6025.340083055198
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 275.6817500339821,
            "full": 6005.909334053285
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 280.73091607075185,
            "full": 5980.896417051554
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 281.3596670748666,
            "full": 6065.073458012193
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/plan_l_distributed/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1338.1507500307634,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_l_distributed/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4912.63383300975,
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
      48,
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
        "identifier": "plan_l_distributed_grid",
        "full_identifier": "plan_l_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.14414092384097044,
            "cvrmse_percent": 3.3367112073655645,
            "rms_normalized_rmse_percent": 0.8405281143328696,
            "reference_energy": 11.717734378872194,
            "candidate_energy": 11.700844328285257,
            "relative_energy_error_percent": 0.1441409238409704,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.024865433573841e-06,
              "p95": 2.9120041290298104e-05,
              "p99": 8.705048821866512e-05,
              "maximum": 0.00034442590549588203
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 138,
              "rgb_channel": 0,
              "reference": 0.007755287457257509,
              "candidate": 0.008099713362753391,
              "position": [
                1.5,
                11.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.21637793322007332,
            "cvrmse_percent": 15.646359754644973,
            "rms_normalized_rmse_percent": 1.4246976973552359,
            "reference_energy": 6.640550572838151,
            "candidate_energy": 6.654919258922092,
            "relative_energy_error_percent": 0.2163779332200733,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.3496690371539444e-05,
              "p90": 4.7950010775821316e-05,
              "p95": 6.765220314264297e-05,
              "p99": 0.00016711652278900146,
              "maximum": 0.0009968206286430359
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.019062090665102005,
              "candidate": 0.01806527003645897,
              "position": [
                0.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.013734205072143985,
            "cvrmse_percent": 5.4426565788278625,
            "rms_normalized_rmse_percent": 1.37008767884051,
            "reference_energy": 18.358284951710345,
            "candidate_energy": 18.35576358720735,
            "relative_energy_error_percent": 0.013734205072143985,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.3328861314221285e-05,
              "p90": 4.595522696035915e-05,
              "p95": 6.484106415882707e-05,
              "p99": 0.00013764947652816772,
              "maximum": 0.0009968206286430359
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.019062090665102005,
              "candidate": 0.01806527003645897,
              "position": [
                0.5,
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
      48,
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
        "identifier": "plan_l_distributed_grid",
        "full_identifier": "plan_l_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.14414092384097044,
            "cvrmse_percent": 3.3367112073655645,
            "rms_normalized_rmse_percent": 0.8405281143328696,
            "reference_energy": 11.717734378872194,
            "candidate_energy": 11.700844328285257,
            "relative_energy_error_percent": 0.1441409238409704,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.024865433573841e-06,
              "p95": 2.9120041290298104e-05,
              "p99": 8.705048821866512e-05,
              "maximum": 0.00034442590549588203
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 138,
              "rgb_channel": 0,
              "reference": 0.007755287457257509,
              "candidate": 0.008099713362753391,
              "position": [
                1.5,
                11.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 93.74176891008617,
            "cvrmse_percent": 555.0705719396329,
            "rms_normalized_rmse_percent": 32.0728361086961,
            "reference_energy": 3.434942963698541,
            "candidate_energy": 6.654919258922092,
            "relative_energy_error_percent": 93.74176891008617,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 7.058999835862778e-05,
              "p90": 0.00016833334229886533,
              "p95": 0.00021190999541431665,
              "p99": 0.0003903799079125747,
              "maximum": 0.014537151902914047
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 45,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025640588253736496,
              "candidate": 0.04017774015665054,
              "position": [
                7.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.138747775204674,
            "cvrmse_percent": 125.80195338245878,
            "rms_normalized_rmse_percent": 32.06611842101566,
            "reference_energy": 15.152677342570735,
            "candidate_energy": 18.35576358720735,
            "relative_energy_error_percent": 21.138747775204674,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.988204438584944e-05,
              "p90": 0.00016660120527376424,
              "p95": 0.0002081539050777792,
              "p99": 0.0003823167644441128,
              "maximum": 0.014537151902914047
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 45,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025640588253736496,
              "candidate": 0.04017774015665054,
              "position": [
                7.5,
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
      "bias_percent": 0.030765639605358643,
      "rms_normalized_error_percent": 0.19250358082837446,
      "absolute_error": {
        "p95": 0.09008783955707579,
        "p99": 0.11626937216106961,
        "maximum": 0.1305283119917231
      },
      "worst_index": [
        47
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 17.2998844449042,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.19250358082837446
    },
    "overcast": {
      "bias_percent": 0.021628506046968685,
      "rms_normalized_error_percent": 0.17770383481116594,
      "absolute_error": {
        "p95": 0.054750919342041016,
        "p99": 0.06780622482299807,
        "maximum": 0.07810020446777344
      },
      "worst_index": [
        47
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 11.070049285888672,
      "reference_fraction_of_uniform": 0.639891505241394,
      "rms_normalized_to_uniform_percent": 0.12195857030395083
    },
    "horizon": {
      "bias_percent": 0.4800742317741323,
      "rms_normalized_error_percent": 1.6532591905328295,
      "absolute_error": {
        "p95": 0.07295117154556312,
        "p99": 0.08736120144584357,
        "maximum": 0.09419008964143671
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.059684947725747,
      "reference_fraction_of_uniform": 0.11905772863890089,
      "rms_normalized_to_uniform_percent": 0.14687873453757036
    },
    "north": {
      "bias_percent": -0.05811739822456215,
      "rms_normalized_error_percent": 0.326429083462932,
      "absolute_error": {
        "p95": 0.05506740808486938,
        "p99": 0.06086139023303986,
        "maximum": 0.06097269058227539
      },
      "worst_index": [
        39
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.465307235717773,
      "reference_fraction_of_uniform": 0.3159158229827881,
      "rms_normalized_to_uniform_percent": 0.11399444239817015
    },
    "east": {
      "bias_percent": 0.03201318358753026,
      "rms_normalized_error_percent": 0.30001165243082534,
      "absolute_error": {
        "p95": 0.062463772296905515,
        "p99": 0.08484108924865727,
        "maximum": 0.10295438766479492
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.9300971031188965,
      "reference_fraction_of_uniform": 0.34278246760368347,
      "rms_normalized_to_uniform_percent": 0.12515425692458554
    },
    "south": {
      "bias_percent": 0.014675501709739618,
      "rms_normalized_error_percent": 0.21923335404977287,
      "absolute_error": {
        "p95": 0.03146177679300308,
        "p99": 0.036896680593490605,
        "maximum": 0.03999745845794678
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.5843048095703125,
      "reference_fraction_of_uniform": 0.20718662440776825,
      "rms_normalized_to_uniform_percent": 0.06763215534457188
    },
    "west": {
      "bias_percent": 0.14404499325654888,
      "rms_normalized_error_percent": 0.3786516038652594,
      "absolute_error": {
        "p95": 0.04576779007911681,
        "p99": 0.06939304113388065,
        "maximum": 0.07875728607177734
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.695645332336426,
      "reference_fraction_of_uniform": 0.2136225402355194,
      "rms_normalized_to_uniform_percent": 0.10258356716068072
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
        "identifier": "plan_l_distributed_grid",
        "sensor_count": 48,
        "illuminance": {
          "nmbe_percent": 0.01992200810742269,
          "cvrmse_percent": 1.5005065666115058,
          "absolute_error_percentiles_lux": {
            "p50": 3.3841552734375,
            "p90": 20.987847900390626,
            "p95": 30.311532592773435,
            "p99": 54.312358398437425
          },
          "maximum_absolute_error_lux": 170.244140625,
          "worst": {
            "sensor_index": 40,
            "position": [
              5.5,
              1.5,
              0.75
            ],
            "hour_of_year": 1861.5,
            "foton_lux": 11808.57421875,
            "radiance_lux": 11638.330078125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.39226883561643816,
            "maximum_error_percentage_points": 2.052739726027397,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1866644483065308,
            "maximum_error_percentage_points": 1.1137042141668232,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.1177654109589041,
            "maximum_error_percentage_points": 1.096986301369867,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.1302397260273973,
            "maximum_error_percentage_points": 1.096986301369867,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.018433219178082192,
            "maximum_error_percentage_points": 0.19630136986301494,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 70.83333333333333,
          "radiance_percent": 70.83333333333333,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.0833333333333335,
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
            "identifier": "plan_l_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_l_distributed_grid",
            "maximum_error_percentage_points": 0.004563891267125086,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_l_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_l_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_l_distributed_grid",
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
      "study_preparation_seconds": 0.3870553390006535,
      "weather_seconds": 0.24045604599814396,
      "metric_reduction_seconds": 0.1932703999991645,
      "write_seconds": 0.04207722800128977,
      "total_seconds": 0.47614914800215047,
      "cold_end_to_end_seconds": 0.8632044870028039,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.02893312099695322,
      "engine_upload_seconds": 0.014361936,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.014419748,
      "engine_annual_reduction_seconds": 0.008008399,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.014419748
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3870553390006535,
      "weather_seconds": 0.2492480639994028,
      "metric_reduction_seconds": 0.17621439099821146,
      "write_seconds": 0.02536431599946809,
      "total_seconds": 0.45110175000081654,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.45110175000081654,
      "raw_export_seconds": 0.010079009000037331,
      "engine_upload_seconds": 0.013702395,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.9e-08,
      "engine_annual_reduction_seconds": 0.008063622,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.014303232997917803,
      "full": 0.024809293998259818
    }
  },
  "elapsed_seconds": 2.774920302003011,
  "result_class": "passed"
}
```
