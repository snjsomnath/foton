# Foton report

Status: **incomplete**

```json
{
  "scene": "interior_glazing",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "interior_glazing",
    "category": "connections",
    "question": "Does daylight pass through a shared glazed wall exactly once?",
    "interactions": [
      "borrowed_light",
      "paired_apertures",
      "room_isolation"
    ],
    "room_count": 2,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 2,
    "apertures": 3,
    "shades": 0,
    "sensors": 72,
    "floor_area": 72.0,
    "aperture_area": 8.999999999999996
  },
  "sky_density": 1,
  "status": "incomplete",
  "passed": false,
  "model_sha256": "fe7bfddabdcefca3d3a2166bee3dbc58c76aa7766da22462edde6db28cbc3a1d",
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 14976319759523577797,
      "basis": "Tregenza",
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 14976319759523577797,
      "basis": "Tregenza",
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
  "oracle_stable": false,
  "reference_source": {
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "c2e4f531547371b27c1dd0c370034fddec9ce9182e94e0b6d120f538dd23366b",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "66350f82bb3c17b7ccff8c0b3c7367203ce64ce6f95104e2c7e1fadb06f6afaf",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00012598984176293015,
          "p95": 1.3630085959448458e-06,
          "p99": 2.2667227312922478e-05
        },
        "bias_percent": -0.03254693500733346,
        "identifier": "interior_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.3334157331607479,
        "worst_index": [
          16,
          94,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 2.5623623514547944e-05,
          "p95": 0.0,
          "p99": 0.0
        },
        "bias_percent": 0.12119452503198108,
        "identifier": "adjacent_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.2060619661767238,
        "worst_index": [
          19,
          21,
          0
        ]
      }
    ],
    "passed": true,
    "samples_per_patch": [
      4096,
      16384
    ]
  },
  "depth_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00045165233314037323,
          "p95": 4.097922501387065e-05,
          "p99": 0.0001440979540348053
        },
        "bias_percent": 0.06024719864245726,
        "identifier": "interior_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0022800739307087,
        "worst_index": [
          9,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00015332363545894623,
          "p95": 4.601403361448316e-06,
          "p99": 1.6721982319722883e-05
        },
        "bias_percent": 1.4615844450157696,
        "identifier": "adjacent_grid",
        "passed": false,
        "rms_normalized_error_percent": 4.338897117254662,
        "worst_index": [
          3,
          0,
          0
        ]
      }
    ],
    "passed": false
  },
  "sample_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00029516033828258514,
          "p95": 3.7823313323315224e-05,
          "p99": 0.00012481026351451874
        },
        "bias_percent": 0.04134777203938683,
        "identifier": "interior_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8763912572221235,
        "worst_index": [
          23,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00010807812213897705,
          "p95": 4.272905675861692e-06,
          "p99": 1.268397318199277e-05
        },
        "bias_percent": -0.788166966400347,
        "identifier": "adjacent_grid",
        "passed": true,
        "rms_normalized_error_percent": 3.4257525544903658,
        "worst_index": [
          2,
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
            "identifier": "interior_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007597273215651512,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 8.01584101282057e-05,
                  "p99": 0.00032518169609829783
                },
                "candidate_energy": 6.022832521786086,
                "cvrmse_percent": 15.036792152337284,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.018356003131175438,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.023938276084664,
                "relative_energy_error_percent": 0.018356003131175438,
                "rms_normalized_rmse_percent": 3.081131588110921,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.01300110761076212,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.012241380289196968,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010468794498592615,
                  "p50": 0.0,
                  "p90": 1.3195175597502384e-05,
                  "p95": 0.00013360291413846393,
                  "p99": 0.0004381577018648386
                },
                "candidate_energy": 2.02043461566112,
                "cvrmse_percent": 65.60811614355144,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.9586858755276412,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0012489248841074,
                "relative_energy_error_percent": 0.9586858755276411,
                "rms_normalized_rmse_percent": 3.5315667099831014,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00024393992498517036,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.0008029395248740911,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "adjacent_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00023886075359769166,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.06391744458596804,
                "cvrmse_percent": 164.0867601958471,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.3740447394153321,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.06415742204808339,
                "relative_energy_error_percent": 0.37404473941533206,
                "rms_normalized_rmse_percent": 10.727795955721406,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001354944979539141,
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "reference": 0.0011160842259414494,
                  "rgb_channel": 0,
                  "sky_patch_index": 19
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003025150945177302,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.398710057605058e-05
                },
                "candidate_energy": 0.0692860026053097,
                "cvrmse_percent": 269.28798365809376,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -1.754214929611053,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.07052312987846676,
                "relative_energy_error_percent": 1.7542149296110527,
                "rms_normalized_rmse_percent": 12.367289313809568,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00017743823991622776,
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "reference": 0.00012507685460150242,
                  "rgb_channel": 0,
                  "sky_patch_index": 19
                }
              }
            },
            "start_sensor_index": 36
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 221.18608397431672,
            "full": 377.15299997944385
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 129.8082920257002,
            "full": 383.44674999825656
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 133.01883300300688,
            "full": 416.28179198596627
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.53279200661927,
            "full": 394.80279106646776
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 128.71545902453363,
            "full": 385.38454193621874
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.74287500604987,
            "full": 427.1705410210416
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.1797500345856,
            "full": 376.2968329247087
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 128.1868750229478,
            "full": 380.60400006361306
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
            "identifier": "interior_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003637145273387432,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.6505157843057495e-05,
                  "p99": 0.00018805917352437973
                },
                "candidate_energy": 6.025263098743153,
                "cvrmse_percent": 8.920646573652961,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.08134981381927359,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.020365542583022,
                "relative_energy_error_percent": 0.0813498138192736,
                "rms_normalized_rmse_percent": 1.825576248018469,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.014826359692960978,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.014462645165622234,
                  "rgb_channel": 0,
                  "sky_patch_index": 95
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010053645819425583,
                  "p50": 2.3782189018106692e-07,
                  "p90": 2.8943250072188675e-05,
                  "p95": 9.494388941675406e-05,
                  "p99": 0.00031534547451883554
                },
                "candidate_energy": 3.6200679214365827,
                "cvrmse_percent": 24.641473524446248,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.0664411159317693,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.6176643049017407,
                "relative_energy_error_percent": 0.0664411159317693,
                "rms_normalized_rmse_percent": 2.0628611307529723,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03138475492596626,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.030379390344023705,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "adjacent_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00010857070446945727,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.06357240663328412,
                "cvrmse_percent": 86.16499299618964,
                "energy_difference_negligible": true,
                "nmbe_percent": -1.4954960820643703,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.06453756336486549,
                "relative_energy_error_percent": 1.49549608206437,
                "rms_normalized_rmse_percent": 5.555480475457376,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0009898418502416462,
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "reference": 0.0010984125547111034,
                  "rgb_channel": 0,
                  "sky_patch_index": 20
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0003602780634537339,
                  "p50": 0.0,
                  "p90": 4.000046686769565e-06,
                  "p95": 7.052615200109346e-06,
                  "p99": 2.6270201487932354e-05
                },
                "candidate_energy": 0.16521023796142842,
                "cvrmse_percent": 80.63714048976522,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.8146271100111664,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.16656713903235598,
                "relative_energy_error_percent": 0.8146271100111664,
                "rms_normalized_rmse_percent": 6.720914789816106,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.003577232942916453,
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "reference": 0.003937511006370187,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 36
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 201.38433296233416,
            "full": 5003.684040973894
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 217.65816595871001,
            "full": 4979.875584016554
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.23808294069022,
            "full": 5061.273041996174
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 183.00637498032302,
            "full": 5130.969875026494
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
            "identifier": "interior_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004196468507871032,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.649724287446582e-05,
                  "p99": 0.00018993648700416088
                },
                "candidate_energy": 6.029150883936154,
                "cvrmse_percent": 8.39989592130731,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.014824604166049506,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.030044814210896,
                "relative_energy_error_percent": 0.014824604166049506,
                "rms_normalized_rmse_percent": 1.721928045072386,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003819831879809499,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.0034001850290223956,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006649261340498924,
                  "p50": 2.1923023041381384e-07,
                  "p90": 2.9809121770085767e-05,
                  "p95": 7.793329423293447e-05,
                  "p99": 0.00029573170468211174
                },
                "candidate_energy": 3.617795418993474,
                "cvrmse_percent": 23.71882395164858,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.005306776196841608,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.61798741748855,
                "relative_energy_error_percent": 0.005306776196841607,
                "rms_normalized_rmse_percent": 1.9815322551067671,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.030905735678970814,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.03024080954492092,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "adjacent_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001286788028664887,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.06430002668457746,
                "cvrmse_percent": 106.98866959872778,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.6488287094687197,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.06388551909549278,
                "relative_energy_error_percent": 0.6488287094687197,
                "rms_normalized_rmse_percent": 6.895276796436246,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0009917201823554933,
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "reference": 0.001120398985221982,
                  "rgb_channel": 0,
                  "sky_patch_index": 49
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00015683704987168312,
                  "p50": 0.0,
                  "p90": 3.984705472248606e-06,
                  "p95": 6.569731306171869e-06,
                  "p99": 1.850776516221231e-05
                },
                "candidate_energy": 0.1685337637940627,
                "cvrmse_percent": 63.44306560753494,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.7981143674133939,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.16988967772070396,
                "relative_energy_error_percent": 0.7981143674133939,
                "rms_normalized_rmse_percent": 5.350892604362133,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -2.7379021048545837e-05,
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "reference": 0.00012945802882313728,
                  "rgb_channel": 0,
                  "sky_patch_index": 20
                }
              }
            },
            "start_sensor_index": 36
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.61533307749778,
            "full": 5490.290667046793
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 185.07904198486358,
            "full": 5456.647041020915
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 183.44716599676758,
            "full": 5418.8487499486655
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 198.5712080495432,
            "full": 5381.118084071204
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
            "identifier": "interior_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00019702245481312275,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3468921426683654e-05,
                  "p99": 9.967992082238197e-05
                },
                "candidate_energy": 6.02306453330533,
                "cvrmse_percent": 4.703269471155023,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.005120681910834891,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.022756127121795,
                "relative_energy_error_percent": 0.005120681910834892,
                "rms_normalized_rmse_percent": 0.9631244359273149,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007167492061853409,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.006970469607040286,
                  "rgb_channel": 0,
                  "sky_patch_index": 45
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004805205389857292,
                  "p50": 1.5231552730199382e-07,
                  "p90": 2.0284751371946186e-05,
                  "p95": 5.6456675520166724e-05,
                  "p99": 0.00015496485866606236
                },
                "candidate_energy": 3.631176508697113,
                "cvrmse_percent": 13.773783357353182,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.14388209011942812,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.6259594025218824,
                "relative_energy_error_percent": 0.14388209011942812,
                "rms_normalized_rmse_percent": 1.1534339383522911,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.026328199543058872,
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "reference": 0.0268087200820446,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "adjacent_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 6.85601553414017e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.06423675049836675,
                "cvrmse_percent": 50.60989860861889,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.37534649516704516,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.0644787692990576,
                "relative_energy_error_percent": 0.37534649516704516,
                "rms_normalized_rmse_percent": 3.2874434482166413,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0010166915017180145,
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "reference": 0.0009481313463766128,
                  "rgb_channel": 0,
                  "sky_patch_index": 51
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0001348581281490624,
                  "p50": 9.562128866491548e-12,
                  "p90": 2.7542134830582654e-06,
                  "p95": 4.4224137752735255e-06,
                  "p99": 1.6259742551483214e-05
                },
                "candidate_energy": 0.16797694998381374,
                "cvrmse_percent": 50.47610252175609,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 1.0455367225709322,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.16623886163820245,
                "relative_energy_error_percent": 1.045536722570932,
                "rms_normalized_rmse_percent": 4.223640892122153,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -3.406745963729918e-05,
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "reference": 0.00010079066851176322,
                  "rgb_channel": 0,
                  "sky_patch_index": 51
                }
              }
            },
            "start_sensor_index": 36
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 305.1850829506293,
            "full": 9424.155957996845
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 304.8240420175716,
            "full": 9494.709457969293
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 298.99233393371105,
            "full": 9367.2692499822
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
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "72",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 305.7465000310913,
            "full": 9317.748541943729
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
    "/content/suite-vulkan-0.3.2/interior_glazing/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2637.144917040132,
      "invocation_count": 5,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 11074.72074998077,
      "invocation_count": 5,
      "sample_count": 1024,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/direct_4096/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/direct_4096/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 44690.786625025794,
      "invocation_count": 5,
      "sample_count": 4096,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/direct_16384/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf1/direct_16384/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 163234.4787500333,
      "invocation_count": 5,
      "sample_count": 16384,
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
      72,
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
        "identifier": "interior_glazing_grid",
        "full_identifier": "interior_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.1512333788854345,
            "cvrmse_percent": 3.1505325255229595,
            "rms_normalized_rmse_percent": 0.6450933617846402,
            "reference_energy": 6.023460207225753,
            "candidate_energy": 6.014350724828546,
            "relative_energy_error_percent": 0.15123337888543453,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.406652831472425e-06,
              "p99": 5.4307631216943264e-05,
              "maximum": 0.00028031491092406213
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 42,
              "rgb_channel": 0,
              "reference": 0.00028031491092406213,
              "candidate": 0.0,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.4179059938940124,
            "cvrmse_percent": 26.005906689557268,
            "rms_normalized_rmse_percent": 2.1791032858622508,
            "reference_energy": 3.62801807951476,
            "candidate_energy": 3.576576193705762,
            "relative_energy_error_percent": 1.4179059938940124,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.701432428395492e-07,
              "p90": 3.6886194720864296e-05,
              "p95": 5.657441797666247e-05,
              "p99": 0.00014183646999299526,
              "maximum": 0.0013017039746046066
            },
            "worst": {
              "global_sensor_index": 14,
              "local_sensor_index": 14,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025933003053069115,
              "candidate": 0.024631299078464508,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.627379209767198,
            "cvrmse_percent": 9.73847953536497,
            "rms_normalized_rmse_percent": 2.1708077677428665,
            "reference_energy": 9.651478286740513,
            "candidate_energy": 9.590926918534308,
            "relative_energy_error_percent": 0.627379209767198,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.639886353492329e-07,
              "p90": 3.716396167874336e-05,
              "p95": 5.569917484535835e-05,
              "p99": 0.00014140550047159195,
              "maximum": 0.0013017039746046066
            },
            "worst": {
              "global_sensor_index": 14,
              "local_sensor_index": 14,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025933003053069115,
              "candidate": 0.024631299078464508,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "adjacent_grid",
        "full_identifier": "adjacent_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.2103905710262133,
            "cvrmse_percent": 15.406810690478805,
            "rms_normalized_rmse_percent": 0.9991398078326813,
            "reference_energy": 0.06411396764679012,
            "candidate_energy": 0.06397907790415047,
            "relative_energy_error_percent": 0.2103905710262133,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 1.9536237232387066e-05
            },
            "worst": {
              "global_sensor_index": 48,
              "local_sensor_index": 12,
              "sky_patch_index": 20,
              "rgb_channel": 0,
              "reference": 0.0007786959176883101,
              "candidate": 0.0007591596804559231,
              "position": [
                8.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.9067124635967254,
            "cvrmse_percent": 59.727075127853226,
            "rms_normalized_rmse_percent": 5.007387265145087,
            "reference_energy": 0.16735169774148062,
            "candidate_energy": 0.1658342990400179,
            "relative_energy_error_percent": 0.9067124635967254,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.4999996739438757e-08,
              "p90": 5.019091986468993e-06,
              "p95": 8.295657016788027e-06,
              "p99": 2.0821829821215943e-05,
              "maximum": 0.00017550855409353971
            },
            "worst": {
              "global_sensor_index": 43,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.001422568573616445,
              "candidate": 0.0012470600195229053,
              "position": [
                7.5,
                4.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.7138373811643927,
            "cvrmse_percent": 43.398179921133746,
            "rms_normalized_rmse_percent": 5.032316008050167,
            "reference_energy": 0.23146566538827074,
            "candidate_energy": 0.22981337694416837,
            "relative_energy_error_percent": 0.7138373811643927,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.4999996739438757e-08,
              "p90": 4.993971742806025e-06,
              "p95": 8.234985705257712e-06,
              "p99": 2.1454558009281754e-05,
              "maximum": 0.00017550855409353971
            },
            "worst": {
              "global_sensor_index": 43,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.001422568573616445,
              "candidate": 0.0012470600195229053,
              "position": [
                7.5,
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
      72,
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
        "identifier": "interior_glazing_grid",
        "full_identifier": "interior_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.1512333788854345,
            "cvrmse_percent": 3.1505325255229595,
            "rms_normalized_rmse_percent": 0.6450933617846402,
            "reference_energy": 6.023460207225753,
            "candidate_energy": 6.014350724828546,
            "relative_energy_error_percent": 0.15123337888543453,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.406652831472425e-06,
              "p99": 5.4307631216943264e-05,
              "maximum": 0.00028031491092406213
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 42,
              "rgb_channel": 0,
              "reference": 0.00028031491092406213,
              "candidate": 0.0,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 77.87124289003378,
            "cvrmse_percent": 410.87570314384664,
            "rms_normalized_rmse_percent": 22.180792283400617,
            "reference_energy": 2.010766965808479,
            "candidate_energy": 3.576576193705762,
            "relative_energy_error_percent": 77.87124289003378,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00021093664690852165,
              "p95": 0.0002711847532623321,
              "p99": 0.0005340806674212217,
              "maximum": 0.007466345094144344
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011481245048344135,
              "candidate": 0.01894759014248848,
              "position": [
                0.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 19.375849250627645,
            "cvrmse_percent": 102.7965086173127,
            "rms_normalized_rmse_percent": 22.17314641701665,
            "reference_energy": 8.034227173034232,
            "candidate_energy": 9.590926918534308,
            "relative_energy_error_percent": 19.375849250627645,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00020842051526415162,
              "p95": 0.0002714996538998093,
              "p99": 0.0005260850302875042,
              "maximum": 0.007466345094144344
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011481245048344135,
              "candidate": 0.01894759014248848,
              "position": [
                0.5,
                0.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "adjacent_grid",
        "full_identifier": "adjacent_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.2103905710262133,
            "cvrmse_percent": 15.406810690478805,
            "rms_normalized_rmse_percent": 0.9991398078326813,
            "reference_energy": 0.06411396764679012,
            "candidate_energy": 0.06397907790415047,
            "relative_energy_error_percent": 0.2103905710262133,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 1.9536237232387066e-05
            },
            "worst": {
              "global_sensor_index": 48,
              "local_sensor_index": 12,
              "sky_patch_index": 20,
              "rgb_channel": 0,
              "reference": 0.0007786959176883101,
              "candidate": 0.0007591596804559231,
              "position": [
                8.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 137.4895775682873,
            "cvrmse_percent": 853.1276862718373,
            "rms_normalized_rmse_percent": 39.05285800762883,
            "reference_energy": 0.06982803234484436,
            "candidate_energy": 0.1658342990400179,
            "relative_energy_error_percent": 137.4895775682873,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.1109999832115136e-05,
              "p95": 1.9896500270988322e-05,
              "p99": 6.540230970131233e-05,
              "maximum": 0.0011847440619021654
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.002640965860337019,
              "candidate": 0.0038257099222391844,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 71.5767846967506,
            "cvrmse_percent": 444.72387136105374,
            "rms_normalized_rmse_percent": 39.049565223442954,
            "reference_energy": 0.13394199999163448,
            "candidate_energy": 0.22981337694416837,
            "relative_energy_error_percent": 71.57678469675058,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.1109999832115136e-05,
              "p95": 1.9896500270988322e-05,
              "p99": 6.679999933112413e-05,
              "maximum": 0.0011847440619021654
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.002640965860337019,
              "candidate": 0.0038257099222391844,
              "position": [
                6.5,
                3.5,
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
      "bias_percent": -0.08455437883800783,
      "rms_normalized_error_percent": 0.25005828829291527,
      "absolute_error": {
        "p95": 0.08802635574199735,
        "p99": 0.14402042375932791,
        "maximum": 0.1571466364763623
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.046234017352733,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.25005828829291527
    },
    "overcast": {
      "bias_percent": -0.09771064078443206,
      "rms_normalized_error_percent": 0.2107933769590195,
      "absolute_error": {
        "p95": 0.047710728645324746,
        "p99": 0.08508809089660653,
        "maximum": 0.09499216079711914
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.8558969497680664,
      "reference_fraction_of_uniform": 0.6377353072166443,
      "rms_normalized_to_uniform_percent": 0.14886387173867296
    },
    "horizon": {
      "bias_percent": 0.21513328732701892,
      "rms_normalized_error_percent": 2.1365069026693133,
      "absolute_error": {
        "p95": 0.03471899306194056,
        "p99": 0.06086008275297916,
        "maximum": 0.06564416508407045
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.5706100325021912,
      "reference_fraction_of_uniform": 0.09437445372847571,
      "rms_normalized_to_uniform_percent": 0.1151053027511446
    },
    "north": {
      "bias_percent": -56.878265011792806,
      "rms_normalized_error_percent": 103.15428326722882,
      "absolute_error": {
        "p95": 4.731240132969106e-05,
        "p99": 0.00015560870320769054,
        "maximum": 0.0001862421922851354
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.2120178325858433e-05,
      "reference_fraction_of_uniform": 2.004582938752719e-06,
      "rms_normalized_to_uniform_percent": 0.00022897951686778507
    },
    "east": {
      "bias_percent": -0.08109142050636965,
      "rms_normalized_error_percent": 0.3317741021333376,
      "absolute_error": {
        "p95": 0.022869783639907843,
        "p99": 0.03271572351455693,
        "maximum": 0.03749966621398926
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.2265836000442505,
      "reference_fraction_of_uniform": 0.20286737382411957,
      "rms_normalized_to_uniform_percent": 0.07113857709982745
    },
    "south": {
      "bias_percent": -0.012616662930801908,
      "rms_normalized_error_percent": 0.2869104932590898,
      "absolute_error": {
        "p95": 0.07703436613082891,
        "p99": 0.1008687067031861,
        "maximum": 0.10700297355651855
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.174383163452148,
      "reference_fraction_of_uniform": 0.6904104351997375,
      "rms_normalized_to_uniform_percent": 0.18684642815560445
    },
    "west": {
      "bias_percent": -0.5192717504496438,
      "rms_normalized_error_percent": 0.5870040038411347,
      "absolute_error": {
        "p95": 0.0337345838546753,
        "p99": 0.07847154736518867,
        "maximum": 0.0862874984741211
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.2044312953948975,
      "reference_fraction_of_uniform": 0.19920355081558228,
      "rms_normalized_to_uniform_percent": 0.119452476394608
    }
  },
  "annual": {
    "schema_version": 1,
    "oracle": "converged-coefficients",
    "passed": false,
    "occupied_hours": 3650,
    "structural": {
      "sun_up_hours_match": true,
      "grid_ids_match": true,
      "grid_counts_match": true
    },
    "grids": [
      {
        "identifier": "interior_glazing_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.1611099515677004,
          "cvrmse_percent": 1.728752654559481,
          "absolute_error_percentiles_lux": {
            "p50": 2.633258819580078,
            "p90": 25.152191162109382,
            "p95": 37.199139404296865,
            "p99": 69.915294189453
          },
          "maximum_absolute_error_lux": 366.24072265625,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 5108.640625,
            "radiance_lux": 5474.88134765625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.5397602739726016,
            "maximum_error_percentage_points": 1.9412328767123341,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.21440022252299665,
            "maximum_error_percentage_points": 0.8166089241473458,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.1383409436834095,
            "maximum_error_percentage_points": 0.5472602739726007,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.1451217656012174,
            "maximum_error_percentage_points": 0.4889041095890434,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.032496194824961945,
            "maximum_error_percentage_points": 0.13369863013698635,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 55.55555555555556,
          "radiance_percent": 52.77777777777778,
          "difference_percentage_points": 2.7777777777777786,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 1,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "adjacent_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.8953560053477247,
          "cvrmse_percent": 15.199782192627545,
          "absolute_error_percentiles_lux": {
            "p50": 0.34748244285583496,
            "p90": 3.413000488281254,
            "p95": 5.1578882694244355,
            "p99": 9.813115386962888
          },
          "maximum_absolute_error_lux": 39.51293182373047,
          "worst": {
            "sensor_index": 3,
            "position": [
              6.5,
              2.5,
              0.75
            ],
            "hour_of_year": 2722.5,
            "foton_lux": 147.13394165039062,
            "radiance_lux": 107.62100982666016
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.007671232876712326,
            "maximum_error_percentage_points": 0.05808219178082197,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1291059856995162,
            "maximum_error_percentage_points": 0.3833544738828927,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.08154109589041052,
            "maximum_error_percentage_points": 1.1550684931506936,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.08154109589041102,
            "maximum_error_percentage_points": 1.1550684931506865,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0,
            "maximum_error_percentage_points": 0.0,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 0.0,
          "radiance_percent": 0.0,
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
    "numerical_correctness": "incomplete",
    "honeybee_compatibility": "passed",
    "performance": "measured"
  },
  "compatibility": {
    "official_loader": {
      "passed": true,
      "tolerance_percentage_points": 0.05,
      "maximum_error_percentage_points": 0.004931506849315426,
      "metrics": {
        "da": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.004109589041095929,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004813784246579189,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.004751520026220035,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.00438356164384146,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004794520547942938,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.004383561643834355,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.0,
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
      "study_preparation_seconds": 0.35982609600000615,
      "weather_seconds": 0.21744159200011381,
      "metric_reduction_seconds": 0.26244224799984295,
      "write_seconds": 0.014506667999967249,
      "total_seconds": 0.49477193999996416,
      "cold_end_to_end_seconds": 0.8545980359999703,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.002546095000070636,
      "engine_upload_seconds": 0.013710161,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.020532216,
      "engine_annual_reduction_seconds": 0.008994274,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.020532216
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.35982609600000615,
      "weather_seconds": 0.2370912869998847,
      "metric_reduction_seconds": 0.45241428899998937,
      "write_seconds": 0.02237234700010049,
      "total_seconds": 0.7122734020001644,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.7122734020001644,
      "raw_export_seconds": 0.003519006000033187,
      "engine_upload_seconds": 0.014026296,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.4e-08,
      "engine_annual_reduction_seconds": 0.00914988,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.014368471999887333,
      "full": 0.02938989099993705
    }
  },
  "elapsed_seconds": 4.381454327999791,
  "result_class": "unstable_reference"
}
```
