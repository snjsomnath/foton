# Foton report

Status: **passed**

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
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "0c69876e0b546a9c00b573b7b8e78820a7a92f5d24b5d88c40918a9b177bbf31",
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
      "scene_fingerprint": 13086254370129758359,
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
    "maximum_samples": 65536,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "atrium_borrowed_light_atrium_grid",
        "bias_percent": 0.0670691152015031,
        "rms_normalized_error_percent": 1.7294094851839876,
        "absolute_error": {
          "p95": 0.00018826813902705908,
          "p99": 0.0005134795792400837,
          "maximum": 0.0011473782360553741
        },
        "worst_index": [
          22,
          125,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "bias_percent": -0.5487684420738758,
        "rms_normalized_error_percent": 1.8489102110370925,
        "absolute_error": {
          "p95": 0.0,
          "p99": 3.227096749469638e-05,
          "maximum": 0.0002651200629770756
        },
        "worst_index": [
          9,
          102,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "bias_percent": 0.34366405264341343,
        "rms_normalized_error_percent": 1.9304986962885404,
        "absolute_error": {
          "p95": 3.4552067518234253e-07,
          "p99": 7.683003786951303e-05,
          "maximum": 0.00029913708567619324
        },
        "worst_index": [
          6,
          76,
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
        "bias_percent": 0.02769676230298559,
        "rms_normalized_error_percent": 0.7584526231960476,
        "absolute_error": {
          "p95": 9.299568482674655e-05,
          "p99": 0.00018726475536823273,
          "maximum": 0.00040670111775398254
        },
        "worst_index": [
          3,
          140,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "bias_percent": 0.24459421534221168,
        "rms_normalized_error_percent": 1.6616258123748473,
        "absolute_error": {
          "p95": 2.2298666226561175e-05,
          "p99": 4.304712638258934e-05,
          "maximum": 0.00014628004282712936
        },
        "worst_index": [
          3,
          136,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "bias_percent": 0.16037345586869017,
        "rms_normalized_error_percent": 1.4311535674479197,
        "absolute_error": {
          "p95": 1.805020801839418e-05,
          "p99": 5.619414150714874e-05,
          "maximum": 0.00013486971147358418
        },
        "worst_index": [
          4,
          79,
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
        "bias_percent": 0.0033283070846272006,
        "rms_normalized_error_percent": 0.6682781021717564,
        "absolute_error": {
          "p95": 8.581551956012844e-05,
          "p99": 0.0001709219068288803,
          "maximum": 0.0003582015633583069
        },
        "worst_index": [
          1,
          115,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "bias_percent": -0.023550152856519357,
        "rms_normalized_error_percent": 1.3359874777955123,
        "absolute_error": {
          "p95": 1.9546394105418573e-05,
          "p99": 3.451004158705473e-05,
          "maximum": 0.00011817971244454384
        },
        "worst_index": [
          1,
          120,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "bias_percent": -0.03283814529418178,
        "rms_normalized_error_percent": 1.1257961247480652,
        "absolute_error": {
          "p95": 1.5629693007213063e-05,
          "p99": 3.772648051381111e-05,
          "maximum": 0.00012715160846710205
        },
        "worst_index": [
          8,
          77,
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.06322932236899759,
                "cvrmse_percent": 5.078904091885118,
                "rms_normalized_rmse_percent": 1.4104683746191535,
                "reference_energy": 24.02390702686057,
                "candidate_energy": 24.008716873240928,
                "relative_energy_error_percent": 0.06322932236899759,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.622357664629817e-05,
                  "p95": 0.00017854359030025058,
                  "p99": 0.0003781057894229889,
                  "maximum": 0.0008015595376491547
                },
                "worst": {
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "sky_patch_index": 142,
                  "rgb_channel": 0,
                  "reference": 0.0226998096331954,
                  "candidate": 0.021898250095546246
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.431099440650593,
                "cvrmse_percent": 40.24666608288786,
                "rms_normalized_rmse_percent": 2.332235412423651,
                "reference_energy": 5.280440804030924,
                "candidate_energy": 5.303204754800987,
                "relative_energy_error_percent": 0.431099440650593,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.4289212888106704e-05,
                  "p90": 0.00013344429316930473,
                  "p95": 0.00027817235677503034,
                  "p99": 0.0006498843431472778,
                  "maximum": 0.0011804597452282906
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 109,
                  "rgb_channel": 0,
                  "reference": 0.003099844790995121,
                  "candidate": 0.0019193850457668304
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
                "nmbe_percent": -0.13361503394907912,
                "cvrmse_percent": 15.643873671081337,
                "rms_normalized_rmse_percent": 1.4480681688809862,
                "reference_energy": 0.9596714382132632,
                "candidate_energy": 0.9583891728952949,
                "relative_energy_error_percent": 0.13361503394907912,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.766010584309697e-05,
                  "maximum": 0.00019495352171361446
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "sky_patch_index": 102,
                  "rgb_channel": 0,
                  "reference": 0.00226523051969707,
                  "candidate": 0.0020702769979834557
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 1.1220292416172528,
                "cvrmse_percent": 191.64316374404638,
                "rms_normalized_rmse_percent": 3.429059077009491,
                "reference_energy": 0.18643953053890172,
                "candidate_energy": 0.18853143658948213,
                "relative_energy_error_percent": 1.1220292416172528,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.6271370188624132e-05,
                  "p95": 4.123524508941042e-05,
                  "p99": 9.159976616501808e-05,
                  "maximum": 0.0003181551583111286
                },
                "worst": {
                  "global_sensor_index": 40,
                  "local_sensor_index": 4,
                  "sky_patch_index": 136,
                  "rgb_channel": 0,
                  "reference": 0.00014032796025276184,
                  "candidate": -0.00017782719805836678
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
                "nmbe_percent": 0.26676057220210164,
                "cvrmse_percent": 17.619382139982633,
                "rms_normalized_rmse_percent": 2.842294127246769,
                "reference_energy": 2.0030159870739226,
                "candidate_energy": 2.0083592439823406,
                "relative_energy_error_percent": 0.26676057220210164,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.369509406387355e-06,
                  "p99": 0.00011831964366137981,
                  "maximum": 0.0003497952129691839
                },
                "worst": {
                  "global_sensor_index": 73,
                  "local_sensor_index": 1,
                  "sky_patch_index": 101,
                  "rgb_channel": 0,
                  "reference": 0.008114913012832403,
                  "candidate": 0.007765117799863219
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -3.388495017647438,
                "cvrmse_percent": 679.87449382032,
                "rms_normalized_rmse_percent": 4.7086370460037905,
                "reference_energy": 0.08615278006056926,
                "candidate_energy": 0.08323349740065211,
                "relative_energy_error_percent": 3.388495017647437,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.7155859950435115e-05,
                  "p95": 3.603850800573122e-05,
                  "p99": 0.00020030420273542404,
                  "maximum": 0.0006790112238377333
                },
                "worst": {
                  "global_sensor_index": 73,
                  "local_sensor_index": 1,
                  "sky_patch_index": 101,
                  "rgb_channel": 0,
                  "reference": -7.176073268055916e-05,
                  "candidate": 0.0006072504911571741
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 313.33308399189264,
            "full": 946.2656669784337
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 245.3720000339672,
            "full": 950.5380420014262
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 237.45195800438523,
            "full": 975.7295000599697
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 264.29220801219344,
            "full": 919.4703330285847
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.022248750327815238,
                "cvrmse_percent": 3.2279655891146732,
                "rms_normalized_rmse_percent": 0.8959219491941488,
                "reference_energy": 24.000298111438042,
                "candidate_energy": 24.005637877842787,
                "relative_energy_error_percent": 0.022248750327815238,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.353704439883586e-05,
                  "p95": 0.00011301947524771093,
                  "p99": 0.00025503523647785187,
                  "maximum": 0.00044677872210741043
                },
                "worst": {
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "sky_patch_index": 124,
                  "rgb_channel": 0,
                  "reference": 0.0219145305454731,
                  "candidate": 0.02236130926758051
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.09798142425153879,
                "cvrmse_percent": 13.164794670489245,
                "rms_normalized_rmse_percent": 1.3834278511631444,
                "reference_energy": 9.994062352375742,
                "candidate_energy": 9.984270027742298,
                "relative_energy_error_percent": 0.09798142425153879,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.023781416937709e-05,
                  "p90": 0.00010044348891824484,
                  "p95": 0.00016777915880084035,
                  "p99": 0.00037707947194576263,
                  "maximum": 0.0007845396175980568
                },
                "worst": {
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "sky_patch_index": 139,
                  "rgb_channel": 0,
                  "reference": 0.0007327208295464516,
                  "candidate": 0.0015172604471445084
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
                "nmbe_percent": -0.08797199682108081,
                "cvrmse_percent": 10.885047665664787,
                "rms_normalized_rmse_percent": 1.005804317927278,
                "reference_energy": 0.959879483712939,
                "candidate_energy": 0.9590350585640408,
                "relative_energy_error_percent": 0.08797199682108081,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.487609162926674e-05,
                  "maximum": 0.00014359783381223679
                },
                "worst": {
                  "global_sensor_index": 46,
                  "local_sensor_index": 10,
                  "sky_patch_index": 104,
                  "rgb_channel": 0,
                  "reference": 0.006030660588294268,
                  "candidate": 0.0061742584221065044
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.15648043827361494,
                "cvrmse_percent": 39.79844008611007,
                "rms_normalized_rmse_percent": 2.407953817761912,
                "reference_energy": 0.6475941357376875,
                "candidate_energy": 0.646580777595851,
                "relative_energy_error_percent": 0.15648043827361494,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.6818416901951423e-06,
                  "p90": 2.1963044673611876e-05,
                  "p95": 3.1952528206602414e-05,
                  "p99": 6.07112015131861e-05,
                  "maximum": 0.00017628027126193047
                },
                "worst": {
                  "global_sensor_index": 40,
                  "local_sensor_index": 4,
                  "sky_patch_index": 105,
                  "rgb_channel": 0,
                  "reference": 0.00019721593707799911,
                  "candidate": 2.093566581606865e-05
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
                "nmbe_percent": 0.008752227642792867,
                "cvrmse_percent": 10.620955741640271,
                "rms_normalized_rmse_percent": 1.7160472557751614,
                "reference_energy": 2.0043593950003924,
                "candidate_energy": 2.0045348210974225,
                "relative_energy_error_percent": 0.008752227642792867,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.111085531301791e-06,
                  "p99": 7.168552838265896e-05,
                  "maximum": 0.00021959410514682531
                },
                "worst": {
                  "global_sensor_index": 85,
                  "local_sensor_index": 13,
                  "sky_patch_index": 77,
                  "rgb_channel": 0,
                  "reference": 0.002409855485893786,
                  "candidate": 0.0026294495910406113
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.229806823089489,
                "cvrmse_percent": 52.20234240007544,
                "rms_normalized_rmse_percent": 2.6776913870178984,
                "reference_energy": 0.6597575302258605,
                "candidate_energy": 0.6582413624055548,
                "relative_energy_error_percent": 0.22980682308948897,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.008242640907156e-06,
                  "p90": 1.7822711015469395e-05,
                  "p95": 2.8876358828711047e-05,
                  "p99": 0.00010924413800239563,
                  "maximum": 0.0003451025113463402
                },
                "worst": {
                  "global_sensor_index": 80,
                  "local_sensor_index": 8,
                  "sky_patch_index": 53,
                  "rgb_channel": 0,
                  "reference": 0.0003019580035470426,
                  "candidate": -4.314450779929757e-05
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
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 439.78466698899865,
            "full": 9549.390833009966
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 337.74091594386846,
            "full": 9323.642250034027
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 359.27283402998,
            "full": 9125.618375022896
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 324.0734579740092,
            "full": 9294.45666691754
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.03161646814772878,
                "cvrmse_percent": 3.037443901402943,
                "rms_normalized_rmse_percent": 0.8429192322547336,
                "reference_energy": 24.000888623495598,
                "candidate_energy": 24.008476856802417,
                "relative_energy_error_percent": 0.03161646814772878,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.334360033273697e-05,
                  "p95": 9.405554737895727e-05,
                  "p99": 0.0002263002097606659,
                  "maximum": 0.00046887435019016266
                },
                "worst": {
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "sky_patch_index": 140,
                  "rgb_channel": 0,
                  "reference": 0.02674692962318659,
                  "candidate": 0.026278055272996426
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.1401470745966781,
                "cvrmse_percent": 12.352817031658397,
                "rms_normalized_rmse_percent": 1.2980401326466497,
                "reference_energy": 9.989866044394944,
                "candidate_energy": 10.00386654941229,
                "relative_energy_error_percent": 0.1401470745966781,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.0826468244194984e-05,
                  "p90": 9.816262172535062e-05,
                  "p95": 0.0001675924751907586,
                  "p99": 0.00034269760362803936,
                  "maximum": 0.0006922557950019836
                },
                "worst": {
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "sky_patch_index": 142,
                  "rgb_channel": 0,
                  "reference": 0.0019747810438275337,
                  "candidate": 0.00128252524882555
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
                "nmbe_percent": -0.020320669697108943,
                "cvrmse_percent": 8.905949728464357,
                "rms_normalized_rmse_percent": 0.8225163350660848,
                "reference_energy": 0.9600961064534204,
                "candidate_energy": 0.9599010084948532,
                "relative_energy_error_percent": 0.020320669697108943,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.3460743250325322e-05,
                  "maximum": 0.00012107426300644875
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "sky_patch_index": 103,
                  "rgb_channel": 0,
                  "reference": 0.00613780808635056,
                  "candidate": 0.006258882349357009
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.3880705345597103,
                "cvrmse_percent": 40.25696435210781,
                "rms_normalized_rmse_percent": 2.4528099045189005,
                "reference_energy": 0.6517402811592277,
                "candidate_energy": 0.6492110691661921,
                "relative_energy_error_percent": 0.38807053455971036,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.586207412809017e-06,
                  "p90": 2.224610443590791e-05,
                  "p95": 3.23156213198672e-05,
                  "p99": 6.540247704833746e-05,
                  "maximum": 0.0002751704305410385
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "sky_patch_index": 102,
                  "rgb_channel": 0,
                  "reference": -8.835410699248314e-05,
                  "candidate": 0.00018681632354855537
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
                "nmbe_percent": -0.009529562524873922,
                "cvrmse_percent": 11.26575077641717,
                "rms_normalized_rmse_percent": 1.8200860461784885,
                "reference_energy": 2.0032935281387836,
                "candidate_energy": 2.003102623029463,
                "relative_energy_error_percent": 0.00952956252487392,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.784072320442535e-06,
                  "p99": 7.779666339047253e-05,
                  "maximum": 0.00022108352277427912
                },
                "worst": {
                  "global_sensor_index": 74,
                  "local_sensor_index": 2,
                  "sky_patch_index": 124,
                  "rgb_channel": 0,
                  "reference": 0.003667594981379807,
                  "candidate": 0.003888678504154086
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.2875138694419262,
                "cvrmse_percent": 52.24225809913658,
                "rms_normalized_rmse_percent": 2.700384608503224,
                "reference_energy": 0.6654766076818355,
                "candidate_energy": 0.6635632701368586,
                "relative_energy_error_percent": 0.2875138694419262,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.1399850942980265e-06,
                  "p90": 1.832546513469424e-05,
                  "p95": 2.8170644372949008e-05,
                  "p99": 0.00011363869998604059,
                  "maximum": 0.00032045645639300346
                },
                "worst": {
                  "global_sensor_index": 74,
                  "local_sensor_index": 2,
                  "sky_patch_index": 104,
                  "rgb_channel": 0,
                  "reference": -1.1962838470935822e-06,
                  "candidate": 0.0003192601725459099
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
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 382.15229206252843,
            "full": 13724.974749959074
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 492.48970800545067,
            "full": 14367.036290932447
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 471.40058304648846,
            "full": 14242.23458301276
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 441.4012919878587,
            "full": 11390.363625017926
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0191605112769732,
                "cvrmse_percent": 1.862945591389963,
                "rms_normalized_rmse_percent": 0.5171624279257542,
                "reference_energy": 24.002494919018773,
                "candidate_energy": 24.007093919764486,
                "relative_energy_error_percent": 0.019160511276973196,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.2040138244628906e-05,
                  "p95": 5.810153270431315e-05,
                  "p99": 0.00013929512351751328,
                  "maximum": 0.00035811495035886765
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 35,
                  "sky_patch_index": 138,
                  "rgb_channel": 0,
                  "reference": 0.0238841250538826,
                  "candidate": 0.02352601010352373
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.02443951554479144,
                "cvrmse_percent": 8.663542194316706,
                "rms_normalized_rmse_percent": 0.9107065650223785,
                "reference_energy": 9.996664702730609,
                "candidate_energy": 9.999107839154593,
                "relative_energy_error_percent": 0.024439515544791443,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.4486053260043263e-05,
                  "p90": 7.097312482073903e-05,
                  "p95": 0.00011354576272424307,
                  "p99": 0.0002457238733768463,
                  "maximum": 0.00043659843504428864
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 35,
                  "sky_patch_index": 124,
                  "rgb_channel": 0,
                  "reference": 0.004353203810751438,
                  "candidate": 0.0039166053757071495
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
                "nmbe_percent": -0.02318251581894874,
                "cvrmse_percent": 8.710986815091147,
                "rms_normalized_rmse_percent": 0.8048973362404477,
                "reference_energy": 0.9591252879276908,
                "candidate_energy": 0.9589029385560934,
                "relative_energy_error_percent": 0.02318251581894874,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.2198463082313538e-05,
                  "maximum": 0.00013919547200202942
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "sky_patch_index": 122,
                  "rgb_channel": 0,
                  "reference": 0.010291509795933962,
                  "candidate": 0.010430705267935991
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.11477962896419935,
                "cvrmse_percent": 28.21254193400181,
                "rms_normalized_rmse_percent": 1.716029236284088,
                "reference_energy": 0.6507074227167955,
                "candidate_energy": 0.6514543022822323,
                "relative_energy_error_percent": 0.11477962896419935,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.4544801817683037e-06,
                  "p90": 1.5505180272157304e-05,
                  "p95": 2.3166419123299416e-05,
                  "p99": 4.577740764943883e-05,
                  "maximum": 0.00017053657211363316
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "sky_patch_index": 101,
                  "rgb_channel": 0,
                  "reference": 0.00017583300359547138,
                  "candidate": 5.296431481838226e-06
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
                "nmbe_percent": -0.09817215627690766,
                "cvrmse_percent": 5.737516799169176,
                "rms_normalized_rmse_percent": 0.9270558706669283,
                "reference_energy": 2.002947933033738,
                "candidate_energy": 2.000981595858775,
                "relative_energy_error_percent": 0.09817215627690766,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.2766837307462974e-06,
                  "p99": 4.088558489456773e-05,
                  "maximum": 0.00012750271707773209
                },
                "worst": {
                  "global_sensor_index": 74,
                  "local_sensor_index": 2,
                  "sky_patch_index": 103,
                  "rgb_channel": 0,
                  "reference": 0.008389104157686234,
                  "candidate": 0.008261601440608501
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.2508251033917482,
                "cvrmse_percent": 29.245530695661213,
                "rms_normalized_rmse_percent": 1.5103022860819808,
                "reference_energy": 0.6640444377412962,
                "candidate_energy": 0.6657100278888279,
                "relative_energy_error_percent": 0.2508251033917482,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.834757424352574e-06,
                  "p90": 1.1876745702465996e-05,
                  "p95": 1.8675591172723194e-05,
                  "p99": 6.234683678485453e-05,
                  "maximum": 0.00015354517381638288
                },
                "worst": {
                  "global_sensor_index": 74,
                  "local_sensor_index": 2,
                  "sky_patch_index": 54,
                  "rgb_channel": 0,
                  "reference": -3.4856784623116255e-06,
                  "candidate": 0.00015005949535407126
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 788.8557920232415,
            "full": 17030.303000006825
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 606.9126250222325,
            "full": 16563.722290913574
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 588.7568749021739,
            "full": 16860.424792044796
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 572.2131659276783,
            "full": 16219.787959009409
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 2614.348959061317,
      "worker_pool_size": 12,
      "invocation_count": 7
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 11783.109582960606,
      "worker_pool_size": 12,
      "invocation_count": 7
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      108,
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
        "identifier": "atrium_borrowed_light_atrium_grid",
        "full_identifier": "atrium_borrowed_light_atrium_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -1.4786319576575537,
            "cvrmse_percent": 14.023858078198208,
            "rms_normalized_rmse_percent": 3.9272157184839114,
            "reference_energy": 23.99577915355235,
            "candidate_energy": 23.640969894498994,
            "relative_energy_error_percent": 1.4786319576575537,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.759407162666321e-05,
              "p95": 0.000200095693435287,
              "p99": 0.0006971295806579292,
              "maximum": 0.0040959627367556095
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 131,
              "rgb_channel": 0,
              "reference": 0.0040959627367556095,
              "candidate": 0.0,
              "position": [
                5.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.5120059076076976,
            "cvrmse_percent": 46.74586540124815,
            "rms_normalized_rmse_percent": 4.919206661934964,
            "reference_energy": 10.006901499699055,
            "candidate_energy": 9.955665572852112,
            "relative_energy_error_percent": 0.5120059076076976,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.374687003088184e-05,
              "p90": 0.0001619253307580948,
              "p95": 0.0003068585414439415,
              "p99": 0.000881945772562176,
              "maximum": 0.004231998696923256
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.006054569035768509,
              "candidate": 0.001822570338845253,
              "position": [
                5.5,
                4.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -1.1941563962001032,
            "cvrmse_percent": 9.936501379374375,
            "rms_normalized_rmse_percent": 3.553030150235154,
            "reference_energy": 34.0026806532514,
            "candidate_energy": 33.596635467351106,
            "relative_energy_error_percent": 1.1941563962001034,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.2601747079752386e-05,
              "p90": 0.00012348918244242668,
              "p95": 0.0001896628178656101,
              "p99": 0.0006451827939599752,
              "maximum": 0.0042320359498262405
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.02988695725798607,
              "candidate": 0.025654921308159828,
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
            "nmbe_percent": 0.33255591361550063,
            "cvrmse_percent": 14.505490807793906,
            "rms_normalized_rmse_percent": 1.3378272180489916,
            "reference_energy": 0.9569211066882417,
            "candidate_energy": 0.9601034044171683,
            "relative_energy_error_percent": 0.33255591361550063,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.4534063413739204e-05,
              "maximum": 0.00024422514252364635
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 9,
              "sky_patch_index": 102,
              "rgb_channel": 0,
              "reference": 0.0028928988613188267,
              "candidate": 0.003137124003842473,
              "position": [
                7.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.373618055728621,
            "cvrmse_percent": 36.494956130446795,
            "rms_normalized_rmse_percent": 2.2285640464681853,
            "reference_energy": 0.6531738671368839,
            "candidate_energy": 0.6442017529625907,
            "relative_energy_error_percent": 1.373618055728621,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.40244048149907e-06,
              "p90": 2.1338259102776647e-05,
              "p95": 3.0033689836272925e-05,
              "p99": 5.217115904088132e-05,
              "maximum": 0.000208052690140903
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 3,
              "sky_patch_index": 105,
              "rgb_channel": 0,
              "reference": 0.00035743264015764,
              "candidate": 0.00014937995001673698,
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
            "nmbe_percent": -0.3595947158080694,
            "cvrmse_percent": 13.248445841415277,
            "rms_normalized_rmse_percent": 1.9942513839642602,
            "reference_energy": 1.6100949738251256,
            "candidate_energy": 1.604305157379759,
            "relative_energy_error_percent": 0.35959471580806934,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.404945457281428e-06,
              "p90": 2.1230924176052213e-05,
              "p95": 2.9725354829679406e-05,
              "p99": 4.9409616622142494e-05,
              "maximum": 0.0001253633527085185
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 134,
              "rgb_channel": 0,
              "reference": 0.0015920907026156783,
              "candidate": 0.0017174540553241968,
              "position": [
                6.5,
                3.5,
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
            "nmbe_percent": -0.1325929355835285,
            "cvrmse_percent": 6.0722114313944475,
            "rms_normalized_rmse_percent": 0.982535812116992,
            "reference_energy": 2.0080703420130703,
            "candidate_energy": 2.005407782598013,
            "relative_energy_error_percent": 0.1325929355835285,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.179069608449736e-07,
              "p99": 3.751774784177542e-05,
              "maximum": 0.00014621688751503825
            },
            "worst": {
              "global_sensor_index": 74,
              "local_sensor_index": 2,
              "sky_patch_index": 106,
              "rgb_channel": 0,
              "reference": 0.000927561370190233,
              "candidate": 0.0010737782577052712,
              "position": [
                6.5,
                3.5,
                3.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.10949307977523963,
            "cvrmse_percent": 36.67394744190022,
            "rms_normalized_rmse_percent": 1.8786997839497988,
            "reference_energy": 0.6587716567074171,
            "candidate_energy": 0.6594929660830324,
            "relative_energy_error_percent": 0.10949307977523963,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.875536317034857e-06,
              "p90": 2.0734249119414017e-05,
              "p95": 2.9829426421201777e-05,
              "p99": 5.690986290574074e-05,
              "maximum": 0.00020980136469006538
            },
            "worst": {
              "global_sensor_index": 76,
              "local_sensor_index": 4,
              "sky_patch_index": 124,
              "rgb_channel": 0,
              "reference": -8.358154445886612e-05,
              "candidate": 0.00012621982023119926,
              "position": [
                6.5,
                1.5,
                3.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.07279209043405625,
            "cvrmse_percent": 8.370978558333057,
            "rms_normalized_rmse_percent": 1.7359544963487181,
            "reference_energy": 2.6668419987204874,
            "candidate_energy": 2.6649007486810454,
            "relative_energy_error_percent": 0.07279209043405625,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.824923391628545e-06,
              "p90": 2.072652569040656e-05,
              "p95": 2.8714262862195023e-05,
              "p99": 5.322739889379591e-05,
              "maximum": 0.00015983916819095612
            },
            "worst": {
              "global_sensor_index": 76,
              "local_sensor_index": 4,
              "sky_patch_index": 124,
              "rgb_channel": 0,
              "reference": 0.003780304454267025,
              "candidate": 0.003940143622457981,
              "position": [
                6.5,
                1.5,
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
        "identifier": "atrium_borrowed_light_atrium_grid",
        "full_identifier": "atrium_borrowed_light_atrium_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -1.4786319576575537,
            "cvrmse_percent": 14.023858078198208,
            "rms_normalized_rmse_percent": 3.9272157184839114,
            "reference_energy": 23.99577915355235,
            "candidate_energy": 23.640969894498994,
            "relative_energy_error_percent": 1.4786319576575537,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 7.759407162666321e-05,
              "p95": 0.000200095693435287,
              "p99": 0.0006971295806579292,
              "maximum": 0.0040959627367556095
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 131,
              "rgb_channel": 0,
              "reference": 0.0040959627367556095,
              "candidate": 0.0,
              "position": [
                5.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 87.40585886308739,
            "cvrmse_percent": 143.19347744826126,
            "rms_normalized_rmse_percent": 8.346818904122342,
            "reference_energy": 5.312355565214958,
            "candidate_energy": 9.955665572852112,
            "relative_energy_error_percent": 87.40585886308739,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.00024711743026273325,
              "p90": 0.0006706211715936661,
              "p95": 0.0008776722217589845,
              "p99": 0.0014586374163627625,
              "maximum": 0.004630844123312272
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 129,
              "rgb_channel": 0,
              "reference": -0.0039408041193382815,
              "candidate": 0.0006900400039739907,
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
            "nmbe_percent": 14.632458836889684,
            "cvrmse_percent": 22.331601856848444,
            "rms_normalized_rmse_percent": 7.181558045290266,
            "reference_energy": 29.308134718767306,
            "candidate_energy": 33.596635467351106,
            "relative_energy_error_percent": 14.632458836889684,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0002470783147145994,
              "p90": 0.0006222624870133586,
              "p95": 0.0007826159209798786,
              "p99": 0.001247179927304387,
              "maximum": 0.003585534170269966
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 137,
              "rgb_channel": 0,
              "reference": 0.028329195454716682,
              "candidate": 0.024743661284446716,
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
        "identifier": "atrium_borrowed_light_office_0_grid",
        "full_identifier": "atrium_borrowed_light_office_0_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.33255591361550063,
            "cvrmse_percent": 14.505490807793906,
            "rms_normalized_rmse_percent": 1.3378272180489916,
            "reference_energy": 0.9569211066882417,
            "candidate_energy": 0.9601034044171683,
            "relative_energy_error_percent": 0.33255591361550063,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 2.4534063413739204e-05,
              "maximum": 0.00024422514252364635
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 9,
              "sky_patch_index": 102,
              "rgb_channel": 0,
              "reference": 0.0028928988613188267,
              "candidate": 0.003137124003842473,
              "position": [
                7.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 239.77838693527838,
            "cvrmse_percent": 426.33274437979424,
            "rms_normalized_rmse_percent": 7.761082006614897,
            "reference_energy": 0.18959468222012,
            "candidate_energy": 0.6442017529625907,
            "relative_energy_error_percent": 239.77838693527838,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.3300004866323434e-05,
              "p90": 8.27034518806613e-05,
              "p95": 0.00011570828792173407,
              "p99": 0.0001884600060293451,
              "maximum": 0.0003797253593802452
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 3,
              "sky_patch_index": 137,
              "rgb_channel": 0,
              "reference": -6.264541298151016e-05,
              "candidate": 0.00031707994639873505,
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
            "nmbe_percent": 39.92874523841271,
            "cvrmse_percent": 70.49454718056398,
            "rms_normalized_rmse_percent": 7.76038014112186,
            "reference_energy": 1.1465157889083617,
            "candidate_energy": 1.604305157379759,
            "relative_energy_error_percent": 39.92874523841271,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.3317587217898108e-05,
              "p90": 8.305162191390991e-05,
              "p95": 0.00011737545414689513,
              "p99": 0.00019109610002487898,
              "maximum": 0.00032267626374959946
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 3,
              "sky_patch_index": 137,
              "rgb_channel": 0,
              "reference": 0.008916624821722507,
              "candidate": 0.009239301085472107,
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
            "nmbe_percent": -0.1325929355835285,
            "cvrmse_percent": 6.0722114313944475,
            "rms_normalized_rmse_percent": 0.982535812116992,
            "reference_energy": 2.0080703420130703,
            "candidate_energy": 2.005407782598013,
            "relative_energy_error_percent": 0.1325929355835285,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.179069608449736e-07,
              "p99": 3.751774784177542e-05,
              "maximum": 0.00014621688751503825
            },
            "worst": {
              "global_sensor_index": 74,
              "local_sensor_index": 2,
              "sky_patch_index": 106,
              "rgb_channel": 0,
              "reference": 0.000927561370190233,
              "candidate": 0.0010737782577052712,
              "position": [
                6.5,
                3.5,
                3.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 701.2265921363842,
            "cvrmse_percent": 1164.1184380145698,
            "rms_normalized_rmse_percent": 7.706050339319142,
            "reference_energy": 0.08231041911933623,
            "candidate_energy": 0.6594929660830324,
            "relative_energy_error_percent": 701.226592136384,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.1904994355281815e-05,
              "p90": 9.235762991011143e-05,
              "p95": 0.00013882594503229474,
              "p99": 0.00023653171956539154,
              "maximum": 0.0004382459446787834
            },
            "worst": {
              "global_sensor_index": 80,
              "local_sensor_index": 8,
              "sky_patch_index": 103,
              "rgb_channel": 0,
              "reference": -0.0002096761018037796,
              "candidate": 0.00022856984287500381,
              "position": [
                7.5,
                3.5,
                3.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 27.483987521843073,
            "cvrmse_percent": 45.47341343939946,
            "rms_normalized_rmse_percent": 7.644741697042001,
            "reference_energy": 2.0903807611324066,
            "candidate_energy": 2.6649007486810454,
            "relative_energy_error_percent": 27.483987521843073,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.18700006371364e-05,
              "p90": 9.242989153790404e-05,
              "p95": 0.00013604597280050254,
              "p99": 0.0002382901730015874,
              "maximum": 0.0004135342314839363
            },
            "worst": {
              "global_sensor_index": 80,
              "local_sensor_index": 8,
              "sky_patch_index": 103,
              "rgb_channel": 0,
              "reference": 0.0038592196069657803,
              "candidate": 0.004272753838449717,
              "position": [
                7.5,
                3.5,
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
      "bias_percent": -1.0808659687301685,
      "rms_normalized_error_percent": 2.054287927241372,
      "absolute_error": {
        "p95": 0.5161070099469305,
        "p99": 3.4727235612826117,
        "maximum": 3.889608861800248
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 21.148293591309475,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 2.054287927241372
    },
    "overcast": {
      "bias_percent": -1.065602640670215,
      "rms_normalized_error_percent": 2.065191556563393,
      "absolute_error": {
        "p95": 0.46255130767822245,
        "p99": 3.1915977478027306,
        "maximum": 3.5325050354003906
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 18.539409637451172,
      "reference_fraction_of_uniform": 0.8766385316848755,
      "rms_normalized_to_uniform_percent": 1.8427588311076415
    },
    "horizon": {
      "bias_percent": 3.573063117736516,
      "rms_normalized_error_percent": 12.747602002323081,
      "absolute_error": {
        "p95": 0.02488373410741231,
        "p99": 0.048696507932604514,
        "maximum": 0.059671277797956196
      },
      "worst_index": [
        20
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": true,
      "reference_mean": 0.06340915428897233,
      "reference_fraction_of_uniform": 0.00299831066819638,
      "rms_normalized_to_uniform_percent": 0.03565243405016679
    },
    "north": {
      "bias_percent": -0.5709274476599345,
      "rms_normalized_error_percent": 1.403190895011427,
      "absolute_error": {
        "p95": 0.07642865180969237,
        "p99": 0.2966305780410754,
        "maximum": 0.7393474578857422
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.1882855892181396,
      "reference_fraction_of_uniform": 0.1507585197687149,
      "rms_normalized_to_uniform_percent": 0.24792894316067896
    },
    "east": {
      "bias_percent": -0.2655615616119822,
      "rms_normalized_error_percent": 0.4631420956171977,
      "absolute_error": {
        "p95": 0.06180208921432489,
        "p99": 0.10626658439636223,
        "maximum": 0.1200876235961914
      },
      "worst_index": [
        0
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.1293184757232666,
      "reference_fraction_of_uniform": 0.1479702591896057,
      "rms_normalized_to_uniform_percent": 0.08479874818634588
    },
    "south": {
      "bias_percent": -1.0318137277279344,
      "rms_normalized_error_percent": 1.913667687870509,
      "absolute_error": {
        "p95": 0.1587179660797119,
        "p99": 0.5171781253814672,
        "maximum": 0.8754405975341797
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.1848948001861572,
      "reference_fraction_of_uniform": 0.1505981832742691,
      "rms_normalized_to_uniform_percent": 0.3384735683848759
    },
    "west": {
      "bias_percent": -2.7131938192086857,
      "rms_normalized_error_percent": 4.884298940760519,
      "absolute_error": {
        "p95": 0.2987286806106567,
        "p99": 1.5788920783996563,
        "maximum": 1.7046318054199219
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.02936315536499,
      "reference_fraction_of_uniform": 0.1905289888381958,
      "rms_normalized_to_uniform_percent": 0.9275896724273202
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
        "identifier": "atrium_borrowed_light_atrium_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -1.543095639302114,
          "cvrmse_percent": 6.104447526700851,
          "absolute_error_percentiles_lux": {
            "p50": 9.745872497558594,
            "p90": 84.99360351562501,
            "p95": 144.19138183593745,
            "p99": 395.8438183593745
          },
          "maximum_absolute_error_lux": 3489.603515625,
          "worst": {
            "sensor_index": 31,
            "position": [
              5.5,
              4.5,
              0.75
            ],
            "hour_of_year": 3829.5,
            "foton_lux": 32595.607421875,
            "radiance_lux": 36085.2109375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.19461948249619473,
            "maximum_error_percentage_points": 1.0110958904109566,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.10298080022173216,
            "maximum_error_percentage_points": 0.5506668310295311,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.0893607305936072,
            "maximum_error_percentage_points": 0.7093150684931508,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.42849695585996983,
            "maximum_error_percentage_points": 1.645753424657535,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.4730783866057837,
            "maximum_error_percentage_points": 1.726575342465754,
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
          "nmbe_percent": -0.4215347965016099,
          "cvrmse_percent": 8.37727267046648,
          "absolute_error_percentiles_lux": {
            "p50": 0.8272595405578613,
            "p90": 10.262062835693362,
            "p95": 16.58188171386718,
            "p99": 33.59307983398435
          },
          "maximum_absolute_error_lux": 115.60498046875,
          "worst": {
            "sensor_index": 1,
            "position": [
              6.5,
              4.5,
              0.75
            ],
            "hour_of_year": 3829.5,
            "foton_lux": 7994.4248046875,
            "radiance_lux": 7878.81982421875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2267237442922373,
            "maximum_error_percentage_points": 2.3560273972602737,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.33286655149936606,
            "maximum_error_percentage_points": 1.2263677802695412,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.6769939117199387,
            "maximum_error_percentage_points": 2.7920547945205527,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.6754870624048702,
            "maximum_error_percentage_points": 2.792054794520548,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0018340943683409518,
            "maximum_error_percentage_points": 0.03,
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
          "nmbe_percent": 0.007803116075789011,
          "cvrmse_percent": 3.2638504375219455,
          "absolute_error_percentiles_lux": {
            "p50": 1.4840202331542969,
            "p90": 11.9389030456543,
            "p95": 17.78436889648436,
            "p99": 33.84662734985351
          },
          "maximum_absolute_error_lux": 127.6708984375,
          "worst": {
            "sensor_index": 1,
            "position": [
              6.5,
              4.5,
              3.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 12360.5830078125,
            "radiance_lux": 12488.25390625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.24437975646879773,
            "maximum_error_percentage_points": 1.6183561643835631,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.28450499458517214,
            "maximum_error_percentage_points": 0.8929183169587347,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.6339421613394218,
            "maximum_error_percentage_points": 3.0153424657534202,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.631830289193303,
            "maximum_error_percentage_points": 3.015342465753424,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.008477929984779246,
            "maximum_error_percentage_points": 0.08643835616438356,
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
    "numerical_correctness": "passed",
    "honeybee_compatibility": "passed",
    "performance": "measured"
  },
  "compatibility": {
    "official_loader": {
      "passed": true,
      "tolerance_percentage_points": 0.05,
      "maximum_error_percentage_points": 0.004999197345888717,
      "metrics": {
        "da": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.004794520547942938,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.004989297945215299,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.004915186215740164,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.004999197345888717,
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
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
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
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.00410958904109604,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
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
      "study_preparation_seconds": 0.014618291985243559,
      "weather_seconds": 0.10607149999123067,
      "metric_reduction_seconds": 0.14639370806980878,
      "write_seconds": 0.053670624969527125,
      "total_seconds": 0.3064057920128107,
      "cold_end_to_end_seconds": 0.32102408399805427,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.03659645898733288,
      "engine_upload_seconds": 0.000328542,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0904579582856968,
      "engine_annual_reduction_seconds": 0.0009097500005736947,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0904579582856968
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.014618291985243559,
      "weather_seconds": 0.08990199991967529,
      "metric_reduction_seconds": 0.016643041977658868,
      "write_seconds": 0.046461834106594324,
      "total_seconds": 0.15335608401801437,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.15335608401801437,
      "raw_export_seconds": 0.02633533300831914,
      "engine_upload_seconds": 7.4667e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0010217499220743775,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.021166125079616904,
      "full": 0.09696029196493328
    }
  },
  "elapsed_seconds": 184.92370633408427,
  "result_class": "passed"
}
```
