# Foton report

Status: **failed**

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
  "sky_density": 2,
  "status": "failed",
  "passed": false,
  "model_sha256": "fbcce45da92c8f96881c818170a6597fb4ce5110cff3fbe6550bc85e07b59751",
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
      "solver_version": "0.3.5",
      "scene_fingerprint": 14976319759523577797,
      "basis": "ReinhartMf2",
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
      "solver_version": "0.3.5",
      "scene_fingerprint": 14976319759523577797,
      "basis": "ReinhartMf2",
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
    "ray_count": 9248,
    "command": [
      "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/rcalc",
      "-e",
      "MF:2",
      "-f",
      "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/lib/reinhart.cal",
      "-e",
      "Dx=$1;Dy=$2;Dz=$3;$1=rbin"
    ],
    "calibration_sha256": "92b8c09984de7a551773530b3146ba79a51e1b003245f230b6e7b430eb6c26cd"
  },
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.5)",
      "weather_id": "82c544d76aea9710a570440071d4833104fdc7da7504bac286ac2afe42bdd614"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/gendaymtx",
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
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "c2e4f531547371b27c1dd0c370034fddec9ce9182e94e0b6d120f538dd23366b",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "66350f82bb3c17b7ccff8c0b3c7367203ce64ce6f95104e2c7e1fadb06f6afaf",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00014028436271473765,
          "p95": 4.362664185464382e-08,
          "p99": 7.011898560449481e-06
        },
        "bias_percent": -0.02630459349567195,
        "identifier": "interior_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7598521188292517,
        "worst_index": [
          17,
          543,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 2.3427215637639165e-05,
          "p95": 0.0,
          "p99": 0.0
        },
        "bias_percent": 0.0434975018413777,
        "identifier": "adjacent_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.2008082752797096,
        "worst_index": [
          7,
          157,
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
          "maximum": 0.0005295071750879288,
          "p95": 2.020248575718142e-05,
          "p99": 9.853305527940392e-05
        },
        "bias_percent": 0.018808273785132276,
        "identifier": "interior_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.7617961112200928,
        "worst_index": [
          20,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00010377319995313883,
          "p95": 2.1546466086874716e-06,
          "p99": 5.6685848903725855e-06
        },
        "bias_percent": -0.3432310905601105,
        "identifier": "adjacent_grid",
        "passed": true,
        "rms_normalized_error_percent": 4.47770642409799,
        "worst_index": [
          8,
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
          "maximum": 0.0006022118031978607,
          "p95": 1.6966136172413826e-05,
          "p99": 8.081085979938507e-05
        },
        "bias_percent": 0.038159527540234016,
        "identifier": "interior_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.482422823964732,
        "worst_index": [
          15,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 8.623674511909485e-05,
          "p95": 1.8638963865669211e-06,
          "p99": 5.0179467052657856e-06
        },
        "bias_percent": 0.5442206144717169,
        "identifier": "adjacent_grid",
        "passed": true,
        "rms_normalized_error_percent": 3.680740939436344,
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
            "identifier": "interior_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004925651010125875,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.9063434340059757e-05,
                  "p99": 0.00017679965822026134
                },
                "candidate_energy": 6.0242209594860014,
                "cvrmse_percent": 30.058056522903733,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.0741224855879456,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.028689574046666,
                "relative_energy_error_percent": 0.0741224855879456,
                "rms_normalized_rmse_percent": 5.800725369760597,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002483247546479106,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.0019906824454665184,
                  "rgb_channel": 0,
                  "sky_patch_index": 220
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009260987862944603,
                  "p50": 0.0,
                  "p90": 4.729128386316018e-06,
                  "p95": 4.5205000787973404e-05,
                  "p99": 0.0002705906517803669
                },
                "candidate_energy": 2.0114852170522823,
                "cvrmse_percent": 150.1597714820945,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.3968093204138728,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0035350034209536,
                "relative_energy_error_percent": 0.3968093204138729,
                "rms_normalized_rmse_percent": 5.492602945421785,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.016126510687172413,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.017052609473466873,
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
                  "maximum": 0.0001709456992102787,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.06450563069847703,
                "cvrmse_percent": 442.4500599305595,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.18792093854086594,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.06462707851096638,
                "relative_energy_error_percent": 0.18792093854086594,
                "rms_normalized_rmse_percent": 21.257463998209875,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 4.886152601102367e-05,
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "reference": 0.00021980722522130236,
                  "rgb_channel": 0,
                  "sky_patch_index": 38
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0002718979667406529,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.23857852385845e-06
                },
                "candidate_energy": 0.06965152337556901,
                "cvrmse_percent": 628.0865402781592,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 1.1640690385149726,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.06885006113094505,
                "relative_energy_error_percent": 1.1640690385149723,
                "rms_normalized_rmse_percent": 16.847688022901732,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0001079530265997164,
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "reference": -0.00016394494014093652,
                  "rgb_channel": 0,
                  "sky_patch_index": 38
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 137.65737495850772,
            "full": 381.33520807605237
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.68458310328424,
            "full": 379.1094170883298
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 128.91441595274955,
            "full": 396.64366701617837
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 135.7452089432627,
            "full": 446.81537500582635
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
            "identifier": "interior_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00042109203059226274,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2141961380839348e-05,
                  "p99": 0.00013110041618347168
                },
                "candidate_energy": 6.025024866511217,
                "cvrmse_percent": 23.61396122243673,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.028038653329373397,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.026714676146412,
                "relative_energy_error_percent": 0.028038653329373393,
                "rms_normalized_rmse_percent": 4.553591827264113,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0035111865727230906,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.003932278603315353,
                  "rgb_channel": 0,
                  "sky_patch_index": 363
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007873745635151863,
                  "p50": 2.0136974754336734e-08,
                  "p90": 1.2797120689356276e-05,
                  "p95": 3.555754665285349e-05,
                  "p99": 0.00019167416030541062
                },
                "candidate_energy": 3.6200263031264512,
                "cvrmse_percent": 61.200201960998314,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.10958083567664215,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.6160637902065424,
                "relative_energy_error_percent": 0.10958083567664216,
                "rms_normalized_rmse_percent": 3.1994360598311284,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.017125659622251987,
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "reference": 0.0163382850587368,
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
                  "maximum": 0.00013043885155639146,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.06493105960726098,
                "cvrmse_percent": 295.24351815375246,
                "energy_difference_negligible": true,
                "nmbe_percent": 1.8030413262771836,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.06378106072406808,
                "relative_energy_error_percent": 1.8030413262771838,
                "rms_normalized_rmse_percent": 13.89272323117169,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00022536074538948014,
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "reference": 9.492189383308869e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 40
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005461839027702808,
                  "p50": 0.0,
                  "p90": 1.6861012504421105e-06,
                  "p95": 3.144284107747808e-06,
                  "p99": 8.539134796592407e-06
                },
                "candidate_energy": 0.16592660042842766,
                "cvrmse_percent": 251.76396917000676,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -1.131202450008735,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.16782504140856958,
                "relative_energy_error_percent": 1.1312024500087352,
                "rms_normalized_rmse_percent": 11.797871010211555,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.003455877071246505,
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "reference": 0.004002060974016786,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 194.9062090134248,
            "full": 5059.5036670565605
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 188.35466704331338,
            "full": 4993.06308303494
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 187.05687497276813,
            "full": 5031.739167054184
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 192.40437494590878,
            "full": 5126.644416013733
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
            "identifier": "interior_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00038522493559867144,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3077154764905572e-05,
                  "p99": 0.00012921495363116264
                },
                "candidate_energy": 6.029578863824781,
                "cvrmse_percent": 24.136347827413715,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.046440148417874104,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.026780018239492,
                "relative_energy_error_percent": 0.046440148417874104,
                "rms_normalized_rmse_percent": 4.661234998392239,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003946701996028423,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.003561477060429752,
                  "rgb_channel": 0,
                  "sky_patch_index": 313
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009616799652576447,
                  "p50": 2.7701094751364508e-08,
                  "p90": 1.2940520900883716e-05,
                  "p95": 3.596383612602949e-05,
                  "p99": 0.00019248202443122864
                },
                "candidate_energy": 3.6137172208629487,
                "cvrmse_percent": 62.282074666976364,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.21163147423853926,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.6213812032912713,
                "relative_energy_error_percent": 0.21163147423853923,
                "rms_normalized_rmse_percent": 3.264091908580125,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.025577395223081112,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.024615715257823467,
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
                  "maximum": 9.450070501770824e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.06325064401153213,
                "cvrmse_percent": 221.85073287247067,
                "energy_difference_negligible": true,
                "nmbe_percent": -1.3194082958759448,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.06409633639123058,
                "relative_energy_error_percent": 1.3194082958759445,
                "rms_normalized_rmse_percent": 10.652339039431347,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00046121359628159553,
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "reference": 0.0005557143012993038,
                  "rgb_channel": 0,
                  "sky_patch_index": 100
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00028253847267478704,
                  "p50": 0.0,
                  "p90": 1.6815409573212107e-06,
                  "p95": 3.0310283136714133e-06,
                  "p99": 8.467964988767562e-06
                },
                "candidate_energy": 0.16613034077421673,
                "cvrmse_percent": 176.11691894175735,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.7579358389410449,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.16739911868883084,
                "relative_energy_error_percent": 0.7579358389410449,
                "rms_normalized_rmse_percent": 8.143163179329733,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.003669074038043618,
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "reference": 0.003951612510718405,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 215.01604199875146,
            "full": 5443.422500044107
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 187.20658402889967,
            "full": 5365.552500006743
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 211.51704096700996,
            "full": 5339.8275000508875
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 197.72979198023677,
            "full": 5415.12124997098
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
            "identifier": "interior_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001685525057837367,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1565134627744555e-05,
                  "p99": 7.016686140559614e-05
                },
                "candidate_energy": 6.025644412807765,
                "cvrmse_percent": 12.88564539449314,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.03146109324579998,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.023749275431328,
                "relative_energy_error_percent": 0.03146109324579998,
                "rms_normalized_rmse_percent": 2.4886889372282393,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003208194044418633,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0033767465502023697,
                  "rgb_channel": 0,
                  "sky_patch_index": 482
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00036730989813804626,
                  "p50": 3.150600669243886e-08,
                  "p90": 9.005756510305252e-06,
                  "p95": 2.16099142562598e-05,
                  "p99": 0.00010975380428135395
                },
                "candidate_energy": 3.6245701697292603,
                "cvrmse_percent": 34.79610693922264,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.007858696292355092,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.6248550360775837,
                "relative_energy_error_percent": 0.007858696292355092,
                "rms_normalized_rmse_percent": 1.8214884252646626,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.029361574910581112,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.029728884808719158,
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
                  "maximum": 6.489299994427711e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.06428762632322105,
                "cvrmse_percent": 126.16243443896163,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.028288084671744075,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.06430581720724149,
                "relative_energy_error_percent": 0.028288084671744075,
                "rms_normalized_rmse_percent": 6.0418389096155085,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00028545790701173246,
                  "global_sensor_index": 49,
                  "local_sensor_index": 13,
                  "reference": 0.00035035090695600957,
                  "rgb_channel": 0,
                  "sky_patch_index": 100
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00023964792490005493,
                  "p50": 0.0,
                  "p90": 1.287383221182385e-06,
                  "p95": 2.1636273004332907e-06,
                  "p99": 5.47405124962097e-06
                },
                "candidate_energy": 0.1676847153328076,
                "cvrmse_percent": 120.609181496883,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.3460399852342431,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.167106460162735,
                "relative_energy_error_percent": 0.3460399852342432,
                "rms_normalized_rmse_percent": 5.574230301785225,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.004191749496385455,
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "reference": 0.00443139742128551,
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
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 308.1730830017477,
            "full": 9285.070084035397
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 310.33533392474055,
            "full": 9261.428958037868
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 317.51000008080155,
            "full": 9427.104000002146
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 311.6852919338271,
            "full": 9483.047250076197
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
    "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/oconv",
    "/content/suite-vulkan/interior_glazing/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10738.50408301223,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 42869.95299998671,
      "invocation_count": 5,
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
      72,
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
        "identifier": "interior_glazing_grid",
        "full_identifier": "interior_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.16948861504332854,
            "cvrmse_percent": 3.7319181304529665,
            "rms_normalized_rmse_percent": 0.7209212968962605,
            "reference_energy": 6.02483990591449,
            "candidate_energy": 6.014628488199378,
            "relative_energy_error_percent": 0.16948861504332854,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.378954716026783e-08,
              "p99": 9.110369319387246e-06,
              "maximum": 0.00011773567530326545
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 144,
              "rgb_channel": 0,
              "reference": 0.00011773567530326545,
              "candidate": 0.0,
              "position": [
                5.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.0607516204614817,
            "cvrmse_percent": 45.66315777843512,
            "rms_normalized_rmse_percent": 2.390027055755507,
            "reference_energy": 3.624569535359754,
            "candidate_energy": 3.586121855278672,
            "relative_energy_error_percent": 1.0607516204614817,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.0243153155897747e-05,
              "p95": 1.739122672006488e-05,
              "p99": 5.296070594340563e-05,
              "maximum": 0.0010471716523170471
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02954523079097271,
              "candidate": 0.028498059138655663,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5042702156264643,
            "cvrmse_percent": 17.03214344207561,
            "rms_normalized_rmse_percent": 2.373288204946637,
            "reference_energy": 9.649409441274244,
            "candidate_energy": 9.60075034347805,
            "relative_energy_error_percent": 0.5042702156264736,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.0135328739124847e-05,
              "p95": 1.6752397641539574e-05,
              "p99": 4.974647890776396e-05,
              "maximum": 0.0010471716523170471
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02954523079097271,
              "candidate": 0.028498059138655663,
              "position": [
                1.5,
                1.5,
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
            "nmbe_percent": -0.023339812571260464,
            "cvrmse_percent": 21.95679484198042,
            "rms_normalized_rmse_percent": 1.052983571700167,
            "reference_energy": 0.06414209702461449,
            "candidate_energy": 0.06412712637938967,
            "relative_energy_error_percent": 0.023339812571260464,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 1.1447875294834375e-05
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 159,
              "rgb_channel": 0,
              "reference": 0.0005599533906206489,
              "candidate": 0.0005485055153258145,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.41919679172414953,
            "cvrmse_percent": 75.42662775296571,
            "rms_normalized_rmse_percent": 3.508230395540072,
            "reference_energy": 0.1675502152153694,
            "candidate_energy": 0.16684785008865965,
            "relative_energy_error_percent": 0.4191967917241496,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.3185826105655e-06,
              "p95": 2.136175396572071e-06,
              "p99": 4.991423338651657e-06,
              "maximum": 0.00016891350969672203
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.004311573691666126,
              "candidate": 0.004142660181969404,
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
            "nmbe_percent": -0.30960706680312744,
            "cvrmse_percent": 53.88318992848979,
            "rms_normalized_rmse_percent": 3.4656392042613766,
            "reference_energy": 0.23169231223998388,
            "candidate_energy": 0.23097497646804932,
            "relative_energy_error_percent": 0.30960706680312744,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.3183965052121496e-06,
              "p95": 2.1361338440328836e-06,
              "p99": 4.912774784315843e-06,
              "maximum": 0.00016891350969672203
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.004311573691666126,
              "candidate": 0.004142660181969404,
              "position": [
                6.5,
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
      72,
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
        "identifier": "interior_glazing_grid",
        "full_identifier": "interior_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.16948861504332854,
            "cvrmse_percent": 3.7319181304529665,
            "rms_normalized_rmse_percent": 0.7209212968962605,
            "reference_energy": 6.02483990591449,
            "candidate_energy": 6.014628488199378,
            "relative_energy_error_percent": 0.16948861504332854,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.378954716026783e-08,
              "p99": 9.110369319387246e-06,
              "maximum": 0.00011773567530326545
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 144,
              "rgb_channel": 0,
              "reference": 0.00011773567530326545,
              "candidate": 0.0,
              "position": [
                5.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 78.4916834335007,
            "cvrmse_percent": 807.4862520691768,
            "rms_normalized_rmse_percent": 29.626376160611567,
            "reference_energy": 2.0091254596826786,
            "candidate_energy": 3.586121855278672,
            "relative_energy_error_percent": 78.49168343350068,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.420399938884666e-05,
              "p95": 7.580000237794593e-05,
              "p99": 0.00016253860667347908,
              "maximum": 0.007478279992938042
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01575234904885292,
              "candidate": 0.023230629041790962,
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
            "nmbe_percent": 19.50201309791707,
            "cvrmse_percent": 201.90604743942237,
            "rms_normalized_rmse_percent": 29.622084797884476,
            "reference_energy": 8.033965365597169,
            "candidate_energy": 9.60075034347805,
            "relative_energy_error_percent": 19.502013097917064,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.3668962209485525e-05,
              "p95": 7.493000157410279e-05,
              "p99": 0.00016128818970173597,
              "maximum": 0.007478279992938042
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01575234904885292,
              "candidate": 0.023230629041790962,
              "position": [
                0.5,
                1.5,
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
            "nmbe_percent": -0.023339812571260464,
            "cvrmse_percent": 21.95679484198042,
            "rms_normalized_rmse_percent": 1.052983571700167,
            "reference_energy": 0.06414209702461449,
            "candidate_energy": 0.06412712637938967,
            "relative_energy_error_percent": 0.023339812571260464,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 1.1447875294834375e-05
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 159,
              "rgb_channel": 0,
              "reference": 0.0005599533906206489,
              "candidate": 0.0005485055153258145,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 139.46570137704666,
            "cvrmse_percent": 1690.2438908798833,
            "rms_normalized_rmse_percent": 45.41269494140657,
            "reference_energy": 0.06967505121994577,
            "candidate_energy": 0.16684785008865965,
            "relative_energy_error_percent": 139.46570137704668,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.7000000955013093e-06,
              "p95": 4.800000169780105e-06,
              "p99": 1.3872809631720884e-05,
              "maximum": 0.001194442855194211
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.002948217326775193,
              "candidate": 0.004142660181969404,
              "position": [
                6.5,
                2.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 72.60491610979953,
            "cvrmse_percent": 879.8880179168143,
            "rms_normalized_rmse_percent": 45.40354655023841,
            "reference_energy": 0.13381714824456026,
            "candidate_energy": 0.23097497646804932,
            "relative_energy_error_percent": 72.60491610979953,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.7000000955013093e-06,
              "p95": 4.819999958272092e-06,
              "p99": 1.3939999917056412e-05,
              "maximum": 0.001194442855194211
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.002948217326775193,
              "candidate": 0.004142660181969404,
              "position": [
                6.5,
                2.5,
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
      "bias_percent": 0.05877463764918458,
      "rms_normalized_error_percent": 0.18718719925704339,
      "absolute_error": {
        "p95": 0.05772412660101788,
        "p99": 0.1006812414904146,
        "maximum": 0.12121265112837598
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.0432872538974545,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.18718719925704339
    },
    "overcast": {
      "bias_percent": 0.03469955937169766,
      "rms_normalized_error_percent": 0.13226688499564487,
      "absolute_error": {
        "p95": 0.03356558084487916,
        "p99": 0.046921122074127304,
        "maximum": 0.05907607078552246
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.8640246391296387,
      "reference_fraction_of_uniform": 0.6393911838531494,
      "rms_normalized_to_uniform_percent": 0.0941629683743373
    },
    "horizon": {
      "bias_percent": 0.7432850319918518,
      "rms_normalized_error_percent": 1.7515605803254422,
      "absolute_error": {
        "p95": 0.037237536999827965,
        "p99": 0.07134690130273137,
        "maximum": 0.08164045899962025
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.7221452617884775,
      "reference_fraction_of_uniform": 0.11949543873208235,
      "rms_normalized_to_uniform_percent": 0.11897963971038666
    },
    "north": {
      "bias_percent": -90.61795460696086,
      "rms_normalized_error_percent": 99.63107547378671,
      "absolute_error": {
        "p95": 4.218674985168036e-05,
        "p99": 0.00012129427609295418,
        "maximum": 0.00018446033431018805
      },
      "worst_index": [
        25
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 8.711785085324664e-06,
      "reference_fraction_of_uniform": 1.4415639952858328e-06,
      "rms_normalized_to_uniform_percent": 0.00018230445188411495
    },
    "east": {
      "bias_percent": 0.05013685157765668,
      "rms_normalized_error_percent": 0.19590449061593737,
      "absolute_error": {
        "p95": 0.010740214586257936,
        "p99": 0.0225319296121598,
        "maximum": 0.030874967575073242
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1377605199813843,
      "reference_fraction_of_uniform": 0.1882684826850891,
      "rms_normalized_to_uniform_percent": 0.039472017147057205
    },
    "south": {
      "bias_percent": 0.12492254648534949,
      "rms_normalized_error_percent": 0.2425059843856206,
      "absolute_error": {
        "p95": 0.0468327403068543,
        "p99": 0.09106572628021244,
        "maximum": 0.09505152702331543
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.201826095581055,
      "reference_fraction_of_uniform": 0.6952881813049316,
      "rms_normalized_to_uniform_percent": 0.1583478628827537
    },
    "west": {
      "bias_percent": -0.31663566515295033,
      "rms_normalized_error_percent": 0.44067734825423127,
      "absolute_error": {
        "p95": 0.026920047402381957,
        "p99": 0.055386184453964316,
        "maximum": 0.06503760814666748
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.172620177268982,
      "reference_fraction_of_uniform": 0.1940368115901947,
      "rms_normalized_to_uniform_percent": 0.08867411605032909
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
          "nmbe_percent": -0.014163308575380774,
          "cvrmse_percent": 1.8161992882497449,
          "absolute_error_percentiles_lux": {
            "p50": 2.0363388061523438,
            "p90": 22.937658691406252,
            "p95": 36.8618194580078,
            "p99": 81.7302050781249
          },
          "maximum_absolute_error_lux": 415.28857421875,
          "worst": {
            "sensor_index": 33,
            "position": [
              5.5,
              2.5,
              0.75
            ],
            "hour_of_year": 1863.5,
            "foton_lux": 5663.458984375,
            "radiance_lux": 6078.74755859375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2782762557077621,
            "maximum_error_percentage_points": 1.012739726027391,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.12983850155020626,
            "maximum_error_percentage_points": 0.8173448724507821,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.11108447488584468,
            "maximum_error_percentage_points": 0.4121917808219173,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.11202435312024307,
            "maximum_error_percentage_points": 0.4089041095890451,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.018812785388127917,
            "maximum_error_percentage_points": 0.07945205479452255,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 52.77777777777778,
          "radiance_percent": 52.77777777777778,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "adjacent_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.4419880065565186,
          "cvrmse_percent": 14.39023850217827,
          "absolute_error_percentiles_lux": {
            "p50": 0.222800612449646,
            "p90": 3.0257740020751958,
            "p95": 4.678919792175291,
            "p99": 9.455699615478501
          },
          "maximum_absolute_error_lux": 52.466552734375,
          "worst": {
            "sensor_index": 2,
            "position": [
              6.5,
              3.5,
              0.75
            ],
            "hour_of_year": 1359.5,
            "foton_lux": 2364.78466796875,
            "radiance_lux": 2312.318115234375
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.004535768645357692,
            "maximum_error_percentage_points": 0.0321917808219178,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.09302190243100274,
            "maximum_error_percentage_points": 0.20174488681227487,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.0692465753424665,
            "maximum_error_percentage_points": 1.2364383561643848,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.06910197869101986,
            "maximum_error_percentage_points": 1.2312328767123333,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0001331811263318111,
            "maximum_error_percentage_points": 0.0047945205479452,
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
    "numerical_correctness": "failed",
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
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.00481538955480687,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.004876106993792595,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004794520547953596,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
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
      "study_preparation_seconds": 0.4154402960000425,
      "weather_seconds": 0.43269721499996194,
      "metric_reduction_seconds": 0.611173215000008,
      "write_seconds": 0.030619423999951323,
      "total_seconds": 1.0750306570000703,
      "cold_end_to_end_seconds": 1.4904709530001128,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.006081313000095179,
      "engine_upload_seconds": 0.076312676,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.064980319,
      "engine_annual_reduction_seconds": 0.012350748,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.064980319
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.4154402960000425,
      "weather_seconds": 0.4586712459999944,
      "metric_reduction_seconds": 0.44828390899988335,
      "write_seconds": 0.014000976999795967,
      "total_seconds": 0.9216449359998933,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.9216449359998933,
      "raw_export_seconds": 0.0025148539998554043,
      "engine_upload_seconds": 0.063721973,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.1e-08,
      "engine_annual_reduction_seconds": 0.014978746,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.037617979000060586,
      "full": 0.11207722099993589
    }
  },
  "elapsed_seconds": 6.410335527999905,
  "result_class": "accuracy_failure"
}
```
