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
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "50efdd63ba6d8ec7632ec921b4048f896f4a4ae255ae1ba7772f8e67120efc93",
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 16353448696249269853,
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 16353448696249269853,
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
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/12f3d0b2-7d1e-44d9-9264-d1e29a27929b/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "57a33891f1556d93b76c7c5a3f7778438334be0f4fdd009692a04f2c9d658b9f",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "581a959e80175fed89f7d9c2cf231ee7b8790a487c3adad0958a5f167ca70cf1",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0006226329132914543,
          "p95": 5.2641611546278e-05,
          "p99": 0.00025876224972307723
        },
        "bias_percent": 0.15600928580071266,
        "identifier": "courtyard_rooms_west_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.6080787043028897,
        "worst_index": [
          20,
          64,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0006568883545696735,
          "p95": 6.438465788960457e-05,
          "p99": 0.0002754469634965063
        },
        "bias_percent": -0.0063153057847264325,
        "identifier": "courtyard_rooms_east_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.750563277906029,
        "worst_index": [
          4,
          56,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0009097978472709656,
          "p95": 6.779102113796398e-05,
          "p99": 0.0003074812702834606
        },
        "bias_percent": -0.052937409357180595,
        "identifier": "courtyard_rooms_north_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.9311502604330366,
        "worst_index": [
          11,
          119,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.000855528749525547,
          "p95": 8.244859054684639e-05,
          "p99": 0.0002848142758011818
        },
        "bias_percent": -0.2635397675840732,
        "identifier": "courtyard_rooms_south_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.729739719298592,
        "worst_index": [
          8,
          64,
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
          "maximum": 0.0006817113608121872,
          "p95": 5.239434540271759e-05,
          "p99": 0.00016529902350157516
        },
        "bias_percent": 0.08775235450135047,
        "identifier": "courtyard_rooms_west_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0431203616581781,
        "worst_index": [
          14,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0006187707185745239,
          "p95": 5.5710239394102246e-05,
          "p99": 0.00015606211964041026
        },
        "bias_percent": 0.09831107267753807,
        "identifier": "courtyard_rooms_east_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.034854912254592,
        "worst_index": [
          3,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0005478681996464729,
          "p95": 6.84549449943006e-05,
          "p99": 0.00020156707614660263
        },
        "bias_percent": -0.010145357629718122,
        "identifier": "courtyard_rooms_north_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0803898888697363,
        "worst_index": [
          20,
          48,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.00046775490045547485,
          "p95": 7.502734661102295e-05,
          "p99": 0.00018834136426448822
        },
        "bias_percent": 0.0021478549166165897,
        "identifier": "courtyard_rooms_south_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0564139561874952,
        "worst_index": [
          16,
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
          "maximum": 0.0004905462265014648,
          "p95": 4.920700303046033e-05,
          "p99": 0.00013227546587586453
        },
        "bias_percent": -0.04657842223122585,
        "identifier": "courtyard_rooms_west_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.893728502317296,
        "worst_index": [
          28,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0007067546248435974,
          "p95": 4.861271008849144e-05,
          "p99": 0.00013897907920181764
        },
        "bias_percent": -0.11075501144593243,
        "identifier": "courtyard_rooms_east_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9051676509158235,
        "worst_index": [
          21,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0004327930510044098,
          "p95": 6.056716665625572e-05,
          "p99": 0.0001725340262055397
        },
        "bias_percent": 0.09937366223488026,
        "identifier": "courtyard_rooms_north_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8965694855965485,
        "worst_index": [
          14,
          0,
          0
        ]
      },
      {
        "absolute_error": {
          "maximum": 0.0005453340709209442,
          "p95": 6.377155659720302e-05,
          "p99": 0.00016719289124011993
        },
        "bias_percent": 0.02916671272858934,
        "identifier": "courtyard_rooms_south_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9395306391223237,
        "worst_index": [
          23,
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
            "identifier": "courtyard_rooms_west_grid",
            "sensor_count": 32,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0009109894745051861,
                  "p50": 0.0,
                  "p90": 2.1983794340485474e-07,
                  "p95": 8.432846516370773e-05,
                  "p99": 0.0003219316015020023
                },
                "candidate_energy": 5.723786687071552,
                "cvrmse_percent": 14.912823614312183,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.005746430086028231,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.724115619373663,
                "relative_energy_error_percent": 0.00574643008602823,
                "rms_normalized_rmse_percent": 3.2239333670331067,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013863185420632362,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.014774174895137548,
                  "rgb_channel": 0,
                  "sky_patch_index": 93
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011414340697228909,
                  "p50": 5.340824827726465e-06,
                  "p90": 6.852674050605856e-05,
                  "p95": 0.0001624235592316836,
                  "p99": 0.0005001923826057475
                },
                "candidate_energy": 2.380910516163297,
                "cvrmse_percent": 57.99161426385505,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.7779235404388748,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.3995773935789977,
                "relative_energy_error_percent": 0.7779235404388748,
                "rms_normalized_rmse_percent": 3.5823260893513083,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00037855468690395355,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.0007628793828189373,
                  "rgb_channel": 0,
                  "sky_patch_index": 69
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
                  "maximum": 0.0006582119967788458,
                  "p50": 0.0,
                  "p90": 2.455744834151119e-07,
                  "p95": 8.934666402637959e-05,
                  "p99": 0.00030346296261996047
                },
                "candidate_energy": 5.726192097155106,
                "cvrmse_percent": 13.782965262434777,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.10001313601712758,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.731924774876603,
                "relative_energy_error_percent": 0.10001313601712758,
                "rms_normalized_rmse_percent": 2.982138787099245,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0029824459925293922,
                  "global_sensor_index": 46,
                  "local_sensor_index": 14,
                  "reference": 0.0023242339957505465,
                  "rgb_channel": 0,
                  "sky_patch_index": 83
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001143051777034998,
                  "p50": 5.774532382929465e-06,
                  "p90": 6.973205017857254e-05,
                  "p95": 0.00016763480380177498,
                  "p99": 0.0004914684803225115
                },
                "candidate_energy": 2.403440179951332,
                "cvrmse_percent": 54.35984874631968,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.08554507380854791,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.40138591259997,
                "relative_energy_error_percent": 0.0855450738085479,
                "rms_normalized_rmse_percent": 3.3677885638478378,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0008508004248142242,
                  "global_sensor_index": 49,
                  "local_sensor_index": 17,
                  "reference": -0.0002922513522207737,
                  "rgb_channel": 0,
                  "sky_patch_index": 51
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
                  "maximum": 0.0008286599768325686,
                  "p50": 0.0,
                  "p90": 8.413364412263036e-06,
                  "p95": 0.0001335714478045702,
                  "p99": 0.0003732205368578434
                },
                "candidate_energy": 5.35389236896043,
                "cvrmse_percent": 14.086218336066286,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.15066391341746171,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.361970924191123,
                "relative_energy_error_percent": 0.15066391341746171,
                "rms_normalized_rmse_percent": 3.4354800469078266,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004459324991330504,
                  "global_sensor_index": 65,
                  "local_sensor_index": 1,
                  "reference": 0.0036306650144979358,
                  "rgb_channel": 0,
                  "sky_patch_index": 44
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011637192219495773,
                  "p50": 1.7727925296640024e-05,
                  "p90": 8.75578261911869e-05,
                  "p95": 0.00020668841898441315,
                  "p99": 0.000634610652923584
                },
                "candidate_energy": 2.2684997883531786,
                "cvrmse_percent": 56.26985064892428,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.6222378767796736,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.2544716120616854,
                "relative_energy_error_percent": 0.6222378767796736,
                "rms_normalized_rmse_percent": 3.841837122799106,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0006794270593672991,
                  "global_sensor_index": 75,
                  "local_sensor_index": 11,
                  "reference": -0.00048429216258227825,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
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
                  "maximum": 0.0007976654451340437,
                  "p50": 0.0,
                  "p90": 9.415458862349624e-06,
                  "p95": 0.0001315669360337779,
                  "p99": 0.0003776873927563429
                },
                "candidate_energy": 5.34987987414641,
                "cvrmse_percent": 14.40376625941043,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.05073371459955728,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.347167057672209,
                "relative_energy_error_percent": 0.050733714599557285,
                "rms_normalized_rmse_percent": 3.456063257846121,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.006565747549757361,
                  "global_sensor_index": 102,
                  "local_sensor_index": 14,
                  "reference": 0.005768082104623318,
                  "rgb_channel": 0,
                  "sky_patch_index": 31
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0019675754010677338,
                  "p50": 1.8572492535895435e-05,
                  "p90": 8.483752571919467e-05,
                  "p95": 0.00020047930593136698,
                  "p99": 0.0006375149823725224
                },
                "candidate_energy": 2.196681369456556,
                "cvrmse_percent": 59.25464955430354,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.6027870944400014,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.210002982220118,
                "relative_energy_error_percent": 0.6027870944400014,
                "rms_normalized_rmse_percent": 4.00981111073481,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03668279945850372,
                  "global_sensor_index": 97,
                  "local_sensor_index": 9,
                  "reference": 0.03865037485957146,
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 205.8622499462217,
            "full": 605.6730420095846
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 198.3637500088662,
            "full": 593.375249998644
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 206.95029199123383,
            "full": 591.0181669751182
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 189.60845796391368,
            "full": 591.800625086762
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
            "identifier": "courtyard_rooms_west_grid",
            "sensor_count": 32,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005905600264668465,
                  "p50": 0.0,
                  "p90": 4.5262277126312256e-07,
                  "p95": 4.511547740548849e-05,
                  "p99": 0.0001774141623172913
                },
                "candidate_energy": 5.722653510492506,
                "cvrmse_percent": 8.822075293403996,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.02247449338242701,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.721367662095904,
                "relative_energy_error_percent": 0.02247449338242701,
                "rms_normalized_rmse_percent": 1.9076092745895077,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.010388399939984083,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.01097895996645093,
                  "rgb_channel": 0,
                  "sky_patch_index": 69
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008993204683065414,
                  "p50": 1.0950979230983648e-05,
                  "p90": 4.831022579310229e-05,
                  "p95": 8.616004379291553e-05,
                  "p99": 0.0003080683527514339
                },
                "candidate_energy": 4.386588460003679,
                "cvrmse_percent": 19.640607170835494,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.12969898794374995,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.380906468651077,
                "relative_energy_error_percent": 0.12969898794374995,
                "rms_normalized_rmse_percent": 1.7938420555676735,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.030216669663786888,
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "reference": 0.03111599013209343,
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
                  "maximum": 0.0005967863835394382,
                  "p50": 0.0,
                  "p90": 9.155301086138934e-07,
                  "p95": 4.577403888106346e-05,
                  "p99": 0.00020553368376568024
                },
                "candidate_energy": 5.7332412797089205,
                "cvrmse_percent": 9.358098599120886,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.06860647924838627,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.729310601420082,
                "relative_energy_error_percent": 0.06860647924838627,
                "rms_normalized_rmse_percent": 2.0237491184254286,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.006365088513121009,
                  "global_sensor_index": 52,
                  "local_sensor_index": 20,
                  "reference": 0.005768302129581571,
                  "rgb_channel": 0,
                  "sky_patch_index": 55
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008324850350618362,
                  "p50": 1.1250557918174309e-05,
                  "p90": 5.159780994290486e-05,
                  "p95": 9.426371980225667e-05,
                  "p99": 0.0003172550117596992
                },
                "candidate_energy": 4.393973112824632,
                "cvrmse_percent": 20.257595469475472,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.23816861171435869,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.383532913340886,
                "relative_energy_error_percent": 0.23816861171435869,
                "rms_normalized_rmse_percent": 1.850946078782397,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.043829699978232384,
                  "global_sensor_index": 52,
                  "local_sensor_index": 20,
                  "reference": 0.04299721494317055,
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
                  "maximum": 0.0007179209496825933,
                  "p50": 0.0,
                  "p90": 4.170829015492927e-06,
                  "p95": 7.057539187371731e-05,
                  "p99": 0.000249107601121068
                },
                "candidate_energy": 5.36080317047081,
                "cvrmse_percent": 8.93535824728781,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.14282719528938106,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.368470806754026,
                "relative_energy_error_percent": 0.14282719528938106,
                "rms_normalized_rmse_percent": 2.180732977770629,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005435948958620429,
                  "global_sensor_index": 76,
                  "local_sensor_index": 12,
                  "reference": 0.006153869908303022,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010235302615910769,
                  "p50": 1.4017776265973225e-05,
                  "p90": 6.44470565021038e-05,
                  "p95": 0.00013402476906776428,
                  "p99": 0.0003769677132368088
                },
                "candidate_energy": 4.120583970974899,
                "cvrmse_percent": 19.78894640225399,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.26297497299616407,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.109776287891613,
                "relative_energy_error_percent": 0.26297497299616407,
                "rms_normalized_rmse_percent": 1.9208040463493947,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0011778022162616253,
                  "global_sensor_index": 76,
                  "local_sensor_index": 12,
                  "reference": 0.00015427195467054844,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
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
                  "maximum": 0.0005060252733528614,
                  "p50": 0.0,
                  "p90": 4.393094968691003e-06,
                  "p95": 7.219472900032997e-05,
                  "p99": 0.00023289071395993233
                },
                "candidate_energy": 5.350461311180055,
                "cvrmse_percent": 8.486426714867521,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.1305587932668302,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.357455941006435,
                "relative_energy_error_percent": 0.13055879326683023,
                "rms_normalized_rmse_percent": 2.0376324400399337,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.011365385260432959,
                  "global_sensor_index": 97,
                  "local_sensor_index": 9,
                  "reference": 0.010859359987080097,
                  "rgb_channel": 0,
                  "sky_patch_index": 108
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008410001173615456,
                  "p50": 1.402152338414453e-05,
                  "p90": 6.216717883944511e-05,
                  "p95": 0.0001301259471802041,
                  "p99": 0.00038193329237401485
                },
                "candidate_energy": 4.078363233238662,
                "cvrmse_percent": 19.07115213206924,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.0938048067121993,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.074541117818683,
                "relative_energy_error_percent": 0.09380480671219929,
                "rms_normalized_rmse_percent": 1.8540708378425197,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0009153955616056919,
                  "global_sensor_index": 97,
                  "local_sensor_index": 9,
                  "reference": 7.439544424414635e-05,
                  "rgb_channel": 0,
                  "sky_patch_index": 84
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 305.1053329836577,
            "full": 7964.71020905301
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 292.003707960248,
            "full": 7836.836208007298
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 286.1515840049833,
            "full": 7776.0771659668535
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 293.14437496941537,
            "full": 8293.556833988987
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
            "identifier": "courtyard_rooms_west_grid",
            "sensor_count": 32,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004616042133420706,
                  "p50": 0.0,
                  "p90": 3.303412370314618e-07,
                  "p95": 4.6339817345142365e-05,
                  "p99": 0.00019541476503945896
                },
                "candidate_energy": 5.721115660464875,
                "cvrmse_percent": 8.893172802837023,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.00107176987162137,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.721054343928078,
                "relative_energy_error_percent": 0.0010717698716213697,
                "rms_normalized_rmse_percent": 1.92478126442752,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0055357166565954685,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.005074112443253398,
                  "rgb_channel": 0,
                  "sky_patch_index": 37
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007071048021316528,
                  "p50": 1.1203117992408806e-05,
                  "p90": 4.824618372367695e-05,
                  "p95": 9.134970605373383e-05,
                  "p99": 0.00030716441106051225
                },
                "candidate_energy": 4.391850551841166,
                "cvrmse_percent": 19.395348048854032,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.07692571987244338,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.395231615401375,
                "relative_energy_error_percent": 0.07692571987244338,
                "rms_normalized_rmse_percent": 1.7778481798084862,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.040968600660562515,
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "reference": 0.04167570546269417,
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
                  "maximum": 0.0005453217308968306,
                  "p50": 0.0,
                  "p90": 8.482754765282152e-07,
                  "p95": 4.4352258555591106e-05,
                  "p99": 0.0001774893375113613
                },
                "candidate_energy": 5.729879731954227,
                "cvrmse_percent": 8.357628088476595,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.15544668095765127,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.720986648091738,
                "relative_energy_error_percent": 0.1554466809576513,
                "rms_normalized_rmse_percent": 1.8076950676333046,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004019003361463547,
                  "global_sensor_index": 61,
                  "local_sensor_index": 29,
                  "reference": 0.004564325092360377,
                  "rgb_channel": 0,
                  "sky_patch_index": 56
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007522795349359512,
                  "p50": 1.1260162409598706e-05,
                  "p90": 4.8684280045563355e-05,
                  "p95": 9.757676161825657e-05,
                  "p99": 0.000303204357624054
                },
                "candidate_energy": 4.40167936668184,
                "cvrmse_percent": 19.25656657596942,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.1300330024678811,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.407410454827335,
                "relative_energy_error_percent": 0.13003300246788108,
                "rms_normalized_rmse_percent": 1.7664531407994257,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03457850031554699,
                  "global_sensor_index": 59,
                  "local_sensor_index": 27,
                  "reference": 0.03533077985048294,
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
                  "maximum": 0.0008063553832471371,
                  "p50": 0.0,
                  "p90": 6.950604984012898e-06,
                  "p95": 7.244106382131577e-05,
                  "p99": 0.0002331715077161789
                },
                "candidate_energy": 5.35363982177104,
                "cvrmse_percent": 9.182822863257563,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.10731837827975073,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.359391433743397,
                "relative_energy_error_percent": 0.10731837827975074,
                "rms_normalized_rmse_percent": 2.239950009480836,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.010046949610114098,
                  "global_sensor_index": 75,
                  "local_sensor_index": 11,
                  "reference": 0.010853304993361235,
                  "rgb_channel": 0,
                  "sky_patch_index": 73
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007789246737957001,
                  "p50": 1.4004961144564732e-05,
                  "p90": 6.166445018607192e-05,
                  "p95": 0.00014624453615397215,
                  "p99": 0.00037101469933986664
                },
                "candidate_energy": 4.125547097173666,
                "cvrmse_percent": 19.09707184813781,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.15572982480189332,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.119132379535657,
                "relative_energy_error_percent": 0.15572982480189332,
                "rms_normalized_rmse_percent": 1.85695978508597,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.058731164783239365,
                  "global_sensor_index": 75,
                  "local_sensor_index": 11,
                  "reference": 0.057952240109443665,
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
                  "maximum": 0.0006489758379757404,
                  "p50": 0.0,
                  "p90": 5.57702378500835e-06,
                  "p95": 7.056840695440769e-05,
                  "p99": 0.00023079011589288712
                },
                "candidate_energy": 5.355353690448375,
                "cvrmse_percent": 9.13165294742209,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.040261675479895245,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.357510714025857,
                "relative_energy_error_percent": 0.04026167547989525,
                "rms_normalized_rmse_percent": 2.190750475593848,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005988312652334571,
                  "global_sensor_index": 98,
                  "local_sensor_index": 10,
                  "reference": 0.006637288490310311,
                  "rgb_channel": 0,
                  "sky_patch_index": 32
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009838398545980453,
                  "p50": 1.3788694104732713e-05,
                  "p90": 6.156639574328437e-05,
                  "p95": 0.00013044176739640534,
                  "p99": 0.00036989850923419
                },
                "candidate_energy": 4.085539112013883,
                "cvrmse_percent": 19.57497595544043,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.5591210407565104,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.062823013695613,
                "relative_energy_error_percent": 0.5591210407565103,
                "rms_normalized_rmse_percent": 1.900295716529453,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05957265943288803,
                  "global_sensor_index": 96,
                  "local_sensor_index": 8,
                  "reference": 0.058588819578289986,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 295.3383750282228,
            "full": 8441.409457940608
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 291.7958330363035,
            "full": 8279.904583934695
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 296.6477080481127,
            "full": 8238.802290987223
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 290.921917068772,
            "full": 8287.586374906823
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
            "identifier": "courtyard_rooms_west_grid",
            "sensor_count": 32,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000252904137596488,
                  "p50": 0.0,
                  "p90": 5.481301741383504e-07,
                  "p95": 3.0380673706531525e-05,
                  "p99": 0.00012024508323520521
                },
                "candidate_energy": 5.721604375066612,
                "cvrmse_percent": 5.089492445182356,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.050446196189495134,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.718719498608817,
                "relative_energy_error_percent": 0.05044619618949513,
                "rms_normalized_rmse_percent": 1.1006121491742384,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005172693403437734,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.005425597541034222,
                  "rgb_channel": 0,
                  "sky_patch_index": 37
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008285250514745712,
                  "p50": 7.82826055001351e-06,
                  "p90": 3.4544260415714234e-05,
                  "p95": 6.217509508132935e-05,
                  "p99": 0.00017086097504943686
                },
                "candidate_energy": 4.384740594909481,
                "cvrmse_percent": 12.129010324351198,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.22810231676050402,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.394765156046606,
                "relative_energy_error_percent": 0.228102316760504,
                "rms_normalized_rmse_percent": 1.1103122104360748,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.040717924013733864,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.041546449065208435,
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
                  "maximum": 0.0003276010975241661,
                  "p50": 0.0,
                  "p90": 4.576800165523309e-07,
                  "p95": 3.0150498787406832e-05,
                  "p99": 0.00011143930605612714
                },
                "candidate_energy": 5.725218400492182,
                "cvrmse_percent": 5.131137911990619,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.01563595864706718,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.726113733267599,
                "relative_energy_error_percent": 0.01563595864706718,
                "rms_normalized_rmse_percent": 1.1094112161488723,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0057839080691337585,
                  "global_sensor_index": 50,
                  "local_sensor_index": 18,
                  "reference": 0.006111509166657925,
                  "rgb_channel": 0,
                  "sky_patch_index": 51
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005497895181179047,
                  "p50": 8.155577233992517e-06,
                  "p90": 3.5688202842720784e-05,
                  "p95": 6.207427941262722e-05,
                  "p99": 0.00018216234166175247
                },
                "candidate_energy": 4.394746377040661,
                "cvrmse_percent": 12.376409232131577,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.07532199188226975,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.3914386579711895,
                "relative_energy_error_percent": 0.07532199188226975,
                "rms_normalized_rmse_percent": 1.1328088669944352,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02936358004808426,
                  "global_sensor_index": 46,
                  "local_sensor_index": 14,
                  "reference": 0.028813790529966354,
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
                  "maximum": 0.0003475609701126814,
                  "p50": 0.0,
                  "p90": 3.834425115201157e-06,
                  "p95": 4.315050318837166e-05,
                  "p99": 0.00014210538938641548
                },
                "candidate_energy": 5.354920081213734,
                "cvrmse_percent": 5.373559832223598,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.011241276436770913,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.354318187504973,
                "relative_energy_error_percent": 0.011241276436770914,
                "rms_normalized_rmse_percent": 1.31059347626511,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005621066549792886,
                  "global_sensor_index": 74,
                  "local_sensor_index": 10,
                  "reference": 0.005968627519905567,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006258673965930939,
                  "p50": 1.0056719474960119e-05,
                  "p90": 4.2670548282330856e-05,
                  "p95": 8.258596062660217e-05,
                  "p99": 0.00021461141295731068
                },
                "candidate_energy": 4.135906837764807,
                "cvrmse_percent": 11.822429524597387,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.10897608012418836,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.131404594983124,
                "relative_energy_error_percent": 0.10897608012418834,
                "rms_normalized_rmse_percent": 1.1530454916318222,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04612595587968826,
                  "global_sensor_index": 77,
                  "local_sensor_index": 13,
                  "reference": 0.04550008848309517,
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
                  "maximum": 0.0002565144095569849,
                  "p50": 0.0,
                  "p90": 4.865154551225714e-06,
                  "p95": 4.270486533641815e-05,
                  "p99": 0.0001348357181996107
                },
                "candidate_energy": 5.356658679537528,
                "cvrmse_percent": 5.056301927334996,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.026092763535777903,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.355261343858352,
                "relative_energy_error_percent": 0.026092763535777903,
                "rms_normalized_rmse_percent": 1.2140269534014434,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0064854740630835295,
                  "global_sensor_index": 102,
                  "local_sensor_index": 14,
                  "reference": 0.006228959653526545,
                  "rgb_channel": 0,
                  "sky_patch_index": 31
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006384607404470444,
                  "p50": 1.0207742434431566e-05,
                  "p90": 4.1016493923962116e-05,
                  "p95": 7.554295007139444e-05,
                  "p99": 0.0002464448334649205
                },
                "candidate_energy": 4.0777929387253415,
                "cvrmse_percent": 12.870273152015676,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.019084296686411678,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.077014869111771,
                "relative_energy_error_percent": 0.019084296686411675,
                "rms_normalized_rmse_percent": 1.2533234238005524,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.036074649542570114,
                  "global_sensor_index": 99,
                  "local_sensor_index": 11,
                  "reference": 0.03671311028301716,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 526.971249957569,
            "full": 14488.62462490797
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 491.9025410199538,
            "full": 14618.175207986496
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 479.72187504637986,
            "full": 14619.328542030416
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 518.3412909973413,
            "full": 14520.474249962717
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
    "/Users/ssanjay/GitHub/foton-release-0.3.2/validation/results/2026-11-04-architectural-v4-metal-0.3.2-release/courtyard_rooms/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 5429.103000089526,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/courtyard_rooms/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 19654.097500024363,
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
        "identifier": "courtyard_rooms_west_grid",
        "full_identifier": "courtyard_rooms_west_grid",
        "start_sensor_index": 0,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.013834163491584504,
            "cvrmse_percent": 7.80096938982314,
            "rms_normalized_rmse_percent": 1.6874446508645145,
            "reference_energy": 5.720563061385121,
            "candidate_energy": 5.71977166933857,
            "relative_energy_error_percent": 0.013834163491584502,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.3441857049656392e-07,
              "p95": 4.4327229261398315e-05,
              "p99": 0.00016583710676059215,
              "maximum": 0.0005219951272010803
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 64,
              "rgb_channel": 0,
              "reference": 0.008402213454246521,
              "candidate": 0.008924208581447601,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.17768039654781317,
            "cvrmse_percent": 15.34145285645144,
            "rms_normalized_rmse_percent": 1.4035835543781037,
            "reference_energy": 4.389351809844982,
            "candidate_energy": 4.381552792143371,
            "relative_energy_error_percent": 0.17768039654781315,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.3319222489371896e-05,
              "p90": 5.06799879076425e-05,
              "p95": 7.536448538303375e-05,
              "p99": 0.00019627148285508253,
              "maximum": 0.0007521659135818481
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05011064559221268,
              "candidate": 0.04935847967863083,
              "position": [
                2.5,
                4.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.08497014918106,
            "cvrmse_percent": 6.0749408754832075,
            "rms_normalized_rmse_percent": 1.2801502462838075,
            "reference_energy": 10.109914871230103,
            "candidate_energy": 10.10132446148194,
            "relative_energy_error_percent": 0.08497014918105998,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.3096251677779946e-05,
              "p90": 4.67214995296672e-05,
              "p95": 6.435126852011308e-05,
              "p99": 0.0001680888381088166,
              "maximum": 0.0007521659135818481
            },
            "worst": {
              "global_sensor_index": 19,
              "local_sensor_index": 19,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05011064559221268,
              "candidate": 0.04935847967863083,
              "position": [
                2.5,
                4.5,
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
            "nmbe_percent": -0.08641736806616868,
            "cvrmse_percent": 7.714185871297887,
            "rms_normalized_rmse_percent": 1.6690328447241052,
            "reference_energy": 5.717453596244933,
            "candidate_energy": 5.712512723326654,
            "relative_energy_error_percent": 0.08641736806616869,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.7066562324762344e-07,
              "p95": 4.211164923617616e-05,
              "p99": 0.00014806110411882427,
              "maximum": 0.00043502962216734886
            },
            "worst": {
              "global_sensor_index": 42,
              "local_sensor_index": 10,
              "sky_patch_index": 102,
              "rgb_channel": 0,
              "reference": 0.005379220470786095,
              "candidate": 0.0058142500929534435,
              "position": [
                11.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.648725842667349,
            "cvrmse_percent": 16.356284495037414,
            "rms_normalized_rmse_percent": 1.4995808681575986,
            "reference_energy": 4.40130502869123,
            "candidate_energy": 4.372752625555492,
            "relative_energy_error_percent": 0.6487258426673491,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.363085084449267e-05,
              "p90": 4.9016656703315675e-05,
              "p95": 7.109964644769207e-05,
              "p99": 0.00017660445300862212,
              "maximum": 0.0009330138564109802
            },
            "worst": {
              "global_sensor_index": 41,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.029439633712172508,
              "candidate": 0.028506619855761528,
              "position": [
                11.5,
                6.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.33100182834164876,
            "cvrmse_percent": 6.6513685344229945,
            "rms_normalized_rmse_percent": 1.4019806350486055,
            "reference_energy": 10.118758624936163,
            "candidate_energy": 10.085265348882146,
            "relative_energy_error_percent": 0.3310018283416487,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.3402351214608643e-05,
              "p90": 4.682325015892275e-05,
              "p95": 6.615649908781052e-05,
              "p99": 0.00014706773217767555,
              "maximum": 0.0009330138564109802
            },
            "worst": {
              "global_sensor_index": 41,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.029439633712172508,
              "candidate": 0.028506619855761528,
              "position": [
                11.5,
                6.5,
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
            "nmbe_percent": -0.38212354477066296,
            "cvrmse_percent": 6.386477592374175,
            "rms_normalized_rmse_percent": 1.5580886921177821,
            "reference_energy": 5.366319925917196,
            "candidate_energy": 5.345813953992547,
            "relative_energy_error_percent": 0.3821235447706629,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.835232049226761e-06,
              "p95": 5.678832530975342e-05,
              "p99": 0.00016435328871011734,
              "maximum": 0.0003651715815067291
            },
            "worst": {
              "global_sensor_index": 82,
              "local_sensor_index": 18,
              "sky_patch_index": 76,
              "rgb_channel": 0,
              "reference": 0.008710086345672607,
              "candidate": 0.009075257927179337,
              "position": [
                8.5,
                9.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.6311805582273806,
            "cvrmse_percent": 18.002639307994883,
            "rms_normalized_rmse_percent": 1.751578831561445,
            "reference_energy": 4.12195494414982,
            "candidate_energy": 4.095937965923454,
            "relative_energy_error_percent": 0.6311805582273806,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.5531601093243808e-05,
              "p90": 5.7186916819773614e-05,
              "p95": 8.891895413398743e-05,
              "p99": 0.00023949146270751953,
              "maximum": 0.0014763958752155304
            },
            "worst": {
              "global_sensor_index": 79,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05865419656038284,
              "candidate": 0.05717780068516731,
              "position": [
                7.5,
                8.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.49032043008980153,
            "cvrmse_percent": 7.422404532083094,
            "rms_normalized_rmse_percent": 1.6623487653582933,
            "reference_energy": 9.488274870067016,
            "candidate_energy": 9.441751919916001,
            "relative_energy_error_percent": 0.49032043008980153,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.5288575013983063e-05,
              "p90": 5.527098255697638e-05,
              "p95": 8.046615403145552e-05,
              "p99": 0.00019664503633975983,
              "maximum": 0.0014763958752155304
            },
            "worst": {
              "global_sensor_index": 79,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05865419656038284,
              "candidate": 0.05717780068516731,
              "position": [
                7.5,
                8.5,
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
            "nmbe_percent": -0.2276783952661703,
            "cvrmse_percent": 5.926218621798515,
            "rms_normalized_rmse_percent": 1.4217865934738816,
            "reference_energy": 5.3559874540273995,
            "candidate_energy": 5.3437930277414125,
            "relative_energy_error_percent": 0.22767839526617026,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 8.64267349243164e-06,
              "p95": 5.051555490354076e-05,
              "p99": 0.0001460714265704155,
              "maximum": 0.0003647543489933014
            },
            "worst": {
              "global_sensor_index": 92,
              "local_sensor_index": 4,
              "sky_patch_index": 64,
              "rgb_channel": 0,
              "reference": 0.008932281285524368,
              "candidate": 0.00929703563451767,
              "position": [
                5.5,
                -0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.4874945397757998,
            "cvrmse_percent": 14.385862100782434,
            "rms_normalized_rmse_percent": 1.4005488205163108,
            "reference_energy": 4.077376436831855,
            "candidate_energy": 4.097253424327516,
            "relative_energy_error_percent": 0.4874945397757998,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.5823886315047275e-05,
              "p90": 6.0104328440502286e-05,
              "p95": 8.689038077136502e-05,
              "p99": 0.00022240116959437728,
              "maximum": 0.0010547861456871033
            },
            "worst": {
              "global_sensor_index": 89,
              "local_sensor_index": 1,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.032545674592256546,
              "candidate": 0.03360046073794365,
              "position": [
                4.5,
                -1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.08144031438369102,
            "cvrmse_percent": 5.887831233361795,
            "rms_normalized_rmse_percent": 1.3261831054575604,
            "reference_energy": 9.433363890859255,
            "candidate_energy": 9.441046452068928,
            "relative_energy_error_percent": 0.08144031438369104,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.5554735000478104e-05,
              "p90": 5.660431634169072e-05,
              "p95": 8.259553578682244e-05,
              "p99": 0.0001887566177174449,
              "maximum": 0.0010547861456871033
            },
            "worst": {
              "global_sensor_index": 89,
              "local_sensor_index": 1,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.032545674592256546,
              "candidate": 0.03360046073794365,
              "position": [
                4.5,
                -1.5,
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
        "identifier": "courtyard_rooms_west_grid",
        "full_identifier": "courtyard_rooms_west_grid",
        "start_sensor_index": 0,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.013834163491584504,
            "cvrmse_percent": 7.80096938982314,
            "rms_normalized_rmse_percent": 1.6874446508645145,
            "reference_energy": 5.720563061385121,
            "candidate_energy": 5.71977166933857,
            "relative_energy_error_percent": 0.013834163491584502,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.3441857049656392e-07,
              "p95": 4.4327229261398315e-05,
              "p99": 0.00016583710676059215,
              "maximum": 0.0005219951272010803
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 64,
              "rgb_channel": 0,
              "reference": 0.008402213454246521,
              "candidate": 0.008924208581447601,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 83.05039101836778,
            "cvrmse_percent": 501.50845750021153,
            "rms_normalized_rmse_percent": 30.994009403547203,
            "reference_energy": 2.3936320309218644,
            "candidate_energy": 4.381552792143371,
            "relative_energy_error_percent": 83.05039101836776,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.6833982449024916e-05,
              "p90": 0.0002271702978760004,
              "p95": 0.0003228699788451195,
              "p99": 0.000580554993939587,
              "maximum": 0.01355784758925438
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021041933447122574,
              "candidate": 0.03459978103637695,
              "position": [
                0.5,
                4.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 24.48954389892522,
            "cvrmse_percent": 147.92163896295602,
            "rms_normalized_rmse_percent": 30.989835201040353,
            "reference_energy": 8.114195092306986,
            "candidate_energy": 10.10132446148194,
            "relative_energy_error_percent": 24.489543898925216,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.619324343162589e-05,
              "p90": 0.00022718000400345773,
              "p95": 0.00032578513491898775,
              "p99": 0.0005610628457361602,
              "maximum": 0.01355784758925438
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021041933447122574,
              "candidate": 0.03459978103637695,
              "position": [
                0.5,
                4.5,
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
            "nmbe_percent": -0.08641736806616868,
            "cvrmse_percent": 7.714185871297887,
            "rms_normalized_rmse_percent": 1.6690328447241052,
            "reference_energy": 5.717453596244933,
            "candidate_energy": 5.712512723326654,
            "relative_energy_error_percent": 0.08641736806616869,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.7066562324762344e-07,
              "p95": 4.211164923617616e-05,
              "p99": 0.00014806110411882427,
              "maximum": 0.00043502962216734886
            },
            "worst": {
              "global_sensor_index": 42,
              "local_sensor_index": 10,
              "sky_patch_index": 102,
              "rgb_channel": 0,
              "reference": 0.005379220470786095,
              "candidate": 0.0058142500929534435,
              "position": [
                11.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.14002757749441,
            "cvrmse_percent": 491.09071293518576,
            "rms_normalized_rmse_percent": 30.581613416356543,
            "reference_energy": 2.4140178645411563,
            "candidate_energy": 4.372752625555492,
            "relative_energy_error_percent": 81.14002757749441,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.6726526104757795e-05,
              "p90": 0.00022192500201434484,
              "p95": 0.00030744998366571963,
              "p99": 0.0005297527241054923,
              "maximum": 0.013384254649281502
            },
            "worst": {
              "global_sensor_index": 60,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021392444148659706,
              "candidate": 0.03477669879794121,
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
            "nmbe_percent": 24.027556359487956,
            "cvrmse_percent": 145.7747645862631,
            "rms_normalized_rmse_percent": 30.578042784176933,
            "reference_energy": 8.13147146078609,
            "candidate_energy": 10.085265348882146,
            "relative_energy_error_percent": 24.027556359487956,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.589320795072126e-05,
              "p90": 0.00022199434897629544,
              "p95": 0.0003081480972468853,
              "p99": 0.0005151490680873395,
              "maximum": 0.013384254649281502
            },
            "worst": {
              "global_sensor_index": 60,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021392444148659706,
              "candidate": 0.03477669879794121,
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
            "nmbe_percent": -0.38212354477066296,
            "cvrmse_percent": 6.386477592374175,
            "rms_normalized_rmse_percent": 1.5580886921177821,
            "reference_energy": 5.366319925917196,
            "candidate_energy": 5.345813953992547,
            "relative_energy_error_percent": 0.3821235447706629,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.835232049226761e-06,
              "p95": 5.678832530975342e-05,
              "p99": 0.00016435328871011734,
              "maximum": 0.0003651715815067291
            },
            "worst": {
              "global_sensor_index": 82,
              "local_sensor_index": 18,
              "sky_patch_index": 76,
              "rgb_channel": 0,
              "reference": 0.008710086345672607,
              "candidate": 0.009075257927179337,
              "position": [
                8.5,
                9.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.79142993904688,
            "cvrmse_percent": 502.6758713825363,
            "rms_normalized_rmse_percent": 34.261133853957546,
            "reference_energy": 2.2530973914979313,
            "candidate_energy": 4.095937965923454,
            "relative_energy_error_percent": 81.79142993904686,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.4043448724551126e-05,
              "p90": 0.00026890001026913524,
              "p95": 0.00037622638046741486,
              "p99": 0.0006426754407584667,
              "maximum": 0.014884479343891144
            },
            "worst": {
              "global_sensor_index": 72,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022088710218667984,
              "candidate": 0.03697318956255913,
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
            "nmbe_percent": 23.91698113628323,
            "cvrmse_percent": 148.58669487752007,
            "rms_normalized_rmse_percent": 34.24801543235147,
            "reference_energy": 7.619417317415127,
            "candidate_energy": 9.441751919916001,
            "relative_energy_error_percent": 23.91698113628323,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.3387677123973845e-05,
              "p90": 0.00025916998856700957,
              "p95": 0.00037303170040559053,
              "p99": 0.0006368327885866165,
              "maximum": 0.014884479343891144
            },
            "worst": {
              "global_sensor_index": 72,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022088710218667984,
              "candidate": 0.03697318956255913,
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
            "nmbe_percent": -0.2276783952661703,
            "cvrmse_percent": 5.926218621798515,
            "rms_normalized_rmse_percent": 1.4217865934738816,
            "reference_energy": 5.3559874540273995,
            "candidate_energy": 5.3437930277414125,
            "relative_energy_error_percent": 0.22767839526617026,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 8.64267349243164e-06,
              "p95": 5.051555490354076e-05,
              "p99": 0.0001460714265704155,
              "maximum": 0.0003647543489933014
            },
            "worst": {
              "global_sensor_index": 92,
              "local_sensor_index": 4,
              "sky_patch_index": 64,
              "rgb_channel": 0,
              "reference": 0.008932281285524368,
              "candidate": 0.00929703563451767,
              "position": [
                5.5,
                -0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 86.58837417754795,
            "cvrmse_percent": 549.6054525835996,
            "rms_normalized_rmse_percent": 36.950741187938995,
            "reference_energy": 2.1958781957276603,
            "candidate_energy": 4.097253424327516,
            "relative_energy_error_percent": 86.58837417754795,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.20571781489798e-05,
              "p90": 0.00028784689493477345,
              "p95": 0.0003813535367953591,
              "p99": 0.0006529632955789566,
              "maximum": 0.015832139179110527
            },
            "worst": {
              "global_sensor_index": 99,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021389910951256752,
              "candidate": 0.03722205013036728,
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
            "nmbe_percent": 25.0160806604808,
            "cvrmse_percent": 159.76874052596983,
            "rms_normalized_rmse_percent": 36.941110090174654,
            "reference_energy": 7.55186564975506,
            "candidate_energy": 9.441046452068928,
            "relative_energy_error_percent": 25.0160806604808,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.1670770769997034e-05,
              "p90": 0.00028408016078174114,
              "p95": 0.00037977000465616584,
              "p99": 0.0006526400102302432,
              "maximum": 0.015832139179110527
            },
            "worst": {
              "global_sensor_index": 99,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021389910951256752,
              "candidate": 0.03722205013036728,
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
      "bias_percent": -0.021808801411662426,
      "rms_normalized_error_percent": 0.31004985103768773,
      "absolute_error": {
        "p95": 0.1235727009298446,
        "p99": 0.16383659696416555,
        "maximum": 0.17126264947073278
      },
      "worst_index": [
        61
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 14.544907126508535,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.31004985103768773
    },
    "overcast": {
      "bias_percent": 0.026126608465617464,
      "rms_normalized_error_percent": 0.26107911228442054,
      "absolute_error": {
        "p95": 0.08201246261596669,
        "p99": 0.09656788349151611,
        "maximum": 0.10615038871765137
      },
      "worst_index": [
        61
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.026504516601562,
      "reference_fraction_of_uniform": 0.6893481016159058,
      "rms_normalized_to_uniform_percent": 0.1911132694701867
    },
    "horizon": {
      "bias_percent": -2.748366234719074,
      "rms_normalized_error_percent": 8.189269231781884,
      "absolute_error": {
        "p95": 0.043154214001576194,
        "p99": 0.055343488165507895,
        "maximum": 0.06048231310124408
      },
      "worst_index": [
        76
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.2518014022145923,
      "reference_fraction_of_uniform": 0.017311997940205243,
      "rms_normalized_to_uniform_percent": 0.10515146935371267
    },
    "north": {
      "bias_percent": -0.11744957402590253,
      "rms_normalized_error_percent": 0.45191642457719244,
      "absolute_error": {
        "p95": 0.07615054845809931,
        "p99": 0.09758195400238037,
        "maximum": 0.11507415771484375
      },
      "worst_index": [
        97
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.83333158493042,
      "reference_fraction_of_uniform": 0.2635514438152313,
      "rms_normalized_to_uniform_percent": 0.15483440214239413
    },
    "east": {
      "bias_percent": -0.016997039499755593,
      "rms_normalized_error_percent": 0.4118368865269976,
      "absolute_error": {
        "p95": 0.06247556209564209,
        "p99": 0.07529442548751832,
        "maximum": 0.07607650756835938
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.770719289779663,
      "reference_fraction_of_uniform": 0.25924670696258545,
      "rms_normalized_to_uniform_percent": 0.1392061377406383
    },
    "south": {
      "bias_percent": 0.010101592298593233,
      "rms_normalized_error_percent": 0.3897033742595909,
      "absolute_error": {
        "p95": 0.06880776882171627,
        "p99": 0.09115343809127807,
        "maximum": 0.12260055541992188
      },
      "worst_index": [
        76
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.7380306720733643,
      "reference_fraction_of_uniform": 0.25699928402900696,
      "rms_normalized_to_uniform_percent": 0.12976425408246114
    },
    "west": {
      "bias_percent": -0.10339382700200804,
      "rms_normalized_error_percent": 0.3394725468185936,
      "absolute_error": {
        "p95": 0.05181769132614127,
        "p99": 0.0772085189819336,
        "maximum": 0.10373497009277344
      },
      "worst_index": [
        61
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.6975314617156982,
      "reference_fraction_of_uniform": 0.2542148530483246,
      "rms_normalized_to_uniform_percent": 0.11345205496914895
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
          "nmbe_percent": 0.05242567845550415,
          "cvrmse_percent": 2.556349846854356,
          "absolute_error_percentiles_lux": {
            "p50": 3.5464038848876953,
            "p90": 26.51952514648439,
            "p95": 40.93946838378902,
            "p99": 91.81420410156265
          },
          "maximum_absolute_error_lux": 333.00927734375,
          "worst": {
            "sensor_index": 17,
            "position": [
              2.5,
              6.5,
              0.75
            ],
            "hour_of_year": 2961.5,
            "foton_lux": 6700.42041015625,
            "radiance_lux": 6367.4111328125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.5030607876712332,
            "maximum_error_percentage_points": 3.5617808219178073,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.270761557331644,
            "maximum_error_percentage_points": 1.6782166312002715,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.21010273972602733,
            "maximum_error_percentage_points": 1.2652054794520566,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.22433219178082164,
            "maximum_error_percentage_points": 1.2652054794520566,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.023484589041095842,
            "maximum_error_percentage_points": 0.24452054794520528,
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
          "nmbe_percent": -0.04626549913994024,
          "cvrmse_percent": 2.3164242001457636,
          "absolute_error_percentiles_lux": {
            "p50": 3.3791770935058594,
            "p90": 25.943960571289086,
            "p95": 38.308100891113256,
            "p99": 71.16548522949225
          },
          "maximum_absolute_error_lux": 244.134765625,
          "worst": {
            "sensor_index": 4,
            "position": [
              10.5,
              3.5,
              0.75
            ],
            "hour_of_year": 5846.5,
            "foton_lux": 18311.255859375,
            "radiance_lux": 18067.12109375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.47707191780821934,
            "maximum_error_percentage_points": 2.2424657534246535,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1827570165974326,
            "maximum_error_percentage_points": 0.6883870688583968,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.171519691780822,
            "maximum_error_percentage_points": 0.6882191780821927,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.1796703767123291,
            "maximum_error_percentage_points": 0.6882191780821927,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.025419520547945232,
            "maximum_error_percentage_points": 0.11068493150684944,
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
          "nmbe_percent": -0.08081526424290247,
          "cvrmse_percent": 1.8186230660649472,
          "absolute_error_percentiles_lux": {
            "p50": 5.1148681640625,
            "p90": 36.837646484375014,
            "p95": 55.45532226562494,
            "p99": 110.89514648437495
          },
          "maximum_absolute_error_lux": 394.21875,
          "worst": {
            "sensor_index": 11,
            "position": [
              6.5,
              8.5,
              0.75
            ],
            "hour_of_year": 4451.5,
            "foton_lux": 24191.5390625,
            "radiance_lux": 24585.7578125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.22601027397260362,
            "maximum_error_percentage_points": 0.7095890410958887,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.11726567434482209,
            "maximum_error_percentage_points": 0.4964268294208125,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.08921803652968026,
            "maximum_error_percentage_points": 0.3336986301369862,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.11468036529680514,
            "maximum_error_percentage_points": 0.3002739726027528,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0683447488584475,
            "maximum_error_percentage_points": 0.19315068493150633,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 91.66666666666667,
          "radiance_percent": 95.83333333333333,
          "difference_percentage_points": 4.166666666666657,
          "tolerance_percentage_points": 4.166666666666667,
          "ambiguous_sensor_count": 1,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": -0.07862144964663255,
          "cvrmse_percent": 3.442507890523702,
          "absolute_error_percentiles_lux": {
            "p50": 2.946338653564453,
            "p90": 19.125820922851567,
            "p95": 27.44900665283194,
            "p99": 50.217948303222634
          },
          "maximum_absolute_error_lux": 137.9185791015625,
          "worst": {
            "sensor_index": 12,
            "position": [
              7.5,
              -0.5,
              0.75
            ],
            "hour_of_year": 2725.5,
            "foton_lux": 1393.990234375,
            "radiance_lux": 1256.0716552734375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.3529794520547937,
            "maximum_error_percentage_points": 1.4536986301369836,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.16094464681643425,
            "maximum_error_percentage_points": 0.44918086772643306,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.10464611872146135,
            "maximum_error_percentage_points": 0.3249315068493175,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.10464611872145972,
            "maximum_error_percentage_points": 0.3249315068493175,
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
      "maximum_error_percentage_points": 0.004980468750005684,
      "metrics": {
        "da": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004963345462329016,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004980468750005684,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004779537671240064,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.0048598030821978,
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
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
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
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
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
      "study_preparation_seconds": 0.008501792093738914,
      "weather_seconds": 0.07502712507266551,
      "metric_reduction_seconds": 0.07718245801515877,
      "write_seconds": 0.03734429192263633,
      "total_seconds": 0.18973645905498415,
      "cold_end_to_end_seconds": 0.19823825114872307,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.004795541986823082,
      "engine_upload_seconds": 0.000300125,
      "engine_acceleration_structure_seconds": 0.00354825,
      "engine_tracing_seconds": 0.05258683336433023,
      "engine_annual_reduction_seconds": 0.0009409167105332017,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.05258683336433023
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.008501792093738914,
      "weather_seconds": 0.07347912504337728,
      "metric_reduction_seconds": 0.01512870891019702,
      "write_seconds": 0.017003207933157682,
      "total_seconds": 0.1057722499826923,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1057722499826923,
      "raw_export_seconds": 0.0036317920312285423,
      "engine_upload_seconds": 4.6915999999999996e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0009935833513736725,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02663737500552088,
      "full": 0.053947333013638854
    }
  },
  "elapsed_seconds": 1.1048998329788446,
  "result_class": "passed"
}
```
