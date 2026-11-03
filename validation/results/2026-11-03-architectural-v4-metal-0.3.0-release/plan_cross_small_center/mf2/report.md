# Foton report

Status: **passed**

```json
{
  "scene": "plan_cross_small_center",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_cross_small_center",
    "category": "form",
    "question": "How does a small center opening illuminate a CROSS-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "cross",
    "window_profile": "small_center"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 44,
    "floor_area": 63.0,
    "aperture_area": 1.4399999999999993
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "02601626c0e1048ff4d6d5e2a9ecf97fb7094b44522fabb21250b32d25f81042",
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
      "scene_fingerprint": 15120444591077378995,
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 15120444591077378995,
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/foton-references-corpus4-2026-11-03",
    "model_sha256": "b82766544bb0e337d3253fb5ed2226c879aa46b4e15866f86c0485551a0db4be",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "9a3231f9777058abb1b3cf65cd66b5db7df4d557b41586683d412e16e4487cf8",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00011640600860118866,
          "p95": 0.0,
          "p99": 6.475020200014114e-07
        },
        "bias_percent": 0.009184016711547068,
        "identifier": "plan_cross_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.662698650730034,
        "worst_index": [
          21,
          515,
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
          "maximum": 0.00033049099147319794,
          "p95": 5.515399607247673e-06,
          "p99": 4.241749411448836e-05
        },
        "bias_percent": 0.14629164848709172,
        "identifier": "plan_cross_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.1179314015754924,
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
          "maximum": 0.00032817013561725616,
          "p95": 4.888612238573842e-06,
          "p99": 3.9249134715646505e-05
        },
        "bias_percent": 0.004075610432098675,
        "identifier": "plan_cross_small_center_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.8335199164094103,
        "worst_index": [
          20,
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
            "identifier": "plan_cross_small_center_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004188643943052739,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.096378249116242e-05
                },
                "candidate_energy": 2.447306981339352,
                "cvrmse_percent": 53.832376814830155,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.07907992245685135,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4453731821231486,
                "relative_energy_error_percent": 0.07907992245685136,
                "rms_normalized_rmse_percent": 5.674757633517232,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001139698753831908,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.0007208343595266342,
                  "rgb_channel": 0,
                  "sky_patch_index": 148
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005464629502967,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.9110078685334884e-06,
                  "p99": 0.00010350975207984447
                },
                "candidate_energy": 0.5882138595363671,
                "cvrmse_percent": 299.6747858091554,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.8468709410933675,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.5932378182305378,
                "relative_energy_error_percent": 0.8468709410933675,
                "rms_normalized_rmse_percent": 5.756693408363947,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00013659571413882077,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.00040986723615787923,
                  "rgb_channel": 0,
                  "sky_patch_index": 142
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.94479198660702,
            "full": 274.28158302791417
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 128.38504102546722,
            "full": 269.1511249868199
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.56337493937463,
            "full": 263.79050000105053
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.51604205649346,
            "full": 273.3597079059109
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 117.83129198011011,
            "full": 274.2776250233874
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.73949990514666,
            "full": 279.3982500443235
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.66141700558364,
            "full": 277.0572090521455
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.05537510290742,
            "full": 265.50666708499193
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
            "identifier": "plan_cross_small_center_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003123405622318387,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.7118403017520905e-05
                },
                "candidate_energy": 2.448250753721368,
                "cvrmse_percent": 39.709804048990755,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.08226043001383926,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4462384674388886,
                "relative_energy_error_percent": 0.08226043001383926,
                "rms_normalized_rmse_percent": 4.196682989851604,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003911082050763071,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.003598741488531232,
                  "rgb_channel": 0,
                  "sky_patch_index": 356
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000609204638749361,
                  "p50": 0.0,
                  "p90": 3.8818084249214735e-06,
                  "p95": 8.053747137637401e-06,
                  "p99": 8.366350084543228e-05
                },
                "candidate_energy": 1.1245707194018166,
                "cvrmse_percent": 138.76618086713214,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.3499596464445092,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1285200842988843,
                "relative_energy_error_percent": 0.3499596464445092,
                "rms_normalized_rmse_percent": 4.15458433539285,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.014489950146526098,
                  "global_sensor_index": 30,
                  "local_sensor_index": 30,
                  "reference": 0.01509915478527546,
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.51849996577948,
            "full": 3187.3328330693766
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.62225007265806,
            "full": 3298.146125045605
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 161.5478330058977,
            "full": 3161.995832924731
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 172.38237499259412,
            "full": 3173.3515000669286
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
            "identifier": "plan_cross_small_center_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00031735061202198267,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.016390398144722e-05
                },
                "candidate_energy": 2.446216702798665,
                "cvrmse_percent": 43.476908780291105,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.04466925099984424,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.445124484005646,
                "relative_energy_error_percent": 0.04466925099984424,
                "rms_normalized_rmse_percent": 4.589812942302675,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003947457065805793,
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "reference": 0.00363010645378381,
                  "rgb_channel": 0,
                  "sky_patch_index": 313
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005179428262636065,
                  "p50": 0.0,
                  "p90": 3.842214709948166e-06,
                  "p95": 7.868442139624676e-06,
                  "p99": 9.407268953509629e-05
                },
                "candidate_energy": 1.1313003139759132,
                "cvrmse_percent": 137.7876637873154,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.36062649498375,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1353948486227274,
                "relative_energy_error_percent": 0.36062649498375005,
                "rms_normalized_rmse_percent": 4.158616493726478,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0003193673910573125,
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "reference": -0.00019857543520629406,
                  "rgb_channel": 0,
                  "sky_patch_index": 361
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.42254198063165,
            "full": 3407.348125008866
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.25108399055898,
            "full": 3434.543374925852
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.29270898271352,
            "full": 3459.118584054522
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.3254580097273,
            "full": 3471.1179999867454
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
            "identifier": "plan_cross_small_center_grid",
            "sensor_count": 44,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00016849578241817653,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.4370459616184235e-05
                },
                "candidate_energy": 2.4458568406043923,
                "cvrmse_percent": 23.788244782641996,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.07916409664479931,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.4477946150991556,
                "relative_energy_error_percent": 0.07916409664479931,
                "rms_normalized_rmse_percent": 2.513616515929769,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0008305718365591019,
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "reference": 0.0009990676189772785,
                  "rgb_channel": 0,
                  "sky_patch_index": 157
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003398749977350235,
                  "p50": 0.0,
                  "p90": 2.6927451699521043e-06,
                  "p95": 5.590302635027911e-06,
                  "p99": 5.197850987315178e-05
                },
                "candidate_energy": 1.1342813963010023,
                "cvrmse_percent": 79.5474529977017,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.34379111266168233,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1303951980720761,
                "relative_energy_error_percent": 0.3437911126616824,
                "rms_normalized_rmse_percent": 2.3891945543952007,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0204694801941514,
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "reference": 0.020809355191886425,
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 229.89233396947384,
            "full": 6036.15337505471
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 225.87404202204198,
            "full": 6078.902791952714
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 231.40087502542883,
            "full": 6084.941250039265
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
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "44",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 232.43774997536093,
            "full": 6011.429582955316
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/plan_cross_small_center/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4091.0562919452786,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_cross_small_center/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 16307.396666961722,
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
      44,
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
        "identifier": "plan_cross_small_center_grid",
        "full_identifier": "plan_cross_small_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 44,
        "stages": {
          "direct": {
            "nmbe_percent": -0.019685668949432484,
            "cvrmse_percent": 3.4897927834179234,
            "rms_normalized_rmse_percent": 0.368649409475182,
            "reference_energy": 2.446227588038255,
            "candidate_energy": 2.445746031773524,
            "relative_energy_error_percent": 0.019685668949432484,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 7.504568202421069e-07,
              "maximum": 7.08320876583457e-05
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 265,
              "rgb_channel": 0,
              "reference": 0.0015869324561208487,
              "candidate": 0.001516100368462503,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.7337177350511197,
            "cvrmse_percent": 76.18267038557681,
            "rms_normalized_rmse_percent": 2.2924715502878175,
            "reference_energy": 1.1329364502669659,
            "candidate_energy": 1.1132945301018289,
            "relative_energy_error_percent": 1.7337177350511195,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.3679389161989093e-06,
              "p95": 6.518983354908414e-06,
              "p99": 2.171550295315683e-05,
              "maximum": 0.0006974907591938972
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014892800711095333,
              "candidate": 0.014195309951901436,
              "position": [
                5.5,
                3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5622395680807246,
            "cvrmse_percent": 24.046349827292186,
            "rms_normalized_rmse_percent": 2.2859829008637287,
            "reference_energy": 3.579164038305221,
            "candidate_energy": 3.559040561875353,
            "relative_energy_error_percent": 0.5622395680807246,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.3723145662634124e-06,
              "p95": 6.486088750534691e-06,
              "p99": 2.164277248084545e-05,
              "maximum": 0.0006974907591938972
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014892800711095333,
              "candidate": 0.014195309951901436,
              "position": [
                5.5,
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
      44,
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
        "identifier": "plan_cross_small_center_grid",
        "full_identifier": "plan_cross_small_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 44,
        "stages": {
          "direct": {
            "nmbe_percent": -0.019685668949432484,
            "cvrmse_percent": 3.4897927834179234,
            "rms_normalized_rmse_percent": 0.368649409475182,
            "reference_energy": 2.446227588038255,
            "candidate_energy": 2.445746031773524,
            "relative_energy_error_percent": 0.019685668949432484,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 7.504568202421069e-07,
              "maximum": 7.08320876583457e-05
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 265,
              "rgb_channel": 0,
              "reference": 0.0015869324561208487,
              "candidate": 0.001516100368462503,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 88.42625094411392,
            "cvrmse_percent": 1436.8314035340318,
            "rms_normalized_rmse_percent": 27.500178885483894,
            "reference_energy": 0.5908383383544713,
            "candidate_energy": 1.1132945301018289,
            "relative_energy_error_percent": 88.4262509441139,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.1610000001383014e-05,
              "p95": 2.4705484975129366e-05,
              "p99": 6.252061575651169e-05,
              "maximum": 0.006850233301520348
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017137886956334114,
              "candidate": 0.02398812025785446,
              "position": [
                6.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 17.186806218019832,
            "cvrmse_percent": 279.4977721792409,
            "rms_normalized_rmse_percent": 27.497525236905577,
            "reference_energy": 3.037065926392726,
            "candidate_energy": 3.559040561875353,
            "relative_energy_error_percent": 17.186806218019832,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.1566646890059928e-05,
              "p95": 2.4839999241521582e-05,
              "p99": 6.197999755386263e-05,
              "maximum": 0.006850233301520348
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017137886956334114,
              "candidate": 0.02398812025785446,
              "position": [
                6.5,
                1.5,
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
      "bias_percent": -0.03885981478201564,
      "rms_normalized_error_percent": 0.11006781481707098,
      "absolute_error": {
        "p95": 0.027538502488638983,
        "p99": 0.03139749098518475,
        "maximum": 0.033776166681192876
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.8157187022226196,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.11006781481707098
    },
    "overcast": {
      "bias_percent": -0.04604613659781023,
      "rms_normalized_error_percent": 0.08745054000890817,
      "absolute_error": {
        "p95": 0.01242005228996277,
        "p99": 0.02338763475418091,
        "maximum": 0.023716211318969727
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.562788248062134,
      "reference_fraction_of_uniform": 0.6716397404670715,
      "rms_normalized_to_uniform_percent": 0.06388005525851678
    },
    "horizon": {
      "bias_percent": 0.12421823367754493,
      "rms_normalized_error_percent": 1.677183512942761,
      "absolute_error": {
        "p95": 0.017782220177310053,
        "p99": 0.02007798031153794,
        "maximum": 0.020349389364984205
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.315929083341325,
      "reference_fraction_of_uniform": 0.08279674367958502,
      "rms_normalized_to_uniform_percent": 0.07134739043008563
    },
    "north": {
      "bias_percent": -98.67439981898112,
      "rms_normalized_error_percent": 100.02116740181005,
      "absolute_error": {
        "p95": 9.76071276454605e-05,
        "p99": 0.00033693222547299235,
        "maximum": 0.00046772867790423334
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.9253575374023058e-05,
      "reference_fraction_of_uniform": 5.04585841554217e-06,
      "rms_normalized_to_uniform_percent": 0.0006919929087571649
    },
    "east": {
      "bias_percent": -0.17549567682922626,
      "rms_normalized_error_percent": 0.2015075861570946,
      "absolute_error": {
        "p95": 0.012295009940862668,
        "p99": 0.01827983140945435,
        "maximum": 0.020974159240722656
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5553944110870361,
      "reference_fraction_of_uniform": 0.1455543339252472,
      "rms_normalized_to_uniform_percent": 0.0427022789644709
    },
    "south": {
      "bias_percent": -0.02638437210903255,
      "rms_normalized_error_percent": 0.14276176926646603,
      "absolute_error": {
        "p95": 0.021616896986961367,
        "p99": 0.024639892578125,
        "maximum": 0.025476455688476562
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.724637269973755,
      "reference_fraction_of_uniform": 0.714056134223938,
      "rms_normalized_to_uniform_percent": 0.09252916461169931
    },
    "west": {
      "bias_percent": 0.028834290442827787,
      "rms_normalized_error_percent": 0.11046438957071948,
      "absolute_error": {
        "p95": 0.005847887694835665,
        "p99": 0.007571172714233398,
        "maximum": 0.007913589477539062
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.563805341720581,
      "reference_fraction_of_uniform": 0.1477586179971695,
      "rms_normalized_to_uniform_percent": 0.023543240710383294
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
        "identifier": "plan_cross_small_center_grid",
        "sensor_count": 44,
        "illuminance": {
          "nmbe_percent": -0.08575983437012086,
          "cvrmse_percent": 2.8997777541881073,
          "absolute_error_percentiles_lux": {
            "p50": 0.572667121887207,
            "p90": 7.826360893249512,
            "p95": 13.924843406677235,
            "p99": 40.60962158203124
          },
          "maximum_absolute_error_lux": 252.375,
          "worst": {
            "sensor_index": 21,
            "position": [
              5.5,
              0.5,
              0.75
            ],
            "hour_of_year": 5243.5,
            "foton_lux": 37316.53125,
            "radiance_lux": 37568.90625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.06512764632627584,
            "maximum_error_percentage_points": 0.6889041095890391,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1616706944280743,
            "maximum_error_percentage_points": 0.6348033065739944,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.29170610211706144,
            "maximum_error_percentage_points": 2.0549315068493144,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.29449252801992554,
            "maximum_error_percentage_points": 2.0549315068493144,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0032814445828146426,
            "maximum_error_percentage_points": 0.051232876712333564,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 13.636363636363637,
          "radiance_percent": 13.636363636363637,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.272727272727273,
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
      "maximum_error_percentage_points": 0.004976723030821972,
      "metrics": {
        "da": [
          {
            "identifier": "plan_cross_small_center_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_cross_small_center_grid",
            "maximum_error_percentage_points": 0.004976723030821972,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_cross_small_center_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_cross_small_center_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_cross_small_center_grid",
            "maximum_error_percentage_points": 0.0035616438356171898,
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
      "study_preparation_seconds": 0.00655470893252641,
      "weather_seconds": 0.10064587509259582,
      "metric_reduction_seconds": 0.13078850007150322,
      "write_seconds": 0.0410880419658497,
      "total_seconds": 0.27267279103398323,
      "cold_end_to_end_seconds": 0.27922749996650964,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.029393292032182217,
      "engine_upload_seconds": 0.000861,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.07694358320441097,
      "engine_annual_reduction_seconds": 0.0018292083404958248,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.07694358320441097
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.00655470893252641,
      "weather_seconds": 0.09820854105055332,
      "metric_reduction_seconds": 0.04408729204442352,
      "write_seconds": 0.051357457996346056,
      "total_seconds": 0.19411791604943573,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.19411791604943573,
      "raw_export_seconds": 0.012414042023010552,
      "engine_upload_seconds": 7.1416e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.001965458272024989,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01771404210012406,
      "full": 0.0841302500339225
    }
  },
  "elapsed_seconds": 1.3200589590705931,
  "result_class": "passed"
}
```
