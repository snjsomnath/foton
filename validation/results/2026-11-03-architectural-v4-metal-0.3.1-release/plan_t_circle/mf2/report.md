# Foton report

Status: **passed**

```json
{
  "scene": "plan_t_circle",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_t_circle",
    "category": "form",
    "question": "How does a circle opening illuminate a T-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "t",
    "window_profile": "circle"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 54,
    "floor_area": 63.0,
    "aperture_area": 1.44
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "dca026f8505eeeb4cbf2fe2651043458124527213a7feba10ded39869ad033b5",
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
      "scene_fingerprint": 13085702229645769746,
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
      "scene_fingerprint": 13085702229645769746,
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
    "model_sha256": "751adb8163a7ab389189b98273868852e7ba164f6ca91d082902a610f5c58977",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "ac3c34594b2170933cb2e75470e0a8f06dd50696589dcbda19cdd379ce27d048",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00017749506514519453,
          "p95": 0.0,
          "p99": 2.00001522898674e-07
        },
        "bias_percent": 0.030282219938408586,
        "identifier": "plan_t_circle_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3779049839741897,
        "worst_index": [
          38,
          485,
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
          "maximum": 0.0003364700824022293,
          "p95": 4.0936333789431956e-06,
          "p99": 3.051256135222502e-05
        },
        "bias_percent": 0.1483127060152576,
        "identifier": "plan_t_circle_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.996139966392411,
        "worst_index": [
          38,
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
          "maximum": 0.00026651937514543533,
          "p95": 3.732064215000719e-06,
          "p99": 2.8396345442160964e-05
        },
        "bias_percent": -0.08362622665359658,
        "identifier": "plan_t_circle_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.736585805348527,
        "worst_index": [
          22,
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
            "identifier": "plan_t_circle_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006416186224669218,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.127683006227016e-05
                },
                "candidate_energy": 2.3646317472193914,
                "cvrmse_percent": 95.97416668937032,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.36011773025368815,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.3731779819026997,
                "relative_energy_error_percent": 0.36011773025368815,
                "rms_normalized_rmse_percent": 8.944020278098256,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0014623114839196205,
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "reference": 0.0021039301063865423,
                  "rgb_channel": 0,
                  "sky_patch_index": 156
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008082566782832146,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00010767346248030663
                },
                "candidate_energy": 0.5746686566655441,
                "cvrmse_percent": 531.0971495084202,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.05279387862043531,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.5743654268792397,
                "relative_energy_error_percent": 0.0527938786204353,
                "rms_normalized_rmse_percent": 8.962290712744577,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00033687951508909464,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": -0.00047137716319411993,
                  "rgb_channel": 0,
                  "sky_patch_index": 483
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.41929189767689,
            "full": 307.80125001911074
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.47249996755272,
            "full": 305.73291704058647
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 126.78325001616031,
            "full": 299.704791046679
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.98250006139278,
            "full": 316.8396670371294
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
            "identifier": "plan_t_circle_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00028657843358814716,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.3794156732037663e-05
                },
                "candidate_energy": 2.371443289481249,
                "cvrmse_percent": 42.495358044549654,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.09145892692248708,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.36927637473309,
                "relative_energy_error_percent": 0.09145892692248708,
                "rms_normalized_rmse_percent": 3.968116529188748,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004548129625618458,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.004261551192030311,
                  "rgb_channel": 0,
                  "sky_patch_index": 447
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005201341409701854,
                  "p50": 0.0,
                  "p90": 2.513554022698372e-06,
                  "p95": 6.093446472732467e-06,
                  "p99": 6.470934022217989e-05
                },
                "candidate_energy": 1.0914037409561246,
                "cvrmse_percent": 145.4752277718689,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.6257609876875709,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.0982763257396115,
                "relative_energy_error_percent": 0.6257609876875709,
                "rms_normalized_rmse_percent": 3.812806269560656,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00011425247066654265,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.00040588167030364275,
                  "rgb_channel": 0,
                  "sky_patch_index": 89
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 164.37775001395494,
            "full": 3769.598333979957
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 164.198916987516,
            "full": 3741.7518330039456
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 164.6787910722196,
            "full": 3759.0685000177473
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 172.37804096657783,
            "full": 3778.9940839866176
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
            "identifier": "plan_t_circle_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00034011807292699814,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.428753163665533e-05
                },
                "candidate_energy": 2.371599682413944,
                "cvrmse_percent": 50.19339994258056,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.01779242247479246,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.372021722540012,
                "relative_energy_error_percent": 0.017792422474792458,
                "rms_normalized_rmse_percent": 4.692628193867774,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0035326045472174883,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.0038727226201444864,
                  "rgb_channel": 0,
                  "sky_patch_index": 312
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005270849796943367,
                  "p50": 0.0,
                  "p90": 2.4281627872824174e-06,
                  "p95": 6.160844350233674e-06,
                  "p99": 5.915772635489702e-05
                },
                "candidate_energy": 1.097237960255807,
                "cvrmse_percent": 151.08063328949717,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.2346752617000403,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.0998189632861255,
                "relative_energy_error_percent": 0.2346752617000403,
                "rms_normalized_rmse_percent": 3.9485004275679807,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00030074501410126686,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": -0.0002263399655930698,
                  "rgb_channel": 0,
                  "sky_patch_index": 152
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 165.95391696318984,
            "full": 4100.021916907281
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 166.17520910222083,
            "full": 4166.931916028261
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 170.81824992783368,
            "full": 4079.9797090003267
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 170.00683303922415,
            "full": 4128.453999990597
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
            "identifier": "plan_t_circle_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002192127431044355,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.3114436771720648e-05
                },
                "candidate_energy": 2.3710379238609676,
                "cvrmse_percent": 27.635885752251816,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.010552716670985072,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.3712881591818586,
                "relative_energy_error_percent": 0.010552716670985072,
                "rms_normalized_rmse_percent": 2.581903433541921,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0005305811500875279,
                  "global_sensor_index": 38,
                  "local_sensor_index": 38,
                  "reference": 0.00031136840698309243,
                  "rgb_channel": 0,
                  "sky_patch_index": 154
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003006600309163332,
                  "p50": 0.0,
                  "p90": 1.6784417766757542e-06,
                  "p95": 4.140165401622653e-06,
                  "p99": 3.883903264068067e-05
                },
                "candidate_energy": 1.0948886155692392,
                "cvrmse_percent": 90.2873019918168,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.25243144884472307,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.0976594532304098,
                "relative_energy_error_percent": 0.25243144884472307,
                "rms_normalized_rmse_percent": 2.3676058916763645,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0002205634955316782,
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "reference": -8.0096535384655e-05,
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 250.02570811193436,
            "full": 7261.512416996993
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 240.83200003951788,
            "full": 7245.364916976541
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 242.15575004927814,
            "full": 7219.7359999408945
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
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "54",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 240.6463329680264,
            "full": 7307.8182090539485
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/suite-0.3.1/run/plan_t_circle/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 6366.094208089635,
      "invocation_count": 4,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_circle/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 26114.322084002197,
      "invocation_count": 4,
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
      54,
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
        "identifier": "plan_t_circle_grid",
        "full_identifier": "plan_t_circle_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": -0.028355191314942546,
            "cvrmse_percent": 6.946423369088749,
            "rms_normalized_rmse_percent": 0.6491258847953467,
            "reference_energy": 2.370571228057429,
            "candidate_energy": 2.3698990480504563,
            "relative_energy_error_percent": 0.028355191314942543,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.174347173422575e-07,
              "maximum": 9.685126133263111e-05
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 485,
              "rgb_channel": 0,
              "reference": 0.001293012173846364,
              "candidate": 0.001196160912513733,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.3796906767619501,
            "cvrmse_percent": 83.43522220909352,
            "rms_normalized_rmse_percent": 2.1873558832542037,
            "reference_energy": 1.0968658458525908,
            "candidate_energy": 1.0817324900407765,
            "relative_energy_error_percent": 1.37969067676195,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.262457542201446e-06,
              "p95": 4.8744623200036585e-06,
              "p99": 2.1678082703147084e-05,
              "maximum": 0.0005868198350071907
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015373799949884415,
              "candidate": 0.014786980114877224,
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
            "nmbe_percent": -0.45582761797502547,
            "cvrmse_percent": 26.417652638240224,
            "rms_normalized_rmse_percent": 2.1893708012717217,
            "reference_energy": 3.4674370739100198,
            "candidate_energy": 3.451631538091233,
            "relative_energy_error_percent": 0.4558276179750254,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.2532653929374646e-06,
              "p95": 4.860953595198225e-06,
              "p99": 2.125135506503284e-05,
              "maximum": 0.0005868198350071907
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.015373799949884415,
              "candidate": 0.014786980114877224,
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
      54,
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
        "identifier": "plan_t_circle_grid",
        "full_identifier": "plan_t_circle_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": -0.028355191314942546,
            "cvrmse_percent": 6.946423369088749,
            "rms_normalized_rmse_percent": 0.6491258847953467,
            "reference_energy": 2.370571228057429,
            "candidate_energy": 2.3698990480504563,
            "relative_energy_error_percent": 0.028355191314942543,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.174347173422575e-07,
              "maximum": 9.685126133263111e-05
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 485,
              "rgb_channel": 0,
              "reference": 0.001293012173846364,
              "candidate": 0.001196160912513733,
              "position": [
                6.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 88.83324251050672,
            "cvrmse_percent": 1727.3369143848747,
            "rms_normalized_rmse_percent": 29.068681226841427,
            "reference_energy": 0.5728506674245075,
            "candidate_energy": 1.0817324900407765,
            "relative_energy_error_percent": 88.83324251050671,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.130000085453503e-06,
              "p95": 2.18700006371364e-05,
              "p99": 6.210999708855525e-05,
              "maximum": 0.006426094099879265
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017778465524315834,
              "candidate": 0.0242045596241951,
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
            "nmbe_percent": 17.265946257632407,
            "cvrmse_percent": 336.13893655528506,
            "rms_normalized_rmse_percent": 29.065526185653795,
            "reference_energy": 2.9434218954819364,
            "candidate_energy": 3.451631538091233,
            "relative_energy_error_percent": 17.26594625763241,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.130000085453503e-06,
              "p95": 2.183683682233095e-05,
              "p99": 6.153000140329823e-05,
              "maximum": 0.006426094099879265
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017778465524315834,
              "candidate": 0.0242045596241951,
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
      "bias_percent": -0.03802282558077267,
      "rms_normalized_error_percent": 0.14144989804917923,
      "absolute_error": {
        "p95": 0.03286572833010851,
        "p99": 0.04366155214442622,
        "maximum": 0.044724844476412784
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.01782298821142,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.14144989804917923
    },
    "overcast": {
      "bias_percent": -0.03976668078079207,
      "rms_normalized_error_percent": 0.11682388235817356,
      "absolute_error": {
        "p95": 0.021307533979415882,
        "p99": 0.02904970169067382,
        "maximum": 0.03218650817871094
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.0411107540130615,
      "reference_fraction_of_uniform": 0.6763520240783691,
      "rms_normalized_to_uniform_percent": 0.08616782716190201
    },
    "horizon": {
      "bias_percent": -0.5315902449525163,
      "rms_normalized_error_percent": 2.4173596449032826,
      "absolute_error": {
        "p95": 0.022339128211260478,
        "p99": 0.03409274378018126,
        "maximum": 0.034273625000615815
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.2604092850172522,
      "reference_fraction_of_uniform": 0.08629044381810795,
      "rms_normalized_to_uniform_percent": 0.10832968898266579
    },
    "north": {
      "bias_percent": -53.88583169685028,
      "rms_normalized_error_percent": 131.28332665565756,
      "absolute_error": {
        "p95": 7.40101405028781e-05,
        "p99": 0.0001545794127218869,
        "maximum": 0.00016302755989272555
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 8.847589924698696e-06,
      "reference_fraction_of_uniform": 2.9317789085325785e-06,
      "rms_normalized_to_uniform_percent": 0.0003601568431905551
    },
    "east": {
      "bias_percent": -0.19230777788686748,
      "rms_normalized_error_percent": 0.164418312269544,
      "absolute_error": {
        "p95": 0.008167046308517452,
        "p99": 0.011557794660329811,
        "maximum": 0.014610230922698975
      },
      "worst_index": [
        37
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.45581477880477905,
      "reference_fraction_of_uniform": 0.1510409265756607,
      "rms_normalized_to_uniform_percent": 0.0367424330946691
    },
    "south": {
      "bias_percent": -0.011814684043413059,
      "rms_normalized_error_percent": 0.16854578560934844,
      "absolute_error": {
        "p95": 0.023854959011077852,
        "p99": 0.03177017927169799,
        "maximum": 0.03416562080383301
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.1225881576538086,
      "reference_fraction_of_uniform": 0.7033507823944092,
      "rms_normalized_to_uniform_percent": 0.10673633480328913
    },
    "west": {
      "bias_percent": -0.01288355160534961,
      "rms_normalized_error_percent": 0.2071685427786851,
      "absolute_error": {
        "p95": 0.007268106192350379,
        "p99": 0.019915655851364133,
        "maximum": 0.021869778633117676
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.46070802211761475,
      "reference_fraction_of_uniform": 0.15266238152980804,
      "rms_normalized_to_uniform_percent": 0.046531412821339144
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
        "identifier": "plan_t_circle_grid",
        "sensor_count": 54,
        "illuminance": {
          "nmbe_percent": -0.057281865351695216,
          "cvrmse_percent": 3.0359732687815764,
          "absolute_error_percentiles_lux": {
            "p50": 0.33164167404174805,
            "p90": 5.520907592773438,
            "p95": 11.186032104492181,
            "p99": 35.70621337890621
          },
          "maximum_absolute_error_lux": 398.650390625,
          "worst": {
            "sensor_index": 37,
            "position": [
              6.5,
              1.5,
              0.75
            ],
            "hour_of_year": 1356.5,
            "foton_lux": 17636.658203125,
            "radiance_lux": 17238.0078125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.076834094368341,
            "maximum_error_percentage_points": 1.2049315068493147,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.17973088576378288,
            "maximum_error_percentage_points": 0.9827238983458884,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.22481988838153186,
            "maximum_error_percentage_points": 2.0782191780821933,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.2262455606291222,
            "maximum_error_percentage_points": 2.0782191780821897,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.003688483003551466,
            "maximum_error_percentage_points": 0.08698630136986196,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 11.11111111111111,
          "radiance_percent": 11.11111111111111,
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
      "maximum_error_percentage_points": 0.0049692148705050565,
      "metrics": {
        "da": [
          {
            "identifier": "plan_t_circle_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_t_circle_grid",
            "maximum_error_percentage_points": 0.0049692148705050565,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_t_circle_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_t_circle_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_t_circle_grid",
            "maximum_error_percentage_points": 0.004794520547942938,
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
      "study_preparation_seconds": 0.006911374977789819,
      "weather_seconds": 0.09933720901608467,
      "metric_reduction_seconds": 0.14811900001950562,
      "write_seconds": 0.05127954203635454,
      "total_seconds": 0.29889612493570894,
      "cold_end_to_end_seconds": 0.30580749991349876,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.03140262502711266,
      "engine_upload_seconds": 0.000871708,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.09053879149723798,
      "engine_annual_reduction_seconds": 0.0023320000618696213,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.09053879149723798
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006911374977789819,
      "weather_seconds": 0.10250837495550513,
      "metric_reduction_seconds": 0.04661850002594292,
      "write_seconds": 0.03364283300470561,
      "total_seconds": 0.18292849999852479,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.18292849999852479,
      "raw_export_seconds": 0.011796665959991515,
      "engine_upload_seconds": 8.4416e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.002350333263166249,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.012058416963554919,
      "full": 0.09362925007008016
    }
  },
  "elapsed_seconds": 1.4561966670444235,
  "result_class": "passed"
}
```
