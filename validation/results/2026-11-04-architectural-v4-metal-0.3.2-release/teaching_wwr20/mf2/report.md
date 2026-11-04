# Foton report

Status: **passed**

```json
{
  "scene": "teaching_wwr20",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_wwr20",
    "category": "teaching",
    "question": "How does a 20% window-to-wall ratio light the base room?",
    "interactions": [
      "multiple_bounces",
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
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 3.6018000000000003
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "0b937c10b88024920d0f0f083b5b4a6ffeddf99428c87144bbfd1499858ba4e2",
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 1765380858695198131,
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 1765380858695198131,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.2)",
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
    "model_sha256": "97042f26c1eaa8818393fd2c3cfb3f6fdbddb22b0a625cebd3cdebc8a3301077",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "42ebbd5873d9863a0ad3aca60e92d9e55c1ae842623c6cc1f4949849ae92cd10",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00012495671398937702,
          "p95": 1.6076955944299698e-07,
          "p99": 1.2711563613265753e-05
        },
        "bias_percent": -0.017853057437220834,
        "identifier": "teaching_wwr20_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7459770005717545,
        "worst_index": [
          11,
          453,
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
          "maximum": 0.0006358195096254349,
          "p95": 4.3820502469316125e-05,
          "p99": 0.00011342158541083336
        },
        "bias_percent": -0.01316226919139232,
        "identifier": "teaching_wwr20_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.8377726642932992,
        "worst_index": [
          7,
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
          "maximum": 0.00038676708936691284,
          "p95": 3.6528799682855606e-05,
          "p99": 9.488730574958026e-05
        },
        "bias_percent": 0.04732759643878303,
        "identifier": "teaching_wwr20_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.4802194822192696,
        "worst_index": [
          9,
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
            "identifier": "teaching_wwr20_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006538742018165067,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 9.127469820668921e-05,
                  "p99": 0.000250030672759749
                },
                "candidate_energy": 7.791142305698941,
                "cvrmse_percent": 38.03688071636541,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.050404796097006745,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.787217174760372,
                "relative_energy_error_percent": 0.050404796097006745,
                "rms_normalized_rmse_percent": 8.658391180522607,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0009807275491766632,
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "reference": 0.0003268533473601565,
                  "rgb_channel": 0,
                  "sky_patch_index": 154
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010111955343745649,
                  "p50": 0.0,
                  "p90": 7.70595136145907e-06,
                  "p95": 0.00012004413292743266,
                  "p99": 0.00034746830351650715
                },
                "candidate_energy": 2.2399634073399124,
                "cvrmse_percent": 181.78157064088487,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.2495559665979948,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.2343873603652096,
                "relative_energy_error_percent": 0.24955596659799478,
                "rms_normalized_rmse_percent": 6.724163338219787,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0004127954598516226,
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "reference": -0.0005984000745229423,
                  "rgb_channel": 0,
                  "sky_patch_index": 263
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 125.58495893608779,
            "full": 228.98162505589426
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 119.1453750943765,
            "full": 228.34683302789927
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 106.41633300110698,
            "full": 215.74225008953363
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.30658397916704,
            "full": 225.43874999973923
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 113.85483399499208,
            "full": 238.08987508527935
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 107.59937507100403,
            "full": 238.64029196556658
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 115.19291694276035,
            "full": 222.53458306659013
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 104.63279206305742,
            "full": 221.9331250526011
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
            "identifier": "teaching_wwr20_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00035593239590525627,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.141720223240554e-05,
                  "p99": 0.0001615938381291926
                },
                "candidate_energy": 7.788576659984756,
                "cvrmse_percent": 24.704681892376158,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.06224893673179381,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.793427986041024,
                "relative_energy_error_percent": 0.06224893673179381,
                "rms_normalized_rmse_percent": 5.634815698116429,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003598409006372094,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.00395434140227735,
                  "rgb_channel": 0,
                  "sky_patch_index": 356
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008535534143447876,
                  "p50": 2.7583105577377864e-08,
                  "p90": 1.8214174451713948e-05,
                  "p95": 8.592044468969107e-05,
                  "p99": 0.0002275985898450017
                },
                "candidate_energy": 4.295348781199543,
                "cvrmse_percent": 65.51659293277552,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.01864885033522819,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.296149963776465,
                "relative_energy_error_percent": 0.01864885033522819,
                "rms_normalized_rmse_percent": 3.479564994277711,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03381529822945595,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.03296174481511116,
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.77745799720287,
            "full": 2245.3498750692233
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.84241700079292,
            "full": 2618.7087080907077
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.48070793412626,
            "full": 2228.230750071816
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.53254200331867,
            "full": 2224.8711249558255
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
            "identifier": "teaching_wwr20_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003269223961979151,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.7133711632341146e-05,
                  "p99": 0.00015769642777740955
                },
                "candidate_energy": 7.783072822365284,
                "cvrmse_percent": 23.31033065054989,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.00233539339742646,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.78325459197913,
                "relative_energy_error_percent": 0.0023353933974264596,
                "rms_normalized_rmse_percent": 5.3066320532402536,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0008844039984978735,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.0005574816022999585,
                  "rgb_channel": 0,
                  "sky_patch_index": 142
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009495466947555542,
                  "p50": 3.19072732679615e-08,
                  "p90": 1.887319194793244e-05,
                  "p95": 8.52005323395133e-05,
                  "p99": 0.00022794987307861447
                },
                "candidate_energy": 4.302234789325254,
                "cvrmse_percent": 63.94322627457426,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.011051783003398126,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.301759368214551,
                "relative_energy_error_percent": 0.011051783003398125,
                "rms_normalized_rmse_percent": 3.3988989502079923,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03288966603577137,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.031940119341015816,
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.43970803264529,
            "full": 2350.6487909471616
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.098791975528,
            "full": 2354.73975003697
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.98704100959003,
            "full": 2419.5798750733957
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.90229109488428,
            "full": 2376.483083004132
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
            "identifier": "teaching_wwr20_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00018426845781505108,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.4241878893226385e-05,
                  "p99": 8.874968625605106e-05
                },
                "candidate_energy": 7.788641054332402,
                "cvrmse_percent": 13.27998910989844,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.03475697669970225,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.791349091720804,
                "relative_energy_error_percent": 0.03475697669970225,
                "rms_normalized_rmse_percent": 3.029375991405884,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0022139025386422873,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.002029634080827236,
                  "rgb_channel": 0,
                  "sky_patch_index": 218
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006575994193553925,
                  "p50": 3.333947518058267e-08,
                  "p90": 1.2518306721176487e-05,
                  "p95": 4.883552901446819e-05,
                  "p99": 0.00012803490972146392
                },
                "candidate_energy": 4.304588684945372,
                "cvrmse_percent": 37.45921129428953,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.17236273103040559,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.29718194478799,
                "relative_energy_error_percent": 0.17236273103040556,
                "rms_normalized_rmse_percent": 1.9894211109465842,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.025330450385808945,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.025988049805164337,
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 210.90120892040431,
            "full": 4285.933499922976
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 208.04604201111943,
            "full": 4160.036833956838
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 209.97416600584984,
            "full": 4170.300500001758
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 213.94212497398257,
            "full": 4266.309375059791
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
    "/Users/ssanjay/GitHub/foton-release-0.3.2/validation/results/2026-11-04-architectural-v4-metal-0.3.2-release/teaching_wwr20/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2794.927875045687,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10686.215874971822,
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
      36,
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
        "identifier": "teaching_wwr20_grid",
        "full_identifier": "teaching_wwr20_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.004010910666130279,
            "cvrmse_percent": 1.5828752914054585,
            "rms_normalized_rmse_percent": 0.3611285980661293,
            "reference_energy": 7.788499300699527,
            "candidate_energy": 7.788186910950344,
            "relative_energy_error_percent": 0.004010910666130278,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.4365650713443756e-07,
              "p99": 7.631955668330193e-06,
              "maximum": 6.136181764304638e-05
            },
            "worst": {
              "global_sensor_index": 11,
              "local_sensor_index": 11,
              "sky_patch_index": 414,
              "rgb_channel": 0,
              "reference": 0.0030791882891207933,
              "candidate": 0.003017826471477747,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.024508491292545,
            "cvrmse_percent": 39.219778026979455,
            "rms_normalized_rmse_percent": 2.0852447992528638,
            "reference_energy": 4.302381095198559,
            "candidate_energy": 4.258302835550484,
            "relative_energy_error_percent": 1.024508491292545,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.2025923570035961e-05,
              "p95": 2.15945765376091e-05,
              "p99": 5.2641844376921654e-05,
              "maximum": 0.0011562816798686981
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03247798979282379,
              "candidate": 0.03132170811295509,
              "position": [
                3.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.367141580627309,
            "cvrmse_percent": 13.971801878637713,
            "rms_normalized_rmse_percent": 2.0876292951207684,
            "reference_energy": 12.090880395898086,
            "candidate_energy": 12.046489746500828,
            "relative_energy_error_percent": 0.36714158062730906,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.2108415103284662e-05,
              "p95": 2.1870906493859366e-05,
              "p99": 5.285884253680706e-05,
              "maximum": 0.0011562816798686981
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03247798979282379,
              "candidate": 0.03132170811295509,
              "position": [
                3.5,
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
      36,
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
        "identifier": "teaching_wwr20_grid",
        "full_identifier": "teaching_wwr20_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.004010910666130279,
            "cvrmse_percent": 1.5828752914054585,
            "rms_normalized_rmse_percent": 0.3611285980661293,
            "reference_energy": 7.788499300699527,
            "candidate_energy": 7.788186910950344,
            "relative_energy_error_percent": 0.004010910666130278,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.4365650713443756e-07,
              "p99": 7.631955668330193e-06,
              "maximum": 6.136181764304638e-05
            },
            "worst": {
              "global_sensor_index": 11,
              "local_sensor_index": 11,
              "sky_patch_index": 414,
              "rgb_channel": 0,
              "reference": 0.0030791882891207933,
              "candidate": 0.003017826471477747,
              "position": [
                1.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 90.28495105792527,
            "cvrmse_percent": 999.4570487988904,
            "rms_normalized_rmse_percent": 36.99770359535133,
            "reference_energy": 2.237855811442598,
            "candidate_energy": 4.258302835550484,
            "relative_energy_error_percent": 90.28495105792528,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.596100211027092e-05,
              "p95": 9.174000297207385e-05,
              "p99": 0.0001595019712112844,
              "maximum": 0.009478643536567688
            },
            "worst": {
              "global_sensor_index": 24,
              "local_sensor_index": 24,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.013810666278004646,
              "candidate": 0.023289309814572334,
              "position": [
                4.5,
                5.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.14824541684423,
            "cvrmse_percent": 223.07620881068723,
            "rms_normalized_rmse_percent": 36.997712224536265,
            "reference_energy": 10.026355112142125,
            "candidate_energy": 12.046489746500828,
            "relative_energy_error_percent": 20.14824541684423,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.596100211027092e-05,
              "p95": 9.199324995279312e-05,
              "p99": 0.00016005450015654787,
              "maximum": 0.009478643536567688
            },
            "worst": {
              "global_sensor_index": 24,
              "local_sensor_index": 24,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.013810666278004646,
              "candidate": 0.023289309814572334,
              "position": [
                4.5,
                5.5,
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
      "bias_percent": 0.03907891975260786,
      "rms_normalized_error_percent": 0.11908848839639655,
      "absolute_error": {
        "p95": 0.060343583694216885,
        "p99": 0.06230048014379194,
        "maximum": 0.06304238689243391
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.06710612372199,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.11908848839639655
    },
    "overcast": {
      "bias_percent": 0.02683373460497141,
      "rms_normalized_error_percent": 0.09724968593553236,
      "absolute_error": {
        "p95": 0.028415054082870483,
        "p99": 0.04076742529869079,
        "maximum": 0.042736053466796875
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.213888168334961,
      "reference_fraction_of_uniform": 0.6115233898162842,
      "rms_normalized_to_uniform_percent": 0.06377239544386626
    },
    "horizon": {
      "bias_percent": 0.21706791238440343,
      "rms_normalized_error_percent": 1.115208710717765,
      "absolute_error": {
        "p95": 0.05505767906071729,
        "p99": 0.0658066566705723,
        "maximum": 0.0675818349346271
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.2584807459098375,
      "reference_fraction_of_uniform": 0.1498947924946274,
      "rms_normalized_to_uniform_percent": 0.10421152362523475
    },
    "north": {
      "bias_percent": -81.47411166946497,
      "rms_normalized_error_percent": 91.7169095136472,
      "absolute_error": {
        "p95": 2.2209426859376435e-05,
        "p99": 9.203954629128917e-05,
        "maximum": 0.00012512719149526674
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 9.300918463850394e-06,
      "reference_fraction_of_uniform": 6.172995767883549e-07,
      "rms_normalized_to_uniform_percent": 8.829107049928886e-05
    },
    "east": {
      "bias_percent": 0.024710043287563457,
      "rms_normalized_error_percent": 0.19729058968738847,
      "absolute_error": {
        "p95": 0.01898932456970215,
        "p99": 0.025672912597656236,
        "maximum": 0.029104232788085938
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.8175954818725586,
      "reference_fraction_of_uniform": 0.18700309097766876,
      "rms_normalized_to_uniform_percent": 0.039769330907926906
    },
    "south": {
      "bias_percent": 0.04998058654053407,
      "rms_normalized_error_percent": 0.14080787522255034,
      "absolute_error": {
        "p95": 0.04397767782211304,
        "p99": 0.06111079454421995,
        "maximum": 0.06602287292480469
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 11.073079109191895,
      "reference_fraction_of_uniform": 0.7349174618721008,
      "rms_normalized_to_uniform_percent": 0.09836080535790621
    },
    "west": {
      "bias_percent": 0.008624713337870555,
      "rms_normalized_error_percent": 0.21570227861224656,
      "absolute_error": {
        "p95": 0.021321415901184082,
        "p99": 0.028737068176269517,
        "maximum": 0.03220844268798828
      },
      "worst_index": [
        29
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.849580764770508,
      "reference_fraction_of_uniform": 0.18912595510482788,
      "rms_normalized_to_uniform_percent": 0.0438120428396379
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
        "identifier": "teaching_wwr20_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.002889573882148334,
          "cvrmse_percent": 1.5270843610861067,
          "absolute_error_percentiles_lux": {
            "p50": 2.2564239501953125,
            "p90": 26.49526367187501,
            "p95": 42.0974151611328,
            "p99": 92.83778320312493
          },
          "maximum_absolute_error_lux": 354.2421875,
          "worst": {
            "sensor_index": 23,
            "position": [
              3.5,
              0.5,
              0.75
            ],
            "hour_of_year": 2602.5,
            "foton_lux": 34151.7421875,
            "radiance_lux": 34505.984375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.31446347031963406,
            "maximum_error_percentage_points": 1.4210958904109567,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.11477363688561562,
            "maximum_error_percentage_points": 0.5066665400380685,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.07376712328767117,
            "maximum_error_percentage_points": 0.3039726027397265,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.08660958904109665,
            "maximum_error_percentage_points": 0.3039726027397336,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.020878995433790116,
            "maximum_error_percentage_points": 0.11397260273972609,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 61.111111111111114,
          "radiance_percent": 63.888888888888886,
          "difference_percentage_points": 2.7777777777777715,
          "tolerance_percentage_points": 2.7777777777777777,
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
      "maximum_error_percentage_points": 0.004945954623281068,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_wwr20_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_wwr20_grid",
            "maximum_error_percentage_points": 0.004945954623281068,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_wwr20_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_wwr20_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_wwr20_grid",
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
      "study_preparation_seconds": 0.006103040999732912,
      "weather_seconds": 0.08592216693796217,
      "metric_reduction_seconds": 0.12336666602641344,
      "write_seconds": 0.01780708401929587,
      "total_seconds": 0.22760974999982864,
      "cold_end_to_end_seconds": 0.23371279099956155,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0019790410296991467,
      "engine_upload_seconds": 0.001001375,
      "engine_acceleration_structure_seconds": 0.003114959,
      "engine_tracing_seconds": 0.049928499734960496,
      "engine_annual_reduction_seconds": 0.0015412499196827412,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.049928499734960496
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006103040999732912,
      "weather_seconds": 0.07829887501429766,
      "metric_reduction_seconds": 0.04911474999971688,
      "write_seconds": 0.020404040929861367,
      "total_seconds": 0.14793174993246794,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14793174993246794,
      "raw_export_seconds": 0.0030643329955637455,
      "engine_upload_seconds": 4.775e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.002259333385154605,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02003445802256465,
      "full": 0.061384208034724
    }
  },
  "elapsed_seconds": 1.3565865829586983,
  "result_class": "passed"
}
```
