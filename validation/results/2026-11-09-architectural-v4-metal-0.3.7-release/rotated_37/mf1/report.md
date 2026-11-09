# Foton report

Status: **passed**

```json
{
  "scene": "rotated_37",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "rotated_37",
    "category": "orientation",
    "question": "Does an oblique room retain its glazing, shades and grids?",
    "interactions": [
      "oblique_orientation",
      "transformed_shades",
      "transformed_sensors"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 3,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "a03707750ead568a3406bab957508af65d94c6b235a3601953a440ce6b2dc137",
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 2776987180082579249,
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 2776987180082579249,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.7)",
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/7fb068ed-087d-41c3-b9b3-215cbbd36098/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "adcb0225a47d7a1010aec02b0ed759ae0cd50071b40e1b28d4f8fecc95266447",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "d72001511e1894b58caccd7133c7a63bc6631d4a71cabd08f0bdf10f34efbfbc",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00031960924388840795,
          "p95": 0.0,
          "p99": 6.006305920891464e-05
        },
        "bias_percent": -0.17009643107224248,
        "identifier": "rotated_37_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.5007483356957938,
        "worst_index": [
          16,
          68,
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
          "maximum": 0.0008216984570026398,
          "p95": 2.6652905580703905e-05,
          "p99": 0.0001278407871723175
        },
        "bias_percent": 0.17050691586954714,
        "identifier": "rotated_37_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3521227967039804,
        "worst_index": [
          16,
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
          "maximum": 0.00056442990899086,
          "p95": 2.022921253228558e-05,
          "p99": 9.646313264966011e-05
        },
        "bias_percent": -0.12191903734590734,
        "identifier": "rotated_37_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0239597138878245,
        "worst_index": [
          23,
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
            "identifier": "rotated_37_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004281951696611941,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00013942259829491377
                },
                "candidate_energy": 2.3449127613239398,
                "cvrmse_percent": 17.631791238228917,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.07781894914181732,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.3430893937802466,
                "relative_energy_error_percent": 0.07781894914181733,
                "rms_normalized_rmse_percent": 2.563362218379496,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0008613336831331253,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.0012895288527943194,
                  "rgb_channel": 0,
                  "sky_patch_index": 9
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011704647913575172,
                  "p50": 0.0,
                  "p90": 9.451065125176683e-06,
                  "p95": 3.986048195656615e-05,
                  "p99": 0.00028775143437087536
                },
                "candidate_energy": 1.8202360819779955,
                "cvrmse_percent": 48.23833564227367,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.18289554081230747,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.8169130290673934,
                "relative_energy_error_percent": 0.1828955408123075,
                "rms_normalized_rmse_percent": 3.1883609630990604,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00036045489832758904,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0008100098930299282,
                  "rgb_channel": 0,
                  "sky_patch_index": 95
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 122.14158300776035,
            "full": 232.8249589772895
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 112.80154203996062,
            "full": 234.225207939744
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.64791600964963,
            "full": 237.06145805772394
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 108.32066705916077,
            "full": 233.92183310352266
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
            "identifier": "rotated_37_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003008861094713211,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00011762534268200397
                },
                "candidate_energy": 2.343014265117745,
                "cvrmse_percent": 15.068705619545595,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.09592216044847143,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.345263892912044,
                "relative_energy_error_percent": 0.09592216044847145,
                "rms_normalized_rmse_percent": 2.1951776906692153,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00709895440377295,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.007399840513244271,
                  "rgb_channel": 0,
                  "sky_patch_index": 44
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006182948127388954,
                  "p50": 2.426141989531061e-07,
                  "p90": 1.7085752915591e-05,
                  "p95": 4.060395785927529e-05,
                  "p99": 0.00024228959227912128
                },
                "candidate_energy": 2.9480745109438686,
                "cvrmse_percent": 23.866916557403666,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.07094273056483465,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.9501674402822395,
                "relative_energy_error_percent": 0.07094273056483463,
                "rms_normalized_rmse_percent": 2.063193577657379,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.01971999928355217,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.019101704470813274,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.7238329043612,
            "full": 2426.571207935922
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 137.00779201462865,
            "full": 2410.224042017944
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 137.98016600776464,
            "full": 2439.3582500051707
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.4750410001725,
            "full": 2455.055958009325
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
            "identifier": "rotated_37_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00041966885328292847,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00018116086721420288
                },
                "candidate_energy": 2.343497936084532,
                "cvrmse_percent": 21.652370032871797,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.011512544761945213,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.343767763397409,
                "relative_energy_error_percent": 0.011512544761945213,
                "rms_normalized_rmse_percent": 3.1537225829852336,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007902097888290882,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.007482429035007954,
                  "rgb_channel": 0,
                  "sky_patch_index": 43
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010328292846679688,
                  "p50": 2.448782225883406e-07,
                  "p90": 1.7590500647202134e-05,
                  "p95": 4.3037445129812006e-05,
                  "p99": 0.00025764014571905136
                },
                "candidate_energy": 2.9561226838210004,
                "cvrmse_percent": 27.3226007872894,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.17087319985428723,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.9611825511997623,
                "relative_energy_error_percent": 0.17087319985428723,
                "rms_normalized_rmse_percent": 2.361439111310223,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.033485595136880875,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.03451842442154884,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.26324993371964,
            "full": 2578.4854580415413
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.62150004692376,
            "full": 2600.6190419429913
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.80020897462964,
            "full": 2595.282332971692
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.21029200032353,
            "full": 2535.8913330128416
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
            "identifier": "rotated_37_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00015973811969161034,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.930816016392782e-05
                },
                "candidate_energy": 2.3448472680984196,
                "cvrmse_percent": 7.932041567225783,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.07440765397489328,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.346593313131052,
                "relative_energy_error_percent": 0.07440765397489328,
                "rms_normalized_rmse_percent": 1.1559712145881862,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007047360995784402,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.0068876228760927916,
                  "rgb_channel": 0,
                  "sky_patch_index": 70
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005430104210972786,
                  "p50": 2.2686850620345922e-07,
                  "p90": 1.1945350706810132e-05,
                  "p95": 2.5121737053268582e-05,
                  "p99": 0.00011709984391927719
                },
                "candidate_energy": 2.951668323712802,
                "cvrmse_percent": 14.152528535244603,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.10633437107827654,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.9485330196703003,
                "relative_energy_error_percent": 0.10633437107827654,
                "rms_normalized_rmse_percent": 1.2222461005814782,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02063562534749508,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.0200926149263978,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 198.01208400167525,
            "full": 4510.388916009106
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 214.0723749762401,
            "full": 4497.001542011276
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 193.47233406733721,
            "full": 4493.1425410322845
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 196.1505829822272,
            "full": 4467.521167011
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub/7fb068ed-087d-41c3-b9b3-215cbbd36098/scratchpad/suite-metal-0.3.7/rotated_37/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 815.1935839559883,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rotated_37/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2715.93579207547,
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
        "identifier": "rotated_37_grid",
        "full_identifier": "rotated_37_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.09253307559155403,
            "cvrmse_percent": 5.899033308424058,
            "rms_normalized_rmse_percent": 0.8596684383044791,
            "reference_energy": 2.3471065742937753,
            "candidate_energy": 2.3449347243931697,
            "relative_energy_error_percent": 0.09253307559155403,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.1582749215886e-05,
              "maximum": 0.0002345321699976921
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 97,
              "rgb_channel": 0,
              "reference": 0.006579566281288862,
              "candidate": 0.00634503411129117,
              "position": [
                4.903855312903767,
                1.304318736457792,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.4949701640107318,
            "cvrmse_percent": 20.102349762220467,
            "rms_normalized_rmse_percent": 1.7370971809921696,
            "reference_energy": 2.9487143739053643,
            "candidate_energy": 2.934119117532637,
            "relative_energy_error_percent": 0.4949701640107318,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.132323342924792e-07,
              "p90": 2.2542350052390248e-05,
              "p95": 3.9106770418584344e-05,
              "p99": 9.925756603479385e-05,
              "maximum": 0.0010948553681373596
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01962207444012165,
              "candidate": 0.01852721907198429,
              "position": [
                1.304318736457792,
                1.0961446870962328,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.31661014292854267,
            "cvrmse_percent": 11.164960612447935,
            "rms_normalized_rmse_percent": 1.7327466669859533,
            "reference_energy": 5.29582094819914,
            "candidate_energy": 5.279053841925807,
            "relative_energy_error_percent": 0.31661014292854267,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.126520056184745e-07,
              "p90": 2.248605596832931e-05,
              "p95": 3.862325538648292e-05,
              "p99": 9.901312296278775e-05,
              "maximum": 0.0010948553681373596
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01962207444012165,
              "candidate": 0.01852721907198429,
              "position": [
                1.304318736457792,
                1.0961446870962328,
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
        "identifier": "rotated_37_grid",
        "full_identifier": "rotated_37_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.09253307559155403,
            "cvrmse_percent": 5.899033308424058,
            "rms_normalized_rmse_percent": 0.8596684383044791,
            "reference_energy": 2.3471065742937753,
            "candidate_energy": 2.3449347243931697,
            "relative_energy_error_percent": 0.09253307559155403,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 3.1582749215886e-05,
              "maximum": 0.0002345321699976921
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
              "sky_patch_index": 97,
              "rgb_channel": 0,
              "reference": 0.006579566281288862,
              "candidate": 0.00634503411129117,
              "position": [
                4.903855312903767,
                1.304318736457792,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 61.61769048460494,
            "cvrmse_percent": 451.5167109148816,
            "rms_normalized_rmse_percent": 29.81500265100904,
            "reference_energy": 1.815469029865966,
            "candidate_energy": 2.934119117532637,
            "relative_energy_error_percent": 61.61769048460495,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00012085666458006017,
              "p95": 0.00018631797902344258,
              "p99": 0.0004189722239971161,
              "maximum": 0.007174665108323097
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.012494014576077461,
              "candidate": 0.01966867968440056,
              "position": [
                5.2974962866942565,
                4.105219802856475,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 26.821812837473686,
            "cvrmse_percent": 196.90123227165589,
            "rms_normalized_rmse_percent": 29.81142581465783,
            "reference_energy": 4.162575604159741,
            "candidate_energy": 5.279053841925807,
            "relative_energy_error_percent": 26.82181283747369,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00011965999874519184,
              "p95": 0.00018581686836114384,
              "p99": 0.0003906411584466696,
              "maximum": 0.007174665108323097
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.012494014576077461,
              "candidate": 0.01966867968440056,
              "position": [
                5.2974962866942565,
                4.105219802856475,
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
      "bias_percent": 0.009340745401012266,
      "rms_normalized_error_percent": 0.5176941805976051,
      "absolute_error": {
        "p95": 0.08877918960676712,
        "p99": 0.10160632006541165,
        "maximum": 0.10418422800709948
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.932731185169831,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.5176941805976051
    },
    "overcast": {
      "bias_percent": -0.03451581891847176,
      "rms_normalized_error_percent": 0.44006398229642596,
      "absolute_error": {
        "p95": 0.04590499401092529,
        "p99": 0.054376527667045586,
        "maximum": 0.05562227964401245
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.742835760116577,
      "reference_fraction_of_uniform": 0.5560480952262878,
      "rms_normalized_to_uniform_percent": 0.26906788940400445
    },
    "horizon": {
      "bias_percent": 0.422707883328567,
      "rms_normalized_error_percent": 2.6328600379826814,
      "absolute_error": {
        "p95": 0.03741708726564938,
        "p99": 0.05171286037348258,
        "maximum": 0.05580598927385649
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.7428774255545688,
      "reference_fraction_of_uniform": 0.15060164393065179,
      "rms_normalized_to_uniform_percent": 0.2639907162462383
    },
    "north": {
      "bias_percent": 1.2586969328984088,
      "rms_normalized_error_percent": 8.55671221231471,
      "absolute_error": {
        "p95": 0.001649999525398016,
        "p99": 0.0023596610408276315,
        "maximum": 0.002454071305692196
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": true,
      "reference_mean": 0.0064283618703484535,
      "reference_fraction_of_uniform": 0.0013032053830102086,
      "rms_normalized_to_uniform_percent": 0.010136449594143712
    },
    "east": {
      "bias_percent": -0.15351174180474766,
      "rms_normalized_error_percent": 0.6408695431761186,
      "absolute_error": {
        "p95": 0.05708432197570801,
        "p99": 0.06683416962623594,
        "maximum": 0.07165908813476562
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.6325466632843018,
      "reference_fraction_of_uniform": 0.5336894392967224,
      "rms_normalized_to_uniform_percent": 0.3409665510516874
    },
    "south": {
      "bias_percent": 0.13769118526959256,
      "rms_normalized_error_percent": 0.5167912984812865,
      "absolute_error": {
        "p95": 0.05160602927207947,
        "p99": 0.07211737036705013,
        "maximum": 0.08288025856018066
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.2078287601470947,
      "reference_fraction_of_uniform": 0.6503149271011353,
      "rms_normalized_to_uniform_percent": 0.33873980391591313
    },
    "west": {
      "bias_percent": 0.21997697948643502,
      "rms_normalized_error_percent": 1.0840211376680176,
      "absolute_error": {
        "p95": 0.0043960073962807655,
        "p99": 0.005802329257130622,
        "maximum": 0.006161808967590332
      },
      "worst_index": [
        29
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.08462986350059509,
      "reference_fraction_of_uniform": 0.017156796529889107,
      "rms_normalized_to_uniform_percent": 0.0269792137049079
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
        "identifier": "rotated_37_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.0837808171223748,
          "cvrmse_percent": 2.664505111849464,
          "absolute_error_percentiles_lux": {
            "p50": 1.3949203491210938,
            "p90": 15.400131225585959,
            "p95": 24.58082885742187,
            "p99": 50.477741088866985
          },
          "maximum_absolute_error_lux": 183.3984375,
          "worst": {
            "sensor_index": 17,
            "position": [
              4.105219802856475,
              0.7025037133057439,
              0.75
            ],
            "hour_of_year": 2722.5,
            "foton_lux": 33476.66796875,
            "radiance_lux": 33660.06640625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.5064307458143068,
            "maximum_error_percentage_points": 2.4090410958904105,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.2667559558741307,
            "maximum_error_percentage_points": 1.6017663480047801,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.2306392694063929,
            "maximum_error_percentage_points": 1.4201369863013724,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.2293455098934558,
            "maximum_error_percentage_points": 1.4201369863013724,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.014478691019786978,
            "maximum_error_percentage_points": 0.08589041095890426,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 13.88888888888889,
          "radiance_percent": 13.88888888888889,
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
      "maximum_error_percentage_points": 0.004954516267133613,
      "metrics": {
        "da": [
          {
            "identifier": "rotated_37_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "rotated_37_grid",
            "maximum_error_percentage_points": 0.004954516267133613,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "rotated_37_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "rotated_37_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "rotated_37_grid",
            "maximum_error_percentage_points": 0.004246575342465753,
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
      "study_preparation_seconds": 0.006689124973490834,
      "weather_seconds": 0.07692904211580753,
      "metric_reduction_seconds": 0.0460736658424139,
      "write_seconds": 0.019024124834686518,
      "total_seconds": 0.1421665831003338,
      "cold_end_to_end_seconds": 0.14885570807382464,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.001774708041921258,
      "engine_upload_seconds": 0.000264375,
      "engine_acceleration_structure_seconds": 0.003322875,
      "engine_tracing_seconds": 0.024960374925285578,
      "engine_annual_reduction_seconds": 0.00035300012677907944,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.024960374925285578
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006689124973490834,
      "weather_seconds": 0.07225625007413328,
      "metric_reduction_seconds": 0.012629457982257009,
      "write_seconds": 0.012813041917979717,
      "total_seconds": 0.09790295897983015,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.09790295897983015,
      "raw_export_seconds": 0.001989291049540043,
      "engine_upload_seconds": 5.2416e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00036925007589161396,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01812970801256597,
      "full": 0.01848979201167822
    }
  },
  "elapsed_seconds": 0.7252635830081999,
  "result_class": "passed"
}
```
