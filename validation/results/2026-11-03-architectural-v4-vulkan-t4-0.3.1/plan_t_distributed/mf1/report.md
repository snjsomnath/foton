# Foton report

Status: **passed**

```json
{
  "scene": "plan_t_distributed",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_t_distributed",
    "category": "form",
    "question": "How does a distributed opening illuminate a T-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "t",
    "window_profile": "distributed"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 8,
    "shades": 0,
    "sensors": 54,
    "floor_area": 63.0,
    "aperture_area": 9.6
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "1c5f3c535a737df8b0448084442da041e927e18dcbda2276bf46aea926de981c",
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 15359727019794020790,
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 15359727019794020790,
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
    "model_sha256": "1af1d0674993c2b846c34bc8cb29d3afcad438ff30fdb5a0242b1043fdf27d56",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "ac3c34594b2170933cb2e75470e0a8f06dd50696589dcbda19cdd379ce27d048",
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
          "p95": 4.7414680011570454e-05,
          "p99": 0.0001686424762010605
        },
        "bias_percent": 0.12369520308831125,
        "identifier": "plan_t_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.4978379597748495,
        "worst_index": [
          52,
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
          "maximum": 0.0007280968129634857,
          "p95": 8.07971809990704e-05,
          "p99": 0.000168159224558622
        },
        "bias_percent": 0.10068887529576356,
        "identifier": "plan_t_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.00211264416208,
        "worst_index": [
          42,
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
          "maximum": 0.00046384334564208984,
          "p95": 6.611272692680359e-05,
          "p99": 0.00013934651389718172
        },
        "bias_percent": -0.017571714715765508,
        "identifier": "plan_t_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8190633739709476,
        "worst_index": [
          53,
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
            "identifier": "plan_t_distributed_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0011168411001563072,
                  "p50": 0.0,
                  "p90": 9.394600056111813e-05,
                  "p95": 0.00020439294166862965,
                  "p99": 0.00042390850809170014
                },
                "candidate_energy": 15.784453150160456,
                "cvrmse_percent": 13.58751399588432,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.06170981852087443,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 15.774718599940254,
                "relative_energy_error_percent": 0.06170981852087443,
                "rms_normalized_rmse_percent": 3.757094784616206,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.015606139786541462,
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "reference": 0.01672298088669777,
                  "rgb_channel": 0,
                  "sky_patch_index": 116
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001897340640425682,
                  "p50": 0.0,
                  "p90": 0.00015420740965055302,
                  "p95": 0.0003068842925131321,
                  "p99": 0.0006776358466595456
                },
                "candidate_energy": 4.708933268446671,
                "cvrmse_percent": 71.01255348416953,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.20870317996289336,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.718781515525073,
                "relative_energy_error_percent": 0.20870317996289334,
                "rms_normalized_rmse_percent": 4.441299886041969,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02450086921453476,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.02639820985496044,
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.03895800933242,
            "full": 364.72824995871633
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 145.43495804537088,
            "full": 351.17183392867446
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.73079205304384,
            "full": 353.99320803117007
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.71012508310378,
            "full": 337.36908400896937
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
            "identifier": "plan_t_distributed_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004941995721310377,
                  "p50": 0.0,
                  "p90": 4.6665314584970474e-05,
                  "p95": 9.576810407452285e-05,
                  "p99": 0.00021052767406217756
                },
                "candidate_energy": 15.769208669991357,
                "cvrmse_percent": 6.674122982431898,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.015898707489463704,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 15.766701968164703,
                "relative_energy_error_percent": 0.015898707489463704,
                "rms_normalized_rmse_percent": 1.8465379797468535,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0017605534521862864,
                  "global_sensor_index": 52,
                  "local_sensor_index": 52,
                  "reference": 0.002254753024317324,
                  "rgb_channel": 0,
                  "sky_patch_index": 9
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009794961661100388,
                  "p50": 1.03870752354851e-05,
                  "p90": 8.4126484580338e-05,
                  "p95": 0.00015850088675506413,
                  "p99": 0.0003533801966113977
                },
                "candidate_energy": 8.91217930618544,
                "cvrmse_percent": 19.84968948293527,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1678227758953249,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.897247698120172,
                "relative_energy_error_percent": 0.16782277589532485,
                "rms_normalized_rmse_percent": 1.888283399556084,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03643901087343693,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.03545951470732689,
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 211.46887494251132,
            "full": 3777.1421660436317
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 206.25295804347843,
            "full": 3785.876917070709
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 206.01504191290587,
            "full": 3864.17449999135
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 214.65412492398173,
            "full": 3848.4301660209894
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
            "identifier": "plan_t_distributed_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005965153686702251,
                  "p50": 0.0,
                  "p90": 4.5973458327353e-05,
                  "p95": 9.386707097291946e-05,
                  "p99": 0.00020641124050598631
                },
                "candidate_energy": 15.774012945194578,
                "cvrmse_percent": 6.434955324921082,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.0075553949379344445,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 15.775204824221316,
                "relative_energy_error_percent": 0.007555394937934444,
                "rms_normalized_rmse_percent": 1.780216164053853,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.014138050377368927,
                  "global_sensor_index": 49,
                  "local_sensor_index": 49,
                  "reference": 0.013541535008698702,
                  "rgb_channel": 0,
                  "sky_patch_index": 67
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007756557315587997,
                  "p50": 1.0485557140782475e-05,
                  "p90": 8.336108294315636e-05,
                  "p95": 0.00015194900333881378,
                  "p99": 0.0003250659490004219
                },
                "candidate_energy": 8.930159650705018,
                "cvrmse_percent": 18.946486332089815,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1627948248410944,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.91564544132536,
                "relative_energy_error_percent": 0.1627948248410944,
                "rms_normalized_rmse_percent": 1.8038644631017662,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04050794057548046,
                  "global_sensor_index": 43,
                  "local_sensor_index": 43,
                  "reference": 0.03973228484392166,
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 203.03108298685402,
            "full": 4030.6550840614364
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 197.34700000844896,
            "full": 3992.700583068654
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 198.59708298463374,
            "full": 4058.5839999839664
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 201.13337505608797,
            "full": 4027.564249932766
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
            "identifier": "plan_t_distributed_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00023897504433989525,
                  "p50": 0.0,
                  "p90": 2.5633838959038258e-05,
                  "p95": 5.805725231766701e-05,
                  "p99": 0.00012120418949052723
                },
                "candidate_energy": 15.771213558041058,
                "cvrmse_percent": 3.7667452274408237,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.02400982182044271,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 15.77500110769919,
                "relative_energy_error_percent": 0.02400982182044271,
                "rms_normalized_rmse_percent": 1.0424382251882474,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.015170984901487827,
                  "global_sensor_index": 52,
                  "local_sensor_index": 52,
                  "reference": 0.014932009857147932,
                  "rgb_channel": 0,
                  "sky_patch_index": 92
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010502859950065613,
                  "p50": 7.0354922172555234e-06,
                  "p90": 4.890657146461308e-05,
                  "p95": 8.93929973244667e-05,
                  "p99": 0.00019440665375441315
                },
                "candidate_energy": 8.91626906368582,
                "cvrmse_percent": 11.97665885009485,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.08505830324812667,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.923859547200916,
                "relative_energy_error_percent": 0.08505830324812667,
                "rms_normalized_rmse_percent": 1.1403487483934966,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.041623955592513084,
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "reference": 0.042674241587519646,
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 304.7717500012368,
            "full": 7187.169166980311
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 307.234917068854,
            "full": 7153.644083067775
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 311.21299997903407,
            "full": 7085.051249945536
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 310.6525420444086,
            "full": 7093.472666922025
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
    "/content/suite-vulkan-0.3.1/plan_t_distributed/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1730.89116695337,
      "invocation_count": 4,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 6476.486333063804,
      "invocation_count": 4,
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
      54,
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
        "identifier": "plan_t_distributed_grid",
        "full_identifier": "plan_t_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": -0.21030369646884745,
            "cvrmse_percent": 3.3546372884168414,
            "rms_normalized_rmse_percent": 0.9280068700479971,
            "reference_energy": 15.776927444376497,
            "candidate_energy": 15.743747982771765,
            "relative_energy_error_percent": 0.21030369646884747,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2784759746864438e-05,
              "p95": 3.661305527202785e-05,
              "p99": 0.0001060298876836931,
              "maximum": 0.00037631718441843987
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 133,
              "rgb_channel": 0,
              "reference": 0.006344357039779425,
              "candidate": 0.0067206742241978645,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.21648054209644896,
            "cvrmse_percent": 15.546643693457664,
            "rms_normalized_rmse_percent": 1.4794529956719795,
            "reference_energy": 8.91624422046604,
            "candidate_energy": 8.896942286642933,
            "relative_energy_error_percent": 0.21648054209644899,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.565827551530674e-05,
              "p90": 5.5152224376797676e-05,
              "p95": 7.865618681535125e-05,
              "p99": 0.00017903594009112956,
              "maximum": 0.0014539174735546112
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.030094146728515625,
              "candidate": 0.028640229254961014,
              "position": [
                6.5,
                7.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.2125340403418553,
            "cvrmse_percent": 5.352226153146636,
            "rms_normalized_rmse_percent": 1.41056759382782,
            "reference_energy": 24.693171664842538,
            "candidate_energy": 24.640690269414698,
            "relative_energy_error_percent": 0.21253404034185533,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.5373794667539187e-05,
              "p90": 5.288515239953995e-05,
              "p95": 7.1654561907053e-05,
              "p99": 0.00014400684274733087,
              "maximum": 0.0014539174735546112
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.030094146728515625,
              "candidate": 0.028640229254961014,
              "position": [
                6.5,
                7.5,
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
      54,
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
        "identifier": "plan_t_distributed_grid",
        "full_identifier": "plan_t_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": -0.21030369646884745,
            "cvrmse_percent": 3.3546372884168414,
            "rms_normalized_rmse_percent": 0.9280068700479971,
            "reference_energy": 15.776927444376497,
            "candidate_energy": 15.743747982771765,
            "relative_energy_error_percent": 0.21030369646884747,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2784759746864438e-05,
              "p95": 3.661305527202785e-05,
              "p99": 0.0001060298876836931,
              "maximum": 0.00037631718441843987
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 133,
              "rgb_channel": 0,
              "reference": 0.006344357039779425,
              "candidate": 0.0067206742241978645,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 88.63378383978065,
            "cvrmse_percent": 514.7331911348981,
            "rms_normalized_rmse_percent": 32.17394600245359,
            "reference_energy": 4.716515835890618,
            "candidate_energy": 8.896942286642933,
            "relative_energy_error_percent": 88.63378383978066,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 8.355574516372144e-05,
              "p90": 0.00019642477855086327,
              "p95": 0.0002457000082358718,
              "p99": 0.00045536783291027285,
              "maximum": 0.015784282237291336
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026409026235342026,
              "candidate": 0.04219330847263336,
              "position": [
                1.5,
                11.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.236945702242803,
            "cvrmse_percent": 118.43099751774712,
            "rms_normalized_rmse_percent": 32.16482401756764,
            "reference_energy": 20.493443280267115,
            "candidate_energy": 24.640690269414698,
            "relative_energy_error_percent": 20.236945702242803,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 8.285000149044208e-05,
              "p90": 0.0001943303068401292,
              "p95": 0.0002423844998702407,
              "p99": 0.0004083311147405869,
              "maximum": 0.015784282237291336
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026409026235342026,
              "candidate": 0.04219330847263336,
              "position": [
                1.5,
                11.5,
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
      "bias_percent": -0.047577935596051994,
      "rms_normalized_error_percent": 0.30094566433304776,
      "absolute_error": {
        "p95": 0.12300472919189687,
        "p99": 0.22062900978349828,
        "maximum": 0.2367549717548414
      },
      "worst_index": [
        47
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 20.64236268677308,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.30094566433304776
    },
    "overcast": {
      "bias_percent": -0.017627687202469,
      "rms_normalized_error_percent": 0.25607807881144545,
      "absolute_error": {
        "p95": 0.0783280849456786,
        "p99": 0.11848060607910153,
        "maximum": 0.13391494750976562
      },
      "worst_index": [
        47
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 13.239574432373047,
      "reference_fraction_of_uniform": 0.6413788199424744,
      "rms_normalized_to_uniform_percent": 0.1741849783132553
    },
    "horizon": {
      "bias_percent": -0.3221485481355524,
      "rms_normalized_error_percent": 1.45011262647551,
      "absolute_error": {
        "p95": 0.06922504784898703,
        "p99": 0.08804638525363832,
        "maximum": 0.09835470278523406
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.2701069895078905,
      "reference_fraction_of_uniform": 0.10997321498291944,
      "rms_normalized_to_uniform_percent": 0.13045640927823277
    },
    "north": {
      "bias_percent": -0.10142708092879768,
      "rms_normalized_error_percent": 0.39003790300620045,
      "absolute_error": {
        "p95": 0.05389381647109984,
        "p99": 0.06284228563308714,
        "maximum": 0.07004427909851074
      },
      "worst_index": [
        47
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.9056971073150635,
      "reference_fraction_of_uniform": 0.18920785188674927,
      "rms_normalized_to_uniform_percent": 0.09745354810387956
    },
    "east": {
      "bias_percent": -0.15483210853647048,
      "rms_normalized_error_percent": 0.41110107057283857,
      "absolute_error": {
        "p95": 0.07375855445861809,
        "p99": 0.12231400489807129,
        "maximum": 0.1259021759033203
      },
      "worst_index": [
        47
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.586851119995117,
      "reference_fraction_of_uniform": 0.270649790763855,
      "rms_normalized_to_uniform_percent": 0.14046751731318424
    },
    "south": {
      "bias_percent": 0.06511993638895033,
      "rms_normalized_error_percent": 0.3882210307682479,
      "absolute_error": {
        "p95": 0.08450386524200439,
        "p99": 0.09111376762390136,
        "maximum": 0.09479999542236328
      },
      "worst_index": [
        48
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.29907751083374,
      "reference_fraction_of_uniform": 0.3535970151424408,
      "rms_normalized_to_uniform_percent": 0.15977474141220602
    },
    "west": {
      "bias_percent": -0.1391628667817363,
      "rms_normalized_error_percent": 0.35513318344179007,
      "absolute_error": {
        "p95": 0.06128549575805658,
        "p99": 0.09674582004547119,
        "maximum": 0.09912824630737305
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.484899044036865,
      "reference_fraction_of_uniform": 0.26571083068847656,
      "rms_normalized_to_uniform_percent": 0.12006855775781525
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
        "identifier": "plan_t_distributed_grid",
        "sensor_count": 54,
        "illuminance": {
          "nmbe_percent": -0.03695833269999258,
          "cvrmse_percent": 1.3689212804596176,
          "absolute_error_percentiles_lux": {
            "p50": 5.329559326171875,
            "p90": 29.11213073730469,
            "p95": 40.61458435058593,
            "p99": 70.74776428222656
          },
          "maximum_absolute_error_lux": 266.423828125,
          "worst": {
            "sensor_index": 0,
            "position": [
              0.5,
              11.5,
              0.75
            ],
            "hour_of_year": 2725.5,
            "foton_lux": 21866.150390625,
            "radiance_lux": 21599.7265625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.17912734652460702,
            "maximum_error_percentage_points": 1.2920547945205527,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.07175947492826316,
            "maximum_error_percentage_points": 0.48418218247968525,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.06386352105530187,
            "maximum_error_percentage_points": 0.3558904109589065,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.07514967021816227,
            "maximum_error_percentage_points": 0.3558904109589065,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.03542110603754426,
            "maximum_error_percentage_points": 0.18794520547945304,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.0,
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
      "maximum_error_percentage_points": 0.004980736301362754,
      "metrics": {
        "da": [
          {
            "identifier": "plan_t_distributed_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_t_distributed_grid",
            "maximum_error_percentage_points": 0.004980736301362754,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_t_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_t_distributed_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_t_distributed_grid",
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
      "study_preparation_seconds": 0.3788266310002655,
      "weather_seconds": 0.22195509399898583,
      "metric_reduction_seconds": 0.21095106400025543,
      "write_seconds": 0.04656728999543702,
      "total_seconds": 0.47994916099560214,
      "cold_end_to_end_seconds": 0.8587757919958676,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.033547532002558,
      "engine_upload_seconds": 0.014206386,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.018016598,
      "engine_annual_reduction_seconds": 0.009208835,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.018016598
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3788266310002655,
      "weather_seconds": 0.24791713499871548,
      "metric_reduction_seconds": 0.19087717799993698,
      "write_seconds": 0.022132437996333465,
      "total_seconds": 0.4612182609998854,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.4612182609998854,
      "raw_export_seconds": 0.009961930001736619,
      "engine_upload_seconds": 0.014185273,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 8.2e-08,
      "engine_annual_reduction_seconds": 0.009285852,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.014540620002662763,
      "full": 0.027460981997137424
    }
  },
  "elapsed_seconds": 2.7769647980021546,
  "result_class": "passed"
}
```
