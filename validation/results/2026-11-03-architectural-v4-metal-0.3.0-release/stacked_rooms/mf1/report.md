# Foton report

Status: **passed**

```json
{
  "scene": "stacked_rooms",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "stacked_rooms",
    "category": "connections",
    "question": "Does an opaque shared slab isolate two storeys?",
    "interactions": [
      "stacked_zones",
      "opaque_adjacency",
      "room_isolation"
    ],
    "room_count": 2,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 2,
    "apertures": 2,
    "shades": 0,
    "sensors": 72,
    "floor_area": 72.0,
    "aperture_area": 5.999999999999997
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "6855a915a6ea5a03b0701648644b6e1f0ab2ee68e4fdb55698b9bf5178215fac",
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 6348620744982744529,
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 6348620744982744529,
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/foton-references-corpus4-2026-11-03",
    "model_sha256": "4bfac668c37ffc604342292b499e2b090d664248f9834ac469cdbb2450989615",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "2b608cd5602657572292d87b033fd5c28fb4057c61e72dafb0127ed46035037c",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0003254120238125324,
          "p95": 3.595137968659345e-06,
          "p99": 9.213294833898544e-05
        },
        "bias_percent": -0.07931914448047922,
        "identifier": "stacked_rooms_0_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0753890946716322,
        "worst_index": [
          9,
          72,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0003254120238125324,
          "p95": 3.595137968659345e-06,
          "p99": 9.213294833898544e-05
        },
        "bias_percent": -0.0793895981759524,
        "identifier": "stacked_rooms_1_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0753908507263903,
        "worst_index": [
          9,
          72,
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
          "maximum": 0.0005673319101333618,
          "p95": 4.536359047051517e-05,
          "p99": 0.00015099160373210907
        },
        "bias_percent": 0.015577800984142182,
        "identifier": "stacked_rooms_0_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.089771236908872,
        "worst_index": [
          17,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00042868219316005707,
          "p95": 4.5239093014970385e-05,
          "p99": 0.00014785118401050568
        },
        "bias_percent": 0.041896660493989296,
        "identifier": "stacked_rooms_1_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0241501860095195,
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
          "maximum": 0.0004816912114620209,
          "p95": 3.6735949106514335e-05,
          "p99": 0.00012060161679983139
        },
        "bias_percent": -0.04415746448064737,
        "identifier": "stacked_rooms_0_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9100621015338393,
        "worst_index": [
          32,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00043617933988571167,
          "p95": 3.9378664223477234e-05,
          "p99": 0.00012317881919443607
        },
        "bias_percent": 0.0336463022040604,
        "identifier": "stacked_rooms_1_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9338823985023088,
        "worst_index": [
          14,
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
            "identifier": "stacked_rooms_0_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007030349224805832,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 9.33124472794588e-05,
                  "p99": 0.00035450514405965805
                },
                "candidate_energy": 6.020412568524989,
                "cvrmse_percent": 16.596226792717374,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0016654465616215775,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.020312303440733,
                "relative_energy_error_percent": 0.0016654465616215773,
                "rms_normalized_rmse_percent": 3.3900485096813466,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.017964884638786316,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.017261849716305733,
                  "rgb_channel": 0,
                  "sky_patch_index": 117
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011910760076716542,
                  "p50": 0.0,
                  "p90": 2.0821184079977684e-05,
                  "p95": 0.0001471229718617905,
                  "p99": 0.0005402052775025368
                },
                "candidate_energy": 2.0761806301402217,
                "cvrmse_percent": 74.69192749066384,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.4563164986381101,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.066749710226901,
                "relative_energy_error_percent": 0.45631649863810997,
                "rms_normalized_rmse_percent": 4.116875737947189,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00025229586753994226,
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "reference": -0.000938780140131712,
                  "rgb_channel": 0,
                  "sky_patch_index": 45
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000877580139786005,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 9.209490381181235e-05,
                  "p99": 0.000388175540138036
                },
                "candidate_energy": 6.017260253524,
                "cvrmse_percent": 19.020002748499333,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.06584661794940948,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.0212250265631155,
                "relative_energy_error_percent": 0.06584661794940946,
                "rms_normalized_rmse_percent": 3.8844460081968637,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013013530056923628,
                  "global_sensor_index": 59,
                  "local_sensor_index": 23,
                  "reference": 0.013891110196709633,
                  "rgb_channel": 0,
                  "sky_patch_index": 71
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011124196462333202,
                  "p50": 0.0,
                  "p90": 1.7408424810128054e-05,
                  "p95": 0.0001650128513574599,
                  "p99": 0.0005089128389954567
                },
                "candidate_energy": 2.088245768132495,
                "cvrmse_percent": 72.48682929320393,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.5190754927568125,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.077462171130861,
                "relative_energy_error_percent": 0.5190754927568125,
                "rms_normalized_rmse_percent": 4.01786360565284,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0005392646417021751,
                  "global_sensor_index": 59,
                  "local_sensor_index": 23,
                  "reference": -0.0005731550045311451,
                  "rgb_channel": 0,
                  "sky_patch_index": 71
                }
              }
            },
            "start_sensor_index": 36
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.4001250723377,
            "full": 438.96724993828684
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 163.55570894666016,
            "full": 437.946958001703
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.30133396573365,
            "full": 421.43387510441244
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.71966701745987,
            "full": 438.4427919285372
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
            "identifier": "stacked_rooms_0_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00044467649422585964,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.3912685214308995e-05,
                  "p99": 0.0001677689142525196
                },
                "candidate_energy": 6.01597168970784,
                "cvrmse_percent": 8.143938918083432,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.051069398044857495,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.012900937394079,
                "relative_energy_error_percent": 0.051069398044857495,
                "rms_normalized_rmse_percent": 1.6638044522920479,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002269585500471294,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.0018249090062454343,
                  "rgb_channel": 0,
                  "sky_patch_index": 15
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009579183533787727,
                  "p50": 2.2657141585114005e-07,
                  "p90": 2.9660041036549956e-05,
                  "p95": 7.86768854595719e-05,
                  "p99": 0.0002653850242495537
                },
                "candidate_energy": 3.8126715594375646,
                "cvrmse_percent": 21.636588065241916,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.4387437953866102,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8294731352143145,
                "relative_energy_error_percent": 0.43874379538661024,
                "rms_normalized_rmse_percent": 1.8749656772141545,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03085209522396326,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.03181001357734203,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00042121484875679016,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.6658568317070555e-05,
                  "p99": 0.00017886795103549957
                },
                "candidate_energy": 6.018676356220567,
                "cvrmse_percent": 8.713518537620843,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.01725533563113666,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.017637992587879,
                "relative_energy_error_percent": 0.01725533563113666,
                "rms_normalized_rmse_percent": 1.7826795042468293,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.01308785006403923,
                  "global_sensor_index": 53,
                  "local_sensor_index": 17,
                  "reference": 0.01350906491279602,
                  "rgb_channel": 0,
                  "sky_patch_index": 71
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000682000070810318,
                  "p50": 2.271372068207711e-07,
                  "p90": 3.053124964935705e-05,
                  "p95": 8.457221556454847e-05,
                  "p99": 0.00027958955615758896
                },
                "candidate_energy": 3.8180786708751135,
                "cvrmse_percent": 21.58671995034623,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.04436556929592384,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8163855097172004,
                "relative_energy_error_percent": 0.04436556929592385,
                "rms_normalized_rmse_percent": 1.8669395283147312,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.029170329682528973,
                  "global_sensor_index": 63,
                  "local_sensor_index": 27,
                  "reference": 0.028488329611718655,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 36
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 210.7504999730736,
            "full": 5046.908958000131
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 211.25520800706,
            "full": 5072.787291952409
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 221.2632920127362,
            "full": 5089.706417056732
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 219.41404195968062,
            "full": 4992.78329196386
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
            "identifier": "stacked_rooms_0_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003142284695059061,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.5626528844877605e-05,
                  "p99": 0.00016157887876033783
                },
                "candidate_energy": 6.010933576734715,
                "cvrmse_percent": 7.658027869035894,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.09176652934715661,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.016454668373626,
                "relative_energy_error_percent": 0.09176652934715661,
                "rms_normalized_rmse_percent": 1.5662232985883877,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007533811032772064,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.007219582563266158,
                  "rgb_channel": 0,
                  "sky_patch_index": 49
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006611496210098267,
                  "p50": 2.2185030346122403e-07,
                  "p90": 2.8994865715503693e-05,
                  "p95": 8.202062454074616e-05,
                  "p99": 0.00026386650279164314
                },
                "candidate_energy": 3.8245072792414128,
                "cvrmse_percent": 20.405579295829472,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.060730601297260045,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8221860426749963,
                "relative_energy_error_percent": 0.060730601297260045,
                "rms_normalized_rmse_percent": 1.7665930015192222,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.026210404932498932,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.02687155455350876,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003756200894713402,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.681425005197434e-05,
                  "p99": 0.00016091135330498219
                },
                "candidate_energy": 6.016682340650732,
                "cvrmse_percent": 7.386502246582983,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.017655625313646513,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.015620245279933,
                "relative_energy_error_percent": 0.01765562531364651,
                "rms_normalized_rmse_percent": 1.5108276477278997,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.01394177507609129,
                  "global_sensor_index": 53,
                  "local_sensor_index": 17,
                  "reference": 0.01356615498661995,
                  "rgb_channel": 0,
                  "sky_patch_index": 94
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006884550675749779,
                  "p50": 2.358348076825223e-07,
                  "p90": 2.9004055249970406e-05,
                  "p95": 8.09881312306968e-05,
                  "p99": 0.0002624606713652611
                },
                "candidate_energy": 3.8256333505742965,
                "cvrmse_percent": 21.064327162279916,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.11905841799828523,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8210840283797225,
                "relative_energy_error_percent": 0.11905841799828523,
                "rms_normalized_rmse_percent": 1.824305446621816,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02141980454325676,
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "reference": 0.020731349475681782,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 36
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 213.27200008090585,
            "full": 5382.6305830152705
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 217.48941706027836,
            "full": 5382.29904207401
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 223.1733340304345,
            "full": 5415.971541078761
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 209.35079199261963,
            "full": 5417.693000053987
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
            "identifier": "stacked_rooms_0_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00023774593137204647,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.596835838630793e-05,
                  "p99": 9.25541389733553e-05
                },
                "candidate_energy": 6.014435920975302,
                "cvrmse_percent": 4.647025932709157,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.004224722699307174,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.0141818384699945,
                "relative_energy_error_percent": 0.004224722699307174,
                "rms_normalized_rmse_percent": 0.9500477010876266,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.006289305631071329,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.006051559699699283,
                  "rgb_channel": 0,
                  "sky_patch_index": 41
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004502497613430023,
                  "p50": 1.394407806998288e-07,
                  "p90": 2.0076942746527493e-05,
                  "p95": 5.136600229889154e-05,
                  "p99": 0.0001653748913668096
                },
                "candidate_energy": 3.817802514517151,
                "cvrmse_percent": 12.87212316870399,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.030670082094082913,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8189737969158166,
                "relative_energy_error_percent": 0.030670082094082913,
                "rms_normalized_rmse_percent": 1.114054258781531,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.021220124326646328,
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "reference": 0.020769874565303326,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00021134037524461746,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.327656548004596e-05,
                  "p99": 9.092455729842186e-05
                },
                "candidate_energy": 6.013411035462013,
                "cvrmse_percent": 4.440872119611246,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.007484476666571658,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.013861141495909,
                "relative_energy_error_percent": 0.007484476666571657,
                "rms_normalized_rmse_percent": 0.9080035832735213,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.017754879780113697,
                  "global_sensor_index": 53,
                  "local_sensor_index": 17,
                  "reference": 0.017966220155358315,
                  "rgb_channel": 0,
                  "sky_patch_index": 119
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006751399487257004,
                  "p50": 1.6048626605424943e-07,
                  "p90": 2.0434737962204963e-05,
                  "p95": 4.934939788654428e-05,
                  "p99": 0.00015752646140754223
                },
                "candidate_energy": 3.829504125749594,
                "cvrmse_percent": 14.006188196126608,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.01669690765501005,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.828864823725741,
                "relative_energy_error_percent": 0.01669690765501005,
                "rms_normalized_rmse_percent": 1.2139853921450487,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03200634941458702,
                  "global_sensor_index": 51,
                  "local_sensor_index": 15,
                  "reference": 0.03133120946586132,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 36
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 337.59762498084456,
            "full": 9409.201957983896
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 334.5474579837173,
            "full": 9536.169208935462
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 347.3362500080839,
            "full": 9371.68129091151
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 344.66654201969504,
            "full": 9335.274958983064
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/stacked_rooms/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 3289.4546249881387,
      "invocation_count": 5,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/stacked_rooms/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 12313.629832933657,
      "invocation_count": 5,
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
      72,
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
        "identifier": "stacked_rooms_0_grid",
        "full_identifier": "stacked_rooms_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.045817622317891354,
            "cvrmse_percent": 3.4361133159179285,
            "rms_normalized_rmse_percent": 0.7026164804842399,
            "reference_energy": 6.017107739270614,
            "candidate_energy": 6.014350843572174,
            "relative_energy_error_percent": 0.04581762231789136,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.2354885004460016e-06,
              "p99": 5.3141440730541945e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.0191827766942523,
            "cvrmse_percent": 23.732988003265,
            "rms_normalized_rmse_percent": 2.052411121331565,
            "reference_energy": 3.8155892802277815,
            "candidate_energy": 3.776701451454308,
            "relative_energy_error_percent": 1.0191827766942523,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.721799993807508e-07,
              "p90": 3.706640563905239e-05,
              "p95": 5.477431113831698e-05,
              "p99": 0.00013474561274051666,
              "maximum": 0.001275908201932907
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02628614753484726,
              "candidate": 0.025010239332914352,
              "position": [
                3.5,
                3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.4235330793711147,
            "cvrmse_percent": 9.11816098825562,
            "rms_normalized_rmse_percent": 2.032030548171239,
            "reference_energy": 9.832697019498395,
            "candidate_energy": 9.791052295026482,
            "relative_energy_error_percent": 0.4235330793711147,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.650581726968085e-07,
              "p90": 3.659774665720761e-05,
              "p95": 5.383537700254233e-05,
              "p99": 0.00012592459097504616,
              "maximum": 0.001275908201932907
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02628614753484726,
              "candidate": 0.025010239332914352,
              "position": [
                3.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "full_identifier": "stacked_rooms_1_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.04574714495092785,
            "cvrmse_percent": 3.436127666028291,
            "rms_normalized_rmse_percent": 0.7026190577945717,
            "reference_energy": 6.017103496630625,
            "candidate_energy": 6.014350843572174,
            "relative_energy_error_percent": 0.04574714495092785,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.4322187528013656e-06,
              "p99": 5.3141440730541945e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                3.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.8646960137880932,
            "cvrmse_percent": 24.07031696183686,
            "rms_normalized_rmse_percent": 2.084547407524757,
            "reference_energy": 3.8257171176762714,
            "candidate_energy": 3.792636294260916,
            "relative_energy_error_percent": 0.8646960137880932,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.683364179276396e-07,
              "p90": 3.751867916435003e-05,
              "p95": 5.687933517037891e-05,
              "p99": 0.00013850838877260685,
              "maximum": 0.0012763682752847672
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02980462834239006,
              "candidate": 0.028528260067105293,
              "position": [
                1.5,
                1.5,
                3.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.3640569901448895,
            "cvrmse_percent": 9.285757911692645,
            "rms_normalized_rmse_percent": 2.0689692703908666,
            "reference_energy": 9.842820614306897,
            "candidate_energy": 9.80698713783309,
            "relative_energy_error_percent": 0.3640569901448895,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.761360739597876e-07,
              "p90": 3.7386780604720116e-05,
              "p95": 5.614608453470281e-05,
              "p99": 0.00013263151049613953,
              "maximum": 0.0012763682752847672
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02980462834239006,
              "candidate": 0.028528260067105293,
              "position": [
                1.5,
                1.5,
                3.75
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
      72,
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
        "identifier": "stacked_rooms_0_grid",
        "full_identifier": "stacked_rooms_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.045817622317891354,
            "cvrmse_percent": 3.4361133159179285,
            "rms_normalized_rmse_percent": 0.7026164804842399,
            "reference_energy": 6.017107739270614,
            "candidate_energy": 6.014350843572174,
            "relative_energy_error_percent": 0.04581762231789136,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.2354885004460016e-06,
              "p99": 5.3141440730541945e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 82.03428143608787,
            "cvrmse_percent": 439.64913546388306,
            "rms_normalized_rmse_percent": 24.32521074728984,
            "reference_energy": 2.0747198943295224,
            "candidate_energy": 3.776701451454308,
            "relative_energy_error_percent": 82.03428143608787,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002216400025645271,
              "p95": 0.00029174920928198833,
              "p99": 0.0005213699769228697,
              "maximum": 0.007833669893443584
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011530480347573757,
              "candidate": 0.01936415024101734,
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
            "nmbe_percent": 20.999269119012897,
            "cvrmse_percent": 112.70175935192466,
            "rms_normalized_rmse_percent": 24.32026123600268,
            "reference_energy": 8.091827633600136,
            "candidate_energy": 9.791052295026482,
            "relative_energy_error_percent": 20.999269119012897,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00022184941917657852,
              "p95": 0.00029013120220042763,
              "p99": 0.0005274565482977778,
              "maximum": 0.007833669893443584
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011530480347573757,
              "candidate": 0.01936415024101734,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "full_identifier": "stacked_rooms_1_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.04574714495092785,
            "cvrmse_percent": 3.436127666028291,
            "rms_normalized_rmse_percent": 0.7026190577945717,
            "reference_energy": 6.017103496630625,
            "candidate_energy": 6.014350843572174,
            "relative_energy_error_percent": 0.04574714495092785,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.4322187528013656e-06,
              "p99": 5.3141440730541945e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                3.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.9016220554361,
            "cvrmse_percent": 435.9831260764742,
            "rms_normalized_rmse_percent": 24.23233075151665,
            "reference_energy": 2.0849931140828843,
            "candidate_energy": 3.792636294260916,
            "relative_energy_error_percent": 81.9016220554361,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002219400048488751,
              "p95": 0.0002967282911413349,
              "p99": 0.0004996056668460369,
              "maximum": 0.00810663215816021
            },
            "worst": {
              "global_sensor_index": 70,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01613665744662285,
              "candidate": 0.024243289604783058,
              "position": [
                5.5,
                1.5,
                3.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.042584518989585,
            "cvrmse_percent": 112.1837214186418,
            "rms_normalized_rmse_percent": 24.22970586814253,
            "reference_energy": 8.10209661071351,
            "candidate_energy": 9.80698713783309,
            "relative_energy_error_percent": 21.04258451898958,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002215443059867539,
              "p95": 0.00029512900218833235,
              "p99": 0.0005023260600864887,
              "maximum": 0.00810663215816021
            },
            "worst": {
              "global_sensor_index": 70,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01613665744662285,
              "candidate": 0.024243289604783058,
              "position": [
                5.5,
                1.5,
                3.75
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
      "bias_percent": 0.13751916793333985,
      "rms_normalized_error_percent": 0.23360869594993994,
      "absolute_error": {
        "p95": 0.10940752973451842,
        "p99": 0.12553166104683172,
        "maximum": 0.14145369610220415
      },
      "worst_index": [
        54
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 12.029068361284198,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.23360869594993994
    },
    "overcast": {
      "bias_percent": 0.09351280512377821,
      "rms_normalized_error_percent": 0.20404062153822078,
      "absolute_error": {
        "p95": 0.06722326278686523,
        "p99": 0.08917659759521486,
        "maximum": 0.0912322998046875
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.68007230758667,
      "reference_fraction_of_uniform": 0.6384594440460205,
      "rms_normalized_to_uniform_percent": 0.143933024311311
    },
    "horizon": {
      "bias_percent": 0.9051864553370355,
      "rms_normalized_error_percent": 2.3176602243531974,
      "absolute_error": {
        "p95": 0.06240580772619885,
        "p99": 0.08921996372346135,
        "maximum": 0.09827149666865709
      },
      "worst_index": [
        60
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1224338629064592,
      "reference_fraction_of_uniform": 0.09331012420870725,
      "rms_normalized_to_uniform_percent": 0.13145546622264281
    },
    "north": {
      "bias_percent": -54.51291700002463,
      "rms_normalized_error_percent": 108.54508680418375,
      "absolute_error": {
        "p95": 9.817854597713454e-05,
        "p99": 0.00018298782544206942,
        "maximum": 0.00021388103778008372
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.8761309547699057e-05,
      "reference_fraction_of_uniform": 1.5596643834214774e-06,
      "rms_normalized_to_uniform_percent": 0.0002089244427238958
    },
    "east": {
      "bias_percent": 0.10167647939843581,
      "rms_normalized_error_percent": 0.30551000362385117,
      "absolute_error": {
        "p95": 0.02692044973373414,
        "p99": 0.03498011350631716,
        "maximum": 0.03729701042175293
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.451106548309326,
      "reference_fraction_of_uniform": 0.20376528799533844,
      "rms_normalized_to_uniform_percent": 0.06533878452577838
    },
    "south": {
      "bias_percent": 0.1794875365031029,
      "rms_normalized_error_percent": 0.28386692391558305,
      "absolute_error": {
        "p95": 0.08883192539215089,
        "p99": 0.10800607919692995,
        "maximum": 0.10949182510375977
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.306117057800293,
      "reference_fraction_of_uniform": 0.6905037760734558,
      "rms_normalized_to_uniform_percent": 0.18497636823062588
    },
    "west": {
      "bias_percent": 0.05019012616766453,
      "rms_normalized_error_percent": 0.33367064381791606,
      "absolute_error": {
        "p95": 0.028725853562355047,
        "p99": 0.0326141765713692,
        "maximum": 0.03575792908668518
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.368411064147949,
      "reference_fraction_of_uniform": 0.19689065217971802,
      "rms_normalized_to_uniform_percent": 0.06834254449264202
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
        "identifier": "stacked_rooms_0_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.01699775337900607,
          "cvrmse_percent": 1.6091226231299587,
          "absolute_error_percentiles_lux": {
            "p50": 2.4513778686523438,
            "p90": 23.95569152832032,
            "p95": 35.661505126953124,
            "p99": 67.11519042968742
          },
          "maximum_absolute_error_lux": 394.072265625,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 5148.72216796875,
            "radiance_lux": 5542.79443359375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.4467884322678846,
            "maximum_error_percentage_points": 2.4415068493150685,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1643046940714312,
            "maximum_error_percentage_points": 0.8190763228396776,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.10580289193302889,
            "maximum_error_percentage_points": 0.4883561643835641,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.10305936073059445,
            "maximum_error_percentage_points": 0.4371232876712412,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.027926179604261716,
            "maximum_error_percentage_points": 0.10890410958904084,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 58.333333333333336,
          "radiance_percent": 55.55555555555556,
          "difference_percentage_points": 2.7777777777777786,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 1,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.026728032449971566,
          "cvrmse_percent": 1.7265655927051335,
          "absolute_error_percentiles_lux": {
            "p50": 2.4715538024902344,
            "p90": 24.8955322265625,
            "p95": 37.835021972656236,
            "p99": 71.79252319335934
          },
          "maximum_absolute_error_lux": 404.9580078125,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              3.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 5181.8408203125,
            "radiance_lux": 5586.798828125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.33139269406392696,
            "maximum_error_percentage_points": 1.4482191780821907,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.15104170251052354,
            "maximum_error_percentage_points": 0.839617538060125,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.14272450532724504,
            "maximum_error_percentage_points": 0.685342465753422,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.14761035007610326,
            "maximum_error_percentage_points": 0.6895890410958856,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.031514459665144566,
            "maximum_error_percentage_points": 0.13890410958904198,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 55.55555555555556,
          "radiance_percent": 55.55555555555556,
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
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.004865689212323332,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "maximum_error_percentage_points": 0.004681078767120539,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
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
      "study_preparation_seconds": 0.007122249924577773,
      "weather_seconds": 0.08961399993859231,
      "metric_reduction_seconds": 0.060167500050738454,
      "write_seconds": 0.05366462504025549,
      "total_seconds": 0.20360070804599673,
      "cold_end_to_end_seconds": 0.2107229579705745,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.02085487497970462,
      "engine_upload_seconds": 0.000288833,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.03998366661835462,
      "engine_annual_reduction_seconds": 0.0006259999936446548,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.03998366661835462
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007122249924577773,
      "weather_seconds": 0.09340666595380753,
      "metric_reduction_seconds": 0.013814041973091662,
      "write_seconds": 0.048984791967086494,
      "total_seconds": 0.15638712502550334,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.15638712502550334,
      "raw_export_seconds": 0.02436799998395145,
      "engine_upload_seconds": 5.8542e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0011245000641793013,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.017421709024347365,
      "full": 0.04660604102537036
    }
  },
  "elapsed_seconds": 0.9083270831033587,
  "result_class": "passed"
}
```
