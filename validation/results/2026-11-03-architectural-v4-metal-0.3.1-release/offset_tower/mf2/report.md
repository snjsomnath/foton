# Foton report

Status: **passed**

```json
{
  "scene": "offset_tower",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "offset_tower",
    "category": "context",
    "question": "Does an off-axis tall obstruction affect the appropriate sky sectors?",
    "interactions": [
      "closed_context",
      "asymmetric_obstruction",
      "height_contrast"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 6,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "fbb2c82ef6cc3e6d378737143a46a01d010b296ee9a3bb8d5eed0be28263dfb3",
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
      "scene_fingerprint": 6801024155776306720,
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
      "scene_fingerprint": 6801024155776306720,
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
    "model_sha256": "36b3ac82d7687aaf37211b5cfd81d610b5cb7cd78d4769c55473ef131309ac0d",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "42ebbd5873d9863a0ad3aca60e92d9e55c1ae842623c6cc1f4949849ae92cd10",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00014028436271473765,
          "p95": 1.280568540096283e-08,
          "p99": 6.806396413594484e-06
        },
        "bias_percent": -0.025992709998800156,
        "identifier": "offset_tower_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7608913309073888,
        "worst_index": [
          17,
          543,
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
          "maximum": 0.0006343461573123932,
          "p95": 1.871419863164192e-05,
          "p99": 9.547988884150982e-05
        },
        "bias_percent": 0.04326389573144371,
        "identifier": "offset_tower_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.721226105109266,
        "worst_index": [
          14,
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
          "maximum": 0.0003454405814409256,
          "p95": 1.5391036868095398e-05,
          "p99": 8.13659280538559e-05
        },
        "bias_percent": 0.0401642144041877,
        "identifier": "offset_tower_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.370438794439763,
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
            "identifier": "offset_tower_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005186202470213175,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.151625812985003e-05,
                  "p99": 0.0002318727201782167
                },
                "candidate_energy": 5.340532457677909,
                "cvrmse_percent": 47.489473007560754,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.22310561093429618,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.328643954029758,
                "relative_energy_error_percent": 0.22310561093429618,
                "rms_normalized_rmse_percent": 8.594117031967917,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001869094732683152,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.0013504744856618345,
                  "rgb_channel": 0,
                  "sky_patch_index": 145
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008802473021205515,
                  "p50": 0.0,
                  "p90": 8.767567851464268e-06,
                  "p95": 3.540881971275667e-05,
                  "p99": 0.000290005231363466
                },
                "candidate_energy": 2.082606957702133,
                "cvrmse_percent": 157.31200506090676,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.12969670360295021,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0799093837934244,
                "relative_energy_error_percent": 0.12969670360295021,
                "rms_normalized_rmse_percent": 6.046674466860802,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0007697162218391895,
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "reference": -0.00011053108028136194,
                  "rgb_channel": 0,
                  "sky_patch_index": 85
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 117.77545802760869,
            "full": 232.20837500412017
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.11029209475964,
            "full": 239.73887495230883
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 115.14929193072021,
            "full": 236.42900004051626
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 108.86004101485014,
            "full": 221.68545797467232
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.63145799562335,
            "full": 226.71650000847876
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 108.09237498324364,
            "full": 218.74958300031722
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.05658291187137,
            "full": 243.82266704924405
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 107.80937492381781,
            "full": 227.58391697425395
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
            "identifier": "offset_tower_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003492120886221528,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.116445779800415e-07,
                  "p99": 0.00013337735435925424
                },
                "candidate_energy": 5.338102273068671,
                "cvrmse_percent": 26.56411473329533,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.06323591600911317,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.341480006879465,
                "relative_energy_error_percent": 0.06323591600911316,
                "rms_normalized_rmse_percent": 4.820495295253322,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003337528556585312,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.002988316467963159,
                  "rgb_channel": 0,
                  "sky_patch_index": 270
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006389003247022629,
                  "p50": 3.525553999850217e-07,
                  "p90": 1.322121011071432e-05,
                  "p95": 3.0066560611885507e-05,
                  "p99": 0.00019152031745761633
                },
                "candidate_energy": 3.717349008225053,
                "cvrmse_percent": 59.830044590123045,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.18019006484350145,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.710662762587024,
                "relative_energy_error_percent": 0.18019006484350145,
                "rms_normalized_rmse_percent": 3.1802031050544084,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.029514124616980553,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.02887522429227829,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.66949996817857,
            "full": 2271.0014999611303
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.19158301036805,
            "full": 2225.881583057344
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.34408300276846,
            "full": 2210.374250076711
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.4466669606045,
            "full": 2200.711708050221
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
            "identifier": "offset_tower_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003461360465735197,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.6644829884171486e-05,
                  "p99": 0.00013322121230885386
                },
                "candidate_energy": 5.3398905074136565,
                "cvrmse_percent": 27.345970656148975,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.00033211541251195744,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.339908242071942,
                "relative_energy_error_percent": 0.0003321154125119575,
                "rms_normalized_rmse_percent": 4.954823167933671,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0034549004631116986,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.0038010365096852183,
                  "rgb_channel": 0,
                  "sky_patch_index": 414
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007247757166624069,
                  "p50": 3.534379757752504e-07,
                  "p90": 1.349355843558445e-05,
                  "p95": 2.896497244364582e-05,
                  "p99": 0.0001904340460896492
                },
                "candidate_energy": 3.7209077927931986,
                "cvrmse_percent": 58.87789473079434,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.16653536598310525,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7147214678015423,
                "relative_energy_error_percent": 0.16653536598310525,
                "rms_normalized_rmse_percent": 3.130138787967397,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02544564940035343,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.02617042511701584,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.79712505917996,
            "full": 2402.761416044086
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.91233299020678,
            "full": 2424.3630409473553
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.57066589500755,
            "full": 2407.840625033714
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.3622919768095,
            "full": 2389.8387919180095
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
            "identifier": "offset_tower_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00017562153516337276,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.232643499970436e-06,
                  "p99": 6.695243064314127e-05
                },
                "candidate_energy": 5.337005596163181,
                "cvrmse_percent": 13.784862372603357,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.03618847342301038,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.338937676205205,
                "relative_energy_error_percent": 0.03618847342301038,
                "rms_normalized_rmse_percent": 2.4979073507158396,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0016980255022644997,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.001522403967101127,
                  "rgb_channel": 0,
                  "sky_patch_index": 158
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006343210116028786,
                  "p50": 2.9359844688769954e-07,
                  "p90": 9.425485586689321e-06,
                  "p95": 1.9423172489041463e-05,
                  "p99": 0.00010319182183593512
                },
                "candidate_energy": 3.7278257674589064,
                "cvrmse_percent": 32.9601196996792,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.2390689149672692,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7189349500255418,
                "relative_energy_error_percent": 0.23906891496726917,
                "rms_normalized_rmse_percent": 1.7570859109628485,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.030923545360565186,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.030289224348962307,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 213.6358340503648,
            "full": 4252.89929099381
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 189.37804200686514,
            "full": 4193.046084023081
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 211.93516708444804,
            "full": 4259.149042074569
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 200.50512498710304,
            "full": 4237.150874920189
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/suite-0.3.1/run/offset_tower/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2678.2838330836967,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10549.487374955788,
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
        "identifier": "offset_tower_grid",
        "full_identifier": "offset_tower_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.03409092830676962,
            "cvrmse_percent": 2.1726425433890526,
            "rms_normalized_rmse_percent": 0.3939117815037371,
            "reference_energy": 5.338116363298241,
            "candidate_energy": 5.336296549875897,
            "relative_energy_error_percent": 0.03409092830676962,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 6.752088665962219e-09,
              "p99": 5.540874553844333e-06,
              "maximum": 5.928060272708535e-05
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 407,
              "rgb_channel": 0,
              "reference": 0.0008973823860287666,
              "candidate": 0.000956662988755852,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.0589756800971535,
            "cvrmse_percent": 40.70408749727825,
            "rms_normalized_rmse_percent": 2.170284949612548,
            "reference_energy": 3.7232356243267155,
            "candidate_energy": 3.683807464552382,
            "relative_energy_error_percent": 1.0589756800971535,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.7909080674580764e-07,
              "p90": 9.495158519712296e-06,
              "p95": 1.571825305290986e-05,
              "p99": 4.445237573236227e-05,
              "maximum": 0.0009140428155660629
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0310528427362442,
              "candidate": 0.03013879992067814,
              "position": [
                3.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.45520771351791023,
            "cvrmse_percent": 16.713793782304897,
            "rms_normalized_rmse_percent": 2.1688337083792604,
            "reference_energy": 9.061351987624956,
            "candidate_energy": 9.020104014428279,
            "relative_energy_error_percent": 0.4552077135179103,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.7916275275051703e-07,
              "p90": 9.455827239435181e-06,
              "p95": 1.5553072444163263e-05,
              "p99": 4.352186806499958e-05,
              "maximum": 0.0009140428155660629
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0310528427362442,
              "candidate": 0.03013879992067814,
              "position": [
                3.5,
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
        "identifier": "offset_tower_grid",
        "full_identifier": "offset_tower_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.03409092830676962,
            "cvrmse_percent": 2.1726425433890526,
            "rms_normalized_rmse_percent": 0.3939117815037371,
            "reference_energy": 5.338116363298241,
            "candidate_energy": 5.336296549875897,
            "relative_energy_error_percent": 0.03409092830676962,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 6.752088665962219e-09,
              "p99": 5.540874553844333e-06,
              "maximum": 5.928060272708535e-05
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 407,
              "rgb_channel": 0,
              "reference": 0.0008973823860287666,
              "candidate": 0.000956662988755852,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 77.29961947585036,
            "cvrmse_percent": 837.6965270650988,
            "rms_normalized_rmse_percent": 32.10960558794015,
            "reference_energy": 2.0777300455820473,
            "candidate_energy": 3.683807464552382,
            "relative_energy_error_percent": 77.29961947585036,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.399999961104186e-07,
              "p90": 5.414700131041177e-05,
              "p95": 7.413000275846571e-05,
              "p99": 0.0001359844027319923,
              "maximum": 0.007573631592094898
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014012818224728107,
              "candidate": 0.021586449816823006,
              "position": [
                0.5,
                2.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.632832142086077,
            "cvrmse_percent": 234.69616697800382,
            "rms_normalized_rmse_percent": 32.10893191994475,
            "reference_energy": 7.415846408880288,
            "candidate_energy": 9.020104014428279,
            "relative_energy_error_percent": 21.632832142086077,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.399999961104186e-07,
              "p90": 5.4188688818612734e-05,
              "p95": 7.434259168803692e-05,
              "p99": 0.00013458129251375794,
              "maximum": 0.007573631592094898
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014012818224728107,
              "candidate": 0.021586449816823006,
              "position": [
                0.5,
                2.5,
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
      "bias_percent": 0.14091397096286526,
      "rms_normalized_error_percent": 0.16140311186689396,
      "absolute_error": {
        "p95": 0.06292119526125073,
        "p99": 0.09301927641157065,
        "maximum": 0.10868580392173488
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.800553638328402,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.16140311186689396
    },
    "overcast": {
      "bias_percent": 0.08455259749220441,
      "rms_normalized_error_percent": 0.1092281254169234,
      "absolute_error": {
        "p95": 0.02867865562438965,
        "p99": 0.04038516283035276,
        "maximum": 0.04657697677612305
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.9138712882995605,
      "reference_fraction_of_uniform": 0.6401404738426208,
      "rms_normalized_to_uniform_percent": 0.07771232353704526
    },
    "horizon": {
      "bias_percent": 1.1314933259753293,
      "rms_normalized_error_percent": 1.9817810979287576,
      "absolute_error": {
        "p95": 0.05345406489165072,
        "p99": 0.07687041492186261,
        "maximum": 0.08560964342185673
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3083336299577537,
      "reference_fraction_of_uniform": 0.12113579301294447,
      "rms_normalized_to_uniform_percent": 0.14331558473555142
    },
    "north": {
      "bias_percent": -0.18405971525075426,
      "rms_normalized_error_percent": 2.2305872876979644,
      "absolute_error": {
        "p95": 0.003006618469953537,
        "p99": 0.005456829816102978,
        "maximum": 0.0064022839069366455
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": true,
      "reference_mean": 0.02921009436249733,
      "reference_fraction_of_uniform": 0.0027044997550547123,
      "rms_normalized_to_uniform_percent": 0.007624933018991463
    },
    "east": {
      "bias_percent": 0.09558918641589786,
      "rms_normalized_error_percent": 0.21163790389650133,
      "absolute_error": {
        "p95": 0.009875848889350891,
        "p99": 0.012390628457069392,
        "maximum": 0.01365286111831665
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3172863721847534,
      "reference_fraction_of_uniform": 0.1219647154211998,
      "rms_normalized_to_uniform_percent": 0.025880839398979505
    },
    "south": {
      "bias_percent": 0.19598071276941975,
      "rms_normalized_error_percent": 0.2200449035236355,
      "absolute_error": {
        "p95": 0.05977368354797363,
        "p99": 0.09014093875885004,
        "maximum": 0.10271549224853516
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.760159969329834,
      "reference_fraction_of_uniform": 0.7184965014457703,
      "rms_normalized_to_uniform_percent": 0.14782834005081288
    },
    "west": {
      "bias_percent": 0.04786576602670931,
      "rms_normalized_error_percent": 0.17009822205771374,
      "absolute_error": {
        "p95": 0.012928366661071777,
        "p99": 0.022026658058166483,
        "maximum": 0.026697158813476562
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.4069666862487793,
      "reference_fraction_of_uniform": 0.22285586595535278,
      "rms_normalized_to_uniform_percent": 0.03907693013103178
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
        "identifier": "offset_tower_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.008315796439487553,
          "cvrmse_percent": 1.8383233959531335,
          "absolute_error_percentiles_lux": {
            "p50": 1.528447151184082,
            "p90": 21.105172729492192,
            "p95": 34.4211029052734,
            "p99": 76.21550048828107
          },
          "maximum_absolute_error_lux": 300.4921875,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5846.5,
            "foton_lux": 22498.03515625,
            "radiance_lux": 22798.52734375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2651255707762561,
            "maximum_error_percentage_points": 1.6709589041095896,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.10605765680471475,
            "maximum_error_percentage_points": 0.6969715589529812,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.08799847792998522,
            "maximum_error_percentage_points": 0.3246575342465725,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.09270547945205562,
            "maximum_error_percentage_points": 0.3004109589041093,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.02373287671232863,
            "maximum_error_percentage_points": 0.11027397260273997,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 47.22222222222222,
          "radiance_percent": 47.22222222222222,
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
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "offset_tower_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "offset_tower_grid",
            "maximum_error_percentage_points": 0.004768300513703139,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "offset_tower_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "offset_tower_grid",
            "maximum_error_percentage_points": 0.004794520547942938,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "offset_tower_grid",
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
      "study_preparation_seconds": 0.007437540916725993,
      "weather_seconds": 0.10279620799701661,
      "metric_reduction_seconds": 0.1276817920152098,
      "write_seconds": 0.021384082967415452,
      "total_seconds": 0.2520602500298992,
      "cold_end_to_end_seconds": 0.2594977909466252,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.01211945794057101,
      "engine_upload_seconds": 0.000871125,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.07281887496355921,
      "engine_annual_reduction_seconds": 0.001631708350032568,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.07281887496355921
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007437540916725993,
      "weather_seconds": 0.1027881670743227,
      "metric_reduction_seconds": 0.045574041083455086,
      "write_seconds": 0.01769120804965496,
      "total_seconds": 0.16622554103378206,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.16622554103378206,
      "raw_export_seconds": 0.008161749923601747,
      "engine_upload_seconds": 9.025e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0015553333796560764,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.012430959031917155,
      "full": 0.08139562502037734
    }
  },
  "elapsed_seconds": 1.4733789999736473,
  "result_class": "passed"
}
```
