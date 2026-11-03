# Foton report

Status: **incomplete**

```json
{
  "scene": "three_room_chain",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "three_room_chain",
    "category": "connections",
    "question": "Can daylight cross two successive internal glass partitions?",
    "interactions": [
      "borrowed_light",
      "serial_glazing",
      "paired_apertures"
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
    "sensors": 72,
    "floor_area": 72.0,
    "aperture_area": 14.999999999999996
  },
  "sky_density": 2,
  "status": "incomplete",
  "passed": false,
  "model_sha256": "1f386a20b7715fdb91accadbfcdba08b12b4fbaea2a7977e1d377c39e473f97b",
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
      "scene_fingerprint": 1666965602579954223,
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
      "scene_fingerprint": 1666965602579954223,
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
  "oracle_stable": false,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "three_room_chain_0_grid",
        "bias_percent": -0.044526401972673935,
        "rms_normalized_error_percent": 0.7459935427594934,
        "absolute_error": {
          "p95": 1.227017492055893e-07,
          "p99": 9.124496136790706e-06,
          "maximum": 0.00014028436271473765
        },
        "worst_index": [
          11,
          543,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_1_grid",
        "bias_percent": 0.4912487188762551,
        "rms_normalized_error_percent": 1.4186753936033216,
        "absolute_error": {
          "p95": 0.0,
          "p99": 1.0549849847051522e-07,
          "maximum": 2.361941005801782e-05
        },
        "worst_index": [
          17,
          153,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_2_grid",
        "bias_percent": 0.394084978895435,
        "rms_normalized_error_percent": 2.744572946270209,
        "absolute_error": {
          "p95": 0.0,
          "p99": 0.0,
          "maximum": 9.880026482278481e-06
        },
        "worst_index": [
          11,
          89,
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
    "passed": false,
    "grids": [
      {
        "identifier": "three_room_chain_0_grid",
        "bias_percent": 0.07113714891369476,
        "rms_normalized_error_percent": 1.3686576770438919,
        "absolute_error": {
          "p95": 3.0061928555369377e-05,
          "p99": 9.485457558184862e-05,
          "maximum": 0.0003257002681493759
        },
        "worst_index": [
          7,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_1_grid",
        "bias_percent": 0.4707113612063034,
        "rms_normalized_error_percent": 4.2528868997017995,
        "absolute_error": {
          "p95": 2.704907728912076e-06,
          "p99": 9.789101386559081e-06,
          "maximum": 0.00019643595442175865
        },
        "worst_index": [
          15,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_2_grid",
        "bias_percent": 0.9905218477517755,
        "rms_normalized_error_percent": 10.436877998661757,
        "absolute_error": {
          "p95": 4.0034303694369555e-07,
          "p99": 1.5029307803615546e-06,
          "maximum": 6.135144212748855e-05
        },
        "worst_index": [
          10,
          90,
          0
        ],
        "passed": false
      }
    ]
  },
  "sample_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "three_room_chain_0_grid",
        "bias_percent": 0.037148061165379956,
        "rms_normalized_error_percent": 1.0237233726622506,
        "absolute_error": {
          "p95": 2.1642539650201797e-05,
          "p99": 6.917111459188139e-05,
          "maximum": 0.00038273632526397705
        },
        "worst_index": [
          2,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_1_grid",
        "bias_percent": 0.17683122679050253,
        "rms_normalized_error_percent": 2.732938162504046,
        "absolute_error": {
          "p95": 2.2276726667769253e-06,
          "p99": 6.7602198214444525e-06,
          "maximum": 0.00010540569201111794
        },
        "worst_index": [
          14,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_2_grid",
        "bias_percent": -0.467546433800442,
        "rms_normalized_error_percent": 7.869123619524697,
        "absolute_error": {
          "p95": 3.7126206819948493e-07,
          "p99": 1.2307464857030876e-06,
          "maximum": 4.7094348701648414e-05
        },
        "worst_index": [
          11,
          90,
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
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.09104959793677243,
                "cvrmse_percent": 41.45183032676885,
                "rms_normalized_rmse_percent": 9.339435726766316,
                "reference_energy": 5.710610691275178,
                "candidate_energy": 5.715810179349319,
                "relative_energy_error_percent": 0.09104959793677242,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 8.855619671521708e-05,
                  "p99": 0.0003177046397468074,
                  "maximum": 0.0007270736386999488
                },
                "worst": {
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "sky_patch_index": 206,
                  "rgb_channel": 0,
                  "reference": 0.0016335189575329423,
                  "candidate": 0.002360592596232891
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.34369234265270326,
                "cvrmse_percent": 173.4442250965871,
                "rms_normalized_rmse_percent": 6.6825684113132455,
                "reference_energy": 1.6961022795760776,
                "candidate_energy": 1.7019316532345385,
                "relative_energy_error_percent": 0.34369234265270326,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.290810455946485e-06,
                  "p95": 9.86602099146694e-05,
                  "p99": 0.0003751239855773735,
                  "maximum": 0.0010338305728510022
                },
                "worst": {
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "sky_patch_index": 360,
                  "rgb_channel": 0,
                  "reference": 0.0007180704269558191,
                  "candidate": -0.0003157601458951831
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "three_room_chain_1_grid",
            "start_sensor_index": 24,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.8829359785358533,
                "cvrmse_percent": 253.52676568867125,
                "rms_normalized_rmse_percent": 18.735552682963032,
                "reference_energy": 0.12407828394566423,
                "candidate_energy": 0.12298275213515808,
                "relative_energy_error_percent": 0.8829359785358534,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.0203621059185553e-07,
                  "maximum": 0.0002528754121158272
                },
                "worst": {
                  "global_sensor_index": 34,
                  "local_sensor_index": 10,
                  "sky_patch_index": 89,
                  "rgb_channel": 0,
                  "reference": 0.000617077894276008,
                  "candidate": 0.0008699533063918352
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 2.3186348088056516,
                "cvrmse_percent": 656.8425344298201,
                "rms_normalized_rmse_percent": 19.393628121824424,
                "reference_energy": 0.0845171827287885,
                "candidate_energy": 0.08647682754696007,
                "relative_energy_error_percent": 2.318634808805652,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.7490739739732807e-05,
                  "maximum": 0.0004965099506080151
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 15,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.003502174513414502,
                  "candidate": 0.003998684464022517
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "three_room_chain_2_grid",
            "start_sensor_index": 48,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 2.1212951331410133,
                "cvrmse_percent": 728.7660220072469,
                "rms_normalized_rmse_percent": 31.791151528500222,
                "reference_energy": 0.012163425859398558,
                "candidate_energy": 0.012421448020177195,
                "relative_energy_error_percent": 2.121295133141013,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.00010221535558230244
                },
                "worst": {
                  "global_sensor_index": 62,
                  "local_sensor_index": 14,
                  "sky_patch_index": 32,
                  "rgb_channel": 0,
                  "reference": 3.3969594369409606e-05,
                  "candidate": 0.00013618494995171204
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -1.630796165197568,
                "cvrmse_percent": 1124.3665964078234,
                "rms_normalized_rmse_percent": 35.16974867856757,
                "reference_energy": 0.0126793301171233,
                "candidate_energy": 0.012472556087800513,
                "relative_energy_error_percent": 1.6307961651975682,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.027269565971245e-07,
                  "maximum": 0.00013697435861104168
                },
                "worst": {
                  "global_sensor_index": 56,
                  "local_sensor_index": 8,
                  "sky_patch_index": 31,
                  "rgb_channel": 0,
                  "reference": 0.00010944965470116585,
                  "candidate": 0.00024642401331220753
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 157.52062504179776,
            "full": 397.2076670033857
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 143.92287493683398,
            "full": 403.8290000753477
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 146.6467500431463,
            "full": 403.3536670031026
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 145.2717089559883,
            "full": 406.4438339555636
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
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.029706626824659715,
                "cvrmse_percent": 20.291426158310703,
                "rms_normalized_rmse_percent": 4.590421389518317,
                "reference_energy": 5.708333473971152,
                "candidate_energy": 5.7100292272941715,
                "relative_energy_error_percent": 0.02970662682465972,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.394201096147299e-05,
                  "p99": 0.00014778976328670958,
                  "maximum": 0.0003730230964720249
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 413,
                  "rgb_channel": 0,
                  "reference": 0.0036038949619978666,
                  "candidate": 0.0039769180584698915
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.23674157067092919,
                "cvrmse_percent": 56.70376983199273,
                "rms_normalized_rmse_percent": 3.0162349294964064,
                "reference_energy": 3.028905826569904,
                "candidate_energy": 3.036076505797869,
                "relative_energy_error_percent": 0.2367415706709292,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.737818587978836e-08,
                  "p90": 1.6209844034165144e-05,
                  "p95": 6.121653132140636e-05,
                  "p99": 0.00021300563239492435,
                  "maximum": 0.0007045557722449303
                },
                "worst": {
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.02654669526964426,
                  "candidate": 0.02584213949739933
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "three_room_chain_1_grid",
            "start_sensor_index": 24,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.9256072412541556,
                "cvrmse_percent": 165.91943486459084,
                "rms_normalized_rmse_percent": 12.47299879834429,
                "reference_energy": 0.12335405356742513,
                "candidate_energy": 0.12449582761962574,
                "relative_energy_error_percent": 0.9256072412541556,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.12692485144233e-08,
                  "maximum": 0.00013832221156917512
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 14,
                  "sky_patch_index": 153,
                  "rgb_channel": 0,
                  "reference": 0.0004021264030598104,
                  "candidate": 0.0005404486146289855
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.043930876279188597,
                "cvrmse_percent": 169.478720233441,
                "rms_normalized_rmse_percent": 8.298203889590889,
                "reference_energy": 0.19991549098036643,
                "candidate_energy": 0.20000331560737195,
                "relative_energy_error_percent": 0.04393087627918858,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.516801203000796e-06,
                  "p95": 4.346649575381889e-06,
                  "p99": 1.933438957166758e-05,
                  "maximum": 0.00023170438362285495
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 14,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": -0.00017772192950360477,
                  "candidate": 5.398245411925018e-05
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "three_room_chain_2_grid",
            "start_sensor_index": 48,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 1.0487777089466461,
                "cvrmse_percent": 488.3192681848236,
                "rms_normalized_rmse_percent": 22.669045133266323,
                "reference_energy": 0.012145401938141731,
                "candidate_energy": 0.012272780206330935,
                "relative_energy_error_percent": 1.0487777089466461,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 7.59109971113503e-05
                },
                "worst": {
                  "global_sensor_index": 58,
                  "local_sensor_index": 10,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": 0.00012653280282393098,
                  "candidate": 0.00020244379993528128
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.23063113239032354,
                "cvrmse_percent": 336.9600175527734,
                "rms_normalized_rmse_percent": 17.39121275837733,
                "reference_energy": 0.026877467195767224,
                "candidate_energy": 0.02693945500271866,
                "relative_energy_error_percent": 0.23063113239032354,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.708901038455224e-07,
                  "p95": 4.848853905059514e-07,
                  "p99": 2.450834688261204e-06,
                  "maximum": 0.00011834818724310026
                },
                "worst": {
                  "global_sensor_index": 59,
                  "local_sensor_index": 11,
                  "sky_patch_index": 90,
                  "rgb_channel": 0,
                  "reference": -4.426884697750211e-05,
                  "candidate": 7.407934026559815e-05
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 208.22133298497647,
            "full": 5221.8245840631425
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 215.39079200010747,
            "full": 5145.6690420163795
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 208.30679195933044,
            "full": 5152.470499975607
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 209.05291696544737,
            "full": 5165.301333065145
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 12,
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
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.001166769907122096,
                "cvrmse_percent": 14.046080365791111,
                "rms_normalized_rmse_percent": 3.1781720001123084,
                "reference_energy": 5.711775788198565,
                "candidate_energy": 5.711842431479624,
                "relative_energy_error_percent": 0.0011667699071220958,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.178749466314912e-05,
                  "p99": 0.00010490279746591075,
                  "maximum": 0.0002511221682652831
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 519,
                  "rgb_channel": 0,
                  "reference": 0.004712891532108188,
                  "candidate": 0.004461769363842905
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.05258798450212768,
                "cvrmse_percent": 40.37977373583716,
                "rms_normalized_rmse_percent": 2.1506026399988705,
                "reference_energy": 3.035283900374175,
                "candidate_energy": 3.0368800950012993,
                "relative_energy_error_percent": 0.05258798450212768,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.5000000292152436e-08,
                  "p90": 1.1687810456351144e-05,
                  "p95": 4.525753320194781e-05,
                  "p99": 0.00015394307483802475,
                  "maximum": 0.00041168369352817535
                },
                "worst": {
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03222745098173618,
                  "candidate": 0.03263913467526436
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "three_room_chain_1_grid",
            "start_sensor_index": 24,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.5713570107290968,
                "cvrmse_percent": 125.05167341367768,
                "rms_normalized_rmse_percent": 9.355161732019603,
                "reference_energy": 0.12387668390340423,
                "candidate_energy": 0.1231689057852634,
                "relative_energy_error_percent": 0.5713570107290968,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.734498128935103e-06,
                  "maximum": 9.247876732842997e-05
                },
                "worst": {
                  "global_sensor_index": 34,
                  "local_sensor_index": 10,
                  "sky_patch_index": 90,
                  "rgb_channel": 0,
                  "reference": 0.0006901555461809039,
                  "candidate": 0.0005976767788524739
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.1671374561553351,
                "cvrmse_percent": 120.73590419482413,
                "rms_normalized_rmse_percent": 5.964235259945803,
                "reference_energy": 0.2020549628269901,
                "candidate_energy": 0.20171725330208545,
                "relative_energy_error_percent": 0.16713745615533507,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.8136479837949082e-06,
                  "p95": 3.089493134211807e-06,
                  "p99": 1.3236844426955463e-05,
                  "maximum": 0.0001832455163821578
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 14,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.002640845545101911,
                  "candidate": 0.002457600028719753
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "three_room_chain_2_grid",
            "start_sensor_index": 48,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -3.526692620090067,
                "cvrmse_percent": 400.4513008505064,
                "rms_normalized_rmse_percent": 18.457813423601703,
                "reference_energy": 0.012498343672177725,
                "candidate_energy": 0.01205756550825754,
                "relative_energy_error_percent": 3.5266926200900675,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 9.680882430984639e-05
                },
                "worst": {
                  "global_sensor_index": 59,
                  "local_sensor_index": 11,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": 0.00028225505229784176,
                  "candidate": 0.00018544622798799537
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 1.029530739233002,
                "cvrmse_percent": 243.88377617153049,
                "rms_normalized_rmse_percent": 12.331288293657659,
                "reference_energy": 0.027087627857349972,
                "candidate_energy": 0.02736650331267043,
                "relative_energy_error_percent": 1.029530739233002,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.6572857930441387e-07,
                  "p95": 4.287227568511298e-07,
                  "p99": 1.7774455836949613e-06,
                  "maximum": 8.615727347205393e-05
                },
                "worst": {
                  "global_sensor_index": 59,
                  "local_sensor_index": 11,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": -2.461212716298178e-05,
                  "candidate": 6.154514630907215e-05
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 224.323375034146,
            "full": 5463.056250009686
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 221.67933406308293,
            "full": 5477.32254199218
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 227.88462496828288,
            "full": 5478.223916958086
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 223.63616595976055,
            "full": 5460.74545790907
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 220.27220902964473,
            "full": 5640.082624973729
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 213.0695420783013,
            "full": 5598.6176249571145
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 218.967916094698,
            "full": 5647.065875004046
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 214.2182500101626,
            "full": 5416.512832976878
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
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.02884417154310827,
                "cvrmse_percent": 11.481667813930908,
                "rms_normalized_rmse_percent": 2.59857833315014,
                "reference_energy": 5.71291516993449,
                "candidate_energy": 5.711267326882762,
                "relative_energy_error_percent": 0.028844171543108265,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.4871376808732748e-05,
                  "p99": 8.589530771132482e-05,
                  "maximum": 0.00022152706515043974
                },
                "worst": {
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "sky_patch_index": 360,
                  "rgb_channel": 0,
                  "reference": 0.004040881525725126,
                  "candidate": 0.0038193544605746865
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.15688329428175654,
                "cvrmse_percent": 33.52062611904812,
                "rms_normalized_rmse_percent": 1.7849190560680614,
                "reference_energy": 3.0414352252121972,
                "candidate_energy": 3.0366637214374386,
                "relative_energy_error_percent": 0.15688329428175654,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.8042519417681433e-08,
                  "p90": 1.1615078619797714e-05,
                  "p95": 4.045170499011874e-05,
                  "p99": 0.00012486970808822645,
                  "maximum": 0.0004413006827235222
                },
                "worst": {
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.02747970074415207,
                  "candidate": 0.027038400061428547
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "three_room_chain_1_grid",
            "start_sensor_index": 24,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.29591695172779836,
                "cvrmse_percent": 88.24963740735157,
                "rms_normalized_rmse_percent": 6.635725583879719,
                "reference_energy": 0.12395085897230729,
                "candidate_energy": 0.12358406736879601,
                "relative_energy_error_percent": 0.2959169517277983,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 8.032605535388419e-07,
                  "maximum": 9.727460565045476e-05
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "sky_patch_index": 151,
                  "rgb_channel": 0,
                  "reference": 0.0009881769074127078,
                  "candidate": 0.0010854515130631626
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.6183293569734201,
                "cvrmse_percent": 110.32274296088025,
                "rms_normalized_rmse_percent": 5.477378268831588,
                "reference_energy": 0.2015936061591077,
                "candidate_energy": 0.20284011860777085,
                "relative_energy_error_percent": 0.6183293569734201,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.8388741125363595e-06,
                  "p95": 3.0989821198090794e-06,
                  "p99": 1.2154869727964672e-05,
                  "maximum": 0.00019071344286203384
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 15,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.005304313497617841,
                  "candidate": 0.005495026940479875
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "three_room_chain_2_grid",
            "start_sensor_index": 48,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -1.6455591712573636,
                "cvrmse_percent": 369.95324761492486,
                "rms_normalized_rmse_percent": 17.573901710294262,
                "reference_energy": 0.012309536473821936,
                "candidate_energy": 0.012106975767437689,
                "relative_energy_error_percent": 1.6455591712573638,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 5.482890992425382e-05
                },
                "worst": {
                  "global_sensor_index": 57,
                  "local_sensor_index": 9,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": 0.00012226960097905248,
                  "candidate": 6.744069105479866e-05
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.5309773865718065,
                "cvrmse_percent": 252.2541962016029,
                "rms_normalized_rmse_percent": 12.871406448780883,
                "reference_energy": 0.027040270603066574,
                "candidate_energy": 0.02718384832523668,
                "relative_energy_error_percent": 0.5309773865718064,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.7941874830285087e-07,
                  "p95": 4.7322834362262256e-07,
                  "p99": 1.7882467886920373e-06,
                  "maximum": 5.92933502048254e-05
                },
                "worst": {
                  "global_sensor_index": 58,
                  "local_sensor_index": 10,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": 4.519389767665416e-05,
                  "candidate": -1.4099452528171241e-05
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 336.15016599651426,
            "full": 9656.168583082035
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 343.8487909734249,
            "full": 9644.373791990802
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 342.6329590147361,
            "full": 9538.691791938618
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 339.43270810414106,
            "full": 9469.53724999912
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 10674.411082989536,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 43166.63079208229,
      "worker_pool_size": 12,
      "invocation_count": 5
    }
  ],
  "coefficients": {
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
        "identifier": "three_room_chain_0_grid",
        "full_identifier": "three_room_chain_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.24487704935656862,
            "cvrmse_percent": 3.41390094177442,
            "rms_normalized_rmse_percent": 0.7731959419938261,
            "reference_energy": 5.711497990101506,
            "candidate_energy": 5.697511842349286,
            "relative_energy_error_percent": 0.24487704935656862,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.2654421627521515e-07,
              "p99": 1.9674193936225476e-05,
              "maximum": 0.0001028992046485655
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 121,
              "rgb_channel": 0,
              "reference": 0.0001028992046485655,
              "candidate": 0.0,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.7269973995743786,
            "cvrmse_percent": 60.740515621180236,
            "rms_normalized_rmse_percent": 3.2354461488597397,
            "reference_energy": 3.0396427656798544,
            "candidate_energy": 3.017544641817011,
            "relative_energy_error_percent": 0.7269973995743787,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.000000058430487e-08,
              "p90": 3.9614747947780415e-05,
              "p95": 5.95140372752212e-05,
              "p99": 0.00011225944435864207,
              "maximum": 0.001699782907962799
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026420563459396362,
              "candidate": 0.024720780551433563,
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
            "nmbe_percent": -0.4123379182448278,
            "cvrmse_percent": 21.010417074463753,
            "rms_normalized_rmse_percent": 3.2220516517995805,
            "reference_energy": 8.75114075578136,
            "candidate_energy": 8.715056484166297,
            "relative_energy_error_percent": 0.41233791824482785,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 3.855035174638033e-05,
              "p95": 5.833024624735117e-05,
              "p99": 0.00011287698216619799,
              "maximum": 0.001699782907962799
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026420563459396362,
              "candidate": 0.024720780551433563,
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
        "identifier": "three_room_chain_1_grid",
        "full_identifier": "three_room_chain_1_grid",
        "start_sensor_index": 24,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -1.0916809914229009,
            "cvrmse_percent": 22.67896182894938,
            "rms_normalized_rmse_percent": 1.7142679834538577,
            "reference_energy": 0.12371634291717726,
            "candidate_energy": 0.12236575511826686,
            "relative_energy_error_percent": 1.0916809914229009,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.0021918569690686e-06,
              "maximum": 2.273775498906616e-05
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 8,
              "sky_patch_index": 61,
              "rgb_channel": 0,
              "reference": 2.273775498906616e-05,
              "candidate": 0.0,
              "position": [
                2.5,
                7.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.07067151108278781,
            "cvrmse_percent": 173.79616036649756,
            "rms_normalized_rmse_percent": 8.606881485446607,
            "reference_energy": 0.20226798362689635,
            "candidate_energy": 0.20241092946736217,
            "relative_energy_error_percent": 0.07067151108278781,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.996602001483552e-06,
              "p95": 1.0552845196798444e-05,
              "p99": 2.5943389300664332e-05,
              "maximum": 0.0003575584851205349
            },
            "worst": {
              "global_sensor_index": 24,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.001059401547536254,
              "candidate": 0.0014169600326567888,
              "position": [
                0.5,
                7.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.3704601295551269,
            "cvrmse_percent": 107.5282385818997,
            "rms_normalized_rmse_percent": 8.58218261831893,
            "reference_energy": 0.3259843265440736,
            "candidate_energy": 0.324776684585629,
            "relative_energy_error_percent": 0.3704601295551269,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.879592324869009e-06,
              "p95": 1.0255167012473976e-05,
              "p99": 2.6029204127553254e-05,
              "maximum": 0.0003575584851205349
            },
            "worst": {
              "global_sensor_index": 24,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.001059401547536254,
              "candidate": 0.0014169600326567888,
              "position": [
                0.5,
                7.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "three_room_chain_2_grid",
        "full_identifier": "three_room_chain_2_grid",
        "start_sensor_index": 48,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.20127926128027132,
            "cvrmse_percent": 32.41449736935534,
            "rms_normalized_rmse_percent": 1.5354751659535568,
            "reference_energy": 0.012260490989135064,
            "candidate_energy": 0.012235813163442799,
            "relative_energy_error_percent": 0.20127926128027132,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 6.955624485271983e-06
            },
            "worst": {
              "global_sensor_index": 53,
              "local_sensor_index": 5,
              "sky_patch_index": 89,
              "rgb_channel": 0,
              "reference": 2.667167609615717e-05,
              "candidate": 3.3627300581429154e-05,
              "position": [
                1.5,
                10.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 5.916982450132822,
            "cvrmse_percent": 526.6028381596493,
            "rms_normalized_rmse_percent": 26.981445612792392,
            "reference_energy": 0.02705982469956858,
            "candidate_energy": 0.02866094977807876,
            "relative_energy_error_percent": 5.916982450132822,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.9291259434339736e-07,
              "p95": 5.551461867980834e-07,
              "p99": 6.369000395523014e-06,
              "maximum": 0.00015866101603023708
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00027885899180546403,
              "candidate": 0.0004375200078357011,
              "position": [
                2.5,
                10.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 4.009243631965072,
            "cvrmse_percent": 362.67739030596044,
            "rms_normalized_rmse_percent": 27.001912051518193,
            "reference_energy": 0.039320315688703644,
            "candidate_energy": 0.04089676294152156,
            "relative_energy_error_percent": 4.009243631965072,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.923228580835712e-07,
              "p95": 5.52481253635051e-07,
              "p99": 6.3800084674880776e-06,
              "maximum": 0.00015866101603023708
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00027885899180546403,
              "candidate": 0.0004375200078357011,
              "position": [
                2.5,
                10.5,
                0.75
              ]
            },
            "passed": false
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
        "identifier": "three_room_chain_0_grid",
        "full_identifier": "three_room_chain_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.24487704935656862,
            "cvrmse_percent": 3.41390094177442,
            "rms_normalized_rmse_percent": 0.7731959419938261,
            "reference_energy": 5.711497990101506,
            "candidate_energy": 5.697511842349286,
            "relative_energy_error_percent": 0.24487704935656862,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.2654421627521515e-07,
              "p99": 1.9674193936225476e-05,
              "maximum": 0.0001028992046485655
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 121,
              "rgb_channel": 0,
              "reference": 0.0001028992046485655,
              "candidate": 0.0,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 77.42649888635768,
            "cvrmse_percent": 859.9413891667716,
            "rms_normalized_rmse_percent": 33.194766595087714,
            "reference_energy": 1.70072940668787,
            "candidate_energy": 3.017544641817011,
            "relative_energy_error_percent": 77.42649888635768,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.234414260892663e-05,
              "p95": 0.00010970999574055895,
              "p99": 0.000204931027838028,
              "maximum": 0.010410412214696407
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014649626798927784,
              "candidate": 0.02506003901362419,
              "position": [
                5.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 17.576755509973214,
            "cvrmse_percent": 197.29721798253672,
            "rms_normalized_rmse_percent": 33.19213911393813,
            "reference_energy": 7.412227396789376,
            "candidate_energy": 8.715056484166297,
            "relative_energy_error_percent": 17.576755509973214,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.2072958573699e-05,
              "p95": 0.00010979815851897001,
              "p99": 0.00020505867942119903,
              "maximum": 0.010410412214696407
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014649626798927784,
              "candidate": 0.02506003901362419,
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
        "identifier": "three_room_chain_1_grid",
        "full_identifier": "three_room_chain_1_grid",
        "start_sensor_index": 24,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -1.0916809914229009,
            "cvrmse_percent": 22.67896182894938,
            "rms_normalized_rmse_percent": 1.7142679834538577,
            "reference_energy": 0.12371634291717726,
            "candidate_energy": 0.12236575511826686,
            "relative_energy_error_percent": 1.0916809914229009,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.0021918569690686e-06,
              "maximum": 2.273775498906616e-05
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 8,
              "sky_patch_index": 61,
              "rgb_channel": 0,
              "reference": 2.273775498906616e-05,
              "candidate": 0.0,
              "position": [
                2.5,
                7.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 137.2619016953106,
            "cvrmse_percent": 1675.7413356884178,
            "rms_normalized_rmse_percent": 49.27208891297098,
            "reference_energy": 0.08531118060719933,
            "candidate_energy": 0.20241092946736217,
            "relative_energy_error_percent": 137.2619016953106,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.11000007968687e-06,
              "p95": 1.2429999515006784e-05,
              "p99": 3.929959384549841e-05,
              "maximum": 0.001651170663535595
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0037504294887185097,
              "candidate": 0.005401600152254105,
              "position": [
                3.5,
                4.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 55.375081285768516,
            "cvrmse_percent": 683.7853243867468,
            "rms_normalized_rmse_percent": 49.261915043423244,
            "reference_energy": 0.2090275235243766,
            "candidate_energy": 0.324776684585629,
            "relative_energy_error_percent": 55.375081285768516,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.739999899858958e-06,
              "p95": 1.2114124729123432e-05,
              "p99": 3.906550027750195e-05,
              "maximum": 0.001651170663535595
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0037504294887185097,
              "candidate": 0.005401600152254105,
              "position": [
                3.5,
                4.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "three_room_chain_2_grid",
        "full_identifier": "three_room_chain_2_grid",
        "start_sensor_index": 48,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.20127926128027132,
            "cvrmse_percent": 32.41449736935534,
            "rms_normalized_rmse_percent": 1.5354751659535568,
            "reference_energy": 0.012260490989135064,
            "candidate_energy": 0.012235813163442799,
            "relative_energy_error_percent": 0.20127926128027132,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 6.955624485271983e-06
            },
            "worst": {
              "global_sensor_index": 53,
              "local_sensor_index": 5,
              "sky_patch_index": 89,
              "rgb_channel": 0,
              "reference": 2.667167609615717e-05,
              "candidate": 3.3627300581429154e-05,
              "position": [
                1.5,
                10.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 127.3255200665548,
            "cvrmse_percent": 2098.5215444561723,
            "rms_normalized_rmse_percent": 65.8019432797175,
            "reference_energy": 0.012607889237287395,
            "candidate_energy": 0.02866094977807876,
            "relative_energy_error_percent": 127.32552006655479,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 8.473700154354385e-06,
              "maximum": 0.0003009135980391875
            },
            "worst": {
              "global_sensor_index": 63,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00011859640653710812,
              "candidate": 0.0004195100045762956,
              "position": [
                3.5,
                8.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 64.45286170294705,
            "cvrmse_percent": 1063.694609256832,
            "rms_normalized_rmse_percent": 65.78810238365934,
            "reference_energy": 0.02486838022642246,
            "candidate_energy": 0.04089676294152156,
            "relative_energy_error_percent": 64.45286170294705,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 8.484154068355557e-06,
              "maximum": 0.0003009135980391875
            },
            "worst": {
              "global_sensor_index": 63,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00011859640653710812,
              "candidate": 0.0004195100045762956,
              "position": [
                3.5,
                8.5,
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
      "bias_percent": -0.011855796482395998,
      "rms_normalized_error_percent": 0.32112697208710067,
      "absolute_error": {
        "p95": 0.11002233655948244,
        "p99": 0.15049842999487922,
        "maximum": 0.1715518025969205
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 5.706988312908392,
      "rms_normalized_to_uniform_percent": 0.32112697208710067
    },
    "overcast": {
      "bias_percent": -0.04766707926702871,
      "rms_normalized_error_percent": 0.25207713468374443,
      "absolute_error": {
        "p95": 0.06776129007339478,
        "p99": 0.0850384902954102,
        "maximum": 0.09120559692382812
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.691338062286377,
      "rms_normalized_to_uniform_percent": 0.17923325090978504
    },
    "horizon": {
      "bias_percent": 0.999699162650554,
      "rms_normalized_error_percent": 3.6092315696369606,
      "absolute_error": {
        "p95": 0.0803278869589652,
        "p99": 0.12116250989746584,
        "maximum": 0.1795887672630192
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.6126741159139479,
      "rms_normalized_to_uniform_percent": 0.23790350304096236
    },
    "north": {
      "bias_percent": -91.53487507395576,
      "rms_normalized_error_percent": 101.40307004621165,
      "absolute_error": {
        "p95": 3.208322577847867e-05,
        "p99": 0.00012861812108894846,
        "maximum": 0.0001688417250989005
      },
      "worst_index": [
        69
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 6.507285888801562e-06,
      "rms_normalized_to_uniform_percent": 0.00016567250373468993
    },
    "east": {
      "bias_percent": -0.026636839673970278,
      "rms_normalized_error_percent": 0.5967712587796359,
      "absolute_error": {
        "p95": 0.041128711402416245,
        "p99": 0.06605377674102796,
        "maximum": 0.08013391494750977
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.0875475406646729,
      "rms_normalized_to_uniform_percent": 0.12050771220843161
    },
    "south": {
      "bias_percent": -0.04908251444415464,
      "rms_normalized_error_percent": 0.38898732550362003,
      "absolute_error": {
        "p95": 0.08061966300010685,
        "p99": 0.12024163722991944,
        "maximum": 0.12170791625976562
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.9259703159332275,
      "rms_normalized_to_uniform_percent": 0.25385404829583114
    },
    "west": {
      "bias_percent": 0.39162267240179843,
      "rms_normalized_error_percent": 0.7414935131381025,
      "absolute_error": {
        "p95": 0.05134499073028565,
        "p99": 0.07464484542608302,
        "maximum": 0.12147307395935059
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.099263072013855,
      "rms_normalized_to_uniform_percent": 0.15082982665507413
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
        "identifier": "three_room_chain_0_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": -0.23251673453556332,
          "cvrmse_percent": 3.8085471318086723,
          "absolute_error_percentiles_lux": {
            "p50": 7.154319763183594,
            "p90": 87.85522460937501,
            "p95": 127.99988098144529,
            "p99": 220.66130859374982
          },
          "maximum_absolute_error_lux": 721.1181640625,
          "worst": {
            "sensor_index": 10,
            "position": [
              2.5,
              1.5,
              0.75
            ],
            "hour_of_year": 2868.5,
            "foton_lux": 12470.9365234375,
            "radiance_lux": 13192.0546875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.5423801369863019,
            "maximum_error_percentage_points": 2.3030136986301315,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.163145482413122,
            "maximum_error_percentage_points": 0.4786639324607762,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.13245433789954375,
            "maximum_error_percentage_points": 0.4686301369863024,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.16474315068493053,
            "maximum_error_percentage_points": 0.49684931506848784,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0746746575342464,
            "maximum_error_percentage_points": 0.24671232876712423,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 91.66666666666667,
          "radiance_percent": 91.66666666666667,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 4.166666666666667,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "three_room_chain_1_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": -0.9497140251068532,
          "cvrmse_percent": 29.859796440509367,
          "absolute_error_percentiles_lux": {
            "p50": 1.086761474609375,
            "p90": 14.547315406799319,
            "p95": 23.83840579986571,
            "p99": 49.62426521301266
          },
          "maximum_absolute_error_lux": 269.048828125,
          "worst": {
            "sensor_index": 15,
            "position": [
              3.5,
              4.5,
              0.75
            ],
            "hour_of_year": 828.5,
            "foton_lux": 5010.908203125,
            "radiance_lux": 4741.859375
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.07501141552511416,
            "maximum_error_percentage_points": 0.4078082191780821,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.47593967228337597,
            "maximum_error_percentage_points": 1.43369269607269,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.9656050228310497,
            "maximum_error_percentage_points": 3.972602739726028,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.9654052511415525,
            "maximum_error_percentage_points": 3.972602739726028,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.00021689497716894981,
            "maximum_error_percentage_points": 0.003972602739725994,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 0.0,
          "radiance_percent": 0.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 4.166666666666667,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "three_room_chain_2_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": 2.920583357741127,
          "cvrmse_percent": 60.376330240081835,
          "absolute_error_percentiles_lux": {
            "p50": 0.16170798242092133,
            "p90": 1.181736946105958,
            "p95": 2.3065818786621044,
            "p99": 9.411345739364608
          },
          "maximum_absolute_error_lux": 94.76789093017578,
          "worst": {
            "sensor_index": 8,
            "position": [
              2.5,
              11.5,
              0.75
            ],
            "hour_of_year": 8604.5,
            "foton_lux": 177.2674560546875,
            "radiance_lux": 82.49956512451172
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.005776255707762558,
            "maximum_error_percentage_points": 0.08136986301369861,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.13185302280639602,
            "maximum_error_percentage_points": 0.3962400423847612,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.042060502283105095,
            "maximum_error_percentage_points": 0.32684931506848613,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.04206050228310501,
            "maximum_error_percentage_points": 0.32684931506849313,
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
    "numerical_correctness": "incomplete",
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
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.0026027397260273977,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004770173373287889,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.0048172624143845155,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.004768486545510431,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.00479452054794538,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.0046575342465753344,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004520547945205511,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.003972602739725994,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
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
      "study_preparation_seconds": 0.013404040946625173,
      "weather_seconds": 0.12307045806664973,
      "metric_reduction_seconds": 0.08543874998576939,
      "write_seconds": 0.05212641693651676,
      "total_seconds": 0.260878250002861,
      "cold_end_to_end_seconds": 0.2742822909494862,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.027009792043827474,
      "engine_upload_seconds": 0.000890334,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.030188083415850997,
      "engine_annual_reduction_seconds": 0.003080083290114999,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.030188083415850997
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.013404040946625173,
      "weather_seconds": 0.11643162497784942,
      "metric_reduction_seconds": 0.04919904097914696,
      "write_seconds": 0.03399550006724894,
      "total_seconds": 0.19981141691096127,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.19981141691096127,
      "raw_export_seconds": 0.020093667088076472,
      "engine_upload_seconds": 9.0833e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00311999989207834,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.017107749939896166,
      "full": 0.02194495894946158
    }
  },
  "elapsed_seconds": 166.6445602090098,
  "result_class": "unstable_reference"
}
```
