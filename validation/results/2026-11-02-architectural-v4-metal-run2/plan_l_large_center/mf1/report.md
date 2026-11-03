# Foton report

Status: **passed**

```json
{
  "scene": "plan_l_large_center",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_l_large_center",
    "category": "form",
    "question": "How does a large center opening illuminate a L-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "l",
    "window_profile": "large_center"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 48,
    "floor_area": 54.0,
    "aperture_area": 4.800000000000001
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "df42ce081a9c6866b2b0000184370f15f4bf408b307ed54d1cc7ccf45dd54b30",
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
      "scene_fingerprint": 9519076420102749743,
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
      "scene_fingerprint": 9519076420102749743,
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
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "plan_l_large_center_grid",
        "bias_percent": -0.04277980441328652,
        "rms_normalized_error_percent": 0.9236977764085991,
        "absolute_error": {
          "p95": 4.3422915041446686e-07,
          "p99": 5.43864443898201e-05,
          "maximum": 0.00047375215217471123
        },
        "worst_index": [
          42,
          99,
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
        "identifier": "plan_l_large_center_grid",
        "bias_percent": 0.09643373517563257,
        "rms_normalized_error_percent": 0.8238683181055928,
        "absolute_error": {
          "p95": 3.2017938792705536e-05,
          "p99": 0.00011201901361346245,
          "maximum": 0.00045915693044662476
        },
        "worst_index": [
          35,
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
        "identifier": "plan_l_large_center_grid",
        "bias_percent": -0.03494859040020623,
        "rms_normalized_error_percent": 0.648236003889438,
        "absolute_error": {
          "p95": 2.6518013328313828e-05,
          "p99": 9.031500667333603e-05,
          "maximum": 0.00026976317167282104
        },
        "worst_index": [
          33,
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
            "identifier": "plan_l_large_center_grid",
            "start_sensor_index": 0,
            "sensor_count": 48,
            "stages": {
              "direct": {
                "nmbe_percent": -0.14766941423268165,
                "cvrmse_percent": 22.693683611271116,
                "rms_normalized_rmse_percent": 3.960672626924795,
                "reference_energy": 6.654412662568575,
                "candidate_energy": 6.6445861303691345,
                "relative_energy_error_percent": 0.14766941423268162,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.6451808884739876e-05,
                  "p99": 0.0003766808658838272,
                  "maximum": 0.0012004300951957703
                },
                "worst": {
                  "global_sensor_index": 41,
                  "local_sensor_index": 41,
                  "sky_patch_index": 100,
                  "rgb_channel": 0,
                  "reference": 0.014379370026290417,
                  "candidate": 0.013178939931094646
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.6784686922846934,
                "cvrmse_percent": 92.12186955767069,
                "rms_normalized_rmse_percent": 3.8837809199670454,
                "reference_energy": 2.152212156718548,
                "candidate_energy": 2.1668142423934285,
                "relative_energy_error_percent": 0.6784686922846933,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.74191136972516e-06,
                  "p95": 8.843716932460666e-05,
                  "p99": 0.0005067299352958798,
                  "maximum": 0.0013854596763849258
                },
                "worst": {
                  "global_sensor_index": 41,
                  "local_sensor_index": 41,
                  "sky_patch_index": 133,
                  "rgb_channel": 0,
                  "reference": 0.0005894806236028671,
                  "candidate": -0.0007959790527820587
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 121.47412507329136,
            "full": 277.44954195804894
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 124.75495901890099,
            "full": 271.2412920081988
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 135.1004169555381,
            "full": 264.72616707906127
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 126.61966704763472,
            "full": 290.2210419997573
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
            "identifier": "plan_l_large_center_grid",
            "start_sensor_index": 0,
            "sensor_count": 48,
            "stages": {
              "direct": {
                "nmbe_percent": 0.014438603135013736,
                "cvrmse_percent": 7.850715809734298,
                "rms_normalized_rmse_percent": 1.3707216897030272,
                "reference_energy": 6.650737049341842,
                "candidate_energy": 6.65169732286995,
                "relative_energy_error_percent": 0.014438603135013736,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.108409535139799e-05,
                  "p99": 0.000132865272462368,
                  "maximum": 0.00040637003257870674
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "sky_patch_index": 71,
                  "rgb_channel": 0,
                  "reference": 0.013403954915702343,
                  "candidate": 0.012997584883123636
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.006582056832185754,
                "cvrmse_percent": 22.69735788361177,
                "rms_normalized_rmse_percent": 1.526354538693861,
                "reference_energy": 4.082415198067459,
                "candidate_energy": 4.082146491178996,
                "relative_energy_error_percent": 0.006582056832185754,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.0000000116860974e-07,
                  "p90": 2.015354039031087e-05,
                  "p95": 4.974941839464009e-05,
                  "p99": 0.00023233599495142698,
                  "maximum": 0.0008388999849557877
                },
                "worst": {
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.027399254962801933,
                  "candidate": 0.026560354977846146
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 166.0362499533221,
            "full": 3034.7393749980256
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 170.4402919858694,
            "full": 3102.0869170315564
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 164.5657499320805,
            "full": 2989.4688329659402
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 162.0450409827754,
            "full": 3043.736333027482
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
            "identifier": "plan_l_large_center_grid",
            "start_sensor_index": 0,
            "sensor_count": 48,
            "stages": {
              "direct": {
                "nmbe_percent": -0.050565298303332985,
                "cvrmse_percent": 8.284288289981626,
                "rms_normalized_rmse_percent": 1.4474874900612325,
                "reference_energy": 6.655559439161152,
                "candidate_energy": 6.652194035676985,
                "relative_energy_error_percent": 0.05056529830333299,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1386193111538887e-05,
                  "p99": 0.00013994146138429642,
                  "maximum": 0.00038034049794077873
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "sky_patch_index": 50,
                  "rgb_channel": 0,
                  "reference": 0.007289521396160126,
                  "candidate": 0.006909180898219347
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.06804894856814332,
                "cvrmse_percent": 23.622478620678013,
                "rms_normalized_rmse_percent": 1.590641287517438,
                "reference_energy": 4.088580826069894,
                "candidate_energy": 4.091363062333393,
                "relative_energy_error_percent": 0.06804894856814332,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.856710754732376e-08,
                  "p90": 2.0564566875691548e-05,
                  "p95": 5.00725582242012e-05,
                  "p99": 0.0002396092750132084,
                  "maximum": 0.0010121110826730728
                },
                "worst": {
                  "global_sensor_index": 42,
                  "local_sensor_index": 42,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04744848050177097,
                  "candidate": 0.0464363694190979
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 215.5497909989208,
            "full": 3226.2837500311434
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 167.86024998873472,
            "full": 3237.7938330173492
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 159.87879200838506,
            "full": 3281.2682079384103
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 161.9339589960873,
            "full": 3305.5433749686927
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
            "identifier": "plan_l_large_center_grid",
            "start_sensor_index": 0,
            "sensor_count": 48,
            "stages": {
              "direct": {
                "nmbe_percent": 0.03476605994211428,
                "cvrmse_percent": 4.414330931546166,
                "rms_normalized_rmse_percent": 0.7709749736977843,
                "reference_energy": 6.652226753880768,
                "candidate_energy": 6.654539471021508,
                "relative_energy_error_percent": 0.03476605994211428,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.0928699339274317e-05,
                  "p99": 7.741013541817665e-05,
                  "maximum": 0.0002065594308078289
                },
                "worst": {
                  "global_sensor_index": 41,
                  "local_sensor_index": 41,
                  "sky_patch_index": 96,
                  "rgb_channel": 0,
                  "reference": 0.014302755240350962,
                  "candidate": 0.01450931467115879
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.049735000413063696,
                "cvrmse_percent": 13.379123239519089,
                "rms_normalized_rmse_percent": 0.8996310329566785,
                "reference_energy": 4.087727286586439,
                "candidate_energy": 4.0856942554035705,
                "relative_energy_error_percent": 0.0497350004130637,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.643791910538766e-08,
                  "p90": 1.4551672211382559e-05,
                  "p95": 3.248623397666961e-05,
                  "p99": 0.00012473651440814137,
                  "maximum": 0.0008323080837726593
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 38,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.06454578414559364,
                  "candidate": 0.06371347606182098
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 262.9444169579074,
            "full": 5748.1113750254735
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 240.82025000825524,
            "full": 5695.246999966912
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 250.35149999894202,
            "full": 5806.369208032265
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 257.1568751009181,
            "full": 5764.498582924716
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 1323.4633340034634,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/plan_l_large_center/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 4990.512082935311,
      "worker_pool_size": 12,
      "invocation_count": 3
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      48,
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
        "identifier": "plan_l_large_center_grid",
        "full_identifier": "plan_l_large_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": 0.05870040520822543,
            "cvrmse_percent": 2.9471831019278656,
            "rms_normalized_rmse_percent": 0.5146542009978081,
            "reference_energy": 6.652876656219178,
            "candidate_energy": 6.656781921774382,
            "relative_energy_error_percent": 0.05870040520822543,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.818422555923462e-07,
              "p99": 3.629550337791443e-05,
              "maximum": 0.0002032020129263401
            },
            "worst": {
              "global_sensor_index": 40,
              "local_sensor_index": 40,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.003940886352211237,
              "candidate": 0.004144088365137577,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.8809589253748874,
            "cvrmse_percent": 21.873917197723987,
            "rms_normalized_rmse_percent": 1.4716194012781694,
            "reference_energy": 4.0872172394340165,
            "candidate_energy": 4.051210534363761,
            "relative_energy_error_percent": 0.8809589253748874,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.0273963485806235e-07,
              "p90": 2.6734306993603243e-05,
              "p95": 4.7289038775488734e-05,
              "p99": 0.00012180604971945286,
              "maximum": 0.0013220496475696564
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04662993922829628,
              "candidate": 0.045307889580726624,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.29889347176045894,
            "cvrmse_percent": 8.313147236214121,
            "rms_normalized_rmse_percent": 1.469652880437254,
            "reference_energy": 10.740093895653194,
            "candidate_energy": 10.707992456138143,
            "relative_energy_error_percent": 0.29889347176045894,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.038563096107282e-07,
              "p90": 2.613837978060474e-05,
              "p95": 4.7023408114910126e-05,
              "p99": 0.00011898763477802277,
              "maximum": 0.0013220496475696564
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04662993922829628,
              "candidate": 0.045307889580726624,
              "position": [
                3.5,
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
      48,
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
        "identifier": "plan_l_large_center_grid",
        "full_identifier": "plan_l_large_center_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": 0.05870040520822543,
            "cvrmse_percent": 2.9471831019278656,
            "rms_normalized_rmse_percent": 0.5146542009978081,
            "reference_energy": 6.652876656219178,
            "candidate_energy": 6.656781921774382,
            "relative_energy_error_percent": 0.05870040520822543,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.818422555923462e-07,
              "p99": 3.629550337791443e-05,
              "maximum": 0.0002032020129263401
            },
            "worst": {
              "global_sensor_index": 40,
              "local_sensor_index": 40,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.003940886352211237,
              "candidate": 0.004144088365137577,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 87.89216829371847,
            "cvrmse_percent": 598.1315641288945,
            "rms_normalized_rmse_percent": 25.272759497748183,
            "reference_energy": 2.1561359215519786,
            "candidate_energy": 4.051210534363761,
            "relative_energy_error_percent": 87.89216829371847,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00020168895271126553,
              "p95": 0.00033073892700485885,
              "p99": 0.0006259205729293171,
              "maximum": 0.01409679651260376
            },
            "worst": {
              "global_sensor_index": 43,
              "local_sensor_index": 43,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025630224496126175,
              "candidate": 0.039727021008729935,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.55723881197436,
            "cvrmse_percent": 146.43151782490193,
            "rms_normalized_rmse_percent": 25.277935557698243,
            "reference_energy": 8.809012577771156,
            "candidate_energy": 10.707992456138143,
            "relative_energy_error_percent": 21.55723881197436,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002035896217421396,
              "p95": 0.00032918220676947385,
              "p99": 0.0006259205729293171,
              "maximum": 0.01409679651260376
            },
            "worst": {
              "global_sensor_index": 43,
              "local_sensor_index": 43,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025630224496126175,
              "candidate": 0.039727021008729935,
              "position": [
                6.5,
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
      "bias_percent": 0.19943696520787546,
      "rms_normalized_error_percent": 0.3094087469693205,
      "absolute_error": {
        "p95": 0.13313749095328448,
        "p99": 0.24984424024046664,
        "maximum": 0.26938766654431134
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.866823989337089,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.3094087469693205
    },
    "overcast": {
      "bias_percent": 0.17090221266344588,
      "rms_normalized_error_percent": 0.2491099125759532,
      "absolute_error": {
        "p95": 0.0741990566253662,
        "p99": 0.14570520401000978,
        "maximum": 0.15174102783203125
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.5396037101745605,
      "reference_fraction_of_uniform": 0.6627870798110962,
      "rms_normalized_to_uniform_percent": 0.1763753030084572
    },
    "horizon": {
      "bias_percent": 0.789932232055033,
      "rms_normalized_error_percent": 2.423740639922774,
      "absolute_error": {
        "p95": 0.05522286282281343,
        "p99": 0.07372405143084135,
        "maximum": 0.085260811957514
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.7496941501179558,
      "reference_fraction_of_uniform": 0.07598130370300896,
      "rms_normalized_to_uniform_percent": 0.12219159949062658
    },
    "north": {
      "bias_percent": -64.15161444195112,
      "rms_normalized_error_percent": 109.47364143603738,
      "absolute_error": {
        "p95": 4.5591114758281035e-05,
        "p99": 5.4293562325256065e-05,
        "maximum": 5.437189611257054e-05
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.0956132427963894e-05,
      "reference_fraction_of_uniform": 1.1104010582130286e-06,
      "rms_normalized_to_uniform_percent": 8.663653863187948e-05
    },
    "east": {
      "bias_percent": 0.14698011235131728,
      "rms_normalized_error_percent": 0.4055136511797355,
      "absolute_error": {
        "p95": 0.04393313229084015,
        "p99": 0.054507725238800056,
        "maximum": 0.05645179748535156
      },
      "worst_index": [
        36
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.3257462978363037,
      "reference_fraction_of_uniform": 0.23571376502513885,
      "rms_normalized_to_uniform_percent": 0.08912786501468459
    },
    "south": {
      "bias_percent": 0.22972766452148644,
      "rms_normalized_error_percent": 0.36830948513876827,
      "absolute_error": {
        "p95": 0.11700086593627923,
        "p99": 0.19299802780151373,
        "maximum": 0.21714401245117188
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.405214786529541,
      "reference_fraction_of_uniform": 0.6491668224334717,
      "rms_normalized_to_uniform_percent": 0.23529183361722847
    },
    "west": {
      "bias_percent": 0.21727812129268814,
      "rms_normalized_error_percent": 0.3673646828877189,
      "absolute_error": {
        "p95": 0.03557615280151367,
        "p99": 0.055875668525695824,
        "maximum": 0.06688165664672852
      },
      "worst_index": [
        46
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.778768539428711,
      "reference_fraction_of_uniform": 0.1802777200937271,
      "rms_normalized_to_uniform_percent": 0.07640646011429522
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
        "identifier": "plan_l_large_center_grid",
        "sensor_count": 48,
        "illuminance": {
          "nmbe_percent": 0.12540696008608754,
          "cvrmse_percent": 1.8950255273114582,
          "absolute_error_percentiles_lux": {
            "p50": 1.5746192932128906,
            "p90": 18.73654174804689,
            "p95": 31.78472137451171,
            "p99": 70.54220703124997
          },
          "maximum_absolute_error_lux": 433.802734375,
          "worst": {
            "sensor_index": 40,
            "position": [
              5.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 11941.185546875,
            "radiance_lux": 11507.3828125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.28017694063926885,
            "maximum_error_percentage_points": 2.7398630136986313,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.3628834231388207,
            "maximum_error_percentage_points": 1.5435708729970727,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.4343093607305932,
            "maximum_error_percentage_points": 2.218493150684928,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.45562785388127924,
            "maximum_error_percentage_points": 2.218493150684928,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.026364155251141774,
            "maximum_error_percentage_points": 0.4099999999999966,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 29.166666666666668,
          "radiance_percent": 29.166666666666668,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.0833333333333335,
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
      "maximum_error_percentage_points": 0.00497056934932516,
      "metrics": {
        "da": [
          {
            "identifier": "plan_l_large_center_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_l_large_center_grid",
            "maximum_error_percentage_points": 0.00497056934932516,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_l_large_center_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_l_large_center_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_l_large_center_grid",
            "maximum_error_percentage_points": 0.0046575342465753344,
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
      "study_preparation_seconds": 0.007080749957822263,
      "weather_seconds": 0.12118991697207093,
      "metric_reduction_seconds": 0.049707208992913365,
      "write_seconds": 0.033149000024423,
      "total_seconds": 0.2042227080091834,
      "cold_end_to_end_seconds": 0.21130345796700567,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.016295374953188002,
      "engine_upload_seconds": 0.0002727079999999999,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.03127816668711603,
      "engine_annual_reduction_seconds": 0.00043212505988776684,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.03127816668711603
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007080749957822263,
      "weather_seconds": 0.11017008300404996,
      "metric_reduction_seconds": 0.013075915980152786,
      "write_seconds": 0.03236954193562269,
      "total_seconds": 0.1560756249818951,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1560756249818951,
      "raw_export_seconds": 0.011729666031897068,
      "engine_upload_seconds": 7.2792e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00044424994848668575,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.00800491706468165,
      "full": 0.02493158297147602
    }
  },
  "elapsed_seconds": 60.634033540962264,
  "result_class": "passed"
}
```
