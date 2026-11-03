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
  "sky_density": 1,
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 1666965602579954223,
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
        "bias_percent": -0.019309767029715968,
        "rms_normalized_error_percent": 0.5180704767451556,
        "absolute_error": {
          "p95": 4.789326339960098e-06,
          "p99": 4.62816096842289e-05,
          "maximum": 0.00023132911883294582
        },
        "worst_index": [
          6,
          96,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_1_grid",
        "bias_percent": 0.2410539148223052,
        "rms_normalized_error_percent": 1.6529468790683417,
        "absolute_error": {
          "p95": 0.0,
          "p99": 5.269888788461685e-06,
          "maximum": 4.955328768119216e-05
        },
        "worst_index": [
          13,
          17,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_2_grid",
        "bias_percent": -0.9189057661873233,
        "rms_normalized_error_percent": 2.1773595316798224,
        "absolute_error": {
          "p95": 0.0,
          "p99": 0.0,
          "maximum": 1.2653428711928427e-05
        },
        "worst_index": [
          4,
          15,
          0
        ],
        "passed": true
      }
    ],
    "samples_per_patch": [
      1024,
      4096
    ]
  },
  "depth_stability": {
    "passed": false,
    "grids": [
      {
        "identifier": "three_room_chain_0_grid",
        "bias_percent": 0.012871286601459699,
        "rms_normalized_error_percent": 1.013925888921719,
        "absolute_error": {
          "p95": 5.681253969669342e-05,
          "p99": 0.00017021503299474716,
          "maximum": 0.0005148556083440781
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
        "bias_percent": 0.2923023458923444,
        "rms_normalized_error_percent": 2.6754788814437065,
        "absolute_error": {
          "p95": 6.788184691686183e-06,
          "p99": 2.9057355277473107e-05,
          "maximum": 9.76421870291233e-05
        },
        "worst_index": [
          18,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_2_grid",
        "bias_percent": 0.49780547628109373,
        "rms_normalized_error_percent": 6.270957486602985,
        "absolute_error": {
          "p95": 1.1954925867030397e-06,
          "p99": 5.750427590101026e-06,
          "maximum": 5.872017936781049e-05
        },
        "worst_index": [
          15,
          17,
          0
        ],
        "passed": false
      }
    ]
  },
  "sample_stability": {
    "passed": false,
    "grids": [
      {
        "identifier": "three_room_chain_0_grid",
        "bias_percent": 0.046936708853996575,
        "rms_normalized_error_percent": 0.8806944707077761,
        "absolute_error": {
          "p95": 5.075428634881973e-05,
          "p99": 0.00015072710812091827,
          "maximum": 0.0004372112452983856
        },
        "worst_index": [
          20,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_1_grid",
        "bias_percent": 0.15428516022592859,
        "rms_normalized_error_percent": 2.52444480145793,
        "absolute_error": {
          "p95": 5.998041160637513e-06,
          "p99": 2.435653004795313e-05,
          "maximum": 8.763594087213278e-05
        },
        "worst_index": [
          7,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_2_grid",
        "bias_percent": 0.027545130634762143,
        "rms_normalized_error_percent": 6.967990712022662,
        "absolute_error": {
          "p95": 9.821187632041983e-07,
          "p99": 5.623514880426228e-06,
          "maximum": 7.48581369407475e-05
        },
        "worst_index": [
          11,
          16,
          0
        ],
        "passed": false
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.09000032795926155,
                "cvrmse_percent": 9.718553866989044,
                "rms_normalized_rmse_percent": 2.326836676309662,
                "reference_energy": 5.711960702889655,
                "candidate_energy": 5.71710148625516,
                "relative_energy_error_percent": 0.09000032795926155,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.2444874048233032e-07,
                  "p95": 9.141850750893354e-05,
                  "p99": 0.00026221468579024076,
                  "maximum": 0.000643567880615592
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 71,
                  "rgb_channel": 0,
                  "reference": 0.012812417466193438,
                  "candidate": 0.01345598534680903
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.9329178604322654,
                "cvrmse_percent": 47.07822440985218,
                "rms_normalized_rmse_percent": 2.6601385421654924,
                "reference_energy": 1.706819042171329,
                "candidate_energy": 1.6908958224816537,
                "relative_energy_error_percent": 0.9329178604322655,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.24370339512825e-05,
                  "p95": 0.00015553284902125597,
                  "p99": 0.00038917246274650097,
                  "maximum": 0.0010474827140569687
                },
                "worst": {
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.017376319505274296,
                  "candidate": 0.018423802219331264
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
                "nmbe_percent": -0.3917323843571053,
                "cvrmse_percent": 77.37008513686432,
                "rms_normalized_rmse_percent": 7.326985150140042,
                "reference_energy": 0.12390734325634867,
                "candidate_energy": 0.12342195806621703,
                "relative_energy_error_percent": 0.3917323843571053,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.7722324375645258e-05,
                  "maximum": 0.0002499332476872951
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 15,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 0.0011068637249991298,
                  "candidate": 0.0013567969726864249
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -1.3818176026773128,
                "cvrmse_percent": 148.36746015661225,
                "rms_normalized_rmse_percent": 7.031471816682178,
                "reference_energy": 0.08642277415668964,
                "candidate_energy": 0.08522856905067044,
                "relative_energy_error_percent": 1.381817602677313,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.7667030451917753e-06,
                  "p99": 5.840887752128765e-05,
                  "maximum": 0.0002092983922921121
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.003751989221200347,
                  "candidate": 0.003542690828908235
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
                "nmbe_percent": -3.6757008983072077,
                "cvrmse_percent": 221.4089783649303,
                "rms_normalized_rmse_percent": 14.12383902667537,
                "reference_energy": 0.012449657506294898,
                "candidate_energy": 0.011992045333499846,
                "relative_energy_error_percent": 3.675700898307207,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 7.614669812028296e-05
                },
                "worst": {
                  "global_sensor_index": 59,
                  "local_sensor_index": 11,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 0.0003475465018709656,
                  "candidate": 0.00042369319999124855
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 7.7461820306509495,
                "cvrmse_percent": 310.0782056932157,
                "rms_normalized_rmse_percent": 13.551095496786346,
                "reference_energy": 0.011707980457259737,
                "candidate_energy": 0.012614901935592115,
                "relative_energy_error_percent": 7.74618203065095,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 8.573358627472771e-06,
                  "maximum": 0.00010022866626968607
                },
                "worst": {
                  "global_sensor_index": 61,
                  "local_sensor_index": 13,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 1.0648051102180034e-05,
                  "candidate": 0.00011087671737186611
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 169.22224999871105,
            "full": 408.13079103827477
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 140.04366705194116,
            "full": 400.18958400469273
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 147.5202499423176,
            "full": 418.5321250697598
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 146.59958390984684,
            "full": 398.11066701076925
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 147.11545803584158,
            "full": 389.44729091599584
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 149.05629202257842,
            "full": 399.72799993120134
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 144.57820798270404,
            "full": 387.31170794926584
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 144.14925000164658,
            "full": 399.9253750080243
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.09707445997668997,
                "cvrmse_percent": 6.7177713803197605,
                "rms_normalized_rmse_percent": 1.6073526853353852,
                "reference_energy": 5.708744817481488,
                "candidate_energy": 5.7142865506845055,
                "relative_energy_error_percent": 0.09707445997668995,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.7945421859622002e-07,
                  "p95": 6.412388756871223e-05,
                  "p99": 0.00019566528499126434,
                  "maximum": 0.000434190034866333
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 73,
                  "rgb_channel": 0,
                  "reference": 0.013521370012313128,
                  "candidate": 0.01395556004717946
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.043849463887642486,
                "cvrmse_percent": 21.377452594749855,
                "rms_normalized_rmse_percent": 1.8277893041525637,
                "reference_energy": 3.0310678300352905,
                "candidate_energy": 3.0323969370288317,
                "relative_energy_error_percent": 0.04384946388764249,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.44330919940694e-07,
                  "p90": 3.652973100543022e-05,
                  "p95": 0.00010933168232440948,
                  "p99": 0.00029928795993328094,
                  "maximum": 0.0008101901039481163
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.029924155212938786,
                  "candidate": 0.030734345316886902
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
                "nmbe_percent": 0.168217415187321,
                "cvrmse_percent": 51.20216329061721,
                "rms_normalized_rmse_percent": 4.85506927420317,
                "reference_energy": 0.12412345277220993,
                "candidate_energy": 0.1243322500361046,
                "relative_energy_error_percent": 0.168217415187321,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.3922021025791764e-05,
                  "maximum": 0.0001391071709804237
                },
                "worst": {
                  "global_sensor_index": 34,
                  "local_sensor_index": 10,
                  "sky_patch_index": 45,
                  "rgb_channel": 0,
                  "reference": 0.0007220451661851257,
                  "candidate": 0.0008611523371655494
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.8030963512842684,
                "cvrmse_percent": 65.19069698120798,
                "rms_normalized_rmse_percent": 5.640287269160731,
                "reference_energy": 0.20143972235894125,
                "candidate_energy": 0.19982196729863944,
                "relative_energy_error_percent": 0.8030963512842683,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.781109387228753e-08,
                  "p90": 5.666604010912124e-06,
                  "p95": 9.752571486387751e-06,
                  "p99": 5.2410352509468794e-05,
                  "maximum": 0.00025722896680235863
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 14,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.002675344469025731,
                  "candidate": 0.0024181155022233725
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
                "nmbe_percent": -1.3462462489683986,
                "cvrmse_percent": 228.79423432589556,
                "rms_normalized_rmse_percent": 14.200604573778437,
                "reference_energy": 0.0119743346094765,
                "candidate_energy": 0.011813130578957498,
                "relative_energy_error_percent": 1.3462462489683986,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.00010117450437974185
                },
                "worst": {
                  "global_sensor_index": 59,
                  "local_sensor_index": 11,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 0.000429724357672967,
                  "candidate": 0.00032854985329322517
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 2.80032446664634,
                "cvrmse_percent": 196.2411067420455,
                "rms_normalized_rmse_percent": 15.854559231954589,
                "reference_energy": 0.02693929322978761,
                "candidate_energy": 0.027693680849242952,
                "relative_energy_error_percent": 2.8003244666463396,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.634014511064379e-07,
                  "p95": 1.703265873231885e-06,
                  "p99": 7.800350431352854e-06,
                  "maximum": 0.00018142123008146882
                },
                "worst": {
                  "global_sensor_index": 63,
                  "local_sensor_index": 15,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": -8.545699529349804e-06,
                  "candidate": 0.00017287553055211902
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 204.78199992794544,
            "full": 5209.113667020574
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 208.51404103450477,
            "full": 5187.604582984932
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 206.46312495227903,
            "full": 5183.270707959309
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 210.88499994948506,
            "full": 5193.081084056757
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.11806810906744389,
                "cvrmse_percent": 6.568621268243933,
                "rms_normalized_rmse_percent": 1.5726946999511489,
                "reference_energy": 5.714297183837402,
                "candidate_energy": 5.707550421205951,
                "relative_energy_error_percent": 0.1180681090674439,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.341119736433029e-08,
                  "p95": 6.80114608258009e-05,
                  "p99": 0.00019554852042347193,
                  "maximum": 0.00037279375828802586
                },
                "worst": {
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "sky_patch_index": 44,
                  "rgb_channel": 0,
                  "reference": 0.007383544696494937,
                  "candidate": 0.007756338454782963
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.20113442464098813,
                "cvrmse_percent": 21.560058906854298,
                "rms_normalized_rmse_percent": 1.8414194747972221,
                "reference_energy": 3.030402060734513,
                "candidate_energy": 3.03649724248368,
                "relative_energy_error_percent": 0.20113442464098816,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.596758719164427e-07,
                  "p90": 3.8383797800634056e-05,
                  "p95": 0.00010162591934204102,
                  "p99": 0.0003038207069039345,
                  "maximum": 0.0010564643889665604
                },
                "worst": {
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.030276404693722725,
                  "candidate": 0.031332869082689285
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
                "nmbe_percent": -1.0133516739578894,
                "cvrmse_percent": 61.11360626424277,
                "rms_normalized_rmse_percent": 5.780496748841364,
                "reference_energy": 0.12435797786565672,
                "candidate_energy": 0.12309779421525491,
                "relative_energy_error_percent": 1.0133516739578892,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.395901563228108e-05,
                  "maximum": 0.00015284749679267406
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "sky_patch_index": 15,
                  "rgb_channel": 0,
                  "reference": 0.0013156619970686734,
                  "candidate": 0.0011628145002759993
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -1.0850613953435235,
                "cvrmse_percent": 71.64223358132925,
                "rms_normalized_rmse_percent": 6.134894157200801,
                "reference_energy": 0.20318271103530705,
                "candidate_energy": 0.20097805387585055,
                "relative_energy_error_percent": 1.0850613953435237,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.496871947561431e-08,
                  "p90": 5.518910711543867e-06,
                  "p95": 9.490965112490812e-06,
                  "p99": 5.2671915909741074e-05,
                  "maximum": 0.0003777176607400179
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0054914518259465694,
                  "candidate": 0.0051137341652065516
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
                "nmbe_percent": -0.6155824817855802,
                "cvrmse_percent": 166.25439528166575,
                "rms_normalized_rmse_percent": 10.457327579284179,
                "reference_energy": 0.012346268553301343,
                "candidate_energy": 0.012270267086933018,
                "relative_energy_error_percent": 0.6155824817855802,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 5.8600769989425316e-05
                },
                "worst": {
                  "global_sensor_index": 59,
                  "local_sensor_index": 11,
                  "sky_patch_index": 15,
                  "rgb_channel": 0,
                  "reference": 0.0001257970325241331,
                  "candidate": 0.00018439780251355842
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 2.1562744183552867,
                "cvrmse_percent": 123.68514405204144,
                "rms_normalized_rmse_percent": 9.753801394326507,
                "reference_energy": 0.026808114297836028,
                "candidate_energy": 0.027386170808483712,
                "relative_energy_error_percent": 2.1562744183552867,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 7.462901301380498e-07,
                  "p95": 1.6256091868172007e-06,
                  "p99": 9.103414413402788e-06,
                  "maximum": 8.403745596297085e-05
                },
                "worst": {
                  "global_sensor_index": 60,
                  "local_sensor_index": 12,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 0.00031190263689495623,
                  "candidate": 0.0003959400928579271
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 210.04325000103563,
            "full": 5482.151082949713
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 213.69158301968127,
            "full": 5479.565000045113
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 208.24129204265773,
            "full": 5469.718290958554
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 203.46087496727705,
            "full": 5520.543082966469
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.029363874828390906,
                "cvrmse_percent": 3.782932597207329,
                "rms_normalized_rmse_percent": 0.905074671892708,
                "reference_energy": 5.712624167377271,
                "candidate_energy": 5.710946719567346,
                "relative_energy_error_percent": 0.029363874828390906,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.4848850443959236e-07,
                  "p95": 3.5340432077646255e-05,
                  "p99": 0.00010718137491494417,
                  "maximum": 0.00026274751871824265
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 44,
                  "rgb_channel": 0,
                  "reference": 0.007569165900349617,
                  "candidate": 0.007306418381631374
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.1351310698095986,
                "cvrmse_percent": 13.026175817520825,
                "rms_normalized_rmse_percent": 1.1144701457514368,
                "reference_energy": 3.0346419799053628,
                "candidate_energy": 3.0387427240777,
                "relative_energy_error_percent": 0.1351310698095986,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.0467136607749126e-07,
                  "p90": 2.4483852030243725e-05,
                  "p95": 5.940953269600868e-05,
                  "p99": 0.0001722150482237339,
                  "maximum": 0.0007785540074110031
                },
                "worst": {
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03426794521510601,
                  "candidate": 0.035046499222517014
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
                "nmbe_percent": 0.14520479493001034,
                "cvrmse_percent": 41.80354969745332,
                "rms_normalized_rmse_percent": 3.97253779932426,
                "reference_energy": 0.12324158730439194,
                "candidate_energy": 0.12342053999850577,
                "relative_energy_error_percent": 0.14520479493001034,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.3736047549173236e-05,
                  "maximum": 0.00011852406896650791
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 15,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 0.0012929420336149633,
                  "candidate": 0.0011744179646484554
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.3129253920520186,
                "cvrmse_percent": 38.78825551134312,
                "rms_normalized_rmse_percent": 3.351002223440441,
                "reference_energy": 0.2026627859462664,
                "candidate_energy": 0.2032969692637323,
                "relative_energy_error_percent": 0.3129253920520185,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.133202852723116e-08,
                  "p90": 3.889241042998037e-06,
                  "p95": 6.893820682307705e-06,
                  "p99": 3.055657725781202e-05,
                  "maximum": 0.0001514334580861032
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 0.00018220097990706563,
                  "candidate": 3.076752182096243e-05
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
                "nmbe_percent": 2.0008443230213584,
                "cvrmse_percent": 102.26901238196577,
                "rms_normalized_rmse_percent": 6.5442576397820575,
                "reference_energy": 0.012056778848091199,
                "candidate_energy": 0.012298016223212471,
                "relative_energy_error_percent": 2.000844323021358,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 3.796513919951394e-05
                },
                "worst": {
                  "global_sensor_index": 60,
                  "local_sensor_index": 12,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 0.0002455714493407868,
                  "candidate": 0.0002835365885403007
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.8119576521688368,
                "cvrmse_percent": 70.6104124810744,
                "rms_normalized_rmse_percent": 5.663045230030414,
                "reference_energy": 0.02734990185266639,
                "candidate_energy": 0.027127832231713,
                "relative_energy_error_percent": 0.8119576521688368,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.93304640972292e-07,
                  "p95": 1.0851481846430033e-06,
                  "p99": 5.906098522245884e-06,
                  "maximum": 4.542146052699536e-05
                },
                "worst": {
                  "global_sensor_index": 61,
                  "local_sensor_index": 13,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 8.792623702902347e-05,
                  "candidate": 0.00013334769755601883
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 330.33133298158646,
            "full": 9467.66420896165
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 320.9412500727922,
            "full": 9449.105832958594
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 337.0532920816913,
            "full": 9496.296832920052
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 320.8649168955162,
            "full": 9509.51433298178
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 2769.863290945068,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 10918.629291001707,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/direct_4096/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/three_room_chain/mf1/direct_4096/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 4096,
      "elapsed_ms": 44122.68149992451,
      "worker_pool_size": 12,
      "invocation_count": 5
    }
  ],
  "coefficients": {
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
        "identifier": "three_room_chain_0_grid",
        "full_identifier": "three_room_chain_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.263418627379176,
            "cvrmse_percent": 3.168318188133712,
            "rms_normalized_rmse_percent": 0.7587082153213763,
            "reference_energy": 5.7121527635904386,
            "candidate_energy": 5.697105889186787,
            "relative_energy_error_percent": 0.263418627379176,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.157183527946472e-07,
              "p95": 8.611590601503849e-06,
              "p99": 9.561795741319656e-05,
              "maximum": 0.00023065120331011713
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 31,
              "rgb_channel": 0,
              "reference": 0.00023065120331011713,
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
            "nmbe_percent": -0.618523706432539,
            "cvrmse_percent": 28.078619090345743,
            "rms_normalized_rmse_percent": 2.4016039447328583,
            "reference_energy": 3.036325037909826,
            "candidate_energy": 3.017544647746007,
            "relative_energy_error_percent": 0.618523706432539,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.0973966482197284e-06,
              "p90": 8.369715214939788e-05,
              "p95": 0.00012608524411916733,
              "p99": 0.00024295924231410027,
              "maximum": 0.0014732424169778824
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026194022968411446,
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
            "nmbe_percent": -0.38666457565531753,
            "cvrmse_percent": 9.692005589475878,
            "rms_normalized_rmse_percent": 2.388490576566451,
            "reference_energy": 8.748477801500265,
            "candidate_energy": 8.714650536932794,
            "relative_energy_error_percent": 0.38666457565531753,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 8.095703378785402e-07,
              "p90": 8.083849388640374e-05,
              "p95": 0.00012047894415445626,
              "p99": 0.00023993638751562685,
              "maximum": 0.0014732424169778824
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026194022968411446,
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
            "nmbe_percent": -0.9754796554230878,
            "cvrmse_percent": 17.9084835492252,
            "rms_normalized_rmse_percent": 1.7161988670449029,
            "reference_energy": 0.1237204066396771,
            "candidate_energy": 0.12251353924330033,
            "relative_energy_error_percent": 0.9754796554230878,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 7.045353413559496e-06,
              "maximum": 4.208993777865544e-05
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 13,
              "sky_patch_index": 1,
              "rgb_channel": 0,
              "reference": 4.208993777865544e-05,
              "candidate": 0.0,
              "position": [
                3.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.08865390065992212,
            "cvrmse_percent": 90.31865698198604,
            "rms_normalized_rmse_percent": 7.7846745752517865,
            "reference_energy": 0.20259053532662996,
            "candidate_energy": 0.2024109309146951,
            "relative_energy_error_percent": 0.08865390065992212,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.225947319331681e-08,
              "p90": 1.4074495993554592e-05,
              "p95": 2.1992407710058615e-05,
              "p99": 5.3607487643603235e-05,
              "maximum": 0.0003496631979942322
            },
            "worst": {
              "global_sensor_index": 24,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0010672968346625566,
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
            "nmbe_percent": -0.4248928337974026,
            "cvrmse_percent": 55.88630348017809,
            "rms_normalized_rmse_percent": 7.758555317571881,
            "reference_energy": 0.32631094196630706,
            "candidate_energy": 0.3249244701579954,
            "relative_energy_error_percent": 0.42489283379740267,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.999999525523435e-08,
              "p90": 1.3548362403525971e-05,
              "p95": 2.1202197331149364e-05,
              "p99": 5.3607487643603235e-05,
              "maximum": 0.0003496631979942322
            },
            "worst": {
              "global_sensor_index": 24,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0010672968346625566,
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
            "nmbe_percent": 0.052020883699592506,
            "cvrmse_percent": 26.743785244385727,
            "rms_normalized_rmse_percent": 1.700308464179009,
            "reference_energy": 0.012266535846720217,
            "candidate_energy": 0.012272917007067008,
            "relative_energy_error_percent": 0.0520208836995925,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 8.907343726605177e-06
            },
            "worst": {
              "global_sensor_index": 59,
              "local_sensor_index": 11,
              "sky_patch_index": 16,
              "rgb_channel": 0,
              "reference": 0.0003732107288669795,
              "candidate": 0.00038211807259358466,
              "position": [
                2.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 5.566247608250214,
            "cvrmse_percent": 266.0350335623504,
            "rms_normalized_rmse_percent": 21.149892932084065,
            "reference_energy": 0.02714972866132115,
            "candidate_energy": 0.02866094978357836,
            "relative_energy_error_percent": 5.566247608250214,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 8.90228193384246e-07,
              "p95": 2.59194939644658e-06,
              "p99": 2.1456748072523624e-05,
              "maximum": 0.00015603183419443667
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00028148817364126444,
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
            "nmbe_percent": 3.850193065084578,
            "cvrmse_percent": 182.4179539639508,
            "rms_normalized_rmse_percent": 21.054595001749515,
            "reference_energy": 0.039416264508041365,
            "candidate_energy": 0.04093386679064537,
            "relative_energy_error_percent": 3.850193065084578,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 8.906679340725532e-07,
              "p95": 2.6131223478387255e-06,
              "p99": 2.1587969968095422e-05,
              "maximum": 0.00015603183419443667
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00028148817364126444,
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
        "identifier": "three_room_chain_0_grid",
        "full_identifier": "three_room_chain_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.263418627379176,
            "cvrmse_percent": 3.168318188133712,
            "rms_normalized_rmse_percent": 0.7587082153213763,
            "reference_energy": 5.7121527635904386,
            "candidate_energy": 5.697105889186787,
            "relative_energy_error_percent": 0.263418627379176,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.157183527946472e-07,
              "p95": 8.611590601503849e-06,
              "p99": 9.561795741319656e-05,
              "maximum": 0.00023065120331011713
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 31,
              "rgb_channel": 0,
              "reference": 0.00023065120331011713,
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
            "nmbe_percent": 77.3736894417446,
            "cvrmse_percent": 431.85257156784877,
            "rms_normalized_rmse_percent": 24.343023289313912,
            "reference_energy": 1.7012357679671926,
            "candidate_energy": 3.017544647746007,
            "relative_energy_error_percent": 77.37368944174462,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00024619000032544136,
              "p95": 0.00032901999657042325,
              "p99": 0.0005556899704970419,
              "maximum": 0.010525193065404892
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0145348459482193,
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
            "nmbe_percent": 17.552863981644762,
            "cvrmse_percent": 99.08259302247616,
            "rms_normalized_rmse_percent": 24.338209493614507,
            "reference_energy": 7.413388531557631,
            "candidate_energy": 8.714650536932794,
            "relative_energy_error_percent": 17.552863981644762,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00024619000032544136,
              "p95": 0.0003291713073849678,
              "p99": 0.0005877669900655746,
              "maximum": 0.010525193065404892
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0145348459482193,
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
            "nmbe_percent": -0.9754796554230878,
            "cvrmse_percent": 17.9084835492252,
            "rms_normalized_rmse_percent": 1.7161988670449029,
            "reference_energy": 0.1237204066396771,
            "candidate_energy": 0.12251353924330033,
            "relative_energy_error_percent": 0.9754796554230878,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 7.045353413559496e-06,
              "maximum": 4.208993777865544e-05
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 13,
              "sky_patch_index": 1,
              "rgb_channel": 0,
              "reference": 4.208993777865544e-05,
              "candidate": 0.0,
              "position": [
                3.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 135.9929179301063,
            "cvrmse_percent": 847.8930481056801,
            "rms_normalized_rmse_percent": 40.03346157768591,
            "reference_energy": 0.08576991745771068,
            "candidate_energy": 0.2024109309146951,
            "relative_energy_error_percent": 135.99291793010633,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.1660000129486434e-05,
              "p95": 4.085999898961745e-05,
              "p99": 0.0001265582068299409,
              "maximum": 0.0017081620171666145
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00369343813508749,
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
            "nmbe_percent": 55.10237599658525,
            "cvrmse_percent": 347.03163526748074,
            "rms_normalized_rmse_percent": 40.02027906257513,
            "reference_energy": 0.20949032409738777,
            "candidate_energy": 0.3249244701579954,
            "relative_energy_error_percent": 55.10237599658525,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.123000012943521e-05,
              "p95": 4.0710001485422254e-05,
              "p99": 0.0001220800040755421,
              "maximum": 0.0017081620171666145
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00369343813508749,
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
            "nmbe_percent": 0.052020883699592506,
            "cvrmse_percent": 26.743785244385727,
            "rms_normalized_rmse_percent": 1.700308464179009,
            "reference_energy": 0.012266535846720217,
            "candidate_energy": 0.012272917007067008,
            "relative_energy_error_percent": 0.0520208836995925,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 8.907343726605177e-06
            },
            "worst": {
              "global_sensor_index": 59,
              "local_sensor_index": 11,
              "sky_patch_index": 16,
              "rgb_channel": 0,
              "reference": 0.0003732107288669795,
              "candidate": 0.00038211807259358466,
              "position": [
                2.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 136.55930603652902,
            "cvrmse_percent": 1141.972304648123,
            "rms_normalized_rmse_percent": 51.20758230051901,
            "reference_energy": 0.01211575662094333,
            "candidate_energy": 0.02866094978357836,
            "relative_energy_error_percent": 136.55930603652902,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.8999999440438842e-07,
              "p95": 2.117439180437941e-06,
              "p99": 5.2102533118159045e-05,
              "maximum": 0.00028015235147904605
            },
            "worst": {
              "global_sensor_index": 63,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00013935765309724957,
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
            "nmbe_percent": 67.88358537218339,
            "cvrmse_percent": 567.0288087257256,
            "rms_normalized_rmse_percent": 51.169104941877094,
            "reference_energy": 0.024382292467663547,
            "candidate_energy": 0.04093386679064537,
            "relative_energy_error_percent": 67.88358537218338,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.8999999440438842e-07,
              "p95": 2.1999999262334313e-06,
              "p99": 5.2102533118159045e-05,
              "maximum": 0.00028015235147904605
            },
            "worst": {
              "global_sensor_index": 63,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00013935765309724957,
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
      "bias_percent": -0.02595992978865874,
      "rms_normalized_error_percent": 0.3462308393660956,
      "absolute_error": {
        "p95": 0.12956512823023678,
        "p99": 0.1451590405694859,
        "maximum": 0.1471666429389531
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 5.70761020416085,
      "rms_normalized_to_uniform_percent": 0.3462308393660956
    },
    "overcast": {
      "bias_percent": -0.04472234151553647,
      "rms_normalized_error_percent": 0.2924642059459377,
      "absolute_error": {
        "p95": 0.07044346332550049,
        "p99": 0.09421838760376,
        "maximum": 0.12012863159179688
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.678346872329712,
      "rms_normalized_to_uniform_percent": 0.20629252838514597
    },
    "horizon": {
      "bias_percent": 0.7879424239413592,
      "rms_normalized_error_percent": 3.986818943068181,
      "absolute_error": {
        "p95": 0.0676699342363612,
        "p99": 0.09479166630434331,
        "maximum": 0.11771261094473906
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.5013978306061744,
      "rms_normalized_to_uniform_percent": 0.21234421157954889
    },
    "north": {
      "bias_percent": -100.0,
      "rms_normalized_error_percent": 100.0,
      "absolute_error": {
        "p95": 2.3164932372310442e-05,
        "p99": 0.00016793415292340897,
        "maximum": 0.0002827525604516268
      },
      "worst_index": [
        63
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 1.046918987412937e-05,
      "rms_normalized_to_uniform_percent": 0.00024666093149446706
    },
    "east": {
      "bias_percent": 0.017798297051261326,
      "rms_normalized_error_percent": 0.6916027562020121,
      "absolute_error": {
        "p95": 0.05054052323102953,
        "p99": 0.07433770179748564,
        "maximum": 0.10713481903076172
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.1659992933273315,
      "rms_normalized_to_uniform_percent": 0.14851137320067506
    },
    "south": {
      "bias_percent": -0.0930835834303716,
      "rms_normalized_error_percent": 0.40172753582904736,
      "absolute_error": {
        "p95": 0.08892042636871338,
        "p99": 0.12753298759460455,
        "maximum": 0.13434267044067383
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.901045083999634,
      "rms_normalized_to_uniform_percent": 0.2615117449226527
    },
    "west": {
      "bias_percent": 0.27633068381619386,
      "rms_normalized_error_percent": 0.7047125239691852,
      "absolute_error": {
        "p95": 0.049290645122528086,
        "p99": 0.07449209690094032,
        "maximum": 0.11737847328186035
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.1304430961608887,
      "rms_normalized_to_uniform_percent": 0.14497468301185637
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
          "nmbe_percent": -0.1382934078429425,
          "cvrmse_percent": 2.373391816693559,
          "absolute_error_percentiles_lux": {
            "p50": 5.071388244628906,
            "p90": 50.27489013671877,
            "p95": 75.70101623535136,
            "p99": 144.6106762695311
          },
          "maximum_absolute_error_lux": 446.87939453125,
          "worst": {
            "sensor_index": 14,
            "position": [
              3.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 4855.5400390625,
            "radiance_lux": 5302.41943359375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.4229052511415527,
            "maximum_error_percentage_points": 2.106986301369865,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1645170992499351,
            "maximum_error_percentage_points": 0.4857575123603226,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.12477168949771696,
            "maximum_error_percentage_points": 0.6056164383561651,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.13953196347031996,
            "maximum_error_percentage_points": 0.5719178082191831,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.07283675799086768,
            "maximum_error_percentage_points": 0.4702739726027403,
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
          "nmbe_percent": -0.4385024124128804,
          "cvrmse_percent": 17.327995047949166,
          "absolute_error_percentiles_lux": {
            "p50": 0.9187226295471191,
            "p90": 9.504986190795902,
            "p95": 14.499470615386953,
            "p99": 26.780848388671863
          },
          "maximum_absolute_error_lux": 119.842041015625,
          "worst": {
            "sensor_index": 15,
            "position": [
              3.5,
              4.5,
              0.75
            ],
            "hour_of_year": 1116.5,
            "foton_lux": 3676.560546875,
            "radiance_lux": 3556.718505859375
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.05489726027397257,
            "maximum_error_percentage_points": 0.713013698630137,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.41890327343936246,
            "maximum_error_percentage_points": 1.0219638698177267,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.4467351598173517,
            "maximum_error_percentage_points": 2.2168493150684867,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.44805936073059344,
            "maximum_error_percentage_points": 2.216849315068494,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0013242009132420085,
            "maximum_error_percentage_points": 0.029589041095890403,
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
          "nmbe_percent": 2.8037558227161297,
          "cvrmse_percent": 40.9655066338283,
          "absolute_error_percentiles_lux": {
            "p50": 0.16981978714466095,
            "p90": 1.2791534900665298,
            "p95": 2.472086977958673,
            "p99": 7.208287568092344
          },
          "maximum_absolute_error_lux": 54.47869873046875,
          "worst": {
            "sensor_index": 12,
            "position": [
              3.5,
              11.5,
              0.75
            ],
            "hour_of_year": 348.5,
            "foton_lux": 341.78448486328125,
            "radiance_lux": 287.3057861328125
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.005525114155251142,
            "maximum_error_percentage_points": 0.08,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.13652547404169812,
            "maximum_error_percentage_points": 0.5528134264683016,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.0532990867579907,
            "maximum_error_percentage_points": 0.2784931506849233,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.05329908675799087,
            "maximum_error_percentage_points": 0.2784931506849315,
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
            "maximum_error_percentage_points": 0.0046575342465753344,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.002191780821917816,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.00488120719178653,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.004900270226883663,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.004832830559717394,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004520547945206843,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.002191780821917816,
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
      "study_preparation_seconds": 0.015287333051674068,
      "weather_seconds": 0.11139504099264741,
      "metric_reduction_seconds": 0.04664462502114475,
      "write_seconds": 0.05872854101471603,
      "total_seconds": 0.21700341696850955,
      "cold_end_to_end_seconds": 0.23229075002018362,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.02344870800152421,
      "engine_upload_seconds": 0.000325708,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.02763887494802475,
      "engine_annual_reduction_seconds": 0.0006006249459460378,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.02763887494802475
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.015287333051674068,
      "weather_seconds": 0.10760179196950048,
      "metric_reduction_seconds": 0.013578874990344048,
      "write_seconds": 0.036740959039889276,
      "total_seconds": 0.1581002080347389,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1581002080347389,
      "raw_export_seconds": 0.02308829198591411,
      "engine_upload_seconds": 6.6208e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0006661249790340662,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.019035083008930087,
      "full": 0.01833604194689542
    }
  },
  "elapsed_seconds": 148.3493989580311,
  "result_class": "unstable_reference"
}
```
