# Foton report

Status: **passed**

```json
{
  "scene": "plan_t_offset_low",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "plan_t_offset_low",
    "category": "form",
    "question": "How does a offset low opening illuminate a T-shaped plan?",
    "interactions": [
      "concave_plan",
      "reentrant_occlusion",
      "window_shape",
      "window_position"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": "t",
    "window_profile": "offset_low"
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 54,
    "floor_area": 63.0,
    "aperture_area": 1.4400000000000002
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "095c856d5c8424298a0c93794f40b160a26e497ae8fac2ad5e776fcc4a1a8159",
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 6325780361428779710,
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 6325780361428779710,
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
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.3)",
      "weather_id": "82c544d76aea9710a570440071d4833104fdc7da7504bac286ac2afe42bdd614"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/usr/local/radiance/bin/gendaymtx",
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/12f3d0b2-7d1e-44d9-9264-d1e29a27929b/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "37ee64dbbcada916904f22220af11893b34808aad821a9d67d5407f73d8fde66",
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
          "maximum": 0.0001382098998874426,
          "p95": 0.0,
          "p99": 3.8708094507455826e-09
        },
        "bias_percent": 0.04711221313537381,
        "identifier": "plan_t_offset_low_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0269080251727867,
        "worst_index": [
          38,
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
          "maximum": 0.000256209634244442,
          "p95": 3.3302512747468427e-06,
          "p99": 1.587904989719391e-05
        },
        "bias_percent": 0.1088359313064477,
        "identifier": "plan_t_offset_low_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.19679932303205,
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
          "maximum": 0.0002154875546693802,
          "p95": 2.736389433266595e-06,
          "p99": 1.4094497601035982e-05
        },
        "bias_percent": -0.07914005203436217,
        "identifier": "plan_t_offset_low_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.7703083259720578,
        "worst_index": [
          38,
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
            "identifier": "plan_t_offset_low_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00040707451989874244,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 1.10571469889328,
                "cvrmse_percent": 92.52357756274003,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.07637274015312752,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1065598089408013,
                "relative_energy_error_percent": 0.07637274015312752,
                "rms_normalized_rmse_percent": 6.492409705704322,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002356966957449913,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.0019498924375511706,
                  "rgb_channel": 0,
                  "sky_patch_index": 206
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008470675093121827,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.475367702776566e-05
                },
                "candidate_energy": 0.4356555896700911,
                "cvrmse_percent": 518.982208820857,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.0910590464456353,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.4352592467504337,
                "relative_energy_error_percent": 0.0910590464456353,
                "rms_normalized_rmse_percent": 9.212918666751872,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0005173180252313614,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": -0.0003297494840808213,
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.53141699917614,
            "full": 303.02983394358307
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 137.99329195171595,
            "full": 325.7313329959288
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.9837499530986,
            "full": 315.8703329972923
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.2798749729991,
            "full": 310.26141706388444
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
            "identifier": "plan_t_offset_low_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003017975250259042,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 1.0993110791332583,
                "cvrmse_percent": 76.67904877267898,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.002104078519518167,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.0993342099882284,
                "relative_energy_error_percent": 0.002104078519518167,
                "rms_normalized_rmse_percent": 5.371235831437771,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0024362190160900354,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.0021344214910641313,
                  "rgb_channel": 0,
                  "sky_patch_index": 212
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00045458972454071045,
                  "p50": 0.0,
                  "p90": 2.027205663779341e-06,
                  "p95": 4.764113100463874e-06,
                  "p99": 2.6842374609259423e-05
                },
                "candidate_energy": 0.949604375595392,
                "cvrmse_percent": 145.97685481278404,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.052833191807792335,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9501063471041356,
                "relative_energy_error_percent": 0.05283319180779234,
                "rms_normalized_rmse_percent": 4.230993694168146,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.01861757505685091,
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "reference": 0.0181629853323102,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 176.18129204493016,
            "full": 3832.098041079007
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 180.93641696032137,
            "full": 3924.3719580117613
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 175.664332928136,
            "full": 3872.7431669831276
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 174.29508396890014,
            "full": 3835.4172909166664
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
            "identifier": "plan_t_offset_low_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00036411010660231113,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 1.0997268068240373,
                "cvrmse_percent": 69.5887738948402,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.22085045089767913,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.0973034073012968,
                "relative_energy_error_percent": 0.2208504508976791,
                "rms_normalized_rmse_percent": 4.8696672452807706,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003493008087389171,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.00312889798078686,
                  "rgb_channel": 0,
                  "sky_patch_index": 267
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005627097561955452,
                  "p50": 0.0,
                  "p90": 2.0114157450734638e-06,
                  "p95": 4.572246893985721e-06,
                  "p99": 2.3846456315368414e-05
                },
                "candidate_energy": 0.9493349071220543,
                "cvrmse_percent": 135.67380837687654,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.7440485187568042,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9564513693684695,
                "relative_energy_error_percent": 0.7440485187568041,
                "rms_normalized_rmse_percent": 3.945129960234264,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.021312260068953037,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.021874969825148582,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 175.63549999613315,
            "full": 4151.351541979238
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 196.7302920529619,
            "full": 4030.537624959834
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 163.9203749364242,
            "full": 4093.6721250182018
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.86950006056577,
            "full": 4079.3072499800473
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
            "identifier": "plan_t_offset_low_grid",
            "sensor_count": 54,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00013713754015043378,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.5688783605583012e-09
                },
                "candidate_energy": 1.1033737629486495,
                "cvrmse_percent": 40.80193306554909,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.05843683666191651,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1040189166797063,
                "relative_energy_error_percent": 0.05843683666191651,
                "rms_normalized_rmse_percent": 2.8702327593877683,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0011409405269660056,
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "reference": 0.0010038029868155718,
                  "rgb_channel": 0,
                  "sky_patch_index": 96
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00034382566809654236,
                  "p50": 0.0,
                  "p90": 1.4422494807320163e-06,
                  "p95": 3.2342213671654463e-06,
                  "p99": 1.4364790331455879e-05
                },
                "candidate_energy": 0.9462879741445143,
                "cvrmse_percent": 77.45428728130084,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.042195646770836995,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.945888850226428,
                "relative_energy_error_percent": 0.04219564677083699,
                "rms_normalized_rmse_percent": 2.235300765122334,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.018197319470345974,
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "reference": 0.018541145138442516,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 230.7362500578165,
            "full": 7203.157000010833
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 237.47074999846518,
            "full": 7137.739542056806
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 234.59891695529222,
            "full": 7131.587750045583
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 229.6983751002699,
            "full": 7155.55675001815
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
    "/Users/ssanjay/GitHub/foton-0.3.3/validation/results/2026-11-04-architectural-v4-metal-0.3.3-release/plan_t_offset_low/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 6384.720542002469,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/plan_t_offset_low/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 26298.984791967086,
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
        "identifier": "plan_t_offset_low_grid",
        "full_identifier": "plan_t_offset_low_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": 0.016526811877770574,
            "cvrmse_percent": 6.590113640870783,
            "rms_normalized_rmse_percent": 0.46343309822997514,
            "reference_energy": 1.102634568874464,
            "candidate_energy": 1.1028167992153612,
            "relative_energy_error_percent": 0.016526811877770574,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 6.984919309616089e-10,
              "maximum": 5.3326133638620377e-05
            },
            "worst": {
              "global_sensor_index": 26,
              "local_sensor_index": 26,
              "sky_patch_index": 414,
              "rgb_channel": 0,
              "reference": 0.001403772970661521,
              "candidate": 0.0014570991043001413,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.691586224131826,
            "cvrmse_percent": 91.87840830042225,
            "rms_normalized_rmse_percent": 2.6550020705801365,
            "reference_energy": 0.9471501879577993,
            "candidate_energy": 0.9311283258564664,
            "relative_energy_error_percent": 1.691586224131826,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.8962023986546228e-06,
              "p95": 4.0402710510534234e-06,
              "p99": 1.3762688467977569e-05,
              "maximum": 0.0006599575281143188
            },
            "worst": {
              "global_sensor_index": 25,
              "local_sensor_index": 25,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02157246693968773,
              "candidate": 0.02091250941157341,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.7727460996887421,
            "cvrmse_percent": 42.409633298868656,
            "rms_normalized_rmse_percent": 2.652194242422219,
            "reference_energy": 2.0497847568322634,
            "candidate_energy": 2.0339451250718277,
            "relative_energy_error_percent": 0.772746099688742,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.8941432813335268e-06,
              "p95": 4.025934686069377e-06,
              "p99": 1.3964148820377886e-05,
              "maximum": 0.0006599575281143188
            },
            "worst": {
              "global_sensor_index": 25,
              "local_sensor_index": 25,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02157246693968773,
              "candidate": 0.02091250941157341,
              "position": [
                5.5,
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
        "identifier": "plan_t_offset_low_grid",
        "full_identifier": "plan_t_offset_low_grid",
        "start_sensor_index": 0,
        "sensor_count": 54,
        "stages": {
          "direct": {
            "nmbe_percent": 0.016526811877770574,
            "cvrmse_percent": 6.590113640870783,
            "rms_normalized_rmse_percent": 0.46343309822997514,
            "reference_energy": 1.102634568874464,
            "candidate_energy": 1.1028167992153612,
            "relative_energy_error_percent": 0.016526811877770574,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 6.984919309616089e-10,
              "maximum": 5.3326133638620377e-05
            },
            "worst": {
              "global_sensor_index": 26,
              "local_sensor_index": 26,
              "sky_patch_index": 414,
              "rgb_channel": 0,
              "reference": 0.001403772970661521,
              "candidate": 0.0014570991043001413,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 112.12140659107735,
            "cvrmse_percent": 2154.265240610407,
            "rms_normalized_rmse_percent": 38.7138605391101,
            "reference_energy": 0.4389600940424998,
            "candidate_energy": 0.9311283258564664,
            "relative_energy_error_percent": 112.12140659107733,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.809999947814504e-06,
              "p95": 1.8849999833037145e-05,
              "p99": 5.76899983570911e-05,
              "maximum": 0.0064456528052687645
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.008648117072880268,
              "candidate": 0.015093769878149033,
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
            "nmbe_percent": 31.937737850185044,
            "cvrmse_percent": 613.4059227545558,
            "rms_normalized_rmse_percent": 38.71332112506263,
            "reference_energy": 1.541594662916964,
            "candidate_energy": 2.0339451250718277,
            "relative_energy_error_percent": 31.937737850185048,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.809999947814504e-06,
              "p95": 1.8900000213761814e-05,
              "p99": 5.76899983570911e-05,
              "maximum": 0.0064456528052687645
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.008648117072880268,
              "candidate": 0.015093769878149033,
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
      "bias_percent": -0.025123799461468786,
      "rms_normalized_error_percent": 0.15300907872284364,
      "absolute_error": {
        "p95": 0.02182506736455658,
        "p99": 0.032859489229092126,
        "maximum": 0.03609954744378285
      },
      "worst_index": [
        37
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.5087702428522272,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.15300907872284364
    },
    "overcast": {
      "bias_percent": -0.024369179652413257,
      "rms_normalized_error_percent": 0.12664298349968225,
      "absolute_error": {
        "p95": 0.012448422610759726,
        "p99": 0.01852925300598144,
        "maximum": 0.02163219451904297
      },
      "worst_index": [
        37
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.9200553894042969,
      "reference_fraction_of_uniform": 0.6098048686981201,
      "rms_normalized_to_uniform_percent": 0.08335997130108685
    },
    "horizon": {
      "bias_percent": -0.2781171954702409,
      "rms_normalized_error_percent": 1.4392879020772722,
      "absolute_error": {
        "p95": 0.016801309117541293,
        "p99": 0.0244650878815792,
        "maximum": 0.02653540399732368
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.23333123309168055,
      "reference_fraction_of_uniform": 0.15464994368564944,
      "rms_normalized_to_uniform_percent": 0.11260613169853849
    },
    "north": {
      "bias_percent": -99.56959545905212,
      "rms_normalized_error_percent": 100.00066407974266,
      "absolute_error": {
        "p95": 0.00012183278195152509,
        "p99": 0.00028455840860260647,
        "maximum": 0.00029250848456285894
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.247149132017512e-05,
      "reference_fraction_of_uniform": 1.4893912521074526e-05,
      "rms_normalized_to_uniform_percent": 0.0009346245886445427
    },
    "east": {
      "bias_percent": -0.07194611551252525,
      "rms_normalized_error_percent": 0.350793947234569,
      "absolute_error": {
        "p95": 0.007171480357646934,
        "p99": 0.008847925961017607,
        "maximum": 0.009433597326278687
      },
      "worst_index": [
        37
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.15501251816749573,
      "reference_fraction_of_uniform": 0.10274097323417664,
      "rms_normalized_to_uniform_percent": 0.04050621514055777
    },
    "south": {
      "bias_percent": 0.001312684529253237,
      "rms_normalized_error_percent": 0.1606681258352472,
      "absolute_error": {
        "p95": 0.02072585225105285,
        "p99": 0.022407989501953125,
        "maximum": 0.0232086181640625
      },
      "worst_index": [
        37
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.142398476600647,
      "reference_fraction_of_uniform": 0.7571719288825989,
      "rms_normalized_to_uniform_percent": 0.11993713301451152
    },
    "west": {
      "bias_percent": 0.006630805066222798,
      "rms_normalized_error_percent": 0.16998677917313643,
      "absolute_error": {
        "p95": 0.006124126911163328,
        "p99": 0.007092107832431792,
        "maximum": 0.007469534873962402
      },
      "worst_index": [
        37
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.36896511912345886,
      "reference_fraction_of_uniform": 0.24454692006111145,
      "rms_normalized_to_uniform_percent": 0.03729685088953133
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
        "identifier": "plan_t_offset_low_grid",
        "sensor_count": 54,
        "illuminance": {
          "nmbe_percent": -0.0386638763246891,
          "cvrmse_percent": 4.747230471520051,
          "absolute_error_percentiles_lux": {
            "p50": 0.2930123805999756,
            "p90": 4.584114074707031,
            "p95": 8.836257457733147,
            "p99": 26.29061309814451
          },
          "maximum_absolute_error_lux": 222.513671875,
          "worst": {
            "sensor_index": 26,
            "position": [
              5.5,
              0.5,
              0.75
            ],
            "hour_of_year": 1860.5,
            "foton_lux": 28163.578125,
            "radiance_lux": 28386.091796875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.043376458650431306,
            "maximum_error_percentage_points": 0.6893150684931513,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.17875345750279548,
            "maximum_error_percentage_points": 0.737955508864939,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.14330542871638777,
            "maximum_error_percentage_points": 1.805616438356168,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.14419837645864997,
            "maximum_error_percentage_points": 1.8056164383561644,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0012861491628614946,
            "maximum_error_percentage_points": 0.0320547945205476,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 5.555555555555555,
          "radiance_percent": 5.555555555555555,
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
      "maximum_error_percentage_points": 0.004931506849314982,
      "metrics": {
        "da": [
          {
            "identifier": "plan_t_offset_low_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "plan_t_offset_low_grid",
            "maximum_error_percentage_points": 0.004756047497056937,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "plan_t_offset_low_grid",
            "maximum_error_percentage_points": 0.004383561643835632,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "plan_t_offset_low_grid",
            "maximum_error_percentage_points": 0.004383561643834355,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "plan_t_offset_low_grid",
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
      "study_preparation_seconds": 0.006355541059747338,
      "weather_seconds": 0.08443162497133017,
      "metric_reduction_seconds": 0.1228352920152247,
      "write_seconds": 0.025537624955177307,
      "total_seconds": 0.23292520898394287,
      "cold_end_to_end_seconds": 0.2392807500436902,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0028202920220792294,
      "engine_upload_seconds": 0.000909208,
      "engine_acceleration_structure_seconds": 0.00280475,
      "engine_tracing_seconds": 0.06100879155565053,
      "engine_annual_reduction_seconds": 0.0023293333360925317,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.06100879155565053
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006355541059747338,
      "weather_seconds": 0.07949775003362447,
      "metric_reduction_seconds": 0.0483644159976393,
      "write_seconds": 0.015809250064194202,
      "total_seconds": 0.1437801249558106,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1437801249558106,
      "raw_export_seconds": 0.0024428750621154904,
      "engine_upload_seconds": 7.2416e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0024198750033974648,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02283912501297891,
      "full": 0.07169249991420656
    }
  },
  "elapsed_seconds": 1.57375454204157,
  "result_class": "passed"
}
```
