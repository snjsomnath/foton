# Foton report

Status: **passed**

```json
{
  "scene": "mixed_glazing",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "mixed_glazing",
    "category": "materials",
    "question": "Are adjacent windows with different glass properties kept distinct?",
    "interactions": [
      "multiple_openings",
      "mixed_glazing",
      "material_assignment"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 2,
    "shades": 0,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 4.799999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "66e692d32025fb2f58c7bd2a656d6c020c789f5189a2d586081e6b8158c30d14",
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 14239135421942143921,
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 14239135421942143921,
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
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.7)",
      "weather_id": "82c544d76aea9710a570440071d4833104fdc7da7504bac286ac2afe42bdd614"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/usr/local/radiance/bin/gendaymtx",
      "weather_id": "a39080f6e203418927f730315e529393ad080464468f645476c383a744bbb720"
    },
    "sun_up_hours_equal": true,
    "compared_hours": 4405,
    "max_relative_difference": 0.0,
    "mean_relative_difference": 0.0
  },
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 262144,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/7fb068ed-087d-41c3-b9b3-215cbbd36098/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "622cae5301e41c07e79497fff4373eee58a1763c09d9697e7a50086c4597855f",
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
          "maximum": 0.00020522536942735314,
          "p95": 2.183951437473297e-07,
          "p99": 1.0579911759123206e-05
        },
        "bias_percent": -0.014381607820977372,
        "identifier": "mixed_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7932678487921643,
        "worst_index": [
          29,
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
          "maximum": 0.0004427265375852585,
          "p95": 3.135490260319784e-05,
          "p99": 0.00012543363845907152
        },
        "bias_percent": 0.08586529488204611,
        "identifier": "mixed_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.6112307629792957,
        "worst_index": [
          1,
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
          "maximum": 0.00037744827568531036,
          "p95": 2.557644620537758e-05,
          "p99": 0.00010126130655407906
        },
        "bias_percent": -0.018922841236236505,
        "identifier": "mixed_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3123478596598828,
        "worst_index": [
          4,
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
            "identifier": "mixed_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0011865179112646729,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.00010124262189492583,
                  "p99": 0.00037337548565119505
                },
                "candidate_energy": 7.926779446755063,
                "cvrmse_percent": 53.92468853226501,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.042541732568151816,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.930153071266886,
                "relative_energy_error_percent": 0.042541732568151816,
                "rms_normalized_rmse_percent": 10.996536883881914,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0008117902034427971,
                  "global_sensor_index": 35,
                  "local_sensor_index": 35,
                  "reference": 0.00199830811470747,
                  "rgb_channel": 0,
                  "sky_patch_index": 96
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0016103610396385193,
                  "p50": 0.0,
                  "p90": 2.122366865933163e-05,
                  "p95": 0.00012197290197946131,
                  "p99": 0.0005042931297793984
                },
                "candidate_energy": 2.868663323261842,
                "cvrmse_percent": 204.0563251801225,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.4148655422439201,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.8568113971680944,
                "relative_energy_error_percent": 0.41486554224392,
                "rms_normalized_rmse_percent": 8.011781959539084,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.01820969022810459,
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "reference": 0.016599329188466072,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.53862507268786,
            "full": 228.044250048697
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.39708292204887,
            "full": 234.6753750462085
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 109.2356670415029,
            "full": 238.86691604275256
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 128.89783293940127,
            "full": 230.3125000325963
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
            "identifier": "mixed_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00047877244651317596,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.1385858164867386e-05,
                  "p99": 0.0001531117595732212
                },
                "candidate_energy": 7.9209983867338,
                "cvrmse_percent": 22.942564376546688,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.03308815230495278,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.923620166242472,
                "relative_energy_error_percent": 0.03308815230495278,
                "rms_normalized_rmse_percent": 4.686740550984528,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0055143318604677916,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.005035559413954616,
                  "rgb_channel": 0,
                  "sky_patch_index": 411
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009728260338306427,
                  "p50": 4.9999993478877514e-08,
                  "p90": 2.0833298913203287e-05,
                  "p95": 5.75758058403153e-05,
                  "p99": 0.0002344705098948907
                },
                "candidate_energy": 5.224227062939502,
                "cvrmse_percent": 54.98457553566058,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.20974286082717658,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.235207536997841,
                "relative_energy_error_percent": 0.20974286082717658,
                "rms_normalized_rmse_percent": 3.006552144394215,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.036936670541763306,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.03596384450793266,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.22891702130437,
            "full": 2234.6587909851223
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.2422499516979,
            "full": 2252.1985000930727
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 161.16541693918407,
            "full": 2279.7191250137985
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.5467080064118,
            "full": 2239.3086249940097
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
            "identifier": "mixed_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004895739257335663,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.383809234946966e-05,
                  "p99": 0.00015650945715606213
                },
                "candidate_energy": 7.925569459749113,
                "cvrmse_percent": 24.356357407125778,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.0445765374633298,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.929103979755155,
                "relative_energy_error_percent": 0.04457653746332979,
                "rms_normalized_rmse_percent": 4.979094697062451,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005170102929696441,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.005659676855430007,
                  "rgb_channel": 0,
                  "sky_patch_index": 362
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007294248789548874,
                  "p50": 4.9999993478877514e-08,
                  "p90": 2.0583916739269694e-05,
                  "p95": 5.874599446542561e-05,
                  "p99": 0.00024159264285117388
                },
                "candidate_energy": 5.242954888741551,
                "cvrmse_percent": 54.59658756334288,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.26666619024655003,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.229010884627936,
                "relative_energy_error_percent": 0.26666619024655,
                "rms_normalized_rmse_percent": 2.9841944628547927,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.040101565420627594,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.04083099029958248,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 158.06687506847084,
            "full": 2386.381166987121
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.5880420077592,
            "full": 2369.0441249636933
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 163.68025005795062,
            "full": 2400.949750095606
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 164.49270909652114,
            "full": 2397.7664170088246
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
            "identifier": "mixed_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000309051014482975,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.8628023099154234e-05,
                  "p99": 9.375694207847118e-05
                },
                "candidate_energy": 7.920856027983518,
                "cvrmse_percent": 13.615082434157658,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.047753186947382315,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.924640296279108,
                "relative_energy_error_percent": 0.047753186947382315,
                "rms_normalized_rmse_percent": 2.7824410939836643,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0020874134497717023,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.0023964644642546773,
                  "rgb_channel": 0,
                  "sky_patch_index": 146
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004425019724294543,
                  "p50": 4.9999993478877514e-08,
                  "p90": 1.3582503561337944e-05,
                  "p95": 3.226678381906822e-05,
                  "p99": 0.00013506400864571333
                },
                "candidate_energy": 5.2437646817790515,
                "cvrmse_percent": 30.48630802860996,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.21726572054823343,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.232396477869468,
                "relative_energy_error_percent": 0.2172657205482334,
                "rms_normalized_rmse_percent": 1.6672129234438187,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0003054230473935604,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": -0.00013707892503589392,
                  "rgb_channel": 0,
                  "sky_patch_index": 146
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 251.65620795451105,
            "full": 4229.391290922649
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 243.58216708060354,
            "full": 4201.022916007787
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 233.86258399114013,
            "full": 4210.100458003581
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 233.43625001143664,
            "full": 4198.513292009011
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub/7fb068ed-087d-41c3-b9b3-215cbbd36098/scratchpad/suite-metal-0.3.7/mixed_glazing/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2544.511790969409,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/mixed_glazing/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10842.988125048578,
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
        "identifier": "mixed_glazing_grid",
        "full_identifier": "mixed_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.007872683747039658,
            "cvrmse_percent": 2.2979542923626384,
            "rms_normalized_rmse_percent": 0.469804177816683,
            "reference_energy": 7.922428888392517,
            "candidate_energy": 7.92180518062105,
            "relative_energy_error_percent": 0.007872683747039658,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.2922176867723465e-07,
              "p99": 8.555594831705093e-06,
              "maximum": 8.415780030190945e-05
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0038631197530776262,
              "candidate": 0.003947277553379536,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.1986708433587605,
            "cvrmse_percent": 40.624699397673794,
            "rms_normalized_rmse_percent": 2.2238234251335514,
            "reference_energy": 5.238399855130021,
            "candidate_energy": 5.17560868340803,
            "relative_energy_error_percent": 1.1986708433587605,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.331864644768757e-08,
              "p90": 1.2868182238889865e-05,
              "p95": 2.0888342987746e-05,
              "p99": 5.829986184835434e-05,
              "maximum": 0.0016661100089550018
            },
            "worst": {
              "global_sensor_index": 27,
              "local_sensor_index": 27,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.045810919255018234,
              "candidate": 0.04414480924606323,
              "position": [
                4.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.4818456400374462,
            "cvrmse_percent": 16.1383487952787,
            "rms_normalized_rmse_percent": 2.219493256902737,
            "reference_energy": 13.160828743522538,
            "candidate_energy": 13.097413864029079,
            "relative_energy_error_percent": 0.48184564003745295,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.205190329287234e-08,
              "p90": 1.2916021660203138e-05,
              "p95": 2.0951556507498026e-05,
              "p99": 5.6306831538677216e-05,
              "maximum": 0.0016661100089550018
            },
            "worst": {
              "global_sensor_index": 27,
              "local_sensor_index": 27,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.045810919255018234,
              "candidate": 0.04414480924606323,
              "position": [
                4.5,
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
        "identifier": "mixed_glazing_grid",
        "full_identifier": "mixed_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.007872683747039658,
            "cvrmse_percent": 2.2979542923626384,
            "rms_normalized_rmse_percent": 0.469804177816683,
            "reference_energy": 7.922428888392517,
            "candidate_energy": 7.92180518062105,
            "relative_energy_error_percent": 0.007872683747039658,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.2922176867723465e-07,
              "p99": 8.555594831705093e-06,
              "maximum": 8.415780030190945e-05
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0038631197530776262,
              "candidate": 0.003947277553379536,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 80.4118220431768,
            "cvrmse_percent": 865.4743774430826,
            "rms_normalized_rmse_percent": 34.109125625725866,
            "reference_energy": 2.86877468715403,
            "candidate_energy": 5.17560868340803,
            "relative_energy_error_percent": 80.4118220431768,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.603420635859963e-05,
              "p95": 0.00010473758447915316,
              "p99": 0.0002109211345668882,
              "maximum": 0.012316148728132248
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03228355199098587,
              "candidate": 0.04459970071911812,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.371205466909462,
            "cvrmse_percent": 230.08085378329022,
            "rms_normalized_rmse_percent": 34.109102898067405,
            "reference_energy": 10.791203575546547,
            "candidate_energy": 13.097413864029079,
            "relative_energy_error_percent": 21.371205466909455,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.617699739057575e-05,
              "p95": 0.00010464999650139362,
              "p99": 0.00021215534070506692,
              "maximum": 0.012316148728132248
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03228355199098587,
              "candidate": 0.04459970071911812,
              "position": [
                5.5,
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
      "bias_percent": 0.057299184029705796,
      "rms_normalized_error_percent": 0.15689108187771394,
      "absolute_error": {
        "p95": 0.0806095141924299,
        "p99": 0.09172606691396956,
        "maximum": 0.09569104109577786
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 16.05090488678836,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.15689108187771394
    },
    "overcast": {
      "bias_percent": 0.04256580629258119,
      "rms_normalized_error_percent": 0.10506854459113212,
      "absolute_error": {
        "p95": 0.03633242845535278,
        "p99": 0.0372519850730896,
        "maximum": 0.03766345977783203
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.285859107971191,
      "reference_fraction_of_uniform": 0.6408273577690125,
      "rms_normalized_to_uniform_percent": 0.07408466812802432
    },
    "horizon": {
      "bias_percent": 0.6474277499223897,
      "rms_normalized_error_percent": 1.6718847856058978,
      "absolute_error": {
        "p95": 0.07972451810036396,
        "p99": 0.09559390383026936,
        "maximum": 0.09941022209900652
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.9435427669371252,
      "reference_fraction_of_uniform": 0.12108618053907182,
      "rms_normalized_to_uniform_percent": 0.1298636488546199
    },
    "north": {
      "bias_percent": -73.8861951185277,
      "rms_normalized_error_percent": 99.63406882929158,
      "absolute_error": {
        "p95": 7.593173359055072e-05,
        "p99": 9.30390604025888e-05,
        "maximum": 9.454269002162619e-05
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.1698833986883983e-05,
      "reference_fraction_of_uniform": 7.288581969078223e-07,
      "rms_normalized_to_uniform_percent": 9.940431645734005e-05
    },
    "east": {
      "bias_percent": 0.007922369758635067,
      "rms_normalized_error_percent": 0.23073455848281313,
      "absolute_error": {
        "p95": 0.023142099380493164,
        "p99": 0.041615724563598605,
        "maximum": 0.049436330795288086
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.356983184814453,
      "reference_fraction_of_uniform": 0.20914603769779205,
      "rms_normalized_to_uniform_percent": 0.05196462654293592
    },
    "south": {
      "bias_percent": 0.08750867363530636,
      "rms_normalized_error_percent": 0.21746326640187172,
      "absolute_error": {
        "p95": 0.07941967248916626,
        "p99": 0.09123854637145995,
        "maximum": 0.0949392318725586
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 11.095128059387207,
      "reference_fraction_of_uniform": 0.6912462711334229,
      "rms_normalized_to_uniform_percent": 0.13974300409705664
    },
    "west": {
      "bias_percent": -0.07829961055346542,
      "rms_normalized_error_percent": 0.20905765417495661,
      "absolute_error": {
        "p95": 0.029317855834960938,
        "p99": 0.042065715789794914,
        "maximum": 0.04404640197753906
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.9388039112091064,
      "reference_fraction_of_uniform": 0.18309272825717926,
      "rms_normalized_to_uniform_percent": 0.048969995162188834
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
        "identifier": "mixed_glazing_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.02448768342470922,
          "cvrmse_percent": 1.6175343671753315,
          "absolute_error_percentiles_lux": {
            "p50": 2.5887374877929688,
            "p90": 28.891894531250024,
            "p95": 44.30462036132811,
            "p99": 96.57178955078103
          },
          "maximum_absolute_error_lux": 391.3271484375,
          "worst": {
            "sensor_index": 26,
            "position": [
              4.5,
              3.5,
              0.75
            ],
            "hour_of_year": 1356.5,
            "foton_lux": 16327.3779296875,
            "radiance_lux": 16718.705078125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.24412861491628568,
            "maximum_error_percentage_points": 1.890273972602742,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.0635858490836192,
            "maximum_error_percentage_points": 0.2610785659261552,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.06431506849315073,
            "maximum_error_percentage_points": 0.24931506849315,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.0869178082191775,
            "maximum_error_percentage_points": 0.2168493150684867,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.04310882800608818,
            "maximum_error_percentage_points": 0.16821917808218956,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 97.22222222222223,
          "radiance_percent": 94.44444444444444,
          "difference_percentage_points": 2.7777777777777857,
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
      "maximum_error_percentage_points": 0.004990368150671998,
      "metrics": {
        "da": [
          {
            "identifier": "mixed_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "mixed_glazing_grid",
            "maximum_error_percentage_points": 0.004990368150671998,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "mixed_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "mixed_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "mixed_glazing_grid",
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
      "study_preparation_seconds": 0.006363583030179143,
      "weather_seconds": 0.08038195804692805,
      "metric_reduction_seconds": 0.138853499898687,
      "write_seconds": 0.024074416840448976,
      "total_seconds": 0.24343095789663494,
      "cold_end_to_end_seconds": 0.24979454092681408,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.002556708874180913,
      "engine_upload_seconds": 0.000876666,
      "engine_acceleration_structure_seconds": 0.003100958,
      "engine_tracing_seconds": 0.058686333475634456,
      "engine_annual_reduction_seconds": 0.001797541743144393,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.058686333475634456
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006363583030179143,
      "weather_seconds": 0.0787485409528017,
      "metric_reduction_seconds": 0.05274887499399483,
      "write_seconds": 0.01636579097248614,
      "total_seconds": 0.14800641709007323,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14800641709007323,
      "raw_export_seconds": 0.004174083936959505,
      "engine_upload_seconds": 4.5834e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0014150000642985106,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.020468374947085977,
      "full": 0.06212504091672599
    }
  },
  "elapsed_seconds": 1.3228740410413593,
  "result_class": "passed"
}
```
