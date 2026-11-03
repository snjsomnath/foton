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
  "model_sha256": "bae0c666ac3604f35a716c72ade67c2e6e373afe2aecca527938174f84fd7811",
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
      "solver_version": "0.2.0",
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
    "maximum_samples": 16384,
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
        "bias_percent": 0.041751771112130645,
        "rms_normalized_error_percent": 1.7532793342949522,
        "absolute_error": {
          "p95": 1.985033304663375e-05,
          "p99": 9.74569411482662e-05,
          "maximum": 0.0005082618445158005
        },
        "worst_index": [
          26,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "adjacent_grid",
        "bias_percent": 0.7658535315431699,
        "rms_normalized_error_percent": 5.003109485227093,
        "absolute_error": {
          "p95": 2.237899934698362e-06,
          "p99": 5.6696744650253095e-06,
          "maximum": 0.00013760710135102272
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
  "sample_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "interior_glazing_grid",
        "bias_percent": -0.0337107707224168,
        "rms_normalized_error_percent": 1.4793748596343224,
        "absolute_error": {
          "p95": 1.7706304788589478e-05,
          "p99": 8.609588257968426e-05,
          "maximum": 0.00041373632848262787
        },
        "worst_index": [
          23,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "adjacent_grid",
        "bias_percent": -0.2573817945617197,
        "rms_normalized_error_percent": 4.715152907835962,
        "absolute_error": {
          "p95": 1.870067080744775e-06,
          "p99": 4.7977400754462e-06,
          "maximum": 0.00017385813407599926
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
                "nmbe_percent": 0.12170693709656809,
                "cvrmse_percent": 32.707901930619066,
                "rms_normalized_rmse_percent": 6.311271427471331,
                "reference_energy": 6.024564883899984,
                "candidate_energy": 6.031897197293574,
                "relative_energy_error_percent": 0.12170693709656809,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.3072486985474825e-05,
                  "p99": 0.00017989042680710554,
                  "maximum": 0.0007490949064958841
                },
                "worst": {
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "sky_patch_index": 94,
                  "rgb_channel": 0,
                  "reference": 0.000702403107425198,
                  "candidate": 0.001451498013921082
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.6775245602712308,
                "cvrmse_percent": 157.51560708644755,
                "rms_normalized_rmse_percent": 5.78322765832502,
                "reference_energy": 2.008839969486459,
                "candidate_energy": 1.9952295853166433,
                "relative_energy_error_percent": 0.6775245602712308,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.7041799462022135e-06,
                  "p95": 4.5880049583502114e-05,
                  "p99": 0.00027465823222883046,
                  "maximum": 0.0008253925188910216
                },
                "worst": {
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "sky_patch_index": 94,
                  "rgb_channel": 0,
                  "reference": 0.0004276213876437396,
                  "candidate": -0.00039777113124728203
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
                "nmbe_percent": 1.6718900240981969,
                "cvrmse_percent": 428.33379897934253,
                "rms_normalized_rmse_percent": 19.882046950330068,
                "reference_energy": 0.06293811913383252,
                "candidate_energy": 0.0639903752689861,
                "relative_energy_error_percent": 1.6718900240981966,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.00028672334155999124
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "sky_patch_index": 97,
                  "rgb_channel": 0,
                  "reference": 0.00040329480543732643,
                  "candidate": 0.0006900181469973177
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.13732118349530031,
                "cvrmse_percent": 581.6149147613663,
                "rms_normalized_rmse_percent": 15.964452055858125,
                "reference_energy": 0.0722754888213899,
                "candidate_energy": 0.07237473837801645,
                "relative_energy_error_percent": 0.13732118349530034,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.976116881356575e-06,
                  "maximum": 0.00024942855816334486
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0031535379821434617,
                  "candidate": 0.0034029665403068066
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 162.1450420934707,
            "full": 473.7519590416923
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 133.32262507174164,
            "full": 387.5914999516681
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 154.68549996148795,
            "full": 447.2304580267519
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 144.9924170738086,
            "full": 416.18812503293157
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
                "nmbe_percent": -0.014767225267457293,
                "cvrmse_percent": 24.21233895170376,
                "rms_normalized_rmse_percent": 4.674712140420901,
                "reference_energy": 6.0262129017803545,
                "candidate_energy": 6.025322997346052,
                "relative_energy_error_percent": 0.014767225267457293,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.171611413359642e-05,
                  "p99": 0.00013146596029400826,
                  "maximum": 0.00035245250910520554
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 363,
                  "rgb_channel": 0,
                  "reference": 0.0040871379896998405,
                  "candidate": 0.003734685480594635
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.25731343992139194,
                "cvrmse_percent": 61.59619120340708,
                "rms_normalized_rmse_percent": 3.2282797086025345,
                "reference_energy": 3.623821454503112,
                "candidate_energy": 3.6144968748619206,
                "relative_energy_error_percent": 0.25731343992139194,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.415462236309395e-08,
                  "p90": 1.273433863389076e-05,
                  "p95": 3.607543112593703e-05,
                  "p99": 0.0001975594786927104,
                  "maximum": 0.0006133457645773888
                },
                "worst": {
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.02611524425446987,
                  "candidate": 0.02672859001904726
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
                "nmbe_percent": -0.7799592029839714,
                "cvrmse_percent": 212.93701214803872,
                "rms_normalized_rmse_percent": 10.282898619237386,
                "reference_energy": 0.06451669577927532,
                "candidate_energy": 0.0640134918730837,
                "relative_energy_error_percent": 0.7799592029839715,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.000118054827908054
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "sky_patch_index": 100,
                  "rgb_channel": 0,
                  "reference": 0.0005324728554114699,
                  "candidate": 0.0006505276833195239
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.3357997864459322,
                "cvrmse_percent": 165.74814584783448,
                "rms_normalized_rmse_percent": 7.721952036695851,
                "reference_energy": 0.1665683327390255,
                "candidate_energy": 0.1660089966334013,
                "relative_energy_error_percent": 0.3357997864459322,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.6994512133550192e-06,
                  "p95": 3.057500919112499e-06,
                  "p99": 8.348586391093704e-06,
                  "maximum": 0.00016168341971933842
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "sky_patch_index": 157,
                  "rgb_channel": 0,
                  "reference": -8.270304533652961e-05,
                  "candidate": 7.89803743828088e-05
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 199.4437500834465,
            "full": 5150.260250084102
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 204.66254197526723,
            "full": 5472.861957969144
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 216.92587493453175,
            "full": 5342.67683303915
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 205.715624964796,
            "full": 5425.4720830358565
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
                "nmbe_percent": 0.04952438026132444,
                "cvrmse_percent": 21.489348363804034,
                "rms_normalized_rmse_percent": 4.146789412944281,
                "reference_energy": 6.022451794279391,
                "candidate_energy": 6.025434376207045,
                "relative_energy_error_percent": 0.04952438026132444,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1646405002684332e-05,
                  "p99": 0.00011404944234527647,
                  "maximum": 0.00031114951707422733
                },
                "worst": {
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "sky_patch_index": 320,
                  "rgb_channel": 0,
                  "reference": 0.00338918250054121,
                  "candidate": 0.003078032983466983
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.43165432362222905,
                "cvrmse_percent": 59.333488011503206,
                "rms_normalized_rmse_percent": 3.109250193919014,
                "reference_energy": 3.6328515979943887,
                "candidate_energy": 3.6171702370008667,
                "relative_energy_error_percent": 0.4316543236222291,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.375613578602497e-08,
                  "p90": 1.2611495003511677e-05,
                  "p95": 3.406479299883358e-05,
                  "p99": 0.00018615927547216415,
                  "maximum": 0.0006488850340247154
                },
                "worst": {
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.020803330466151237,
                  "candidate": 0.020154445432126522
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
                "nmbe_percent": 0.09152655793437392,
                "cvrmse_percent": 301.42638501045593,
                "rms_normalized_rmse_percent": 14.323756869768419,
                "reference_energy": 0.06398360859839158,
                "candidate_energy": 0.0640421705929839,
                "relative_energy_error_percent": 0.09152655793437392,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.00015256134793162346
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "sky_patch_index": 157,
                  "rgb_channel": 0,
                  "reference": 0.00041121215326711535,
                  "candidate": 0.0005637735011987388
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 1.1658266197278,
                "cvrmse_percent": 194.7955013700254,
                "rms_normalized_rmse_percent": 9.11466593722439,
                "reference_energy": 0.16733117581924972,
                "candidate_energy": 0.16928196721005406,
                "relative_energy_error_percent": 1.1658266197277998,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.6968502841052706e-06,
                  "p95": 3.1673628626549544e-06,
                  "p99": 8.338584279954375e-06,
                  "maximum": 0.00022525867098011076
                },
                "worst": {
                  "global_sensor_index": 42,
                  "local_sensor_index": 6,
                  "sky_patch_index": 97,
                  "rgb_channel": 0,
                  "reference": 4.61502349935472e-05,
                  "candidate": 0.00027140890597365797
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 227.45400003623217,
            "full": 6196.956459083594
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 219.52033403795213,
            "full": 6204.015666968189
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 214.49774992652237,
            "full": 5661.519792047329
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 203.70966708287597,
            "full": 5932.294209022075
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
                "nmbe_percent": -0.029655352147175698,
                "cvrmse_percent": 13.37037008722648,
                "rms_normalized_rmse_percent": 2.5819644489108984,
                "reference_energy": 6.023768583908236,
                "candidate_energy": 6.021982214122147,
                "relative_energy_error_percent": 0.029655352147175695,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1566589819267392e-05,
                  "p99": 6.852101068943739e-05,
                  "maximum": 0.00020666749333031476
                },
                "worst": {
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "sky_patch_index": 407,
                  "rgb_channel": 0,
                  "reference": 0.0010330035001970828,
                  "candidate": 0.000826336006866768
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.2587880981938858,
                "cvrmse_percent": 35.83279660994004,
                "rms_normalized_rmse_percent": 1.8752129962891342,
                "reference_energy": 3.6181442101388157,
                "candidate_energy": 3.627507536730146,
                "relative_energy_error_percent": 0.2587880981938859,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 9.972090708743053e-09,
                  "p90": 9.002512524603e-06,
                  "p95": 2.205752934969496e-05,
                  "p99": 0.0001056735054589808,
                  "maximum": 0.000543215312063694
                },
                "worst": {
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.026192015036940575,
                  "candidate": 0.02564879972487688
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
                "nmbe_percent": 0.20279655245611886,
                "cvrmse_percent": 147.74087323463743,
                "rms_normalized_rmse_percent": 7.050486515969128,
                "reference_energy": 0.06395401605459483,
                "candidate_energy": 0.06408371259431078,
                "relative_energy_error_percent": 0.20279655245611886,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 6.613990990445018e-05
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "sky_patch_index": 98,
                  "rgb_channel": 0,
                  "reference": 0.0005300046468619257,
                  "candidate": 0.0005961445567663759
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.012003560459536183,
                "cvrmse_percent": 132.87206994942147,
                "rms_normalized_rmse_percent": 6.229997013989164,
                "reference_energy": 0.16769258568417555,
                "candidate_energy": 0.16771271476508431,
                "relative_energy_error_percent": 0.012003560459536185,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.2511861058328577e-06,
                  "p95": 2.2136291022434307e-06,
                  "p99": 5.573549060500227e-06,
                  "maximum": 0.0002255819272249937
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.004268924938514829,
                  "candidate": 0.004043343011289835
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 355.8409579563886,
            "full": 10515.887083020061
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 365.0849589612335,
            "full": 10048.15837496426
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 327.30079197790474,
            "full": 10061.410875059664
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 336.8582910625264,
            "full": 10280.548915965483
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 11970.130125060678,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/interior_glazing/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 47730.962999979965,
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
            "nmbe_percent": -0.7295144398138569,
            "cvrmse_percent": 70.80386566352266,
            "rms_normalized_rmse_percent": 3.7068976190165372,
            "reference_energy": 3.620861372671314,
            "candidate_energy": 3.5944466661120344,
            "relative_energy_error_percent": 0.7295144398138569,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 3.24551946505381e-05,
              "p95": 5.01996255479753e-05,
              "p99": 9.772914927452803e-05,
              "maximum": 0.0018088053911924362
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.020631534978747368,
              "candidate": 0.01882272958755493,
              "position": [
                1.5,
                4.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.37971326983153597,
            "cvrmse_percent": 26.516928434297064,
            "rms_normalized_rmse_percent": 3.698271141390461,
            "reference_energy": 9.645701278585804,
            "candidate_energy": 9.609075270862704,
            "relative_energy_error_percent": 0.37971326983153597,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 3.228144832974067e-05,
              "p95": 4.9405236495658755e-05,
              "p99": 9.655806934460998e-05,
              "maximum": 0.0018088053911924362
            },
            "worst": {
              "global_sensor_index": 7,
              "local_sensor_index": 7,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.020631534978747368,
              "candidate": 0.01882272958755493,
              "position": [
                1.5,
                4.5,
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
            "nmbe_percent": -3.304158060862979,
            "cvrmse_percent": 247.42527914724843,
            "rms_normalized_rmse_percent": 11.600508380081534,
            "reference_energy": 0.16757941733558468,
            "candidate_energy": 0.16204232850934375,
            "relative_energy_error_percent": 3.3041580608629784,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.7979185006188407e-06,
              "p95": 5.699331268260721e-06,
              "p99": 1.8841031305782963e-05,
              "maximum": 0.00027156516443938017
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 1,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0010578148066997528,
              "candidate": 0.001329379971139133,
              "position": [
                6.5,
                4.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -2.396004305679058,
            "cvrmse_percent": 178.86176296986244,
            "rms_normalized_rmse_percent": 11.595677876931571,
            "reference_energy": 0.23172151436019917,
            "candidate_energy": 0.22616945689894408,
            "relative_energy_error_percent": 2.396004305679058,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.7966589414063533e-06,
              "p95": 5.689744284609333e-06,
              "p99": 1.8844103351511876e-05,
              "maximum": 0.00027156516443938017
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 1,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0010578148066997528,
              "candidate": 0.001329379971139133,
              "position": [
                6.5,
                4.5,
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
            "nmbe_percent": 79.2360735523306,
            "cvrmse_percent": 828.9681611369049,
            "rms_normalized_rmse_percent": 30.400961166735243,
            "reference_energy": 2.0054259139204937,
            "candidate_energy": 3.5944466661120344,
            "relative_energy_error_percent": 79.23607355233061,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.209383464010913e-05,
              "p95": 9.59077151492238e-05,
              "p99": 0.0001888724509626627,
              "maximum": 0.00808284804224968
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011175772175192833,
              "candidate": 0.019258620217442513,
              "position": [
                2.5,
                5.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 19.660737096996414,
            "cvrmse_percent": 206.99187723421954,
            "rms_normalized_rmse_percent": 30.39667404246388,
            "reference_energy": 8.030265819834984,
            "candidate_energy": 9.609075270862704,
            "relative_energy_error_percent": 19.660737096996414,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.141599806142075e-05,
              "p95": 9.493963443674147e-05,
              "p99": 0.00018895487301051617,
              "maximum": 0.00808284804224968
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011175772175192833,
              "candidate": 0.019258620217442513,
              "position": [
                2.5,
                5.5,
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
            "nmbe_percent": 126.16680815022156,
            "cvrmse_percent": 1607.3892099604614,
            "rms_normalized_rmse_percent": 43.20250090067941,
            "reference_energy": 0.07164726328971938,
            "candidate_energy": 0.16204232850934375,
            "relative_energy_error_percent": 126.16680815022157,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.099999723119254e-07,
              "p95": 4.890000127488747e-06,
              "p99": 2.4270000722026452e-05,
              "maximum": 0.0013751729857176542
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0026795968879014254,
              "candidate": 0.00405476987361908,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 66.55904142665716,
            "cvrmse_percent": 848.1001705926475,
            "rms_normalized_rmse_percent": 43.20172876372033,
            "reference_energy": 0.13578936031433386,
            "candidate_energy": 0.22616945689894408,
            "relative_energy_error_percent": 66.55904142665715,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.099999723119254e-07,
              "p95": 4.890000127488747e-06,
              "p99": 2.4270000722026452e-05,
              "maximum": 0.0013751729857176542
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0026795968879014254,
              "candidate": 0.00405476987361908,
              "position": [
                6.5,
                3.5,
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
      "bias_percent": 0.03582428195184442,
      "rms_normalized_error_percent": 0.5206997065356036,
      "absolute_error": {
        "p95": 0.17235523029150993,
        "p99": 0.2208385975086659,
        "maximum": 0.2298306083891788
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 6.043274975854437,
      "rms_normalized_to_uniform_percent": 0.5206997065356036
    },
    "overcast": {
      "bias_percent": -0.011825087592920386,
      "rms_normalized_error_percent": 0.45295018792671493,
      "absolute_error": {
        "p95": 0.10954319834709168,
        "p99": 0.13429633617401146,
        "maximum": 0.1608142852783203
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.8641772270202637,
      "rms_normalized_to_uniform_percent": 0.3224916665786882
    },
    "horizon": {
      "bias_percent": 0.9157933813376219,
      "rms_normalized_error_percent": 3.2951550104547653,
      "absolute_error": {
        "p95": 0.06822718898622063,
        "p99": 0.10179875184518725,
        "maximum": 0.1326708529519378
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.7223831810334802,
      "rms_normalized_to_uniform_percent": 0.22391134294002535
    },
    "north": {
      "bias_percent": -100.0,
      "rms_normalized_error_percent": 100.0,
      "absolute_error": {
        "p95": 3.828675580734854e-05,
        "p99": 8.331611599714993e-05,
        "maximum": 0.00012003425945295021
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 7.3655423875607084e-06,
      "rms_normalized_to_uniform_percent": 0.00013130242774643617
    },
    "east": {
      "bias_percent": 0.22374060018126893,
      "rms_normalized_error_percent": 0.7672330703191007,
      "absolute_error": {
        "p95": 0.05059280991554261,
        "p99": 0.0688974595069887,
        "maximum": 0.08904838562011719
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.137437105178833,
      "rms_normalized_to_uniform_percent": 0.15451886470088563
    },
    "south": {
      "bias_percent": 0.15700972453182369,
      "rms_normalized_error_percent": 0.5847430899763024,
      "absolute_error": {
        "p95": 0.15012255907058716,
        "p99": 0.16738134384155284,
        "maximum": 0.17863082885742188
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 4.201578140258789,
      "rms_normalized_to_uniform_percent": 0.3818107378606506
    },
    "west": {
      "bias_percent": -0.6349075941615151,
      "rms_normalized_error_percent": 0.6713135665505398,
      "absolute_error": {
        "p95": 0.04222109317779544,
        "p99": 0.07331391632556918,
        "maximum": 0.07579505443572998
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.1726100444793701,
      "rms_normalized_to_uniform_percent": 0.13512658685546822
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
          "nmbe_percent": -0.06640910492268229,
          "cvrmse_percent": 4.906793557376126,
          "absolute_error_percentiles_lux": {
            "p50": 6.5688934326171875,
            "p90": 78.39602050781252,
            "p95": 115.81272583007808,
            "p99": 208.8905554199217
          },
          "maximum_absolute_error_lux": 770.103515625,
          "worst": {
            "sensor_index": 2,
            "position": [
              0.5,
              3.5,
              0.75
            ],
            "hour_of_year": 6826.5,
            "foton_lux": 5946.66015625,
            "radiance_lux": 5176.556640625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.9017199391171995,
            "maximum_error_percentage_points": 4.465753424657535,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.4680275941002308,
            "maximum_error_percentage_points": 2.6221968911825613,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.24520928462709263,
            "maximum_error_percentage_points": 1.2291780821917833,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.2463698630137008,
            "maximum_error_percentage_points": 1.2084931506849301,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.043801369863013535,
            "maximum_error_percentage_points": 0.24561643835616565,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 50.0,
          "radiance_percent": 52.77777777777778,
          "difference_percentage_points": 2.7777777777777786,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 1,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "adjacent_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -2.7700892769858885,
          "cvrmse_percent": 50.44423110012449,
          "absolute_error_percentiles_lux": {
            "p50": 0.7818174362182617,
            "p90": 9.480490398406987,
            "p95": 15.549729442596403,
            "p99": 34.976706237792904
          },
          "maximum_absolute_error_lux": 132.70357513427734,
          "worst": {
            "sensor_index": 22,
            "position": [
              9.5,
              1.5,
              0.75
            ],
            "hour_of_year": 6252.5,
            "foton_lux": 160.04220581054688,
            "radiance_lux": 27.33863067626953
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.016133942161339412,
            "maximum_error_percentage_points": 0.16671232876712327,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.3259594061398514,
            "maximum_error_percentage_points": 1.0173052203986934,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.2939383561643834,
            "maximum_error_percentage_points": 3.346027397260272,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.2940715372907155,
            "maximum_error_percentage_points": 3.3460273972602756,
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
      "maximum_error_percentage_points": 0.004954783818490682,
      "metrics": {
        "da": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.003150684931506831,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004954783818490682,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.004517592338666665,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
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
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004657534246572226,
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
      "study_preparation_seconds": 0.009484542068094015,
      "weather_seconds": 0.10996420902665704,
      "metric_reduction_seconds": 0.08516699995379895,
      "write_seconds": 0.047138958936557174,
      "total_seconds": 0.24248324998188764,
      "cold_end_to_end_seconds": 0.25196779204998165,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.021028541959822178,
      "engine_upload_seconds": 0.000831041,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.03029716678429395,
      "engine_annual_reduction_seconds": 0.004086749977432191,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.03029716678429395
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.009484542068094015,
      "weather_seconds": 0.11930329096503556,
      "metric_reduction_seconds": 0.05156900000292808,
      "write_seconds": 0.04103699990082532,
      "total_seconds": 0.21248274995014071,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.21248274995014071,
      "raw_export_seconds": 0.021137625095434487,
      "engine_upload_seconds": 7.825e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0031639999942854047,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.03089479194022715,
      "full": 0.028987957979552448
    }
  },
  "elapsed_seconds": 154.17084316699766,
  "result_class": "accuracy_failure"
}
```
