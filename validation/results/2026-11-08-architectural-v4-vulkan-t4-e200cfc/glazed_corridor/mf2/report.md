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
  "model_sha256": "efa494d3764ae4094e8d29856ad05610958d60eb59789ebb0d71085dae86d7e3",
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
      "scene_fingerprint": 706269953697064074,
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
      "scene_fingerprint": 706269953697064074,
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
    "model_sha256": "270810b9b663bc6b0d9aa1af68fdff739164431696bd930ad5e7a63a75a1755c",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "94ed5584a1f4c854071651885dd6e15bc9326094d0a19791950cc11f1dfe41d3",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 8.967035682871938e-05,
          "p95": 4.677567631006241e-07,
          "p99": 3.271352034062147e-05
        },
        "bias_percent": 0.0233909624570281,
        "identifier": "glazed_corridor_corridor_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.6002617812356064,
        "worst_index": [
          10,
          355,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 3.489520167931914e-05,
          "p95": 0.0,
          "p99": 1.9874132703989744e-06
        },
        "bias_percent": -0.05300659065101828,
        "identifier": "glazed_corridor_office_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0203818254958257,
        "worst_index": [
          17,
          215,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 7.67746678320691e-06,
          "p95": 0.0,
          "p99": 0.0
        },
        "bias_percent": -0.988769369831759,
        "identifier": "glazed_corridor_meeting_grid",
        "passed": true,
        "rms_normalized_error_percent": 3.4742097341224922,
        "worst_index": [
          12,
          98,
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
          "maximum": 0.0008144080638885498,
          "p95": 7.972866296768188e-05,
          "p99": 0.0001466765534132719
        },
        "bias_percent": 0.02454252355928191,
        "identifier": "glazed_corridor_corridor_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0785621539511,
        "worst_index": [
          3,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00024414295330643654,
          "p95": 5.477281774801668e-06,
          "p99": 3.6612487747333944e-05
        },
        "bias_percent": 0.15447356222809588,
        "identifier": "glazed_corridor_office_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.7888871955963035,
        "worst_index": [
          10,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 8.657283615320921e-05,
          "p95": 6.847362410411506e-07,
          "p99": 1.900255028886022e-06
        },
        "bias_percent": 0.7584200727340452,
        "identifier": "glazed_corridor_meeting_grid",
        "passed": true,
        "rms_normalized_error_percent": 8.936110043717676,
        "worst_index": [
          3,
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
          "maximum": 0.0005277469754219055,
          "p95": 6.570550613105297e-05,
          "p99": 0.00012131384573876858
        },
        "bias_percent": 0.021234496217716656,
        "identifier": "glazed_corridor_corridor_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8987541451867437,
        "worst_index": [
          6,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0001763300970196724,
          "p95": 4.599716703523882e-06,
          "p99": 2.6273075491189957e-05
        },
        "bias_percent": 0.11279450423732813,
        "identifier": "glazed_corridor_office_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.1738299880328453,
        "worst_index": [
          17,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 8.290947880595922e-05,
          "p95": 5.751238916218426e-07,
          "p99": 1.6420772617209423e-06
        },
        "bias_percent": -0.7016667721756824,
        "identifier": "glazed_corridor_meeting_grid",
        "passed": true,
        "rms_normalized_error_percent": 8.875216597057095,
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
            "identifier": "glazed_corridor_corridor_grid",
            "sensor_count": 18,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004479877825360745,
                  "p50": 0.0,
                  "p90": 5.49189280718565e-05,
                  "p95": 0.0001110364064516034,
                  "p99": 0.0002105872263200581
                },
                "candidate_energy": 11.029256732301292,
                "cvrmse_percent": 12.836366348945775,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.020388701460787167,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.0270084684646,
                "relative_energy_error_percent": 0.020388701460787167,
                "rms_normalized_rmse_percent": 4.534686884905135,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0020535342628136277,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.0016055464802775532,
                  "rgb_channel": 0,
                  "sky_patch_index": 149
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007372703403234482,
                  "p50": 0.0,
                  "p90": 9.241598309017718e-05,
                  "p95": 0.0001772399409674108,
                  "p99": 0.0003404820163268596
                },
                "candidate_energy": 3.324974608400593,
                "cvrmse_percent": 69.11161432357159,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.04551498024862838,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.3234619353571446,
                "relative_energy_error_percent": 0.045514980248628385,
                "rms_normalized_rmse_percent": 3.085094259954635,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.045452662743628025,
                  "global_sensor_index": 0,
                  "local_sensor_index": 0,
                  "reference": 0.04471539240330458,
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
                  "maximum": 0.0002401376550551504,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.278275264368858e-05
                },
                "candidate_energy": 0.62778556265323,
                "cvrmse_percent": 100.04415922011968,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.3355973488571758,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6256857777708547,
                "relative_energy_error_percent": 0.33559734885717574,
                "rms_normalized_rmse_percent": 12.344601129041562,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00045193135156296194,
                  "global_sensor_index": 32,
                  "local_sensor_index": 14,
                  "reference": 0.0006920690066181123,
                  "rgb_channel": 0,
                  "sky_patch_index": 90
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007398047018796206,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.7697817611406208e-06,
                  "p99": 7.606693682760124e-05
                },
                "candidate_energy": 0.4469829316628111,
                "cvrmse_percent": 245.91525645833343,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.9756375212614339,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.44266413427565077,
                "relative_energy_error_percent": 0.9756375212614339,
                "rms_normalized_rmse_percent": 9.305012446203689,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.010534037835896015,
                  "global_sensor_index": 41,
                  "local_sensor_index": 23,
                  "reference": 0.011273842537775636,
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
                  "maximum": 4.106514188606525e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.004159639320732822,
                "cvrmse_percent": 941.9626273679281,
                "energy_difference_negligible": true,
                "nmbe_percent": 1.4218290945727716,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.004101325481769891,
                "relative_energy_error_percent": 1.4218290945727712,
                "rms_normalized_rmse_percent": 22.169343113554024,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 9.608377877157182e-05,
                  "global_sensor_index": 56,
                  "local_sensor_index": 2,
                  "reference": 5.501863688550657e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 37
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 8.541023817087989e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.505510051127203e-07
                },
                "candidate_energy": 0.01127914778983552,
                "cvrmse_percent": 829.5823138532749,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 2.33836578145025,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.011021426523385003,
                "relative_energy_error_percent": 2.33836578145025,
                "rms_normalized_rmse_percent": 24.069089924045695,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -5.8701161833596416e-05,
                  "global_sensor_index": 55,
                  "local_sensor_index": 1,
                  "reference": 2.6709076337283477e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 96
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 174.6128749800846,
            "full": 511.38837495818734
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 176.47133290302008,
            "full": 502.11325008422136
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 168.97429095115513,
            "full": 506.50787504855543
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 180.77391595579684,
            "full": 514.6291670389473
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 173.35391696542501,
            "full": 502.44979199487716
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 170.80358299426734,
            "full": 494.5015830453485
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 173.27520798426121,
            "full": 501.7806669929996
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 177.0636250730604,
            "full": 503.25695890933275
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
            "identifier": "glazed_corridor_corridor_grid",
            "sensor_count": 18,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003573969006538391,
                  "p50": 0.0,
                  "p90": 5.2505580242723227e-05,
                  "p95": 0.00010539605136727914,
                  "p99": 0.00020005597616545856
                },
                "candidate_energy": 11.025143760804895,
                "cvrmse_percent": 11.969262736392979,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.04265315317693845,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.029848338912075,
                "relative_energy_error_percent": 0.04265315317693845,
                "rms_normalized_rmse_percent": 4.230007161752847,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003913359949365258,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.003555963048711419,
                  "rgb_channel": 0,
                  "sky_patch_index": 356
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0012937523424625397,
                  "p50": 5.791807922150838e-08,
                  "p90": 8.312670979648829e-05,
                  "p95": 0.00015850986528676003,
                  "p99": 0.00030283204978331923
                },
                "candidate_energy": 5.643627796816048,
                "cvrmse_percent": 37.02096260123544,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.06461426168985285,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.639983563077337,
                "relative_energy_error_percent": 0.06461426168985286,
                "rms_normalized_rmse_percent": 2.0897385799385932,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07738173007965088,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.07867548242211342,
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
                  "maximum": 0.00018287728016730398,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.2162282625213265e-05
                },
                "candidate_energy": 0.6270019222482688,
                "cvrmse_percent": 86.27809153949501,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.11334483599020077,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6277134029753597,
                "relative_energy_error_percent": 0.11334483599020079,
                "rms_normalized_rmse_percent": 10.619744691732873,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0005472400080179796,
                  "global_sensor_index": 38,
                  "local_sensor_index": 20,
                  "reference": 0.0007301172881852835,
                  "rgb_channel": 0,
                  "sky_patch_index": 92
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00036447448655962944,
                  "p50": 0.0,
                  "p90": 4.152158498982329e-06,
                  "p95": 7.849339908716502e-06,
                  "p99": 7.14851776137948e-05
                },
                "candidate_energy": 0.9196564585771014,
                "cvrmse_percent": 94.49561981166593,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1552797869335254,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9182306320081608,
                "relative_energy_error_percent": 0.1552797869335254,
                "rms_normalized_rmse_percent": 5.105628561711114,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.015529875177890062,
                  "global_sensor_index": 41,
                  "local_sensor_index": 23,
                  "reference": 0.015894349664449692,
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
                  "maximum": 7.466106035280973e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.004340113202033535,
                "cvrmse_percent": 1159.5102264963944,
                "energy_difference_negligible": true,
                "nmbe_percent": 2.9957860027797913,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.004213874538436357,
                "relative_energy_error_percent": 2.995786002779792,
                "rms_normalized_rmse_percent": 28.799194447854198,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0002646316570462659,
                  "global_sensor_index": 56,
                  "local_sensor_index": 2,
                  "reference": 0.00018997059669345617,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00013042113278061152,
                  "p50": 0.0,
                  "p90": 3.5166928071817235e-07,
                  "p95": 8.981434689303569e-07,
                  "p99": 2.782717047011829e-06
                },
                "candidate_energy": 0.031152488576406512,
                "cvrmse_percent": 316.49580763283427,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -3.978023635895265,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.0324430820485091,
                "relative_energy_error_percent": 3.9780236358952656,
                "rms_normalized_rmse_percent": 15.336307174477312,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0006709371227771044,
                  "global_sensor_index": 57,
                  "local_sensor_index": 3,
                  "reference": 0.0008013582555577159,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 250.77112508006394,
            "full": 6728.860375005752
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 260.93308301642537,
            "full": 6760.396333993413
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 260.80987497698516,
            "full": 6733.369542052969
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 257.4528750265017,
            "full": 6754.624791909009
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
            "identifier": "glazed_corridor_corridor_grid",
            "sensor_count": 18,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003723949193954468,
                  "p50": 0.0,
                  "p90": 5.5127544328570366e-05,
                  "p95": 0.00010440504411235452,
                  "p99": 0.00019587844144552946
                },
                "candidate_energy": 11.029196514249861,
                "cvrmse_percent": 11.873527575013322,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.04771492289365561,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.023936451472196,
                "relative_energy_error_percent": 0.047714922893655615,
                "rms_normalized_rmse_percent": 4.195165920800013,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004149901447817683,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.0037775065284222364,
                  "rgb_channel": 0,
                  "sky_patch_index": 358
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007712692022323608,
                  "p50": 6.259022633514633e-08,
                  "p90": 8.666451321914792e-05,
                  "p95": 0.00015915895346552134,
                  "p99": 0.00029567594174295664
                },
                "candidate_energy": 5.645918677634128,
                "cvrmse_percent": 35.82362714535474,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.032141401040517055,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.647733938448987,
                "relative_energy_error_percent": 0.03214140104051705,
                "rms_normalized_rmse_percent": 2.0247949877741274,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05900990590453148,
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "reference": 0.05978117510676384,
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
                  "maximum": 0.00018286664271727204,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.079914651811123e-05
                },
                "candidate_energy": 0.625778801860065,
                "cvrmse_percent": 81.41982202980925,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.036802183848043214,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6255485863192689,
                "relative_energy_error_percent": 0.036802183848043214,
                "rms_normalized_rmse_percent": 10.019874396380676,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00039416609797626734,
                  "global_sensor_index": 36,
                  "local_sensor_index": 18,
                  "reference": 0.0005770327406935394,
                  "rgb_channel": 0,
                  "sky_patch_index": 91
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00046023447066545486,
                  "p50": 0.0,
                  "p90": 4.242311308644279e-06,
                  "p95": 7.710979843977839e-06,
                  "p99": 6.492117336165393e-05
                },
                "candidate_energy": 0.9216093025942094,
                "cvrmse_percent": 95.06144633201087,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.3065275053065318,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9244429745821776,
                "relative_energy_error_percent": 0.3065275053065318,
                "rms_normalized_rmse_percent": 5.152151069177905,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.015361415222287178,
                  "global_sensor_index": 35,
                  "local_sensor_index": 17,
                  "reference": 0.015821649692952633,
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
                  "maximum": 6.144416875031311e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.004159426608111971,
                "cvrmse_percent": 1308.4070405253576,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.03752734550045218,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.004157866271270905,
                "relative_energy_error_percent": 0.03752734550045218,
                "rms_normalized_rmse_percent": 29.389263391378837,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00010919049964286387,
                  "global_sensor_index": 61,
                  "local_sensor_index": 7,
                  "reference": 4.774633089255076e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 6.932665291969897e-05,
                  "p50": 0.0,
                  "p90": 3.3877545035920823e-07,
                  "p95": 8.521632857139139e-07,
                  "p99": 2.812140554198095e-06
                },
                "candidate_energy": 0.03208558403625972,
                "cvrmse_percent": 221.56588833117564,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.6449960237871322,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.03229387826700858,
                "relative_energy_error_percent": 0.6449960237871323,
                "rms_normalized_rmse_percent": 10.776280081458466,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -4.7122764044615906e-05,
                  "global_sensor_index": 61,
                  "local_sensor_index": 7,
                  "reference": 2.2203888875083067e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 260.0407919380814,
            "full": 7146.271000034176
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 251.53854198288172,
            "full": 7102.057624957524
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 252.1070409566164,
            "full": 7163.049500086345
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 255.97604201175272,
            "full": 7045.079625095241
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
            "identifier": "glazed_corridor_corridor_grid",
            "sensor_count": 18,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002026500878855586,
                  "p50": 0.0,
                  "p90": 3.0158029403537512e-05,
                  "p95": 5.806551780551672e-05,
                  "p99": 0.00010807742364704609
                },
                "candidate_energy": 11.025200844432959,
                "cvrmse_percent": 6.625730717112588,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.016605939312992604,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.023370310248993,
                "relative_energy_error_percent": 0.016605939312992604,
                "rms_normalized_rmse_percent": 2.3412313773404967,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003468493465334177,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.0036711435532197356,
                  "rgb_channel": 0,
                  "sky_patch_index": 318
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007241107523441315,
                  "p50": 5.000000058430487e-08,
                  "p90": 4.6384986490011215e-05,
                  "p95": 8.618365973234177e-05,
                  "p99": 0.00016459685866720974
                },
                "candidate_energy": 5.654119192034933,
                "cvrmse_percent": 20.288793463787986,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.05207624547931448,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.651176271607262,
                "relative_energy_error_percent": 0.052076245479314484,
                "rms_normalized_rmse_percent": 1.147270193206927,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05984524078667164,
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "reference": 0.05912113003432751,
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
                  "maximum": 0.00011931332119274884,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.0844105165451765e-05
                },
                "candidate_energy": 0.626001247979957,
                "cvrmse_percent": 46.59353184634739,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.14105432927325226,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6268854971132214,
                "relative_energy_error_percent": 0.14105432927325226,
                "rms_normalized_rmse_percent": 5.747800155929288,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0005332367145456374,
                  "global_sensor_index": 24,
                  "local_sensor_index": 6,
                  "reference": 0.0004139233933528885,
                  "rgb_channel": 0,
                  "sky_patch_index": 90
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0001807553635444492,
                  "p50": 0.0,
                  "p90": 2.910663079092065e-06,
                  "p95": 5.296048811942455e-06,
                  "p99": 3.506988286972046e-05
                },
                "candidate_energy": 0.9247645913377305,
                "cvrmse_percent": 51.23717186828798,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.16708648135322807,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.9232220121625296,
                "relative_energy_error_percent": 0.1670864813532281,
                "rms_normalized_rmse_percent": 2.781820129608898,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -6.704343832097948e-05,
                  "global_sensor_index": 32,
                  "local_sensor_index": 14,
                  "reference": 0.00011371192522346973,
                  "rgb_channel": 0,
                  "sky_patch_index": 88
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
                  "maximum": 2.0051058527315035e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0
                },
                "candidate_energy": 0.004315138279935127,
                "cvrmse_percent": 508.6093878183743,
                "energy_difference_negligible": true,
                "nmbe_percent": 1.7515070089747968,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.0042408593315030885,
                "relative_energy_error_percent": 1.7515070089747968,
                "rms_normalized_rmse_percent": 12.189119762805992,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 7.606897997902706e-05,
                  "global_sensor_index": 55,
                  "local_sensor_index": 1,
                  "reference": 9.61200385063421e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 36
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 4.563240509014577e-05,
                  "p50": 0.0,
                  "p90": 3.1217594838040064e-07,
                  "p95": 7.138780233617581e-07,
                  "p99": 1.9599990537244594e-06
                },
                "candidate_energy": 0.031706901913214125,
                "cvrmse_percent": 160.0284546479824,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.6793196175460585,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.03192376632048877,
                "relative_energy_error_percent": 0.6793196175460585,
                "rms_normalized_rmse_percent": 8.060006155429344,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0003478466533124447,
                  "global_sensor_index": 63,
                  "local_sensor_index": 9,
                  "reference": 0.0003022142482222989,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 430.8753339573741,
            "full": 12609.89454202354
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 414.50049995910376,
            "full": 12562.210834003054
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 422.67362505663186,
            "full": 12882.22799997311
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 423.31745801493526,
            "full": 12905.986667028628
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
    "/content/suite-vulkan/glazed_corridor/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 15393.565999926068,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/glazed_corridor/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 60594.17133301031,
      "invocation_count": 6,
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
            "nmbe_percent": -0.4614289220384379,
            "cvrmse_percent": 3.2837002390291343,
            "rms_normalized_rmse_percent": 1.1633108628530415,
            "reference_energy": 11.025441250186844,
            "candidate_energy": 10.974566675476126,
            "relative_energy_error_percent": 0.46142892203843794,
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
            "nmbe_percent": -0.6270622724494027,
            "cvrmse_percent": 28.464990614296877,
            "rms_normalized_rmse_percent": 1.6085860956466749,
            "reference_energy": 5.6514920233392765,
            "candidate_energy": 5.6160536490304285,
            "relative_energy_error_percent": 0.6270622724494027,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.508166628307663e-07,
              "p90": 2.7973734177066945e-05,
              "p95": 5.2746618166565895e-05,
              "p99": 0.00010280629066983238,
              "maximum": 0.0016357079148292542
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.08343245834112167,
              "candidate": 0.08179675042629242,
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
            "nmbe_percent": -0.5175588797047257,
            "cvrmse_percent": 9.41363490127831,
            "rms_normalized_rmse_percent": 1.5697976991495628,
            "reference_energy": 16.67693327352612,
            "candidate_energy": 16.590620324506553,
            "relative_energy_error_percent": 0.5175588797047364,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 8.780292581889171e-08,
              "p90": 2.3263506591320038e-05,
              "p95": 4.141454701311886e-05,
              "p99": 9.025121107697487e-05,
              "maximum": 0.0016357079148292542
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.08343245834112167,
              "candidate": 0.08179675042629242,
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
            "nmbe_percent": -0.08409660438304968,
            "cvrmse_percent": 7.2442012724129174,
            "rms_normalized_rmse_percent": 0.8940501972851158,
            "reference_energy": 0.6264574536384657,
            "candidate_energy": 0.6259306241920513,
            "relative_energy_error_percent": 0.08409660438304968,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.1505471775308251e-06,
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
            "nmbe_percent": -0.043693870660686314,
            "cvrmse_percent": 42.003352762727154,
            "rms_normalized_rmse_percent": 2.282458663402736,
            "reference_energy": 0.923979220869402,
            "candidate_energy": 0.9235754985837037,
            "relative_energy_error_percent": 0.043693870660686314,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.0713196792930976e-06,
              "p95": 5.351032086764462e-06,
              "p99": 1.8250724679091945e-05,
              "maximum": 0.00030486471951007843
            },
            "worst": {
              "global_sensor_index": 42,
              "local_sensor_index": 24,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.004874785430729389,
              "candidate": 0.005179650150239468,
              "position": [
                4.5,
                8.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.06001868682628605,
            "cvrmse_percent": 24.911778375539946,
            "rms_normalized_rmse_percent": 2.2715145499742837,
            "reference_energy": 1.5504366745078677,
            "candidate_energy": 1.549506122775755,
            "relative_energy_error_percent": 0.06001868682628604,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.0681218959216513e-06,
              "p95": 5.316936949384399e-06,
              "p99": 1.7868791474029422e-05,
              "maximum": 0.00030486471951007843
            },
            "worst": {
              "global_sensor_index": 42,
              "local_sensor_index": 24,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.004874785430729389,
              "candidate": 0.005179650150239468,
              "position": [
                4.5,
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
            "nmbe_percent": -0.036412175282988644,
            "cvrmse_percent": 77.21890628276569,
            "rms_normalized_rmse_percent": 1.8444696841709451,
            "reference_energy": 0.004285219445932853,
            "candidate_energy": 0.004283659104316939,
            "relative_energy_error_percent": 0.03641217528298864,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 4.808054654859006e-06
            },
            "worst": {
              "global_sensor_index": 66,
              "local_sensor_index": 12,
              "sky_patch_index": 98,
              "rgb_channel": 0,
              "reference": 3.326051592011936e-05,
              "candidate": 3.8068570574978366e-05,
              "position": [
                8.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.3061051756945194,
            "cvrmse_percent": 134.95617765859285,
            "rms_normalized_rmse_percent": 6.752398947634877,
            "reference_energy": 0.03180811349572643,
            "candidate_energy": 0.03190547977742764,
            "relative_energy_error_percent": 0.30610517569451945,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.566414454425685e-07,
              "p95": 7.058523578962195e-07,
              "p99": 1.8208781966677634e-06,
              "maximum": 4.654895747080445e-05
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0007398110465146601,
              "candidate": 0.0007863600039854646,
              "position": [
                6.5,
                5.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.26543943791544833,
            "cvrmse_percent": 118.93233859297108,
            "rms_normalized_rmse_percent": 6.752340870215658,
            "reference_energy": 0.036093332941659284,
            "candidate_energy": 0.036189138881744576,
            "relative_energy_error_percent": 0.26543943791544833,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.5784155407725497e-07,
              "p95": 7.080472528286919e-07,
              "p99": 1.8208781966677634e-06,
              "maximum": 4.654895747080445e-05
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0007398110465146601,
              "candidate": 0.0007863600039854646,
              "position": [
                6.5,
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
            "nmbe_percent": -0.4614289220384379,
            "cvrmse_percent": 3.2837002390291343,
            "rms_normalized_rmse_percent": 1.1633108628530415,
            "reference_energy": 11.025441250186844,
            "candidate_energy": 10.974566675476126,
            "relative_energy_error_percent": 0.46142892203843794,
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
            "nmbe_percent": 68.80692133119375,
            "cvrmse_percent": 792.6828775739943,
            "rms_normalized_rmse_percent": 35.40556077409982,
            "reference_energy": 3.3269095868479894,
            "candidate_energy": 5.6160536490304285,
            "relative_energy_error_percent": 68.80692133119375,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.0561920618101794e-06,
              "p90": 0.00013446633238345385,
              "p95": 0.0001806700020097196,
              "p99": 0.0002680043107829988,
              "maximum": 0.025043781846761703
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04508402571082115,
              "candidate": 0.07012780755758286,
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
            "nmbe_percent": 15.595141958877466,
            "cvrmse_percent": 183.7264721338417,
            "rms_normalized_rmse_percent": 35.40183548037705,
            "reference_energy": 14.352350837034834,
            "candidate_energy": 16.590620324506553,
            "relative_energy_error_percent": 15.595141958877454,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00013295573080540635,
              "p95": 0.00018003606237471104,
              "p99": 0.0002676979638636112,
              "maximum": 0.025043781846761703
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04508402571082115,
              "candidate": 0.07012780755758286,
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
            "nmbe_percent": -0.08409660438304968,
            "cvrmse_percent": 7.2442012724129174,
            "rms_normalized_rmse_percent": 0.8940501972851158,
            "reference_energy": 0.6264574536384657,
            "candidate_energy": 0.6259306241920513,
            "relative_energy_error_percent": 0.08409660438304968,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.1505471775308251e-06,
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
            "nmbe_percent": 107.49761239929659,
            "cvrmse_percent": 1292.2960052914045,
            "rms_normalized_rmse_percent": 49.01336746165614,
            "reference_energy": 0.44510174739091823,
            "candidate_energy": 0.9235754985837037,
            "relative_energy_error_percent": 107.49761239929659,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2630000128410757e-05,
              "p95": 2.4169999960577115e-05,
              "p99": 5.610312655335292e-05,
              "maximum": 0.0048225997015833855
            },
            "worst": {
              "global_sensor_index": 41,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.010903940536081791,
              "candidate": 0.015726540237665176,
              "position": [
                3.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 44.60294132953508,
            "cvrmse_percent": 536.776111360138,
            "rms_normalized_rmse_percent": 49.01201865737419,
            "reference_energy": 1.071559201029384,
            "candidate_energy": 1.549506122775755,
            "relative_energy_error_percent": 44.60294132953508,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2608376124489974e-05,
              "p95": 2.4060000214376487e-05,
              "p99": 5.67562528885901e-05,
              "maximum": 0.0048225997015833855
            },
            "worst": {
              "global_sensor_index": 41,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.010903940536081791,
              "candidate": 0.015726540237665176,
              "position": [
                3.5,
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
            "nmbe_percent": -0.036412175282988644,
            "cvrmse_percent": 77.21890628276569,
            "rms_normalized_rmse_percent": 1.8444696841709451,
            "reference_energy": 0.004285219445932853,
            "candidate_energy": 0.004283659104316939,
            "relative_energy_error_percent": 0.03641217528298864,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 4.808054654859006e-06
            },
            "worst": {
              "global_sensor_index": 66,
              "local_sensor_index": 12,
              "sky_patch_index": 98,
              "rgb_channel": 0,
              "reference": 3.326051592011936e-05,
              "candidate": 3.8068570574978366e-05,
              "position": [
                8.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 190.16719900930636,
            "cvrmse_percent": 2822.634008650823,
            "rms_normalized_rmse_percent": 82.00374474032157,
            "reference_energy": 0.010995550112610886,
            "candidate_energy": 0.03190547977742764,
            "relative_energy_error_percent": 190.16719900930636,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.0000000467443897e-07,
              "p95": 1.050000037139398e-06,
              "p99": 3.533115886966698e-06,
              "maximum": 0.00036813304177485406
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0004182269622106105,
              "candidate": 0.0007863600039854646,
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
            "nmbe_percent": 136.82798659515555,
            "cvrmse_percent": 2030.941675893967,
            "rms_normalized_rmse_percent": 81.99829668584293,
            "reference_energy": 0.015280769558543739,
            "candidate_energy": 0.036189138881744576,
            "relative_energy_error_percent": 136.82798659515555,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.0000000467443897e-07,
              "p95": 1.040000029206567e-06,
              "p99": 3.533115886966698e-06,
              "maximum": 0.00036813304177485406
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0004182269622106105,
              "candidate": 0.0007863600039854646,
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
      "bias_percent": -0.22106499931701787,
      "rms_normalized_error_percent": 0.3733221396630993,
      "absolute_error": {
        "p95": 0.1688453871999267,
        "p99": 0.39503500020055055,
        "maximum": 0.49057607645344703
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.110527500231026,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.3733221396630993
    },
    "overcast": {
      "bias_percent": -0.18643828741357707,
      "rms_normalized_error_percent": 0.2648858912607975,
      "absolute_error": {
        "p95": 0.07557315826416011,
        "p99": 0.2042045402526855,
        "maximum": 0.2570981979370117
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.943963527679443,
      "reference_fraction_of_uniform": 0.6524280905723572,
      "rms_normalized_to_uniform_percent": 0.18490497203377004
    },
    "horizon": {
      "bias_percent": 0.23205146139460092,
      "rms_normalized_error_percent": 1.6232852812363585,
      "absolute_error": {
        "p95": 0.06602246771327068,
        "p99": 0.09951201613617805,
        "maximum": 0.10552905506637789
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.9901093895891361,
      "reference_fraction_of_uniform": 0.10867750408129812,
      "rms_normalized_to_uniform_percent": 0.12353838210581718
    },
    "north": {
      "bias_percent": -89.23508046534121,
      "rms_normalized_error_percent": 99.60614086333918,
      "absolute_error": {
        "p95": 1.3713220459976576e-05,
        "p99": 0.0002311271772487088,
        "maximum": 0.0003977157757617533
      },
      "worst_index": [
        76
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.1521859960339498e-05,
      "reference_fraction_of_uniform": 1.2646754612433142e-06,
      "rms_normalized_to_uniform_percent": 0.00021728555830045904
    },
    "east": {
      "bias_percent": -0.1821413560207447,
      "rms_normalized_error_percent": 0.2669318824770829,
      "absolute_error": {
        "p95": 0.029041957855224603,
        "p99": 0.05851305484771729,
        "maximum": 0.05961942672729492
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.7275162935256958,
      "reference_fraction_of_uniform": 0.1896176040172577,
      "rms_normalized_to_uniform_percent": 0.05474470457472387
    },
    "south": {
      "bias_percent": -0.2898443202274544,
      "rms_normalized_error_percent": 0.5401115466607962,
      "absolute_error": {
        "p95": 0.15190734863281236,
        "p99": 0.37077995300292965,
        "maximum": 0.4411735534667969
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.21759557723999,
      "reference_fraction_of_uniform": 0.682462751865387,
      "rms_normalized_to_uniform_percent": 0.3474903293107861
    },
    "west": {
      "bias_percent": -0.1935449774498777,
      "rms_normalized_error_percent": 0.2827827086425074,
      "absolute_error": {
        "p95": 0.029915535449981663,
        "p99": 0.050485596656799296,
        "maximum": 0.08576345443725586
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.746212124824524,
      "reference_fraction_of_uniform": 0.19166971743106842,
      "rms_normalized_to_uniform_percent": 0.058423729668560034
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
          "nmbe_percent": -0.2559470969730226,
          "cvrmse_percent": 1.368702748949943,
          "absolute_error_percentiles_lux": {
            "p50": 6.20867919921875,
            "p90": 56.251074218750006,
            "p95": 90.56171875000007,
            "p99": 211.28968261718754
          },
          "maximum_absolute_error_lux": 942.06640625,
          "worst": {
            "sensor_index": 6,
            "position": [
              2.5,
              2.5,
              0.75
            ],
            "hour_of_year": 1356.5,
            "foton_lux": 20045.34765625,
            "radiance_lux": 20987.4140625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.06869863013698563,
            "maximum_error_percentage_points": 0.2515068493150636,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.02379160538955776,
            "maximum_error_percentage_points": 0.09432401696298598,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.014452054794520879,
            "maximum_error_percentage_points": 0.051643835616438594,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.13237442922374537,
            "maximum_error_percentage_points": 0.2473972602739707,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.13876712328767116,
            "maximum_error_percentage_points": 0.29863013698630425,
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
          "nmbe_percent": -0.36512756083833653,
          "cvrmse_percent": 5.035556870202872,
          "absolute_error_percentiles_lux": {
            "p50": 0.7635550498962402,
            "p90": 7.690740966796878,
            "p95": 11.994320297241194,
            "p99": 25.574889831542915
          },
          "maximum_absolute_error_lux": 133.076171875,
          "worst": {
            "sensor_index": 17,
            "position": [
              2.5,
              3.5,
              0.75
            ],
            "hour_of_year": 827.5,
            "foton_lux": 5397.0830078125,
            "radiance_lux": 5530.1591796875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.1553006088280061,
            "maximum_error_percentage_points": 0.9884931506849313,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.3490304993300896,
            "maximum_error_percentage_points": 1.0401717580508176,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.6792579908675792,
            "maximum_error_percentage_points": 3.3956164383561713,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.6766818873668188,
            "maximum_error_percentage_points": 3.3956164383561642,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0031659056316590533,
            "maximum_error_percentage_points": 0.03205479452054805,
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
          "nmbe_percent": 0.2544411023664025,
          "cvrmse_percent": 32.17435097974691,
          "absolute_error_percentiles_lux": {
            "p50": 0.06703159213066101,
            "p90": 0.7793360471725479,
            "p95": 1.3159945011138916,
            "p99": 2.999763832092284
          },
          "maximum_absolute_error_lux": 16.854843139648438,
          "worst": {
            "sensor_index": 6,
            "position": [
              7.5,
              8.5,
              0.75
            ],
            "hour_of_year": 638.5,
            "foton_lux": 195.08731079101562,
            "radiance_lux": 178.2324676513672
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
            "mean_absolute_error_percentage_points": 0.03036050032433641,
            "maximum_error_percentage_points": 0.09125111802408803,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.003759512937595133,
            "maximum_error_percentage_points": 0.07863013698629118,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.0037595129375951283,
            "maximum_error_percentage_points": 0.07863013698630139,
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
      "maximum_error_percentage_points": 0.004984599074272289,
      "metrics": {
        "da": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
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
            "maximum_error_percentage_points": 0.004711579623275952,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.0048297035530815435,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.004984599074272289,
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
            "maximum_error_percentage_points": 0.004931506849302991,
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
            "maximum_error_percentage_points": 0.004246575342467196,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
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
      "study_preparation_seconds": 0.3515437529999872,
      "weather_seconds": 0.2439948999999615,
      "metric_reduction_seconds": 0.5440118420001454,
      "write_seconds": 0.014767158999802632,
      "total_seconds": 0.8032089379998979,
      "cold_end_to_end_seconds": 1.154752690999885,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0032195899998441746,
      "engine_upload_seconds": 0.061476389,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.089702389,
      "engine_annual_reduction_seconds": 0.011292229,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.089702389
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3515437529999872,
      "weather_seconds": 0.24693678199992064,
      "metric_reduction_seconds": 0.4727684350000345,
      "write_seconds": 0.01666065100016567,
      "total_seconds": 0.7366913949999798,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.7366913949999798,
      "raw_export_seconds": 0.003901469999618712,
      "engine_upload_seconds": 0.063516423,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5e-08,
      "engine_annual_reduction_seconds": 0.010139445,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.03692104299989296,
      "full": 0.11855814299997292
    }
  },
  "elapsed_seconds": 6.295120052999664,
  "result_class": "accuracy_failure"
}
```
