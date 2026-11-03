# Foton report

Status: **passed**

```json
{
  "scene": "context_obstruction",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "context_obstruction",
    "category": "context",
    "question": "How much sky does a neighbouring facade obstruct?",
    "interactions": [
      "external_obstruction",
      "horizon_sky"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 1,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "db5c2e950584c16ffe0d51c7bc25224fb72b4e1bb7bc7ea3ce430dfef333a39d",
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
      "scene_fingerprint": 14793621846004041752,
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
      "scene_fingerprint": 14793621846004041752,
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
    "model_sha256": "983c1c58a88e88bfc0c380a3c61201837ebb9491fa195c8f63ddfc4ac7aa881b",
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
          "maximum": 0.00035545602440834045,
          "p95": 0.0,
          "p99": 1.7517711967229843e-05
        },
        "bias_percent": -0.4575824892542755,
        "identifier": "context_obstruction_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.7263588325986352,
        "worst_index": [
          17,
          116,
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
          "maximum": 0.000497862696647644,
          "p95": 4.40298528701532e-05,
          "p99": 9.290192974731326e-05
        },
        "bias_percent": 0.03303637378572072,
        "identifier": "context_obstruction_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3054304940450385,
        "worst_index": [
          17,
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
          "maximum": 0.00030439719557762146,
          "p95": 3.824965242529284e-05,
          "p99": 8.739865734241903e-05
        },
        "bias_percent": 0.06695131039243135,
        "identifier": "context_obstruction_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1161383516816246,
        "worst_index": [
          8,
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
            "identifier": "context_obstruction_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003150906413793564,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.5512170143192634e-05
                },
                "candidate_energy": 0.8512494884053012,
                "cvrmse_percent": 23.92264335582753,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.14592321478221607,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.8500091277601314,
                "relative_energy_error_percent": 0.14592321478221607,
                "rms_normalized_rmse_percent": 1.8682995430481106,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.017795279622077942,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.0181103702634573,
                  "rgb_channel": 0,
                  "sky_patch_index": 133
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007509663701057434,
                  "p50": 0.0,
                  "p90": 4.8476118536200374e-05,
                  "p95": 7.90511680861527e-05,
                  "p99": 0.00019111335859633982
                },
                "candidate_energy": 1.8693453648866125,
                "cvrmse_percent": 37.25813972106152,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.07974435853843924,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.8678558552164475,
                "relative_energy_error_percent": 0.07974435853843925,
                "rms_normalized_rmse_percent": 3.2153583904776037,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04183262586593628,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.041081659495830536,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 104.64058304205537,
            "full": 229.7604160849005
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 100.52079195156693,
            "full": 220.5619999440387
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 98.95204100757837,
            "full": 228.6677920492366
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 99.1960420506075,
            "full": 235.11174996383488
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
            "identifier": "context_obstruction_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001507950946688652,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.9779079593718052e-05
                },
                "candidate_energy": 0.8479274431010708,
                "cvrmse_percent": 12.656552018788126,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.023713367504425764,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.8481285629441118,
                "relative_energy_error_percent": 0.023713367504425764,
                "rms_normalized_rmse_percent": 0.9872077180003856,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.018075719475746155,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.01792492438107729,
                  "rgb_channel": 0,
                  "sky_patch_index": 133
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010196547955274582,
                  "p50": 5.804416105092969e-06,
                  "p90": 3.978872518928256e-05,
                  "p95": 6.54629748169099e-05,
                  "p99": 0.00014631589874625206
                },
                "candidate_energy": 3.0050573584873206,
                "cvrmse_percent": 19.507495222945035,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.13804496246968084,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.009211423267203,
                "relative_energy_error_percent": 0.13804496246968087,
                "rms_normalized_rmse_percent": 2.0899227198658443,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05151259899139404,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.050492944195866585,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 129.88845794461668,
            "full": 2301.427375059575
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.69458295870572,
            "full": 2294.1523340996355
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 128.71370802167803,
            "full": 2300.9635839844123
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 129.83316695317626,
            "full": 2268.9339169301093
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
            "identifier": "context_obstruction_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00025589787401258945,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.135802060365677e-05
                },
                "candidate_energy": 0.8497907183100324,
                "cvrmse_percent": 17.064135636825988,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.142534270638336,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.8485811992868548,
                "relative_energy_error_percent": 0.142534270638336,
                "rms_normalized_rmse_percent": 1.3322555895363475,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007193954428657889,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.0069380565546453,
                  "rgb_channel": 0,
                  "sky_patch_index": 93
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008334051817655563,
                  "p50": 5.982627044431865e-06,
                  "p90": 3.9599326555617154e-05,
                  "p95": 6.55858544632792e-05,
                  "p99": 0.0001507009583292529
                },
                "candidate_energy": 3.003196321296663,
                "cvrmse_percent": 20.887750593978264,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.26923102851636993,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.0113036851800246,
                "relative_energy_error_percent": 0.2692310285163699,
                "rms_normalized_rmse_percent": 2.2408516778578047,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.021695325151085854,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.020861919969320297,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 129.70504094846547,
            "full": 2831.029916065745
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 124.97291702311486,
            "full": 2449.667250039056
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.20966609474272,
            "full": 2472.975332988426
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.56137507595122,
            "full": 2414.3930000718683
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
            "identifier": "context_obstruction_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00014759507030248642,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.4404533430933952e-05
                },
                "candidate_energy": 0.8495667912293356,
                "cvrmse_percent": 9.985344048821839,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.10046708771135637,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.8487141128771327,
                "relative_energy_error_percent": 0.10046708771135637,
                "rms_normalized_rmse_percent": 0.7795544969038605,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013940189965069294,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.013792594894766808,
                  "rgb_channel": 0,
                  "sky_patch_index": 132
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006439238786697388,
                  "p50": 4.288071409064287e-06,
                  "p90": 2.8387978090904653e-05,
                  "p95": 4.553884236884172e-05,
                  "p99": 0.00010509889398235828
                },
                "candidate_energy": 3.0092298671784334,
                "cvrmse_percent": 14.435803816038725,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.043023766976207925,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.0105251084858686,
                "relative_energy_error_percent": 0.043023766976207925,
                "rms_normalized_rmse_percent": 1.54512324744072,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05057347007095814,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.051217393949627876,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 195.13320794794708,
            "full": 4372.668833006173
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 187.71325005218387,
            "full": 4294.4712090538815
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 185.97516603767872,
            "full": 4317.187707987614
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 220.61108308844268,
            "full": 4277.785832993686
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
    "/content/suite-vulkan-0.3.1/context_obstruction/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 782.7278330223635,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/context_obstruction/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2611.9042090140283,
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
        "identifier": "context_obstruction_grid",
        "full_identifier": "context_obstruction_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.04624710441052017,
            "cvrmse_percent": 13.77053660142539,
            "rms_normalized_rmse_percent": 1.0744564373700007,
            "reference_energy": 0.849546850695333,
            "candidate_energy": 0.8499397415143903,
            "relative_energy_error_percent": 0.04624710441052017,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.1757860193029046e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.9619913909572209,
            "cvrmse_percent": 19.157789444301965,
            "rms_normalized_rmse_percent": 2.0521332735347984,
            "reference_energy": 3.009471064407908,
            "candidate_energy": 2.980520211854955,
            "relative_energy_error_percent": 0.9619913909572207,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 7.292040436368552e-06,
              "p90": 3.1495990697294474e-05,
              "p95": 4.4223599616088864e-05,
              "p99": 0.00010246946476399899,
              "maximum": 0.0009191520512104034
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05089543014764786,
              "candidate": 0.049976278096437454,
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
            "nmbe_percent": -0.7400318516824335,
            "cvrmse_percent": 14.89055827065582,
            "rms_normalized_rmse_percent": 2.045303537636396,
            "reference_energy": 3.859017915103241,
            "candidate_energy": 3.8304599533693455,
            "relative_energy_error_percent": 0.7400318516824336,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 7.266531611094251e-06,
              "p90": 3.1343777664005756e-05,
              "p95": 4.400456891744393e-05,
              "p99": 0.00010176340583711863,
              "maximum": 0.0009191520512104034
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05089543014764786,
              "candidate": 0.049976278096437454,
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
        "identifier": "context_obstruction_grid",
        "full_identifier": "context_obstruction_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.04624710441052017,
            "cvrmse_percent": 13.77053660142539,
            "rms_normalized_rmse_percent": 1.0744564373700007,
            "reference_energy": 0.849546850695333,
            "candidate_energy": 0.8499397415143903,
            "relative_energy_error_percent": 0.04624710441052017,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.1757860193029046e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 59.41312537837079,
            "cvrmse_percent": 415.156541410292,
            "rms_normalized_rmse_percent": 35.86219505468934,
            "reference_energy": 1.8696830670502322,
            "candidate_energy": 2.980520211854955,
            "relative_energy_error_percent": 59.41312537837079,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.3148739273892716e-05,
              "p90": 8.372518641408533e-05,
              "p95": 0.00010674974710127558,
              "p99": 0.00024673488223925233,
              "maximum": 0.008663114160299301
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.041650597006082535,
              "candidate": 0.050313711166381836,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 40.86561523804758,
            "cvrmse_percent": 285.4532189694557,
            "rms_normalized_rmse_percent": 35.8622771774995,
            "reference_energy": 2.719229917745565,
            "candidate_energy": 3.8304599533693455,
            "relative_energy_error_percent": 40.865615238047575,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.3102185878087766e-05,
              "p90": 8.382962550967932e-05,
              "p95": 0.00010769005075417223,
              "p99": 0.00023237569257616997,
              "maximum": 0.008663114160299301
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.041650597006082535,
              "candidate": 0.050313711166381836,
              "position": [
                2.5,
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
      "bias_percent": -0.11819627573392481,
      "rms_normalized_error_percent": 0.41711841647165665,
      "absolute_error": {
        "p95": 0.055603124809803534,
        "p99": 0.07136567906122784,
        "maximum": 0.07411136228467186
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.4606633308171273,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.41711841647165665
    },
    "overcast": {
      "bias_percent": -0.10686774557623945,
      "rms_normalized_error_percent": 0.4272240081025099,
      "absolute_error": {
        "p95": 0.051963165402412415,
        "p99": 0.05262161195278168,
        "maximum": 0.052715301513671875
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.5368051528930664,
      "reference_fraction_of_uniform": 0.7330401539802551,
      "rms_normalized_to_uniform_percent": 0.3324020596732739
    },
    "horizon": {
      "bias_percent": -1.1290284850537626,
      "rms_normalized_error_percent": 2.1011335496641377,
      "absolute_error": {
        "p95": 0.022695553903364328,
        "p99": 0.025479330622505247,
        "maximum": 0.026327424543088007
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3291794247253598,
      "reference_fraction_of_uniform": 0.09512032615077712,
      "rms_normalized_to_uniform_percent": 0.14998034229572524
    },
    "north": {
      "bias_percent": -0.17824304905008312,
      "rms_normalized_error_percent": 0.7924698758700256,
      "absolute_error": {
        "p95": 0.021608538925647736,
        "p99": 0.03449140489101408,
        "maximum": 0.039934515953063965
      },
      "worst_index": [
        20
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.0562111139297485,
      "reference_fraction_of_uniform": 0.3052048087120056,
      "rms_normalized_to_uniform_percent": 0.19086547544846097
    },
    "east": {
      "bias_percent": -0.45403584014846593,
      "rms_normalized_error_percent": 0.8820407710022766,
      "absolute_error": {
        "p95": 0.024891525506973267,
        "p99": 0.049500501155853235,
        "maximum": 0.0580446720123291
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.813428521156311,
      "reference_fraction_of_uniform": 0.23504988849163055,
      "rms_normalized_to_uniform_percent": 0.2055297308426881
    },
    "south": {
      "bias_percent": 0.12149069337906916,
      "rms_normalized_error_percent": 0.5087274597067664,
      "absolute_error": {
        "p95": 0.017206210643053055,
        "p99": 0.028675818443298324,
        "maximum": 0.032482147216796875
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5962584018707275,
      "reference_fraction_of_uniform": 0.17229598760604858,
      "rms_normalized_to_uniform_percent": 0.12170391264556826
    },
    "west": {
      "bias_percent": 0.16354303898795,
      "rms_normalized_error_percent": 0.9286716606083871,
      "absolute_error": {
        "p95": 0.0261581689119339,
        "p99": 0.04553683698177334,
        "maximum": 0.054244041442871094
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.7740232348442078,
      "reference_fraction_of_uniform": 0.22366325557231903,
      "rms_normalized_to_uniform_percent": 0.2031805165887258
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
        "identifier": "context_obstruction_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.2740440230408934,
          "cvrmse_percent": 4.348332926722071,
          "absolute_error_percentiles_lux": {
            "p50": 1.0258369445800781,
            "p90": 9.370553588867189,
            "p95": 14.460647964477518,
            "p99": 30.129933776855463
          },
          "maximum_absolute_error_lux": 227.2421875,
          "worst": {
            "sensor_index": 23,
            "position": [
              3.5,
              0.5,
              0.75
            ],
            "hour_of_year": 3829.5,
            "foton_lux": 15205.83203125,
            "radiance_lux": 14978.58984375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.09754946727549506,
            "maximum_error_percentage_points": 0.9842465753424658,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.3545498035825866,
            "maximum_error_percentage_points": 1.1032714518563758,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.7921499238964995,
            "maximum_error_percentage_points": 4.275205479452055,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.7988089802130898,
            "maximum_error_percentage_points": 4.275205479452055,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.010121765601217705,
            "maximum_error_percentage_points": 0.14150684931506952,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 5.555555555555555,
          "radiance_percent": 5.555555555555555,
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
      "maximum_error_percentage_points": 0.00499866224314971,
      "metrics": {
        "da": [
          {
            "identifier": "context_obstruction_grid",
            "maximum_error_percentage_points": 0.0046575342465753344,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "context_obstruction_grid",
            "maximum_error_percentage_points": 0.00499866224314971,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "context_obstruction_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "context_obstruction_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "context_obstruction_grid",
            "maximum_error_percentage_points": 0.004520547945205067,
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
      "study_preparation_seconds": 0.4327990320016397,
      "weather_seconds": 0.41259079400333576,
      "metric_reduction_seconds": 0.3059071550014778,
      "write_seconds": 0.03309540799818933,
      "total_seconds": 0.7520688559961854,
      "cold_end_to_end_seconds": 1.1848678879978252,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.012201917998027056,
      "engine_upload_seconds": 0.015695146,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.013183057,
      "engine_annual_reduction_seconds": 0.007097908,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.013183057
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.4327990320016397,
      "weather_seconds": 0.39768754100077786,
      "metric_reduction_seconds": 0.24263719099690206,
      "write_seconds": 0.02861600599862868,
      "total_seconds": 0.6693410970037803,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.6693410970037803,
      "raw_export_seconds": 0.01054311800544383,
      "engine_upload_seconds": 0.01550191,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 7.5e-08,
      "engine_annual_reduction_seconds": 0.007051945,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01473178399464814,
      "full": 0.02734582599805435
    }
  },
  "elapsed_seconds": 3.403947363003681,
  "result_class": "passed"
}
```
