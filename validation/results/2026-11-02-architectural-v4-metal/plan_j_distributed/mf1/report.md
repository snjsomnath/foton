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
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "f495b13ca441337bb01f4a62467cfe31d565c423a2001c720caed91399a9f987",
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 12112216450189513340,
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
    "maximum_samples": 16384,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "plan_j_distributed_grid",
        "bias_percent": 0.0496755077453874,
        "rms_normalized_error_percent": 1.7073718912538698,
        "absolute_error": {
          "p95": 3.8819824112579226e-05,
          "p99": 0.00016517454059794545,
          "maximum": 0.0006667673587799072
        },
        "worst_index": [
          10,
          129,
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
        "bias_percent": 0.07104508298600803,
        "rms_normalized_error_percent": 1.0609912473942162,
        "absolute_error": {
          "p95": 7.291813381016254e-05,
          "p99": 0.00016387179493904114,
          "maximum": 0.0007935352623462677
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
        "bias_percent": -0.0008864128290098104,
        "rms_normalized_error_percent": 0.9000595270528696,
        "absolute_error": {
          "p95": 5.8741308748722076e-05,
          "p99": 0.0001369025558233261,
          "maximum": 0.0007006525993347168
        },
        "worst_index": [
          6,
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_j_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 47,
            "stages": {
              "direct": {
                "nmbe_percent": -0.10171819590956035,
                "cvrmse_percent": 10.688623563621755,
                "rms_normalized_rmse_percent": 2.7349764209110003,
                "reference_energy": 11.698518374523886,
                "candidate_energy": 11.686618852685172,
                "relative_energy_error_percent": 0.10171819590956035,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.681700374931097e-05,
                  "p95": 0.00013522955123335123,
                  "p99": 0.0003088309895247221,
                  "maximum": 0.0006548305973410606
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 110,
                  "rgb_channel": 0,
                  "reference": 0.01750189997255802,
                  "candidate": 0.018156730569899082
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.0998298023789353,
                "cvrmse_percent": 54.39821170470053,
                "rms_normalized_rmse_percent": 3.3062270000404212,
                "reference_energy": 3.717274574354306,
                "candidate_energy": 3.7135636264928458,
                "relative_energy_error_percent": 0.0998298023789353,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.9611832868804413e-07,
                  "p90": 0.00010368903167545795,
                  "p95": 0.00021891016513109207,
                  "p99": 0.0004600069369189441,
                  "maximum": 0.0010893414728343487
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 60,
                  "rgb_channel": 0,
                  "reference": 0.0005845844279974699,
                  "candidate": -0.0005047570448368788
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 132.39554094616324,
            "full": 301.0024590184912
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 136.7498750332743,
            "full": 318.40233295224607
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 133.88116704300046,
            "full": 299.5097499806434
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 131.12320797517896,
            "full": 289.0780840534717
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_j_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 47,
            "stages": {
              "direct": {
                "nmbe_percent": -0.02422317126094042,
                "cvrmse_percent": 7.134232236294882,
                "rms_normalized_rmse_percent": 1.8239916599818564,
                "reference_energy": 11.698532334119903,
                "candidate_energy": 11.695698578597593,
                "relative_energy_error_percent": 0.02422317126094042,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.921007737517357e-05,
                  "p95": 8.899593376554549e-05,
                  "p99": 0.0001888452097773552,
                  "maximum": 0.0006471879314631224
                },
                "worst": {
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "sky_patch_index": 47,
                  "rgb_channel": 0,
                  "reference": 0.007843413623049855,
                  "candidate": 0.007196225691586733
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.2655694087026864,
                "cvrmse_percent": 19.026878457402702,
                "rms_normalized_rmse_percent": 1.7896805015990256,
                "reference_energy": 7.193277131917327,
                "candidate_energy": 7.212380275462905,
                "relative_energy_error_percent": 0.2655694087026864,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.138802690547891e-05,
                  "p90": 6.836489774286747e-05,
                  "p95": 0.0001389624085277319,
                  "p99": 0.00029754440765827894,
                  "maximum": 0.0007932689040899277
                },
                "worst": {
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05313311517238617,
                  "candidate": 0.0539263840764761
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 174.63791696354747,
            "full": 3242.19424999319
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 178.6499589215964,
            "full": 3299.3899579159915
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 177.9110839124769,
            "full": 3274.945291923359
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 185.9352079918608,
            "full": 3256.313999998383
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_j_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 47,
            "stages": {
              "direct": {
                "nmbe_percent": 0.1045514601600724,
                "cvrmse_percent": 7.105853302107048,
                "rms_normalized_rmse_percent": 1.8146543353577973,
                "reference_energy": 11.683989015762371,
                "candidate_energy": 11.696204796883293,
                "relative_energy_error_percent": 0.1045514601600724,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.922016185242683e-05,
                  "p95": 9.071314707398415e-05,
                  "p99": 0.00019717542454600334,
                  "maximum": 0.0005126050673425198
                },
                "worst": {
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "sky_patch_index": 120,
                  "rgb_channel": 0,
                  "reference": 0.012260150164365768,
                  "candidate": 0.011747545097023249
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.2950070127559579,
                "cvrmse_percent": 20.225205682615613,
                "rms_normalized_rmse_percent": 1.9080336053550602,
                "reference_energy": 7.233944987846357,
                "candidate_energy": 7.212604342833302,
                "relative_energy_error_percent": 0.2950070127559579,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.1221427030250197e-05,
                  "p90": 7.326307240873575e-05,
                  "p95": 0.00014226743951439857,
                  "p99": 0.0003076051361858845,
                  "maximum": 0.0011472608894109726
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03239884041249752,
                  "candidate": 0.03125157952308655
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 174.5971660129726,
            "full": 3495.3589589567855
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 178.865542053245,
            "full": 3507.684624986723
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 178.59849997330457,
            "full": 3434.1137079754844
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 177.19462502282113,
            "full": 3435.7520419871435
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "plan_j_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 47,
            "stages": {
              "direct": {
                "nmbe_percent": -0.0817770297013866,
                "cvrmse_percent": 3.8524482199748404,
                "rms_normalized_rmse_percent": 0.9849475586826149,
                "reference_energy": 11.696854762492606,
                "candidate_energy": 11.687289422099354,
                "relative_energy_error_percent": 0.0817770297013866,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.0296196453273296e-05,
                  "p95": 4.5703956857323647e-05,
                  "p99": 0.00011353357695043087,
                  "maximum": 0.00022864993661642075
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 73,
                  "rgb_channel": 0,
                  "reference": 0.013858689926564693,
                  "candidate": 0.013630039989948273
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.17859379147399135,
                "cvrmse_percent": 11.65238686316504,
                "rms_normalized_rmse_percent": 1.0977824307856823,
                "reference_energy": 7.2146893303350765,
                "candidate_energy": 7.2275743175531915,
                "relative_energy_error_percent": 0.17859379147399135,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.848488166928291e-06,
                  "p90": 4.238079782226123e-05,
                  "p95": 8.114241063594818e-05,
                  "p99": 0.00018149311654269695,
                  "maximum": 0.0009001307189464569
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.047669075429439545,
                  "candidate": 0.048569206148386
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 264.4872920354828,
            "full": 6159.417333081365
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 275.8470829576254,
            "full": 6057.9979999456555
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 270.6937500042841,
            "full": 6211.907000048086
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 263.95954191684723,
            "full": 6125.414666952565
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 1398.5995830735192,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_j_distributed/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 4849.330332945101,
      "worker_pool_size": 12,
      "invocation_count": 3
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      47,
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
        "identifier": "plan_j_distributed_grid",
        "full_identifier": "plan_j_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": -0.24122717926379814,
            "cvrmse_percent": 4.386105240679791,
            "rms_normalized_rmse_percent": 1.1209744128669668,
            "reference_energy": 11.693484146288114,
            "candidate_energy": 11.665276284324364,
            "relative_energy_error_percent": 0.24122717926379816,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.085386611521244e-05,
              "p95": 3.6797195207327604e-05,
              "p99": 0.0001160530373454094,
              "maximum": 0.0005514095537364483
            },
            "worst": {
              "global_sensor_index": 40,
              "local_sensor_index": 40,
              "sky_patch_index": 130,
              "rgb_channel": 0,
              "reference": 0.007197155151516199,
              "candidate": 0.006645745597779751,
              "position": [
                8.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 1.116930805194458,
            "cvrmse_percent": 32.53084572387204,
            "rms_normalized_rmse_percent": 3.0649343603174444,
            "reference_energy": 7.219719807524825,
            "candidate_energy": 7.300359082103796,
            "relative_energy_error_percent": 1.116930805194458,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.00270057778107e-05,
              "p90": 0.00010037158062914386,
              "p95": 0.00013587428838945925,
              "p99": 0.0002616571728140116,
              "maximum": 0.003132987767457962
            },
            "worst": {
              "global_sensor_index": 28,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03794599324464798,
              "candidate": 0.04107898101210594,
              "position": [
                7.5,
                6.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.2772212087558558,
            "cvrmse_percent": 12.189551443082559,
            "rms_normalized_rmse_percent": 3.0085574646364566,
            "reference_energy": 18.91320395381294,
            "candidate_energy": 18.96563536642816,
            "relative_energy_error_percent": 0.2772212087558559,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.961249049349135e-05,
              "p90": 9.702070383355021e-05,
              "p95": 0.00012811343185603619,
              "p99": 0.0002479320392012596,
              "maximum": 0.003132987767457962
            },
            "worst": {
              "global_sensor_index": 28,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03794599324464798,
              "candidate": 0.04107898101210594,
              "position": [
                7.5,
                6.5,
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
        "identifier": "plan_j_distributed_grid",
        "full_identifier": "plan_j_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 47,
        "stages": {
          "direct": {
            "nmbe_percent": -0.24122717926379814,
            "cvrmse_percent": 4.386105240679791,
            "rms_normalized_rmse_percent": 1.1209744128669668,
            "reference_energy": 11.693484146288114,
            "candidate_energy": 11.665276284324364,
            "relative_energy_error_percent": 0.24122717926379816,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.085386611521244e-05,
              "p95": 3.6797195207327604e-05,
              "p99": 0.0001160530373454094,
              "maximum": 0.0005514095537364483
            },
            "worst": {
              "global_sensor_index": 40,
              "local_sensor_index": 40,
              "sky_patch_index": 130,
              "rgb_channel": 0,
              "reference": 0.007197155151516199,
              "candidate": 0.006645745597779751,
              "position": [
                8.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 96.5366031054972,
            "cvrmse_percent": 579.9586594604738,
            "rms_normalized_rmse_percent": 35.24072819655508,
            "reference_energy": 3.714503541197921,
            "candidate_energy": 7.300359082103796,
            "relative_energy_error_percent": 96.53660310549718,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 7.462819485226646e-05,
              "p90": 0.00021812974591739476,
              "p95": 0.0002776100009214133,
              "p99": 0.00047637056559324265,
              "maximum": 0.018589451909065247
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03707277774810791,
              "candidate": 0.05566222965717316,
              "position": [
                1.5,
                4.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 23.08963215119618,
            "cvrmse_percent": 139.77028746989234,
            "rms_normalized_rmse_percent": 35.22961044455575,
            "reference_energy": 15.407987687486035,
            "candidate_energy": 18.96563536642816,
            "relative_energy_error_percent": 23.089632151196184,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 7.439499677275307e-05,
              "p90": 0.00021357828518375754,
              "p95": 0.0002719626063480973,
              "p99": 0.00045109353959560394,
              "maximum": 0.018589451909065247
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03707277774810791,
              "candidate": 0.05566222965717316,
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
      "bias_percent": 0.1060667369637334,
      "rms_normalized_error_percent": 0.42299976968232317,
      "absolute_error": {
        "p95": 0.17761039835263398,
        "p99": 0.23633965240355598,
        "maximum": 0.24771416169107852
      },
      "worst_index": [
        37
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 17.896491696769367,
      "rms_normalized_to_uniform_percent": 0.42299976968232317
    },
    "overcast": {
      "bias_percent": 0.1174890154459169,
      "rms_normalized_error_percent": 0.38788664091943853,
      "absolute_error": {
        "p95": 0.1188392639160156,
        "p99": 0.152726035118103,
        "maximum": 0.15565133094787598
      },
      "worst_index": [
        37
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 11.557661056518555,
      "rms_normalized_to_uniform_percent": 0.26565561370356816
    },
    "horizon": {
      "bias_percent": 0.3769186665450396,
      "rms_normalized_error_percent": 2.530573941896242,
      "absolute_error": {
        "p95": 0.10818917827301637,
        "p99": 0.146616853295036,
        "maximum": 0.161389044305972
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.9665741616295704,
      "rms_normalized_to_uniform_percent": 0.2160955468816427
    },
    "north": {
      "bias_percent": -0.08385788471745288,
      "rms_normalized_error_percent": 0.7863965537302303,
      "absolute_error": {
        "p95": 0.13622486591339103,
        "p99": 0.1726457118988037,
        "maximum": 0.18047523498535156
      },
      "worst_index": [
        37
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 6.096602916717529,
      "rms_normalized_to_uniform_percent": 0.29399432119508684
    },
    "east": {
      "bias_percent": 0.1815372918169005,
      "rms_normalized_error_percent": 0.5951226924445521,
      "absolute_error": {
        "p95": 0.09993857741355892,
        "p99": 0.10947097778320312,
        "maximum": 0.11263656616210938
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 4.324701309204102,
      "rms_normalized_to_uniform_percent": 0.1846545961949568
    },
    "south": {
      "bias_percent": 0.175204701533805,
      "rms_normalized_error_percent": 0.4807640020708301,
      "absolute_error": {
        "p95": 0.07563238143920897,
        "p99": 0.10439412117004392,
        "maximum": 0.12174344062805176
      },
      "worst_index": [
        0
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.6240286827087402,
      "rms_normalized_to_uniform_percent": 0.15001934719732046
    },
    "west": {
      "bias_percent": 0.17536202210742488,
      "rms_normalized_error_percent": 0.6655559196928864,
      "absolute_error": {
        "p95": 0.10112656354904169,
        "p99": 0.16053201675415035,
        "maximum": 0.1786336898803711
      },
      "worst_index": [
        10
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 5.112454414367676,
      "rms_normalized_to_uniform_percent": 0.2041564117182391
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
          "nmbe_percent": 0.2517110991612151,
          "cvrmse_percent": 2.930637257564127,
          "absolute_error_percentiles_lux": {
            "p50": 6.4981689453125,
            "p90": 41.22292480468751,
            "p95": 59.31247558593746,
            "p99": 105.24849853515641
          },
          "maximum_absolute_error_lux": 337.51739501953125,
          "worst": {
            "sensor_index": 12,
            "position": [
              2.5,
              2.5,
              0.75
            ],
            "hour_of_year": 6250.5,
            "foton_lux": 1158.302490234375,
            "radiance_lux": 820.7850952148438
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.8976916350918098,
            "maximum_error_percentage_points": 6.823835616438355,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.23838137555536335,
            "maximum_error_percentage_points": 1.5687407412539756,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.18591081317400165,
            "maximum_error_percentage_points": 0.9350684931506805,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.1973389682308363,
            "maximum_error_percentage_points": 0.9350684931506805,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.03031769163509178,
            "maximum_error_percentage_points": 0.22410958904109624,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 68.08510638297872,
          "radiance_percent": 68.08510638297872,
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
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_j_distributed_grid",
            "maximum_error_percentage_points": 0.004911039169527953,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_j_distributed_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_j_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_j_distributed_grid",
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
      "study_preparation_seconds": 0.008361291023902595,
      "weather_seconds": 0.11169995809905231,
      "metric_reduction_seconds": 0.0389792500063777,
      "write_seconds": 0.03604379098396748,
      "total_seconds": 0.1868702919455245,
      "cold_end_to_end_seconds": 0.1952315829694271,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.01964595797471702,
      "engine_upload_seconds": 0.00028212499999999993,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.02099420828744769,
      "engine_annual_reduction_seconds": 0.00042629160452634096,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.02099420828744769
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.008361291023902595,
      "weather_seconds": 0.10797587502747774,
      "metric_reduction_seconds": 0.012032333062961698,
      "write_seconds": 0.03517666691914201,
      "total_seconds": 0.15534400008618832,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.15534400008618832,
      "raw_export_seconds": 0.01029141596518457,
      "engine_upload_seconds": 6.0041e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0004917916376143694,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.020950375008396804,
      "full": 0.013619707897305489
    }
  },
  "elapsed_seconds": 64.17901620897464,
  "result_class": "passed"
}
```
