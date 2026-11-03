# Foton report

Status: **passed**

```json
{
  "scene": "balcony_above",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "balcony_above",
    "category": "shading",
    "question": "How does an upper balcony slab shade a full-width facade?",
    "interactions": [
      "balcony",
      "overhang",
      "context_occlusion"
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
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "8139c7e916a82e23b5c8f056c80b99bc2f480d5bd47f7d292adb3b07c80843ee",
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
      "scene_fingerprint": 9723977500591765372,
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
      "scene_fingerprint": 9723977500591765372,
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
    "model_sha256": "f86339d7b5aabcd354a29792e78084a9654ae1dc1ac7a6382fc4f2d8bfa4ff93",
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
          "maximum": 0.0003998326137661934,
          "p95": 1.2582822819240165e-06,
          "p99": 8.885929128155112e-05
        },
        "bias_percent": -0.04592571391656873,
        "identifier": "balcony_above_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.659658509445179,
        "worst_index": [
          23,
          76,
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
          "maximum": 0.00041427090764045715,
          "p95": 3.469635848887253e-05,
          "p99": 0.00013695773668587208
        },
        "bias_percent": 0.06370847496271467,
        "identifier": "balcony_above_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9253767131491892,
        "worst_index": [
          20,
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
          "maximum": 0.00037201307713985443,
          "p95": 2.6772985438583392e-05,
          "p99": 0.00010574329644441605
        },
        "bias_percent": -0.0026007974376117053,
        "identifier": "balcony_above_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7669051420293354,
        "worst_index": [
          34,
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
            "identifier": "balcony_above_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00047114037442952394,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.558027430903167e-05,
                  "p99": 0.00021806755103170872
                },
                "candidate_energy": 3.4097550653968938,
                "cvrmse_percent": 18.40011880475448,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.15357042055478906,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.404526719396017,
                "relative_energy_error_percent": 0.15357042055478906,
                "rms_normalized_rmse_percent": 3.460192905745178,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004234763793647289,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.0037636234192177653,
                  "rgb_channel": 0,
                  "sky_patch_index": 46
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008359435014426708,
                  "p50": 0.0,
                  "p90": 1.1197510048077675e-05,
                  "p95": 8.982565195765323e-05,
                  "p99": 0.0003477690042927861
                },
                "candidate_energy": 2.4322752086912374,
                "cvrmse_percent": 39.60880842875824,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.33703629758531145,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4405005814936516,
                "relative_energy_error_percent": 0.33703629758531145,
                "rms_normalized_rmse_percent": 2.7213855927420325,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0005628683138638735,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": -0.00027307518757879734,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 100.53537494968623,
            "full": 247.6707500172779
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 113.7385000474751,
            "full": 230.28970800805837
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 101.58220899756998,
            "full": 231.11004196107388
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 108.45320799853653,
            "full": 238.36812493391335
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
            "identifier": "balcony_above_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003875924739986658,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2937735775485627e-05,
                  "p99": 0.00016251509077847004
                },
                "candidate_energy": 3.4035725123248994,
                "cvrmse_percent": 13.724431038493686,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.13994546336674493,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.4083423327956552,
                "relative_energy_error_percent": 0.13994546336674493,
                "rms_normalized_rmse_percent": 2.5879928330372115,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007621638476848602,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.0072340460028499365,
                  "rgb_channel": 0,
                  "sky_patch_index": 44
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006846096366643906,
                  "p50": 0.0,
                  "p90": 2.161235170206055e-05,
                  "p95": 6.041641390766016e-05,
                  "p99": 0.0002551199868321419
                },
                "candidate_energy": 3.928988757572185,
                "cvrmse_percent": 19.59861914083398,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1962218849720825,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.921294319942291,
                "relative_energy_error_percent": 0.19622188497208254,
                "rms_normalized_rmse_percent": 1.738638779053505,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03441830538213253,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.03510291501879692,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.08699997328222,
            "full": 2336.984209017828
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.84758406411856,
            "full": 2352.117917034775
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 131.2162090325728,
            "full": 2313.9098749961704
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.59874999616295,
            "full": 2331.404374912381
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
            "identifier": "balcony_above_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00036772561725229025,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.315930032636969e-05,
                  "p99": 0.00013912096619606018
                },
                "candidate_energy": 3.3993334656843217,
                "cvrmse_percent": 11.839152281600224,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0203293971969583,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.3986425421426247,
                "relative_energy_error_percent": 0.0203293971969583,
                "rms_normalized_rmse_percent": 2.227866264135376,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0028512830613180995,
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "reference": 0.0024835574440658092,
                  "rgb_channel": 0,
                  "sky_patch_index": 44
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008401442319154739,
                  "p50": 0.0,
                  "p90": 2.290974953211844e-05,
                  "p95": 6.0582740115933096e-05,
                  "p99": 0.00025806238409131765
                },
                "candidate_energy": 3.937420432814722,
                "cvrmse_percent": 19.578621365929898,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.032465965208886303,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.9361425261516096,
                "relative_energy_error_percent": 0.032465965208886303,
                "rms_normalized_rmse_percent": 1.7445574735668186,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.044595690444111824,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.0454358346760273,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.08062502276152,
            "full": 2547.6110419258475
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.29875004012138,
            "full": 2455.361041938886
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.30937493871897,
            "full": 2466.7072909651324
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.24245798867196,
            "full": 2442.5948340212926
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
            "identifier": "balcony_above_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001623840071260929,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.5186516975517628e-05,
                  "p99": 9.26030334085226e-05
                },
                "candidate_energy": 3.4006256708016736,
                "cvrmse_percent": 7.374918427877103,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.10152530881939133,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.40408167523492,
                "relative_energy_error_percent": 0.10152530881939133,
                "rms_normalized_rmse_percent": 1.3876934608467626,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007500414503738284,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.007662798510864377,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005003400146961212,
                  "p50": 0.0,
                  "p90": 1.4959296095184982e-05,
                  "p95": 3.9017884409986336e-05,
                  "p99": 0.0001465866807848215
                },
                "candidate_energy": 3.9312652668305255,
                "cvrmse_percent": 12.056436101897553,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.09959847056568936,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.9351846505564154,
                "relative_energy_error_percent": 0.09959847056568938,
                "rms_normalized_rmse_percent": 1.072428757652629,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.021507300436496735,
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "reference": 0.022007640451192856,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 185.502375010401,
            "full": 4354.053542017937
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 193.62879206892103,
            "full": 4408.915417036042
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 194.22962504904717,
            "full": 4320.818374981172
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 194.09366697072983,
            "full": 4264.874542015605
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/balcony_above/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 792.6151249557734,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/balcony_above/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2597.1611669519916,
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
        "identifier": "balcony_above_grid",
        "full_identifier": "balcony_above_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.019684413924885496,
            "cvrmse_percent": 5.718216399757019,
            "rms_normalized_rmse_percent": 1.076029810475828,
            "reference_energy": 3.4009350730520964,
            "candidate_energy": 3.4016045271891926,
            "relative_energy_error_percent": 0.019684413924885492,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 7.388996891677323e-07,
              "p99": 5.1843468099832535e-05,
              "maximum": 0.00041109882295131683
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 76,
              "rgb_channel": 0,
              "reference": 0.008998706936836243,
              "candidate": 0.00940980575978756,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.1291105099468266,
            "cvrmse_percent": 24.083023309782856,
            "rms_normalized_rmse_percent": 2.142607320512336,
            "reference_energy": 3.9346435907514934,
            "candidate_energy": 3.890217116439369,
            "relative_energy_error_percent": 1.1291105099468266,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.4999996739438757e-08,
              "p90": 2.9605304007418454e-05,
              "p95": 5.0805584760382734e-05,
              "p99": 0.000130354892462492,
              "maximum": 0.0012821014970541
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.027245551347732544,
              "candidate": 0.025963449850678444,
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
            "nmbe_percent": -0.5965040003039047,
            "cvrmse_percent": 12.813686656526787,
            "rms_normalized_rmse_percent": 2.125370545507787,
            "reference_energy": 7.33557866380359,
            "candidate_energy": 7.291821643628562,
            "relative_energy_error_percent": 0.5965040003039047,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.4999996739438757e-08,
              "p90": 2.9353424906730652e-05,
              "p95": 4.8220749886240745e-05,
              "p99": 0.00011403602547943592,
              "maximum": 0.0012821014970541
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.027245551347732544,
              "candidate": 0.025963449850678444,
              "position": [
                3.5,
                3.5,
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
        "identifier": "balcony_above_grid",
        "full_identifier": "balcony_above_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.019684413924885496,
            "cvrmse_percent": 5.718216399757019,
            "rms_normalized_rmse_percent": 1.076029810475828,
            "reference_energy": 3.4009350730520964,
            "candidate_energy": 3.4016045271891926,
            "relative_energy_error_percent": 0.019684413924885492,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 7.388996891677323e-07,
              "p99": 5.1843468099832535e-05,
              "maximum": 0.00041109882295131683
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 76,
              "rgb_channel": 0,
              "reference": 0.008998706936836243,
              "candidate": 0.00940980575978756,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 59.265827860439295,
            "cvrmse_percent": 404.7664355825673,
            "rms_normalized_rmse_percent": 27.853835733416272,
            "reference_energy": 2.4425937244041265,
            "candidate_energy": 3.890217116439369,
            "relative_energy_error_percent": 59.26582786043929,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00018026000179816037,
              "p95": 0.0002585718986665597,
              "p99": 0.0005423133843578398,
              "maximum": 0.008816776797175407
            },
            "worst": {
              "global_sensor_index": 29,
              "local_sensor_index": 29,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02524770237505436,
              "candidate": 0.03406447917222977,
              "position": [
                4.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 24.784559063057976,
            "cvrmse_percent": 169.18375780692364,
            "rms_normalized_rmse_percent": 27.852432882562688,
            "reference_energy": 5.843528797456223,
            "candidate_energy": 7.291821643628562,
            "relative_energy_error_percent": 24.78455906305797,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00018023999291472137,
              "p95": 0.0002563407360867131,
              "p99": 0.0005476316437125206,
              "maximum": 0.008816776797175407
            },
            "worst": {
              "global_sensor_index": 29,
              "local_sensor_index": 29,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02524770237505436,
              "candidate": 0.03406447917222977,
              "position": [
                4.5,
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
      "bias_percent": 0.2682309468463395,
      "rms_normalized_error_percent": 0.3627458826634988,
      "absolute_error": {
        "p95": 0.07474320947004609,
        "p99": 0.107461138461537,
        "maximum": 0.1182457687098526
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.113102602988631,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.3627458826634988
    },
    "overcast": {
      "bias_percent": 0.2139036771235435,
      "rms_normalized_error_percent": 0.299784850162822,
      "absolute_error": {
        "p95": 0.03648287057876587,
        "p99": 0.046690720319747914,
        "maximum": 0.04873478412628174
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.8683788776397705,
      "reference_fraction_of_uniform": 0.5438385009765625,
      "rms_normalized_to_uniform_percent": 0.17618436627024062
    },
    "horizon": {
      "bias_percent": 1.238253894246722,
      "rms_normalized_error_percent": 2.406907186877097,
      "absolute_error": {
        "p95": 0.06027265818809199,
        "p99": 0.08377563847785494,
        "maximum": 0.09252575928260365
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1272437054580788,
      "reference_fraction_of_uniform": 0.15847426480034996,
      "rms_normalized_to_uniform_percent": 0.2709167696292988
    },
    "north": {
      "bias_percent": -5.657121985972092,
      "rms_normalized_error_percent": 61.82573559245109,
      "absolute_error": {
        "p95": 0.0004401525045523158,
        "p99": 0.0006146549945697186,
        "maximum": 0.0006687317509204149
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 0.00012096410500817001,
      "reference_fraction_of_uniform": 1.7005815607262775e-05,
      "rms_normalized_to_uniform_percent": 0.0016724136745053877
    },
    "east": {
      "bias_percent": 0.06292171474489196,
      "rms_normalized_error_percent": 0.5797176560846526,
      "absolute_error": {
        "p95": 0.03031700849533081,
        "p99": 0.0369848608970642,
        "maximum": 0.039466142654418945
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.4902143478393555,
      "reference_fraction_of_uniform": 0.20950272679328918,
      "rms_normalized_to_uniform_percent": 0.13013624778426586
    },
    "south": {
      "bias_percent": 0.3145066145465243,
      "rms_normalized_error_percent": 0.42395712902348587,
      "absolute_error": {
        "p95": 0.07129526138305664,
        "p99": 0.10631089210510249,
        "maximum": 0.11912727355957031
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.578793048858643,
      "reference_fraction_of_uniform": 0.7842981219291687,
      "rms_normalized_to_uniform_percent": 0.3290161754460578
    },
    "west": {
      "bias_percent": 0.22364722591277583,
      "rms_normalized_error_percent": 0.5447748154772786,
      "absolute_error": {
        "p95": 0.023561209440231323,
        "p99": 0.028361496329307546,
        "maximum": 0.030540764331817627
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.4608830213546753,
      "reference_fraction_of_uniform": 0.2053791582584381,
      "rms_normalized_to_uniform_percent": 0.12140994120629733
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
        "identifier": "balcony_above_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.05420398613579096,
          "cvrmse_percent": 2.0535963261274675,
          "absolute_error_percentiles_lux": {
            "p50": 1.7356414794921875,
            "p90": 15.176339721679692,
            "p95": 24.508416748046848,
            "p99": 51.188874511718744
          },
          "maximum_absolute_error_lux": 239.427734375,
          "worst": {
            "sensor_index": 23,
            "position": [
              3.5,
              0.5,
              0.75
            ],
            "hour_of_year": 6086.5,
            "foton_lux": 17150.095703125,
            "radiance_lux": 16910.66796875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.5111149162861488,
            "maximum_error_percentage_points": 1.39958904109589,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.20039178736963828,
            "maximum_error_percentage_points": 0.7987559071740264,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.13850456621004564,
            "maximum_error_percentage_points": 0.6309589041095904,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.14666286149162844,
            "maximum_error_percentage_points": 0.6349315068493127,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.030410958904109733,
            "maximum_error_percentage_points": 0.13493150684931976,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 36.111111111111114,
          "radiance_percent": 36.111111111111114,
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
            "identifier": "balcony_above_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "balcony_above_grid",
            "maximum_error_percentage_points": 0.004852044092459096,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "balcony_above_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "balcony_above_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "balcony_above_grid",
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
      "study_preparation_seconds": 0.006832374958321452,
      "weather_seconds": 0.09492079203482717,
      "metric_reduction_seconds": 0.03878704202361405,
      "write_seconds": 0.03598575002979487,
      "total_seconds": 0.16984745801892132,
      "cold_end_to_end_seconds": 0.17667983297724277,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.008582958951592445,
      "engine_upload_seconds": 0.000267291,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.01935787487309426,
      "engine_annual_reduction_seconds": 0.000360458274371922,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.01935787487309426
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006832374958321452,
      "weather_seconds": 0.09688199998345226,
      "metric_reduction_seconds": 0.01249804103281349,
      "write_seconds": 0.019830625038594007,
      "total_seconds": 0.12936591601464897,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.12936591601464897,
      "raw_export_seconds": 0.010657541919499636,
      "engine_upload_seconds": 6.1959e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0003433750243857503,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01828166702762246,
      "full": 0.024173542042262852
    }
  },
  "elapsed_seconds": 0.7450470419134945,
  "result_class": "passed"
}
```
