# Foton report

Status: **passed**

```json
{
  "scene": "coloured_walls",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "coloured_walls",
    "category": "materials",
    "question": "Do coloured diffuse walls preserve RGB reflected transport?",
    "interactions": [
      "spectral_reflection",
      "surface_specific_materials"
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
    "aperture_area": 2.999999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "a43e8570ba5df3b1bc6c5827f6518a1a6493a529ded70b5a1b649744f71795a1",
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 7819928560470180135,
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 7819928560470180135,
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/foton-references-corpus4-2026-11-03",
    "model_sha256": "c465368276f3f56dcb0b634f953aa5b7bbd9853532027f26bf53bfb2f73a2ac6",
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
          "maximum": 0.00014028436271473765,
          "p95": 3.259629011154175e-08,
          "p99": 7.011898560449481e-06
        },
        "bias_percent": -0.02574736435175291,
        "identifier": "coloured_walls_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7597631247218805,
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
          "maximum": 0.00058705173432827,
          "p95": 2.2552793961949615e-05,
          "p99": 0.00010068394592963146
        },
        "bias_percent": 0.18231324939864735,
        "identifier": "coloured_walls_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.851289422793028,
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
          "maximum": 0.0007002316415309906,
          "p95": 1.9211938706575886e-05,
          "p99": 8.211308915633685e-05
        },
        "bias_percent": -0.06385989717107518,
        "identifier": "coloured_walls_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.5768943570491558,
        "worst_index": [
          18,
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
            "identifier": "coloured_walls_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0008171797962859273,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.428122388664633e-05,
                  "p99": 0.00021224763986538164
                },
                "candidate_energy": 6.013656371010711,
                "cvrmse_percent": 41.29589551632076,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.1318360713474736,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.005738641130847,
                "relative_energy_error_percent": 0.1318360713474736,
                "rms_normalized_rmse_percent": 7.949844106676617,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004245119285769761,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0034279394894838333,
                  "rgb_channel": 0,
                  "sky_patch_index": 364
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011947203893214464,
                  "p50": 0.0,
                  "p90": 1.896262665468395e-06,
                  "p95": 4.766693090516581e-05,
                  "p99": 0.00028312845097389045
                },
                "candidate_energy": 1.8242537128664198,
                "cvrmse_percent": 177.94584783914175,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.6505815386539344,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.8361996890562406,
                "relative_energy_error_percent": 0.6505815386539344,
                "rms_normalized_rmse_percent": 6.173927946350122,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.012076607206836343,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.01327132759615779,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 119.96466701384634,
            "full": 226.1930829845369
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 109.16454205289483,
            "full": 231.17337503936142
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 109.7678750520572,
            "full": 231.8404580000788
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 111.92083300556988,
            "full": 224.48333399370313
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.14479203894734,
            "full": 237.44499997701496
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 122.93716706335545,
            "full": 232.69929189700633
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 115.08329096250236,
            "full": 230.3406250430271
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.03599991090596,
            "full": 235.9122079797089
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
            "identifier": "coloured_walls_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00027292402228340507,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2355496184900403e-05,
                  "p99": 0.00011757100583054125
                },
                "candidate_energy": 6.012441132450476,
                "cvrmse_percent": 23.393032846198494,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.04001144328277586,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.014847759850454,
                "relative_energy_error_percent": 0.04001144328277586,
                "rms_normalized_rmse_percent": 4.507672127207816,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0014210329973138869,
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "reference": 0.001693957019597292,
                  "rgb_channel": 0,
                  "sky_patch_index": 259
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006084016204113141,
                  "p50": 6.582791201026339e-09,
                  "p90": 1.1876461530846453e-05,
                  "p95": 3.694537226692773e-05,
                  "p99": 0.00019902491068933114
                },
                "candidate_energy": 3.155394488330248,
                "cvrmse_percent": 71.30615138329564,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.03871306455005051,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.154173411141572,
                "relative_energy_error_percent": 0.03871306455005898,
                "rms_normalized_rmse_percent": 3.3872040168510313,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0005804593383800238,
                  "global_sensor_index": 32,
                  "local_sensor_index": 32,
                  "reference": 0.001188860958791338,
                  "rgb_channel": 0,
                  "sky_patch_index": 37
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.17920901905745,
            "full": 2407.6865420211107
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.48399995733052,
            "full": 2402.06312504597
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.37395797297359,
            "full": 2398.2647920493037
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.2243749992922,
            "full": 2351.4464169275016
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
            "identifier": "coloured_walls_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005039101233705878,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2907915990799665e-05,
                  "p99": 0.00014073893544264138
                },
                "candidate_energy": 6.016273752016787,
                "cvrmse_percent": 26.418118818420343,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0288580987073645,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.014538070683557,
                "relative_energy_error_percent": 0.028858098707364496,
                "rms_normalized_rmse_percent": 5.092319198362783,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003625390469096601,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.004129300592467189,
                  "rgb_channel": 0,
                  "sky_patch_index": 358
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013038050383329391,
                  "p50": 4.962127819752027e-09,
                  "p90": 1.1735240605048606e-05,
                  "p95": 3.841813695544257e-05,
                  "p99": 0.00019830227829515905
                },
                "candidate_energy": 3.166864709595986,
                "cvrmse_percent": 74.74130273473537,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.18111560314431047,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.172610802786874,
                "relative_energy_error_percent": 0.18111560314428365,
                "rms_normalized_rmse_percent": 3.558835186649487,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.035635629668831825,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.036939434707164764,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.13999996334314,
            "full": 2712.538417079486
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.80820899736136,
            "full": 2688.9092080527917
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 165.915249963291,
            "full": 2684.2392499092966
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.08537508826703,
            "full": 2662.340624956414
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
            "identifier": "coloured_walls_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001928189303725958,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1350595741532743e-05,
                  "p99": 6.873396341688931e-05
                },
                "candidate_energy": 6.017509063352463,
                "cvrmse_percent": 13.12531492939282,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.03323350309197659,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.015509898684286,
                "relative_energy_error_percent": 0.03323350309197659,
                "rms_normalized_rmse_percent": 2.531212709103128,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003773353062570095,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.003966171992942691,
                  "rgb_channel": 0,
                  "sky_patch_index": 357
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005438253283500671,
                  "p50": 8.03442278679567e-09,
                  "p90": 8.048691915973908e-06,
                  "p95": 2.2214503223949545e-05,
                  "p99": 0.00010703618310799298
                },
                "candidate_energy": 3.161930343895004,
                "cvrmse_percent": 40.482198780631336,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.052990232764021004,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.163606746473699,
                "relative_energy_error_percent": 0.05299023276403279,
                "rms_normalized_rmse_percent": 1.9252901589386728,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03177694045007229,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.032320765778422356,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 216.12712496425956,
            "full": 5057.559459004551
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 198.28437501564622,
            "full": 5054.410458076745
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 201.40049990732223,
            "full": 5071.44274993334
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 219.69858300872147,
            "full": 5103.760500089265
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/coloured_walls/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2700.813874951564,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/coloured_walls/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 11016.199042089283,
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
        "identifier": "coloured_walls_grid",
        "full_identifier": "coloured_walls_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.02545918042736604,
            "cvrmse_percent": 2.1862248649500637,
            "rms_normalized_rmse_percent": 0.4217274666145703,
            "reference_energy": 6.016160269848569,
            "candidate_energy": 6.014628604750669,
            "relative_energy_error_percent": 0.02545918042736604,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.1525920601561666e-08,
              "p99": 6.127869710326195e-06,
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
            "nmbe_percent": -1.610430849003406,
            "cvrmse_percent": 54.66025574916002,
            "rms_normalized_rmse_percent": 2.599449884737501,
            "reference_energy": 3.1631177688985193,
            "candidate_energy": 3.1121779445578692,
            "relative_energy_error_percent": 1.6104308490034065,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 9.914397747223802e-09,
              "p90": 8.67495909915306e-06,
              "p95": 1.6003303608158602e-05,
              "p99": 4.5963423108332726e-05,
              "maximum": 0.0011024661362171173
            },
            "worst": {
              "global_sensor_index": 28,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03642137721180916,
              "candidate": 0.03531891107559204,
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
            "nmbe_percent": -0.5716298081075697,
            "cvrmse_percent": 18.799904974729685,
            "rms_normalized_rmse_percent": 2.594529462046533,
            "reference_energy": 9.17927803874709,
            "candidate_energy": 9.126806549308538,
            "relative_energy_error_percent": 0.5716298081075747,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 9.914397747223802e-09,
              "p90": 8.676897141413065e-06,
              "p95": 1.598455255589215e-05,
              "p99": 4.4943362008780205e-05,
              "maximum": 0.0011024661362171173
            },
            "worst": {
              "global_sensor_index": 28,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03642137721180916,
              "candidate": 0.03531891107559204,
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
        "identifier": "coloured_walls_grid",
        "full_identifier": "coloured_walls_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.02545918042736604,
            "cvrmse_percent": 2.1862248649500637,
            "rms_normalized_rmse_percent": 0.4217274666145703,
            "reference_energy": 6.016160269848569,
            "candidate_energy": 6.014628604750669,
            "relative_energy_error_percent": 0.02545918042736604,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.1525920601561666e-08,
              "p99": 6.127869710326195e-06,
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
            "nmbe_percent": 70.64587743358943,
            "cvrmse_percent": 1006.9189102975549,
            "rms_normalized_rmse_percent": 34.76175426416868,
            "reference_energy": 1.8237639205606013,
            "candidate_energy": 3.1121779445578692,
            "relative_energy_error_percent": 70.64587743358945,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.730233013106046e-05,
              "p95": 7.93919723946601e-05,
              "p99": 0.00014643263810285094,
              "maximum": 0.01367915142327547
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.012415687553584576,
              "candidate": 0.026094838976860046,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 16.41447452353751,
            "cvrmse_percent": 234.22622683990107,
            "rms_normalized_rmse_percent": 34.76049511902344,
            "reference_energy": 7.839924190409171,
            "candidate_energy": 9.126806549308538,
            "relative_energy_error_percent": 16.414474523537507,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.7156999426079026e-05,
              "p95": 7.922507987245808e-05,
              "p99": 0.00014578408246961744,
              "maximum": 0.01367915142327547
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.012415687553584576,
              "candidate": 0.026094838976860046,
              "position": [
                5.5,
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
      "bias_percent": 0.11157235161903842,
      "rms_normalized_error_percent": 0.12103053982024368,
      "absolute_error": {
        "p95": 0.04504758640365425,
        "p99": 0.05975626592716389,
        "maximum": 0.06633762166943669
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 11.410519173801216,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.12103053982024368
    },
    "overcast": {
      "bias_percent": 0.09129777977073418,
      "rms_normalized_error_percent": 0.0945757318271436,
      "absolute_error": {
        "p95": 0.025698930025100708,
        "p99": 0.03439472317695617,
        "maximum": 0.0369110107421875
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.372922897338867,
      "reference_fraction_of_uniform": 0.6461513638496399,
      "rms_normalized_to_uniform_percent": 0.06751922268598441
    },
    "horizon": {
      "bias_percent": 0.47934662851823484,
      "rms_normalized_error_percent": 1.2422620153810846,
      "absolute_error": {
        "p95": 0.028825355197062086,
        "p99": 0.04280647924998594,
        "maximum": 0.04781495082708864
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1987573962362057,
      "reference_fraction_of_uniform": 0.10505721764076932,
      "rms_normalized_to_uniform_percent": 0.07500515972308078
    },
    "north": {
      "bias_percent": -87.08743027205085,
      "rms_normalized_error_percent": 99.20857479560264,
      "absolute_error": {
        "p95": 3.0027490140582813e-05,
        "p99": 7.83809191489126e-05,
        "maximum": 9.062319441e-05
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 7.80575555836549e-06,
      "reference_fraction_of_uniform": 6.84084170643473e-07,
      "rms_normalized_to_uniform_percent": 8.856762673902721e-05
    },
    "east": {
      "bias_percent": -0.017391147410968033,
      "rms_normalized_error_percent": 0.1500458355279008,
      "absolute_error": {
        "p95": 0.013187825679779053,
        "p99": 0.017888069152832024,
        "maximum": 0.019373416900634766
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.1373393535614014,
      "reference_fraction_of_uniform": 0.18731306493282318,
      "rms_normalized_to_uniform_percent": 0.029965438639549393
    },
    "south": {
      "bias_percent": 0.1487368519664829,
      "rms_normalized_error_percent": 0.1639614496305017,
      "absolute_error": {
        "p95": 0.04601788520812988,
        "p99": 0.057538366317749,
        "maximum": 0.0627584457397461
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.917000770568848,
      "reference_fraction_of_uniform": 0.6938335299491882,
      "rms_normalized_to_uniform_percent": 0.10691140941546017
    },
    "west": {
      "bias_percent": 0.08043826159008727,
      "rms_normalized_error_percent": 0.1678688487117499,
      "absolute_error": {
        "p95": 0.014695882797241211,
        "p99": 0.017860770225524902,
        "maximum": 0.01825547218322754
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.16275954246521,
      "reference_fraction_of_uniform": 0.18954084813594818,
      "rms_normalized_to_uniform_percent": 0.033777257149413924
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
        "identifier": "coloured_walls_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.001470142723061572,
          "cvrmse_percent": 1.6882260751866283,
          "absolute_error_percentiles_lux": {
            "p50": 1.508209228515625,
            "p90": 19.309631347656254,
            "p95": 31.208319091796874,
            "p99": 75.54953124999975
          },
          "maximum_absolute_error_lux": 341.552734375,
          "worst": {
            "sensor_index": 17,
            "position": [
              2.5,
              0.5,
              0.75
            ],
            "hour_of_year": 6829.5,
            "foton_lux": 16549.345703125,
            "radiance_lux": 16207.79296875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.24475646879756457,
            "maximum_error_percentage_points": 1.2593150684931516,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1047881694770633,
            "maximum_error_percentage_points": 0.5082279295083509,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.09694063926940652,
            "maximum_error_percentage_points": 0.7438356164383606,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.0997070015220708,
            "maximum_error_percentage_points": 0.6321917808219126,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.021423135464231455,
            "maximum_error_percentage_points": 0.11164383561643842,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 38.888888888888886,
          "radiance_percent": 38.888888888888886,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.7777777777777777,
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
            "identifier": "coloured_walls_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "coloured_walls_grid",
            "maximum_error_percentage_points": 0.00452803938355828,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "coloured_walls_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "coloured_walls_grid",
            "maximum_error_percentage_points": 0.004794520547953596,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "coloured_walls_grid",
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
      "study_preparation_seconds": 0.006584499962627888,
      "weather_seconds": 0.09697779198177159,
      "metric_reduction_seconds": 0.1218602090375498,
      "write_seconds": 0.042893624980933964,
      "total_seconds": 0.2618601249996573,
      "cold_end_to_end_seconds": 0.26844462496228516,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.019715250004082918,
      "engine_upload_seconds": 0.000919375,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.07043804158456624,
      "engine_annual_reduction_seconds": 0.0016859166789799929,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.07043804158456624
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006584499962627888,
      "weather_seconds": 0.10877799999434501,
      "metric_reduction_seconds": 0.043903709040023386,
      "write_seconds": 0.04066150006838143,
      "total_seconds": 0.19371891696937382,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.19371891696937382,
      "raw_export_seconds": 0.011507458984851837,
      "engine_upload_seconds": 6.3041e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0018565832870081067,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.019621834042482078,
      "full": 0.07378791691735387
    }
  },
  "elapsed_seconds": 1.2192522919503972,
  "result_class": "passed"
}
```
