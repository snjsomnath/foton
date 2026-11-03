# Foton report

Status: **passed**

```json
{
  "scene": "multiple_rooflights",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "multiple_rooflights",
    "category": "openings",
    "question": "How do four separated rooflights combine across the workplane?",
    "interactions": [
      "roof_glazing",
      "multiple_openings",
      "punched_roof"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 4,
    "shades": 0,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 4.0
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "74acf782eb79bdf3549132bed646a7ad958ef83d36b20b7ab8c46de0f1902a8d",
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
      "scene_fingerprint": 9669362914231080515,
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 9669362914231080515,
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
    "model_sha256": "fcfd891186ba4925b6420263eed28dbc7254f2d162a9c861464a733f0c9743d5",
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
          "maximum": 0.00027515029069036245,
          "p95": 1.8663908122107387e-05,
          "p99": 9.511946700513363e-05
        },
        "bias_percent": -0.02745070358697988,
        "identifier": "multiple_rooflights_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.072997508576628,
        "worst_index": [
          13,
          561,
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
          "maximum": 0.0002487683668732643,
          "p95": 3.780028782784939e-05,
          "p99": 0.00010945601388812065
        },
        "bias_percent": 0.03264595676547041,
        "identifier": "multiple_rooflights_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.41051220092536,
        "worst_index": [
          9,
          468,
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
          "maximum": 0.00019592163152992725,
          "p95": 3.176573954988271e-05,
          "p99": 8.615385740995407e-05
        },
        "bias_percent": -0.022313677290360916,
        "identifier": "multiple_rooflights_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.976345597597143,
        "worst_index": [
          27,
          323,
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
            "identifier": "multiple_rooflights_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004215158987790346,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.6384986490011215e-05,
                  "p99": 0.0001827473024604842
                },
                "candidate_energy": 12.065647413925035,
                "cvrmse_percent": 16.95955157832684,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.01317528182025175,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.067237306448078,
                "relative_energy_error_percent": 0.013175281820251749,
                "rms_normalized_rmse_percent": 3.7923466343541654,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0055363979190588,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.005114882020279765,
                  "rgb_channel": 0,
                  "sky_patch_index": 537
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000846207607537508,
                  "p50": 4.2573649352561915e-06,
                  "p90": 3.096295686191302e-05,
                  "p95": 9.202680303133093e-05,
                  "p99": 0.00028239228413440287
                },
                "candidate_energy": 1.369856054746034,
                "cvrmse_percent": 250.06605243347195,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.32994125346364506,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3743907367704224,
                "relative_energy_error_percent": 0.3299412534636451,
                "rms_normalized_rmse_percent": 6.297186059716378,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.000750421779230237,
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "reference": 9.5785828307271e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 541
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 125.0482079340145,
            "full": 241.5661660488695
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.007707901299,
            "full": 257.65475002117455
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 125.87704206816852,
            "full": 244.13883301895112
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 119.53062494285405,
            "full": 259.43504204042256
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
            "identifier": "multiple_rooflights_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000374447088688612,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.500115755945444e-05,
                  "p99": 0.00014819949865341187
                },
                "candidate_energy": 12.063355379250424,
                "cvrmse_percent": 14.186622086700552,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.0037907278932024697,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.06381268556288,
                "relative_energy_error_percent": 0.0037907278932024697,
                "rms_normalized_rmse_percent": 3.171828566082599,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0042064746376127005,
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "reference": 0.0038320275489240885,
                  "rgb_channel": 0,
                  "sky_patch_index": 385
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004499246133491397,
                  "p50": 6.247503051781678e-06,
                  "p90": 2.9272627216414694e-05,
                  "p95": 6.76803792885039e-05,
                  "p99": 0.00021073746029287577
                },
                "candidate_energy": 3.805315597691642,
                "cvrmse_percent": 67.0474957638849,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.30895840531496427,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7935949671769436,
                "relative_energy_error_percent": 0.30895840531496427,
                "rms_normalized_rmse_percent": 4.559328847483701,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0001855556620284915,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.0002643689513206482,
                  "rgb_channel": 0,
                  "sky_patch_index": 440
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 160.5635000159964,
            "full": 2430.2573750028387
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 175.73258304037154,
            "full": 2427.487291977741
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 158.4381670691073,
            "full": 2425.0413340050727
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 163.00716705154628,
            "full": 2434.513457934372
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
            "identifier": "multiple_rooflights_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003665155963972211,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.457722752704285e-05,
                  "p99": 0.00014598589041270316
                },
                "candidate_energy": 12.067013574636803,
                "cvrmse_percent": 14.40577772679685,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.10579217438697339,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.054261109702566,
                "relative_energy_error_percent": 0.10579217438697337,
                "rms_normalized_rmse_percent": 3.219892644887319,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003432173514738679,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.003065657918341458,
                  "rgb_channel": 0,
                  "sky_patch_index": 498
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005799835780635476,
                  "p50": 6.274450697674183e-06,
                  "p90": 2.8770048447768272e-05,
                  "p95": 6.507401121780276e-05,
                  "p99": 0.0002121410216204822
                },
                "candidate_energy": 3.8020720020797327,
                "cvrmse_percent": 67.5750781105009,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.28893185451816905,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8130892315107694,
                "relative_energy_error_percent": 0.2889318545181691,
                "rms_normalized_rmse_percent": 4.616486609041611,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00012827105820178986,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.00045171251986175776,
                  "rgb_channel": 0,
                  "sky_patch_index": 425
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 160.76933301519603,
            "full": 2579.095916938968
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 159.1711250366643,
            "full": 2576.1214999947697
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.04337493237108,
            "full": 2627.97429098282
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 166.01141600403935,
            "full": 2561.909500043839
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
            "identifier": "multiple_rooflights_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002114749513566494,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3292843252420425e-05,
                  "p99": 8.344868547283113e-05
                },
                "candidate_energy": 12.063441567370319,
                "cvrmse_percent": 7.9907132317541105,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0042432813061289,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.062929703329246,
                "relative_energy_error_percent": 0.004243281306128901,
                "rms_normalized_rmse_percent": 1.7862762339357616,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0035961420508101583,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.0038076170021668077,
                  "rgb_channel": 0,
                  "sky_patch_index": 575
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00032850506249815226,
                  "p50": 4.483298653212842e-06,
                  "p90": 2.0066539946128628e-05,
                  "p95": 4.024461668450385e-05,
                  "p99": 0.00011902712867595255
                },
                "candidate_energy": 3.7993084774294417,
                "cvrmse_percent": 39.76367861753014,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.11478671714829287,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8036745906230216,
                "relative_energy_error_percent": 0.11478671714829287,
                "rms_normalized_rmse_percent": 2.712561293459362,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -6.896955892443657e-05,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.0002595355035737157,
                  "rgb_channel": 0,
                  "sky_patch_index": 570
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 233.26720797922462,
            "full": 4561.054792022333
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 238.97404200397432,
            "full": 4502.044332912192
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 251.98841700330377,
            "full": 4506.605832953937
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 234.40670897252858,
            "full": 4569.852167041972
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
    "/content/suite-vulkan-0.3.1/multiple_rooflights/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2674.628374981694,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/multiple_rooflights/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10681.896124966443,
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
        "identifier": "multiple_rooflights_grid",
        "full_identifier": "multiple_rooflights_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.007830294704226963,
            "cvrmse_percent": 5.389259664083597,
            "rms_normalized_rmse_percent": 1.2060785691011424,
            "reference_energy": 12.062760689435208,
            "candidate_energy": 12.063705239146657,
            "relative_energy_error_percent": 0.007830294704226963,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.0512361768633127e-05,
              "p99": 4.8212590627372265e-05,
              "maximum": 0.00013783667236566544
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 561,
              "rgb_channel": 0,
              "reference": 0.0055317687802016735,
              "candidate": 0.005669605452567339,
              "position": [
                1.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.19956769428096277,
            "cvrmse_percent": 26.09450534770516,
            "rms_normalized_rmse_percent": 1.7793483480842094,
            "reference_energy": 3.8019164882473344,
            "candidate_energy": 3.7943290911732515,
            "relative_energy_error_percent": 0.1995676942809628,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.824676577503851e-06,
              "p90": 2.0936079818056913e-05,
              "p95": 3.027627826668322e-05,
              "p99": 6.692600436508656e-05,
              "maximum": 0.00018691609147936106
            },
            "worst": {
              "global_sensor_index": 13,
              "local_sensor_index": 13,
              "sky_patch_index": 561,
              "rgb_channel": 0,
              "reference": -8.26461473479867e-05,
              "candidate": 0.00010426994413137436,
              "position": [
                2.5,
                4.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.04187193529521856,
            "cvrmse_percent": 5.821744531766462,
            "rms_normalized_rmse_percent": 1.656508699194442,
            "reference_energy": 15.864677177682543,
            "candidate_energy": 15.858034330319908,
            "relative_energy_error_percent": 0.041871935295218564,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.817397322971374e-06,
              "p90": 2.0374613814055924e-05,
              "p95": 2.8867019864264876e-05,
              "p99": 5.9345271438360214e-05,
              "maximum": 0.0001577083021402359
            },
            "worst": {
              "global_sensor_index": 1,
              "local_sensor_index": 1,
              "sky_patch_index": 533,
              "rgb_channel": 0,
              "reference": 0.004852483049035072,
              "candidate": 0.005010191351175308,
              "position": [
                0.5,
                4.5,
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
        "identifier": "multiple_rooflights_grid",
        "full_identifier": "multiple_rooflights_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.007830294704226963,
            "cvrmse_percent": 5.389259664083597,
            "rms_normalized_rmse_percent": 1.2060785691011424,
            "reference_energy": 12.062760689435208,
            "candidate_energy": 12.063705239146657,
            "relative_energy_error_percent": 0.007830294704226963,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.0512361768633127e-05,
              "p99": 4.8212590627372265e-05,
              "maximum": 0.00013783667236566544
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 561,
              "rgb_channel": 0,
              "reference": 0.0055317687802016735,
              "candidate": 0.005669605452567339,
              "position": [
                1.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 175.78973217169423,
            "cvrmse_percent": 256.7079347411245,
            "rms_normalized_rmse_percent": 6.474196594500875,
            "reference_energy": 1.3758050603606495,
            "candidate_energy": 3.7943290911732515,
            "relative_energy_error_percent": 175.78973217169423,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.3960439168367884e-05,
              "p90": 8.754323275752544e-05,
              "p95": 0.00010624393325997517,
              "p99": 0.00017990253400057554,
              "maximum": 0.000515074236318469
            },
            "worst": {
              "global_sensor_index": 11,
              "local_sensor_index": 11,
              "sky_patch_index": 554,
              "rgb_channel": 0,
              "reference": -0.00039355421904474497,
              "candidate": 0.00012152001727372408,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 18.003919656089817,
            "cvrmse_percent": 26.17782070697402,
            "rms_normalized_rmse_percent": 6.448758259308948,
            "reference_energy": 13.438565749795858,
            "candidate_energy": 15.858034330319908,
            "relative_energy_error_percent": 18.003919656089817,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.4004722692770883e-05,
              "p90": 8.72802903188586e-05,
              "p95": 0.00010571694338068482,
              "p99": 0.00017913361079990864,
              "maximum": 0.0004462907090783119
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 556,
              "rgb_channel": 0,
              "reference": 0.003097070846706629,
              "candidate": 0.0035433615557849407,
              "position": [
                1.5,
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
      "bias_percent": -0.04178387510577163,
      "rms_normalized_error_percent": 0.18946255687907182,
      "absolute_error": {
        "p95": 0.09773497177950041,
        "p99": 0.10686593159015681,
        "maximum": 0.11076928208839831
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 26.29421058616752,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.18946255687907182
    },
    "overcast": {
      "bias_percent": -0.03880633643265258,
      "rms_normalized_error_percent": 0.17855452430343186,
      "absolute_error": {
        "p95": 0.08066225051879883,
        "p99": 0.09040408134460448,
        "maximum": 0.09463214874267578
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 22.380176544189453,
      "reference_fraction_of_uniform": 0.8511446714401245,
      "rms_normalized_to_uniform_percent": 0.15240724171665418
    },
    "horizon": {
      "bias_percent": 2.1994547507574755,
      "rms_normalized_error_percent": 9.498854700530355,
      "absolute_error": {
        "p95": 0.012915578048012275,
        "p99": 0.016299863194868484,
        "maximum": 0.018078097256222697
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": true,
      "reference_mean": 0.07028672581351887,
      "reference_fraction_of_uniform": 0.002673087506589542,
      "rms_normalized_to_uniform_percent": 0.02524389310027855
    },
    "north": {
      "bias_percent": -0.06925935030392517,
      "rms_normalized_error_percent": 0.3136082299278428,
      "absolute_error": {
        "p95": 0.030206918716430664,
        "p99": 0.036265945434570304,
        "maximum": 0.03774261474609375
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.676648139953613,
      "reference_fraction_of_uniform": 0.17785847187042236,
      "rms_normalized_to_uniform_percent": 0.06379765847717893
    },
    "east": {
      "bias_percent": -0.01336225566111952,
      "rms_normalized_error_percent": 0.3314174892600425,
      "absolute_error": {
        "p95": 0.03384721279144287,
        "p99": 0.03823881149291991,
        "maximum": 0.040355682373046875
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.730530738830566,
      "reference_fraction_of_uniform": 0.1799076944589615,
      "rms_normalized_to_uniform_percent": 0.06822217298805747
    },
    "south": {
      "bias_percent": -0.0723143192520325,
      "rms_normalized_error_percent": 0.3309200186914576,
      "absolute_error": {
        "p95": 0.03147530555725098,
        "p99": 0.04086914062499998,
        "maximum": 0.045393943786621094
      },
      "worst_index": [
        0
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.679233074188232,
      "reference_fraction_of_uniform": 0.17795677483081818,
      "rms_normalized_to_uniform_percent": 0.06728235125864496
    },
    "west": {
      "bias_percent": -0.11729119604212321,
      "rms_normalized_error_percent": 0.3557135456710561,
      "absolute_error": {
        "p95": 0.03801274299621582,
        "p99": 0.04355690479278564,
        "maximum": 0.0441131591796875
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.725424289703369,
      "reference_fraction_of_uniform": 0.17971348762512207,
      "rms_normalized_to_uniform_percent": 0.07307506809546509
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
        "identifier": "multiple_rooflights_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.016075615284206354,
          "cvrmse_percent": 2.6378002855776495,
          "absolute_error_percentiles_lux": {
            "p50": 3.6400299072265625,
            "p90": 36.25028686523439,
            "p95": 55.112921142578124,
            "p99": 112.35201904296827
          },
          "maximum_absolute_error_lux": 380.3515625,
          "worst": {
            "sensor_index": 14,
            "position": [
              2.5,
              3.5,
              0.75
            ],
            "hour_of_year": 2725.5,
            "foton_lux": 30205.939453125,
            "radiance_lux": 29825.587890625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.12103881278538668,
            "maximum_error_percentage_points": 0.3324657534246569,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.03977371210014703,
            "maximum_error_percentage_points": 0.138900860259497,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.03612252663622452,
            "maximum_error_percentage_points": 0.16849315068493453,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.07287671232876668,
            "maximum_error_percentage_points": 0.3298630136986276,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0630859969558599,
            "maximum_error_percentage_points": 0.40780821917808296,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
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
      "maximum_error_percentage_points": 0.004931506849315426,
      "metrics": {
        "da": [
          {
            "identifier": "multiple_rooflights_grid",
            "maximum_error_percentage_points": 0.004794520547953596,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "multiple_rooflights_grid",
            "maximum_error_percentage_points": 0.004864083904109862,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "multiple_rooflights_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "multiple_rooflights_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "multiple_rooflights_grid",
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
      "study_preparation_seconds": 0.3482554859947413,
      "weather_seconds": 0.2531576449982822,
      "metric_reduction_seconds": 1.0988510040042456,
      "write_seconds": 0.024668598001881037,
      "total_seconds": 1.3770078660018044,
      "cold_end_to_end_seconds": 1.7252633519965457,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.012939790001837537,
      "engine_upload_seconds": 0.044953708,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.033751284,
      "engine_annual_reduction_seconds": 0.021743432,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.033751284
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3482554859947413,
      "weather_seconds": 0.24669846100005088,
      "metric_reduction_seconds": 1.0052540059987223,
      "write_seconds": 0.019154378001985606,
      "total_seconds": 1.2714035319950199,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 1.2714035319950199,
      "raw_export_seconds": 0.007981276001373772,
      "engine_upload_seconds": 0.044806486,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.1e-08,
      "engine_annual_reduction_seconds": 0.021049724,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01817185200343374,
      "full": 0.046904025999538135
    }
  },
  "elapsed_seconds": 5.074354853000841,
  "result_class": "passed"
}
```
