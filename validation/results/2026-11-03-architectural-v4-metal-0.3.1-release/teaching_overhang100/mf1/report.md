# Foton report

Status: **passed**

```json
{
  "scene": "teaching_overhang100",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_overhang100",
    "category": "teaching",
    "question": "What does a 1.0 m overhang remove from the base room?",
    "interactions": [
      "multiple_bounces",
      "overhang",
      "side_glazing"
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
    "aperture_area": 4.499999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "2124bf84c92a0ec57d1f84963a604833840e83453ffbe812cdba984624e1bb5a",
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
      "scene_fingerprint": 18413353015155885056,
      "basis": "Tregenza",
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
      "scene_fingerprint": 18413353015155885056,
      "basis": "Tregenza",
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/refbundle/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "10168649335a6278897f6292bb21d63b48ce2f88595354b33dd9d3c320a17cfe",
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
          "maximum": 0.0005787150003015995,
          "p95": 9.785384463611966e-06,
          "p99": 0.00011097453534603119
        },
        "bias_percent": -0.09571524593148503,
        "identifier": "teaching_overhang100_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.448056337746342,
        "worst_index": [
          16,
          70,
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
          "maximum": 0.000568147748708725,
          "p95": 5.518285906873633e-05,
          "p99": 0.00017307419329881668
        },
        "bias_percent": 0.11568321327462874,
        "identifier": "teaching_overhang100_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8803819200036115,
        "worst_index": [
          19,
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
          "maximum": 0.0006906129419803619,
          "p95": 4.4234050437808e-05,
          "p99": 0.00012241210788488388
        },
        "bias_percent": 0.010671222885046261,
        "identifier": "teaching_overhang100_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7864544198749828,
        "worst_index": [
          19,
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
            "identifier": "teaching_overhang100_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.001088376040570438,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.00010768781066872091,
                  "p99": 0.0004182918928563595
                },
                "candidate_energy": 5.1451932538584515,
                "cvrmse_percent": 24.579851633469563,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.006013545220002826,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.144883863940777,
                "relative_energy_error_percent": 0.006013545220002825,
                "rms_normalized_rmse_percent": 5.420388282383029,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002443436998873949,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0013550609583035111,
                  "rgb_channel": 0,
                  "sky_patch_index": 19
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.002356000244617462,
                  "p50": 0.0,
                  "p90": 2.3255999167304253e-05,
                  "p95": 0.00019190959283150682,
                  "p99": 0.0006481236778199673
                },
                "candidate_energy": 3.5124321862459453,
                "cvrmse_percent": 54.406446153199674,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.03016927098924902,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.5134921812232847,
                "relative_energy_error_percent": 0.030169270989249024,
                "rms_normalized_rmse_percent": 3.9602396067629235,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.045855239033699036,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.043499238789081573,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 112.6618329435587,
            "full": 250.40158303454518
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 111.42458289396018,
            "full": 240.95387500710785
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.87812500167638,
            "full": 239.69358298927546
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 115.10195897426456,
            "full": 235.16283289063722
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
            "identifier": "teaching_overhang100_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003870297223329544,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.2640907708555e-05,
                  "p99": 0.00018958118744194508
                },
                "candidate_energy": 5.148860627243266,
                "cvrmse_percent": 10.911827451671092,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.09008995891005625,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.153503416353487,
                "relative_energy_error_percent": 0.09008995891005625,
                "rms_normalized_rmse_percent": 2.4094357586527897,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0076535046100616455,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.007266474887728691,
                  "rgb_channel": 0,
                  "sky_patch_index": 72
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009073354303836823,
                  "p50": 1.10331896507887e-07,
                  "p90": 3.240609657950699e-05,
                  "p95": 9.762514382600769e-05,
                  "p99": 0.0002907395828515291
                },
                "candidate_energy": 5.620067969264227,
                "cvrmse_percent": 17.262025251040495,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.041402519693150536,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.622395782785421,
                "relative_energy_error_percent": 0.041402519693150536,
                "rms_normalized_rmse_percent": 1.5928705993443795,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03826049901545048,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.03916783444583416,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.82604099530727,
            "full": 2243.4087499277666
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.5495000546798,
            "full": 2245.727500063367
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.01237504556775,
            "full": 2264.3440830288455
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 145.6522090593353,
            "full": 2235.236707958393
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
            "identifier": "teaching_overhang100_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00038739945739507675,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.707000043708827e-05,
                  "p99": 0.0001780269667506218
                },
                "candidate_energy": 5.154633728154295,
                "cvrmse_percent": 10.117625379601737,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.11302755562929288,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.148814149377358,
                "relative_energy_error_percent": 0.11302755562929287,
                "rms_normalized_rmse_percent": 2.229966793164287,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007175076520070434,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.00756247597746551,
                  "rgb_channel": 0,
                  "sky_patch_index": 72
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009724423289299011,
                  "p50": 1.207120661206318e-07,
                  "p90": 3.155804006382823e-05,
                  "p95": 0.00010039986809715616,
                  "p99": 0.00028555537573993206
                },
                "candidate_energy": 5.633758740096489,
                "cvrmse_percent": 15.731384739597242,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.021550583413826034,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.632544893810827,
                "relative_energy_error_percent": 0.021550583413826034,
                "rms_normalized_rmse_percent": 1.4523589965821961,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07014906033873558,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.06917661800980568,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.97433302737772,
            "full": 2400.1325418939814
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.35170803032815,
            "full": 2388.0424589151517
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.76383293792605,
            "full": 2408.311666920781
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.73249995615333,
            "full": 2402.8820829698816
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
            "identifier": "teaching_overhang100_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000263735419139266,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.313518536742776e-05,
                  "p99": 0.00011293549323454499
                },
                "candidate_energy": 5.1497325848622495,
                "cvrmse_percent": 6.1404708919565865,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.061244662833550186,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.152888454022104,
                "relative_energy_error_percent": 0.06124466283355017,
                "rms_normalized_rmse_percent": 1.3560067906798914,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.006346061592921615,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.006609797012060881,
                  "rgb_channel": 0,
                  "sky_patch_index": 42
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005544386804103851,
                  "p50": 1.0776453152061549e-07,
                  "p90": 2.0694445993285626e-05,
                  "p95": 5.8092828840017086e-05,
                  "p99": 0.00017638271674513817
                },
                "candidate_energy": 5.636149639345131,
                "cvrmse_percent": 9.830424368722463,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.05089676112966234,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.633282481017009,
                "relative_energy_error_percent": 0.05089676112966234,
                "rms_normalized_rmse_percent": 0.90733122214588,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.041580185294151306,
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "reference": 0.04102574661374092,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 197.54725007805973,
            "full": 4174.066832987592
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 196.42375002149493,
            "full": 4228.122374974191
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 200.0585829373449,
            "full": 4213.861666969024
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 192.38824991043657,
            "full": 4167.895499966107
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/suite-0.3.1/run/teaching_overhang100/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 765.7434999709949,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_overhang100/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2736.731334007345,
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
        "identifier": "teaching_overhang100_grid",
        "full_identifier": "teaching_overhang100_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.054825361397700355,
            "cvrmse_percent": 4.192957358379689,
            "rms_normalized_rmse_percent": 0.9257446061562035,
            "reference_energy": 5.150337977747768,
            "candidate_energy": 5.147514286338264,
            "relative_energy_error_percent": 0.05482536139770036,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.612474003806648e-06,
              "p99": 5.642976611852646e-05,
              "maximum": 0.00029316358268260956
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 70,
              "rgb_channel": 0,
              "reference": 0.004271685611456633,
              "candidate": 0.004564849194139242,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.0300958473722803,
            "cvrmse_percent": 23.22095817629416,
            "rms_normalized_rmse_percent": 2.1446649473361163,
            "reference_energy": 5.6356886388610885,
            "candidate_energy": 5.577635644221349,
            "relative_energy_error_percent": 1.03009584737228,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5204867881711834e-07,
              "p90": 3.4877914004027843e-05,
              "p95": 5.6480766943423044e-05,
              "p99": 0.00013019455946050584,
              "maximum": 0.0019852519035339355
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05090299993753433,
              "candidate": 0.0489177480340004,
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
            "nmbe_percent": -0.5644032618601345,
            "cvrmse_percent": 12.106889329698378,
            "rms_normalized_rmse_percent": 2.140062152310578,
            "reference_energy": 10.786026616608856,
            "candidate_energy": 10.725149930559613,
            "relative_energy_error_percent": 0.5644032618601345,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.52178878668019e-07,
              "p90": 3.354546788614243e-05,
              "p95": 5.5339123355224696e-05,
              "p99": 0.00012846291065216064,
              "maximum": 0.0019852519035339355
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05090299993753433,
              "candidate": 0.0489177480340004,
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
        "identifier": "teaching_overhang100_grid",
        "full_identifier": "teaching_overhang100_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.054825361397700355,
            "cvrmse_percent": 4.192957358379689,
            "rms_normalized_rmse_percent": 0.9257446061562035,
            "reference_energy": 5.150337977747768,
            "candidate_energy": 5.147514286338264,
            "relative_energy_error_percent": 0.05482536139770036,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.612474003806648e-06,
              "p99": 5.642976611852646e-05,
              "maximum": 0.00029316358268260956
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 70,
              "rgb_channel": 0,
              "reference": 0.004271685611456633,
              "candidate": 0.004564849194139242,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 59.01288363907214,
            "cvrmse_percent": 406.0620288749089,
            "rms_normalized_rmse_percent": 29.492956432705995,
            "reference_energy": 3.5076627230290853,
            "candidate_energy": 5.577635644221349,
            "relative_energy_error_percent": 59.01288363907214,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00023317999148275703,
              "p95": 0.00032528983711017624,
              "p99": 0.0006599292391911149,
              "maximum": 0.012477202340960503
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015905337408185005,
              "candidate": 0.028382539749145508,
              "position": [
                3.5,
                5.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 23.875595547102257,
            "cvrmse_percent": 164.50300909158895,
            "rms_normalized_rmse_percent": 29.4916835187146,
            "reference_energy": 8.658000700776853,
            "candidate_energy": 10.725149930559613,
            "relative_energy_error_percent": 23.875595547102254,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002318723127245903,
              "p95": 0.0003254064573411596,
              "p99": 0.0006789981853216887,
              "maximum": 0.012477202340960503
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015905337408185005,
              "candidate": 0.028382539749145508,
              "position": [
                3.5,
                5.5,
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
      "bias_percent": 0.19281148373676849,
      "rms_normalized_error_percent": 0.3403439525440924,
      "absolute_error": {
        "p95": 0.11797407192428444,
        "p99": 0.13386475229393408,
        "maximum": 0.13598692630449127
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.573314515024116,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.3403439525440924
    },
    "overcast": {
      "bias_percent": 0.13027683612984575,
      "rms_normalized_error_percent": 0.31946320696167246,
      "absolute_error": {
        "p95": 0.06417706608772278,
        "p99": 0.08712992668151852,
        "maximum": 0.09491348266601562
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.945851802825928,
      "reference_fraction_of_uniform": 0.5623450875282288,
      "rms_normalized_to_uniform_percent": 0.19526984546072246
    },
    "horizon": {
      "bias_percent": 1.037210447766554,
      "rms_normalized_error_percent": 2.2053657360634262,
      "absolute_error": {
        "p95": 0.07640738101982336,
        "p99": 0.10564069162165307,
        "maximum": 0.1155354994570934
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.599954948419566,
      "reference_fraction_of_uniform": 0.15132009419998957,
      "rms_normalized_to_uniform_percent": 0.22760301176997616
    },
    "north": {
      "bias_percent": -99.52333823732256,
      "rms_normalized_error_percent": 99.75910260939258,
      "absolute_error": {
        "p95": 0.00010651095146840817,
        "p99": 0.00019686644689045338,
        "maximum": 0.00023377168690785766
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.1740888769272715e-05,
      "reference_fraction_of_uniform": 2.0562038116622716e-06,
      "rms_normalized_to_uniform_percent": 0.00031425859828658183
    },
    "east": {
      "bias_percent": 0.08345805757069408,
      "rms_normalized_error_percent": 0.3604980464843767,
      "absolute_error": {
        "p95": 0.019681744277477264,
        "p99": 0.03720536381006237,
        "maximum": 0.045928955078125
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.2859389781951904,
      "reference_fraction_of_uniform": 0.2161988914012909,
      "rms_normalized_to_uniform_percent": 0.08682284717732958
    },
    "south": {
      "bias_percent": 0.27163089667829254,
      "rms_normalized_error_percent": 0.4078360455756808,
      "absolute_error": {
        "p95": 0.11190664768218994,
        "p99": 0.13035666942596433,
        "maximum": 0.13405919075012207
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.009634017944336,
      "reference_fraction_of_uniform": 0.7575329542160034,
      "rms_normalized_to_uniform_percent": 0.2940334166380464
    },
    "west": {
      "bias_percent": 0.027863156790783845,
      "rms_normalized_error_percent": 0.3883735979727965,
      "absolute_error": {
        "p95": 0.02700687199831009,
        "p99": 0.03195293396711348,
        "maximum": 0.03456592559814453
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.2278928756713867,
      "reference_fraction_of_uniform": 0.21070903539657593,
      "rms_normalized_to_uniform_percent": 0.0926105692493609
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
        "identifier": "teaching_overhang100_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.027699155264056058,
          "cvrmse_percent": 1.7981934856805366,
          "absolute_error_percentiles_lux": {
            "p50": 2.5878372192382812,
            "p90": 20.956256103515628,
            "p95": 32.09018859863278,
            "p99": 65.90986816406242
          },
          "maximum_absolute_error_lux": 372.248046875,
          "worst": {
            "sensor_index": 23,
            "position": [
              3.5,
              0.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 6335.7646484375,
            "radiance_lux": 6708.0126953125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.3346080669710811,
            "maximum_error_percentage_points": 2.1413698630137006,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.13776792091323248,
            "maximum_error_percentage_points": 0.7172014234381265,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.09162480974124781,
            "maximum_error_percentage_points": 0.33232876712328974,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.10913242009132408,
            "maximum_error_percentage_points": 0.2980821917808214,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.043721461187214705,
            "maximum_error_percentage_points": 0.2693150684931531,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 69.44444444444444,
          "radiance_percent": 66.66666666666667,
          "difference_percentage_points": 2.7777777777777715,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 1,
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
      "maximum_error_percentage_points": 0.004931506849302991,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_overhang100_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_overhang100_grid",
            "maximum_error_percentage_points": 0.004734053938349803,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_overhang100_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_overhang100_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_overhang100_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
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
      "study_preparation_seconds": 0.006864249939098954,
      "weather_seconds": 0.09808204194996506,
      "metric_reduction_seconds": 0.04039212502539158,
      "write_seconds": 0.04360633308533579,
      "total_seconds": 0.18226112495176494,
      "cold_end_to_end_seconds": 0.1891253748908639,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.025140915997326374,
      "engine_upload_seconds": 0.000306667,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.019493750063702464,
      "engine_annual_reduction_seconds": 0.00035087508149445057,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.019493750063702464
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006864249939098954,
      "weather_seconds": 0.09497433307114989,
      "metric_reduction_seconds": 0.012719791964627802,
      "write_seconds": 0.02761895803268999,
      "total_seconds": 0.1354970420943573,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1354970420943573,
      "raw_export_seconds": 0.010169041925109923,
      "engine_upload_seconds": 5.1375e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0003733333433046937,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.010064041009172797,
      "full": 0.021601916989311576
    }
  },
  "elapsed_seconds": 0.6814355839742348,
  "result_class": "passed"
}
```
