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
  "model_sha256": "0a83f90fff73e119aba1eb96c518af4ebd491c7f53bd89a5c41d7d86343c1e63",
  "weather_sha256": "98246499f5e0508387c41d22a6f492c76a8ec52c17ceb31712069871a196bcee",
  "gpu_executed": true,
  "candidate": {
    "capabilities": {
      "name": "Vulkan device: Tesla T4",
      "hardware_acceleration": true,
      "supports_ray_tracing": true,
      "supports_async_jobs": true
    },
    "direct": {
      "metric_label": "static_sDA300_50",
      "solver_version": "0.3.5",
      "scene_fingerprint": 15359727019794020790,
      "basis": "ReinhartMf2",
      "quality": "Final",
      "glazing_model": "radiance_thin_glass_non_refracting",
      "schedule_timestep_count": 1,
      "direct_sample_count": 256,
      "convergence": 1.0,
      "transport_backend": "vulkan",
      "used_reference_fallback": false
    },
    "full": {
      "metric_label": "static_sDA300_50",
      "solver_version": "0.3.5",
      "scene_fingerprint": 15359727019794020790,
      "basis": "ReinhartMf2",
      "quality": "Final",
      "glazing_model": "radiance_thin_glass_non_refracting",
      "schedule_timestep_count": 1,
      "direct_sample_count": 256,
      "convergence": 1.0,
      "transport_backend": "vulkan",
      "used_reference_fallback": false
    }
  },
  "sky_bin_audit": {
    "passed": true,
    "ray_count": 9248,
    "command": [
      "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/rcalc",
      "-e",
      "MF:2",
      "-f",
      "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/lib/reinhart.cal",
      "-e",
      "Dx=$1;Dy=$2;Dz=$3;$1=rbin"
    ],
    "calibration_sha256": "92b8c09984de7a551773530b3146ba79a51e1b003245f230b6e7b430eb6c26cd"
  },
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.5)",
      "weather_id": "82c544d76aea9710a570440071d4833104fdc7da7504bac286ac2afe42bdd614"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/gendaymtx",
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
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "1af1d0674993c2b846c34bc8cb29d3afcad438ff30fdb5a0242b1043fdf27d56",
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
          "maximum": 0.00014044740237295628,
          "p95": 2.7839014364872128e-06,
          "p99": 2.2931082639843225e-05
        },
        "bias_percent": 0.023579238888071327,
        "identifier": "plan_t_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8984624100039241,
        "worst_index": [
          24,
          333,
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
          "maximum": 0.0006569698452949524,
          "p95": 4.889070987701416e-05,
          "p99": 0.00012048054486513138
        },
        "bias_percent": -0.01859494432676883,
        "identifier": "plan_t_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.5332650986704133,
        "worst_index": [
          28,
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
          "maximum": 0.0005294792354106903,
          "p95": 4.127644933760166e-05,
          "p99": 0.00010038760956376791
        },
        "bias_percent": 0.002662131825295153,
        "identifier": "plan_t_distributed_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3022580091869627,
        "worst_index": [
          3,
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
            "identifier": "plan_t_distributed_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007464060909114778,
                  "p50": 0.0,
                  "p90": 3.236524935346097e-05,
                  "p95": 9.289052104577422e-05,
                  "p99": 0.0002356140175834298
                },
                "candidate_energy": 15.769444700385744,
                "cvrmse_percent": 28.21247636612544,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.026633867866642548,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 15.765245805649016,
                "relative_energy_error_percent": 0.026633867866642544,
                "rms_normalized_rmse_percent": 7.17296670860851,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002144747064448893,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.0013983409735374153,
                  "rgb_channel": 0,
                  "sky_patch_index": 169
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011369651183485985,
                  "p50": 0.0,
                  "p90": 4.601902037393302e-05,
                  "p95": 0.00014021259266883135,
                  "p99": 0.0003647015546448529
                },
                "candidate_energy": 4.72843661386807,
                "cvrmse_percent": 142.03846918500656,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.4169482027982496,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.748234291410757,
                "relative_energy_error_percent": 0.4169482027982496,
                "rms_normalized_rmse_percent": 5.827623350174684,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02947189472615719,
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "reference": 0.02833492960780859,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.99587498884648,
            "full": 348.0022919829935
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.5111670549959,
            "full": 339.24850006587803
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.33974999096245,
            "full": 332.3723330395296
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.2994999922812,
            "full": 334.520542062819
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
            "identifier": "plan_t_distributed_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004219035618007183,
                  "p50": 0.0,
                  "p90": 2.2103475203039125e-05,
                  "p95": 6.95795170031488e-05,
                  "p99": 0.00016214264906011522
                },
                "candidate_energy": 15.775419059012481,
                "cvrmse_percent": 19.11298395007576,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.01378059604026079,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 15.777593305410775,
                "relative_energy_error_percent": 0.013780596040260789,
                "rms_normalized_rmse_percent": 4.867250735091022,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0034779359120875597,
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "reference": 0.003899839473888278,
                  "rgb_channel": 0,
                  "sky_patch_index": 328
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006390325725078583,
                  "p50": 4.708454980573151e-06,
                  "p90": 3.654684405773878e-05,
                  "p95": 9.863986633718014e-05,
                  "p99": 0.0002393699251115322
                },
                "candidate_energy": 8.911737641711582,
                "cvrmse_percent": 50.548203718255365,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.05870212111846187,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.91697209346999,
                "relative_energy_error_percent": 0.05870212111846187,
                "rms_normalized_rmse_percent": 2.838738049780049,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03656519390642643,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.03592616133391857,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 205.23391698952764,
            "full": 3884.965959005058
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 209.9497920135036,
            "full": 3872.015833039768
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 216.45033301319927,
            "full": 3833.6076250998303
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 211.62533306051046,
            "full": 3902.016666950658
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
            "identifier": "plan_t_distributed_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003698590735439211,
                  "p50": 0.0,
                  "p90": 2.2027932573109865e-05,
                  "p95": 6.838003173470497e-05,
                  "p99": 0.00016208860324695706
                },
                "candidate_energy": 15.778490424488638,
                "cvrmse_percent": 18.94411094017117,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.03474470846088721,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 15.773010138100648,
                "relative_energy_error_percent": 0.0347447084608872,
                "rms_normalized_rmse_percent": 4.823222338621533,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0012704484979622066,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.0009005894244182855,
                  "rgb_channel": 0,
                  "sky_patch_index": 87
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008607301861047745,
                  "p50": 4.680061124417989e-06,
                  "p90": 3.61842212441843e-05,
                  "p95": 0.00010075594764202833,
                  "p99": 0.0002419933443889022
                },
                "candidate_energy": 8.913200669012042,
                "cvrmse_percent": 52.13636326950799,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.060198653346965995,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.907838270330977,
                "relative_energy_error_percent": 0.060198653346966,
                "rms_normalized_rmse_percent": 2.9276830994662357,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03622627072036266,
                  "global_sensor_index": 44,
                  "local_sensor_index": 44,
                  "reference": 0.03536554053425789,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 208.8591669453308,
            "full": 4157.912458991632
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 205.19745897036046,
            "full": 4026.6280830837786
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 212.77916699182242,
            "full": 4031.199207995087
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 217.3842090414837,
            "full": 4135.603709029965
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
            "identifier": "plan_t_distributed_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00022994843311607838,
                  "p50": 0.0,
                  "p90": 1.1337906471453607e-05,
                  "p95": 3.5239290809840895e-05,
                  "p99": 9.176903404295444e-05
                },
                "candidate_energy": 15.773791503813761,
                "cvrmse_percent": 10.558079667062183,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0020148915638453432,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 15.773473685423149,
                "relative_energy_error_percent": 0.002014891563845343,
                "rms_normalized_rmse_percent": 2.689246571001249,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002182243042625487,
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "reference": 0.0024121914757415652,
                  "rgb_channel": 0,
                  "sky_patch_index": 229
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000776359811425209,
                  "p50": 3.3305029774055583e-06,
                  "p90": 2.2625191832048586e-05,
                  "p95": 5.4793403251096606e-05,
                  "p99": 0.0001315240515395999
                },
                "candidate_energy": 8.914942110904533,
                "cvrmse_percent": 29.649315163704667,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.03698108842531437,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.911646487037011,
                "relative_energy_error_percent": 0.036981088425314376,
                "rms_normalized_rmse_percent": 1.664573504306609,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04176902957260609,
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "reference": 0.04099266976118088,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 345.2946670586243,
            "full": 7175.936124986038
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 325.26774995494634,
            "full": 7259.844249929301
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 320.659292046912,
            "full": 7148.093500058167
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 329.71054199151695,
            "full": 7184.921749983914
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
    "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/oconv",
    "/content/suite-vulkan/plan_t_distributed/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 6389.526958926581,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_distributed/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 25823.9285829477,
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
        "identifier": "plan_t_distributed_grid",
        "full_identifier": "plan_t_distributed_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": -0.181169415845402,
            "cvrmse_percent": 3.239441771665923,
            "rms_normalized_rmse_percent": 0.8248608190022455,
            "reference_energy": 15.772856235204046,
            "candidate_energy": 15.744280643700591,
            "relative_energy_error_percent": 0.181169415845402,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.008202373981476e-08,
              "p95": 3.322900738567114e-06,
              "p99": 2.146991027984768e-05,
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
            "nmbe_percent": -0.23325889328390487,
            "cvrmse_percent": 21.77077773694521,
            "rms_normalized_rmse_percent": 1.2225598319331756,
            "reference_energy": 8.914070691653482,
            "candidate_energy": 8.893277829011586,
            "relative_energy_error_percent": 0.2332588932839049,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.032290235045366e-06,
              "p90": 1.646280725253746e-05,
              "p95": 2.684793435037136e-05,
              "p99": 6.165984086692333e-05,
              "maximum": 0.0008894037455320358
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.030152464285492897,
              "candidate": 0.02926306053996086,
              "position": [
                6.5,
                7.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.1999781272558509,
            "cvrmse_percent": 7.6898282032620395,
            "rms_normalized_rmse_percent": 1.1959245294368759,
            "reference_energy": 24.686926926857527,
            "candidate_energy": 24.63755847271218,
            "relative_energy_error_percent": 0.1999781272558437,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.006064955319744e-06,
              "p90": 1.611188054084778e-05,
              "p95": 2.581800799816847e-05,
              "p99": 5.7479424867779016e-05,
              "maximum": 0.0008894037455320358
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.030152464285492897,
              "candidate": 0.02926306053996086,
              "position": [
                6.5,
                7.5,
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
            "nmbe_percent": -0.181169415845402,
            "cvrmse_percent": 3.239441771665923,
            "rms_normalized_rmse_percent": 0.8248608190022455,
            "reference_energy": 15.772856235204046,
            "candidate_energy": 15.744280643700591,
            "relative_energy_error_percent": 0.181169415845402,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.008202373981476e-08,
              "p95": 3.322900738567114e-06,
              "p99": 2.146991027984768e-05,
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
            "nmbe_percent": 87.90635360392984,
            "cvrmse_percent": 1010.7712224978019,
            "rms_normalized_rmse_percent": 41.37326525560308,
            "reference_energy": 4.73282444070885,
            "candidate_energy": 8.893277829011586,
            "relative_energy_error_percent": 87.90635360392984,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.1247749828035012e-05,
              "p90": 5.479693572851829e-05,
              "p95": 7.830956019461155e-05,
              "p99": 0.0001715654507279396,
              "maximum": 0.015176646411418915
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.019482683390378952,
              "candidate": 0.03465932980179787,
              "position": [
                0.5,
                11.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.14991778182138,
            "cvrmse_percent": 233.27561198728168,
            "rms_normalized_rmse_percent": 41.37043251514129,
            "reference_energy": 20.505680675912892,
            "candidate_energy": 24.63755847271218,
            "relative_energy_error_percent": 20.149917781821404,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.114000017172657e-05,
              "p90": 5.454070969790337e-05,
              "p95": 7.670715058338828e-05,
              "p99": 0.0001681133871898055,
              "maximum": 0.015176646411418915
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.019482683390378952,
              "candidate": 0.03465932980179787,
              "position": [
                0.5,
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
      "bias_percent": -0.04348920260032674,
      "rms_normalized_error_percent": 0.22182432626709656,
      "absolute_error": {
        "p95": 0.12425614011223796,
        "p99": 0.1751623877015072,
        "maximum": 0.18991694616020993
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 20.639173757244766,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.22182432626709656
    },
    "overcast": {
      "bias_percent": -0.02539494369811858,
      "rms_normalized_error_percent": 0.16706663885601564,
      "absolute_error": {
        "p95": 0.06010289192199706,
        "p99": 0.09020652770996092,
        "maximum": 0.1001739501953125
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 13.319239616394043,
      "reference_fraction_of_uniform": 0.6453378200531006,
      "rms_normalized_to_uniform_percent": 0.11445993464848017
    },
    "horizon": {
      "bias_percent": -0.11363717964171628,
      "rms_normalized_error_percent": 1.4955522625529805,
      "absolute_error": {
        "p95": 0.0652594333861682,
        "p99": 0.08305611660767404,
        "maximum": 0.09038205496537843
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.091364298988797,
      "reference_fraction_of_uniform": 0.10132984602906818,
      "rms_normalized_to_uniform_percent": 0.12094801816184512
    },
    "north": {
      "bias_percent": -0.1399388370804813,
      "rms_normalized_error_percent": 0.30305196594784317,
      "absolute_error": {
        "p95": 0.04310504198074338,
        "p99": 0.06670004487037658,
        "maximum": 0.07463550567626953
      },
      "worst_index": [
        47
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.876970052719116,
      "reference_fraction_of_uniform": 0.18784521520137787,
      "rms_normalized_to_uniform_percent": 0.07519237657853278
    },
    "east": {
      "bias_percent": -0.06997260592358084,
      "rms_normalized_error_percent": 0.2609696870357165,
      "absolute_error": {
        "p95": 0.036177515983581536,
        "p99": 0.0860200023651123,
        "maximum": 0.08836174011230469
      },
      "worst_index": [
        47
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.442607879638672,
      "reference_fraction_of_uniform": 0.2637028098106384,
      "rms_normalized_to_uniform_percent": 0.0884827549819603
    },
    "south": {
      "bias_percent": 0.08776778755808047,
      "rms_normalized_error_percent": 0.28177797717946373,
      "absolute_error": {
        "p95": 0.06493558883666968,
        "p99": 0.10187309265136717,
        "maximum": 0.11020994186401367
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.304484844207764,
      "reference_fraction_of_uniform": 0.35391363501548767,
      "rms_normalized_to_uniform_percent": 0.11604121670383082
    },
    "west": {
      "bias_percent": -0.18221042685273672,
      "rms_normalized_error_percent": 0.3256512431575191,
      "absolute_error": {
        "p95": 0.057794690132141086,
        "p99": 0.11479982852935788,
        "maximum": 0.125244140625
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.476428985595703,
      "reference_fraction_of_uniform": 0.26534149050712585,
      "rms_normalized_to_uniform_percent": 0.11074163015658382
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
          "nmbe_percent": -0.011978716794044292,
          "cvrmse_percent": 1.5523642593698996,
          "absolute_error_percentiles_lux": {
            "p50": 4.40533447265625,
            "p90": 28.292236328125,
            "p95": 42.83012084960935,
            "p99": 91.17407592773435
          },
          "maximum_absolute_error_lux": 345.0751953125,
          "worst": {
            "sensor_index": 36,
            "position": [
              6.5,
              2.5,
              0.75
            ],
            "hour_of_year": 6492.5,
            "foton_lux": 4150.1416015625,
            "radiance_lux": 3805.06640625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.1300634195839668,
            "maximum_error_percentage_points": 0.8501369863013721,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.05198637998570158,
            "maximum_error_percentage_points": 0.28736092951734804,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.037874175545408444,
            "maximum_error_percentage_points": 0.32410958904109677,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.059614408929476254,
            "maximum_error_percentage_points": 0.3241095890411003,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.031714865550482085,
            "maximum_error_percentage_points": 0.21767123287671275,
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
            "identifier": "plan_t_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_t_distributed_grid",
            "maximum_error_percentage_points": 0.004891374143824123,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_t_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_t_distributed_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_t_distributed_grid",
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
      "study_preparation_seconds": 0.38626722300023175,
      "weather_seconds": 0.260657474999789,
      "metric_reduction_seconds": 0.40100097300000925,
      "write_seconds": 0.017269814999963273,
      "total_seconds": 0.6792713919999187,
      "cold_end_to_end_seconds": 1.0655386150001505,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.002581627999916236,
      "engine_upload_seconds": 0.062489652,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.04835071,
      "engine_annual_reduction_seconds": 0.009782452,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.04835071
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.38626722300023175,
      "weather_seconds": 0.2592485019999913,
      "metric_reduction_seconds": 0.3560066370000641,
      "write_seconds": 0.02131372299982104,
      "total_seconds": 0.6368984509999791,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.6368984509999791,
      "raw_export_seconds": 0.002868571000362863,
      "engine_upload_seconds": 0.063459994,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4e-08,
      "engine_annual_reduction_seconds": 0.009503668,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.031846474000303715,
      "full": 0.0854416779998246
    }
  },
  "elapsed_seconds": 5.048658183000043,
  "result_class": "passed"
}
```
