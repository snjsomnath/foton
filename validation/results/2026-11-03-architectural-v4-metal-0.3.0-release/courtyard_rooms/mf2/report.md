# Foton report

Status: **passed**

```json
{
  "scene": "courtyard_rooms",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "courtyard_rooms",
    "category": "connections",
    "question": "Do four inward-facing rooms shade one another beneath a pergola?",
    "interactions": [
      "multiroom_context",
      "courtyard",
      "combined_shading"
    ],
    "room_count": 4,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 4,
    "apertures": 4,
    "shades": 4,
    "sensors": 112,
    "floor_area": 112.0,
    "aperture_area": 17.999999999999996
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "0318bf1fe42a53217dac4d6f17974a6d981e3bb1d9ac49a8c1fa7882c02a161c",
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
      "scene_fingerprint": 16353448696249269853,
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
      "scene_fingerprint": 16353448696249269853,
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
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/foton-references-corpus4-2026-11-03",
    "model_sha256": "57a33891f1556d93b76c7c5a3f7778438334be0f4fdd009692a04f2c9d658b9f",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "581a959e80175fed89f7d9c2cf231ee7b8790a487c3adad0958a5f167ca70cf1",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.000219903071410954,
          "p95": 2.225817434009452e-06,
          "p99": 5.3780851885676384e-05
        },
        "bias_percent": -0.06178660567835731,
        "identifier": "courtyard_rooms_west_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.005478911746854,
        "worst_index": [
          20,
          257,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00020035728812217712,
          "p95": 1.8526833628129107e-06,
          "p99": 4.403468687087163e-05
        },
        "bias_percent": -0.038773132578713614,
        "identifier": "courtyard_rooms_east_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.7126260037326528,
        "worst_index": [
          20,
          281,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00014028436271473765,
          "p95": 6.941612809896469e-06,
          "p99": 5.37758693099015e-05
        },
        "bias_percent": -0.029120648353555694,
        "identifier": "courtyard_rooms_north_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.7911551601294353,
        "worst_index": [
          11,
          543,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0001625253353267908,
          "p95": 6.831385235273046e-06,
          "p99": 5.762645887443718e-05
        },
        "bias_percent": 0.14528336103197517,
        "identifier": "courtyard_rooms_south_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.8407748934768098,
        "worst_index": [
          14,
          285,
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
          "maximum": 0.0007588118314743042,
          "p95": 2.665119695848255e-05,
          "p99": 9.930603438988267e-05
        },
        "bias_percent": 0.14895011308282669,
        "identifier": "courtyard_rooms_west_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.4682414283558247,
        "worst_index": [
          19,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0004695504903793335,
          "p95": 2.6515607351029728e-05,
          "p99": 9.607685962691856e-05
        },
        "bias_percent": 0.027405222137722094,
        "identifier": "courtyard_rooms_east_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.3508199354924375,
        "worst_index": [
          23,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0009326599538326263,
          "p95": 3.616389585658908e-05,
          "p99": 0.00011980285635217875
        },
        "bias_percent": 0.06405468821876067,
        "identifier": "courtyard_rooms_north_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.427521407484758,
        "worst_index": [
          11,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0009758993983268738,
          "p95": 3.4229597076773643e-05,
          "p99": 0.00011345311067998345
        },
        "bias_percent": 0.13634718017992167,
        "identifier": "courtyard_rooms_south_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.475691056221564,
        "worst_index": [
          9,
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
          "maximum": 0.0005502291023731232,
          "p95": 2.2792358140577468e-05,
          "p99": 8.281097398139505e-05
        },
        "bias_percent": -0.04646783721658075,
        "identifier": "courtyard_rooms_west_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1356910588441214,
        "worst_index": [
          27,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0006952658295631409,
          "p95": 2.2686901502311216e-05,
          "p99": 7.978760870173554e-05
        },
        "bias_percent": 0.004503286159499922,
        "identifier": "courtyard_rooms_east_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1343055546931091,
        "worst_index": [
          4,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0008973926305770874,
          "p95": 2.9488835025404114e-05,
          "p99": 9.869927307590803e-05
        },
        "bias_percent": 0.007090869153030828,
        "identifier": "courtyard_rooms_north_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1809800943253455,
        "worst_index": [
          11,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00038580596446990967,
          "p95": 2.9867514967918396e-05,
          "p99": 9.555309661663997e-05
        },
        "bias_percent": 0.05483111444786064,
        "identifier": "courtyard_rooms_south_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1415851524950527,
        "worst_index": [
          12,
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
            "identifier": "courtyard_rooms_west_grid",
            "sensor_count": 32,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00043821928557008505,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.259501488879304e-05,
                  "p99": 0.00015714094139184344
                },
                "candidate_energy": 5.726185990972176,
                "cvrmse_percent": 27.312083329059515,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.06727266288368836,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.722336422881341,
                "relative_energy_error_percent": 0.06727266288368836,
                "rms_normalized_rmse_percent": 5.451200536237399,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0018173313001170754,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.0013791120145469904,
                  "rgb_channel": 0,
                  "sky_patch_index": 189
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010173819027841091,
                  "p50": 0.0,
                  "p90": 2.3086477995093446e-05,
                  "p95": 4.6087424854590596e-05,
                  "p99": 0.00022552354890649265
                },
                "candidate_energy": 2.3953873297296564,
                "cvrmse_percent": 100.08270004612102,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.013954929634718753,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.395721651000297,
                "relative_energy_error_percent": 0.013954929634718753,
                "rms_normalized_rmse_percent": 3.8096072295158447,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.017663630191236734,
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "reference": 0.018681012094020844,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "sensor_count": 32,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004705397295765579,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1916035075264458e-05,
                  "p99": 0.00014518230207613594
                },
                "candidate_energy": 5.729087613968197,
                "cvrmse_percent": 26.33162970774562,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.19087911440037558,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.718172816336491,
                "relative_energy_error_percent": 0.19087911440037555,
                "rms_normalized_rmse_percent": 5.244049132554999,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0023312107659876347,
                  "global_sensor_index": 34,
                  "local_sensor_index": 2,
                  "reference": 0.0018606710364110768,
                  "rgb_channel": 0,
                  "sky_patch_index": 273
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007033562287688255,
                  "p50": 0.0,
                  "p90": 2.257996402477147e-05,
                  "p95": 4.448209970178073e-05,
                  "p99": 0.00022956032116780962
                },
                "candidate_energy": 2.4039334747275376,
                "cvrmse_percent": 96.7372320518214,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.6628115633730757,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.419973337841295,
                "relative_energy_error_percent": 0.6628115633730757,
                "rms_normalized_rmse_percent": 3.69820276504077,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.031995007768273354,
                  "global_sensor_index": 51,
                  "local_sensor_index": 19,
                  "reference": 0.03269836399704218,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 32
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003963109920732677,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.4391199480742216e-05,
                  "p99": 0.00018010000567301145
                },
                "candidate_energy": 5.358611808744598,
                "cvrmse_percent": 24.98573234048482,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.1424966582679851,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.350986831325599,
                "relative_energy_error_percent": 0.1424966582679851,
                "rms_normalized_rmse_percent": 5.597947782857931,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002077115757856518,
                  "global_sensor_index": 78,
                  "local_sensor_index": 14,
                  "reference": 0.0016808047657832503,
                  "rgb_channel": 0,
                  "sky_patch_index": 210
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001168854534626007,
                  "p50": 8.139657268202427e-07,
                  "p90": 2.5991835514105333e-05,
                  "p95": 6.467429921030998e-05,
                  "p99": 0.0002544521033996713
                },
                "candidate_energy": 2.2587526940781792,
                "cvrmse_percent": 89.98957273815718,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.3787559386758844,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.2673403804190126,
                "relative_energy_error_percent": 0.3787559386758844,
                "rms_normalized_rmse_percent": 3.7430861086001204,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04556958470493555,
                  "global_sensor_index": 79,
                  "local_sensor_index": 15,
                  "reference": 0.04673843923956156,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 64
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004727232444565743,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.279339009372052e-05,
                  "p99": 0.00017025259512593036
                },
                "candidate_energy": 5.352821255491897,
                "cvrmse_percent": 23.820622155270083,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.09770237364211003,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.358056203583876,
                "relative_energy_error_percent": 0.09770237364211003,
                "rms_normalized_rmse_percent": 5.316899528497009,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0014672255201730877,
                  "global_sensor_index": 100,
                  "local_sensor_index": 12,
                  "reference": 0.001939948764629662,
                  "rgb_channel": 0,
                  "sky_patch_index": 332
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006204902310855687,
                  "p50": 1.0595968547022494e-06,
                  "p90": 2.694278009585105e-05,
                  "p95": 6.822968134656549e-05,
                  "p99": 0.000261093392236939
                },
                "candidate_energy": 2.2066707208490044,
                "cvrmse_percent": 92.31978547452034,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.7391772708882473,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.1904791965049046,
                "relative_energy_error_percent": 0.7391772708882473,
                "rms_normalized_rmse_percent": 3.825441516402272,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0004853952268604189,
                  "global_sensor_index": 94,
                  "local_sensor_index": 6,
                  "reference": -0.00013509500422514975,
                  "rgb_channel": 0,
                  "sky_patch_index": 122
                }
              }
            },
            "start_sensor_index": 88
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 209.61708400864154,
            "full": 564.8762499913573
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 206.95224998053163,
            "full": 560.037708026357
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 192.63016700278968,
            "full": 564.2640000442043
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 207.55708310753107,
            "full": 567.8284589666873
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 201.17083296645433,
            "full": 587.5351250870153
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 196.3109999196604,
            "full": 563.5636250954121
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 200.31083293724805,
            "full": 566.3389579858631
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 194.90891695022583,
            "full": 555.916209006682
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
            "identifier": "courtyard_rooms_west_grid",
            "sensor_count": 32,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003330204635858536,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.152941015083341e-05,
                  "p99": 0.00013094455513055358
                },
                "candidate_energy": 5.727298805413795,
                "cvrmse_percent": 22.640568801689234,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.042628796884008155,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.724858367168558,
                "relative_energy_error_percent": 0.04262879688400816,
                "rms_normalized_rmse_percent": 4.517926132948928,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004157746909186244,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.0038247264456003904,
                  "rgb_channel": 0,
                  "sky_patch_index": 348
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007262062281370163,
                  "p50": 4.476065782910155e-06,
                  "p90": 2.300665801158175e-05,
                  "p95": 4.2547918923219145e-05,
                  "p99": 0.00019753095759369844
                },
                "candidate_energy": 4.379909332502034,
                "cvrmse_percent": 47.46824391375968,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1264753455805889,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.374376824296508,
                "relative_energy_error_percent": 0.1264753455805889,
                "rms_normalized_rmse_percent": 2.488351807232109,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04051143117249012,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.039785224944353104,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "sensor_count": 32,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00037298048846423626,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.0849789143539763e-05,
                  "p99": 0.00013011226488742928
                },
                "candidate_energy": 5.7306856424657155,
                "cvrmse_percent": 22.442621896187674,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.08498118018161463,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.725819773247338,
                "relative_energy_error_percent": 0.08498118018161463,
                "rms_normalized_rmse_percent": 4.478910751860241,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0014664935297332704,
                  "global_sensor_index": 58,
                  "local_sensor_index": 26,
                  "reference": 0.0018394740181975067,
                  "rgb_channel": 0,
                  "sky_patch_index": 164
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006116210133768618,
                  "p50": 4.561525656754384e-06,
                  "p90": 2.2781105144531466e-05,
                  "p95": 4.1940180278743344e-05,
                  "p99": 0.0001921937864972262
                },
                "candidate_energy": 4.381525346641201,
                "cvrmse_percent": 45.732174850116984,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.33261308320389876,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.396147508411119,
                "relative_energy_error_percent": 0.33261308320389876,
                "rms_normalized_rmse_percent": 2.401084846967027,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0006538290181197226,
                  "global_sensor_index": 58,
                  "local_sensor_index": 26,
                  "reference": 4.2208004742860794e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 164
                }
              }
            },
            "start_sensor_index": 32
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00041051500011235476,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.590659434848931e-05,
                  "p99": 0.00014032591134309768
                },
                "candidate_energy": 5.354486229970462,
                "cvrmse_percent": 21.278128785288157,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.08499388595517407,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.359041087240442,
                "relative_energy_error_percent": 0.08499388595517407,
                "rms_normalized_rmse_percent": 4.770389038728271,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0023997159441933036,
                  "global_sensor_index": 74,
                  "local_sensor_index": 10,
                  "reference": 0.001989200944080949,
                  "rgb_channel": 0,
                  "sky_patch_index": 267
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006236711051315069,
                  "p50": 6.1138850071529305e-06,
                  "p90": 2.882901435441454e-05,
                  "p95": 5.7076511438935995e-05,
                  "p99": 0.00021145608916412994
                },
                "candidate_energy": 4.138898342030732,
                "cvrmse_percent": 42.744055700582095,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.5436827868611793,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.116517544721958,
                "relative_energy_error_percent": 0.5436827868611793,
                "rms_normalized_rmse_percent": 2.3472951863379863,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00010203546844422817,
                  "global_sensor_index": 74,
                  "local_sensor_index": 10,
                  "reference": 0.0005216356366872787,
                  "rgb_channel": 0,
                  "sky_patch_index": 267
                }
              }
            },
            "start_sensor_index": 64
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004066105466336012,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.162604454904795e-05,
                  "p99": 0.0001599850249476727
                },
                "candidate_energy": 5.353694528542803,
                "cvrmse_percent": 22.159160646398284,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.051228514371067325,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.3564385524364155,
                "relative_energy_error_percent": 0.051228514371067325,
                "rms_normalized_rmse_percent": 4.950056751024249,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004030595533549786,
                  "global_sensor_index": 96,
                  "local_sensor_index": 8,
                  "reference": 0.0036239849869161844,
                  "rgb_channel": 0,
                  "sky_patch_index": 290
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008548200130462646,
                  "p50": 6.226700634215376e-06,
                  "p90": 2.940667513939843e-05,
                  "p95": 6.255693733692169e-05,
                  "p99": 0.00021854182123206507
                },
                "candidate_energy": 4.062143217009002,
                "cvrmse_percent": 45.09159955075113,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.09608381151030337,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.066050032858488,
                "relative_energy_error_percent": 0.09608381151030337,
                "rms_normalized_rmse_percent": 2.496453897019439,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.043218210339546204,
                  "global_sensor_index": 93,
                  "local_sensor_index": 5,
                  "reference": 0.04236339032649994,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 88
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 327.8071660315618,
            "full": 7606.595291988924
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 305.44749996624887,
            "full": 7745.748416986316
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 293.969291029498,
            "full": 7700.8596250088885
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 300.1412919256836,
            "full": 7644.957290962338
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
            "identifier": "courtyard_rooms_west_grid",
            "sensor_count": 32,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00039474701043218374,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1298754836607226e-05,
                  "p99": 0.00013449092773953403
                },
                "candidate_energy": 5.715186367789684,
                "cvrmse_percent": 22.243965168491798,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.11892897410594315,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.721991473547604,
                "relative_energy_error_percent": 0.11892897410594315,
                "rms_normalized_rmse_percent": 4.437450408019911,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0019719289848580956,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.0023666759952902794,
                  "rgb_channel": 0,
                  "sky_patch_index": 195
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007953457534313202,
                  "p50": 4.504358706469702e-06,
                  "p90": 2.3515349919733808e-05,
                  "p95": 4.288188129066818e-05,
                  "p99": 0.0001943195448257015
                },
                "candidate_energy": 4.399829053592629,
                "cvrmse_percent": 47.507036096373724,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.006706067150087839,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.399534017887099,
                "relative_energy_error_percent": 0.00670606715008784,
                "rms_normalized_rmse_percent": 2.4926329398916494,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.034194549545645714,
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "reference": 0.034989895299077034,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "sensor_count": 32,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003915459383279085,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1711098270316038e-05,
                  "p99": 0.00013635233452077917
                },
                "candidate_energy": 5.728836364338456,
                "cvrmse_percent": 23.831555094639167,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.041621143866209846,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.731221764394306,
                "relative_energy_error_percent": 0.041621143866209846,
                "rms_normalized_rmse_percent": 4.757027191381835,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0036917245015501976,
                  "global_sensor_index": 35,
                  "local_sensor_index": 3,
                  "reference": 0.004083270439878106,
                  "rgb_channel": 0,
                  "sky_patch_index": 376
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006575807929039001,
                  "p50": 4.447607267366038e-06,
                  "p90": 2.3409483247860408e-05,
                  "p95": 4.3534593169169755e-05,
                  "p99": 0.00020012252789456352
                },
                "candidate_energy": 4.389618856587578,
                "cvrmse_percent": 49.32610134751075,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.009741161937925616,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.390046498126111,
                "relative_energy_error_percent": 0.009741161937925614,
                "rms_normalized_rmse_percent": 2.5825384004205088,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0533168651163578,
                  "global_sensor_index": 36,
                  "local_sensor_index": 4,
                  "reference": 0.0526592843234539,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 32
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003728155279532075,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.8502446841448545e-05,
                  "p99": 0.00015635564923286403
                },
                "candidate_energy": 5.351925381980809,
                "cvrmse_percent": 21.347612126990906,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.03833036812085435,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.349874755293101,
                "relative_energy_error_percent": 0.038330368120854344,
                "rms_normalized_rmse_percent": 4.785359422633835,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0013274864759296179,
                  "global_sensor_index": 81,
                  "local_sensor_index": 17,
                  "reference": 0.0017003020038828254,
                  "rgb_channel": 0,
                  "sky_patch_index": 153
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0017456747591495514,
                  "p50": 6.0711236073984765e-06,
                  "p90": 2.8368634957587346e-05,
                  "p95": 5.84509689360857e-05,
                  "p99": 0.0002260628592921415
                },
                "candidate_energy": 4.127114787011205,
                "cvrmse_percent": 46.97229040126253,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.6036337721052726,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.1521787401650165,
                "relative_energy_error_percent": 0.6036337721052725,
                "rms_normalized_rmse_percent": 2.589442023793599,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.052709560841321945,
                  "global_sensor_index": 78,
                  "local_sensor_index": 14,
                  "reference": 0.0544552356004715,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 64
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00040016951970756054,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.163433550274931e-05,
                  "p99": 0.00016104564856505004
                },
                "candidate_energy": 5.359017269948559,
                "cvrmse_percent": 22.67622429620006,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.08515752711004393,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.354457546311963,
                "relative_energy_error_percent": 0.08515752711004392,
                "rms_normalized_rmse_percent": 5.068111524244913,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003623315948061645,
                  "global_sensor_index": 105,
                  "local_sensor_index": 17,
                  "reference": 0.004023485467769206,
                  "rgb_channel": 0,
                  "sky_patch_index": 384
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006914902478456497,
                  "p50": 6.12358066476304e-06,
                  "p90": 3.009105739693041e-05,
                  "p95": 6.472616223618388e-05,
                  "p99": 0.0002313595119630914
                },
                "candidate_energy": 4.070696600239408,
                "cvrmse_percent": 46.59055520334975,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.2241220737575411,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.079840423201887,
                "relative_energy_error_percent": 0.2241220737575411,
                "rms_normalized_rmse_percent": 2.5801249991773862,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.026589345186948776,
                  "global_sensor_index": 91,
                  "local_sensor_index": 3,
                  "reference": 0.025897854939103127,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 88
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 293.9587499713525,
            "full": 8255.9809590457
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 286.94241598714143,
            "full": 7946.103458059952
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 297.3558750236407,
            "full": 7963.65087502636
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 292.49625001102686,
            "full": 8066.393416956998
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
            "identifier": "courtyard_rooms_west_grid",
            "sensor_count": 32,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00019641098333522677,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1143662413815032e-05,
                  "p99": 7.991045247763365e-05
                },
                "candidate_energy": 5.719117350693086,
                "cvrmse_percent": 13.501622889530566,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.10834486443893669,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.725320441363976,
                "relative_energy_error_percent": 0.10834486443893669,
                "rms_normalized_rmse_percent": 2.6963359983505275,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0017576490063220263,
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "reference": 0.0015612380229867995,
                  "rgb_channel": 0,
                  "sky_patch_index": 198
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005412884056568146,
                  "p50": 3.604014523261867e-06,
                  "p90": 1.6268721083179116e-05,
                  "p95": 2.8823425839163755e-05,
                  "p99": 0.00011088905623182652
                },
                "candidate_energy": 4.3946024313993135,
                "cvrmse_percent": 28.719608165274074,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.14824697303955664,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.38809721011129,
                "relative_energy_error_percent": 0.14824697303955664,
                "rms_normalized_rmse_percent": 1.5041105518082454,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0373117309063673,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.037853019312024117,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "sensor_count": 32,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00022156647173687816,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1166254989802827e-05,
                  "p99": 7.979488174896674e-05
                },
                "candidate_energy": 5.729570178715431,
                "cvrmse_percent": 13.847863955548725,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.0928876279485539,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.724253055834094,
                "relative_energy_error_percent": 0.09288762794855389,
                "rms_normalized_rmse_percent": 2.7637290467121227,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0012874724925495684,
                  "global_sensor_index": 35,
                  "local_sensor_index": 3,
                  "reference": 0.0015090389642864466,
                  "rgb_channel": 0,
                  "sky_patch_index": 220
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006242245435714722,
                  "p50": 3.593085640574145e-06,
                  "p90": 1.6333664348167076e-05,
                  "p95": 2.8191031651658672e-05,
                  "p99": 0.0001164197592879641
                },
                "candidate_energy": 4.39225284997401,
                "cvrmse_percent": 30.594159945061133,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.05247396874861062,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.39455884941129,
                "relative_energy_error_percent": 0.052473968748610614,
                "rms_normalized_rmse_percent": 1.603222202457745,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.024298515170812607,
                  "global_sensor_index": 57,
                  "local_sensor_index": 25,
                  "reference": 0.02492273971438408,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 32
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00020676897838711739,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1271369405440055e-05,
                  "p99": 8.758606854826163e-05
                },
                "candidate_energy": 5.358505571139485,
                "cvrmse_percent": 12.450224692463234,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.0917775328217625,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.353592176322717,
                "relative_energy_error_percent": 0.0917775328217625,
                "rms_normalized_rmse_percent": 2.79337857076722,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0029328060336411,
                  "global_sensor_index": 75,
                  "local_sensor_index": 11,
                  "reference": 0.0027260370552539825,
                  "rgb_channel": 0,
                  "sky_patch_index": 264
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005959793925285339,
                  "p50": 4.627017688108026e-06,
                  "p90": 1.9728095139726065e-05,
                  "p95": 3.734044548764359e-05,
                  "p99": 0.00013396806607488516
                },
                "candidate_energy": 4.128959273472574,
                "cvrmse_percent": 27.948937428111158,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.29997896604571056,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.14138255002614,
                "relative_energy_error_percent": 0.29997896604571056,
                "rms_normalized_rmse_percent": 1.5414166896732535,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.053178925067186356,
                  "global_sensor_index": 78,
                  "local_sensor_index": 14,
                  "reference": 0.05377490445971489,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 64
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002218285226263106,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.214113192167133e-05,
                  "p99": 8.951985510066106e-05
                },
                "candidate_energy": 5.352021753567573,
                "cvrmse_percent": 12.820786977611428,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.0102781833562706,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.352571900721806,
                "relative_energy_error_percent": 0.010278183356270598,
                "rms_normalized_rmse_percent": 2.862973591638607,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001482256455346942,
                  "global_sensor_index": 98,
                  "local_sensor_index": 10,
                  "reference": 0.0017040849779732525,
                  "rgb_channel": 0,
                  "sky_patch_index": 180
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005027251318097115,
                  "p50": 4.661564162233844e-06,
                  "p90": 1.996643925394892e-05,
                  "p95": 3.6795507185161114e-05,
                  "p99": 0.0001353099301923061
                },
                "candidate_energy": 4.082818270315677,
                "cvrmse_percent": 27.307161672182676,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.1009296707863305,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.086943208641383,
                "relative_energy_error_percent": 0.1009296707863305,
                "rms_normalized_rmse_percent": 1.5152087743419809,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0313971946015954,
                  "global_sensor_index": 90,
                  "local_sensor_index": 2,
                  "reference": 0.03189991973340511,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 88
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 502.0684170303866,
            "full": 14253.16920899786
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 528.4391249297187,
            "full": 14131.28954207059
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 495.0631250394508,
            "full": 14114.914042060263
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 498.5802919836715,
            "full": 14286.139791016467
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/courtyard_rooms/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 20724.073708057404,
      "invocation_count": 7,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 79672.73916699924,
      "invocation_count": 7,
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
      112,
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
        "identifier": "courtyard_rooms_west_grid",
        "full_identifier": "courtyard_rooms_west_grid",
        "start_sensor_index": 0,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.16359605002523034,
            "cvrmse_percent": 5.954521336989146,
            "rms_normalized_rmse_percent": 1.1885696846377043,
            "reference_energy": 5.72482586599638,
            "candidate_energy": 5.715460277008788,
            "relative_energy_error_percent": 0.16359605002523037,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.174793139099947e-06,
              "p99": 2.9640955126523754e-05,
              "maximum": 0.00012478476855903864
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 257,
              "rgb_channel": 0,
              "reference": 0.001890760031528771,
              "candidate": 0.0020155448000878096,
              "position": [
                2.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.18392006844219722,
            "cvrmse_percent": 24.93112154968276,
            "rms_normalized_rmse_percent": 1.3053859772811907,
            "reference_energy": 4.388742823007717,
            "candidate_energy": 4.380671044203889,
            "relative_energy_error_percent": 0.18392006844219724,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.5426892281975597e-06,
              "p90": 1.3966759070171975e-05,
              "p95": 2.1156111506570154e-05,
              "p99": 5.01465331763027e-05,
              "maximum": 0.0007469542324542999
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03758237510919571,
              "candidate": 0.03683542087674141,
              "position": [
                1.5,
                5.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.1724155768119638,
            "cvrmse_percent": 10.62289941579539,
            "rms_normalized_rmse_percent": 1.2817534424732469,
            "reference_energy": 10.113568689004097,
            "candidate_energy": 10.096131321212678,
            "relative_energy_error_percent": 0.172415576811955,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.5207621067456785e-06,
              "p90": 1.3523413144866936e-05,
              "p95": 1.9996142145828273e-05,
              "p99": 4.71364849363445e-05,
              "maximum": 0.0007469542324542999
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03758237510919571,
              "candidate": 0.03683542087674141,
              "position": [
                1.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "full_identifier": "courtyard_rooms_east_grid",
        "start_sensor_index": 32,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.2272898171043522,
            "cvrmse_percent": 5.5035608800970435,
            "rms_normalized_rmse_percent": 1.0991809066047356,
            "reference_energy": 5.727734964299774,
            "candidate_energy": 5.714716405975196,
            "relative_energy_error_percent": 0.22728981710434054,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.5632256185633095e-06,
              "p99": 2.8286944143474102e-05,
              "maximum": 9.812612552195787e-05
            },
            "worst": {
              "global_sensor_index": 43,
              "local_sensor_index": 11,
              "sky_patch_index": 221,
              "rgb_channel": 0,
              "reference": 0.001702859066426754,
              "candidate": 0.0016047329409047961,
              "position": [
                11.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.3360944194270689,
            "cvrmse_percent": 26.181993270573,
            "rms_normalized_rmse_percent": 1.3723181053084887,
            "reference_energy": 4.392582503084398,
            "candidate_energy": 4.377819278422801,
            "relative_energy_error_percent": 0.33609441942708407,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.4955596674990375e-06,
              "p90": 1.4003591786604375e-05,
              "p95": 2.089716899718041e-05,
              "p99": 5.188581610127563e-05,
              "maximum": 0.0009514465928077698
            },
            "worst": {
              "global_sensor_index": 42,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04140515625476837,
              "candidate": 0.0404537096619606,
              "position": [
                11.5,
                5.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.27451493567974355,
            "cvrmse_percent": 11.18977031156451,
            "rms_normalized_rmse_percent": 1.3512865907765281,
            "reference_energy": 10.120317467384172,
            "candidate_energy": 10.092535684397998,
            "relative_energy_error_percent": 0.27451493567973473,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.4709191822912544e-06,
              "p90": 1.3652850611833856e-05,
              "p95": 1.991336830542414e-05,
              "p99": 4.791198763996354e-05,
              "maximum": 0.0009514465928077698
            },
            "worst": {
              "global_sensor_index": 42,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04140515625476837,
              "candidate": 0.0404537096619606,
              "position": [
                11.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "full_identifier": "courtyard_rooms_north_grid",
        "start_sensor_index": 64,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.2530182437707748,
            "cvrmse_percent": 5.308416207054502,
            "rms_normalized_rmse_percent": 1.1914820539487456,
            "reference_energy": 5.3573850281143836,
            "candidate_energy": 5.34382986660421,
            "relative_energy_error_percent": 0.25301824377077475,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 7.207738235592842e-06,
              "p99": 3.3115266705863073e-05,
              "maximum": 0.00013747472257819027
            },
            "worst": {
              "global_sensor_index": 75,
              "local_sensor_index": 11,
              "sky_patch_index": 157,
              "rgb_channel": 0,
              "reference": 0.00013747472257819027,
              "candidate": 0.0,
              "position": [
                6.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.00932540346426,
            "cvrmse_percent": 30.848517974503892,
            "rms_normalized_rmse_percent": 1.6993112231025573,
            "reference_energy": 4.133834755854681,
            "candidate_energy": 4.092110911526605,
            "relative_energy_error_percent": 1.0093254034642603,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.200477171423245e-06,
              "p90": 1.6227295418502763e-05,
              "p95": 2.520460111554712e-05,
              "p99": 6.171009154058989e-05,
              "maximum": 0.0011290200054645538
            },
            "worst": {
              "global_sensor_index": 77,
              "local_sensor_index": 13,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.046150170266628265,
              "candidate": 0.04502115026116371,
              "position": [
                7.5,
                10.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5824225662924517,
            "cvrmse_percent": 13.296300870683233,
            "rms_normalized_rmse_percent": 1.6816606925166173,
            "reference_energy": 9.491219783969065,
            "candidate_energy": 9.435940778130815,
            "relative_energy_error_percent": 0.5824225662924517,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.170395186520182e-06,
              "p90": 1.5767749573569745e-05,
              "p95": 2.3472588509321213e-05,
              "p99": 6.0378154739737513e-05,
              "maximum": 0.0011290200054645538
            },
            "worst": {
              "global_sensor_index": 77,
              "local_sensor_index": 13,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.046150170266628265,
              "candidate": 0.04502115026116371,
              "position": [
                7.5,
                10.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "full_identifier": "courtyard_rooms_south_grid",
        "start_sensor_index": 88,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.24431236401409803,
            "cvrmse_percent": 5.59435712364629,
            "rms_normalized_rmse_percent": 1.25009040433421,
            "reference_energy": 5.357599603552905,
            "candidate_energy": 5.344510325307056,
            "relative_energy_error_percent": 0.24431236401408557,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 8.114147931337357e-06,
              "p99": 3.4202588722109795e-05,
              "maximum": 0.00013347197091206908
            },
            "worst": {
              "global_sensor_index": 96,
              "local_sensor_index": 8,
              "sky_patch_index": 175,
              "rgb_channel": 0,
              "reference": 0.00013347197091206908,
              "candidate": 0.0,
              "position": [
                6.5,
                -0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.5984435560288339,
            "cvrmse_percent": 18.94924101526582,
            "rms_normalized_rmse_percent": 1.04993456696272,
            "reference_energy": 4.079577988742045,
            "candidate_energy": 4.103991960328843,
            "relative_energy_error_percent": 0.5984435560288394,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.2189558371319436e-06,
              "p90": 1.6504571249242872e-05,
              "p95": 2.605945337563753e-05,
              "p99": 6.676666380371858e-05,
              "maximum": 0.0007186084985733032
            },
            "worst": {
              "global_sensor_index": 107,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03215216100215912,
              "candidate": 0.03287076950073242,
              "position": [
                8.5,
                -3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.12000085015029872,
            "cvrmse_percent": 7.802978919149455,
            "rms_normalized_rmse_percent": 1.0001329512731816,
            "reference_energy": 9.437177592294951,
            "candidate_energy": 9.4485022856359,
            "relative_energy_error_percent": 0.12000085015031756,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.191482730675489e-06,
              "p90": 1.5975208953022957e-05,
              "p95": 2.4195658625103533e-05,
              "p99": 5.892455228604326e-05,
              "maximum": 0.0007186084985733032
            },
            "worst": {
              "global_sensor_index": 107,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03215216100215912,
              "candidate": 0.03287076950073242,
              "position": [
                8.5,
                -3.5,
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
      112,
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
        "identifier": "courtyard_rooms_west_grid",
        "full_identifier": "courtyard_rooms_west_grid",
        "start_sensor_index": 0,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.16359605002523034,
            "cvrmse_percent": 5.954521336989146,
            "rms_normalized_rmse_percent": 1.1885696846377043,
            "reference_energy": 5.72482586599638,
            "candidate_energy": 5.715460277008788,
            "relative_energy_error_percent": 0.16359605002523037,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.174793139099947e-06,
              "p99": 2.9640955126523754e-05,
              "maximum": 0.00012478476855903864
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 257,
              "rgb_channel": 0,
              "reference": 0.001890760031528771,
              "candidate": 0.0020155448000878096,
              "position": [
                2.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 82.90979881928548,
            "cvrmse_percent": 986.3521655118617,
            "rms_normalized_rmse_percent": 37.54005301708177,
            "reference_energy": 2.3949898105415244,
            "candidate_energy": 4.380671044203889,
            "relative_energy_error_percent": 82.90979881928548,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 9.379999937664252e-06,
              "p90": 5.616999987978488e-05,
              "p95": 8.074948607372781e-05,
              "p99": 0.00014292343767010522,
              "maximum": 0.013431057333946228
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02140972390770912,
              "candidate": 0.03484078124165535,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 24.339415122258362,
            "cvrmse_percent": 290.91428026184917,
            "rms_normalized_rmse_percent": 37.53793863923687,
            "reference_energy": 8.119815676537904,
            "candidate_energy": 10.096131321212678,
            "relative_energy_error_percent": 24.339415122258384,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 9.329999556939583e-06,
              "p90": 5.546000102185644e-05,
              "p95": 8.019746587706316e-05,
              "p99": 0.00014304051888757338,
              "maximum": 0.013431057333946228
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02140972390770912,
              "candidate": 0.03484078124165535,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "full_identifier": "courtyard_rooms_east_grid",
        "start_sensor_index": 32,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.2272898171043522,
            "cvrmse_percent": 5.5035608800970435,
            "rms_normalized_rmse_percent": 1.0991809066047356,
            "reference_energy": 5.727734964299774,
            "candidate_energy": 5.714716405975196,
            "relative_energy_error_percent": 0.22728981710434054,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.5632256185633095e-06,
              "p99": 2.8286944143474102e-05,
              "maximum": 9.812612552195787e-05
            },
            "worst": {
              "global_sensor_index": 43,
              "local_sensor_index": 11,
              "sky_patch_index": 221,
              "rgb_channel": 0,
              "reference": 0.001702859066426754,
              "candidate": 0.0016047329409047961,
              "position": [
                11.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.81455281937029,
            "cvrmse_percent": 969.1150529347736,
            "rms_normalized_rmse_percent": 36.920356864294426,
            "reference_energy": 2.407848662572182,
            "candidate_energy": 4.377819278422801,
            "relative_energy_error_percent": 81.81455281937029,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 9.20242246138514e-06,
              "p90": 5.596999835688621e-05,
              "p95": 7.884399747126642e-05,
              "p99": 0.00014060658824746478,
              "maximum": 0.012926051393151283
            },
            "worst": {
              "global_sensor_index": 60,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021570568904280663,
              "candidate": 0.034496620297431946,
              "position": [
                13.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 24.05423073843403,
            "cvrmse_percent": 286.8118556160505,
            "rms_normalized_rmse_percent": 36.918766001100686,
            "reference_energy": 8.135583626871956,
            "candidate_energy": 10.092535684397998,
            "relative_energy_error_percent": 24.05423073843405,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 9.143641364062205e-06,
              "p90": 5.572000009124167e-05,
              "p95": 7.857378312152716e-05,
              "p99": 0.00013821160173676925,
              "maximum": 0.012926051393151283
            },
            "worst": {
              "global_sensor_index": 60,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021570568904280663,
              "candidate": 0.034496620297431946,
              "position": [
                13.5,
                3.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "full_identifier": "courtyard_rooms_north_grid",
        "start_sensor_index": 64,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.2530182437707748,
            "cvrmse_percent": 5.308416207054502,
            "rms_normalized_rmse_percent": 1.1914820539487456,
            "reference_energy": 5.3573850281143836,
            "candidate_energy": 5.34382986660421,
            "relative_energy_error_percent": 0.25301824377077475,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 7.207738235592842e-06,
              "p99": 3.3115266705863073e-05,
              "maximum": 0.00013747472257819027
            },
            "worst": {
              "global_sensor_index": 75,
              "local_sensor_index": 11,
              "sky_patch_index": 157,
              "rgb_channel": 0,
              "reference": 0.00013747472257819027,
              "candidate": 0.0,
              "position": [
                6.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.02994461016007,
            "cvrmse_percent": 985.4174029591398,
            "rms_normalized_rmse_percent": 40.91411249123961,
            "reference_energy": 2.260460787489486,
            "candidate_energy": 4.092110911526605,
            "relative_energy_error_percent": 81.02994461016007,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.0849999853235204e-05,
              "p90": 6.571000267285854e-05,
              "p95": 9.61499972618185e-05,
              "p99": 0.00016346801421604924,
              "maximum": 0.014651119709014893
            },
            "worst": {
              "global_sensor_index": 72,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022360511124134064,
              "candidate": 0.037011630833148956,
              "position": [
                6.5,
                11.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 23.866260968460207,
            "cvrmse_percent": 292.3823561946589,
            "rms_normalized_rmse_percent": 40.91092219687317,
            "reference_energy": 7.61784581560387,
            "candidate_energy": 9.435940778130815,
            "relative_energy_error_percent": 23.866260968460207,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.0803139275594731e-05,
              "p90": 6.375089287757874e-05,
              "p95": 9.560999751556665e-05,
              "p99": 0.0001623237330932168,
              "maximum": 0.014651119709014893
            },
            "worst": {
              "global_sensor_index": 72,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022360511124134064,
              "candidate": 0.037011630833148956,
              "position": [
                6.5,
                11.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "full_identifier": "courtyard_rooms_south_grid",
        "start_sensor_index": 88,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.24431236401409803,
            "cvrmse_percent": 5.59435712364629,
            "rms_normalized_rmse_percent": 1.25009040433421,
            "reference_energy": 5.357599603552905,
            "candidate_energy": 5.344510325307056,
            "relative_energy_error_percent": 0.24431236401408557,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 8.114147931337357e-06,
              "p99": 3.4202588722109795e-05,
              "maximum": 0.00013347197091206908
            },
            "worst": {
              "global_sensor_index": 96,
              "local_sensor_index": 8,
              "sky_patch_index": 175,
              "rgb_channel": 0,
              "reference": 0.00013347197091206908,
              "candidate": 0.0,
              "position": [
                6.5,
                -0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 86.8496484362028,
            "cvrmse_percent": 1084.8260320723837,
            "rms_normalized_rmse_percent": 45.016755641052995,
            "reference_energy": 2.1964140658953895,
            "candidate_energy": 4.103991960328843,
            "relative_energy_error_percent": 86.8496484362028,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.0453321010572836e-05,
              "p90": 7.383513730019331e-05,
              "p95": 9.669875544204842e-05,
              "p99": 0.00016077015898190394,
              "maximum": 0.015571080148220062
            },
            "worst": {
              "global_sensor_index": 99,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02129228040575981,
              "candidate": 0.036863360553979874,
              "position": [
                6.5,
                -3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 25.079232035940525,
            "cvrmse_percent": 315.39995319659624,
            "rms_normalized_rmse_percent": 45.01313578682216,
            "reference_energy": 7.554013669448295,
            "candidate_energy": 9.4485022856359,
            "relative_energy_error_percent": 25.079232035940546,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.042088410940778e-05,
              "p90": 7.227342575788498e-05,
              "p95": 9.638576011639088e-05,
              "p99": 0.00015926244668662526,
              "maximum": 0.015571080148220062
            },
            "worst": {
              "global_sensor_index": 99,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02129228040575981,
              "candidate": 0.036863360553979874,
              "position": [
                6.5,
                -3.5,
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
      "bias_percent": -0.007869784071826685,
      "rms_normalized_error_percent": 0.26014378367633323,
      "absolute_error": {
        "p95": 0.10904470181983458,
        "p99": 0.18312301746234066,
        "maximum": 0.201621832581516
      },
      "worst_index": [
        75
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 14.549067112302394,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.26014378367633323
    },
    "overcast": {
      "bias_percent": 0.03430890030912667,
      "rms_normalized_error_percent": 0.20571244019628487,
      "absolute_error": {
        "p95": 0.0682310342788696,
        "p99": 0.10275962829589845,
        "maximum": 0.10700225830078125
      },
      "worst_index": [
        75
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.112030982971191,
      "reference_fraction_of_uniform": 0.6950294971466064,
      "rms_normalized_to_uniform_percent": 0.15195602323632448
    },
    "horizon": {
      "bias_percent": -1.3278772165544042,
      "rms_normalized_error_percent": 5.512009138209018,
      "absolute_error": {
        "p95": 0.02618966236901173,
        "p99": 0.03617200755913226,
        "maximum": 0.048749491740769146
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.20760252140244528,
      "reference_fraction_of_uniform": 0.014269129408778438,
      "rms_normalized_to_uniform_percent": 0.0602961604202981
    },
    "north": {
      "bias_percent": -0.08701002145550957,
      "rms_normalized_error_percent": 0.3054086920702685,
      "absolute_error": {
        "p95": 0.05386083126068102,
        "p99": 0.06699909210205078,
        "maximum": 0.0701761245727539
      },
      "worst_index": [
        36
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.80735445022583,
      "reference_fraction_of_uniform": 0.261690616607666,
      "rms_normalized_to_uniform_percent": 0.10363198490588674
    },
    "east": {
      "bias_percent": 0.00263861753383913,
      "rms_normalized_error_percent": 0.28698312738976656,
      "absolute_error": {
        "p95": 0.04664420932531354,
        "p99": 0.06221948623657227,
        "maximum": 0.07813072204589844
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.6959898471832275,
      "reference_fraction_of_uniform": 0.25403618812561035,
      "rms_normalized_to_uniform_percent": 0.09615548608455857
    },
    "south": {
      "bias_percent": -0.06244989734906528,
      "rms_normalized_error_percent": 0.3238705051084136,
      "absolute_error": {
        "p95": 0.04521398544311517,
        "p99": 0.08604637145996095,
        "maximum": 0.13678359985351562
      },
      "worst_index": [
        75
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.7162668704986572,
      "reference_fraction_of_uniform": 0.2554298937320709,
      "rms_normalized_to_uniform_percent": 0.1078448031822574
    },
    "west": {
      "bias_percent": -0.04676611113771059,
      "rms_normalized_error_percent": 0.32008174215398044,
      "absolute_error": {
        "p95": 0.0441114604473114,
        "p99": 0.07435086250305176,
        "maximum": 0.10693550109863281
      },
      "worst_index": [
        79
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.7037060260772705,
      "reference_fraction_of_uniform": 0.2545665502548218,
      "rms_normalized_to_uniform_percent": 0.10734291135340276
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
        "identifier": "courtyard_rooms_west_grid",
        "sensor_count": 32,
        "illuminance": {
          "nmbe_percent": 0.11656007026075343,
          "cvrmse_percent": 2.6333920952695404,
          "absolute_error_percentiles_lux": {
            "p50": 3.177001953125,
            "p90": 25.765734863281253,
            "p95": 39.603677368164,
            "p99": 88.54345214843757
          },
          "maximum_absolute_error_lux": 482.052734375,
          "worst": {
            "sensor_index": 19,
            "position": [
              2.5,
              4.5,
              0.75
            ],
            "hour_of_year": 2960.5,
            "foton_lux": 18657.0078125,
            "radiance_lux": 19139.060546875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.5541994863013701,
            "maximum_error_percentage_points": 2.60041095890411,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.2263458807669294,
            "maximum_error_percentage_points": 0.7385456742653602,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.22462756849315046,
            "maximum_error_percentage_points": 0.9058904109589037,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.22554794520548094,
            "maximum_error_percentage_points": 0.9058904109589037,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.010744863013698657,
            "maximum_error_percentage_points": 0.05602739726027295,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 34.375,
          "radiance_percent": 31.25,
          "difference_percentage_points": 3.125,
          "tolerance_percentage_points": 3.125,
          "ambiguous_sensor_count": 1,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "sensor_count": 32,
        "illuminance": {
          "nmbe_percent": 0.05703328199890432,
          "cvrmse_percent": 2.7042382750016927,
          "absolute_error_percentiles_lux": {
            "p50": 3.1961669921875,
            "p90": 25.830163574218773,
            "p95": 39.771623229980456,
            "p99": 88.55316894531255
          },
          "maximum_absolute_error_lux": 434.083984375,
          "worst": {
            "sensor_index": 2,
            "position": [
              10.5,
              5.5,
              0.75
            ],
            "hour_of_year": 4456.5,
            "foton_lux": 17375.703125,
            "radiance_lux": 16941.619140625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.38215753424657545,
            "maximum_error_percentage_points": 1.9135616438356173,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.144788588390927,
            "maximum_error_percentage_points": 0.7753304535721028,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.13474743150684904,
            "maximum_error_percentage_points": 0.4419178082191806,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.13918664383561707,
            "maximum_error_percentage_points": 0.4419178082191877,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.01978167808219196,
            "maximum_error_percentage_points": 0.08589041095890426,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 43.75,
          "radiance_percent": 46.875,
          "difference_percentage_points": 3.125,
          "tolerance_percentage_points": 3.125,
          "ambiguous_sensor_count": 1,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": -0.18007840672701458,
          "cvrmse_percent": 2.007609171100863,
          "absolute_error_percentiles_lux": {
            "p50": 4.3070068359375,
            "p90": 37.72064514160158,
            "p95": 57.474298095703055,
            "p99": 125.51287109374982
          },
          "maximum_absolute_error_lux": 524.0361328125,
          "worst": {
            "sensor_index": 10,
            "position": [
              6.5,
              9.5,
              0.75
            ],
            "hour_of_year": 1114.5,
            "foton_lux": 5244.392578125,
            "radiance_lux": 5768.4287109375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.16249429223744283,
            "maximum_error_percentage_points": 0.6283561643835611,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.05639610699051959,
            "maximum_error_percentage_points": 0.23073061556590346,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.060490867579908736,
            "maximum_error_percentage_points": 0.19493150684931493,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.0848002283105016,
            "maximum_error_percentage_points": 0.21904109589040388,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.04420662100456593,
            "maximum_error_percentage_points": 0.16835616438356027,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 87.5,
          "radiance_percent": 87.5,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 4.166666666666667,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": 0.12664555297327168,
          "cvrmse_percent": 3.743187019147684,
          "absolute_error_percentiles_lux": {
            "p50": 2.82232666015625,
            "p90": 20.988256835937502,
            "p95": 31.041323852539062,
            "p99": 54.950125122070304
          },
          "maximum_absolute_error_lux": 163.1148681640625,
          "worst": {
            "sensor_index": 8,
            "position": [
              6.5,
              -0.5,
              0.75
            ],
            "hour_of_year": 3367.5,
            "foton_lux": 1511.5570068359375,
            "radiance_lux": 1674.671875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.3683675799086757,
            "maximum_error_percentage_points": 1.0945205479452014,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.11019876202946695,
            "maximum_error_percentage_points": 0.38284293844267836,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.08983447488584462,
            "maximum_error_percentage_points": 0.27657534246575466,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.08983447488584358,
            "maximum_error_percentage_points": 0.27657534246575466,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0,
            "maximum_error_percentage_points": 0.0,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 41.666666666666664,
          "radiance_percent": 41.666666666666664,
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
    "numerical_correctness": "passed",
    "honeybee_compatibility": "passed",
    "performance": "measured"
  },
  "compatibility": {
    "official_loader": {
      "passed": true,
      "tolerance_percentage_points": 0.05,
      "maximum_error_percentage_points": 0.0049464897260236285,
      "metrics": {
        "da": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.0049464897260236285,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004901005993161789,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004925620719177459,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.004819937928090212,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.0046575342465753344,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004520547945206843,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.0039726027397266606,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
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
      "study_preparation_seconds": 0.010532750049605966,
      "weather_seconds": 0.10232120798900723,
      "metric_reduction_seconds": 0.3380167919676751,
      "write_seconds": 0.07106791704427451,
      "total_seconds": 0.5116276670014486,
      "cold_end_to_end_seconds": 0.5221604170510545,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.03460174996871501,
      "engine_upload_seconds": 0.000815541,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.27550041663926095,
      "engine_annual_reduction_seconds": 0.005076249944977462,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.27550041663926095
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.010532750049605966,
      "weather_seconds": 0.11132837494369596,
      "metric_reduction_seconds": 0.05422091705258936,
      "write_seconds": 0.07335049996618181,
      "total_seconds": 0.2391295830020681,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.2391295830020681,
      "raw_export_seconds": 0.037006999948062,
      "engine_upload_seconds": 9.3458e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.004551999969407916,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.029420125065371394,
      "full": 0.27906591596547514
    }
  },
  "elapsed_seconds": 2.5893843750236556,
  "result_class": "passed"
}
```
