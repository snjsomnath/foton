# Foton report

Status: **passed**

```json
{
  "scene": "courtyard_context",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "courtyard_context",
    "category": "context",
    "question": "How does enclosing context restrict a room's courtyard view?",
    "interactions": [
      "closed_context",
      "courtyard",
      "multiple_obstructions"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 18,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "cb3e924d1247babe58d39c649a3acb275b82974a3274b11ba3543287092e5c1c",
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
      "scene_fingerprint": 4828330442288497760,
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
      "scene_fingerprint": 4828330442288497760,
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
    "model_sha256": "51eefacff3d2ce7d39e1da3d32e708a07944c43faa4fa12312d8e0b7ee1504f4",
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
          "maximum": 0.00015125086065381765,
          "p95": 0.0,
          "p99": 0.0
        },
        "bias_percent": -0.33202337097547235,
        "identifier": "courtyard_context_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.805196136769607,
        "worst_index": [
          23,
          404,
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
          "maximum": 0.0003597661852836609,
          "p95": 1.0527602171350736e-05,
          "p99": 2.666660293471068e-05
        },
        "bias_percent": 0.06079422073169393,
        "identifier": "courtyard_context_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1006881277173937,
        "worst_index": [
          35,
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
          "maximum": 0.00038202106952667236,
          "p95": 9.436851541977376e-06,
          "p99": 2.259502434753813e-05
        },
        "bias_percent": -0.004146662663052636,
        "identifier": "courtyard_context_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0854932766268504,
        "worst_index": [
          21,
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
            "identifier": "courtyard_context_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006543917115777731,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 1.108472370932759,
                "cvrmse_percent": 76.33537301470672,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.31342531043621774,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1050089930658942,
                "relative_energy_error_percent": 0.3134253104362178,
                "rms_normalized_rmse_percent": 5.445360478745545,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0044592577032744884,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0051136494148522615,
                  "rgb_channel": 0,
                  "sky_patch_index": 452
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007493346929550171,
                  "p50": 0.0,
                  "p90": 9.388210537508712e-06,
                  "p95": 1.7790209312806837e-05,
                  "p99": 4.577014078677166e-05
                },
                "candidate_energy": 1.6973950342018043,
                "cvrmse_percent": 86.13203069724489,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.6640425348455895,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.7087418066083728,
                "relative_energy_error_percent": 0.6640425348455896,
                "rms_normalized_rmse_percent": 3.453718853444298,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.021170989610254765,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.020421654917299747,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.6098340395838,
            "full": 234.6260000485927
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 108.57933294028044,
            "full": 251.61741604097188
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.15050002001226,
            "full": 242.63412493746728
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 107.470125076361,
            "full": 236.90283298492432
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.07399996742606,
            "full": 249.12179203238338
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 109.18154090177268,
            "full": 227.1181670948863
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 108.19537495262921,
            "full": 257.22999998833984
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.02770892810076,
            "full": 239.44954096805304
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
            "identifier": "courtyard_context_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002643114421516657,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 1.103191076073017,
                "cvrmse_percent": 40.26088296495597,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.24121961447133272,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1058586239823853,
                "relative_energy_error_percent": 0.24121961447133275,
                "rms_normalized_rmse_percent": 2.870994456995395,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002524508978240192,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.0022601975360885262,
                  "rgb_channel": 0,
                  "sky_patch_index": 417
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010849358513951302,
                  "p50": 9.508982188322079e-07,
                  "p90": 9.82421538537896e-06,
                  "p95": 1.5232140867738053e-05,
                  "p99": 4.120967423659749e-05
                },
                "candidate_energy": 2.5805112561124943,
                "cvrmse_percent": 45.60846147117631,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.27664879772377277,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.573391998089061,
                "relative_energy_error_percent": 0.27664879772377277,
                "rms_normalized_rmse_percent": 2.131405566615526,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.020164585672318935,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.019079649820923805,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.2076249299571,
            "full": 2412.721624947153
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.90716701280326,
            "full": 2428.0260000377893
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 137.68166699446738,
            "full": 2427.7204589452595
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.469041980803,
            "full": 2419.7137500159442
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
            "identifier": "courtyard_context_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00024635251611471176,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 1.1077517054382042,
                "cvrmse_percent": 39.51116599756026,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.15269964801233663,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1060627515098531,
                "relative_energy_error_percent": 0.15269964801233663,
                "rms_normalized_rmse_percent": 2.819378480052664,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00425849505700171,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.004504847573116422,
                  "rgb_channel": 0,
                  "sky_patch_index": 455
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006725592538714409,
                  "p50": 9.576484760742687e-07,
                  "p90": 9.586648536696891e-06,
                  "p95": 1.5140449249884114e-05,
                  "p99": 4.167884253547527e-05
                },
                "candidate_energy": 2.5742637423935903,
                "cvrmse_percent": 41.80827359111333,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.19723077677757622,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.5793510164391336,
                "relative_energy_error_percent": 0.19723077677757622,
                "rms_normalized_rmse_percent": 1.952400752151123,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.026804620400071144,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.027477179653942585,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.6006249859929,
            "full": 2591.9380420818925
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.79816692881286,
            "full": 2637.0543749071658
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.04908403754234,
            "full": 2561.996416072361
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.9472080366686,
            "full": 2572.677250020206
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
            "identifier": "courtyard_context_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00013499963097274303,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 1.1060455533588538,
                "cvrmse_percent": 21.576020566385058,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.04937957867505085,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1054996622833642,
                "relative_energy_error_percent": 0.049379578675050835,
                "rms_normalized_rmse_percent": 1.5404750722716707,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003192600910551846,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.003327600541524589,
                  "rgb_channel": 0,
                  "sky_patch_index": 416
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003345757722854614,
                  "p50": 7.713290628430514e-07,
                  "p90": 6.753560410288632e-06,
                  "p95": 1.0659969348125742e-05,
                  "p99": 2.7347388822818175e-05
                },
                "candidate_energy": 2.5736358352977042,
                "cvrmse_percent": 23.196393322725367,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.3217304342546669,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.5819427308579,
                "relative_energy_error_percent": 0.32173043425466685,
                "rms_normalized_rmse_percent": 1.0842220505294902,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.035742344334721565,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.03607692010700703,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 191.31625001318753,
            "full": 4542.20116592478
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 187.30462493840605,
            "full": 4531.113417004235
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.7375411093235,
            "full": 4470.97024996765
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 191.55312492512167,
            "full": 4546.246874961071
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub/84026bf0-52b9-4ab1-a34a-84203a41be12/scratchpad/suite-0.3.1/run/courtyard_context/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2684.3606249894947,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_context/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10340.470416937023,
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
        "identifier": "courtyard_context_grid",
        "full_identifier": "courtyard_context_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.16839547051163067,
            "cvrmse_percent": 11.045981456368633,
            "rms_normalized_rmse_percent": 0.7894645245898226,
            "reference_energy": 1.1070635565574776,
            "candidate_energy": 1.1051993116725498,
            "relative_energy_error_percent": 0.1683954705116307,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 7.202103734016418e-05
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 457,
              "rgb_channel": 0,
              "reference": 0.002848703181371093,
              "candidate": 0.0027766821440309286,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.8750545790399449,
            "cvrmse_percent": 52.84116418514184,
            "rms_normalized_rmse_percent": 2.467443929459648,
            "reference_energy": 2.57649830003567,
            "candidate_energy": 2.528187550681965,
            "relative_energy_error_percent": 1.8750545790399447,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 7.392482075374573e-07,
              "p90": 5.432541729533119e-06,
              "p95": 8.050148608163e-06,
              "p99": 1.6586101992288604e-05,
              "maximum": 0.0009779520332813263
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03404594212770462,
              "candidate": 0.033067990094423294,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -1.3621325280265217,
            "cvrmse_percent": 36.886103978872946,
            "rms_normalized_rmse_percent": 2.462497556648505,
            "reference_energy": 3.6835618565931476,
            "candidate_energy": 3.6333868623545147,
            "relative_energy_error_percent": 1.3621325280265217,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 7.39333700039424e-07,
              "p90": 5.407059006756764e-06,
              "p95": 8.013912520254962e-06,
              "p99": 1.607414014870301e-05,
              "maximum": 0.0009779520332813263
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03404594212770462,
              "candidate": 0.033067990094423294,
              "position": [
                2.5,
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
        "identifier": "courtyard_context_grid",
        "full_identifier": "courtyard_context_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.16839547051163067,
            "cvrmse_percent": 11.045981456368633,
            "rms_normalized_rmse_percent": 0.7894645245898226,
            "reference_energy": 1.1070635565574776,
            "candidate_energy": 1.1051993116725498,
            "relative_energy_error_percent": 0.1683954705116307,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 7.202103734016418e-05
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 457,
              "rgb_channel": 0,
              "reference": 0.002848703181371093,
              "candidate": 0.0027766821440309286,
              "position": [
                3.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 48.47712079117175,
            "cvrmse_percent": 779.3972647367822,
            "rms_normalized_rmse_percent": 31.12379387983455,
            "reference_energy": 1.7027455389829242,
            "candidate_energy": 2.528187550681965,
            "relative_energy_error_percent": 48.47712079117174,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.730000008137722e-06,
              "p90": 1.418266074324494e-05,
              "p95": 2.2790000002714805e-05,
              "p99": 4.7289999201893806e-05,
              "maximum": 0.0060790665447711945
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.012101592496037483,
              "candidate": 0.018180659040808678,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 29.31080862828927,
            "cvrmse_percent": 472.29985343016466,
            "rms_normalized_rmse_percent": 31.122790321115836,
            "reference_energy": 2.809809095540402,
            "candidate_energy": 3.6333868623545147,
            "relative_energy_error_percent": 29.31080862828927,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.730000008137722e-06,
              "p90": 1.4188314889906934e-05,
              "p95": 2.277000021422282e-05,
              "p99": 4.6989385737106204e-05,
              "maximum": 0.0060790665447711945
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.012101592496037483,
              "candidate": 0.018180659040808678,
              "position": [
                0.5,
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
      "bias_percent": -0.07509713048741863,
      "rms_normalized_error_percent": 0.17864017429580356,
      "absolute_error": {
        "p95": 0.023264265329984102,
        "p99": 0.03355556522622341,
        "maximum": 0.03820678580887105
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.7363552830063895,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.17864017429580356
    },
    "overcast": {
      "bias_percent": -0.09735540500018039,
      "rms_normalized_error_percent": 0.17489863057878371,
      "absolute_error": {
        "p95": 0.02115398645401001,
        "p99": 0.029406487941741936,
        "maximum": 0.031291961669921875
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.2800369262695312,
      "reference_fraction_of_uniform": 0.8332386016845703,
      "rms_normalized_to_uniform_percent": 0.15039930204815008
    },
    "horizon": {
      "bias_percent": 0.6339970306753032,
      "rms_normalized_error_percent": 4.150156444772728,
      "absolute_error": {
        "p95": 0.008530233842449459,
        "p99": 0.010418708726628308,
        "maximum": 0.011154036167092207
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.047282112395774026,
      "reference_fraction_of_uniform": 0.017279230036176416,
      "rms_normalized_to_uniform_percent": 0.04582737161958624
    },
    "north": {
      "bias_percent": 0.26750234291852165,
      "rms_normalized_error_percent": 0.9096988668674392,
      "absolute_error": {
        "p95": 0.008074654266238213,
        "p99": 0.012675246596336358,
        "maximum": 0.014181017875671387
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.3501361608505249,
      "reference_fraction_of_uniform": 0.12795712053775787,
      "rms_normalized_to_uniform_percent": 0.06833365376290176
    },
    "east": {
      "bias_percent": -0.06840167829797213,
      "rms_normalized_error_percent": 0.375925799962659,
      "absolute_error": {
        "p95": 0.009001076221466064,
        "p99": 0.011037957668304442,
        "maximum": 0.011394023895263672
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.4089314639568329,
      "reference_fraction_of_uniform": 0.1494438499212265,
      "rms_normalized_to_uniform_percent": 0.051775503002875006
    },
    "south": {
      "bias_percent": -0.13500663937682605,
      "rms_normalized_error_percent": 0.20689622351932488,
      "absolute_error": {
        "p95": 0.013268589973449707,
        "p99": 0.01792973279953002,
        "maximum": 0.02023911476135254
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.0084452629089355,
      "reference_fraction_of_uniform": 0.36853593587875366,
      "rms_normalized_to_uniform_percent": 0.08658152686421701
    },
    "west": {
      "bias_percent": -0.04115991511354883,
      "rms_normalized_error_percent": 0.3009027112875003,
      "absolute_error": {
        "p95": 0.005834158509969711,
        "p99": 0.007711675018072127,
        "maximum": 0.007940292358398438
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.4077330231666565,
      "reference_fraction_of_uniform": 0.14900587499141693,
      "rms_normalized_to_uniform_percent": 0.041491403959402914
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
        "identifier": "courtyard_context_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.4010637567787493,
          "cvrmse_percent": 3.9569046294370325,
          "absolute_error_percentiles_lux": {
            "p50": 0.5325021743774414,
            "p90": 7.61891021728516,
            "p95": 14.910013961791975,
            "p99": 41.554338226318336
          },
          "maximum_absolute_error_lux": 290.201171875,
          "worst": {
            "sensor_index": 16,
            "position": [
              2.5,
              1.5,
              0.75
            ],
            "hour_of_year": 2868.5,
            "foton_lux": 9869.3359375,
            "radiance_lux": 10159.537109375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2229756468797568,
            "maximum_error_percentage_points": 1.0439726027397258,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.30037158572548267,
            "maximum_error_percentage_points": 0.9474605344066234,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.4341019786910192,
            "maximum_error_percentage_points": 1.2287671232876818,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.4340715372907159,
            "maximum_error_percentage_points": 1.2287671232876711,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0049809741248097944,
            "maximum_error_percentage_points": 0.05972602739726085,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 5.555555555555555,
          "radiance_percent": 5.555555555555555,
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
            "identifier": "courtyard_context_grid",
            "maximum_error_percentage_points": 0.004794520547945602,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "courtyard_context_grid",
            "maximum_error_percentage_points": 0.004832512842462222,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "courtyard_context_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "courtyard_context_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "courtyard_context_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
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
      "study_preparation_seconds": 0.007838250021450222,
      "weather_seconds": 0.10509587498381734,
      "metric_reduction_seconds": 0.147237041965127,
      "write_seconds": 0.031432082992978394,
      "total_seconds": 0.2839193339459598,
      "cold_end_to_end_seconds": 0.29175758396741003,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.011276458040811121,
      "engine_upload_seconds": 0.000881875,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.09275029168929905,
      "engine_annual_reduction_seconds": 0.0014162500156089664,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.09275029168929905
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007838250021450222,
      "weather_seconds": 0.1011914589907974,
      "metric_reduction_seconds": 0.04590420797467232,
      "write_seconds": 0.0343142079655081,
      "total_seconds": 0.1815977079095319,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1815977079095319,
      "raw_export_seconds": 0.018966958043165505,
      "engine_upload_seconds": 9.5417e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0016465834341943264,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013403375050984323,
      "full": 0.09581829200033098
    }
  },
  "elapsed_seconds": 1.2481608339585364,
  "result_class": "passed"
}
```
