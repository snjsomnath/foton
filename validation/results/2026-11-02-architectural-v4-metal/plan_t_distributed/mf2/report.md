# Foton report

Status: **passed**

```json
{
  "scene": "plan_t_distributed",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_t_distributed",
    "category": "form",
    "question": "How does a distributed opening illuminate a T-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "t",
    "window_profile": "distributed"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 8,
    "shades": 0,
    "sensors": 54,
    "floor_area": 63.0,
    "aperture_area": 9.6
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "dd1d4f849dc3aea9d90f21a79d3aad5b55500ff51f60747f6fd09c84734a140b",
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
      "scene_fingerprint": 15359727019794020790,
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
      "scene_fingerprint": 15359727019794020790,
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
        "identifier": "plan_t_distributed_grid",
        "bias_percent": 0.023576823718254328,
        "rms_normalized_error_percent": 0.8984624597009108,
        "absolute_error": {
          "p95": 2.7839014364872128e-06,
          "p99": 2.2931082639843225e-05,
          "maximum": 0.00014044740237295628
        },
        "worst_index": [
          24,
          333,
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
        "identifier": "plan_t_distributed_grid",
        "bias_percent": 0.02518854019893455,
        "rms_normalized_error_percent": 1.5184141283023798,
        "absolute_error": {
          "p95": 4.948384594172239e-05,
          "p99": 0.00011969858314841986,
          "maximum": 0.0006306841969490051
        },
        "worst_index": [
          45,
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
        "identifier": "plan_t_distributed_grid",
        "bias_percent": 0.011918293930366001,
        "rms_normalized_error_percent": 1.2207061910629884,
        "absolute_error": {
          "p95": 4.0373968658968806e-05,
          "p99": 9.61225014179945e-05,
          "maximum": 0.0005580037832260132
        },
        "worst_index": [
          45,
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
            "identifier": "plan_t_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 54,
            "stages": {
              "direct": {
                "nmbe_percent": -0.08312892085894111,
                "cvrmse_percent": 26.91465461793566,
                "rms_normalized_rmse_percent": 6.849944706854719,
                "reference_energy": 15.787157172368072,
                "candidate_energy": 15.774033478976378,
                "relative_energy_error_percent": 0.08312892085894112,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.196951001882553e-05,
                  "p95": 9.250477887690067e-05,
                  "p99": 0.00023260049056261778,
                  "maximum": 0.0006307640578597784
                },
                "worst": {
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "sky_patch_index": 311,
                  "rgb_channel": 0,
                  "reference": 0.004119622055441141,
                  "candidate": 0.0034888579975813627
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.7919293488142589,
                "cvrmse_percent": 136.97698456353902,
                "rms_normalized_rmse_percent": 5.574057157940031,
                "reference_energy": 4.703249998779793,
                "candidate_energy": 4.740496415868236,
                "relative_energy_error_percent": 0.7919293488142589,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.6248023863881826e-05,
                  "p95": 0.00013925053644925356,
                  "p99": 0.00034380704164505005,
                  "maximum": 0.0013265898451209068
                },
                "worst": {
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.029692400246858597,
                  "candidate": 0.02836581040173769
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 150.24937503039837,
            "full": 331.427791970782
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 139.34691692702472,
            "full": 338.16612500231713
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 143.07795802596956,
            "full": 328.59966706018895
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 139.73862503189594,
            "full": 326.8746250541881
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
            "identifier": "plan_t_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 54,
            "stages": {
              "direct": {
                "nmbe_percent": -0.03519289399100002,
                "cvrmse_percent": 18.898697383039174,
                "rms_normalized_rmse_percent": 4.811548732215028,
                "reference_energy": 15.773344621128249,
                "candidate_energy": 15.7677935246769,
                "relative_energy_error_percent": 0.03519289399100003,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.1536106942221522e-05,
                  "p95": 6.807642057538033e-05,
                  "p99": 0.00016266369493678212,
                  "maximum": 0.0004243723815307021
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 269,
                  "rgb_channel": 0,
                  "reference": 0.0033656179439276457,
                  "candidate": 0.0029412455623969436
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.009517502869649403,
                "cvrmse_percent": 50.646619696191365,
                "rms_normalized_rmse_percent": 2.842442359696983,
                "reference_energy": 8.910877441202476,
                "candidate_energy": 8.910029348186299,
                "relative_energy_error_percent": 0.009517502869649403,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.644848104362609e-06,
                  "p90": 3.631003346526995e-05,
                  "p95": 9.654543828219175e-05,
                  "p99": 0.00023863476235419512,
                  "maximum": 0.0007145237177610397
                },
                "worst": {
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03380658105015755,
                  "candidate": 0.03452110476791859
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 203.81966698914766,
            "full": 3951.756792026572
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 201.97950000874698,
            "full": 3941.849666996859
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 200.83091710694134,
            "full": 3909.214042010717
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 201.822999981232,
            "full": 3886.704000062309
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
            "identifier": "plan_t_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 54,
            "stages": {
              "direct": {
                "nmbe_percent": 0.018073193878992706,
                "cvrmse_percent": 18.609421402773457,
                "rms_normalized_rmse_percent": 4.736800127469554,
                "reference_energy": 15.770934355088418,
                "candidate_energy": 15.773784666630942,
                "relative_energy_error_percent": 0.018073193878992706,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.2038468159735203e-05,
                  "p95": 6.82625686749816e-05,
                  "p99": 0.0001617142916074954,
                  "maximum": 0.00045904936268925667
                },
                "worst": {
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "sky_patch_index": 364,
                  "rgb_channel": 0,
                  "reference": 0.004041307372972369,
                  "candidate": 0.0035822580102831125
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.02561088835579554,
                "cvrmse_percent": 51.57683875733462,
                "rms_normalized_rmse_percent": 2.8940877298644523,
                "reference_energy": 8.913738225676237,
                "candidate_energy": 8.916021113221543,
                "relative_energy_error_percent": 0.025610888355795544,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.749764229927678e-06,
                  "p90": 3.776676021516323e-05,
                  "p95": 0.00010117050260305405,
                  "p99": 0.00023861629597377032,
                  "maximum": 0.0011140909045934677
                },
                "worst": {
                  "global_sensor_index": 50,
                  "local_sensor_index": 50,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.045845380052924156,
                  "candidate": 0.04473128914833069
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 211.0622499603778,
            "full": 4090.792916016653
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 200.78674994874746,
            "full": 4113.33670897875
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 196.90708303824067,
            "full": 4408.345625037327
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 203.34358396939933,
            "full": 4103.266916936263
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
            "identifier": "plan_t_distributed_grid",
            "start_sensor_index": 0,
            "sensor_count": 54,
            "stages": {
              "direct": {
                "nmbe_percent": 0.01877925994086907,
                "cvrmse_percent": 10.48377840363412,
                "rms_normalized_rmse_percent": 2.669646798399786,
                "reference_energy": 15.771863103370379,
                "candidate_energy": 15.774824942540079,
                "relative_energy_error_percent": 0.018779259940869066,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.112715654016938e-05,
                  "p95": 3.5232267691753805e-05,
                  "p99": 9.120709728449583e-05,
                  "maximum": 0.00022667995654046535
                },
                "worst": {
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "sky_patch_index": 486,
                  "rgb_channel": 0,
                  "reference": 0.0040876304265111685,
                  "candidate": 0.004314310383051634
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.05634780784532488,
                "cvrmse_percent": 29.123221716922316,
                "rms_normalized_rmse_percent": 1.6356067395709202,
                "reference_energy": 8.919350388195777,
                "candidate_energy": 8.914324529777986,
                "relative_energy_error_percent": 0.05634780784532488,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.3486674055893673e-06,
                  "p90": 2.2634005290456116e-05,
                  "p95": 5.698757013306022e-05,
                  "p99": 0.00013218598905950785,
                  "maximum": 0.0005945395678281784
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03549553081393242,
                  "candidate": 0.0360900703817606
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 331.6043330123648,
            "full": 7384.67399997171
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 326.02341601159424,
            "full": 7281.521250028163
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 318.81079101003706,
            "full": 7210.585708031431
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 323.56400007847697,
            "full": 7248.7180000171065
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 6476.908500073478,
      "worker_pool_size": 12,
      "invocation_count": 4
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/plan_t_distributed/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 25632.479166029952,
      "worker_pool_size": 12,
      "invocation_count": 4
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
        "identifier": "plan_t_distributed_grid",
        "full_identifier": "plan_t_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": -0.18116726623292298,
            "cvrmse_percent": 3.238713163396713,
            "rms_normalized_rmse_percent": 0.8246752902814263,
            "reference_energy": 15.772856184677977,
            "candidate_energy": 15.744280932321345,
            "relative_energy_error_percent": 0.18116726623292298,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.008202373981476e-08,
              "p95": 3.3137621358036995e-06,
              "p99": 2.1469881176017225e-05,
              "maximum": 0.00015418848488479853
            },
            "worst": {
              "global_sensor_index": 44,
              "local_sensor_index": 44,
              "sky_patch_index": 141,
              "rgb_channel": 0,
              "reference": 0.0015848726034164429,
              "candidate": 0.0014306841185316443,
              "position": [
                8.5,
                9.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.5834380287617632,
            "cvrmse_percent": 58.0677753551347,
            "rms_normalized_rmse_percent": 3.26126018593045,
            "reference_energy": 8.917325342422911,
            "candidate_energy": 8.865298275226806,
            "relative_energy_error_percent": 0.5834380287617633,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.4405750931700823e-05,
              "p90": 4.750189327751286e-05,
              "p95": 6.504031989607029e-05,
              "p99": 0.00011489312601042911,
              "maximum": 0.0024579837918281555
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.042334672063589096,
              "candidate": 0.03987668827176094,
              "position": [
                6.5,
                4.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.32645494916375895,
            "cvrmse_percent": 20.91237575552882,
            "rms_normalized_rmse_percent": 3.251945850600376,
            "reference_energy": 24.69018152710089,
            "candidate_energy": 24.60957920754815,
            "relative_energy_error_percent": 0.3264549491637661,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.4379891581484117e-05,
              "p90": 4.723878009826876e-05,
              "p95": 6.427492917282507e-05,
              "p99": 0.00011308288958389312,
              "maximum": 0.0024579837918281555
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.042334672063589096,
              "candidate": 0.03987668827176094,
              "position": [
                6.5,
                4.5,
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
        "identifier": "plan_t_distributed_grid",
        "full_identifier": "plan_t_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": -0.18116726623292298,
            "cvrmse_percent": 3.238713163396713,
            "rms_normalized_rmse_percent": 0.8246752902814263,
            "reference_energy": 15.772856184677977,
            "candidate_energy": 15.744280932321345,
            "relative_energy_error_percent": 0.18116726623292298,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.008202373981476e-08,
              "p95": 3.3137621358036995e-06,
              "p99": 2.1469881176017225e-05,
              "maximum": 0.00015418848488479853
            },
            "worst": {
              "global_sensor_index": 44,
              "local_sensor_index": 44,
              "sky_patch_index": 141,
              "rgb_channel": 0,
              "reference": 0.0015848726034164429,
              "candidate": 0.0014306841185316443,
              "position": [
                8.5,
                9.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 87.44238516407583,
            "cvrmse_percent": 1009.7500055100628,
            "rms_normalized_rmse_percent": 41.31704044808168,
            "reference_energy": 4.729612391277808,
            "candidate_energy": 8.865298275226806,
            "relative_energy_error_percent": 87.44238516407583,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.596000038261991e-05,
              "p90": 7.780690248182509e-05,
              "p95": 0.00010933051817119122,
              "p99": 0.0001978105865418911,
              "maximum": 0.016408627852797508
            },
            "worst": {
              "global_sensor_index": 51,
              "local_sensor_index": 51,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.019733870401978493,
              "candidate": 0.036142498254776,
              "position": [
                11.5,
                11.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.032273754629568,
            "cvrmse_percent": 232.91817452778747,
            "rms_normalized_rmse_percent": 41.314197713107774,
            "reference_energy": 20.50246857595579,
            "candidate_energy": 24.60957920754815,
            "relative_energy_error_percent": 20.032273754629554,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.5878706733474246e-05,
              "p90": 7.742999878246337e-05,
              "p95": 0.00010860677321034018,
              "p99": 0.00019593839533627033,
              "maximum": 0.016408627852797508
            },
            "worst": {
              "global_sensor_index": 51,
              "local_sensor_index": 51,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.019733870401978493,
              "candidate": 0.036142498254776,
              "position": [
                11.5,
                11.5,
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
      "bias_percent": -0.12361383553082178,
      "rms_normalized_error_percent": 0.4435827577577992,
      "absolute_error": {
        "p95": 0.2523951793774447,
        "p99": 0.26404194740119746,
        "maximum": 0.2681730035335761
      },
      "worst_index": [
        52
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 20.64088141714722,
      "rms_normalized_to_uniform_percent": 0.4435827577577992
    },
    "overcast": {
      "bias_percent": -0.07193019652657236,
      "rms_normalized_error_percent": 0.3900988491573641,
      "absolute_error": {
        "p95": 0.12893729209899896,
        "p99": 0.1705590724945068,
        "maximum": 0.18352127075195312
      },
      "worst_index": [
        52
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 13.319330215454102,
      "rms_normalized_to_uniform_percent": 0.2672756814126367
    },
    "horizon": {
      "bias_percent": -0.36723587377650396,
      "rms_normalized_error_percent": 3.582275575586652,
      "absolute_error": {
        "p95": 0.1398589115765763,
        "p99": 0.16706630632067118,
        "maximum": 0.1882335901134875
      },
      "worst_index": [
        38
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.0946507077944005,
      "rms_normalized_to_uniform_percent": 0.2901878109348504
    },
    "north": {
      "bias_percent": 0.06339870101538445,
      "rms_normalized_error_percent": 0.7688927631818816,
      "absolute_error": {
        "p95": 0.08452251851558677,
        "p99": 0.13031200885772698,
        "maximum": 0.1673731803894043
      },
      "worst_index": [
        50
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.874572992324829,
      "rms_normalized_to_uniform_percent": 0.19068666740130555
    },
    "east": {
      "bias_percent": -0.31323031942748436,
      "rms_normalized_error_percent": 0.6816002337975936,
      "absolute_error": {
        "p95": 0.11119130849838256,
        "p99": 0.13423762321472169,
        "maximum": 0.13520050048828125
      },
      "worst_index": [
        52
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 5.441839218139648,
      "rms_normalized_to_uniform_percent": 0.23106839101748927
    },
    "south": {
      "bias_percent": -0.17243720005436455,
      "rms_normalized_error_percent": 0.546914728741682,
      "absolute_error": {
        "p95": 0.11983265876770015,
        "p99": 0.14608199715614315,
        "maximum": 0.16411781311035156
      },
      "worst_index": [
        45
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 7.3076300621032715,
      "rms_normalized_to_uniform_percent": 0.2253246723604039
    },
    "west": {
      "bias_percent": -0.14810613042687307,
      "rms_normalized_error_percent": 0.4957741546218892,
      "absolute_error": {
        "p95": 0.09061524868011472,
        "p99": 0.09813670635223387,
        "maximum": 0.10384750366210938
      },
      "worst_index": [
        0
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 5.478924751281738,
      "rms_normalized_to_uniform_percent": 0.16860970063108408
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
        "identifier": "plan_t_distributed_grid",
        "sensor_count": 54,
        "illuminance": {
          "nmbe_percent": -0.08782810468039755,
          "cvrmse_percent": 4.022970714408396,
          "absolute_error_percentiles_lux": {
            "p50": 14.601604461669922,
            "p90": 87.92878723144531,
            "p95": 123.34286499023438,
            "p99": 211.3202386474609
          },
          "maximum_absolute_error_lux": 749.52099609375,
          "worst": {
            "sensor_index": 5,
            "position": [
              1.5,
              9.5,
              0.75
            ],
            "hour_of_year": 3540.5,
            "foton_lux": 2167.417236328125,
            "radiance_lux": 1417.896240234375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.4348325722983254,
            "maximum_error_percentage_points": 4.467945205479452,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.16804709261897383,
            "maximum_error_percentage_points": 1.5877021986273405,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.10532724505327228,
            "maximum_error_percentage_points": 0.6612328767123259,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.1363926940639266,
            "maximum_error_percentage_points": 0.6598630136986401,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.05156265854895998,
            "maximum_error_percentage_points": 0.2779452054794529,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 98.14814814814815,
          "radiance_percent": 100.0,
          "difference_percentage_points": 1.8518518518518476,
          "tolerance_percentage_points": 2.0,
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
      "maximum_error_percentage_points": 0.00497163955479607,
      "metrics": {
        "da": [
          {
            "identifier": "plan_t_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_t_distributed_grid",
            "maximum_error_percentage_points": 0.00497163955479607,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_t_distributed_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_t_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_t_distributed_grid",
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
      "study_preparation_seconds": 0.008586499956436455,
      "weather_seconds": 0.11540908296592534,
      "metric_reduction_seconds": 0.07507233298383653,
      "write_seconds": 0.04419708298519254,
      "total_seconds": 0.23481854191049933,
      "cold_end_to_end_seconds": 0.2434050418669358,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.016722582979127765,
      "engine_upload_seconds": 0.000832625,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.024413541657850146,
      "engine_annual_reduction_seconds": 0.002316458383575082,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.024413541657850146
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.008586499956436455,
      "weather_seconds": 0.1089559169486165,
      "metric_reduction_seconds": 0.04415429092478007,
      "write_seconds": 0.035970250028185546,
      "total_seconds": 0.18924441700801253,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.18924441700801253,
      "raw_export_seconds": 0.01040195906534791,
      "engine_upload_seconds": 8.175e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0023220833390951157,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.018991874996572733,
      "full": 0.02277091599535197
    }
  },
  "elapsed_seconds": 101.1806009169668,
  "result_class": "passed"
}
```
