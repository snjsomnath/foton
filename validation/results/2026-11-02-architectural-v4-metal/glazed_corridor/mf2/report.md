# Foton report

Status: **failed**

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
  "sky_density": 2,
  "status": "failed",
  "passed": false,
  "model_sha256": "1659d34e511112066d7c346748c85009a2f30d25bd4c9b7b205a76ff2579b640",
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
      "scene_fingerprint": 706269953697064074,
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
      "scene_fingerprint": 706269953697064074,
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
        "identifier": "glazed_corridor_corridor_grid",
        "bias_percent": 0.023381738820299657,
        "rms_normalized_error_percent": 0.6002616966062914,
        "absolute_error": {
          "p95": 4.6589411795139313e-07,
          "p99": 3.271352034062147e-05,
          "maximum": 8.967035682871938e-05
        },
        "worst_index": [
          10,
          355,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_office_grid",
        "bias_percent": -0.05260456054945142,
        "rms_normalized_error_percent": 1.0204583337733673,
        "absolute_error": {
          "p95": 0.0,
          "p99": 1.9874132703989744e-06,
          "maximum": 3.489520167931914e-05
        },
        "worst_index": [
          17,
          215,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_meeting_grid",
        "bias_percent": -0.988769369831759,
        "rms_normalized_error_percent": 3.4742097341224922,
        "absolute_error": {
          "p95": 0.0,
          "p99": 0.0,
          "maximum": 7.67746678320691e-06
        },
        "worst_index": [
          12,
          98,
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
        "identifier": "glazed_corridor_corridor_grid",
        "bias_percent": 0.05195230673818099,
        "rms_normalized_error_percent": 1.0393141818791185,
        "absolute_error": {
          "p95": 7.81866256147623e-05,
          "p99": 0.00014678214211016893,
          "maximum": 0.0007239729166030884
        },
        "worst_index": [
          1,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_office_grid",
        "bias_percent": 0.24126541921147837,
        "rms_normalized_error_percent": 2.580020231572475,
        "absolute_error": {
          "p95": 5.408681317931041e-06,
          "p99": 3.2350741093978286e-05,
          "maximum": 0.00022605806589126587
        },
        "worst_index": [
          23,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_meeting_grid",
        "bias_percent": 0.8910570683411271,
        "rms_normalized_error_percent": 7.720802212561664,
        "absolute_error": {
          "p95": 7.00809437148564e-07,
          "p99": 1.8647848492037156e-06,
          "maximum": 4.105299012735486e-05
        },
        "worst_index": [
          2,
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
        "identifier": "glazed_corridor_corridor_grid",
        "bias_percent": -0.040892203131264925,
        "rms_normalized_error_percent": 0.9163945917748559,
        "absolute_error": {
          "p95": 6.543053314089775e-05,
          "p99": 0.00012169079855084419,
          "maximum": 0.0009634047746658325
        },
        "worst_index": [
          7,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_office_grid",
        "bias_percent": -0.0798441560286261,
        "rms_normalized_error_percent": 2.2590786723441143,
        "absolute_error": {
          "p95": 4.749417712446302e-06,
          "p99": 2.787192352116108e-05,
          "maximum": 0.0002925209701061249
        },
        "worst_index": [
          17,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_meeting_grid",
        "bias_percent": -0.34849378993235686,
        "rms_normalized_error_percent": 6.338486017193666,
        "absolute_error": {
          "p95": 6.167722634842221e-07,
          "p99": 1.6498179320478812e-06,
          "maximum": 4.084056126885116e-05
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
            "identifier": "glazed_corridor_corridor_grid",
            "start_sensor_index": 0,
            "sensor_count": 18,
            "stages": {
              "direct": {
                "nmbe_percent": -0.008087207391360134,
                "cvrmse_percent": 14.839193148205252,
                "rms_normalized_rmse_percent": 5.242966499638805,
                "reference_energy": 11.029255646508204,
                "candidate_energy": 11.028363687730348,
                "relative_energy_error_percent": 0.008087207391360134,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.882852176204324e-05,
                  "p95": 0.00013300549471750855,
                  "p99": 0.00023751862681820057,
                  "maximum": 0.000500077789183706
                },
                "worst": {
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "sky_patch_index": 262,
                  "rgb_channel": 0,
                  "reference": 0.0032315581920556724,
                  "candidate": 0.0037316359812393785
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.008096961796736647,
                "cvrmse_percent": 66.5535804142474,
                "rms_normalized_rmse_percent": 2.96938913926536,
                "reference_energy": 3.3201280305402623,
                "candidate_energy": 3.3198592010420267,
                "relative_energy_error_percent": 0.008096961796736647,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 9.083686745725572e-05,
                  "p95": 0.0001707973424345255,
                  "p99": 0.0003182857180945575,
                  "maximum": 0.0007764352485537529
                },
                "worst": {
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.054566667415201664,
                  "candidate": 0.05534310266375542
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "start_sensor_index": 18,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.2871827649785246,
                "cvrmse_percent": 98.68992275168932,
                "rms_normalized_rmse_percent": 12.150169534132958,
                "reference_energy": 0.6243203576443648,
                "candidate_energy": 0.6261132981097717,
                "relative_energy_error_percent": 0.2871827649785246,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.28009225288406e-05,
                  "maximum": 0.0002555332175688818
                },
                "worst": {
                  "global_sensor_index": 50,
                  "local_sensor_index": 32,
                  "sky_patch_index": 96,
                  "rgb_channel": 0,
                  "reference": 0.0007511738658649847,
                  "candidate": 0.0004956406482961029
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.3922902006039929,
                "cvrmse_percent": 215.74518182731796,
                "rms_normalized_rmse_percent": 8.168726922470947,
                "reference_energy": 0.4441316302073357,
                "candidate_energy": 0.44587391507042184,
                "relative_energy_error_percent": 0.39229020060399283,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.7514264527562773e-06,
                  "p99": 6.980168109294027e-05,
                  "maximum": 0.0005960999988019466
                },
                "worst": {
                  "global_sensor_index": 41,
                  "local_sensor_index": 23,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.011204527458176017,
                  "candidate": 0.01060842745937407
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "start_sensor_index": 54,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -3.071211432413918,
                "cvrmse_percent": 903.5802192140119,
                "rms_normalized_rmse_percent": 21.14507707629169,
                "reference_energy": 0.00450615059617121,
                "candidate_energy": 0.004367757183899812,
                "relative_energy_error_percent": 3.071211432413918,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 4.1206063542631455e-05
                },
                "worst": {
                  "global_sensor_index": 60,
                  "local_sensor_index": 6,
                  "sky_patch_index": 37,
                  "rgb_channel": 0,
                  "reference": 7.558281868114136e-05,
                  "candidate": 3.437675513850991e-05
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.9068304127394536,
                "cvrmse_percent": 835.9477429572725,
                "rms_normalized_rmse_percent": 22.91876764573153,
                "reference_energy": 0.010655364259022804,
                "candidate_energy": 0.010751990342711792,
                "relative_energy_error_percent": 0.9068304127394538,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 8.010225087673462e-07,
                  "maximum": 9.88237516139634e-05
                },
                "worst": {
                  "global_sensor_index": 57,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0004901801075902767,
                  "candidate": 0.00039135635597631335
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 172.94783296529204,
            "full": 498.3537079533562
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 165.83962505683303,
            "full": 488.0166669609025
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 167.49250004068017,
            "full": 478.0148329446092
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 163.8610839145258,
            "full": 482.43066703435034
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 173.18904190324247,
            "full": 485.1019170600921
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 169.5947500411421,
            "full": 478.67887502070516
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 163.954040966928,
            "full": 488.0509169306606
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 165.4448329936713,
            "full": 491.18570797145367
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
            "identifier": "glazed_corridor_corridor_grid",
            "start_sensor_index": 0,
            "sensor_count": 18,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0012780249712792137,
                "cvrmse_percent": 12.607942195028572,
                "rms_normalized_rmse_percent": 4.4536440246686055,
                "reference_energy": 11.026279777780701,
                "candidate_energy": 11.026420696389664,
                "relative_energy_error_percent": 0.0012780249712792137,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.874427733942866e-05,
                  "p95": 0.00011047185398638248,
                  "p99": 0.00020956969819962978,
                  "maximum": 0.0003512974362820387
                },
                "worst": {
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "sky_patch_index": 364,
                  "rgb_channel": 0,
                  "reference": 0.004042614949867129,
                  "candidate": 0.0036913175135850906
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.005665245455064989,
                "cvrmse_percent": 36.48645230893468,
                "rms_normalized_rmse_percent": 2.062114702147036,
                "reference_energy": 5.640485153464098,
                "candidate_energy": 5.6408047007928985,
                "relative_energy_error_percent": 0.005665245455064991,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.326710355608611e-08,
                  "p90": 8.05185700301081e-05,
                  "p95": 0.00015902903396636248,
                  "p99": 0.0003023028839379549,
                  "maximum": 0.0009704194962978363
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05969488434493542,
                  "candidate": 0.05872446484863758
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "start_sensor_index": 18,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.33524795169771154,
                "cvrmse_percent": 86.54383375487726,
                "rms_normalized_rmse_percent": 10.705863189589236,
                "reference_energy": 0.6254366453097191,
                "candidate_energy": 0.6275334088522868,
                "relative_energy_error_percent": 0.33524795169771154,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.143384285271168e-05,
                  "maximum": 0.0002376608463237062
                },
                "worst": {
                  "global_sensor_index": 34,
                  "local_sensor_index": 16,
                  "sky_patch_index": 89,
                  "rgb_channel": 0,
                  "reference": 0.0007397267909254879,
                  "candidate": 0.0005020659446017817
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.15843618400617437,
                "cvrmse_percent": 91.97824729353577,
                "rms_normalized_rmse_percent": 4.985476085487164,
                "reference_energy": 0.9208541043952145,
                "candidate_energy": 0.9223130704984825,
                "relative_energy_error_percent": 0.15843618400617437,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.072757110407117e-06,
                  "p95": 7.92397440818604e-06,
                  "p99": 6.479075091192499e-05,
                  "maximum": 0.00048423768021166325
                },
                "worst": {
                  "global_sensor_index": 34,
                  "local_sensor_index": 16,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.008078968618065119,
                  "candidate": 0.0075947309378534555
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "start_sensor_index": 54,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 9.191805406856469,
                "cvrmse_percent": 1089.1255498260202,
                "rms_normalized_rmse_percent": 27.113713737716324,
                "reference_energy": 0.004159520129633165,
                "candidate_energy": 0.00454185512580807,
                "relative_energy_error_percent": 9.191805406856469,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 6.535481225000694e-05
                },
                "worst": {
                  "global_sensor_index": 55,
                  "local_sensor_index": 1,
                  "sky_patch_index": 96,
                  "rgb_channel": 0,
                  "reference": 0.00019151639571646228,
                  "candidate": 0.00025687120796646923
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -1.1212243268158928,
                "cvrmse_percent": 274.07721215036753,
                "rms_normalized_rmse_percent": 13.739553499880577,
                "reference_energy": 0.031814636554987175,
                "candidate_energy": 0.0314579231104446,
                "relative_energy_error_percent": 1.1212243268158928,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.498018880776518e-07,
                  "p95": 9.280724384552741e-07,
                  "p99": 2.9119741924432674e-06,
                  "maximum": 9.669335122453049e-05
                },
                "worst": {
                  "global_sensor_index": 55,
                  "local_sensor_index": 1,
                  "sky_patch_index": 96,
                  "rgb_channel": 0,
                  "reference": 3.516139986459166e-05,
                  "candidate": -6.153195135993883e-05
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 244.53312496189028,
            "full": 6619.6127500152215
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 246.10054201912135,
            "full": 6668.011541943997
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 255.1718750037253,
            "full": 6714.236667030491
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 253.16808302886784,
            "full": 6630.986667005345
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
            "identifier": "glazed_corridor_corridor_grid",
            "start_sensor_index": 0,
            "sensor_count": 18,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0007311086782722481,
                "cvrmse_percent": 11.823316464236475,
                "rms_normalized_rmse_percent": 4.175985910268436,
                "reference_energy": 11.023296214158108,
                "candidate_energy": 11.023376806433362,
                "relative_energy_error_percent": 0.000731108678272248,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.973460454493761e-05,
                  "p95": 0.00010843959171324968,
                  "p99": 0.00018976646242663264,
                  "maximum": 0.00039963540621101856
                },
                "worst": {
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "sky_patch_index": 362,
                  "rgb_channel": 0,
                  "reference": 0.003712380537763238,
                  "candidate": 0.0041120159439742565
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.07812112876622576,
                "cvrmse_percent": 34.41186966428013,
                "rms_normalized_rmse_percent": 1.9449523456773887,
                "reference_energy": 5.654526276098171,
                "candidate_energy": 5.6501088963449,
                "relative_energy_error_percent": 0.07812112876622576,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.4037375463167336e-08,
                  "p90": 7.62260751798749e-05,
                  "p95": 0.00015163607895374298,
                  "p99": 0.0002811020240187645,
                  "maximum": 0.0009962469339370728
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.08353259786963463,
                  "candidate": 0.08253635093569756
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "start_sensor_index": 18,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.13567381346593635,
                "cvrmse_percent": 82.8845085104867,
                "rms_normalized_rmse_percent": 10.208484196995313,
                "reference_energy": 0.6274680425851784,
                "candidate_energy": 0.626616732763523,
                "relative_energy_error_percent": 0.13567381346593638,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.0749990148469806e-05,
                  "maximum": 0.0002067600580630824
                },
                "worst": {
                  "global_sensor_index": 46,
                  "local_sensor_index": 28,
                  "sky_patch_index": 97,
                  "rgb_channel": 0,
                  "reference": 0.00041386189695913345,
                  "candidate": 0.0006206219550222158
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.3668267831456385,
                "cvrmse_percent": 94.18764628219475,
                "rms_normalized_rmse_percent": 5.109160253556747,
                "reference_energy": 0.9230681501225035,
                "candidate_energy": 0.9264542113238399,
                "relative_energy_error_percent": 0.36682678314563844,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.188218099443475e-06,
                  "p95": 7.813084721419727e-06,
                  "p99": 6.821528950240463e-05,
                  "maximum": 0.00030338484793901443
                },
                "worst": {
                  "global_sensor_index": 41,
                  "local_sensor_index": 23,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.015370475128293037,
                  "candidate": 0.015673859976232052
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "start_sensor_index": 54,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 6.878667868258566,
                "cvrmse_percent": 1150.0659872021981,
                "rms_normalized_rmse_percent": 25.244100681584392,
                "reference_energy": 0.0041940038372558774,
                "candidate_energy": 0.004482495431602729,
                "relative_energy_error_percent": 6.8786678682585665,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 6.843718210802763e-05
                },
                "worst": {
                  "global_sensor_index": 56,
                  "local_sensor_index": 2,
                  "sky_patch_index": 37,
                  "rgb_channel": 0,
                  "reference": 2.724289015532122e-05,
                  "candidate": 9.568007226334885e-05
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -4.007572434359223,
                "cvrmse_percent": 329.0279361928719,
                "rms_normalized_rmse_percent": 16.476334850912277,
                "reference_energy": 0.032623078827079155,
                "candidate_energy": 0.03131568531276585,
                "relative_energy_error_percent": 4.007572434359223,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.447278871249184e-07,
                  "p95": 8.413841889876039e-07,
                  "p99": 2.7806352065340434e-06,
                  "maximum": 0.00011513880599522963
                },
                "worst": {
                  "global_sensor_index": 63,
                  "local_sensor_index": 9,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0003638934576883912,
                  "candidate": 0.0002487546516931616
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 250.12533296830952,
            "full": 7079.154124949127
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 242.24699998740107,
            "full": 7049.316457938403
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 245.88204105384648,
            "full": 7152.2689160192385
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 246.41487502958626,
            "full": 7080.321166082285
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
            "identifier": "glazed_corridor_corridor_grid",
            "start_sensor_index": 0,
            "sensor_count": 18,
            "stages": {
              "direct": {
                "nmbe_percent": 0.006696372899450527,
                "cvrmse_percent": 6.907322520893301,
                "rms_normalized_rmse_percent": 2.4407515192516436,
                "reference_energy": 11.023963065906287,
                "candidate_energy": 11.024701271581478,
                "relative_energy_error_percent": 0.006696372899450526,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.242696402594447e-05,
                  "p95": 5.750951822847128e-05,
                  "p99": 0.00011312455171719193,
                  "maximum": 0.00024034950183704495
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 144,
                  "rgb_channel": 0,
                  "reference": 0.0014900155365467072,
                  "candidate": 0.001730365038383752
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.06442679063670166,
                "cvrmse_percent": 20.00196840809815,
                "rms_normalized_rmse_percent": 1.130562235876227,
                "reference_energy": 5.642685094536365,
                "candidate_energy": 5.64632049544851,
                "relative_energy_error_percent": 0.06442679063670166,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.000000058430487e-08,
                  "p90": 4.430171975400299e-05,
                  "p95": 8.774318848736584e-05,
                  "p99": 0.00016859360039234161,
                  "maximum": 0.00043830275535583496
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.06959613785147667,
                  "candidate": 0.0700344406068325
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "start_sensor_index": 18,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.1340308010135656,
                "cvrmse_percent": 47.68508164384377,
                "rms_normalized_rmse_percent": 5.88830177573863,
                "reference_energy": 0.6262578952507738,
                "candidate_energy": 0.6270972737241891,
                "relative_energy_error_percent": 0.1340308010135656,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.1461448341142386e-05,
                  "maximum": 8.407412678934634e-05
                },
                "worst": {
                  "global_sensor_index": 33,
                  "local_sensor_index": 15,
                  "sky_patch_index": 90,
                  "rgb_channel": 0,
                  "reference": 0.0006803402793593705,
                  "candidate": 0.0005962661525700241
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.32260922210180126,
                "cvrmse_percent": 59.43722392496916,
                "rms_normalized_rmse_percent": 3.2305435465080814,
                "reference_energy": 0.9253796375888328,
                "candidate_energy": 0.922394277538519,
                "relative_energy_error_percent": 0.32260922210180126,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.9282849482115156e-06,
                  "p95": 5.6466960813850164e-06,
                  "p99": 4.069498390890658e-05,
                  "maximum": 0.00033475039526820183
                },
                "worst": {
                  "global_sensor_index": 41,
                  "local_sensor_index": 23,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.01578108500689268,
                  "candidate": 0.01544633461162448
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "start_sensor_index": 54,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 3.291823996698404,
                "cvrmse_percent": 431.49076183985136,
                "rms_normalized_rmse_percent": 10.19746395741209,
                "reference_energy": 0.004264577011099391,
                "candidate_energy": 0.004404959380508444,
                "relative_energy_error_percent": 3.291823996698405,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 2.0412197045516223e-05
                },
                "worst": {
                  "global_sensor_index": 60,
                  "local_sensor_index": 6,
                  "sky_patch_index": 37,
                  "rgb_channel": 0,
                  "reference": 8.183489262592047e-05,
                  "candidate": 6.142269558040425e-05
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -1.7490522191905506,
                "cvrmse_percent": 173.96791571649277,
                "rms_normalized_rmse_percent": 8.567372404633298,
                "reference_energy": 0.032127295077994944,
                "candidate_energy": 0.03156537191046738,
                "relative_energy_error_percent": 1.7490522191905506,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.066450233291119e-07,
                  "p95": 7.110249811148606e-07,
                  "p99": 1.9468920875453932e-06,
                  "maximum": 6.546909571625292e-05
                },
                "worst": {
                  "global_sensor_index": 57,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0007800387393217534,
                  "candidate": 0.0007145696436055005
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 426.61358299665153,
            "full": 12229.870208073407
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 423.5287909395993,
            "full": 12510.385333909653
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 416.21200006920844,
            "full": 12302.750707953237
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 412.3632499249652,
            "full": 12473.562416969799
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 15173.322916030884,
      "worker_pool_size": 12,
      "invocation_count": 6
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 59181.05341703631,
      "worker_pool_size": 12,
      "invocation_count": 6
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": false,
    "matrix_shape": [
      90,
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
        "identifier": "glazed_corridor_corridor_grid",
        "full_identifier": "glazed_corridor_corridor_grid",
        "start_sensor_index": 0,
        "sensor_count": 18,
        "stages": {
          "direct": {
            "nmbe_percent": -0.46142203283769384,
            "cvrmse_percent": 3.2836729050592424,
            "rms_normalized_rmse_percent": 1.1633011190808238,
            "reference_energy": 11.02544066799382,
            "candidate_energy": 10.974566855534249,
            "relative_energy_error_percent": 0.4614220328376939,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.1918170861899853e-07,
              "p95": 6.418791599571705e-06,
              "p99": 6.387694884324446e-05,
              "maximum": 0.00013667577877640724
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 181,
              "rgb_channel": 0,
              "reference": 0.00013667577877640724,
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
            "nmbe_percent": -0.182253162279998,
            "cvrmse_percent": 36.45405710446109,
            "rms_normalized_rmse_percent": 2.060109644806866,
            "reference_energy": 5.643394379438419,
            "candidate_energy": 5.633109114721961,
            "relative_energy_error_percent": 0.18225316227999797,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 7.93009093058572e-07,
              "p90": 6.603878864552826e-05,
              "p95": 9.842388681136072e-05,
              "p99": 0.00016894587315618992,
              "maximum": 0.0033123046159744263
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07767532765865326,
              "candidate": 0.07436302304267883,
              "position": [
                1.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.36690672744674124,
            "cvrmse_percent": 12.157728939972996,
            "rms_normalized_rmse_percent": 2.029372494726136,
            "reference_energy": 16.66883504743224,
            "candidate_energy": 16.60767597025621,
            "relative_energy_error_percent": 0.36690672744674124,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.0000000116860974e-07,
              "p90": 6.271947859204374e-05,
              "p95": 9.026401676237583e-05,
              "p99": 0.0001689250930212438,
              "maximum": 0.0033123046159744263
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07767532765865326,
              "candidate": 0.07436302304267883,
              "position": [
                1.5,
                2.5,
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
            "nmbe_percent": -0.08401741961934546,
            "cvrmse_percent": 7.244081231339007,
            "rms_normalized_rmse_percent": 0.8940349738851646,
            "reference_energy": 0.626456997744242,
            "candidate_energy": 0.6259306647397125,
            "relative_energy_error_percent": 0.08401741961934546,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.1658961511784582e-06,
              "maximum": 4.912434087600559e-05
            },
            "worst": {
              "global_sensor_index": 49,
              "local_sensor_index": 31,
              "sky_patch_index": 86,
              "rgb_channel": 0,
              "reference": 4.912434087600559e-05,
              "candidate": 0.0,
              "position": [
                5.5,
                7.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.6910722120856719,
            "cvrmse_percent": 103.65462049606145,
            "rms_normalized_rmse_percent": 5.631706627288709,
            "reference_energy": 0.924107541091141,
            "candidate_energy": 0.917721290664872,
            "relative_energy_error_percent": 0.6910722120856719,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.1187382824573445e-05,
              "p95": 1.8077994582199608e-05,
              "p99": 4.483059274207335e-05,
              "maximum": 0.000625348649919033
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 27,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.004694128409028053,
              "candidate": 0.00406877975910902,
              "position": [
                4.5,
                5.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.44581075199814507,
            "cvrmse_percent": 61.69700223966267,
            "rms_normalized_rmse_percent": 5.6244848740754705,
            "reference_energy": 1.550564538835383,
            "candidate_energy": 1.5436519554045844,
            "relative_energy_error_percent": 0.44581075199814507,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.1125019409519205e-05,
              "p95": 1.804891394385777e-05,
              "p99": 4.46247540821787e-05,
              "maximum": 0.000625348649919033
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 27,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.004694128409028053,
              "candidate": 0.00406877975910902,
              "position": [
                4.5,
                5.5,
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
            "nmbe_percent": -0.03640350793459441,
            "cvrmse_percent": 77.2188377553826,
            "rms_normalized_rmse_percent": 1.8444680473091102,
            "reference_energy": 0.004285219445932853,
            "candidate_energy": 0.004283659475731838,
            "relative_energy_error_percent": 0.036403507934594403,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 4.8080582928378135e-06
            },
            "worst": {
              "global_sensor_index": 66,
              "local_sensor_index": 12,
              "sky_patch_index": 98,
              "rgb_channel": 0,
              "reference": 3.326051592011936e-05,
              "candidate": 3.8068574212957174e-05,
              "position": [
                8.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 1.710871325676232,
            "cvrmse_percent": 440.59075710416033,
            "rms_normalized_rmse_percent": 21.90320274570779,
            "reference_energy": 0.031895882246057994,
            "candidate_energy": 0.032441579749477256,
            "relative_energy_error_percent": 1.7108713256762322,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.087764066047386e-07,
              "p95": 1.1509428645695152e-06,
              "p99": 6.0142556321807206e-06,
              "maximum": 0.0001886058016680181
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0007473041769117117,
              "candidate": 0.0009359099785797298,
              "position": [
                6.5,
                5.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 1.5039274863725316,
            "cvrmse_percent": 388.72786303220306,
            "rms_normalized_rmse_percent": 21.921238107708795,
            "reference_energy": 0.03618110169199085,
            "candidate_energy": 0.036725239225209094,
            "relative_energy_error_percent": 1.5039274863725316,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.087764066047386e-07,
              "p95": 1.1521731266839197e-06,
              "p99": 6.0142556321807206e-06,
              "maximum": 0.0001886058016680181
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0007473041769117117,
              "candidate": 0.0009359099785797298,
              "position": [
                6.5,
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
  "one_bounce_diagnostic": {
    "schema_version": 1,
    "passed": false,
    "matrix_shape": [
      90,
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
        "identifier": "glazed_corridor_corridor_grid",
        "full_identifier": "glazed_corridor_corridor_grid",
        "start_sensor_index": 0,
        "sensor_count": 18,
        "stages": {
          "direct": {
            "nmbe_percent": -0.46142203283769384,
            "cvrmse_percent": 3.2836729050592424,
            "rms_normalized_rmse_percent": 1.1633011190808238,
            "reference_energy": 11.02544066799382,
            "candidate_energy": 10.974566855534249,
            "relative_energy_error_percent": 0.4614220328376939,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.1918170861899853e-07,
              "p95": 6.418791599571705e-06,
              "p99": 6.387694884324446e-05,
              "maximum": 0.00013667577877640724
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 181,
              "rgb_channel": 0,
              "reference": 0.00013667577877640724,
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
            "nmbe_percent": 69.50028708683398,
            "cvrmse_percent": 804.3767093921247,
            "rms_normalized_rmse_percent": 35.92927450387643,
            "reference_energy": 3.323362580404453,
            "candidate_energy": 5.633109114721961,
            "relative_energy_error_percent": 69.50028708683398,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0001417272724211216,
              "p95": 0.00019904505461454391,
              "p99": 0.00032455986365675926,
              "maximum": 0.025893613696098328
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04498261958360672,
              "candidate": 0.07087623327970505,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 15.74258621261735,
            "cvrmse_percent": 186.28427542892837,
            "rms_normalized_rmse_percent": 35.925524101025104,
            "reference_energy": 14.348803248398273,
            "candidate_energy": 16.60767597025621,
            "relative_energy_error_percent": 15.742586212617352,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00014110957272350788,
              "p95": 0.00019907282330677845,
              "p99": 0.0003239322977606207,
              "maximum": 0.025893613696098328
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04498261958360672,
              "candidate": 0.07087623327970505,
              "position": [
                5.5,
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
            "nmbe_percent": -0.08401741961934546,
            "cvrmse_percent": 7.244081231339007,
            "rms_normalized_rmse_percent": 0.8940349738851646,
            "reference_energy": 0.626456997744242,
            "candidate_energy": 0.6259306647397125,
            "relative_energy_error_percent": 0.08401741961934546,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.1658961511784582e-06,
              "maximum": 4.912434087600559e-05
            },
            "worst": {
              "global_sensor_index": 49,
              "local_sensor_index": 31,
              "sky_patch_index": 86,
              "rgb_channel": 0,
              "reference": 4.912434087600559e-05,
              "candidate": 0.0,
              "position": [
                5.5,
                7.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 106.80455705804262,
            "cvrmse_percent": 1265.8563905035758,
            "rms_normalized_rmse_percent": 47.96613011913446,
            "reference_energy": 0.443762605486155,
            "candidate_energy": 0.917721290664872,
            "relative_energy_error_percent": 106.80455705804262,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.7227999705937867e-05,
              "p95": 2.803999996103812e-05,
              "p99": 7.33186025172472e-05,
              "maximum": 0.004405955784022808
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01091950386762619,
              "candidate": 0.015325459651648998,
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
            "nmbe_percent": 44.236935180888004,
            "cvrmse_percent": 524.851231633563,
            "rms_normalized_rmse_percent": 47.96325652633605,
            "reference_energy": 1.070219603230397,
            "candidate_energy": 1.5436519554045844,
            "relative_energy_error_percent": 44.236935180888,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.7018964877024845e-05,
              "p95": 2.7976767341897357e-05,
              "p99": 7.341025047935545e-05,
              "maximum": 0.004405955784022808
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 17,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01091950386762619,
              "candidate": 0.015325459651648998,
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
            "nmbe_percent": -0.03640350793459441,
            "cvrmse_percent": 77.2188377553826,
            "rms_normalized_rmse_percent": 1.8444680473091102,
            "reference_energy": 0.004285219445932853,
            "candidate_energy": 0.004283659475731838,
            "relative_energy_error_percent": 0.036403507934594403,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 4.8080582928378135e-06
            },
            "worst": {
              "global_sensor_index": 66,
              "local_sensor_index": 12,
              "sky_patch_index": 98,
              "rgb_channel": 0,
              "reference": 3.326051592011936e-05,
              "candidate": 3.8068574212957174e-05,
              "position": [
                8.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 198.85167471042203,
            "cvrmse_percent": 3356.7097203756157,
            "rms_normalized_rmse_percent": 96.26199123133466,
            "reference_energy": 0.010855411729217224,
            "candidate_energy": 0.032441579749477256,
            "relative_energy_error_percent": 198.85167471042203,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.6000000136482413e-07,
              "p99": 7.209405339381192e-06,
              "maximum": 0.0004951417504344136
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00044076822814531624,
              "candidate": 0.0009359099785797298,
              "position": [
                6.5,
                5.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 142.5608206181343,
            "cvrmse_percent": 2406.629928504482,
            "rms_normalized_rmse_percent": 96.26048556178415,
            "reference_energy": 0.015140631175150077,
            "candidate_energy": 0.036725239225209094,
            "relative_energy_error_percent": 142.56082061813427,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.6000000136482413e-07,
              "p99": 7.209405339381192e-06,
              "maximum": 0.0004951417504344136
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00044076822814531624,
              "candidate": 0.0009359099785797298,
              "position": [
                6.5,
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
      "bias_percent": -0.1417451541701316,
      "rms_normalized_error_percent": 0.4109616279002827,
      "absolute_error": {
        "p95": 0.15262838472584708,
        "p99": 0.41213750910415514,
        "maximum": 0.4729175065940012
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 9.109022944852741,
      "rms_normalized_to_uniform_percent": 0.4109616279002827
    },
    "overcast": {
      "bias_percent": -0.11226964938871042,
      "rms_normalized_error_percent": 0.28403763067280746,
      "absolute_error": {
        "p95": 0.08838973045349116,
        "p99": 0.18987308502197262,
        "maximum": 0.23475265502929688
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 5.943142890930176,
      "rms_normalized_to_uniform_percent": 0.19827757701676924
    },
    "horizon": {
      "bias_percent": 0.04665350178702169,
      "rms_normalized_error_percent": 2.073492870958149,
      "absolute_error": {
        "p95": 0.08304060737283182,
        "p99": 0.11426198658040554,
        "maximum": 0.12578839754464832
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.9907004468965308,
      "rms_normalized_to_uniform_percent": 0.15796368524204876
    },
    "north": {
      "bias_percent": -93.52905570468741,
      "rms_normalized_error_percent": 101.08953414536533,
      "absolute_error": {
        "p95": 4.986920422354046e-05,
        "p99": 0.0001153700642316834,
        "maximum": 0.00028195622144266963
      },
      "worst_index": [
        62
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 1.0309971912647597e-05,
      "rms_normalized_to_uniform_percent": 0.0001538562900335976
    },
    "east": {
      "bias_percent": -0.042348342059805484,
      "rms_normalized_error_percent": 0.5552101472257513,
      "absolute_error": {
        "p95": 0.07314949631690978,
        "p99": 0.08643606185913084,
        "maximum": 0.1195363998413086
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.726973295211792,
      "rms_normalized_to_uniform_percent": 0.11385128283606365
    },
    "south": {
      "bias_percent": -0.1996357862909059,
      "rms_normalized_error_percent": 0.5769711309917016,
      "absolute_error": {
        "p95": 0.15708961486816403,
        "p99": 0.39006189346313475,
        "maximum": 0.4000892639160156
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 6.216495037078857,
      "rms_normalized_to_uniform_percent": 0.3712137365279875
    },
    "west": {
      "bias_percent": -0.2299202796760935,
      "rms_normalized_error_percent": 0.5028500434944235,
      "absolute_error": {
        "p95": 0.050048077106475825,
        "p99": 0.10253466606140137,
        "maximum": 0.10919666290283203
      },
      "worst_index": [
        13
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.7462410926818848,
      "rms_normalized_to_uniform_percent": 0.10393798027036176
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
          "nmbe_percent": -0.17837989569945237,
          "cvrmse_percent": 2.480216671686388,
          "absolute_error_percentiles_lux": {
            "p50": 13.029541015625,
            "p90": 145.2708496093751,
            "p95": 212.4438964843751,
            "p99": 371.4840295410156
          },
          "maximum_absolute_error_lux": 1036.7421875,
          "worst": {
            "sensor_index": 6,
            "position": [
              2.5,
              2.5,
              0.75
            ],
            "hour_of_year": 6828.5,
            "foton_lux": 19531.9375,
            "radiance_lux": 20568.6796875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.09108828006088426,
            "maximum_error_percentage_points": 0.30095890410959214,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.0315596721524282,
            "maximum_error_percentage_points": 0.12303164660657728,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.017876712328767357,
            "maximum_error_percentage_points": 0.08383561643835513,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.2857077625570772,
            "maximum_error_percentage_points": 0.7416438356164434,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.29076103500761025,
            "maximum_error_percentage_points": 0.7421917808219174,
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
          "nmbe_percent": -0.2717481273261151,
          "cvrmse_percent": 14.916723735458216,
          "absolute_error_percentiles_lux": {
            "p50": 2.047962188720703,
            "p90": 25.679496002197265,
            "p95": 39.308194351196285,
            "p99": 77.33766098022431
          },
          "maximum_absolute_error_lux": 316.50146484375,
          "worst": {
            "sensor_index": 17,
            "position": [
              2.5,
              3.5,
              0.75
            ],
            "hour_of_year": 2868.5,
            "foton_lux": 1033.5076904296875,
            "radiance_lux": 717.0062255859375
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.37913622526636215,
            "maximum_error_percentage_points": 2.6856164383561634,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.7338145438394934,
            "maximum_error_percentage_points": 2.485540728696975,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 1.9170547945205476,
            "maximum_error_percentage_points": 5.53328767123287,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 1.917994672754947,
            "maximum_error_percentage_points": 5.533287671232877,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0045167427701674305,
            "maximum_error_percentage_points": 0.051643835616438594,
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
          "nmbe_percent": -0.11246940896517106,
          "cvrmse_percent": 109.77133629481241,
          "absolute_error_percentiles_lux": {
            "p50": 0.17599144577980042,
            "p90": 1.8133410155773164,
            "p95": 3.3910953044891334,
            "p99": 10.345153267383568
          },
          "maximum_absolute_error_lux": 87.1195068359375,
          "worst": {
            "sensor_index": 25,
            "position": [
              10.5,
              7.5,
              0.75
            ],
            "hour_of_year": 1357.5,
            "foton_lux": 92.82786560058594,
            "radiance_lux": 5.7083587646484375
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.00014459665144596654,
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.11743548001673935,
            "maximum_error_percentage_points": 0.5104121351764337,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.002568493150685056,
            "maximum_error_percentage_points": 0.03095890410959612,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.0025684931506849335,
            "maximum_error_percentage_points": 0.030958904109589014,
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
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
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
        "cda": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.004807630565068166,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.0048540507277401446,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.004722281678082307,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.0035616438356164126,
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
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.003561643835624295,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
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
      "study_preparation_seconds": 0.012093500001356006,
      "weather_seconds": 0.11789262492675334,
      "metric_reduction_seconds": 0.08855020895134658,
      "write_seconds": 0.06712841696571559,
      "total_seconds": 0.273783165961504,
      "cold_end_to_end_seconds": 0.28587666596286,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.02913366607390344,
      "engine_upload_seconds": 0.000784292,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.03510649979580194,
      "engine_annual_reduction_seconds": 0.004005124908871949,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.03510649979580194
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.012093500001356006,
      "weather_seconds": 0.12631575006525964,
      "metric_reduction_seconds": 0.046679125051014125,
      "write_seconds": 0.06045970902778208,
      "total_seconds": 0.2336420409847051,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.2336420409847051,
      "raw_export_seconds": 0.02419495803769678,
      "engine_upload_seconds": 8.3667e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0036554166581481695,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01667475001886487,
      "full": 0.025737582938745618
    }
  },
  "elapsed_seconds": 191.48903329204768,
  "result_class": "accuracy_failure"
}
```
