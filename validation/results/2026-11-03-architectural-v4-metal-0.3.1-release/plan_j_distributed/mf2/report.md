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
  "model_sha256": "5d964eb23b088323d3a60fb906fc4301048f48f7b9e3dbe7ddb240b5de7cbd9e",
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
      "scene_fingerprint": 12112216450189513340,
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
      "scene_fingerprint": 12112216450189513340,
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/suite-0.3.1/run/plan_j_distributed/mf2/oracle/scene.rad"
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
            "nmbe_percent": -0.24330066945045214,
            "cvrmse_percent": 4.101148751290915,
            "rms_normalized_rmse_percent": 0.9675902835211223,
            "reference_energy": 11.693547670222983,
            "candidate_energy": 11.665097190458823,
            "relative_energy_error_percent": 0.2433006694504521,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.3387762010097504e-08,
              "p95": 2.0561274141073227e-06,
              "p99": 2.2016349248588085e-05,
              "maximum": 0.00016737228725105524
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 117,
              "rgb_channel": 0,
              "reference": 0.0009160776971839368,
              "candidate": 0.0007487054099328816,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.29459110579676,
            "cvrmse_percent": 19.36086603442708,
            "rms_normalized_rmse_percent": 1.0696866108521943,
            "reference_energy": 7.219695077840029,
            "candidate_energy": 7.2409636574049925,
            "relative_energy_error_percent": 0.29459110579676,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.020184860564768e-06,
              "p90": 1.572177279740572e-05,
              "p95": 2.5396235287189484e-05,
              "p99": 5.829217843711376e-05,
              "maximum": 0.0005698725581169128
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03913457691669464,
              "candidate": 0.039704449474811554,
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
            "nmbe_percent": -0.03797286533496534,
            "cvrmse_percent": 7.068496789364156,
            "rms_normalized_rmse_percent": 1.0230714987495966,
            "reference_energy": 18.913242748063013,
            "candidate_energy": 18.906060847863813,
            "relative_energy_error_percent": 0.037972865334979435,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.010576958535239e-06,
              "p90": 1.5443831216543913e-05,
              "p95": 2.409704029560089e-05,
              "p99": 5.3494004532694817e-05,
              "maximum": 0.0005698725581169128
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03913457691669464,
              "candidate": 0.039704449474811554,
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
            "nmbe_percent": -0.24330066945045214,
            "cvrmse_percent": 4.101148751290915,
            "rms_normalized_rmse_percent": 0.9675902835211223,
            "reference_energy": 11.693547670222983,
            "candidate_energy": 11.665097190458823,
            "relative_energy_error_percent": 0.2433006694504521,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.3387762010097504e-08,
              "p95": 2.0561274141073227e-06,
              "p99": 2.2016349248588085e-05,
              "maximum": 0.00016737228725105524
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 117,
              "rgb_channel": 0,
              "reference": 0.0009160776971839368,
              "candidate": 0.0007487054099328816,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 95.12674562043472,
            "cvrmse_percent": 1130.7854580634898,
            "rms_normalized_rmse_percent": 44.70802784685068,
            "reference_energy": 3.7109026926991806,
            "candidate_energy": 7.2409636574049925,
            "relative_energy_error_percent": 95.12674562043473,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.9836955289065372e-05,
              "p90": 5.425999916042201e-05,
              "p95": 7.524635293520987e-05,
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
            "nmbe_percent": 22.73116146597398,
            "cvrmse_percent": 272.38335218639327,
            "rms_normalized_rmse_percent": 44.70462940912725,
            "reference_energy": 15.404450362922164,
            "candidate_energy": 18.906060847863813,
            "relative_energy_error_percent": 22.731161465973962,
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
      "bias_percent": -0.09082908647148294,
      "rms_normalized_error_percent": 0.2588150365419545,
      "absolute_error": {
        "p95": 0.12334156620924726,
        "p99": 0.21900150862526757,
        "maximum": 0.28726650462897396
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 17.90403306644751,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2588150365419545
    },
    "overcast": {
      "bias_percent": -0.0591518590069775,
      "rms_normalized_error_percent": 0.20197953917574224,
      "absolute_error": {
        "p95": 0.05770182609558099,
        "p99": 0.11808469772338862,
        "maximum": 0.153533935546875
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 11.62510871887207,
      "reference_fraction_of_uniform": 0.6493011116981506,
      "rms_normalized_to_uniform_percent": 0.13920518879747806
    },
    "horizon": {
      "bias_percent": 0.053258016754219845,
      "rms_normalized_error_percent": 1.2130228727605814,
      "absolute_error": {
        "p95": 0.040414956362475406,
        "p99": 0.06423613185099007,
        "maximum": 0.06784471030318118
      },
      "worst_index": [
        39
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.722544906287882,
      "reference_fraction_of_uniform": 0.09620988186823465,
      "rms_normalized_to_uniform_percent": 0.08942991737470428
    },
    "north": {
      "bias_percent": -0.254418684018977,
      "rms_normalized_error_percent": 0.47079548120165077,
      "absolute_error": {
        "p95": 0.09979610443115232,
        "p99": 0.15285356521606444,
        "maximum": 0.1555633544921875
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.071594715118408,
      "reference_fraction_of_uniform": 0.3391188085079193,
      "rms_normalized_to_uniform_percent": 0.1750088783394158
    },
    "east": {
      "bias_percent": -0.03884466968975173,
      "rms_normalized_error_percent": 0.2076925523455375,
      "absolute_error": {
        "p95": 0.03209246397018432,
        "p99": 0.03577933311462402,
        "maximum": 0.037502288818359375
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.23331356048584,
      "reference_fraction_of_uniform": 0.23644468188285828,
      "rms_normalized_to_uniform_percent": 0.06417297675228346
    },
    "south": {
      "bias_percent": 0.024645207885641802,
      "rms_normalized_error_percent": 0.15742901466111733,
      "absolute_error": {
        "p95": 0.024789381027221676,
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
      "rms_normalized_to_uniform_percent": 0.04912551017326363
    },
    "west": {
      "bias_percent": -0.14525443591674306,
      "rms_normalized_error_percent": 0.4483309525383209,
      "absolute_error": {
        "p95": 0.04750308990478513,
        "p99": 0.12945220947265615,
        "maximum": 0.18216609954833984
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.175545692443848,
      "reference_fraction_of_uniform": 0.2890715003013611,
      "rms_normalized_to_uniform_percent": 0.1387592034008185
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
          "nmbe_percent": 0.004513305414968747,
          "cvrmse_percent": 1.73311217977707,
          "absolute_error_percentiles_lux": {
            "p50": 3.006256103515625,
            "p90": 21.04598388671876,
            "p95": 31.676647949218726,
            "p99": 66.99856933593753
          },
          "maximum_absolute_error_lux": 293.7939453125,
          "worst": {
            "sensor_index": 5,
            "position": [
              1.5,
              4.5,
              0.75
            ],
            "hour_of_year": 4448.5,
            "foton_lux": 13185.080078125,
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
      "study_preparation_seconds": 0.0074860419845208526,
      "weather_seconds": 0.09961274999659508,
      "metric_reduction_seconds": 0.15480645804200321,
      "write_seconds": 0.04057170799933374,
      "total_seconds": 0.2951371669769287,
      "cold_end_to_end_seconds": 0.30262320896144956,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.02198341698385775,
      "engine_upload_seconds": 0.0008383749999999999,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.10000112489797175,
      "engine_annual_reduction_seconds": 0.0021092500537633896,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.10000112489797175
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.0074860419845208526,
      "weather_seconds": 0.10029037506319582,
      "metric_reduction_seconds": 0.04689645895268768,
      "write_seconds": 0.03467325004749,
      "total_seconds": 0.1820292080519721,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1820292080519721,
      "raw_export_seconds": 0.013980875024572015,
      "engine_upload_seconds": 8.175e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0020379999186843634,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01247208402492106,
      "full": 0.10310995893087238
    }
  },
  "elapsed_seconds": 1.4104831670410931,
  "result_class": "passed"
}
```
