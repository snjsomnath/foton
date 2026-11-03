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
  "model_sha256": "a8ddbb683ca1bbd715f479827288b93c8977ca7059e7a8b188f45bfb937981d1",
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
      "solver_version": "0.2.0",
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
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "plan_j_distributed_grid",
        "bias_percent": 0.027579275212866447,
        "rms_normalized_error_percent": 0.8702989876428405,
        "absolute_error": {
          "p95": 1.7549609765410423e-06,
          "p99": 2.1459069103002548e-05,
          "maximum": 0.00013830000534653664
        },
        "worst_index": [
          1,
          522,
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
        "identifier": "plan_j_distributed_grid",
        "bias_percent": 0.06561623881362658,
        "rms_normalized_error_percent": 1.5582122199599473,
        "absolute_error": {
          "p95": 4.319613799452782e-05,
          "p99": 0.00011527910828590393,
          "maximum": 0.0008328072726726532
        },
        "worst_index": [
          10,
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
        "identifier": "plan_j_distributed_grid",
        "bias_percent": 0.017335417544033865,
        "rms_normalized_error_percent": 1.2802991685036653,
        "absolute_error": {
          "p95": 3.565254155546427e-05,
          "p99": 8.975889068096876e-05,
          "maximum": 0.0007283799350261688
        },
        "worst_index": [
          10,
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
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_j_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 47,
            "stages": {
              "direct": {
                "nmbe_percent": -0.04341693699018499,
                "cvrmse_percent": 42.13012656567445,
                "rms_normalized_rmse_percent": 9.929937119559366,
                "reference_energy": 11.689669675932663,
                "candidate_energy": 11.684594379415103,
                "relative_energy_error_percent": 0.043416936990184986,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.979805347218644e-06,
                  "p95": 9.47134685702622e-05,
                  "p99": 0.00031626998679712415,
                  "maximum": 0.0009019519202411175
                },
                "worst": {
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "sky_patch_index": 337,
                  "rgb_channel": 0,
                  "reference": 0.0011721840128302574,
                  "candidate": 0.002074135933071375
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.5849949830623952,
                "cvrmse_percent": 197.85654463720525,
                "rms_normalized_rmse_percent": 7.811484422581043,
                "reference_energy": 3.7276820516864824,
                "candidate_energy": 3.7494888046733656,
                "relative_energy_error_percent": 0.5849949830623952,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.733331661554985e-05,
                  "p95": 0.00017471355386078358,
                  "p99": 0.0004580627864925191,
                  "maximum": 0.0014332793653011322
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.044717490673065186,
                  "candidate": 0.04328421130776405
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 137.72962498478591,
            "full": 298.3002089895308
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 131.81441696360707,
            "full": 306.9787500426173
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 137.85733305849135,
            "full": 311.15516705904156
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 133.01745802164078,
            "full": 294.5595000637695
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
            "identifier": "plan_j_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 47,
            "stages": {
              "direct": {
                "nmbe_percent": -6.751981948815427e-05,
                "cvrmse_percent": 20.873147999741494,
                "rms_normalized_rmse_percent": 4.92329402550674,
                "reference_energy": 11.69583369912339,
                "candidate_energy": 11.69582580211759,
                "relative_energy_error_percent": 6.751981948815427e-05,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.7551343464438105e-06,
                  "p95": 6.008890341036022e-05,
                  "p99": 0.0001558584626764059,
                  "maximum": 0.00036538601852953434
                },
                "worst": {
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "sky_patch_index": 207,
                  "rgb_channel": 0,
                  "reference": 0.002395077026449144,
                  "candidate": 0.0020296910079196095
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.05925133057149084,
                "cvrmse_percent": 52.60294084895277,
                "rms_normalized_rmse_percent": 2.8970665132158717,
                "reference_energy": 7.2060212126184915,
                "candidate_energy": 7.201751549168751,
                "relative_energy_error_percent": 0.05925133057149084,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.942294253851287e-06,
                  "p90": 3.2087309591588564e-05,
                  "p95": 8.567075383325573e-05,
                  "p99": 0.00023009348660707474,
                  "maximum": 0.0011981967836618423
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05955027602612972,
                  "candidate": 0.05835207924246788
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 181.05954199563712,
            "full": 3316.3344169734046
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 182.53412505146116,
            "full": 3240.8015829278156
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 186.12645799294114,
            "full": 3321.416415972635
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 183.19904198870063,
            "full": 3362.9064169945195
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
            "identifier": "plan_j_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 47,
            "stages": {
              "direct": {
                "nmbe_percent": 0.08721009641470957,
                "cvrmse_percent": 20.759097246570082,
                "rms_normalized_rmse_percent": 4.894355582920606,
                "reference_energy": 11.690693137468301,
                "candidate_energy": 11.700888602225035,
                "relative_energy_error_percent": 0.08721009641470957,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.7800080033557606e-06,
                  "p95": 5.8893594541586936e-05,
                  "p99": 0.00015894195530563593,
                  "maximum": 0.0003313085180707276
                },
                "worst": {
                  "global_sensor_index": 40,
                  "local_sensor_index": 40,
                  "sky_patch_index": 85,
                  "rgb_channel": 0,
                  "reference": 0.0010530200088396668,
                  "candidate": 0.0007217114907689393
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.19010857357427668,
                "cvrmse_percent": 52.71793023999419,
                "rms_normalized_rmse_percent": 2.9112824380110824,
                "reference_energy": 7.223192484333392,
                "candidate_energy": 7.2094605761349015,
                "relative_energy_error_percent": 0.1901085735742767,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.914530109090265e-06,
                  "p90": 2.976735595439095e-05,
                  "p95": 8.503254503011703e-05,
                  "p99": 0.00023047346621751785,
                  "maximum": 0.0011042598634958267
                },
                "worst": {
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05314957909286022,
                  "candidate": 0.05425383895635605
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 179.12562505807728,
            "full": 3482.7322080964223
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 184.56087505910546,
            "full": 3538.553083082661
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 179.35237498022616,
            "full": 3520.8460420835763
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 179.6059999614954,
            "full": 3496.251832926646
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
            "identifier": "plan_j_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 47,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0001488901632326299,
                "cvrmse_percent": 11.411690968656862,
                "rms_normalized_rmse_percent": 2.6913732342583465,
                "reference_energy": 11.69091230792101,
                "candidate_energy": 11.690929714539429,
                "relative_energy_error_percent": 0.0001488901632326299,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.355904598516645e-06,
                  "p95": 3.1720963306725025e-05,
                  "p99": 8.669309318065643e-05,
                  "maximum": 0.00026201747823506594
                },
                "worst": {
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "sky_patch_index": 144,
                  "rgb_channel": 0,
                  "reference": 0.0017416984774172306,
                  "candidate": 0.0014796809991821647
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.1345931923851301,
                "cvrmse_percent": 31.394496156262345,
                "rms_normalized_rmse_percent": 1.7341682980282138,
                "reference_energy": 7.229339993680057,
                "candidate_energy": 7.219609794194188,
                "relative_energy_error_percent": 0.1345931923851301,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.581379587558331e-06,
                  "p90": 2.059844700852409e-05,
                  "p95": 4.802283365279436e-05,
                  "p99": 0.0001315850531682372,
                  "maximum": 0.0006543900817632675
                },
                "worst": {
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05368473008275032,
                  "candidate": 0.05433912016451359
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 274.5480000739917,
            "full": 6149.802541011013
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 278.6010830895975,
            "full": 6118.13470791094
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 278.21562509052455,
            "full": 6185.800709063187
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 279.54404102638364,
            "full": 6129.625459085219
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 4870.688709081151,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_j_distributed/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 18546.396374935284,
      "worker_pool_size": 12,
      "invocation_count": 3
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
            "nmbe_percent": -0.24330097762515931,
            "cvrmse_percent": 4.101153747889933,
            "rms_normalized_rmse_percent": 0.9675914624806878,
            "reference_energy": 11.693547706347431,
            "candidate_energy": 11.665097190458823,
            "relative_energy_error_percent": 0.24330097762515934,
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
            "nmbe_percent": 0.264689162002163,
            "cvrmse_percent": 18.96814370209003,
            "rms_normalized_rmse_percent": 1.0473317556382076,
            "reference_energy": 7.221848207902427,
            "candidate_energy": 7.2409636574049925,
            "relative_energy_error_percent": 0.264689162002163,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.999015461886302e-06,
              "p90": 1.571649409015663e-05,
              "p95": 2.525246236473322e-05,
              "p99": 5.806807894259691e-05,
              "maximum": 0.000645272433757782
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.032136350870132446,
              "candidate": 0.031491078436374664,
              "position": [
                8.5,
                9.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.04935168382603078,
            "cvrmse_percent": 6.923128918556668,
            "rms_normalized_rmse_percent": 1.001218669761098,
            "reference_energy": 18.91539591424986,
            "candidate_energy": 18.906060847863813,
            "relative_energy_error_percent": 0.04935168382605425,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.988943021226987e-06,
              "p90": 1.5312547475332394e-05,
              "p95": 2.440926618874073e-05,
              "p99": 5.3487252444028854e-05,
              "maximum": 0.000645272433757782
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.032136350870132446,
              "candidate": 0.031491078436374664,
              "position": [
                8.5,
                9.5,
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
            "nmbe_percent": -0.24330097762515931,
            "cvrmse_percent": 4.101153747889933,
            "rms_normalized_rmse_percent": 0.9675914624806878,
            "reference_energy": 11.693547706347431,
            "candidate_energy": 11.665097190458823,
            "relative_energy_error_percent": 0.24330097762515934,
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
            "nmbe_percent": 94.01485473344985,
            "cvrmse_percent": 1111.1965283999905,
            "rms_normalized_rmse_percent": 43.92394389223555,
            "reference_energy": 3.73216971832033,
            "candidate_energy": 7.2409636574049925,
            "relative_energy_error_percent": 94.01485473344984,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.98500001715729e-05,
              "p90": 5.5623502703383565e-05,
              "p95": 7.941864896565676e-05,
              "p99": 0.0001873873407021165,
              "maximum": 0.019528448581695557
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02887658029794693,
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
            "nmbe_percent": 22.561954996209938,
            "cvrmse_percent": 268.8237624683005,
            "rms_normalized_rmse_percent": 43.919975995663954,
            "reference_energy": 15.425717424667761,
            "candidate_energy": 18.906060847863813,
            "relative_energy_error_percent": 22.561954996209916,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.9744747461913903e-05,
              "p90": 5.508762478712015e-05,
              "p95": 7.732619997113943e-05,
              "p99": 0.00018493947573006153,
              "maximum": 0.019528448581695557
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02887658029794693,
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
      "bias_percent": -0.07359240498657468,
      "rms_normalized_error_percent": 0.2596106179473561,
      "absolute_error": {
        "p95": 0.12735236662414803,
        "p99": 0.211383238097139,
        "maximum": 0.26363685113778246
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 17.900944732515683,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2596106179473561
    },
    "overcast": {
      "bias_percent": -0.0364414132688723,
      "rms_normalized_error_percent": 0.18710020959269308,
      "absolute_error": {
        "p95": 0.05806841850280761,
        "p99": 0.10072206497192379,
        "maximum": 0.1180419921875
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 11.622468948364258,
      "reference_fraction_of_uniform": 0.6492656469345093,
      "rms_normalized_to_uniform_percent": 0.1289389455844376
    },
    "horizon": {
      "bias_percent": -0.2073186386835879,
      "rms_normalized_error_percent": 1.5560667671846766,
      "absolute_error": {
        "p95": 0.06127049205567303,
        "p99": 0.08234212324373373,
        "maximum": 0.08728172756188757
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.7270427811259854,
      "reference_fraction_of_uniform": 0.09647774499794672,
      "rms_normalized_to_uniform_percent": 0.11496300985955063
    },
    "north": {
      "bias_percent": -0.26420292208379736,
      "rms_normalized_error_percent": 0.5003780150521409,
      "absolute_error": {
        "p95": 0.10598225593566872,
        "p99": 0.1643376541137695,
        "maximum": 0.18282318115234375
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.072189807891846,
      "reference_fraction_of_uniform": 0.339210569858551,
      "rms_normalized_to_uniform_percent": 0.18609886384699587
    },
    "east": {
      "bias_percent": 0.02242561734825559,
      "rms_normalized_error_percent": 0.23276271941968824,
      "absolute_error": {
        "p95": 0.03392139673233029,
        "p99": 0.05350273132324217,
        "maximum": 0.06376457214355469
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.230720520019531,
      "reference_fraction_of_uniform": 0.23634061217308044,
      "rms_normalized_to_uniform_percent": 0.07187728495122643
    },
    "south": {
      "bias_percent": 0.05387036500896081,
      "rms_normalized_error_percent": 0.1885147840001041,
      "absolute_error": {
        "p95": 0.03250614404678343,
        "p99": 0.03904030799865722,
        "maximum": 0.04288959503173828
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.6122658252716064,
      "reference_fraction_of_uniform": 0.2017918974161148,
      "rms_normalized_to_uniform_percent": 0.05882539903382676
    },
    "west": {
      "bias_percent": -0.1528398791708151,
      "rms_normalized_error_percent": 0.493063072736721,
      "absolute_error": {
        "p95": 0.06012094020843502,
        "p99": 0.14412189483642568,
        "maximum": 0.1930551528930664
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.175939083099365,
      "reference_fraction_of_uniform": 0.28914332389831543,
      "rms_normalized_to_uniform_percent": 0.15262809293620086
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
          "nmbe_percent": 0.013451685204437408,
          "cvrmse_percent": 1.7960115989621879,
          "absolute_error_percentiles_lux": {
            "p50": 3.063232421875,
            "p90": 21.295849609375,
            "p95": 31.88752136230469,
            "p99": 69.73794921875
          },
          "maximum_absolute_error_lux": 293.935546875,
          "worst": {
            "sensor_index": 28,
            "position": [
              7.5,
              6.5,
              0.75
            ],
            "hour_of_year": 2719.5,
            "foton_lux": 17401.759765625,
            "radiance_lux": 17107.82421875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2594957738268734,
            "maximum_error_percentage_points": 2.740136986301369,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.09122265075221733,
            "maximum_error_percentage_points": 0.40212094586197367,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.059306324686680206,
            "maximum_error_percentage_points": 0.38726027397260054,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.06812591081317432,
            "maximum_error_percentage_points": 0.38726027397260054,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.014937336053628623,
            "maximum_error_percentage_points": 0.10958904109589085,
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
      "study_preparation_seconds": 0.008048959076404572,
      "weather_seconds": 0.1170131660765037,
      "metric_reduction_seconds": 0.16125208302401006,
      "write_seconds": 0.031174707924947143,
      "total_seconds": 0.3095947919646278,
      "cold_end_to_end_seconds": 0.3176437510410324,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.017103541060350835,
      "engine_upload_seconds": 0.000866708,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.11011308338493109,
      "engine_annual_reduction_seconds": 0.0020207916386425495,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.11011308338493109
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.008048959076404572,
      "weather_seconds": 0.11271433299407363,
      "metric_reduction_seconds": 0.04401325003709644,
      "write_seconds": 0.03885245800483972,
      "total_seconds": 0.19594362506177276,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.19594362506177276,
      "raw_export_seconds": 0.012294666958041489,
      "engine_upload_seconds": 6.4792e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0020810416899621487,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.011000875034369528,
      "full": 0.10305770800914615
    }
  },
  "elapsed_seconds": 82.42366970796138,
  "result_class": "passed"
}
```
