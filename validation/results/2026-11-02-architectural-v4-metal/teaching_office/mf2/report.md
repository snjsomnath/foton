# Foton report

Status: **passed**

```json
{
  "scene": "teaching_office",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_office",
    "category": "teaching",
    "question": "How is a 12 x 8 m open-plan office with a ribbon window lit?",
    "interactions": [
      "multiple_bounces",
      "room",
      "side_glazing",
      "window"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 96,
    "floor_area": 96.0,
    "aperture_area": 17.6
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "9d884188229e6333f46b72c59e94eb3687d4ded403ab2b2e22cdf96a1fb20667",
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
      "scene_fingerprint": 17113111844658936175,
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 17113111844658936175,
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
    "maximum_samples": 16384,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "teaching_office_grid",
        "bias_percent": 0.033900770041301743,
        "rms_normalized_error_percent": 0.7639001981790288,
        "absolute_error": {
          "p95": 1.038727532431949e-06,
          "p99": 2.4425185984000564e-05,
          "maximum": 0.00013817357830703259
        },
        "worst_index": [
          6,
          356,
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
        "identifier": "teaching_office_grid",
        "bias_percent": 0.01630006531475502,
        "rms_normalized_error_percent": 1.0429299174356472,
        "absolute_error": {
          "p95": 6.503588519990444e-05,
          "p99": 0.00013963853474706367,
          "maximum": 0.0008445456624031067
        },
        "worst_index": [
          62,
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
        "identifier": "teaching_office_grid",
        "bias_percent": 0.00010561813845889186,
        "rms_normalized_error_percent": 0.8610790567573474,
        "absolute_error": {
          "p95": 5.31667610630393e-05,
          "p99": 0.00011170711659360663,
          "maximum": 0.0008056536316871643
        },
        "worst_index": [
          62,
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "teaching_office_grid",
            "start_sensor_index": 0,
            "sensor_count": 96,
            "stages": {
              "direct": {
                "nmbe_percent": -0.022102404959055313,
                "cvrmse_percent": 24.456010063020123,
                "rms_normalized_rmse_percent": 7.153361546707228,
                "reference_energy": 37.08322193625963,
                "candidate_energy": 37.075025652375416,
                "relative_energy_error_percent": 0.022102404959055313,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.5891087211202884e-05,
                  "p95": 0.00012787955347448587,
                  "p99": 0.00027569997007958536,
                  "maximum": 0.0006965970387682319
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 44,
                  "sky_patch_index": 209,
                  "rgb_channel": 0,
                  "reference": 0.0025582039961591363,
                  "candidate": 0.0018616069573909044
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.16362002878338094,
                "cvrmse_percent": 95.80360443207094,
                "rms_normalized_rmse_percent": 3.7211265449497657,
                "reference_energy": 15.49374622942565,
                "candidate_energy": 15.51909710146586,
                "relative_energy_error_percent": 0.16362002878338094,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.109835616778651e-05,
                  "p95": 0.00019419382442720234,
                  "p99": 0.00042915389029076195,
                  "maximum": 0.002236798405647278
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.07741205394268036,
                  "candidate": 0.07964885234832764
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 189.73604100756347,
            "full": 474.38466700259596
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 186.24904192984104,
            "full": 489.7485830588266
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 185.7383749447763,
            "full": 476.92908393219113
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 189.77895902935416,
            "full": 485.858291038312
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "teaching_office_grid",
            "start_sensor_index": 0,
            "sensor_count": 96,
            "stages": {
              "direct": {
                "nmbe_percent": -0.011111567044041346,
                "cvrmse_percent": 16.263229643015503,
                "rms_normalized_rmse_percent": 4.759135121947264,
                "reference_energy": 37.08910636831695,
                "candidate_energy": 37.084985187396796,
                "relative_energy_error_percent": 0.011111567044041346,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.9414531309158758e-05,
                  "p95": 8.73330282047391e-05,
                  "p99": 0.00018204225343652067,
                  "maximum": 0.00040902348700910807
                },
                "worst": {
                  "global_sensor_index": 53,
                  "local_sensor_index": 53,
                  "sky_patch_index": 156,
                  "rgb_channel": 0,
                  "reference": 0.0014088714960962534,
                  "candidate": 0.0018178949831053615
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.0805569638149195,
                "cvrmse_percent": 34.45653714729221,
                "rms_normalized_rmse_percent": 1.8815729440218314,
                "reference_energy": 26.784470538226987,
                "candidate_energy": 26.806047294466484,
                "relative_energy_error_percent": 0.08055696381491949,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.000000058430487e-08,
                  "p90": 5.005709062970754e-05,
                  "p95": 0.00012451864313334227,
                  "p99": 0.0002611882425844669,
                  "maximum": 0.0009146835654973984
                },
                "worst": {
                  "global_sensor_index": 73,
                  "local_sensor_index": 73,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03659958392381668,
                  "candidate": 0.03568490035831928
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 286.6653329692781,
            "full": 5811.256834072992
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 283.8911669095978,
            "full": 5719.091832987033
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 300.7143749855459,
            "full": 5658.905624994077
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 300.5765830166638,
            "full": 6040.791583014652
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "teaching_office_grid",
            "start_sensor_index": 0,
            "sensor_count": 96,
            "stages": {
              "direct": {
                "nmbe_percent": 0.05566771406034831,
                "cvrmse_percent": 16.516152482357843,
                "rms_normalized_rmse_percent": 4.8329751061247315,
                "reference_energy": 37.07599352110287,
                "candidate_energy": 37.096632879161234,
                "relative_energy_error_percent": 0.05566771406034831,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.082590319536426e-05,
                  "p95": 8.848914876580238e-05,
                  "p99": 0.0001834182604216037,
                  "maximum": 0.00040704989805817604
                },
                "worst": {
                  "global_sensor_index": 62,
                  "local_sensor_index": 62,
                  "sky_patch_index": 357,
                  "rgb_channel": 0,
                  "reference": 0.0040125459199771285,
                  "candidate": 0.0036054960219189525
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.04705819772504035,
                "cvrmse_percent": 34.89604834305114,
                "rms_normalized_rmse_percent": 1.9091155548208667,
                "reference_energy": 26.812713250885963,
                "candidate_energy": 26.800095671268913,
                "relative_energy_error_percent": 0.04705819772504036,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.000000058430487e-08,
                  "p90": 5.044646677561112e-05,
                  "p95": 0.00012620881898328662,
                  "p99": 0.00027078128936409404,
                  "maximum": 0.001062549650669098
                },
                "worst": {
                  "global_sensor_index": 30,
                  "local_sensor_index": 30,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.10424190014600754,
                  "candidate": 0.10530444979667664
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 287.74541697930545,
            "full": 5989.801625022665
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 279.2998329969123,
            "full": 5946.695666061714
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 296.86720902100205,
            "full": 5977.551791933365
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 286.26504202838987,
            "full": 5918.459334061481
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "teaching_office_grid",
            "start_sensor_index": 0,
            "sensor_count": 96,
            "stages": {
              "direct": {
                "nmbe_percent": 0.015299766330235942,
                "cvrmse_percent": 9.443111678898326,
                "rms_normalized_rmse_percent": 2.7650752778309933,
                "reference_energy": 37.086223890241456,
                "candidate_energy": 37.09189799583737,
                "relative_energy_error_percent": 0.01529976633023594,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.0952895283699036e-05,
                  "p95": 4.692497896030545e-05,
                  "p99": 0.00010349417469114958,
                  "maximum": 0.00023646559566259384
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 307,
                  "rgb_channel": 0,
                  "reference": 0.003267888445407152,
                  "candidate": 0.003504354041069746
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.06125255239659564,
                "cvrmse_percent": 20.712651201785196,
                "rms_normalized_rmse_percent": 1.132378409545624,
                "reference_energy": 26.8119355965525,
                "candidate_energy": 26.795512601652682,
                "relative_energy_error_percent": 0.06125255239659564,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.000000058430487e-08,
                  "p90": 2.9876301414333335e-05,
                  "p95": 7.244700100272894e-05,
                  "p99": 0.00015320491540478522,
                  "maximum": 0.0011527128517627716
                },
                "worst": {
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.09834581986069679,
                  "candidate": 0.09719310700893402
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 473.03779202047735,
            "full": 10509.304334060289
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 480.63700005877763,
            "full": 10432.978042052127
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 472.5373330293223,
            "full": 10463.838708004914
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 474.7534159105271,
            "full": 10683.703333954327
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 16448.448957991786,
      "worker_pool_size": 12,
      "invocation_count": 6
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_office/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 66111.93791602273,
      "worker_pool_size": 12,
      "invocation_count": 6
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      96,
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
        "identifier": "teaching_office_grid",
        "full_identifier": "teaching_office_grid",
        "start_sensor_index": 0,
        "sensor_count": 96,
        "stages": {
          "direct": {
            "nmbe_percent": 0.013198406140027399,
            "cvrmse_percent": 1.4533457640649505,
            "rms_normalized_rmse_percent": 0.42563872445607287,
            "reference_energy": 37.08307247574339,
            "candidate_energy": 37.08796685025794,
            "relative_energy_error_percent": 0.0131984061400274,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.470348358154297e-08,
              "p95": 7.529743015766144e-07,
              "p99": 1.4563087024724947e-05,
              "maximum": 7.757823914289474e-05
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 265,
              "rgb_channel": 0,
              "reference": 0.0005262034246698022,
              "candidate": 0.00044862518552690744,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.831396420361818,
            "cvrmse_percent": 71.47435895558121,
            "rms_normalized_rmse_percent": 3.9067121794213535,
            "reference_energy": 26.809712635165486,
            "candidate_energy": 26.318720517655777,
            "relative_energy_error_percent": 1.8313964203618114,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 7.499999554738679e-08,
              "p90": 5.35588085767814e-05,
              "p95": 8.047721348702908e-05,
              "p99": 0.00015105429163668295,
              "maximum": 0.006234504282474518
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.10740287601947784,
              "candidate": 0.10116837173700333,
              "position": [
                4.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.7608022441835398,
            "cvrmse_percent": 29.984853344212567,
            "rms_normalized_rmse_percent": 3.9059145437739495,
            "reference_energy": 63.89278511090889,
            "candidate_energy": 63.40668736791372,
            "relative_energy_error_percent": 0.7608022441835537,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 7.499999554738679e-08,
              "p90": 5.340353193332716e-05,
              "p95": 8.010666351765394e-05,
              "p99": 0.00015020896273199458,
              "maximum": 0.006234504282474518
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.10740287601947784,
              "candidate": 0.10116837173700333,
              "position": [
                4.5,
                1.5,
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
      96,
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
        "identifier": "teaching_office_grid",
        "full_identifier": "teaching_office_grid",
        "start_sensor_index": 0,
        "sensor_count": 96,
        "stages": {
          "direct": {
            "nmbe_percent": 0.013198406140027399,
            "cvrmse_percent": 1.4533457640649505,
            "rms_normalized_rmse_percent": 0.42563872445607287,
            "reference_energy": 37.08307247574339,
            "candidate_energy": 37.08796685025794,
            "relative_energy_error_percent": 0.0131984061400274,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.470348358154297e-08,
              "p95": 7.529743015766144e-07,
              "p99": 1.4563087024724947e-05,
              "maximum": 7.757823914289474e-05
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 265,
              "rgb_channel": 0,
              "reference": 0.0005262034246698022,
              "candidate": 0.00044862518552690744,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 69.77111061026098,
            "cvrmse_percent": 595.9561574282747,
            "rms_normalized_rmse_percent": 23.153407570843292,
            "reference_energy": 15.502472960829573,
            "candidate_energy": 26.318720517655777,
            "relative_energy_error_percent": 69.77111061026099,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00016196254000533402,
              "p95": 0.00023871439043432474,
              "p99": 0.0003915884703746991,
              "maximum": 0.020484663546085358
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0534072145819664,
              "candidate": 0.07389187812805176,
              "position": [
                0.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.578168090683544,
            "cvrmse_percent": 175.6951791315613,
            "rms_normalized_rmse_percent": 23.153990513497988,
            "reference_energy": 52.585545436572964,
            "candidate_energy": 63.40668736791372,
            "relative_energy_error_percent": 20.578168090683548,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00016216353542404272,
              "p95": 0.00023946911096572876,
              "p99": 0.0003914870147127655,
              "maximum": 0.020484663546085358
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0534072145819664,
              "candidate": 0.07389187812805176,
              "position": [
                0.5,
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
      "bias_percent": 0.19662692667836817,
      "rms_normalized_error_percent": 0.36079477810738503,
      "absolute_error": {
        "p95": 0.3025293207961277,
        "p99": 0.3550449707394343,
        "maximum": 0.4334335880673539
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 28.437877071353,
      "rms_normalized_to_uniform_percent": 0.36079477810738503
    },
    "overcast": {
      "bias_percent": 0.14595273844925133,
      "rms_normalized_error_percent": 0.30493648908491283,
      "absolute_error": {
        "p95": 0.15257740020751953,
        "p99": 0.23173885345458975,
        "maximum": 0.2605094909667969
      },
      "worst_index": [
        70
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 18.155546188354492,
      "rms_normalized_to_uniform_percent": 0.21360794327041274
    },
    "horizon": {
      "bias_percent": 0.8379752282093974,
      "rms_normalized_error_percent": 2.797777891612535,
      "absolute_error": {
        "p95": 0.21284681578450915,
        "p99": 0.3496132517628661,
        "maximum": 0.3891658643947995
      },
      "worst_index": [
        48
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.4839416949814734,
      "rms_normalized_to_uniform_percent": 0.2567689986203915
    },
    "north": {
      "bias_percent": -93.46785266136172,
      "rms_normalized_error_percent": 99.48552447310195,
      "absolute_error": {
        "p95": 8.018971129786223e-05,
        "p99": 0.00017260432214243328,
        "maximum": 0.00020075553038623184
      },
      "worst_index": [
        1
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 1.7276952348765917e-05,
      "rms_normalized_to_uniform_percent": 9.532456683563821e-05
    },
    "east": {
      "bias_percent": 0.09427127781776114,
      "rms_normalized_error_percent": 0.5488584231572909,
      "absolute_error": {
        "p95": 0.08728241920471191,
        "p99": 0.1213626146316527,
        "maximum": 0.16772985458374023
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 5.44617223739624,
      "rms_normalized_to_uniform_percent": 0.11219987211765335
    },
    "south": {
      "bias_percent": 0.2503024710706884,
      "rms_normalized_error_percent": 0.45774091992774124,
      "absolute_error": {
        "p95": 0.23867416381835938,
        "p99": 0.34269709587097164,
        "maximum": 0.3652191162109375
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 19.68645668029785,
      "rms_normalized_to_uniform_percent": 0.29025847893844564
    },
    "west": {
      "bias_percent": 0.08621389476531564,
      "rms_normalized_error_percent": 0.4854982760748107,
      "absolute_error": {
        "p95": 0.07661652565002441,
        "p99": 0.08269655704498283,
        "maximum": 0.10836100578308105
      },
      "worst_index": [
        90
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 5.5114569664001465,
      "rms_normalized_to_uniform_percent": 0.10002227305270482
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
        "identifier": "teaching_office_grid",
        "sensor_count": 96,
        "illuminance": {
          "nmbe_percent": 0.010501995945681315,
          "cvrmse_percent": 3.0761822606657874,
          "absolute_error_percentiles_lux": {
            "p50": 9.90069580078125,
            "p90": 117.42239990234376,
            "p95": 174.97901611328115,
            "p99": 311.553300781252
          },
          "maximum_absolute_error_lux": 921.010498046875,
          "worst": {
            "sensor_index": 13,
            "position": [
              1.5,
              2.5,
              0.75
            ],
            "hour_of_year": 3226.5,
            "foton_lux": 3938.318603515625,
            "radiance_lux": 3017.30810546875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.14811643835616498,
            "maximum_error_percentage_points": 0.7957534246575335,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.06814000028509619,
            "maximum_error_percentage_points": 0.39659660885865833,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.059774543378995404,
            "maximum_error_percentage_points": 0.4145205479452052,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.22401113013698618,
            "maximum_error_percentage_points": 1.4205479452054774,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.2267109018264839,
            "maximum_error_percentage_points": 1.423698630136986,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
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
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_office_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_office_grid",
            "maximum_error_percentage_points": 0.004829302226028176,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_office_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_office_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_office_grid",
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
      "study_preparation_seconds": 0.00986900005955249,
      "weather_seconds": 0.12114720791578293,
      "metric_reduction_seconds": 0.08337070804554969,
      "write_seconds": 0.029927709023468196,
      "total_seconds": 0.23465841705910861,
      "cold_end_to_end_seconds": 0.2445274171186611,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.010843917028978467,
      "engine_upload_seconds": 0.00078,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.027560833259485662,
      "engine_annual_reduction_seconds": 0.0036791249876841903,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.027560833259485662
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.00986900005955249,
      "weather_seconds": 0.11620587506331503,
      "metric_reduction_seconds": 0.04866299999412149,
      "write_seconds": 0.027362209046259522,
      "total_seconds": 0.19242637499701232,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.19242637499701232,
      "raw_export_seconds": 0.013873832998797297,
      "engine_upload_seconds": 0.0001015,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0036606249632313848,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.023775540990754962,
      "full": 0.025286832940764725
    }
  },
  "elapsed_seconds": 182.08291462506168,
  "result_class": "passed"
}
```
