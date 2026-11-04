# Foton report

Status: **passed**

```json
{
  "scene": "irregular",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "irregular",
    "category": "form",
    "question": "Is an L-shaped room triangulated without filling its recess?",
    "interactions": [
      "concave_plan",
      "self_occlusion"
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
    "sensors": 24,
    "floor_area": 27.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "1d444627399faaa47e77d9a52a10ff2e2a8e074ad6b7d2731e99d88e1e7bcd0e",
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
      "scene_fingerprint": 5737655811555480342,
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
      "scene_fingerprint": 5737655811555480342,
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
    "model_sha256": "4483f3819c3a4eadb4201536260d7bbf4e71dceebb3e10de5a023408a0de957f",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "01b8e2121007e365364398ee48d8b708424c5c15cddced03ada4fc5c521806f0",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00014028436271473765,
          "p95": 7.450580596923828e-08,
          "p99": 7.905660822871073e-06
        },
        "bias_percent": -0.03090303805115706,
        "identifier": "irregular_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7402378158509368,
        "worst_index": [
          17,
          543,
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
          "maximum": 0.0003913082182407379,
          "p95": 2.9124494176357985e-05,
          "p99": 0.0001071847509592767
        },
        "bias_percent": 0.04150551770843347,
        "identifier": "irregular_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.639140699121665,
        "worst_index": [
          18,
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
          "maximum": 0.0003625229001045227,
          "p95": 2.410408342257142e-05,
          "p99": 8.529992192052287e-05
        },
        "bias_percent": 0.01610061473984418,
        "identifier": "irregular_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3313521037364162,
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
            "identifier": "irregular_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005741905188187957,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.630824645981193e-05,
                  "p99": 0.00023562766727991402
                },
                "candidate_energy": 5.326301650394271,
                "cvrmse_percent": 34.47319332904128,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.060478384019725516,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.329524860906076,
                "relative_energy_error_percent": 0.06047838401972551,
                "rms_normalized_rmse_percent": 7.448591680854843,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0016405295464210212,
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "reference": 0.0010663390276022255,
                  "rgb_channel": 0,
                  "sky_patch_index": 203
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00075956666842103,
                  "p50": 0.0,
                  "p90": 8.745247214392293e-06,
                  "p95": 9.189604315906763e-05,
                  "p99": 0.00034023833432001886
                },
                "candidate_energy": 1.4644745881369587,
                "cvrmse_percent": 177.88740192145676,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.06511315810346409,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.4654287750921782,
                "relative_energy_error_percent": 0.06511315810346409,
                "rms_normalized_rmse_percent": 6.387000750070225,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.01587336719967425,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.015113800531253219,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 109.483249951154,
            "full": 184.3655409757048
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 97.78195794206113,
            "full": 185.3868329199031
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 104.07029208727181,
            "full": 193.3552500559017
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 100.21429206244648,
            "full": 174.0007920889184
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 99.70629098825157,
            "full": 183.09375003445894
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 97.74933394510299,
            "full": 183.25670796912163
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 113.29849995672703,
            "full": 181.62570800632238
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 101.01154202129692,
            "full": 178.38737496640533
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
            "identifier": "irregular_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00034744443837553263,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.8718513678759336e-05,
                  "p99": 0.00015842782740946792
                },
                "candidate_energy": 5.328230921500108,
                "cvrmse_percent": 21.659639245727803,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.0651020363342734,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.331701968052585,
                "relative_energy_error_percent": 0.06510203633427342,
                "rms_normalized_rmse_percent": 4.6900719079089805,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0024547195062041283,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.0021072750678285956,
                  "rgb_channel": 0,
                  "sky_patch_index": 204
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000637703575193882,
                  "p50": 1.9838530818105937e-08,
                  "p90": 1.4785000530537218e-05,
                  "p95": 5.429028533399105e-05,
                  "p99": 0.0002198325011704553
                },
                "candidate_energy": 2.728250058979036,
                "cvrmse_percent": 63.02605651985753,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.21683745341667243,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.72234699109039,
                "relative_energy_error_percent": 0.2168374534166724,
                "rms_normalized_rmse_percent": 3.242518205208255,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03138905484229326,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.032026758417487144,
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 128.21945804171264,
            "full": 1624.8336670687422
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.0701249903068,
            "full": 1618.6347500188276
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.895083097741,
            "full": 1584.3769169878215
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 137.7091669710353,
            "full": 1601.9945000298321
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
            "identifier": "irregular_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003099064342677593,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.56503767054528e-05,
                  "p99": 0.0001410720869898796
                },
                "candidate_energy": 5.333915753358269,
                "cvrmse_percent": 20.99468467871397,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.022907739070016888,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.3326941536961385,
                "relative_energy_error_percent": 0.022907739070016888,
                "rms_normalized_rmse_percent": 4.544882848332718,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004923104541376233,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.004613198107108474,
                  "rgb_channel": 0,
                  "sky_patch_index": 453
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006197355687618256,
                  "p50": 2.9883473473546474e-08,
                  "p90": 1.5617093595210463e-05,
                  "p95": 5.937728565186262e-05,
                  "p99": 0.00021806886215927057
                },
                "candidate_energy": 2.726038959782585,
                "cvrmse_percent": 62.37781168487181,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.05399287778250994,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.724567887173162,
                "relative_energy_error_percent": 0.05399287778250994,
                "rms_normalized_rmse_percent": 3.2113311351054064,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.037043819203972816,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.03642408363521099,
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 137.836208101362,
            "full": 1741.7629580013454
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.96245799958706,
            "full": 1766.8083329917863
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.95583302900195,
            "full": 1719.3885000888258
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.09537500329316,
            "full": 1741.3135409587994
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
            "identifier": "irregular_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00019567669369280338,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1655097953043878e-05,
                  "p99": 8.127992041409012e-05
                },
                "candidate_energy": 5.334282316431199,
                "cvrmse_percent": 11.618953630488807,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.026394663620630476,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.335690654031168,
                "relative_energy_error_percent": 0.026394663620630476,
                "rms_normalized_rmse_percent": 2.516899291411809,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003840093966573477,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.00403577066026628,
                  "rgb_channel": 0,
                  "sky_patch_index": 358
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005401894450187683,
                  "p50": 1.9993763089587446e-08,
                  "p90": 1.0263058356940746e-05,
                  "p95": 3.15680808853358e-05,
                  "p99": 0.00012220736825838664
                },
                "candidate_energy": 2.726390424383613,
                "cvrmse_percent": 36.17722119741854,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.10802983318209733,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.723448287741565,
                "relative_energy_error_percent": 0.10802983318209733,
                "rms_normalized_rmse_percent": 1.859948978461339,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04036998562514782,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.04091017507016659,
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 188.7197910109535,
            "full": 3076.1820420157164
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 197.609500028193,
            "full": 3004.840958979912
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 203.26483296230435,
            "full": 3381.0889170272276
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 192.77579197660089,
            "full": 3066.816332982853
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
    "/Users/ssanjay/GitHub/foton-0.3.3/validation/results/2026-11-04-architectural-v4-metal-0.3.3-release/irregular/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1433.904125005938,
      "invocation_count": 2,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 5650.74991597794,
      "invocation_count": 2,
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
      24,
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
        "identifier": "irregular_grid",
        "full_identifier": "irregular_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.035485083039695955,
            "cvrmse_percent": 1.9021787863380246,
            "rms_normalized_rmse_percent": 0.41219358709611537,
            "reference_energy": 5.334909990154756,
            "candidate_energy": 5.333016892914657,
            "relative_energy_error_percent": 0.035485083039695955,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 6.2515027821064e-08,
              "p99": 7.468089461326439e-06,
              "maximum": 5.9494748711586e-05
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052893467247486,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.902799192124929,
            "cvrmse_percent": 36.68626644972857,
            "rms_normalized_rmse_percent": 1.8874832122414615,
            "reference_energy": 2.724995857876454,
            "candidate_energy": 2.7003946172861077,
            "relative_energy_error_percent": 0.902799192124929,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.0909148841165006e-05,
              "p95": 1.9257189705967903e-05,
              "p99": 5.32598256540943e-05,
              "maximum": 0.0009774528443813324
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.029377233237028122,
              "candidate": 0.02839978039264679,
              "position": [
                1.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.3287177087424368,
            "cvrmse_percent": 12.367481890904415,
            "rms_normalized_rmse_percent": 1.882023261250581,
            "reference_energy": 8.05990584803121,
            "candidate_energy": 8.033411510200764,
            "relative_energy_error_percent": 0.3287177087424367,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.071763108484447e-05,
              "p95": 1.9049279217142612e-05,
              "p99": 5.162100133020428e-05,
              "maximum": 0.0009774528443813324
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.029377233237028122,
              "candidate": 0.02839978039264679,
              "position": [
                1.5,
                2.5,
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
      24,
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
        "identifier": "irregular_grid",
        "full_identifier": "irregular_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.035485083039695955,
            "cvrmse_percent": 1.9021787863380246,
            "rms_normalized_rmse_percent": 0.41219358709611537,
            "reference_energy": 5.334909990154756,
            "candidate_energy": 5.333016892914657,
            "relative_energy_error_percent": 0.035485083039695955,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 6.2515027821064e-08,
              "p99": 7.468089461326439e-06,
              "maximum": 5.9494748711586e-05
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052893467247486,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 85.21797485227627,
            "cvrmse_percent": 962.3248963742296,
            "rms_normalized_rmse_percent": 34.43433630448325,
            "reference_energy": 1.4579549417057676,
            "candidate_energy": 2.7003946172861077,
            "relative_energy_error_percent": 85.21797485227627,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.039000072632916e-05,
              "p95": 8.632568642497063e-05,
              "p99": 0.0001621433768377753,
              "maximum": 0.011024221777915955
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01837252825498581,
              "candidate": 0.029396750032901764,
              "position": [
                5.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 18.262494408238776,
            "cvrmse_percent": 206.53416195507353,
            "rms_normalized_rmse_percent": 34.432675431910496,
            "reference_energy": 6.792864931860524,
            "candidate_energy": 8.033411510200764,
            "relative_energy_error_percent": 18.262494408238773,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.012337780703092e-05,
              "p95": 8.635774793219753e-05,
              "p99": 0.0001621207631615102,
              "maximum": 0.011024221777915955
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01837252825498581,
              "candidate": 0.029396750032901764,
              "position": [
                5.5,
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
      "bias_percent": 0.11213501186638877,
      "rms_normalized_error_percent": 0.13569356548488018,
      "absolute_error": {
        "p95": 0.06481654524464917,
        "p99": 0.0790937507316235,
        "maximum": 0.08310121043084528
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.437599514036657,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.13569356548488018
    },
    "overcast": {
      "bias_percent": 0.07473494828624332,
      "rms_normalized_error_percent": 0.09746608299930914,
      "absolute_error": {
        "p95": 0.032676601409912104,
        "p99": 0.04262961864471435,
        "maximum": 0.045484066009521484
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.158856391906738,
      "reference_fraction_of_uniform": 0.6580593585968018,
      "rms_normalized_to_uniform_percent": 0.06953028896736525
    },
    "horizon": {
      "bias_percent": 0.9558598127145591,
      "rms_normalized_error_percent": 1.4919032712914837,
      "absolute_error": {
        "p95": 0.04397112482142957,
        "p99": 0.04585857002896462,
        "maximum": 0.04633826710805522
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.5076879269243648,
      "reference_fraction_of_uniform": 0.09766336570355369,
      "rms_normalized_to_uniform_percent": 0.0916569863395063
    },
    "north": {
      "bias_percent": -72.12166294208943,
      "rms_normalized_error_percent": 98.03481783123617,
      "absolute_error": {
        "p95": 2.0644008509407274e-05,
        "p99": 3.688062092237486e-05,
        "maximum": 4.147260904119321e-05
      },
      "worst_index": [
        20
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 5.5603049986530095e-06,
      "reference_fraction_of_uniform": 3.6017939919474884e-07,
      "rms_normalized_to_uniform_percent": 3.971458881619937e-05
    },
    "east": {
      "bias_percent": 0.06605408632159346,
      "rms_normalized_error_percent": 0.2303026290992157,
      "absolute_error": {
        "p95": 0.023187589645385743,
        "p99": 0.0312665581703186,
        "maximum": 0.03367304801940918
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.2878189086914062,
      "reference_fraction_of_uniform": 0.21297475695610046,
      "rms_normalized_to_uniform_percent": 0.04666480619944004
    },
    "south": {
      "bias_percent": 0.15569126572932163,
      "rms_normalized_error_percent": 0.1804201558071149,
      "absolute_error": {
        "p95": 0.058086073398590066,
        "p99": 0.06667362213134766,
        "maximum": 0.06879425048828125
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.403655052185059,
      "reference_fraction_of_uniform": 0.6739166378974915,
      "rms_normalized_to_uniform_percent": 0.11713396951007088
    },
    "west": {
      "bias_percent": 0.07268095319833529,
      "rms_normalized_error_percent": 0.12284623418938193,
      "absolute_error": {
        "p95": 0.009882271289825438,
        "p99": 0.020558373928070063,
        "maximum": 0.023694515228271484
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.6763248443603516,
      "reference_fraction_of_uniform": 0.17336405813694,
      "rms_normalized_to_uniform_percent": 0.024669953107651087
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
        "identifier": "irregular_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": 0.07093883158693709,
          "cvrmse_percent": 1.502730447821217,
          "absolute_error_percentiles_lux": {
            "p50": 1.984130859375,
            "p90": 24.406356811523445,
            "p95": 39.56091308593746,
            "p99": 93.2183984374999
          },
          "maximum_absolute_error_lux": 416.61328125,
          "worst": {
            "sensor_index": 16,
            "position": [
              2.5,
              1.5,
              0.75
            ],
            "hour_of_year": 6827.5,
            "foton_lux": 19789.626953125,
            "radiance_lux": 20206.240234375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.16986872146118767,
            "maximum_error_percentage_points": 0.6846575342465755,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.08031740999908295,
            "maximum_error_percentage_points": 0.5139843650767659,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.05722031963470283,
            "maximum_error_percentage_points": 0.2501369863013707,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.07297945205479343,
            "maximum_error_percentage_points": 0.24561643835616565,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.02622146118721443,
            "maximum_error_percentage_points": 0.08643835616438356,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 62.5,
          "radiance_percent": 62.5,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 4.166666666666667,
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
      "maximum_error_percentage_points": 0.00498287671232589,
      "metrics": {
        "da": [
          {
            "identifier": "irregular_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "irregular_grid",
            "maximum_error_percentage_points": 0.00498287671232589,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "irregular_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "irregular_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "irregular_grid",
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
      "study_preparation_seconds": 0.006278750021010637,
      "weather_seconds": 0.08203250006772578,
      "metric_reduction_seconds": 0.1514098329935223,
      "write_seconds": 0.04149916605092585,
      "total_seconds": 0.27506474999245256,
      "cold_end_to_end_seconds": 0.2813435000134632,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0077024579513818026,
      "engine_upload_seconds": 0.00090625,
      "engine_acceleration_structure_seconds": 0.00296375,
      "engine_tracing_seconds": 0.03144616668578237,
      "engine_annual_reduction_seconds": 0.0009941249154508114,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.03144616668578237
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006278750021010637,
      "weather_seconds": 0.07802549994084984,
      "metric_reduction_seconds": 0.0496807909803465,
      "write_seconds": 0.015512209036387503,
      "total_seconds": 0.14333224995061755,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14333224995061755,
      "raw_export_seconds": 0.001729167066514492,
      "engine_upload_seconds": 5.3042e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00100041669793427,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.016145417001098394,
      "full": 0.04589824995491654
    }
  },
  "elapsed_seconds": 1.1913578750099987,
  "result_class": "passed"
}
```
