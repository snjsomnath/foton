# Foton report

Status: **failed**

```json
{
  "scene": "atrium_borrowed_light",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "atrium_borrowed_light",
    "category": "connections",
    "question": "Can a rooflit atrium feed rooms at two levels through internal glass?",
    "interactions": [
      "roof_glazing",
      "borrowed_light",
      "split_adjacency",
      "stacked_zones"
    ],
    "room_count": 3,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 3,
    "apertures": 5,
    "shades": 0,
    "sensors": 108,
    "floor_area": 108.0,
    "aperture_area": 35.2
  },
  "sky_density": 2,
  "status": "failed",
  "passed": false,
  "model_sha256": "4dbea10fc2d26d15fe18ffbc5e7cee5fe74ee211ebf3cc5cfb55ef2c28d22e20",
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 13086254370129758359,
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 13086254370129758359,
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
    "maximum_samples": 16384,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "atrium_borrowed_light_atrium_grid",
        "bias_percent": -0.07672382825287284,
        "rms_normalized_error_percent": 1.0908881235476013,
        "absolute_error": {
          "p95": 6.735310307703912e-06,
          "p99": 8.77203419804573e-05,
          "maximum": 0.00024381768889725208
        },
        "worst_index": [
          33,
          528,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "bias_percent": 0.2312468068990563,
        "rms_normalized_error_percent": 1.278655093290519,
        "absolute_error": {
          "p95": 0.0,
          "p99": 3.562308847904205e-08,
          "maximum": 7.613853085786104e-05
        },
        "worst_index": [
          4,
          502,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "bias_percent": 0.23460445669819746,
        "rms_normalized_error_percent": 1.3484971770294452,
        "absolute_error": {
          "p95": 0.0,
          "p99": 9.63243655860424e-06,
          "maximum": 8.24473099783063e-05
        },
        "worst_index": [
          4,
          333,
          0
        ],
        "passed": true
      }
    ],
    "samples_per_patch": [
      256,
      1024
    ]
  },
  "depth_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "atrium_borrowed_light_atrium_grid",
        "bias_percent": 0.016556900529608166,
        "rms_normalized_error_percent": 1.8992875896781656,
        "absolute_error": {
          "p95": 5.771336145699024e-05,
          "p99": 0.00013027340173721313,
          "maximum": 0.00028239982202649117
        },
        "worst_index": [
          27,
          577,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "bias_percent": 0.02492744154294337,
        "rms_normalized_error_percent": 3.212010769453354,
        "absolute_error": {
          "p95": 1.0904395594479865e-05,
          "p99": 2.2407511323763174e-05,
          "maximum": 9.232270531356335e-05
        },
        "worst_index": [
          3,
          422,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "bias_percent": 0.11848168399562858,
        "rms_normalized_error_percent": 3.281788060881443,
        "absolute_error": {
          "p95": 8.868214990798151e-06,
          "p99": 3.8046506233513355e-05,
          "maximum": 0.00012138625606894493
        },
        "worst_index": [
          2,
          374,
          0
        ],
        "passed": true
      }
    ]
  },
  "sample_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "atrium_borrowed_light_atrium_grid",
        "bias_percent": 0.02419687687564188,
        "rms_normalized_error_percent": 1.614931638500342,
        "absolute_error": {
          "p95": 4.84651536680758e-05,
          "p99": 0.00011210888624191284,
          "maximum": 0.00030094804242253304
        },
        "worst_index": [
          26,
          562,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "bias_percent": 0.15865905688977766,
        "rms_normalized_error_percent": 2.7723949731533493,
        "absolute_error": {
          "p95": 9.577557648299262e-06,
          "p99": 1.8934295439976268e-05,
          "maximum": 8.731894195079803e-05
        },
        "worst_index": [
          3,
          420,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "bias_percent": 0.03359332814784545,
        "rms_normalized_error_percent": 2.6154346410119826,
        "absolute_error": {
          "p95": 7.614675268996507e-06,
          "p99": 2.9411516152322292e-05,
          "maximum": 0.00011196639388799667
        },
        "worst_index": [
          3,
          278,
          0
        ],
        "passed": true
      }
    ]
  },
  "oracle_levels": [
    {
      "samples": 20000,
      "material_bounces": 1,
      "repeatability": {
        "schema_version": 1,
        "run_count": 8,
        "half_run_count": 4,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.007447101321518384,
                "cvrmse_percent": 10.649270850693332,
                "rms_normalized_rmse_percent": 2.9497058465406902,
                "reference_energy": 24.002909807962624,
                "candidate_energy": 24.001122286949112,
                "relative_energy_error_percent": 0.007447101321518384,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.597178167387124e-06,
                  "p95": 8.958429680205882e-05,
                  "p99": 0.00020995503291487694,
                  "maximum": 0.0004714902024716139
                },
                "worst": {
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "sky_patch_index": 559,
                  "rgb_channel": 0,
                  "reference": 0.007172059966251254,
                  "candidate": 0.00670056976377964
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.036127782834659616,
                "cvrmse_percent": 74.98440532085172,
                "rms_normalized_rmse_percent": 4.372885948589472,
                "reference_energy": 5.321637298900667,
                "candidate_energy": 5.319714709334072,
                "relative_energy_error_percent": 0.036127782834659616,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 8.208475264837034e-06,
                  "p90": 4.99406401104352e-05,
                  "p95": 0.00012150581460446119,
                  "p99": 0.00032610981725156307,
                  "maximum": 0.000784141244366765
                },
                "worst": {
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "sky_patch_index": 548,
                  "rgb_channel": 0,
                  "reference": -0.0001264079473912716,
                  "candidate": 0.0006577332969754934
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.1439216320175102,
                "cvrmse_percent": 39.08215882085284,
                "rms_normalized_rmse_percent": 3.415848088587429,
                "reference_energy": 0.9584020837287426,
                "candidate_energy": 0.9597814316489348,
                "relative_energy_error_percent": 0.1439216320175102,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.360358722507954e-07,
                  "maximum": 0.00017012422904372215
                },
                "worst": {
                  "global_sensor_index": 45,
                  "local_sensor_index": 9,
                  "sky_patch_index": 372,
                  "rgb_channel": 0,
                  "reference": 0.0015599245380144566,
                  "candidate": 0.0017300487670581788
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -1.674545387998833,
                "cvrmse_percent": 333.01183963266317,
                "rms_normalized_rmse_percent": 5.752029850414197,
                "reference_energy": 0.19010327327958443,
                "candidate_energy": 0.18691990768444633,
                "relative_energy_error_percent": 1.674545387998833,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 7.922964323370269e-06,
                  "p95": 1.3599945305031724e-05,
                  "p99": 3.33512343786424e-05,
                  "maximum": 0.00028313524671830237
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "sky_patch_index": 369,
                  "rgb_channel": 0,
                  "reference": -0.0001888437254820019,
                  "candidate": 9.429152123630047e-05
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "start_sensor_index": 72,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.1247564043974394,
                "cvrmse_percent": 29.970632395449154,
                "rms_normalized_rmse_percent": 4.3906596415481305,
                "reference_energy": 2.006020323136454,
                "candidate_energy": 2.003517684309827,
                "relative_energy_error_percent": 0.1247564043974394,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.117811087984592e-05,
                  "maximum": 0.00020084003335796297
                },
                "worst": {
                  "global_sensor_index": 81,
                  "local_sensor_index": 9,
                  "sky_patch_index": 327,
                  "rgb_channel": 0,
                  "reference": 0.0020966915180906653,
                  "candidate": 0.0018958514847327024
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 3.904356928059588,
                "cvrmse_percent": 1068.3697724989036,
                "rms_normalized_rmse_percent": 6.5229987443116135,
                "reference_energy": 0.08366204355211337,
                "candidate_energy": 0.08692850834569654,
                "relative_energy_error_percent": 3.904356928059588,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.9208311654401865e-06,
                  "p95": 1.0308199279052133e-05,
                  "p99": 7.514849312428851e-05,
                  "maximum": 0.0002731666900217533
                },
                "worst": {
                  "global_sensor_index": 74,
                  "local_sensor_index": 2,
                  "sky_patch_index": 370,
                  "rgb_channel": 0,
                  "reference": -0.00016506772954016924,
                  "candidate": 0.00010809896048158407
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 263.7771249283105,
            "full": 721.5355000225827
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 256.8706659367308,
            "full": 773.404625011608
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 337.9758750088513,
            "full": 805.6040829978883
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 256.53420807793736,
            "full": 807.2070829803124
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 271.41129202209413,
            "full": 754.0337080135942
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 220.39895795751363,
            "full": 751.6862920019776
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 245.86645897943527,
            "full": 814.4059589831159
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 242.90708301123232,
            "full": 724.8309589922428
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 8,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.01577231546567601,
                "cvrmse_percent": 8.979630789220005,
                "rms_normalized_rmse_percent": 2.4874298629299454,
                "reference_energy": 23.99486073489095,
                "candidate_energy": 23.998645280021606,
                "relative_energy_error_percent": 0.015772315465676007,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.678529512603175e-06,
                  "p95": 7.016141898930073e-05,
                  "p99": 0.0001709607895463705,
                  "maximum": 0.00040045357309281826
                },
                "worst": {
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "sky_patch_index": 577,
                  "rgb_channel": 0,
                  "reference": 0.00565408356487751,
                  "candidate": 0.005253629991784692
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.10630643600868182,
                "cvrmse_percent": 33.12971841231258,
                "rms_normalized_rmse_percent": 3.4833968503311694,
                "reference_energy": 9.9892172143926,
                "candidate_energy": 9.999836395198386,
                "relative_energy_error_percent": 0.10630643600868184,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.0525025572860613e-05,
                  "p90": 5.258291130303413e-05,
                  "p95": 0.00010298890992999077,
                  "p99": 0.0002552636433392763,
                  "maximum": 0.0006336127407848835
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 577,
                  "rgb_channel": 0,
                  "reference": -6.166612729430199e-05,
                  "candidate": 0.0005719466134905815
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0039048783655888574,
                "cvrmse_percent": 31.983997780913306,
                "rms_normalized_rmse_percent": 2.7976248673687367,
                "reference_energy": 0.9586197955859461,
                "candidate_energy": 0.9586572285229522,
                "relative_energy_error_percent": 0.0039048783655888574,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.4139957278966904e-06,
                  "maximum": 0.00015683250967413187
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "sky_patch_index": 419,
                  "rgb_channel": 0,
                  "reference": 0.002218374516814947,
                  "candidate": 0.0020615420071408153
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.6382776073768397,
                "cvrmse_percent": 91.59165309193902,
                "rms_normalized_rmse_percent": 5.278469828084292,
                "reference_energy": 0.6504495711125458,
                "candidate_energy": 0.6462978971528557,
                "relative_energy_error_percent": 0.6382776073768396,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.6357400145494694e-06,
                  "p90": 1.1059347161790394e-05,
                  "p95": 1.6293304270220688e-05,
                  "p99": 3.409567989365314e-05,
                  "maximum": 0.0001689514610916376
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "sky_patch_index": 419,
                  "rgb_channel": 0,
                  "reference": 1.8667546100914478e-05,
                  "candidate": 0.0001876190071925521
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "start_sensor_index": 72,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.10529066376473327,
                "cvrmse_percent": 32.51536783697834,
                "rms_normalized_rmse_percent": 4.764053521368835,
                "reference_energy": 2.0031186906126095,
                "candidate_energy": 2.005227787577951,
                "relative_energy_error_percent": 0.10529066376473327,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.444791167974472e-05,
                  "maximum": 0.0002086050226353109
                },
                "worst": {
                  "global_sensor_index": 75,
                  "local_sensor_index": 3,
                  "sky_patch_index": 377,
                  "rgb_channel": 0,
                  "reference": 0.0021704374812543392,
                  "candidate": 0.0019618324586190283
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.5957743585519987,
                "cvrmse_percent": 134.93752490612073,
                "rms_normalized_rmse_percent": 6.3037198329533135,
                "reference_energy": 0.6601613851467363,
                "candidate_energy": 0.6562283128889703,
                "relative_energy_error_percent": 0.5957743585519987,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.7960893625712515e-06,
                  "p90": 8.293747146126412e-06,
                  "p95": 1.2831891581299715e-05,
                  "p99": 6.85351260472089e-05,
                  "maximum": 0.00030283897649496794
                },
                "worst": {
                  "global_sensor_index": 75,
                  "local_sensor_index": 3,
                  "sky_patch_index": 328,
                  "rgb_channel": 0,
                  "reference": 0.00020028301514685154,
                  "candidate": -0.0001025559613481164
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 386.8225420592353,
            "full": 9341.444249963388
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 348.38437498547137,
            "full": 8768.767875037156
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 317.92429194319993,
            "full": 8731.010625022464
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 322.9001249419525,
            "full": 8647.693375009112
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 12,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.01668072422801226,
                "cvrmse_percent": 8.77549752490554,
                "rms_normalized_rmse_percent": 2.4298451408341535,
                "reference_energy": 23.99998542583387,
                "candidate_energy": 24.003988797217517,
                "relative_energy_error_percent": 0.01668072422801226,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.037500409343984e-06,
                  "p95": 6.986538937781006e-05,
                  "p99": 0.00016487948596477509,
                  "maximum": 0.0003426771145313978
                },
                "worst": {
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "sky_patch_index": 491,
                  "rgb_channel": 0,
                  "reference": 0.004708735505118966,
                  "candidate": 0.005051412619650364
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.05281624189735963,
                "cvrmse_percent": 33.158416448143285,
                "rms_normalized_rmse_percent": 3.4867980752583008,
                "reference_energy": 9.992281843694908,
                "candidate_energy": 9.99755939144454,
                "relative_energy_error_percent": 0.05281624189735964,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.060753311321605e-05,
                  "p90": 5.3693164227297535e-05,
                  "p95": 0.0001028948463499546,
                  "p99": 0.0002549515338614583,
                  "maximum": 0.0006664029788225889
                },
                "worst": {
                  "global_sensor_index": 24,
                  "local_sensor_index": 24,
                  "sky_patch_index": 491,
                  "rgb_channel": 0,
                  "reference": 0.0010911249555647373,
                  "candidate": 0.0004247219767421484
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.1074908813395574,
                "cvrmse_percent": 30.313321030324076,
                "rms_normalized_rmse_percent": 2.6467531460422364,
                "reference_energy": 0.9592414639787421,
                "candidate_energy": 0.9602725610825473,
                "relative_energy_error_percent": 0.1074908813395574,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.34000127017498e-07,
                  "maximum": 0.0001335709821432829
                },
                "worst": {
                  "global_sensor_index": 45,
                  "local_sensor_index": 9,
                  "sky_patch_index": 422,
                  "rgb_channel": 0,
                  "reference": 0.0014710164978168905,
                  "candidate": 0.0013374455156736076
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.7220807846449652,
                "cvrmse_percent": 92.64380979070194,
                "rms_normalized_rmse_percent": 5.33618732733699,
                "reference_energy": 0.6500025860795589,
                "candidate_energy": 0.645309042305783,
                "relative_energy_error_percent": 0.7220807846449652,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.6234494921718579e-06,
                  "p90": 1.0761167231976321e-05,
                  "p95": 1.5864149645494763e-05,
                  "p99": 3.142732657579472e-05,
                  "maximum": 0.00023215985856950283
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "sky_patch_index": 521,
                  "rgb_channel": 0,
                  "reference": -0.00014786038082093,
                  "candidate": 8.429947774857283e-05
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "start_sensor_index": 72,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.009929551176661802,
                "cvrmse_percent": 26.983479143771543,
                "rms_normalized_rmse_percent": 3.951423630680185,
                "reference_energy": 2.004568319505779,
                "candidate_energy": 2.0043692748686226,
                "relative_energy_error_percent": 0.009929551176661802,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.577601794153452e-05,
                  "maximum": 0.00017376954201608896
                },
                "worst": {
                  "global_sensor_index": 74,
                  "local_sensor_index": 2,
                  "sky_patch_index": 319,
                  "rgb_channel": 0,
                  "reference": 0.0013742754817940295,
                  "candidate": 0.0015480450238101184
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.7064832872393185,
                "cvrmse_percent": 125.78639651989307,
                "rms_normalized_rmse_percent": 5.906753811728209,
                "reference_energy": 0.6633971050797527,
                "candidate_energy": 0.6587103154043348,
                "relative_energy_error_percent": 0.7064832872393185,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.781395710054312e-06,
                  "p90": 8.288925755550737e-06,
                  "p95": 1.2886478089058073e-05,
                  "p99": 6.846770702395588e-05,
                  "maximum": 0.000244687485974282
                },
                "worst": {
                  "global_sensor_index": 73,
                  "local_sensor_index": 1,
                  "sky_patch_index": 272,
                  "rgb_channel": 0,
                  "reference": 0.00011764501687139273,
                  "candidate": -0.0001270424691028893
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 316.36320799589157,
            "full": 9083.22962501552
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 359.9818330258131,
            "full": 9150.997792021371
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 321.06170791666955,
            "full": 9297.965249978006
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 319.38620808068663,
            "full": 9080.240625073202
          }
        }
      ]
    },
    {
      "samples": 80000,
      "material_bounces": 12,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.04732181289931941,
                "cvrmse_percent": 5.431743102984399,
                "rms_normalized_rmse_percent": 1.5042721267707035,
                "reference_energy": 23.995891138011643,
                "candidate_energy": 24.007246428719498,
                "relative_energy_error_percent": 0.047321812899319415,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.5648990888148546e-06,
                  "p95": 4.5168912038207054e-05,
                  "p99": 0.00011420994997024536,
                  "maximum": 0.000211448990739882
                },
                "worst": {
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "sky_patch_index": 569,
                  "rgb_channel": 0,
                  "reference": 0.0035139269893988967,
                  "candidate": 0.0037253759801387787
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.031896301242602086,
                "cvrmse_percent": 20.75851880119187,
                "rms_normalized_rmse_percent": 2.1862489100610745,
                "reference_energy": 10.001969976157941,
                "candidate_energy": 10.005160234631731,
                "relative_energy_error_percent": 0.031896301242602086,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.5966429449181305e-06,
                  "p90": 3.7008846993558185e-05,
                  "p95": 6.77232164889574e-05,
                  "p99": 0.00015207519754767418,
                  "maximum": 0.0003599936608225107
                },
                "worst": {
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "sky_patch_index": 555,
                  "rgb_channel": 0,
                  "reference": 0.0002707268577069044,
                  "candidate": 0.0006307205185294151
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.04090954576352397,
                "cvrmse_percent": 19.708356938683337,
                "rms_normalized_rmse_percent": 1.723796386586955,
                "reference_energy": 0.9597081002286814,
                "candidate_energy": 0.9593154880042221,
                "relative_energy_error_percent": 0.04090954576352397,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.492525476962328e-06,
                  "maximum": 7.698638364672661e-05
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "sky_patch_index": 524,
                  "rgb_channel": 0,
                  "reference": 0.00292193447239697,
                  "candidate": 0.002844948088750243
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.7299836572315352,
                "cvrmse_percent": 63.08207529425212,
                "rms_normalized_rmse_percent": 3.6272446626116857,
                "reference_energy": 0.648085878133557,
                "candidate_energy": 0.6528167991287575,
                "relative_energy_error_percent": 0.7299836572315351,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.2539519218535133e-06,
                  "p90": 7.838378951419152e-06,
                  "p95": 1.1360739790688967e-05,
                  "p99": 2.442380991851678e-05,
                  "maximum": 0.00014101597480475903
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "sky_patch_index": 524,
                  "rgb_channel": 0,
                  "reference": -3.802007995545864e-06,
                  "candidate": 0.00013721396680921316
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "start_sensor_index": 72,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.0823643642488479,
                "cvrmse_percent": 14.763764752915796,
                "rms_normalized_rmse_percent": 2.1641990953835513,
                "reference_energy": 2.00498983284956,
                "candidate_energy": 2.0033384357204795,
                "relative_energy_error_percent": 0.08236436424884791,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.541212597861886e-05,
                  "maximum": 9.944598423317075e-05
                },
                "worst": {
                  "global_sensor_index": 78,
                  "local_sensor_index": 6,
                  "sky_patch_index": 320,
                  "rgb_channel": 0,
                  "reference": 0.0013201715191826224,
                  "candidate": 0.0012207255349494517
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.10239923735352317,
                "cvrmse_percent": 69.66322387183827,
                "rms_normalized_rmse_percent": 3.2638362672261048,
                "reference_energy": 0.6619149119979575,
                "candidate_energy": 0.6625927078197726,
                "relative_energy_error_percent": 0.10239923735352317,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.3376572809420395e-06,
                  "p90": 5.9312523035259835e-06,
                  "p95": 8.889836294656561e-06,
                  "p99": 3.7585967220366e-05,
                  "maximum": 0.00011848984286189079
                },
                "worst": {
                  "global_sensor_index": 82,
                  "local_sensor_index": 10,
                  "sky_patch_index": 327,
                  "rgb_channel": 0,
                  "reference": 0.00012736988719552755,
                  "candidate": 8.88004433363676e-06
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 566.7627090588212,
            "full": 15605.102334055118
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 562.1967499610037,
            "full": 15717.591250082478
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 561.054875026457,
            "full": 16038.004708010703
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "108",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 572.8958749677986,
            "full": 16128.126042080112
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 19620.338334003463,
      "worker_pool_size": 12,
      "invocation_count": 7
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/atrium_borrowed_light/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 85444.02816705406,
      "worker_pool_size": 12,
      "invocation_count": 7
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      108,
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
        "identifier": "atrium_borrowed_light_atrium_grid",
        "full_identifier": "atrium_borrowed_light_atrium_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -1.5432083209500536,
            "cvrmse_percent": 14.465039831597002,
            "rms_normalized_rmse_percent": 4.045788025541006,
            "reference_energy": 24.001344877539083,
            "candidate_energy": 23.63095412624898,
            "relative_energy_error_percent": 1.5432083209500536,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.725290298461914e-09,
              "p95": 1.8398870452074334e-05,
              "p99": 0.00020123893045820296,
              "maximum": 0.0012144509237259626
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 509,
              "rgb_channel": 0,
              "reference": 0.0012144509237259626,
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
            "nmbe_percent": -0.5124672628908296,
            "cvrmse_percent": 65.8565430140364,
            "rms_normalized_rmse_percent": 6.935991783603972,
            "reference_energy": 10.00378902476798,
            "candidate_energy": 9.95252288096738,
            "relative_energy_error_percent": 0.5124672628908296,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.626246689236723e-05,
              "p90": 0.0001288109458982945,
              "p95": 0.00017366498650517315,
              "p99": 0.00040635198820382357,
              "maximum": 0.0014273687120294198
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 509,
              "rgb_channel": 0,
              "reference": -0.001035448702168651,
              "candidate": 0.0003919200098607689,
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
            "nmbe_percent": -1.2399801050690675,
            "cvrmse_percent": 16.576544899424057,
            "rms_normalized_rmse_percent": 5.934492971640512,
            "reference_energy": 34.005133902307065,
            "candidate_energy": 33.58347700721636,
            "relative_energy_error_percent": 1.2399801050690729,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.5594428481999785e-05,
              "p90": 0.00012230146821821142,
              "p95": 0.00016010343097150326,
              "p99": 0.0002923072315752506,
              "maximum": 0.001420903019607067
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 520,
              "rgb_channel": 0,
              "reference": 0.008126022294163704,
              "candidate": 0.006705119274556637,
              "position": [
                5.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "full_identifier": "atrium_borrowed_light_office_0_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.022337097386452263,
            "cvrmse_percent": 8.364116384548517,
            "rms_normalized_rmse_percent": 0.7313977807624535,
            "reference_energy": 0.9588268793086172,
            "candidate_energy": 0.9590410534024159,
            "relative_energy_error_percent": 0.022337097386452263,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 4.307366907596588e-08,
              "maximum": 5.270994734019041e-05
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 491,
              "rgb_channel": 0,
              "reference": 0.0012057150015607476,
              "candidate": 0.001258424948900938,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.5758598266085038,
            "cvrmse_percent": 132.22459925611338,
            "rms_normalized_rmse_percent": 7.639546891678363,
            "reference_energy": 0.6511362589264582,
            "candidate_energy": 0.6408752642055546,
            "relative_energy_error_percent": 1.5758598266085038,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.7518366298172623e-06,
              "p90": 2.241574875370137e-05,
              "p95": 3.143496360280551e-05,
              "p99": 5.180501284485217e-05,
              "maximum": 0.00013452261555357836
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 3,
              "sky_patch_index": 485,
              "rgb_channel": 0,
              "reference": 3.746738730114885e-05,
              "candidate": 0.0001719900028547272,
              "position": [
                6.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.6240404136282759,
            "cvrmse_percent": 53.341981469848115,
            "rms_normalized_rmse_percent": 7.620238044523893,
            "reference_energy": 1.6099631382350754,
            "candidate_energy": 1.5999163176079705,
            "relative_energy_error_percent": 0.6240404136282759,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.752135285139957e-06,
              "p90": 2.2426212308346344e-05,
              "p95": 3.133598056592746e-05,
              "p99": 5.154638165549841e-05,
              "maximum": 0.00013452261555357836
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 3,
              "sky_patch_index": 485,
              "rgb_channel": 0,
              "reference": 3.746738730114885e-05,
              "candidate": 0.0001719900028547272,
              "position": [
                6.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "full_identifier": "atrium_borrowed_light_office_1_grid",
        "start_sensor_index": 72,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.03702766820649462,
            "cvrmse_percent": 4.693532072983746,
            "rms_normalized_rmse_percent": 0.6882520789598133,
            "reference_energy": 2.004155770185548,
            "candidate_energy": 2.0034136780366225,
            "relative_energy_error_percent": 0.03702766820649462,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 5.412206519395113e-06,
              "maximum": 4.994310438632965e-05
            },
            "worst": {
              "global_sensor_index": 74,
              "local_sensor_index": 2,
              "sky_patch_index": 378,
              "rgb_channel": 0,
              "reference": 0.0003819783159997314,
              "candidate": 0.00043192142038606107,
              "position": [
                6.5,
                3.5,
                3.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.02499588439942763,
            "cvrmse_percent": 122.24928896646219,
            "rms_normalized_rmse_percent": 5.734030633765198,
            "reference_energy": 0.662262173982139,
            "candidate_energy": 0.6620966356947093,
            "relative_energy_error_percent": 0.024995884399427633,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.932959654979641e-06,
              "p90": 1.9429312305874202e-05,
              "p95": 2.8581474907696247e-05,
              "p99": 4.862874084210489e-05,
              "maximum": 0.00011697272202582099
            },
            "worst": {
              "global_sensor_index": 91,
              "local_sensor_index": 19,
              "sky_patch_index": 277,
              "rgb_channel": 0,
              "reference": 6.505728015326895e-05,
              "candidate": 0.00018203000217908993,
              "position": [
                9.5,
                4.5,
                3.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.03403931624224975,
            "cvrmse_percent": 30.30147346969769,
            "rms_normalized_rmse_percent": 5.722366733839163,
            "reference_energy": 2.666417944167687,
            "candidate_energy": 2.665510313731332,
            "relative_energy_error_percent": 0.03403931624224975,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.928447651764145e-06,
              "p90": 1.9414646476434455e-05,
              "p95": 2.841587229340803e-05,
              "p99": 4.8572663217782974e-05,
              "maximum": 0.00012115002755308524
            },
            "worst": {
              "global_sensor_index": 91,
              "local_sensor_index": 19,
              "sky_patch_index": 277,
              "rgb_channel": 0,
              "reference": 0.00011166945478180423,
              "candidate": 0.00023281948233488947,
              "position": [
                9.5,
                4.5,
                3.75
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
      108,
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
        "identifier": "atrium_borrowed_light_atrium_grid",
        "full_identifier": "atrium_borrowed_light_atrium_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -1.5432083209500536,
            "cvrmse_percent": 14.465039831597002,
            "rms_normalized_rmse_percent": 4.045788025541006,
            "reference_energy": 24.001344877539083,
            "candidate_energy": 23.63095412624898,
            "relative_energy_error_percent": 1.5432083209500536,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.725290298461914e-09,
              "p95": 1.8398870452074334e-05,
              "p99": 0.00020123893045820296,
              "maximum": 0.0012144509237259626
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 509,
              "rgb_channel": 0,
              "reference": 0.0012144509237259626,
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
            "nmbe_percent": 87.03013561732932,
            "cvrmse_percent": 166.82230387959189,
            "rms_normalized_rmse_percent": 9.73044893390348,
            "reference_energy": 5.321347197935318,
            "candidate_energy": 9.95252288096738,
            "relative_energy_error_percent": 87.03013561732932,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.6494878663215786e-05,
              "p90": 0.00021623311149596706,
              "p95": 0.00027787359431385994,
              "p99": 0.000493566898512654,
              "maximum": 0.0015779943369125249
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 509,
              "rgb_channel": 0,
              "reference": -0.001186074327051756,
              "candidate": 0.0003919200098607689,
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
            "nmbe_percent": 14.530674471412853,
            "cvrmse_percent": 26.93540042101695,
            "rms_normalized_rmse_percent": 8.65733938550801,
            "reference_energy": 29.3226920754744,
            "candidate_energy": 33.58347700721636,
            "relative_energy_error_percent": 14.530674471412857,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.556212954616058e-05,
              "p90": 0.0002039965729636606,
              "p95": 0.0002585050169727765,
              "p99": 0.00040392215669271536,
              "maximum": 0.0011014617048203945
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 520,
              "rgb_channel": 0,
              "reference": 0.007686471100896597,
              "candidate": 0.006585009396076202,
              "position": [
                5.5,
                3.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "full_identifier": "atrium_borrowed_light_office_0_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.022337097386452263,
            "cvrmse_percent": 8.364116384548517,
            "rms_normalized_rmse_percent": 0.7313977807624535,
            "reference_energy": 0.9588268793086172,
            "candidate_energy": 0.9590410534024159,
            "relative_energy_error_percent": 0.022337097386452263,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 4.307366907596588e-08,
              "maximum": 5.270994734019041e-05
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 491,
              "rgb_channel": 0,
              "reference": 0.0012057150015607476,
              "candidate": 0.001258424948900938,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 239.4889477568136,
            "cvrmse_percent": 615.5869364253127,
            "rms_normalized_rmse_percent": 10.571952440736878,
            "reference_energy": 0.18877647370854422,
            "candidate_energy": 0.6408752642055546,
            "relative_energy_error_percent": 239.48894775681362,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.3299999156733975e-06,
              "p90": 3.032818094652613e-05,
              "p95": 4.2830000893445686e-05,
              "p99": 7.267000182764605e-05,
              "maximum": 0.0001845991937443614
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 456,
              "rgb_channel": 0,
              "reference": -5.7729193940758705e-05,
              "candidate": 0.0001268699998036027,
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
            "nmbe_percent": 39.41370190333045,
            "cvrmse_percent": 101.27947696479718,
            "rms_normalized_rmse_percent": 10.573802512332684,
            "reference_energy": 1.1476033530171614,
            "candidate_energy": 1.5999163176079705,
            "relative_energy_error_percent": 39.413701903330455,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.3299999156733975e-06,
              "p90": 3.0270348634076073e-05,
              "p95": 4.274164439266315e-05,
              "p99": 7.268437184393406e-05,
              "maximum": 0.00017163436859846115
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 3,
              "sky_patch_index": 523,
              "rgb_channel": 0,
              "reference": 0.0028213593177497387,
              "candidate": 0.0029929936863482,
              "position": [
                6.5,
                2.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "full_identifier": "atrium_borrowed_light_office_1_grid",
        "start_sensor_index": 72,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.03702766820649462,
            "cvrmse_percent": 4.693532072983746,
            "rms_normalized_rmse_percent": 0.6882520789598133,
            "reference_energy": 2.004155770185548,
            "candidate_energy": 2.0034136780366225,
            "relative_energy_error_percent": 0.03702766820649462,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 5.412206519395113e-06,
              "maximum": 4.994310438632965e-05
            },
            "worst": {
              "global_sensor_index": 74,
              "local_sensor_index": 2,
              "sky_patch_index": 378,
              "rgb_channel": 0,
              "reference": 0.0003819783159997314,
              "candidate": 0.00043192142038606107,
              "position": [
                6.5,
                3.5,
                3.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 670.6996859121298,
            "cvrmse_percent": 1462.5683714678044,
            "rms_normalized_rmse_percent": 9.170288527679954,
            "reference_energy": 0.0859085124591834,
            "candidate_energy": 0.6620966356947093,
            "relative_energy_error_percent": 670.6996859121297,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.8531482598737057e-06,
              "p90": 3.13218655264791e-05,
              "p95": 4.558882210403681e-05,
              "p99": 8.171000081347302e-05,
              "maximum": 0.00018558032388682477
            },
            "worst": {
              "global_sensor_index": 91,
              "local_sensor_index": 19,
              "sky_patch_index": 277,
              "rgb_channel": 0,
              "reference": -3.550321707734838e-06,
              "candidate": 0.00018203000217908993,
              "position": [
                9.5,
                4.5,
                3.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 27.53245610027079,
            "cvrmse_percent": 59.98196463142589,
            "rms_normalized_rmse_percent": 9.149786358732605,
            "reference_energy": 2.0900642826447315,
            "candidate_energy": 2.665510313731332,
            "relative_energy_error_percent": 27.53245610027079,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.853598971341853e-06,
              "p90": 3.135815011319212e-05,
              "p95": 4.555000123218633e-05,
              "p99": 8.138999692164361e-05,
              "maximum": 0.00018975762941408902
            },
            "worst": {
              "global_sensor_index": 91,
              "local_sensor_index": 19,
              "sky_patch_index": 277,
              "rgb_channel": 0,
              "reference": 4.306185292080045e-05,
              "candidate": 0.00023281948233488947,
              "position": [
                9.5,
                4.5,
                3.75
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
      "bias_percent": -1.1299818794691312,
      "rms_normalized_error_percent": 2.084463697609865,
      "absolute_error": {
        "p95": 0.7049021777902562,
        "p99": 3.60932899931133,
        "maximum": 3.9640089669896597
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 21.149334959749073,
      "rms_normalized_to_uniform_percent": 2.084463697609865
    },
    "overcast": {
      "bias_percent": -1.1095982642086106,
      "rms_normalized_error_percent": 2.073769926805362,
      "absolute_error": {
        "p95": 0.5547048568725585,
        "p99": 3.239439926147456,
        "maximum": 3.6054534912109375
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 18.619279861450195,
      "rms_normalized_to_uniform_percent": 1.8578292052310443
    },
    "horizon": {
      "bias_percent": 3.363367440059005,
      "rms_normalized_error_percent": 24.216322384287775,
      "absolute_error": {
        "p95": 0.034116759434258216,
        "p99": 0.06694543244307458,
        "maximum": 0.06874100627884672
      },
      "worst_index": [
        20
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.04847884904044384,
      "rms_normalized_to_uniform_percent": 0.052658687338032674
    },
    "north": {
      "bias_percent": -0.8271717164072677,
      "rms_normalized_error_percent": 1.730297969461723,
      "absolute_error": {
        "p95": 0.16799359321594232,
        "p99": 0.4178766155242901,
        "maximum": 0.7542524337768555
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.1404080390930176,
      "rms_normalized_to_uniform_percent": 0.3031353265053045
    },
    "east": {
      "bias_percent": -0.08038080580637964,
      "rms_normalized_error_percent": 0.7475160881040643,
      "absolute_error": {
        "p95": 0.12056000232696513,
        "p99": 0.14595164299011223,
        "maximum": 0.18045496940612793
      },
      "worst_index": [
        27
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.0169591903686523,
      "rms_normalized_to_uniform_percent": 0.13351456948234025
    },
    "south": {
      "bias_percent": -1.0476527124721025,
      "rms_normalized_error_percent": 1.96071743929499,
      "absolute_error": {
        "p95": 0.19059081077575657,
        "p99": 0.5576218557357765,
        "maximum": 0.7977218627929688
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.15777587890625,
      "rms_normalized_to_uniform_percent": 0.34496817354897114
    },
    "west": {
      "bias_percent": -2.9007988996096707,
      "rms_normalized_error_percent": 5.066860922025229,
      "absolute_error": {
        "p95": 0.31601386070251447,
        "p99": 1.6769103050231904,
        "maximum": 1.7880630493164062
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 4.027054786682129,
      "rms_normalized_to_uniform_percent": 0.9588235186833749
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
        "identifier": "atrium_borrowed_light_atrium_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -1.5972964348779324,
          "cvrmse_percent": 10.689240000837728,
          "absolute_error_percentiles_lux": {
            "p50": 23.903976440429688,
            "p90": 221.88712158203134,
            "p95": 341.19556274414055,
            "p99": 686.8619921874991
          },
          "maximum_absolute_error_lux": 5512.54296875,
          "worst": {
            "sensor_index": 31,
            "position": [
              5.5,
              4.5,
              0.75
            ],
            "hour_of_year": 3829.5,
            "foton_lux": 31408.0625,
            "radiance_lux": 36920.60546875
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.263835616438357,
            "maximum_error_percentage_points": 1.2310958904109555,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.12569259098736613,
            "maximum_error_percentage_points": 0.5687569160112531,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.11035768645357688,
            "maximum_error_percentage_points": 0.737123287671233,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.6100038051750377,
            "maximum_error_percentage_points": 2.301506849315068,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.6625722983257227,
            "maximum_error_percentage_points": 2.631369863013699,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.4845562570934045,
          "cvrmse_percent": 30.732626109559124,
          "absolute_error_percentiles_lux": {
            "p50": 1.9522438049316406,
            "p90": 34.621286773681646,
            "p95": 57.64772567749018,
            "p99": 123.16415679931593
          },
          "maximum_absolute_error_lux": 351.4495849609375,
          "worst": {
            "sensor_index": 15,
            "position": [
              8.5,
              2.5,
              0.75
            ],
            "hour_of_year": 5245.5,
            "foton_lux": 527.3421020507812,
            "radiance_lux": 175.89251708984375
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.4029452054794518,
            "maximum_error_percentage_points": 4.4905479452054795,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.7570494301071302,
            "maximum_error_percentage_points": 2.8355513388270452,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 2.022952815829528,
            "maximum_error_percentage_points": 4.764109589041098,
            "passed": false
          },
          "udi": {
            "mean_absolute_error_percentage_points": 2.0233409436834093,
            "maximum_error_percentage_points": 4.7641095890410945,
            "passed": false
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0030745814307458178,
            "maximum_error_percentage_points": 0.05232876712328771,
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
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.036707398957943484,
          "cvrmse_percent": 9.893317346728153,
          "absolute_error_percentiles_lux": {
            "p50": 4.1269941329956055,
            "p90": 39.35795898437503,
            "p95": 58.34671287536617,
            "p99": 106.19631500244128
          },
          "maximum_absolute_error_lux": 278.63494873046875,
          "worst": {
            "sensor_index": 3,
            "position": [
              6.5,
              2.5,
              3.75
            ],
            "hour_of_year": 2722.5,
            "foton_lux": 733.7241821289062,
            "radiance_lux": 455.0892333984375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.7821385083713853,
            "maximum_error_percentage_points": 4.5526027397260265,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.5637521013553137,
            "maximum_error_percentage_points": 2.070069058605455,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 1.862172754946727,
            "maximum_error_percentage_points": 7.2091780821917695,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 1.8543226788432274,
            "maximum_error_percentage_points": 7.20917808219178,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.01923135464231353,
            "maximum_error_percentage_points": 0.11424657534246574,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 8.333333333333334,
          "radiance_percent": 8.333333333333334,
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
    "numerical_correctness": "failed",
    "honeybee_compatibility": "passed",
    "performance": "measured"
  },
  "compatibility": {
    "official_loader": {
      "passed": true,
      "tolerance_percentage_points": 0.05,
      "maximum_error_percentage_points": 0.004985284674653201,
      "metrics": {
        "da": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.004938463184927855,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.004828599903682118,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.004985284674653201,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.004794520547945602,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.004383561643835243,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.004794520547945602,
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
      "study_preparation_seconds": 0.04236950003542006,
      "weather_seconds": 0.13270687498152256,
      "metric_reduction_seconds": 0.09518620790913701,
      "write_seconds": 0.1128149579744786,
      "total_seconds": 0.3414537919452414,
      "cold_end_to_end_seconds": 0.38382329198066145,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.07843125006183982,
      "engine_upload_seconds": 0.00084,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.04304029163904488,
      "engine_annual_reduction_seconds": 0.0039696249878033996,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.04304029163904488
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.04236950003542006,
      "weather_seconds": 0.0940314169274643,
      "metric_reduction_seconds": 0.04963662498630583,
      "write_seconds": 0.07387787499465048,
      "total_seconds": 0.2177083749556914,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.2177083749556914,
      "raw_export_seconds": 0.04683345800731331,
      "engine_upload_seconds": 8.9375e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.004029166651889682,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.07148887496441603,
      "full": 0.03218149999156594
    }
  },
  "elapsed_seconds": 257.3120735840639,
  "result_class": "accuracy_failure"
}
```
