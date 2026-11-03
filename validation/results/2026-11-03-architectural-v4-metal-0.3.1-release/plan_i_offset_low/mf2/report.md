# Foton report

Status: **passed**

```json
{
  "scene": "plan_i_offset_low",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_i_offset_low",
    "category": "form",
    "question": "How does a offset low opening illuminate a I-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "i",
    "window_profile": "offset_low"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 74,
    "floor_area": 90.0,
    "aperture_area": 1.4399999999999997
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "8b2f8b048fb9147b797fee76bb0ef92a174a2802c41fbd6a40433c1e3d613717",
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
      "scene_fingerprint": 8364362664664098958,
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
      "scene_fingerprint": 8364362664664098958,
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
    "model_sha256": "9778f08e7e3143835cb1853ce8405829109e98b622205ab00a1b5309f2b50973",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "274288e18ebb896ca8da417745929f291321088f610eaef564604626c7d101ce",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0001382098998874426,
          "p95": 0.0,
          "p99": 0.0
        },
        "bias_percent": 0.036050030505363824,
        "identifier": "plan_i_offset_low_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0091113081369516,
        "worst_index": [
          9,
          321,
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
          "maximum": 0.00045733340084552765,
          "p95": 2.5664523946034024e-06,
          "p99": 9.663728587838823e-06
        },
        "bias_percent": 0.17433326676828545,
        "identifier": "plan_i_offset_low_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.1293885875285046,
        "worst_index": [
          4,
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
          "maximum": 0.00022450380492955446,
          "p95": 2.2131853256723844e-06,
          "p99": 8.870681631379005e-06
        },
        "bias_percent": -0.04178376095462693,
        "identifier": "plan_i_offset_low_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.4718227053406143,
        "worst_index": [
          4,
          91,
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
            "identifier": "plan_i_offset_low_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006473474786616862,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 1.35469017294281,
                "cvrmse_percent": 177.28819390826953,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.12982519494924555,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3529337240979658,
                "relative_energy_error_percent": 0.12982519494924552,
                "rms_normalized_rmse_percent": 11.50687082885798,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0016648565069772303,
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "reference": 0.0010175090283155441,
                  "rgb_channel": 0,
                  "sky_patch_index": 155
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007857604650780559,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.570011325697335e-06
                },
                "candidate_energy": 0.41258692592619894,
                "cvrmse_percent": 671.3761945640929,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.9221769689385141,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.4088169105321455,
                "relative_energy_error_percent": 0.9221769689385141,
                "rms_normalized_rmse_percent": 8.420465636645668,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0003219490172341466,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": -0.00046381144784390926,
                  "rgb_channel": 0,
                  "sky_patch_index": 214
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.87258298322558,
            "full": 404.0173749672249
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.28770890180022,
            "full": 414.05879193916917
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.77541701309383,
            "full": 389.3981659784913
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.6137090465054,
            "full": 384.6852920250967
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
            "identifier": "plan_i_offset_low_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00028745122835971415,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 1.3522678695790091,
                "cvrmse_percent": 75.7306196396612,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.18714885283550398,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3548033685414111,
                "relative_energy_error_percent": 0.187148852835504,
                "rms_normalized_rmse_percent": 4.932918120048695,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0007437878812197596,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.0010312391095794737,
                  "rgb_channel": 0,
                  "sky_patch_index": 100
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005575697869062424,
                  "p50": 0.0,
                  "p90": 1.543903731970886e-06,
                  "p95": 3.5364946597837843e-06,
                  "p99": 1.4798266101934199e-05
                },
                "candidate_energy": 0.914789341820768,
                "cvrmse_percent": 165.44659868865608,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.3240960364147274,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9118341235676084,
                "relative_energy_error_percent": 0.32409603641472734,
                "rms_normalized_rmse_percent": 3.5421892746188686,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.022041140124201775,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.022598709911108017,
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 204.1597500210628,
            "full": 5302.3480830015615
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 194.18891705572605,
            "full": 5252.837916952558
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 201.3025829801336,
            "full": 5337.367749889381
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 202.69445795565844,
            "full": 5284.944209037349
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
            "identifier": "plan_i_offset_low_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003555745352059603,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 1.3514027170203917,
                "cvrmse_percent": 68.96678554918155,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.015651865629597885,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3516142698697422,
                "relative_energy_error_percent": 0.015651865629597885,
                "rms_normalized_rmse_percent": 4.480522141905503,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004096961580216885,
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "reference": 0.0037413870450109243,
                  "rgb_channel": 0,
                  "sky_patch_index": 361
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006828149780631065,
                  "p50": 0.0,
                  "p90": 1.5563830508824594e-06,
                  "p95": 3.617955030676967e-06,
                  "p99": 1.3917306091571037e-05
                },
                "candidate_energy": 0.9165037709045762,
                "cvrmse_percent": 173.0724380689794,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.604497726664315,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9220777096977777,
                "relative_energy_error_percent": 0.6044977266643151,
                "rms_normalized_rmse_percent": 3.735420860810672,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02259121462702751,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.021908399648964405,
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 193.80395801272243,
            "full": 5673.837708076462
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 208.82625004742295,
            "full": 5695.289541967213
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 198.67595797404647,
            "full": 5617.980582988821
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 199.91329091135412,
            "full": 5683.522457955405
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
            "identifier": "plan_i_offset_low_grid",
            "sensor_count": 74,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00018504547188058496,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 1.3537932410681606,
                "cvrmse_percent": 44.66934635086633,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.10712268606534604,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3523445732364507,
                "relative_energy_error_percent": 0.10712268606534603,
                "rms_normalized_rmse_percent": 2.904561613657837,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0016655760118737817,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.0014805305399931967,
                  "rgb_channel": 0,
                  "sky_patch_index": 213
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00035086460411548615,
                  "p50": 0.0,
                  "p90": 1.1410306228754052e-06,
                  "p95": 2.5530828224873403e-06,
                  "p99": 1.0225149208054127e-05
                },
                "candidate_energy": 0.9181130919462106,
                "cvrmse_percent": 101.73356525008057,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.2909181259027739,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9154498823050297,
                "relative_energy_error_percent": 0.2909181259027739,
                "rms_normalized_rmse_percent": 2.1907946087769115,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03161734528839588,
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "reference": 0.031266480684280396,
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 299.12029195111245,
            "full": 10126.071250066161
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 304.31754095479846,
            "full": 10104.177083005197
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 304.05695899389684,
            "full": 10094.797583064064
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
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "74",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 298.82283392362297,
            "full": 10249.105458031408
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/suite-0.3.1/run/plan_i_offset_low/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10885.747916996479,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_i_offset_low/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 45322.779209003784,
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
      74,
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
        "identifier": "plan_i_offset_low_grid",
        "full_identifier": "plan_i_offset_low_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": 0.007558399884142822,
            "cvrmse_percent": 7.022571447884038,
            "rms_normalized_rmse_percent": 0.4568776304366784,
            "reference_energy": 1.352405252281045,
            "candidate_energy": 1.3525074724780666,
            "relative_energy_error_percent": 0.007558399884142822,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 5.3326133638620377e-05
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 414,
              "rgb_channel": 0,
              "reference": 0.001403772970661521,
              "candidate": 0.0014570991043001413,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.6679132285018807,
            "cvrmse_percent": 87.72029632384557,
            "rms_normalized_rmse_percent": 1.8896177404038885,
            "reference_energy": 0.9174451446217944,
            "candidate_energy": 0.9021429556903993,
            "relative_energy_error_percent": 1.667913228501881,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.5262885426636785e-06,
              "p95": 3.2680964068276808e-06,
              "p99": 1.074651736416858e-05,
              "maximum": 0.0006737522780895233
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.031441912055015564,
              "candidate": 0.03076815977692604,
              "position": [
                0.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.6696462795571722,
            "cvrmse_percent": 35.38555220110562,
            "rms_normalized_rmse_percent": 1.8858926699511283,
            "reference_energy": 2.2698503969028394,
            "candidate_energy": 2.254650428168466,
            "relative_energy_error_percent": 0.6696462795571722,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.5262885426636785e-06,
              "p95": 3.2688067221897654e-06,
              "p99": 1.072336053766782e-05,
              "maximum": 0.0006737522780895233
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.031441912055015564,
              "candidate": 0.03076815977692604,
              "position": [
                0.5,
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
      74,
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
        "identifier": "plan_i_offset_low_grid",
        "full_identifier": "plan_i_offset_low_grid",
        "start_sensor_index": 0,
        "sensor_count": 74,
        "stages": {
          "direct": {
            "nmbe_percent": 0.007558399884142822,
            "cvrmse_percent": 7.022571447884038,
            "rms_normalized_rmse_percent": 0.4568776304366784,
            "reference_energy": 1.352405252281045,
            "candidate_energy": 1.3525074724780666,
            "relative_energy_error_percent": 0.007558399884142822,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 5.3326133638620377e-05
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 414,
              "rgb_channel": 0,
              "reference": 0.001403772970661521,
              "candidate": 0.0014570991043001413,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 118.9090259412337,
            "cvrmse_percent": 2936.6040203850343,
            "rms_normalized_rmse_percent": 36.98255711278318,
            "reference_energy": 0.41210861535356713,
            "candidate_energy": 0.9021429556903993,
            "relative_energy_error_percent": 118.9090259412337,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.9900000956549775e-06,
              "p95": 1.1520000043674372e-05,
              "p99": 4.642185012926459e-05,
              "maximum": 0.007568352855741978
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014195657335221767,
              "candidate": 0.021764010190963745,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 27.777427512706236,
            "cvrmse_percent": 685.8160796502384,
            "rms_normalized_rmse_percent": 36.98048418565789,
            "reference_energy": 1.7645138676346122,
            "candidate_energy": 2.254650428168466,
            "relative_energy_error_percent": 27.777427512706236,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.980000201408984e-06,
              "p95": 1.1520000043674372e-05,
              "p99": 4.6465978084597895e-05,
              "maximum": 0.007568352855741978
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014195657335221767,
              "candidate": 0.021764010190963745,
              "position": [
                1.5,
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
      "bias_percent": -0.2591775033551765,
      "rms_normalized_error_percent": 0.17910495319587977,
      "absolute_error": {
        "p95": 0.01779521743710948,
        "p99": 0.03672141292727066,
        "maximum": 0.07788026866166575
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3221918069638052,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.17910495319587977
    },
    "overcast": {
      "bias_percent": -0.22340527642721367,
      "rms_normalized_error_percent": 0.16058443167325515,
      "absolute_error": {
        "p95": 0.011496410518884653,
        "p99": 0.021552759408950677,
        "maximum": 0.045413970947265625
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.8225340247154236,
      "reference_fraction_of_uniform": 0.6220988631248474,
      "rms_normalized_to_uniform_percent": 0.10471289344707085
    },
    "horizon": {
      "bias_percent": -0.5547445061781167,
      "rms_normalized_error_percent": 0.7923099144089222,
      "absolute_error": {
        "p95": 0.006008743369531766,
        "p99": 0.01802700600429049,
        "maximum": 0.022370641827706983
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.15935870306715566,
      "reference_fraction_of_uniform": 0.12052616135407507,
      "rms_normalized_to_uniform_percent": 0.06598860438409138
    },
    "north": {
      "bias_percent": -98.11447414835759,
      "rms_normalized_error_percent": 99.99686065883674,
      "absolute_error": {
        "p95": 9.406775013189863e-05,
        "p99": 0.00026534174467087693,
        "maximum": 0.0003255380433984101
      },
      "worst_index": [
        0
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.604579847480636e-05,
      "reference_fraction_of_uniform": 1.2135757060605101e-05,
      "rms_normalized_to_uniform_percent": 0.0008859995675515723
    },
    "east": {
      "bias_percent": -0.5104725607399228,
      "rms_normalized_error_percent": 0.2862063730745718,
      "absolute_error": {
        "p95": 0.006498319655656811,
        "p99": 0.015499410927295636,
        "maximum": 0.024453163146972656
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.20204758644104004,
      "reference_fraction_of_uniform": 0.15281261503696442,
      "rms_normalized_to_uniform_percent": 0.06045710260892218
    },
    "south": {
      "bias_percent": -0.26496673357128664,
      "rms_normalized_error_percent": 0.1725758105091833,
      "absolute_error": {
        "p95": 0.0120750069618225,
        "p99": 0.026629111468791815,
        "maximum": 0.053516387939453125
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.9658470153808594,
      "reference_fraction_of_uniform": 0.7304893136024475,
      "rms_normalized_to_uniform_percent": 0.12657851660329855
    },
    "west": {
      "bias_percent": -0.1213524369318667,
      "rms_normalized_error_percent": 0.23022322472091705,
      "absolute_error": {
        "p95": 0.007124041393399238,
        "p99": 0.011677998304367037,
        "maximum": 0.01692938804626465
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3052036762237549,
      "reference_fraction_of_uniform": 0.23083160817623138,
      "rms_normalized_to_uniform_percent": 0.05145697615219209
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
        "identifier": "plan_i_offset_low_grid",
        "sensor_count": 74,
        "illuminance": {
          "nmbe_percent": -0.25864919581270795,
          "cvrmse_percent": 5.581495710952783,
          "absolute_error_percentiles_lux": {
            "p50": 0.11254430189728737,
            "p90": 3.7374902725219754,
            "p95": 7.5515114784240716,
            "p99": 23.707694702148427
          },
          "maximum_absolute_error_lux": 285.048828125,
          "worst": {
            "sensor_index": 9,
            "position": [
              1.5,
              0.5,
              0.75
            ],
            "hour_of_year": 3085.5,
            "foton_lux": 21097.447265625,
            "radiance_lux": 20812.3984375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.04586449463161806,
            "maximum_error_percentage_points": 1.1473972602739728,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.12750016985431378,
            "maximum_error_percentage_points": 0.8874321916822154,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.09526471677156623,
            "maximum_error_percentage_points": 1.3673972602739752,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.09951499444650133,
            "maximum_error_percentage_points": 1.3673972602739717,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.004424287300999599,
            "maximum_error_percentage_points": 0.14095890410958845,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 5.405405405405405,
          "radiance_percent": 5.405405405405405,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.0,
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
      "maximum_error_percentage_points": 0.004929901541103732,
      "metrics": {
        "da": [
          {
            "identifier": "plan_i_offset_low_grid",
            "maximum_error_percentage_points": 0.004383561643835632,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_i_offset_low_grid",
            "maximum_error_percentage_points": 0.004929901541103732,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_i_offset_low_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_i_offset_low_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_i_offset_low_grid",
            "maximum_error_percentage_points": 0.00438356164384146,
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
      "study_preparation_seconds": 0.00664408307056874,
      "weather_seconds": 0.09875975002069026,
      "metric_reduction_seconds": 0.1771946670487523,
      "write_seconds": 0.02770762494765222,
      "total_seconds": 0.3037982910173014,
      "cold_end_to_end_seconds": 0.3104423740878701,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.012614708044566214,
      "engine_upload_seconds": 0.000974625,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.11981962516438216,
      "engine_annual_reduction_seconds": 0.003078916692174971,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.11981962516438216
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.00664408307056874,
      "weather_seconds": 0.10025254194624722,
      "metric_reduction_seconds": 0.04973929200787097,
      "write_seconds": 0.03683879098389298,
      "total_seconds": 0.18718441692180932,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.18718441692180932,
      "raw_export_seconds": 0.015016249963082373,
      "engine_upload_seconds": 9.6875e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.003215000033378601,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.012519125011749566,
      "full": 0.12298474996350706
    }
  },
  "elapsed_seconds": 1.695189250051044,
  "result_class": "passed"
}
```
