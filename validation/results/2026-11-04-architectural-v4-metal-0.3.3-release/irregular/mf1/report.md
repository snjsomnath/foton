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
  "sky_density": 1,
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 5737655811555480342,
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
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.3)",
      "weather_id": "aff05f88fed2459a6796dca3cabd63daf743bc359ea5c7394adb01155f6785fb"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/usr/local/radiance/bin/gendaymtx",
      "weather_id": "fa596a1b71c81c8eee4f32b17ea6d10a57aabce8541ff637ac4a9c1ee69c4ac1"
    },
    "sun_up_hours_equal": true,
    "compared_hours": 4405,
    "max_relative_difference": 0.0,
    "mean_relative_difference": 0.0
  },
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 65536,
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
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0003254120238125324,
          "p95": 6.251735612750053e-06,
          "p99": 0.00011040223762392998
        },
        "bias_percent": -0.10206692341571803,
        "identifier": "irregular_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9897713926942276,
        "worst_index": [
          9,
          72,
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
          "maximum": 0.0004888903349637985,
          "p95": 5.139806307852268e-05,
          "p99": 0.0001636762171983719
        },
        "bias_percent": 0.04197681718276041,
        "identifier": "irregular_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0538868852530898,
        "worst_index": [
          14,
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
          "maximum": 0.00037735141813755035,
          "p95": 5.1836250349879265e-05,
          "p99": 0.0001334547996520996
        },
        "bias_percent": -0.028689682467824586,
        "identifier": "irregular_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8422752991411153,
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
          "rms_normalized_rmse_percent": 5.0
        },
        "grids": [
          {
            "identifier": "irregular_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0011272234842181206,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.00014074881619308144,
                  "p99": 0.000545385992154479
                },
                "candidate_energy": 5.326012398334569,
                "cvrmse_percent": 20.42223130695624,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.1474931980659811,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.333879507801612,
                "relative_energy_error_percent": 0.1474931980659811,
                "rms_normalized_rmse_percent": 4.674268617157855,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.008161235600709915,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.007034012116491795,
                  "rgb_channel": 0,
                  "sky_patch_index": 46
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0014767629327252507,
                  "p50": 0.0,
                  "p90": 4.0386752516496927e-05,
                  "p95": 0.0002264147624373436,
                  "p99": 0.0006685382686555386
                },
                "candidate_energy": 1.4746879715561931,
                "cvrmse_percent": 89.13034714020401,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.6259371062772123,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.4839767325738933,
                "relative_energy_error_percent": 0.6259371062772123,
                "rms_normalized_rmse_percent": 4.5989084964947295,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0006144879152998328,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": -0.0008622750174254179,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 106.08612501528114,
            "full": 183.50637494586408
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 98.00604195334017,
            "full": 180.46841700561345
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 95.05054098553956,
            "full": 178.33383299876004
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 105.51008302718401,
            "full": 186.5514579694718
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
          "rms_normalized_rmse_percent": 5.0
        },
        "grids": [
          {
            "identifier": "irregular_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00042140495497733355,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.416987162083387e-05,
                  "p99": 0.0002025809371843934
                },
                "candidate_energy": 5.333617595911164,
                "cvrmse_percent": 7.768825051218794,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.11403270402939379,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.33970660774321,
                "relative_energy_error_percent": 0.1140327040293938,
                "rms_normalized_rmse_percent": 1.7767169184499103,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0019661745755001903,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.002387579530477524,
                  "rgb_channel": 0,
                  "sky_patch_index": 15
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007933899760246277,
                  "p50": 2.403025973762851e-07,
                  "p90": 3.596223541535437e-05,
                  "p95": 0.00010818988084793091,
                  "p99": 0.0003154166042804718
                },
                "candidate_energy": 2.7260768202243533,
                "cvrmse_percent": 23.50985136475669,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.18896429987901467,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.720935224028107,
                "relative_energy_error_percent": 0.18896429987901467,
                "rms_normalized_rmse_percent": 1.9039066006149963,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.036235494539141655,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.03702888451516628,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 129.14470792748034,
            "full": 1675.3797499695793
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.33333296515048,
            "full": 1646.08187507838
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 119.74108300637454,
            "full": 1664.136499981396
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.4754999903962,
            "full": 1661.5945419762284
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
          "rms_normalized_rmse_percent": 5.0
        },
        "grids": [
          {
            "identifier": "irregular_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003379050176590681,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.618606857955456e-05,
                  "p99": 0.00016251369379460812
                },
                "candidate_energy": 5.336810426131706,
                "cvrmse_percent": 6.00642731904917,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.12299647493906828,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.330254401113052,
                "relative_energy_error_percent": 0.12299647493906829,
                "rms_normalized_rmse_percent": 1.372862775905532,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002385772531852126,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.002047867514193058,
                  "rgb_channel": 0,
                  "sky_patch_index": 13
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010592807084321976,
                  "p50": 2.2065327698328474e-07,
                  "p90": 3.446199116297066e-05,
                  "p95": 0.00010157492943108082,
                  "p99": 0.0002743904769886285
                },
                "candidate_energy": 2.7232082138437264,
                "cvrmse_percent": 22.778790829576007,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.497720195430998,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.736829969315618,
                "relative_energy_error_percent": 0.497720195430998,
                "rms_normalized_rmse_percent": 1.8535050357262115,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.028851214796304703,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.0299104955047369,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.57704096939415,
            "full": 1721.6660409467295
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.12266703601927,
            "full": 1752.665458014235
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 126.44208304118365,
            "full": 1753.899791976437
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.74695791956037,
            "full": 1751.7285000067204
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
          "rms_normalized_rmse_percent": 5.0
        },
        "grids": [
          {
            "identifier": "irregular_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00020847981795668602,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.4425524063408375e-05,
                  "p99": 0.00012045027688145638
                },
                "candidate_energy": 5.334703350319614,
                "cvrmse_percent": 4.343145378309935,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.023447183654307827,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.335954481366571,
                "relative_energy_error_percent": 0.02344718365430783,
                "rms_normalized_rmse_percent": 0.9921508671038254,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013174924999475479,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.013383404817432165,
                  "rgb_channel": 0,
                  "sky_patch_index": 75
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007165335118770599,
                  "p50": 1.7586099865241067e-07,
                  "p90": 2.2766304027754813e-05,
                  "p95": 6.335973739624023e-05,
                  "p99": 0.00020148511976003647
                },
                "candidate_energy": 2.726003221351629,
                "cvrmse_percent": 15.355812935495601,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.006899052227966298,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.725815165939693,
                "relative_energy_error_percent": 0.006899052227966297,
                "rms_normalized_rmse_percent": 1.2466898246083227,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.033333294093608856,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.032616760581731796,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 182.2540839202702,
            "full": 3007.1183749241754
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 168.60704100690782,
            "full": 3043.8337919767946
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 170.22508394438773,
            "full": 2978.061791975051
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 172.08966705948114,
            "full": 2999.205250060186
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
    "/Users/ssanjay/GitHub/foton-0.3.3/validation/results/2026-11-04-architectural-v4-metal-0.3.3-release/irregular/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 471.4937499957159,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/irregular/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1555.7696250034496,
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
        "identifier": "irregular_grid",
        "full_identifier": "irregular_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.050881984057356444,
            "cvrmse_percent": 2.978640693250752,
            "rms_normalized_rmse_percent": 0.6807278910027041,
            "reference_energy": 5.335683251440969,
            "candidate_energy": 5.33296834993962,
            "relative_energy_error_percent": 0.050881984057356444,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.41819429397583e-06,
              "p99": 5.921628326177597e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.99147615644362,
            "cvrmse_percent": 20.918904220954513,
            "rms_normalized_rmse_percent": 1.6974850376796102,
            "reference_energy": 2.725554857889138,
            "candidate_energy": 2.6985316313423766,
            "relative_energy_error_percent": 0.9914761564436199,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.267023309192155e-07,
              "p90": 3.878120332956314e-05,
              "p95": 6.191828288137913e-05,
              "p99": 0.0001412034034729004,
              "maximum": 0.0011907350271940231
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02430090494453907,
              "candidate": 0.023110169917345047,
              "position": [
                0.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.3689027373312767,
            "cvrmse_percent": 6.99083305601167,
            "rms_normalized_rmse_percent": 1.6778099914379123,
            "reference_energy": 8.061238109330107,
            "candidate_energy": 8.031499981281996,
            "relative_energy_error_percent": 0.3689027373312767,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.129105258878553e-07,
              "p90": 3.7940219044685364e-05,
              "p95": 6.14621676504612e-05,
              "p99": 0.00012882775627076626,
              "maximum": 0.0011907350271940231
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02430090494453907,
              "candidate": 0.023110169917345047,
              "position": [
                0.5,
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
        "identifier": "irregular_grid",
        "full_identifier": "irregular_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.050881984057356444,
            "cvrmse_percent": 2.978640693250752,
            "rms_normalized_rmse_percent": 0.6807278910027041,
            "reference_energy": 5.335683251440969,
            "candidate_energy": 5.33296834993962,
            "relative_energy_error_percent": 0.050881984057356444,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.41819429397583e-06,
              "p99": 5.921628326177597e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 83.125725993151,
            "cvrmse_percent": 472.94409533496815,
            "rms_normalized_rmse_percent": 24.29067579068734,
            "reference_energy": 1.473595048815426,
            "candidate_energy": 2.6985316313423766,
            "relative_energy_error_percent": 83.12572599315101,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00023416802287101746,
              "p95": 0.00032099196687340736,
              "p99": 0.0006409280467778444,
              "maximum": 0.010514507070183754
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.018792102113366127,
              "candidate": 0.02930660918354988,
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
            "nmbe_percent": 17.94935714376045,
            "cvrmse_percent": 102.31816807110627,
            "rms_normalized_rmse_percent": 24.283175377444163,
            "reference_energy": 6.809278300256395,
            "candidate_energy": 8.031499981281996,
            "relative_energy_error_percent": 17.94935714376045,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00023372727446258068,
              "p95": 0.00031857998692430556,
              "p99": 0.0006133196875452995,
              "maximum": 0.010514507070183754
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.018792102113366127,
              "candidate": 0.02930660918354988,
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
      "bias_percent": 0.03520867641653386,
      "rms_normalized_error_percent": 0.1163376590333757,
      "absolute_error": {
        "p95": 0.0634031767309733,
        "p99": 0.06522816430192159,
        "maximum": 0.0654633139677454
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.443155397523585,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.1163376590333757
    },
    "overcast": {
      "bias_percent": 0.012789726623257627,
      "rms_normalized_error_percent": 0.12778423637276803,
      "absolute_error": {
        "p95": 0.04826316833496093,
        "p99": 0.05753576755523681,
        "maximum": 0.0601048469543457
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.11250114440918,
      "reference_fraction_of_uniform": 0.6548209190368652,
      "rms_normalized_to_uniform_percent": 0.09041743348510983
    },
    "horizon": {
      "bias_percent": 0.34597916147646324,
      "rms_normalized_error_percent": 1.7843692665170354,
      "absolute_error": {
        "p95": 0.04530676898163909,
        "p99": 0.05952718749039723,
        "maximum": 0.0635022162446035
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.122031050301951,
      "reference_fraction_of_uniform": 0.07265555655043635,
      "rms_normalized_to_uniform_percent": 0.08642774284116
    },
    "north": {
      "bias_percent": -53.14794766201901,
      "rms_normalized_error_percent": 107.09176860759544,
      "absolute_error": {
        "p95": 0.00014860489172860972,
        "p99": 0.00018077360487950498,
        "maximum": 0.00018850619380827993
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 3.2956817449303344e-05,
      "reference_fraction_of_uniform": 2.1340727016649907e-06,
      "rms_normalized_to_uniform_percent": 0.0002548746714371933
    },
    "east": {
      "bias_percent": -0.044121974286983626,
      "rms_normalized_error_percent": 0.2717859181036688,
      "absolute_error": {
        "p95": 0.033640456199645966,
        "p99": 0.03927420139312744,
        "maximum": 0.04031181335449219
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.5373785495758057,
      "reference_fraction_of_uniform": 0.22905801236629486,
      "rms_normalized_to_uniform_percent": 0.058553907203921896
    },
    "south": {
      "bias_percent": 0.07305086691055611,
      "rms_normalized_error_percent": 0.14447449971340592,
      "absolute_error": {
        "p95": 0.05249922275543212,
        "p99": 0.05907962560653686,
        "maximum": 0.060784101486206055
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.330764770507812,
      "reference_fraction_of_uniform": 0.6689542531967163,
      "rms_normalized_to_uniform_percent": 0.09358077738626809
    },
    "west": {
      "bias_percent": -0.015986840819257265,
      "rms_normalized_error_percent": 0.27322706040281863,
      "absolute_error": {
        "p95": 0.02533566132187842,
        "p99": 0.033929400444030755,
        "maximum": 0.0361933708190918
      },
      "worst_index": [
        20
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.7475521564483643,
      "reference_fraction_of_uniform": 0.17791390419006348,
      "rms_normalized_to_uniform_percent": 0.05545428478725561
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
          "nmbe_percent": -0.05019921822114592,
          "cvrmse_percent": 1.3558811197854213,
          "absolute_error_percentiles_lux": {
            "p50": 2.246490478515625,
            "p90": 25.503466796875003,
            "p95": 38.600769042968736,
            "p99": 75.04319915771477
          },
          "maximum_absolute_error_lux": 327.14453125,
          "worst": {
            "sensor_index": 20,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 5410.03759765625,
            "radiance_lux": 5737.18212890625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.24343607305936107,
            "maximum_error_percentage_points": 0.9039726027397279,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.13441065137268815,
            "maximum_error_percentage_points": 0.5952665857800241,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.10079908675799103,
            "maximum_error_percentage_points": 0.35438356164383933,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.09484018264840473,
            "maximum_error_percentage_points": 0.35890410958904795,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.03314497716894954,
            "maximum_error_percentage_points": 0.25123287671232575,
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
      "maximum_error_percentage_points": 0.004931506849310097,
      "metrics": {
        "da": [
          {
            "identifier": "irregular_grid",
            "maximum_error_percentage_points": 0.004520547945212172,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "irregular_grid",
            "maximum_error_percentage_points": 0.004480682791097479,
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
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "irregular_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
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
      "study_preparation_seconds": 0.005776792066171765,
      "weather_seconds": 0.07460283290129155,
      "metric_reduction_seconds": 0.029701792052946985,
      "write_seconds": 0.011200624983757734,
      "total_seconds": 0.11562679091002792,
      "cold_end_to_end_seconds": 0.12140358297619969,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0014284170465543866,
      "engine_upload_seconds": 0.000282625,
      "engine_acceleration_structure_seconds": 0.00289775,
      "engine_tracing_seconds": 0.008892666664905846,
      "engine_annual_reduction_seconds": 0.00027299998328089714,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.008892666664905846
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.005776792066171765,
      "weather_seconds": 0.07323237496893853,
      "metric_reduction_seconds": 0.012489333050325513,
      "write_seconds": 0.010026709060184658,
      "total_seconds": 0.0958566670306027,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.0958566670306027,
      "raw_export_seconds": 0.0016502079088240862,
      "engine_upload_seconds": 6.1708e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0002639999147504568,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01510650001000613,
      "full": 0.016939874971285462
    }
  },
  "elapsed_seconds": 0.6224946250440553,
  "result_class": "passed"
}
```
