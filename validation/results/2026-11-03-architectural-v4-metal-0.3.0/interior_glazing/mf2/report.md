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
  "model_sha256": "c2e4f531547371b27c1dd0c370034fddec9ce9182e94e0b6d120f538dd23366b",
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
      "scene_fingerprint": 14976319759523577797,
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
      "scene_fingerprint": 14976319759523577797,
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
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "interior_glazing_grid",
        "bias_percent": -0.02630459349567195,
        "rms_normalized_error_percent": 0.7598521188292517,
        "absolute_error": {
          "p95": 4.362664185464382e-08,
          "p99": 7.011898560449481e-06,
          "maximum": 0.00014028436271473765
        },
        "worst_index": [
          17,
          543,
          0
        ],
        "passed": true
      },
      {
        "identifier": "adjacent_grid",
        "bias_percent": 0.0434975018413777,
        "rms_normalized_error_percent": 2.2008082752797096,
        "absolute_error": {
          "p95": 0.0,
          "p99": 0.0,
          "maximum": 2.3427215637639165e-05
        },
        "worst_index": [
          7,
          157,
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
        "identifier": "interior_glazing_grid",
        "bias_percent": 0.018808273785132276,
        "rms_normalized_error_percent": 1.7617961112200928,
        "absolute_error": {
          "p95": 2.020248575718142e-05,
          "p99": 9.853305527940392e-05,
          "maximum": 0.0005295071750879288
        },
        "worst_index": [
          20,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "adjacent_grid",
        "bias_percent": -0.3432310905601105,
        "rms_normalized_error_percent": 4.47770642409799,
        "absolute_error": {
          "p95": 2.1546466086874716e-06,
          "p99": 5.6685848903725855e-06,
          "maximum": 0.00010377319995313883
        },
        "worst_index": [
          8,
          0,
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
        "identifier": "interior_glazing_grid",
        "bias_percent": 0.038159527540234016,
        "rms_normalized_error_percent": 1.482422823964732,
        "absolute_error": {
          "p95": 1.6966136172413826e-05,
          "p99": 8.081085979938507e-05,
          "maximum": 0.0006022118031978607
        },
        "worst_index": [
          15,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "adjacent_grid",
        "bias_percent": 0.5442206144717169,
        "rms_normalized_error_percent": 3.680740939436344,
        "absolute_error": {
          "p95": 1.8638963865669211e-06,
          "p99": 5.0179467052657856e-06,
          "maximum": 8.623674511909485e-05
        },
        "worst_index": [
          3,
          0,
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
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "interior_glazing_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.0741224855879456,
                "cvrmse_percent": 30.058056522903733,
                "rms_normalized_rmse_percent": 5.800725369760597,
                "reference_energy": 6.028689574046666,
                "candidate_energy": 6.0242209594860014,
                "relative_energy_error_percent": 0.0741224855879456,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.9063434340059757e-05,
                  "p99": 0.00017679965822026134,
                  "maximum": 0.0004925651010125875
                },
                "worst": {
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "sky_patch_index": 220,
                  "rgb_channel": 0,
                  "reference": 0.0019906824454665184,
                  "candidate": 0.002483247546479106
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.3968093204138728,
                "cvrmse_percent": 150.1597714820945,
                "rms_normalized_rmse_percent": 5.492602945421785,
                "reference_energy": 2.0035350034209536,
                "candidate_energy": 2.0114852170522823,
                "relative_energy_error_percent": 0.3968093204138729,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.729128386316018e-06,
                  "p95": 4.5205000787973404e-05,
                  "p99": 0.0002705906517803669,
                  "maximum": 0.0009260987862944603
                },
                "worst": {
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.017052609473466873,
                  "candidate": 0.016126510687172413
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "adjacent_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.18792093854086594,
                "cvrmse_percent": 442.4500599305595,
                "rms_normalized_rmse_percent": 21.257463998209875,
                "reference_energy": 0.06462707851096638,
                "candidate_energy": 0.06450563069847703,
                "relative_energy_error_percent": 0.18792093854086594,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.0001709456992102787
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "sky_patch_index": 38,
                  "rgb_channel": 0,
                  "reference": 0.00021980722522130236,
                  "candidate": 4.886152601102367e-05
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 1.1640690385149726,
                "cvrmse_percent": 628.0865402781592,
                "rms_normalized_rmse_percent": 16.847688022901732,
                "reference_energy": 0.06885006113094505,
                "candidate_energy": 0.06965152337556901,
                "relative_energy_error_percent": 1.1640690385149723,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.23857852385845e-06,
                  "maximum": 0.0002718979667406529
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "sky_patch_index": 38,
                  "rgb_channel": 0,
                  "reference": -0.00016394494014093652,
                  "candidate": 0.0001079530265997164
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 137.65737495850772,
            "full": 381.33520807605237
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 135.68458310328424,
            "full": 379.1094170883298
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 128.91441595274955,
            "full": 396.64366701617837
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 135.7452089432627,
            "full": 446.81537500582635
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
            "identifier": "interior_glazing_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.028038653329373397,
                "cvrmse_percent": 23.61396122243673,
                "rms_normalized_rmse_percent": 4.553591827264113,
                "reference_energy": 6.026714676146412,
                "candidate_energy": 6.025024866511217,
                "relative_energy_error_percent": 0.028038653329373393,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2141961380839348e-05,
                  "p99": 0.00013110041618347168,
                  "maximum": 0.00042109203059226274
                },
                "worst": {
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "sky_patch_index": 363,
                  "rgb_channel": 0,
                  "reference": 0.003932278603315353,
                  "candidate": 0.0035111865727230906
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.10958083567664215,
                "cvrmse_percent": 61.200201960998314,
                "rms_normalized_rmse_percent": 3.1994360598311284,
                "reference_energy": 3.6160637902065424,
                "candidate_energy": 3.6200263031264512,
                "relative_energy_error_percent": 0.10958083567664216,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.0136974754336734e-08,
                  "p90": 1.2797120689356276e-05,
                  "p95": 3.555754665285349e-05,
                  "p99": 0.00019167416030541062,
                  "maximum": 0.0007873745635151863
                },
                "worst": {
                  "global_sensor_index": 31,
                  "local_sensor_index": 31,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0163382850587368,
                  "candidate": 0.017125659622251987
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "adjacent_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 1.8030413262771836,
                "cvrmse_percent": 295.24351815375246,
                "rms_normalized_rmse_percent": 13.89272323117169,
                "reference_energy": 0.06378106072406808,
                "candidate_energy": 0.06493105960726098,
                "relative_energy_error_percent": 1.8030413262771838,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.00013043885155639146
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "sky_patch_index": 40,
                  "rgb_channel": 0,
                  "reference": 9.492189383308869e-05,
                  "candidate": 0.00022536074538948014
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -1.131202450008735,
                "cvrmse_percent": 251.76396917000676,
                "rms_normalized_rmse_percent": 11.797871010211555,
                "reference_energy": 0.16782504140856958,
                "candidate_energy": 0.16592660042842766,
                "relative_energy_error_percent": 1.1312024500087352,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.6861012504421105e-06,
                  "p95": 3.144284107747808e-06,
                  "p99": 8.539134796592407e-06,
                  "maximum": 0.0005461839027702808
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.004002060974016786,
                  "candidate": 0.003455877071246505
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 194.9062090134248,
            "full": 5059.5036670565605
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 188.35466704331338,
            "full": 4993.06308303494
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 187.05687497276813,
            "full": 5031.739167054184
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 192.40437494590878,
            "full": 5126.644416013733
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
            "identifier": "interior_glazing_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.046440148417874104,
                "cvrmse_percent": 24.136347827413715,
                "rms_normalized_rmse_percent": 4.661234998392239,
                "reference_energy": 6.026780018239492,
                "candidate_energy": 6.029578863824781,
                "relative_energy_error_percent": 0.046440148417874104,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3077154764905572e-05,
                  "p99": 0.00012921495363116264,
                  "maximum": 0.00038522493559867144
                },
                "worst": {
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "sky_patch_index": 313,
                  "rgb_channel": 0,
                  "reference": 0.003561477060429752,
                  "candidate": 0.003946701996028423
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.21163147423853926,
                "cvrmse_percent": 62.282074666976364,
                "rms_normalized_rmse_percent": 3.264091908580125,
                "reference_energy": 3.6213812032912713,
                "candidate_energy": 3.6137172208629487,
                "relative_energy_error_percent": 0.21163147423853923,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.7701094751364508e-08,
                  "p90": 1.2940520900883716e-05,
                  "p95": 3.596383612602949e-05,
                  "p99": 0.00019248202443122864,
                  "maximum": 0.0009616799652576447
                },
                "worst": {
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.024615715257823467,
                  "candidate": 0.025577395223081112
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "adjacent_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -1.3194082958759448,
                "cvrmse_percent": 221.85073287247067,
                "rms_normalized_rmse_percent": 10.652339039431347,
                "reference_energy": 0.06409633639123058,
                "candidate_energy": 0.06325064401153213,
                "relative_energy_error_percent": 1.3194082958759445,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 9.450070501770824e-05
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "sky_patch_index": 100,
                  "rgb_channel": 0,
                  "reference": 0.0005557143012993038,
                  "candidate": 0.00046121359628159553
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.7579358389410449,
                "cvrmse_percent": 176.11691894175735,
                "rms_normalized_rmse_percent": 8.143163179329733,
                "reference_energy": 0.16739911868883084,
                "candidate_energy": 0.16613034077421673,
                "relative_energy_error_percent": 0.7579358389410449,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.6815409573212107e-06,
                  "p95": 3.0310283136714133e-06,
                  "p99": 8.467964988767562e-06,
                  "maximum": 0.00028253847267478704
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.003951612510718405,
                  "candidate": 0.003669074038043618
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 215.01604199875146,
            "full": 5443.422500044107
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 187.20658402889967,
            "full": 5365.552500006743
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 211.51704096700996,
            "full": 5339.8275000508875
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 197.72979198023677,
            "full": 5415.12124997098
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
            "identifier": "interior_glazing_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.03146109324579998,
                "cvrmse_percent": 12.88564539449314,
                "rms_normalized_rmse_percent": 2.4886889372282393,
                "reference_energy": 6.023749275431328,
                "candidate_energy": 6.025644412807765,
                "relative_energy_error_percent": 0.03146109324579998,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1565134627744555e-05,
                  "p99": 7.016686140559614e-05,
                  "maximum": 0.0001685525057837367
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 482,
                  "rgb_channel": 0,
                  "reference": 0.0033767465502023697,
                  "candidate": 0.003208194044418633
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.007858696292355092,
                "cvrmse_percent": 34.79610693922264,
                "rms_normalized_rmse_percent": 1.8214884252646626,
                "reference_energy": 3.6248550360775837,
                "candidate_energy": 3.6245701697292603,
                "relative_energy_error_percent": 0.007858696292355092,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.150600669243886e-08,
                  "p90": 9.005756510305252e-06,
                  "p95": 2.16099142562598e-05,
                  "p99": 0.00010975380428135395,
                  "maximum": 0.00036730989813804626
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.029728884808719158,
                  "candidate": 0.029361574910581112
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "adjacent_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.028288084671744075,
                "cvrmse_percent": 126.16243443896163,
                "rms_normalized_rmse_percent": 6.0418389096155085,
                "reference_energy": 0.06430581720724149,
                "candidate_energy": 0.06428762632322105,
                "relative_energy_error_percent": 0.028288084671744075,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 6.489299994427711e-05
                },
                "worst": {
                  "global_sensor_index": 49,
                  "local_sensor_index": 13,
                  "sky_patch_index": 100,
                  "rgb_channel": 0,
                  "reference": 0.00035035090695600957,
                  "candidate": 0.00028545790701173246
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.3460399852342431,
                "cvrmse_percent": 120.609181496883,
                "rms_normalized_rmse_percent": 5.574230301785225,
                "reference_energy": 0.167106460162735,
                "candidate_energy": 0.1676847153328076,
                "relative_energy_error_percent": 0.3460399852342432,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.287383221182385e-06,
                  "p95": 2.1636273004332907e-06,
                  "p99": 5.47405124962097e-06,
                  "maximum": 0.00023964792490005493
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.00443139742128551,
                  "candidate": 0.004191749496385455
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 308.1730830017477,
            "full": 9285.070084035397
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 310.33533392474055,
            "full": 9261.428958037868
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 317.51000008080155,
            "full": 9427.104000002146
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
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 311.6852919338271,
            "full": 9483.047250076197
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/interior_glazing/mf2/oracle/scene.rad"
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
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 10738.50408301223,
      "worker_pool_size": 12,
      "invocation_count": 5
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
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 42869.95299998671,
      "worker_pool_size": 12,
      "invocation_count": 5
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
            "nmbe_percent": -0.16948668053065924,
            "cvrmse_percent": 3.731919546018636,
            "rms_normalized_rmse_percent": 0.7209215703511979,
            "reference_energy": 6.02483990591449,
            "candidate_energy": 6.014628604750669,
            "relative_energy_error_percent": 0.16948668053065924,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.3818650990724564e-08,
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
            "nmbe_percent": -1.0605307834380262,
            "cvrmse_percent": 45.66136774311221,
            "rms_normalized_rmse_percent": 2.3899333646254872,
            "reference_energy": 3.624569535359754,
            "candidate_energy": 3.586129859670147,
            "relative_energy_error_percent": 1.0605307834380262,
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
            "nmbe_percent": -0.5041860556287393,
            "cvrmse_percent": 17.031493103411563,
            "rms_normalized_rmse_percent": 2.3731975856369854,
            "reference_energy": 9.649409441274244,
            "candidate_energy": 9.600758464420815,
            "relative_energy_error_percent": 0.5041860556287485,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.0135328739124847e-05,
              "p95": 1.6738002159399912e-05,
              "p99": 4.9746595323085785e-05,
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
            "nmbe_percent": -0.023336678575401514,
            "cvrmse_percent": 21.956772502759733,
            "rms_normalized_rmse_percent": 1.0529825003765718,
            "reference_energy": 0.06414209702461449,
            "candidate_energy": 0.06412712838960033,
            "relative_energy_error_percent": 0.023336678575401514,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 1.1447817087173462e-05
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 159,
              "rgb_channel": 0,
              "reference": 0.0005599533906206489,
              "candidate": 0.0005485055735334754,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.4083820851770847,
            "cvrmse_percent": 75.44840859799056,
            "rms_normalized_rmse_percent": 3.5092434624745636,
            "reference_energy": 0.1675502152153694,
            "candidate_energy": 0.16686597015275417,
            "relative_energy_error_percent": 0.4083820851770847,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.3185826105655e-06,
              "p95": 2.1365242606208312e-06,
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
            "nmbe_percent": -0.3017854545407353,
            "cvrmse_percent": 53.89913695293035,
            "rms_normalized_rmse_percent": 3.4666648791177814,
            "reference_energy": 0.23169231223998388,
            "candidate_energy": 0.2309930985423545,
            "relative_energy_error_percent": 0.3017854545407353,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.3183965052121496e-06,
              "p95": 2.136175396572071e-06,
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
            "nmbe_percent": -0.16948668053065924,
            "cvrmse_percent": 3.731919546018636,
            "rms_normalized_rmse_percent": 0.7209215703511979,
            "reference_energy": 6.02483990591449,
            "candidate_energy": 6.014628604750669,
            "relative_energy_error_percent": 0.16948668053065924,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.3818650990724564e-08,
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
            "nmbe_percent": 78.49208183527477,
            "cvrmse_percent": 807.5006488833368,
            "rms_normalized_rmse_percent": 29.626904374473693,
            "reference_energy": 2.0091254596826786,
            "candidate_energy": 3.586129859670147,
            "relative_energy_error_percent": 78.49208183527476,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.420399938884666e-05,
              "p95": 7.580000237794593e-05,
              "p99": 0.00016253860667347908,
              "maximum": 0.007478291168808937
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01575234904885292,
              "candidate": 0.023230640217661858,
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
            "nmbe_percent": 19.50211418053813,
            "cvrmse_percent": 201.90965200226228,
            "rms_normalized_rmse_percent": 29.622613631307036,
            "reference_energy": 8.033965365597169,
            "candidate_energy": 9.600758464420815,
            "relative_energy_error_percent": 19.50211418053812,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.3668962209485525e-05,
              "p95": 7.493000157410279e-05,
              "p99": 0.00016128818970173597,
              "maximum": 0.007478291168808937
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01575234904885292,
              "candidate": 0.023230640217661858,
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
            "nmbe_percent": -0.023336678575401514,
            "cvrmse_percent": 21.956772502759733,
            "rms_normalized_rmse_percent": 1.0529825003765718,
            "reference_energy": 0.06414209702461449,
            "candidate_energy": 0.06412712838960033,
            "relative_energy_error_percent": 0.023336678575401514,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 1.1447817087173462e-05
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 159,
              "rgb_channel": 0,
              "reference": 0.0005599533906206489,
              "candidate": 0.0005485055735334754,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 139.49170790847685,
            "cvrmse_percent": 1690.5998239058092,
            "rms_normalized_rmse_percent": 45.42225798613234,
            "reference_energy": 0.06967505121994577,
            "candidate_energy": 0.16686597015275417,
            "relative_energy_error_percent": 139.49170790847685,
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
            "nmbe_percent": 72.61845852535906,
            "cvrmse_percent": 880.0733815296244,
            "rms_normalized_rmse_percent": 45.41311159175684,
            "reference_energy": 0.13381714824456026,
            "candidate_energy": 0.2309930985423545,
            "relative_energy_error_percent": 72.61845852535906,
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
      "bias_percent": 0.058733490244932116,
      "rms_normalized_error_percent": 0.1871673057432924,
      "absolute_error": {
        "p95": 0.05772450496351131,
        "p99": 0.10068124138622325,
        "maximum": 0.1212125104695625
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.0432872538974545,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.1871673057432924
    },
    "overcast": {
      "bias_percent": 0.03467680637159189,
      "rms_normalized_error_percent": 0.13224576314594366,
      "absolute_error": {
        "p95": 0.03356386423110962,
        "p99": 0.046921933889389145,
        "maximum": 0.05907595157623291
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.8640246391296387,
      "reference_fraction_of_uniform": 0.6393911838531494,
      "rms_normalized_to_uniform_percent": 0.09414792739225422
    },
    "horizon": {
      "bias_percent": 0.7436444380944405,
      "rms_normalized_error_percent": 1.7505508944539798,
      "absolute_error": {
        "p95": 0.03723756929925925,
        "p99": 0.071346895259612,
        "maximum": 0.08164043816127764
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.7221452617884775,
      "reference_fraction_of_uniform": 0.11949543873208235,
      "rms_normalized_to_uniform_percent": 0.11891105398029166
    },
    "north": {
      "bias_percent": -90.61795463752841,
      "rms_normalized_error_percent": 99.63107547015417,
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
      "rms_normalized_to_uniform_percent": 0.00018230443981471554
    },
    "east": {
      "bias_percent": 0.050223392677567126,
      "rms_normalized_error_percent": 0.19595038900788872,
      "absolute_error": {
        "p95": 0.010740214586257936,
        "p99": 0.02253204107284553,
        "maximum": 0.030875205993652344
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1377605199813843,
      "reference_fraction_of_uniform": 0.1882684826850891,
      "rms_normalized_to_uniform_percent": 0.03948126790719622
    },
    "south": {
      "bias_percent": 0.12487415113609822,
      "rms_normalized_error_percent": 0.24248915239514512,
      "absolute_error": {
        "p95": 0.0468327403068543,
        "p99": 0.09106731891632083,
        "maximum": 0.09505176544189453
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.201826095581055,
      "reference_fraction_of_uniform": 0.6952881813049316,
      "rms_normalized_to_uniform_percent": 0.15833687567398474
    },
    "west": {
      "bias_percent": -0.31689509872563704,
      "rms_normalized_error_percent": 0.4406595350072428,
      "absolute_error": {
        "p95": 0.026919972896575987,
        "p99": 0.055385438203811733,
        "maximum": 0.06503736972808838
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.172620177268982,
      "reference_fraction_of_uniform": 0.1940368115901947,
      "rms_normalized_to_uniform_percent": 0.0886705319214843
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
          "nmbe_percent": -0.014163983989360238,
          "cvrmse_percent": 1.8161502969777736,
          "absolute_error_percentiles_lux": {
            "p50": 2.036090850830078,
            "p90": 22.938339233398438,
            "p95": 36.86175842285155,
            "p99": 81.7086376953123
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
            "mean_absolute_error_percentage_points": 0.13011627932798378,
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
          "nmbe_percent": -0.44068975290352724,
          "cvrmse_percent": 14.390092091667798,
          "absolute_error_percentiles_lux": {
            "p50": 0.22334063053131104,
            "p90": 3.0257736206054693,
            "p95": 4.6795273780822715,
            "p99": 9.451233825683534
          },
          "maximum_absolute_error_lux": 52.467041015625,
          "worst": {
            "sensor_index": 2,
            "position": [
              6.5,
              3.5,
              0.75
            ],
            "hour_of_year": 1359.5,
            "foton_lux": 2364.78515625,
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
      "maximum_error_percentage_points": 0.004997190710611221,
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
            "maximum_error_percentage_points": 0.004835455907539199,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.004997190710611221,
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
      "study_preparation_seconds": 0.009129459038376808,
      "weather_seconds": 0.14285066700540483,
      "metric_reduction_seconds": 0.2469627090031281,
      "write_seconds": 0.06151279201731086,
      "total_seconds": 0.45149970799684525,
      "cold_end_to_end_seconds": 0.46062916703522205,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.03622304101008922,
      "engine_upload_seconds": 0.000827625,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.1914740416686982,
      "engine_annual_reduction_seconds": 0.0031595000764355063,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.1914740416686982
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.009129459038376808,
      "weather_seconds": 0.10199579200707376,
      "metric_reduction_seconds": 0.04662958299741149,
      "write_seconds": 0.04190029203891754,
      "total_seconds": 0.19069633295293897,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.19069633295293897,
      "raw_export_seconds": 0.02829162497073412,
      "engine_upload_seconds": 7.7125e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0031137500191107392,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.018863832927308977,
      "full": 0.18324862502049655
    }
  },
  "elapsed_seconds": 140.77942008303944,
  "result_class": "accuracy_failure"
}
```
