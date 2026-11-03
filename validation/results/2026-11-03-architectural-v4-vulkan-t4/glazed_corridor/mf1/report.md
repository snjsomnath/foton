# Foton report

Status: **incomplete**

```json
{
  "scene": "glazed_corridor",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "glazed_corridor",
    "category": "connections",
    "question": "Does a glazed corridor feed an office and an adjoining meeting room?",
    "interactions": [
      "borrowed_light",
      "turning_light_path",
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
    "sensors": 90,
    "floor_area": 90.0,
    "aperture_area": 20.699999999999996
  },
  "sky_density": 1,
  "status": "incomplete",
  "passed": false,
  "model_sha256": "da618b3ff3995bfc783d78a25d021f7966783c66f1c1658daa2a343307ebd21a",
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 706269953697064074,
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 706269953697064074,
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
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 65536,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": false,
  "reference_source": {
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "270810b9b663bc6b0d9aa1af68fdff739164431696bd930ad5e7a63a75a1755c",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "94ed5584a1f4c854071651885dd6e15bc9326094d0a19791950cc11f1dfe41d3",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0001775913406163454,
          "p95": 7.075606845319271e-06,
          "p99": 5.537690594792366e-05
        },
        "bias_percent": -0.025761129979878127,
        "identifier": "glazed_corridor_corridor_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.2869348303474293,
        "worst_index": [
          1,
          94,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 4.316645208746195e-05,
          "p95": 0.0,
          "p99": 6.303394911810756e-06
        },
        "bias_percent": -0.08395684853458937,
        "identifier": "glazed_corridor_office_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.5392727983793265,
        "worst_index": [
          28,
          47,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 8.049566531553864e-06,
          "p95": 0.0,
          "p99": 0.0
        },
        "bias_percent": -0.403069868915149,
        "identifier": "glazed_corridor_meeting_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.627412963662213,
        "worst_index": [
          1,
          19,
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
          "maximum": 0.0004888772964477539,
          "p95": 9.183678776025772e-05,
          "p99": 0.00016102241352200508
        },
        "bias_percent": 0.017472739816809968,
        "identifier": "glazed_corridor_corridor_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.5430618753269252,
        "worst_index": [
          3,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00022150762379169464,
          "p95": 1.1698783418978563e-05,
          "p99": 5.0235510570928454e-05
        },
        "bias_percent": 0.3988215736245471,
        "identifier": "glazed_corridor_office_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.075151854167271,
        "worst_index": [
          23,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 5.669821985065937e-05,
          "p95": 1.29595152316142e-06,
          "p99": 4.343566047282366e-06
        },
        "bias_percent": 0.621585567331912,
        "identifier": "glazed_corridor_meeting_grid",
        "passed": false,
        "rms_normalized_error_percent": 7.20480949377249,
        "worst_index": [
          2,
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
          "maximum": 0.0006406009197235107,
          "p95": 8.579622954130173e-05,
          "p99": 0.00017005298286676407
        },
        "bias_percent": -0.02771017393930103,
        "identifier": "glazed_corridor_corridor_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.5613591205678966,
        "worst_index": [
          1,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00030458346009254456,
          "p95": 1.158159993792648e-05,
          "p99": 5.522114224731922e-05
        },
        "bias_percent": -0.22048227817991908,
        "identifier": "glazed_corridor_office_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.9451442766721194,
        "worst_index": [
          23,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 3.3506585168652236e-05,
          "p95": 1.3047666726606571e-06,
          "p99": 3.962164555559866e-06
        },
        "bias_percent": -0.017708471398588818,
        "identifier": "glazed_corridor_meeting_grid",
        "passed": false,
        "rms_normalized_error_percent": 5.4051834452756,
        "worst_index": [
          4,
          0,
          0
        ]
      }
    ],
    "passed": false
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
            "identifier": "glazed_corridor_corridor_grid",
            "sensor_count": 18,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007029096595942974,
                  "p50": 0.0,
                  "p90": 0.00010835132561624048,
                  "p95": 0.00018590502440929413,
                  "p99": 0.00038910703733563423
                },
                "candidate_energy": 11.023911380072605,
                "cvrmse_percent": 5.881276109050882,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.005775829511787681,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.024548139177568,
                "relative_energy_error_percent": 0.005775829511787681,
                "rms_normalized_rmse_percent": 2.149206503542682,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.015082514844834805,
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "reference": 0.014379605185240507,
                  "rgb_channel": 0,
                  "sky_patch_index": 98
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0014110561460256577,
                  "p50": 0.0,
                  "p90": 0.00021756316709797794,
                  "p95": 0.00037439598236232996,
                  "p99": 0.000697605311870575
                },
                "candidate_energy": 3.31723147051315,
                "cvrmse_percent": 36.7015343450348,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.1385127505556599,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.32183263226095,
                "relative_energy_error_percent": 0.13851275055565987,
                "rms_normalized_rmse_percent": 2.6691948918361703,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04717621952295303,
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "reference": 0.04858727566897869,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003521800972521305,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00012814643559977412
                },
                "candidate_energy": 0.6251508331297373,
                "cvrmse_percent": 55.871708840497355,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.014185027164234051,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6250621678914285,
                "relative_energy_error_percent": 0.014185027164234051,
                "rms_normalized_rmse_percent": 8.00471362263119,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003902406431734562,
                  "global_sensor_index": 35,
                  "local_sensor_index": 17,
                  "reference": 0.004254586528986692,
                  "rgb_channel": 0,
                  "sky_patch_index": 44
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00048391136806458235,
                  "p50": 0.0,
                  "p90": 6.07119829965086e-08,
                  "p95": 1.4209358096195484e-05,
                  "p99": 0.0001946364063769579
                },
                "candidate_energy": 0.44651003970861325,
                "cvrmse_percent": 120.4922192113812,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.4098228072072831,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.4446876084682856,
                "relative_energy_error_percent": 0.4098228072072831,
                "rms_normalized_rmse_percent": 7.607765011829363,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0002592849778011441,
                  "global_sensor_index": 29,
                  "local_sensor_index": 11,
                  "reference": 0.00022462639026343822,
                  "rgb_channel": 0,
                  "sky_patch_index": 43
                }
              }
            },
            "start_sensor_index": 18
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 5.488307942869142e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.004449123764061369,
                "cvrmse_percent": 398.9001342506559,
                "energy_difference_negligible": true,
                "nmbe_percent": 1.8859419874128238,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.004366769033367746,
                "relative_energy_error_percent": 1.885941987412824,
                "rms_normalized_rmse_percent": 11.762641164406165,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0001377416483592242,
                  "global_sensor_index": 66,
                  "local_sensor_index": 12,
                  "reference": 8.285856893053278e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 19
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0001478658741689287,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.516414825659012e-06
                },
                "candidate_energy": 0.01092653417745737,
                "cvrmse_percent": 537.6562934387846,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.8575930163043374,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.011021049931997595,
                "relative_energy_error_percent": 0.8575930163043375,
                "rms_normalized_rmse_percent": 25.172558215565033,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 8.291505218949169e-05,
                  "global_sensor_index": 66,
                  "local_sensor_index": 12,
                  "reference": 0.0002307809263584204,
                  "rgb_channel": 0,
                  "sky_patch_index": 19
                }
              }
            },
            "start_sensor_index": 54
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 295.4837919678539,
            "full": 531.4694161061198
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 177.6509169721976,
            "full": 532.5613330351189
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 175.55329203605652,
            "full": 551.6739580780268
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 167.81637503299862,
            "full": 528.7161250598729
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
            "identifier": "glazed_corridor_corridor_grid",
            "sensor_count": 18,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002911465708166361,
                  "p50": 0.0,
                  "p90": 5.064266733825206e-05,
                  "p95": 9.359768591821194e-05,
                  "p99": 0.00018462492153048515
                },
                "candidate_energy": 11.028762652583737,
                "cvrmse_percent": 2.8032709083693916,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.04187543128283318,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.024146243798896,
                "relative_energy_error_percent": 0.04187543128283318,
                "rms_normalized_rmse_percent": 1.0251360912998337,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007711993297562003,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.00800313986837864,
                  "rgb_channel": 0,
                  "sky_patch_index": 48
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008119139820337296,
                  "p50": 3.0628008573785337e-07,
                  "p90": 7.872894348110997e-05,
                  "p95": 0.00013430771650746465,
                  "p99": 0.0002701869234442711
                },
                "candidate_energy": 5.644859411757334,
                "cvrmse_percent": 8.536285441739821,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.08338324396726096,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.64957020666586,
                "relative_energy_error_percent": 0.08338324396726096,
                "rms_normalized_rmse_percent": 0.8422729516106302,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07099012844264507,
                  "global_sensor_index": 0,
                  "local_sensor_index": 0,
                  "reference": 0.07017821446061134,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001392950362060219,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.202575701128808e-05
                },
                "candidate_energy": 0.6256762523153157,
                "cvrmse_percent": 20.7106816209686,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.07920959521919277,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6251810489370655,
                "relative_energy_error_percent": 0.07920959521919277,
                "rms_normalized_rmse_percent": 2.9795244126853437,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0014807689876761287,
                  "global_sensor_index": 40,
                  "local_sensor_index": 22,
                  "reference": 0.0016200640238821507,
                  "rgb_channel": 0,
                  "sky_patch_index": 17
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004186653532087803,
                  "p50": 5.27507539871408e-08,
                  "p90": 6.700426865791087e-06,
                  "p95": 1.3674282649844827e-05,
                  "p99": 8.39041022118181e-05
                },
                "candidate_energy": 0.9168158335033301,
                "cvrmse_percent": 27.863528129415418,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.5527270216654585,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9219114874100836,
                "relative_energy_error_percent": 0.5527270216654585,
                "rms_normalized_rmse_percent": 2.7128478384122934,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.01542772981338203,
                  "global_sensor_index": 41,
                  "local_sensor_index": 23,
                  "reference": 0.01584639516659081,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 18
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 2.0337654859758914e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.004229307060086285,
                "cvrmse_percent": 163.97816535686715,
                "energy_difference_negligible": true,
                "nmbe_percent": -1.6557631058096185,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.00430051337389159,
                "relative_energy_error_percent": 1.6557631058096183,
                "rms_normalized_rmse_percent": 5.226235482317415,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0002019337989622727,
                  "global_sensor_index": 61,
                  "local_sensor_index": 7,
                  "reference": 0.00022227145382203162,
                  "rgb_channel": 0,
                  "sky_patch_index": 19
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 5.8163757785223424e-05,
                  "p50": 0.0,
                  "p90": 8.386947456529015e-07,
                  "p95": 1.648782415220038e-06,
                  "p99": 4.856003840814083e-06
                },
                "candidate_energy": 0.03183024819346514,
                "cvrmse_percent": 97.23493055659841,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.2877058043692902,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.03192208989898049,
                "relative_energy_error_percent": 0.2877058043692902,
                "rms_normalized_rmse_percent": 8.998521622510395,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00027086544287158176,
                  "global_sensor_index": 63,
                  "local_sensor_index": 9,
                  "reference": 0.0003290292006568052,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 54
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 249.12049993872643,
            "full": 6682.176292059012
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 260.97816694527864,
            "full": 6865.685916971415
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 237.76208399794996,
            "full": 6843.58033305034
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 239.63920795358717,
            "full": 6890.554500045255
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 246.2986670434475,
            "full": 6781.935291015543
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 254.6770420158282,
            "full": 6727.661540964618
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 237.91116592474282,
            "full": 7043.84400008712
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 246.56704103108495,
            "full": 6834.428749978542
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
            "identifier": "glazed_corridor_corridor_grid",
            "sensor_count": 18,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005704197101294994,
                  "p50": 0.0,
                  "p90": 6.942802574485538e-05,
                  "p95": 0.00013093336019665003,
                  "p99": 0.0002463730052113533
                },
                "candidate_energy": 11.03022346367652,
                "cvrmse_percent": 3.9451925260611995,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.025085246333245756,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.02745719887389,
                "relative_energy_error_percent": 0.02508524633324576,
                "rms_normalized_rmse_percent": 1.4434289706574432,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.014000074937939644,
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "reference": 0.013429655227810144,
                  "rgb_channel": 0,
                  "sky_patch_index": 73
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009200610220432281,
                  "p50": 4.498508303640847e-07,
                  "p90": 0.00011310381814837433,
                  "p95": 0.00020517490338534117,
                  "p99": 0.00035690050572156906
                },
                "candidate_energy": 5.63996677926804,
                "cvrmse_percent": 11.610086276459644,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.2749705314011164,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.655517786579281,
                "relative_energy_error_percent": 0.2749705314011164,
                "rms_normalized_rmse_percent": 1.1453739747340985,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07047392427921295,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.07139398530125618,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002341500949114561,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.5084688938222826e-05
                },
                "candidate_energy": 0.6287730420344815,
                "cvrmse_percent": 27.464104177362053,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.6266923481767577,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6248571103369613,
                "relative_energy_error_percent": 0.6266923481767577,
                "rms_normalized_rmse_percent": 3.957636712081611,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0026910080341622233,
                  "global_sensor_index": 40,
                  "local_sensor_index": 22,
                  "reference": 0.0024568579392507672,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004090755246579647,
                  "p50": 6.290441589840157e-08,
                  "p90": 9.388450052938424e-06,
                  "p95": 1.880046929727535e-05,
                  "p99": 0.00011250213719904423
                },
                "candidate_energy": 0.9228482773213109,
                "cvrmse_percent": 34.89040112599774,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.2787754059031793,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.925428143384373,
                "relative_energy_error_percent": 0.2787754059031793,
                "rms_normalized_rmse_percent": 3.414840888142219,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.006671447539702058,
                  "global_sensor_index": 29,
                  "local_sensor_index": 11,
                  "reference": 0.0070805230643600225,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 18
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 2.6870358851738274e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.004278600797988474,
                "cvrmse_percent": 197.88596254782533,
                "energy_difference_negligible": true,
                "nmbe_percent": 2.909829791074202,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.004157621100603137,
                "relative_energy_error_percent": 2.909829791074202,
                "rms_normalized_rmse_percent": 6.282657084162957,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0002641737082740292,
                  "global_sensor_index": 60,
                  "local_sensor_index": 6,
                  "reference": 0.00023730334942229092,
                  "rgb_channel": 0,
                  "sky_patch_index": 19
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 6.22618681518361e-05,
                  "p50": 0.0,
                  "p90": 1.0930571079370566e-06,
                  "p95": 2.1228969501407817e-06,
                  "p99": 6.784083254274265e-06
                },
                "candidate_energy": 0.03198309756451323,
                "cvrmse_percent": 102.27895677249744,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -1.0183059486002548,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.032312133946611254,
                "relative_energy_error_percent": 1.0183059486002548,
                "rms_normalized_rmse_percent": 9.20895612385731,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00027754549228120595,
                  "global_sensor_index": 62,
                  "local_sensor_index": 8,
                  "reference": 0.00033980736043304205,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 54
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 239.99270796775818,
            "full": 7001.355167012662
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 241.36341700796038,
            "full": 7151.106292032637
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 252.28037498891354,
            "full": 7039.171208045445
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 238.9225410297513,
            "full": 7022.2921669483185
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
            "identifier": "glazed_corridor_corridor_grid",
            "sensor_count": 18,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00021080859005451202,
                  "p50": 0.0,
                  "p90": 3.725268179550767e-05,
                  "p95": 7.164443377405405e-05,
                  "p99": 0.00012383703142404556
                },
                "candidate_energy": 11.026225451706523,
                "cvrmse_percent": 2.023340833387347,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.01063736673280157,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.027398476523558,
                "relative_energy_error_percent": 0.010637366732801572,
                "rms_normalized_rmse_percent": 0.7400942326111692,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0058320085518062115,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.0060428171418607235,
                  "rgb_channel": 0,
                  "sky_patch_index": 75
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005022026598453522,
                  "p50": 3.4788746461345e-07,
                  "p90": 6.607616087421763e-05,
                  "p95": 0.00011363998055458069,
                  "p99": 0.00021619186736643314
                },
                "candidate_energy": 5.648139624240017,
                "cvrmse_percent": 6.953311404534451,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.10599170739614755,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.642159403154601,
                "relative_energy_error_percent": 0.10599170739614754,
                "rms_normalized_rmse_percent": 0.685066898775782,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.08090208098292351,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.08039987832307816,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 8.723716018721461e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.498289152048528e-05
                },
                "candidate_energy": 0.626091961588827,
                "cvrmse_percent": 15.36094100207,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.09423521576234667,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6266825172110657,
                "relative_energy_error_percent": 0.09423521576234668,
                "rms_normalized_rmse_percent": 2.2103593281439546,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0009913828398566693,
                  "global_sensor_index": 27,
                  "local_sensor_index": 9,
                  "reference": 0.0009041456796694547,
                  "rgb_channel": 0,
                  "sky_patch_index": 44
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00019937986508011818,
                  "p50": 5.2145422202443115e-08,
                  "p90": 6.2364106270251796e-06,
                  "p95": 1.2890429934486733e-05,
                  "p99": 6.368005415424705e-05
                },
                "candidate_energy": 0.9210899058432354,
                "cvrmse_percent": 21.99671691264759,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.012280436260381996,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9212030335946046,
                "relative_energy_error_percent": 0.012280436260381996,
                "rms_normalized_rmse_percent": 2.1452557570337634,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.015270440373569727,
                  "global_sensor_index": 35,
                  "local_sensor_index": 17,
                  "reference": 0.015469820238649845,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 18
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 1.925874676089734e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.004415296367369592,
                "cvrmse_percent": 141.56750773283795,
                "energy_difference_negligible": true,
                "nmbe_percent": 1.3195853165993232,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.0043577915894275066,
                "relative_energy_error_percent": 1.3195853165993232,
                "rms_normalized_rmse_percent": 4.429310935076277,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00017225794726982713,
                  "global_sensor_index": 55,
                  "local_sensor_index": 1,
                  "reference": 0.0001529992005089298,
                  "rgb_channel": 0,
                  "sky_patch_index": 18
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 5.0659000407904387e-05,
                  "p50": 0.0,
                  "p90": 7.762722589177429e-07,
                  "p95": 1.5332564032632936e-06,
                  "p99": 4.900872681901092e-06
                },
                "candidate_energy": 0.03216368197780284,
                "cvrmse_percent": 86.66027387438956,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 1.2015613007333674,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.03178180411883602,
                "relative_energy_error_percent": 1.2015613007333674,
                "rms_normalized_rmse_percent": 7.710809539400464,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0002544069502619095,
                  "global_sensor_index": 67,
                  "local_sensor_index": 13,
                  "reference": 0.00020374794985400513,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 54
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 393.9120420254767,
            "full": 12746.663541998714
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 399.14970903191715,
            "full": 12355.440582963638
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 392.5106250680983,
            "full": 12405.205333023332
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
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 388.9275830006227,
            "full": 12547.182917012833
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
    "/content/foton-run/validation/results/2026-11-03-architectural-v4-vulkan-t4/glazed_corridor/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4193.047709064558,
      "invocation_count": 6,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 15194.103415939026,
      "invocation_count": 6,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/direct_4096/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/direct_4096/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 62649.583957972936,
      "invocation_count": 6,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/direct_16384/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf1/direct_16384/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 222916.8956669746,
      "invocation_count": 6,
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
      90,
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
        "identifier": "glazed_corridor_corridor_grid",
        "full_identifier": "glazed_corridor_corridor_grid",
        "start_sensor_index": 0,
        "sensor_count": 18,
        "stages": {
          "direct": {
            "nmbe_percent": -0.43182938500037543,
            "cvrmse_percent": 2.779007932329969,
            "rms_normalized_rmse_percent": 1.0188235052607055,
            "reference_energy": 11.024760408826978,
            "candidate_energy": 10.977152253755776,
            "relative_energy_error_percent": 0.43182938500037543,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.0874468716792738e-05,
              "p95": 5.478193997987546e-05,
              "p99": 0.00016140971274580806,
              "maximum": 0.0004501957446336746
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 31,
              "rgb_channel": 0,
              "reference": 0.0004501957446336746,
              "candidate": 0.0,
              "position": [
                2.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.4444753632287619,
            "cvrmse_percent": 14.438132946826611,
            "rms_normalized_rmse_percent": 1.4240022038371016,
            "reference_energy": 5.647201030336298,
            "candidate_energy": 5.622100613044452,
            "relative_energy_error_percent": 0.4444753632287619,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.908628968929406e-06,
              "p90": 8.863581460900591e-05,
              "p95": 0.0001442911452613771,
              "p99": 0.0004226421006023884,
              "maximum": 0.0018492639064788818
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.08343791216611862,
              "candidate": 0.08158864825963974,
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
            "nmbe_percent": -0.4361128870670968,
            "cvrmse_percent": 4.604889476246014,
            "rms_normalized_rmse_percent": 1.3408255743946143,
            "reference_energy": 16.671961439163276,
            "candidate_energy": 16.599252866800228,
            "relative_energy_error_percent": 0.4361128870670968,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.57954411861283e-06,
              "p90": 7.321984739974138e-05,
              "p95": 0.00011909939348697662,
              "p99": 0.00029464811086654663,
              "maximum": 0.0018492639064788818
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.08343791216611862,
              "candidate": 0.08158864825963974,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "glazed_corridor_office_grid",
        "full_identifier": "glazed_corridor_office_grid",
        "start_sensor_index": 18,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.036315361967766004,
            "cvrmse_percent": 5.776812400987404,
            "rms_normalized_rmse_percent": 0.8311967704061786,
            "reference_energy": 0.626363030980384,
            "candidate_energy": 0.6265904969823168,
            "relative_energy_error_percent": 0.036315361967766004,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 7.80163099989295e-06,
              "maximum": 6.863447197247297e-05
            },
            "worst": {
              "global_sensor_index": 50,
              "local_sensor_index": 32,
              "sky_patch_index": 13,
              "rgb_channel": 0,
              "reference": 6.863447197247297e-05,
              "candidate": 0.0,
              "position": [
                5.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.0727849567207299,
            "cvrmse_percent": 29.594677857653018,
            "rms_normalized_rmse_percent": 2.8898326564682186,
            "reference_energy": 0.9211706769756312,
            "candidate_energy": 0.9205002032970704,
            "relative_energy_error_percent": 0.07278495672072992,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.1308541658650029e-07,
              "p90": 1.1943880963372067e-05,
              "p95": 2.058414247585457e-05,
              "p99": 5.6239485275000334e-05,
              "maximum": 0.00040520913898944855
            },
            "worst": {
              "global_sensor_index": 36,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.005311180837452412,
              "candidate": 0.00571638997644186,
              "position": [
                3.5,
                8.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.028626689961609712,
            "cvrmse_percent": 17.56434886433665,
            "rms_normalized_rmse_percent": 2.881317683301492,
            "reference_energy": 1.5475337079560152,
            "candidate_energy": 1.5470907002793872,
            "relative_energy_error_percent": 0.028626689961609712,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.1299527713504176e-07,
              "p90": 1.1982258001808077e-05,
              "p95": 2.0422942543518727e-05,
              "p99": 5.663646152243018e-05,
              "maximum": 0.00040520913898944855
            },
            "worst": {
              "global_sensor_index": 36,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.005311180837452412,
              "candidate": 0.00571638997644186,
              "position": [
                3.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "glazed_corridor_meeting_grid",
        "full_identifier": "glazed_corridor_meeting_grid",
        "start_sensor_index": 54,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.10614576222249403,
            "cvrmse_percent": 39.93749274302548,
            "rms_normalized_rmse_percent": 1.2614532858188487,
            "reference_energy": 0.004281973812432227,
            "candidate_energy": 0.004286518946173601,
            "relative_energy_error_percent": 0.10614576222249404,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 5.7412253227084875e-06
            },
            "worst": {
              "global_sensor_index": 55,
              "local_sensor_index": 1,
              "sky_patch_index": 19,
              "rgb_channel": 0,
              "reference": 0.0002758817281574011,
              "candidate": 0.00028162295348010957,
              "position": [
                6.5,
                7.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.34830392602088356,
            "cvrmse_percent": 97.85706092470521,
            "rms_normalized_rmse_percent": 8.80945122533569,
            "reference_energy": 0.032077313266484,
            "candidate_energy": 0.03218903980795318,
            "relative_energy_error_percent": 0.34830392602088356,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.3935712104284903e-06,
              "p95": 2.7918486665612362e-06,
              "p99": 7.496764737879857e-06,
              "maximum": 6.056932033970952e-05
            },
            "worst": {
              "global_sensor_index": 56,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0007399606984108686,
              "candidate": 0.0008005300187505782,
              "position": [
                6.5,
                6.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.3197853548618616,
            "cvrmse_percent": 85.6804853280644,
            "rms_normalized_rmse_percent": 8.742909421463263,
            "reference_energy": 0.036359287078916225,
            "candidate_energy": 0.03647555875412678,
            "relative_energy_error_percent": 0.31978535486186166,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.3952277981843508e-06,
              "p95": 2.8008481251617874e-06,
              "p99": 7.496764737879857e-06,
              "maximum": 6.056932033970952e-05
            },
            "worst": {
              "global_sensor_index": 56,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0007399606984108686,
              "candidate": 0.0008005300187505782,
              "position": [
                6.5,
                6.5,
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
      90,
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
        "identifier": "glazed_corridor_corridor_grid",
        "full_identifier": "glazed_corridor_corridor_grid",
        "start_sensor_index": 0,
        "sensor_count": 18,
        "stages": {
          "direct": {
            "nmbe_percent": -0.43182938500037543,
            "cvrmse_percent": 2.779007932329969,
            "rms_normalized_rmse_percent": 1.0188235052607055,
            "reference_energy": 11.024760408826978,
            "candidate_energy": 10.977152253755776,
            "relative_energy_error_percent": 0.43182938500037543,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.0874468716792738e-05,
              "p95": 5.478193997987546e-05,
              "p99": 0.00016140971274580806,
              "maximum": 0.0004501957446336746
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 31,
              "rgb_channel": 0,
              "reference": 0.0004501957446336746,
              "candidate": 0.0,
              "position": [
                2.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 69.39133177960285,
            "cvrmse_percent": 410.95177577335716,
            "rms_normalized_rmse_percent": 29.89735981068174,
            "reference_energy": 3.3190013644614567,
            "candidate_energy": 5.622100613044452,
            "relative_energy_error_percent": 69.39133177960287,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.5483830793527886e-05,
              "p90": 0.0005096106004202738,
              "p95": 0.0006715171039104462,
              "p99": 0.001072942279279232,
              "maximum": 0.02596067637205124
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04485659301280975,
              "candidate": 0.07081726938486099,
              "position": [
                0.5,
                2.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 15.724543736581465,
            "cvrmse_percent": 95.06791289149332,
            "rms_normalized_rmse_percent": 29.890389133981447,
            "reference_energy": 14.343761773288435,
            "candidate_energy": 16.599252866800228,
            "relative_energy_error_percent": 15.724543736581465,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 9.642780582908017e-07,
              "p90": 0.0005090439604828132,
              "p95": 0.0006735436618328094,
              "p99": 0.001061558723449707,
              "maximum": 0.02596067637205124
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04485659301280975,
              "candidate": 0.07081726938486099,
              "position": [
                0.5,
                2.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "glazed_corridor_office_grid",
        "full_identifier": "glazed_corridor_office_grid",
        "start_sensor_index": 18,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.036315361967766004,
            "cvrmse_percent": 5.776812400987404,
            "rms_normalized_rmse_percent": 0.8311967704061786,
            "reference_energy": 0.626363030980384,
            "candidate_energy": 0.6265904969823168,
            "relative_energy_error_percent": 0.036315361967766004,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 7.80163099989295e-06,
              "maximum": 6.863447197247297e-05
            },
            "worst": {
              "global_sensor_index": 50,
              "local_sensor_index": 32,
              "sky_patch_index": 13,
              "rgb_channel": 0,
              "reference": 6.863447197247297e-05,
              "candidate": 0.0,
              "position": [
                5.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 107.16015722585016,
            "cvrmse_percent": 647.2318316252483,
            "rms_normalized_rmse_percent": 40.89148547479851,
            "reference_energy": 0.4443422980672498,
            "candidate_energy": 0.9205002032970704,
            "relative_energy_error_percent": 107.16015722585016,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.8639998314902186e-05,
              "p95": 0.00010336491141060825,
              "p99": 0.00024251220747828484,
              "maximum": 0.004558149725198746
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011153580620884895,
              "candidate": 0.01571173034608364,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 44.49266836614015,
            "cvrmse_percent": 268.6387284162963,
            "rms_normalized_rmse_percent": 40.89723526620326,
            "reference_energy": 1.0707053290476338,
            "candidate_energy": 1.5470907002793872,
            "relative_energy_error_percent": 44.49266836614015,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.796999903395772e-05,
              "p95": 0.00010172708534810225,
              "p99": 0.00024416189990006387,
              "maximum": 0.004558149725198746
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011153580620884895,
              "candidate": 0.01571173034608364,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "glazed_corridor_meeting_grid",
        "full_identifier": "glazed_corridor_meeting_grid",
        "start_sensor_index": 54,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.10614576222249403,
            "cvrmse_percent": 39.93749274302548,
            "rms_normalized_rmse_percent": 1.2614532858188487,
            "reference_energy": 0.004281973812432227,
            "candidate_energy": 0.004286518946173601,
            "relative_energy_error_percent": 0.10614576222249404,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 5.7412253227084875e-06
            },
            "worst": {
              "global_sensor_index": 55,
              "local_sensor_index": 1,
              "sky_patch_index": 19,
              "rgb_channel": 0,
              "reference": 0.0002758817281574011,
              "candidate": 0.00028162295348010957,
              "position": [
                6.5,
                7.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 189.99750229367572,
            "cvrmse_percent": 1507.0371496726327,
            "rms_normalized_rmse_percent": 70.85544530630041,
            "reference_energy": 0.01109976449912864,
            "candidate_energy": 0.03218903980795318,
            "relative_energy_error_percent": 189.99750229367572,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.9300000531075057e-06,
              "p95": 4.4164999735585265e-06,
              "p99": 2.1175259462324902e-05,
              "maximum": 0.00042109665810130537
            },
            "worst": {
              "global_sensor_index": 56,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0003794333606492728,
              "candidate": 0.0008005300187505782,
              "position": [
                6.5,
                6.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 137.13547854803815,
            "cvrmse_percent": 1087.435886504497,
            "rms_normalized_rmse_percent": 70.85077230332331,
            "reference_energy": 0.015381738311560866,
            "candidate_energy": 0.03647555875412678,
            "relative_energy_error_percent": 137.13547854803812,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.933150088007096e-06,
              "p95": 4.439499889485876e-06,
              "p99": 2.1140935132279992e-05,
              "maximum": 0.00042109665810130537
            },
            "worst": {
              "global_sensor_index": 56,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0003794333606492728,
              "candidate": 0.0008005300187505782,
              "position": [
                6.5,
                6.5,
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
      "bias_percent": -0.20597470715330743,
      "rms_normalized_error_percent": 0.38249269951099624,
      "absolute_error": {
        "p95": 0.15122172337106998,
        "p99": 0.4484303800621088,
        "maximum": 0.49327934948383856
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.109785253966558,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.38249269951099624
    },
    "overcast": {
      "bias_percent": -0.15330826275806267,
      "rms_normalized_error_percent": 0.2668830842746556,
      "absolute_error": {
        "p95": 0.06718854904174802,
        "p99": 0.22058916091918943,
        "maximum": 0.25067806243896484
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.923061847686768,
      "reference_fraction_of_uniform": 0.6501867771148682,
      "rms_normalized_to_uniform_percent": 0.1850944777044247
    },
    "horizon": {
      "bias_percent": -0.06289754285629588,
      "rms_normalized_error_percent": 1.7404420273847983,
      "absolute_error": {
        "p95": 0.055158614121533084,
        "p99": 0.08138966060483278,
        "maximum": 0.1011555962478563
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.7794898594965706,
      "reference_fraction_of_uniform": 0.08556621674008914,
      "rms_normalized_to_uniform_percent": 0.1082048572680901
    },
    "north": {
      "bias_percent": -70.46715215776571,
      "rms_normalized_error_percent": 102.2323029562356,
      "absolute_error": {
        "p95": 7.810600691300351e-05,
        "p99": 0.00010526534144901231,
        "maximum": 0.00014820325304754078
      },
      "worst_index": [
        47
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.5294521290343255e-05,
      "reference_fraction_of_uniform": 1.6789113033155445e-06,
      "rms_normalized_to_uniform_percent": 0.0001364364480518431
    },
    "east": {
      "bias_percent": -0.1897838772004144,
      "rms_normalized_error_percent": 0.3880227325776278,
      "absolute_error": {
        "p95": 0.048400354385375974,
        "p99": 0.09233688354492188,
        "maximum": 0.09283256530761719
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.8535122871398926,
      "reference_fraction_of_uniform": 0.20346388220787048,
      "rms_normalized_to_uniform_percent": 0.08452295277298019
    },
    "south": {
      "bias_percent": -0.2833604024981477,
      "rms_normalized_error_percent": 0.5445221304178046,
      "absolute_error": {
        "p95": 0.15568675994873038,
        "p99": 0.40232515335083,
        "maximum": 0.4501533508300781
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.17833137512207,
      "reference_fraction_of_uniform": 0.6782082319259644,
      "rms_normalized_to_uniform_percent": 0.3492912772475492
    },
    "west": {
      "bias_percent": -0.21067213606689345,
      "rms_normalized_error_percent": 0.34345782904380495,
      "absolute_error": {
        "p95": 0.03838310241699216,
        "p99": 0.06128429889678953,
        "maximum": 0.08477783203125
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.795233130455017,
      "reference_fraction_of_uniform": 0.19706647098064423,
      "rms_normalized_to_uniform_percent": 0.07193481756291352
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
        "identifier": "glazed_corridor_corridor_grid",
        "sensor_count": 18,
        "illuminance": {
          "nmbe_percent": -0.21787857727937388,
          "cvrmse_percent": 1.1760441870560503,
          "absolute_error_percentiles_lux": {
            "p50": 6.56671142578125,
            "p90": 52.764257812500034,
            "p95": 81.62192382812502,
            "p99": 178.03958007812503
          },
          "maximum_absolute_error_lux": 734.634765625,
          "worst": {
            "sensor_index": 9,
            "position": [
              3.5,
              2.5,
              0.75
            ],
            "hour_of_year": 1116.5,
            "foton_lux": 15856.734375,
            "radiance_lux": 16591.369140625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.06758751902587869,
            "maximum_error_percentage_points": 0.27876712328767894,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.02609985465147149,
            "maximum_error_percentage_points": 0.11253290119786641,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.01999238964992421,
            "maximum_error_percentage_points": 0.11123287671232873,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.1476712328767105,
            "maximum_error_percentage_points": 0.3534246575342479,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.1616362252663618,
            "maximum_error_percentage_points": 0.4646575342465731,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 5.555555555555555,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "glazed_corridor_office_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.1449500247767255,
          "cvrmse_percent": 5.1305811281729,
          "absolute_error_percentiles_lux": {
            "p50": 0.9421520233154297,
            "p90": 8.482250595092774,
            "p95": 12.953905487060538,
            "p99": 25.776700439453112
          },
          "maximum_absolute_error_lux": 100.1334228515625,
          "worst": {
            "sensor_index": 18,
            "position": [
              3.5,
              8.5,
              0.75
            ],
            "hour_of_year": 8604.5,
            "foton_lux": 1613.9307861328125,
            "radiance_lux": 1513.79736328125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.1707648401826486,
            "maximum_error_percentage_points": 0.7972602739726042,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.36643154621650753,
            "maximum_error_percentage_points": 1.2501313890931485,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.8937290715372909,
            "maximum_error_percentage_points": 3.29150684931507,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.8889345509893464,
            "maximum_error_percentage_points": 3.29150684931507,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.006872146118721465,
            "maximum_error_percentage_points": 0.11369863013698644,
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
        "identifier": "glazed_corridor_meeting_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -1.1235927300642563,
          "cvrmse_percent": 34.245586761425265,
          "absolute_error_percentiles_lux": {
            "p50": 0.08998455852270126,
            "p90": 0.906082451343537,
            "p95": 1.4968756258487674,
            "p99": 3.4443802738189535
          },
          "maximum_absolute_error_lux": 11.705045700073242,
          "worst": {
            "sensor_index": 9,
            "position": [
              7.5,
              5.5,
              0.75
            ],
            "hour_of_year": 1117.5,
            "foton_lux": 28.729753494262695,
            "radiance_lux": 17.024707794189453
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.0,
            "maximum_error_percentage_points": 0.0,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.05202994299322436,
            "maximum_error_percentage_points": 0.19361797022242072,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.00238964992389591,
            "maximum_error_percentage_points": 0.02863013698629402,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.0023896499238965,
            "maximum_error_percentage_points": 0.028630136986301402,
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
      "maximum_error_percentage_points": 0.0049785248220782785,
      "metrics": {
        "da": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.004794520547945602,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.0,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.004955586472604523,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.004962007705479721,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.0049785248220782785,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.0045205479452086195,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
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
      "study_preparation_seconds": 0.37376579599731485,
      "weather_seconds": 0.22012594899933902,
      "metric_reduction_seconds": 0.3337679010001011,
      "write_seconds": 0.0524732359990594,
      "total_seconds": 0.6068576229990867,
      "cold_end_to_end_seconds": 0.9806234189964016,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.035450747000140836,
      "engine_upload_seconds": 0.013812038,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.026936186,
      "engine_annual_reduction_seconds": 0.013896341,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.026936186
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.37376579599731485,
      "weather_seconds": 0.2386278419980954,
      "metric_reduction_seconds": 0.2981526589974237,
      "write_seconds": 0.04856364599982044,
      "total_seconds": 0.5857990010008507,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.5857990010008507,
      "raw_export_seconds": 0.031543860997771844,
      "engine_upload_seconds": 0.014074883,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.3e-08,
      "engine_annual_reduction_seconds": 0.014087442,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.015479277997656027,
      "full": 0.0404800440010149
    }
  },
  "elapsed_seconds": 3.39056889800122,
  "result_class": "unstable_reference"
}
```
