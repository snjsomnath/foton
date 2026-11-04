# Foton report

Status: **passed**

```json
{
  "scene": "east_facing",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "east_facing",
    "category": "orientation",
    "question": "Is east-facing glazing assigned to the correct sky patches?",
    "interactions": [
      "east_glazing",
      "sky_patch_order"
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
    "aperture_area": 2.9999999999999987
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "3f2d45df03fe94e5099808c2f4ee059ab30d42856adada5a974dbb4e0d12b398",
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
      "scene_fingerprint": 11084893264255879771,
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 11084893264255879771,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.2)",
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
    "model_sha256": "969c61725f20e38cfb9b7e9601d3d3c786b6be7f2ef102ebf41d31ba6b5cdadd",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "42ebbd5873d9863a0ad3aca60e92d9e55c1ae842623c6cc1f4949849ae92cd10",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0005308212712407112,
          "p95": 3.920438211935105e-06,
          "p99": 9.482726454734802e-05
        },
        "bias_percent": -0.0686826144664144,
        "identifier": "east_facing_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.2763013167518,
        "worst_index": [
          32,
          131,
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
          "maximum": 0.0004746783524751663,
          "p95": 4.671555943787095e-05,
          "p99": 0.00013472791761159897
        },
        "bias_percent": 0.06419073754143312,
        "identifier": "east_facing_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.024973442702285,
        "worst_index": [
          11,
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
          "maximum": 0.00036566704511642456,
          "p95": 3.581177734304219e-05,
          "p99": 0.00011366093531250954
        },
        "bias_percent": -0.02094546235734018,
        "identifier": "east_facing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8246825303828869,
        "worst_index": [
          4,
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
            "identifier": "east_facing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000514989485964179,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.751933738589287e-05,
                  "p99": 0.00023486651480197906
                },
                "candidate_energy": 6.011600192307014,
                "cvrmse_percent": 11.498205194976855,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.04680241074882251,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.014415083558561,
                "relative_energy_error_percent": 0.046802410748822514,
                "rms_normalized_rmse_percent": 2.3505363624916473,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0032784100621938705,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.0027634205762296915,
                  "rgb_channel": 0,
                  "sky_patch_index": 10
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008317809551954269,
                  "p50": 0.0,
                  "p90": 1.6681160559528507e-05,
                  "p95": 0.00012703697429969853,
                  "p99": 0.000401222612708807
                },
                "candidate_energy": 2.041548862785131,
                "cvrmse_percent": 57.115175994412176,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.30577039501871933,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0353254401468774,
                "relative_energy_error_percent": 0.30577039501871933,
                "rms_normalized_rmse_percent": 3.1272697128086953,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02583344466984272,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.026665225625038147,
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.89479095954448,
            "full": 233.3026248961687
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.47620900254697,
            "full": 229.48812507092953
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 114.19324995949864,
            "full": 234.21595804393291
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.36295798234642,
            "full": 226.2145000277087
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
            "identifier": "east_facing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00036535668186843395,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.538597713690241e-05,
                  "p99": 0.00017710542306303978
                },
                "candidate_energy": 6.013954847427158,
                "cvrmse_percent": 8.095193708551289,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.003350023015285662,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.014156323048155,
                "relative_energy_error_percent": 0.0033500230152856626,
                "rms_normalized_rmse_percent": 1.656039327047794,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0072650795336812735,
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "reference": 0.0068997228518128395,
                  "rgb_channel": 0,
                  "sky_patch_index": 89
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006278641521930695,
                  "p50": 2.6773457761919417e-07,
                  "p90": 2.920479528256692e-05,
                  "p95": 8.14218001323751e-05,
                  "p99": 0.0002650319365784526
                },
                "candidate_energy": 3.775946915374174,
                "cvrmse_percent": 21.38105250559426,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1552569404001649,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7700935834263234,
                "relative_energy_error_percent": 0.1552569404001649,
                "rms_normalized_rmse_percent": 1.8436036814473933,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.020767120644450188,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.021394984796643257,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 154.52683391049504,
            "full": 2262.352833058685
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.95933303423226,
            "full": 2302.0269999979064
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.30200004205108,
            "full": 2263.153583975509
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.69129199907184,
            "full": 2241.341583081521
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
            "identifier": "east_facing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000303150387480855,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.694039234891533e-05,
                  "p99": 0.00018275436013936996
                },
                "candidate_energy": 6.0136954890131165,
                "cvrmse_percent": 8.443156581675934,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.014828414128091367,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.0145873569344985,
                "relative_energy_error_percent": 0.014828414128091369,
                "rms_normalized_rmse_percent": 1.7261138584523976,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0074050710536539555,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.0077082214411348104,
                  "rgb_channel": 0,
                  "sky_patch_index": 39
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007742205634713173,
                  "p50": 3.0103490544775013e-07,
                  "p90": 3.086309152422473e-05,
                  "p95": 8.618396823294389e-05,
                  "p99": 0.00027033197693526745
                },
                "candidate_energy": 3.7816768355590717,
                "cvrmse_percent": 22.299296221528362,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.13027172540504953,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7767567893252654,
                "relative_energy_error_percent": 0.13027172540504953,
                "rms_normalized_rmse_percent": 1.9216628370447701,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.028193780221045017,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.028968000784516335,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.27349994145334,
            "full": 2436.702042003162
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.02525001950562,
            "full": 2458.492874982767
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.53512502647936,
            "full": 2413.7915420578793
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.06320795509964,
            "full": 2464.6466249832883
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
            "identifier": "east_facing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00020452146418392658,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3153144866228087e-05,
                  "p99": 8.874648483470082e-05
                },
                "candidate_energy": 6.011454909892564,
                "cvrmse_percent": 4.332714106850885,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.007393812559344925,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.011010467045708,
                "relative_energy_error_percent": 0.007393812559344925,
                "rms_normalized_rmse_percent": 0.8855008723132997,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004137798445299268,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.003933276981115341,
                  "rgb_channel": 0,
                  "sky_patch_index": 116
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005427412688732147,
                  "p50": 2.3675767657493907e-07,
                  "p90": 1.9195707864128053e-05,
                  "p95": 4.383628838695571e-05,
                  "p99": 0.000148785300552845
                },
                "candidate_energy": 3.780957519507421,
                "cvrmse_percent": 12.79786976492637,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.046742705700724176,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.779191023369499,
                "relative_energy_error_percent": 0.04674270570072418,
                "rms_normalized_rmse_percent": 1.104932548203873,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03134937584400177,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.030806634575128555,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 236.52466607745737,
            "full": 4295.970750041306
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 233.31720801070333,
            "full": 4247.706708032638
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 218.9487499417737,
            "full": 4235.635832999833
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 215.82616702653468,
            "full": 4266.777624958195
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
    "/Users/ssanjay/GitHub/foton-release-0.3.2/validation/results/2026-11-04-architectural-v4-metal-0.3.2-release/east_facing/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 818.5577499680221,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/east_facing/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2786.942334030755,
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
        "identifier": "east_facing_grid",
        "full_identifier": "east_facing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.05560779401580021,
            "cvrmse_percent": 3.337376173042436,
            "rms_normalized_rmse_percent": 0.6825867527442264,
            "reference_energy": 6.013580994041149,
            "candidate_energy": 6.016925013773289,
            "relative_energy_error_percent": 0.055607794015800224,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.6223715394735336e-06,
              "p99": 5.300762131810188e-05,
              "maximum": 0.00035939039662480354
            },
            "worst": {
              "global_sensor_index": 25,
              "local_sensor_index": 25,
              "sky_patch_index": 94,
              "rgb_channel": 0,
              "reference": 0.0009222719818353653,
              "candidate": 0.0012816623784601688,
              "position": [
                4.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.16835120054704583,
            "cvrmse_percent": 15.41057906490297,
            "rms_normalized_rmse_percent": 1.329369711274734,
            "reference_energy": 3.777725944099549,
            "candidate_energy": 3.784085791079818,
            "relative_energy_error_percent": 0.16835120054704586,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.667791865311301e-07,
              "p90": 3.625531098805368e-05,
              "p95": 5.4859228839632036e-05,
              "p99": 0.00013568252325057983,
              "maximum": 0.0007512439042329788
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.023683663457632065,
              "candidate": 0.022932419553399086,
              "position": [
                3.5,
                5.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.09910696063064307,
            "cvrmse_percent": 5.7630133921802695,
            "rms_normalized_rmse_percent": 1.2885066568109849,
            "reference_energy": 9.791306938140698,
            "candidate_energy": 9.801010804853107,
            "relative_energy_error_percent": 0.09910696063064309,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.701751544824219e-07,
              "p90": 3.622056101448834e-05,
              "p95": 5.322599317878474e-05,
              "p99": 0.0001241664867848158,
              "maximum": 0.0007512439042329788
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.023683663457632065,
              "candidate": 0.022932419553399086,
              "position": [
                3.5,
                5.5,
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
        "identifier": "east_facing_grid",
        "full_identifier": "east_facing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.05560779401580021,
            "cvrmse_percent": 3.337376173042436,
            "rms_normalized_rmse_percent": 0.6825867527442264,
            "reference_energy": 6.013580994041149,
            "candidate_energy": 6.016925013773289,
            "relative_energy_error_percent": 0.055607794015800224,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.6223715394735336e-06,
              "p99": 5.300762131810188e-05,
              "maximum": 0.00035939039662480354
            },
            "worst": {
              "global_sensor_index": 25,
              "local_sensor_index": 25,
              "sky_patch_index": 94,
              "rgb_channel": 0,
              "reference": 0.0009222719818353653,
              "candidate": 0.0012816623784601688,
              "position": [
                4.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 85.68884972096501,
            "cvrmse_percent": 469.7066340349483,
            "rms_normalized_rmse_percent": 25.742482553146953,
            "reference_energy": 2.0378637687541126,
            "candidate_energy": 3.784085791079818,
            "relative_energy_error_percent": 85.688849720965,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002172423992305994,
              "p95": 0.00029299036250449715,
              "p99": 0.0005542589351534843,
              "maximum": 0.008243595249950886
            },
            "worst": {
              "global_sensor_index": 30,
              "local_sensor_index": 30,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011243355460464954,
              "candidate": 0.01948695071041584,
              "position": [
                5.5,
                5.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.7298397194796,
            "cvrmse_percent": 118.89190746390781,
            "rms_normalized_rmse_percent": 25.743921204814466,
            "reference_energy": 8.051444762795262,
            "candidate_energy": 9.801010804853107,
            "relative_energy_error_percent": 21.7298397194796,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00021786626166431233,
              "p95": 0.00029255240224301777,
              "p99": 0.0005706658121198416,
              "maximum": 0.008243595249950886
            },
            "worst": {
              "global_sensor_index": 30,
              "local_sensor_index": 30,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011243355460464954,
              "candidate": 0.01948695071041584,
              "position": [
                5.5,
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
      "bias_percent": 0.2945991182878051,
      "rms_normalized_error_percent": 0.2922324332143567,
      "absolute_error": {
        "p95": 0.12374715746025067,
        "p99": 0.14146137180530458,
        "maximum": 0.1427782584869406
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 12.013767645939529,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2922324332143567
    },
    "overcast": {
      "bias_percent": 0.22859442073276445,
      "rms_normalized_error_percent": 0.22505100947596718,
      "absolute_error": {
        "p95": 0.06689870357513428,
        "p99": 0.07536931037902832,
        "maximum": 0.07723617553710938
      },
      "worst_index": [
        26
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.622777938842773,
      "reference_fraction_of_uniform": 0.6345035433769226,
      "rms_normalized_to_uniform_percent": 0.15850794989173939
    },
    "horizon": {
      "bias_percent": 1.1466249109257887,
      "rms_normalized_error_percent": 2.1385093828586497,
      "absolute_error": {
        "p95": 0.07852596567503162,
        "p99": 0.11878314268119888,
        "maximum": 0.1282842731193068
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.5548169133561744,
      "reference_fraction_of_uniform": 0.12941959251906116,
      "rms_normalized_to_uniform_percent": 0.16652393751421235
    },
    "north": {
      "bias_percent": 0.022361426152081063,
      "rms_normalized_error_percent": 0.3512972167758862,
      "absolute_error": {
        "p95": 0.024589993059635162,
        "p99": 0.03752220124006269,
        "maximum": 0.0428011417388916
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.300008773803711,
      "reference_fraction_of_uniform": 0.19144774973392487,
      "rms_normalized_to_uniform_percent": 0.07126009951053733
    },
    "east": {
      "bias_percent": 0.3633353575881969,
      "rms_normalized_error_percent": 0.3666140412122664,
      "absolute_error": {
        "p95": 0.10275888442993164,
        "p99": 0.1353078246116638,
        "maximum": 0.14104318618774414
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.40697193145752,
      "reference_fraction_of_uniform": 0.699778139591217,
      "rms_normalized_to_uniform_percent": 0.2402978391487386
    },
    "south": {
      "bias_percent": 0.42936515204008524,
      "rms_normalized_error_percent": 0.45078277519742477,
      "absolute_error": {
        "p95": 0.03595311939716339,
        "p99": 0.05452103614807126,
        "maximum": 0.06281661987304688
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.293274164199829,
      "reference_fraction_of_uniform": 0.1908871829509735,
      "rms_normalized_to_uniform_percent": 0.09121119108467542
    },
    "west": {
      "bias_percent": -38.568848106462056,
      "rms_normalized_error_percent": 99.98811706102191,
      "absolute_error": {
        "p95": 0.00038519358963640116,
        "p99": 0.0004839851493215973,
        "maximum": 0.0005215270793996751
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 0.00010079436469823122,
      "reference_fraction_of_uniform": 8.389904905925505e-06,
      "rms_normalized_to_uniform_percent": 0.0007297588320526394
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
        "identifier": "east_facing_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.31967896503189874,
          "cvrmse_percent": 1.83091214652223,
          "absolute_error_percentiles_lux": {
            "p50": 1.3996315002441406,
            "p90": 17.496063232421896,
            "p95": 29.01659240722655,
            "p99": 61.923943481445306
          },
          "maximum_absolute_error_lux": 170.887451171875,
          "worst": {
            "sensor_index": 2,
            "position": [
              0.5,
              3.5,
              0.75
            ],
            "hour_of_year": 5743.5,
            "foton_lux": 3121.96435546875,
            "radiance_lux": 2951.076904296875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2644786910197864,
            "maximum_error_percentage_points": 1.3387671232876706,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.28372902478512035,
            "maximum_error_percentage_points": 1.0647746039688997,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.32507229832572276,
            "maximum_error_percentage_points": 1.5383561643835648,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.32739345509893525,
            "maximum_error_percentage_points": 1.5383561643835648,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.007956621004566101,
            "maximum_error_percentage_points": 0.0320547945205476,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 27.77777777777778,
          "radiance_percent": 27.77777777777778,
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
      "maximum_error_percentage_points": 0.00479452054794649,
      "metrics": {
        "da": [
          {
            "identifier": "east_facing_grid",
            "maximum_error_percentage_points": 0.004657534246572226,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "east_facing_grid",
            "maximum_error_percentage_points": 0.004789035744863668,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "east_facing_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "east_facing_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "east_facing_grid",
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
      "study_preparation_seconds": 0.00591808301396668,
      "weather_seconds": 0.07422700000461191,
      "metric_reduction_seconds": 0.03552995796781033,
      "write_seconds": 0.02111854194663465,
      "total_seconds": 0.1309969169087708,
      "cold_end_to_end_seconds": 0.13691499992273748,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.00742466701194644,
      "engine_upload_seconds": 0.000263625,
      "engine_acceleration_structure_seconds": 0.002975458,
      "engine_tracing_seconds": 0.01380112487822771,
      "engine_annual_reduction_seconds": 0.00035829166881740093,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.01380112487822771
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.00591808301396668,
      "weather_seconds": 0.07245387509465218,
      "metric_reduction_seconds": 0.01335862500127405,
      "write_seconds": 0.030268457951024175,
      "total_seconds": 0.11619700002484024,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.11619700002484024,
      "raw_export_seconds": 0.0017031249590218067,
      "engine_upload_seconds": 4.6625e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0003772915806621313,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.010906999930739403,
      "full": 0.023579875007271767
    }
  },
  "elapsed_seconds": 0.73908970807679,
  "result_class": "passed"
}
```
