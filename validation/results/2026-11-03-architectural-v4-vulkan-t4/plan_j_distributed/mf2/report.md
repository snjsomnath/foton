# Foton report

Status: **passed**

```json
{
  "scene": "plan_j_distributed",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_j_distributed",
    "category": "form",
    "question": "How does a distributed opening illuminate a J-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "j",
    "window_profile": "distributed"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 8,
    "shades": 0,
    "sensors": 47,
    "floor_area": 63.0,
    "aperture_area": 9.6
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "ecf76d891c5940ac607b49f9d424d1466006c7c6173341ddae306a132170c50b",
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
      "scene_fingerprint": 12112216450189513340,
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
      "scene_fingerprint": 12112216450189513340,
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
    "model_sha256": "f531a21d60afaa1c32abd8ac8222729e859983cccbc4dbe490b6df200829363a",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "23633e9e91bc013f4a3a6d776a0b95fe8d48adfbd13e89c51c834683d9ee6bfe",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00013830000534653664,
          "p95": 1.7549609765410423e-06,
          "p99": 2.1459069103002548e-05
        },
        "bias_percent": 0.02758189141148551,
        "identifier": "plan_j_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8702987838515097,
        "worst_index": [
          1,
          522,
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
          "maximum": 0.0007255598902702332,
          "p95": 4.4248066842556e-05,
          "p99": 0.00011633231770247221
        },
        "bias_percent": 0.04023416265887518,
        "identifier": "plan_j_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.504592377900902,
        "worst_index": [
          5,
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
          "maximum": 0.0006468668580055237,
          "p95": 3.749394090846181e-05,
          "p99": 9.367265738546848e-05
        },
        "bias_percent": 0.038239581982908256,
        "identifier": "plan_j_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.2724484146598203,
        "worst_index": [
          5,
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
            "identifier": "plan_j_distributed_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005705400835722685,
                  "p50": 0.0,
                  "p90": 9.919749572873116e-07,
                  "p95": 8.586365584051237e-05,
                  "p99": 0.0002242045011371374
                },
                "candidate_energy": 11.697352579643777,
                "cvrmse_percent": 28.940728434501825,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.025153699227368587,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.700295636816975,
                "relative_energy_error_percent": 0.025153699227368584,
                "rms_normalized_rmse_percent": 6.821149455773818,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0035991331096738577,
                  "global_sensor_index": 30,
                  "local_sensor_index": 30,
                  "reference": 0.003028593026101589,
                  "rgb_channel": 0,
                  "sky_patch_index": 248
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008944105356931686,
                  "p50": 0.0,
                  "p90": 4.097384226042777e-05,
                  "p95": 0.00011948528117500246,
                  "p99": 0.00031834200490266085
                },
                "candidate_energy": 3.7174983119884537,
                "cvrmse_percent": 138.0082594116668,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.642816584246009,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.69375424710676,
                "relative_energy_error_percent": 0.642816584246009,
                "rms_normalized_rmse_percent": 5.437655965709082,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.019326400011777878,
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "reference": 0.020220810547471046,
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.43179207388312,
            "full": 289.77633407339454
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.9457920724526,
            "full": 290.5564169632271
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.23779199365526,
            "full": 293.7247919617221
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.2957079699263,
            "full": 304.1686658980325
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
            "identifier": "plan_j_distributed_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004077500198036432,
                  "p50": 0.0,
                  "p90": 1.743258167152817e-06,
                  "p95": 5.434740160126239e-05,
                  "p99": 0.00015330297173932195
                },
                "candidate_energy": 11.687857962600027,
                "cvrmse_percent": 20.26212971816126,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.05153375214681554,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.693884259930876,
                "relative_energy_error_percent": 0.051533752146815534,
                "rms_normalized_rmse_percent": 4.779820915461486,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0036910774651914835,
                  "global_sensor_index": 41,
                  "local_sensor_index": 41,
                  "reference": 0.004098827484995127,
                  "rgb_channel": 0,
                  "sky_patch_index": 300
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007519256323575974,
                  "p50": 4.951194796376512e-06,
                  "p90": 3.075731910939794e-05,
                  "p95": 8.455506758764386e-05,
                  "p99": 0.00022434699349105358
                },
                "candidate_energy": 7.209663105925344,
                "cvrmse_percent": 50.99093002146761,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.05897512566508426,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.205413704138639,
                "relative_energy_error_percent": 0.05897512566508426,
                "rms_normalized_rmse_percent": 2.812217134701721,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.029431375674903393,
                  "global_sensor_index": 41,
                  "local_sensor_index": 41,
                  "reference": 0.028679450042545795,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 175.33441702835262,
            "full": 3296.0330420173705
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 184.8046249942854,
            "full": 3279.6412089373916
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 183.1132499501109,
            "full": 3294.7478749556467
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 178.82429191377014,
            "full": 3314.060000004247
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
            "identifier": "plan_j_distributed_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004676756216213107,
                  "p50": 0.0,
                  "p90": 3.891736014338676e-06,
                  "p95": 6.08492991887033e-05,
                  "p99": 0.00015879713464528322
                },
                "candidate_energy": 11.69349415138366,
                "cvrmse_percent": 21.006210572053465,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.006723037440100236,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.694280362230764,
                "relative_energy_error_percent": 0.006723037440100236,
                "rms_normalized_rmse_percent": 4.955915177578472,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001380365516524762,
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "reference": 0.0009126898949034512,
                  "rgb_channel": 0,
                  "sky_patch_index": 63
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008504204452037811,
                  "p50": 4.9384634621674195e-06,
                  "p90": 3.0244029403547756e-05,
                  "p95": 8.637038990855217e-05,
                  "p99": 0.00022646994329988956
                },
                "candidate_energy": 7.208794878652878,
                "cvrmse_percent": 52.23442137599956,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.0923305633065166,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.215456950700599,
                "relative_energy_error_percent": 0.0923305633065166,
                "rms_normalized_rmse_percent": 2.879108581123901,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04205549508333206,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.04120507463812828,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 181.55841703992337,
            "full": 3538.3008749922737
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 191.28475000616163,
            "full": 3458.3818749524653
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 183.21083299815655,
            "full": 3479.0687919594347
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 185.95600000116974,
            "full": 3560.5006660334766
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
            "identifier": "plan_j_distributed_grid",
            "sensor_count": 47,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00023879448417574167,
                  "p50": 0.0,
                  "p90": 2.163404133170843e-06,
                  "p95": 3.260502126067877e-05,
                  "p99": 8.247606456279755e-05
                },
                "candidate_energy": 11.70030733022342,
                "cvrmse_percent": 11.38899258946954,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.045185447920082625,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.695022881749946,
                "relative_energy_error_percent": 0.045185447920082625,
                "rms_normalized_rmse_percent": 2.687778777310817,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001816175994463265,
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "reference": 0.0015773815102875233,
                  "rgb_channel": 0,
                  "sky_patch_index": 171
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006567612290382385,
                  "p50": 3.550548399289255e-06,
                  "p90": 2.0254101400496438e-05,
                  "p95": 4.8875343054533005e-05,
                  "p99": 0.00012458243872970343
                },
                "candidate_energy": 7.218151705983047,
                "cvrmse_percent": 30.06800202552241,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.07137282296956579,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.2130035817058875,
                "relative_energy_error_percent": 0.07137282296956579,
                "rms_normalized_rmse_percent": 1.6611800223488815,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04358101449906826,
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "reference": 0.0442377757281065,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 279.56704096868634,
            "full": 6052.823874983005
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 274.99562490265816,
            "full": 6177.701042033732
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 280.07516695652157,
            "full": 6145.0134590268135
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 272.0705420942977,
            "full": 6122.1883749822155
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/plan_j_distributed/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4578.289874945767,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_j_distributed/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 18494.91887493059,
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
        "identifier": "plan_j_distributed_grid",
        "full_identifier": "plan_j_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": -0.24330259137774418,
            "cvrmse_percent": 4.10114861531818,
            "rms_normalized_rmse_percent": 0.9675902514408674,
            "reference_energy": 11.693547670222983,
            "candidate_energy": 11.66509696571734,
            "relative_energy_error_percent": 0.2433025913777442,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.30385160446167e-08,
              "p95": 2.0561274141073227e-06,
              "p99": 2.2016349248588085e-05,
              "maximum": 0.00016737217083573341
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 117,
              "rgb_channel": 0,
              "reference": 0.0009160776971839368,
              "candidate": 0.0007487055263482034,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.29438949967347555,
            "cvrmse_percent": 19.360744114565755,
            "rms_normalized_rmse_percent": 1.0696798747876495,
            "reference_energy": 7.219695077840029,
            "candidate_energy": 7.240949102057633,
            "relative_energy_error_percent": 0.2943894996734756,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.0197955968324095e-06,
              "p90": 1.572177279740572e-05,
              "p95": 2.5396235287189484e-05,
              "p99": 5.829217843711376e-05,
              "maximum": 0.0005698837339878082
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03913457691669464,
              "candidate": 0.03970446065068245,
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
            "nmbe_percent": -0.0380510121077867,
            "cvrmse_percent": 7.0684491304822465,
            "rms_normalized_rmse_percent": 1.0230646007562612,
            "reference_energy": 18.913242748063013,
            "candidate_energy": 18.906046067774973,
            "relative_energy_error_percent": 0.038051012107782,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.010399607068393e-06,
              "p90": 1.5443802112713456e-05,
              "p95": 2.40975059568882e-05,
              "p99": 5.3494004532694817e-05,
              "maximum": 0.0005698837339878082
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03913457691669464,
              "candidate": 0.03970446065068245,
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
        "identifier": "plan_j_distributed_grid",
        "full_identifier": "plan_j_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": -0.24330259137774418,
            "cvrmse_percent": 4.10114861531818,
            "rms_normalized_rmse_percent": 0.9675902514408674,
            "reference_energy": 11.693547670222983,
            "candidate_energy": 11.66509696571734,
            "relative_energy_error_percent": 0.2433025913777442,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.30385160446167e-08,
              "p95": 2.0561274141073227e-06,
              "p99": 2.2016349248588085e-05,
              "maximum": 0.00016737217083573341
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 117,
              "rgb_channel": 0,
              "reference": 0.0009160776971839368,
              "candidate": 0.0007487055263482034,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 95.12635338844792,
            "cvrmse_percent": 1130.7765131866167,
            "rms_normalized_rmse_percent": 44.707674191962866,
            "reference_energy": 3.7109026926991806,
            "candidate_energy": 7.240949102057633,
            "relative_energy_error_percent": 95.12635338844794,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.9836955289065372e-05,
              "p90": 5.425999916042201e-05,
              "p95": 7.524000102421269e-05,
              "p99": 0.00016649486497044563,
              "maximum": 0.018756015226244926
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02964901365339756,
              "candidate": 0.04840502887964249,
              "position": [
                0.5,
                4.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 22.73106551909827,
            "cvrmse_percent": 272.381197156688,
            "rms_normalized_rmse_percent": 44.70427571715758,
            "reference_energy": 15.404450362922164,
            "candidate_energy": 18.906046067774973,
            "relative_energy_error_percent": 22.731065519098273,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.9749999410123564e-05,
              "p90": 5.3870000556344166e-05,
              "p95": 7.415121945086867e-05,
              "p99": 0.00016454304568469524,
              "maximum": 0.018756015226244926
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02964901365339756,
              "candidate": 0.04840502887964249,
              "position": [
                0.5,
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
      "bias_percent": -0.09081260379098391,
      "rms_normalized_error_percent": 0.2588794086652851,
      "absolute_error": {
        "p95": 0.12333665506768236,
        "p99": 0.21902041505838057,
        "maximum": 0.2873120246865284
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 17.90403306644751,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2588794086652851
    },
    "overcast": {
      "bias_percent": -0.05912279750557969,
      "rms_normalized_error_percent": 0.20203859137640928,
      "absolute_error": {
        "p95": 0.05770244598388666,
        "p99": 0.11809429168701166,
        "maximum": 0.15356063842773438
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 11.62510871887207,
      "reference_fraction_of_uniform": 0.6493011116981506,
      "rms_normalized_to_uniform_percent": 0.1392459029725359
    },
    "horizon": {
      "bias_percent": 0.05322086817473972,
      "rms_normalized_error_percent": 1.2130238043253676,
      "absolute_error": {
        "p95": 0.04041490892268544,
        "p99": 0.0642369686276702,
        "maximum": 0.06784470444239732
      },
      "worst_index": [
        39
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.722544906287882,
      "reference_fraction_of_uniform": 0.09620988186823465,
      "rms_normalized_to_uniform_percent": 0.08942998605416921
    },
    "north": {
      "bias_percent": -0.25439067709815283,
      "rms_normalized_error_percent": 0.4708386434287956,
      "absolute_error": {
        "p95": 0.09979710578918455,
        "p99": 0.1528609275817871,
        "maximum": 0.15555667877197266
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.071594715118408,
      "reference_fraction_of_uniform": 0.3391188085079193,
      "rms_normalized_to_uniform_percent": 0.17502491359991468
    },
    "east": {
      "bias_percent": -0.038841060005201905,
      "rms_normalized_error_percent": 0.20769673144352627,
      "absolute_error": {
        "p95": 0.03209246397018432,
        "p99": 0.035776834487915035,
        "maximum": 0.03749847412109375
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.23331356048584,
      "reference_fraction_of_uniform": 0.23644468188285828,
      "rms_normalized_to_uniform_percent": 0.06417426651218247
    },
    "south": {
      "bias_percent": 0.024660685549337563,
      "rms_normalized_error_percent": 0.15742162162714515,
      "absolute_error": {
        "p95": 0.02478399276733398,
        "p99": 0.029175484180450437,
        "maximum": 0.03072488307952881
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.613321542739868,
      "reference_fraction_of_uniform": 0.20181606709957123,
      "rms_normalized_to_uniform_percent": 0.04912320218186539
    },
    "west": {
      "bias_percent": -0.14530824620894325,
      "rms_normalized_error_percent": 0.44838962309951463,
      "absolute_error": {
        "p95": 0.047504520416259736,
        "p99": 0.12947023391723622,
        "maximum": 0.18219947814941406
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.175545692443848,
      "reference_fraction_of_uniform": 0.2890715003013611,
      "rms_normalized_to_uniform_percent": 0.1387773505488713
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
        "identifier": "plan_j_distributed_grid",
        "sensor_count": 47,
        "illuminance": {
          "nmbe_percent": 0.00452139153158597,
          "cvrmse_percent": 1.7331331059765882,
          "absolute_error_percentiles_lux": {
            "p50": 3.0064697265625,
            "p90": 21.0454345703125,
            "p95": 31.677563476562497,
            "p99": 66.99857971191409
          },
          "maximum_absolute_error_lux": 293.79296875,
          "worst": {
            "sensor_index": 5,
            "position": [
              1.5,
              4.5,
              0.75
            ],
            "hour_of_year": 4448.5,
            "foton_lux": 13185.0791015625,
            "radiance_lux": 12891.2861328125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.37181288254153383,
            "maximum_error_percentage_points": 2.767534246575342,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.120538363225331,
            "maximum_error_percentage_points": 0.6445626887829263,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.07323229379189716,
            "maximum_error_percentage_points": 0.6576712328767087,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.07739434567181366,
            "maximum_error_percentage_points": 0.6576712328767087,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.014039638589332546,
            "maximum_error_percentage_points": 0.08547945205479479,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 65.95744680851064,
          "radiance_percent": 65.95744680851064,
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
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "plan_j_distributed_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_j_distributed_grid",
            "maximum_error_percentage_points": 0.004767364083910763,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_j_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_j_distributed_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_j_distributed_grid",
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
      "study_preparation_seconds": 0.3707570360020327,
      "weather_seconds": 0.248164923999866,
      "metric_reduction_seconds": 1.3146448850020533,
      "write_seconds": 0.0400692090006487,
      "total_seconds": 1.6032167220000701,
      "cold_end_to_end_seconds": 1.9739737580021028,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.027696647000993835,
      "engine_upload_seconds": 0.045207652,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.052065945,
      "engine_annual_reduction_seconds": 0.032231869,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.052065945
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3707570360020327,
      "weather_seconds": 0.2472887189978792,
      "metric_reduction_seconds": 1.5651204050009255,
      "write_seconds": 0.030803926001681248,
      "total_seconds": 1.8435077680005634,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 1.8435077680005634,
      "raw_export_seconds": 0.011488702999486122,
      "engine_upload_seconds": 0.046005971,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.3e-08,
      "engine_annual_reduction_seconds": 0.026030117,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.019492882001941325,
      "full": 0.0660145400033798
    }
  },
  "elapsed_seconds": 7.195077590000437,
  "result_class": "passed"
}
```
