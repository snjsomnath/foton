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
  "sky_density": 2,
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
      "scene_fingerprint": 13086254370129758359,
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
        "identifier": "atrium_borrowed_light_atrium_grid",
        "bias_percent": -0.07672382825287284,
        "rms_normalized_error_percent": 1.0908881235476013,
        "absolute_error": {
          "p95": 6.735310307703912e-06,
          "p99": 8.77203419804573e-05,
          "maximum": 0.00024381768889725208
        },
        "worst_index": [
          33,
          528,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "bias_percent": 0.2312468068990563,
        "rms_normalized_error_percent": 1.278655093290519,
        "absolute_error": {
          "p95": 0.0,
          "p99": 3.562308847904205e-08,
          "maximum": 7.613853085786104e-05
        },
        "worst_index": [
          4,
          502,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "bias_percent": 0.23460445669819746,
        "rms_normalized_error_percent": 1.3484971770294452,
        "absolute_error": {
          "p95": 0.0,
          "p99": 9.63243655860424e-06,
          "maximum": 8.24473099783063e-05
        },
        "worst_index": [
          4,
          333,
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
        "bias_percent": 0.047332221109124675,
        "rms_normalized_error_percent": 1.6578436369736063,
        "absolute_error": {
          "p95": 4.970887675881386e-05,
          "p99": 0.00011498434469103813,
          "maximum": 0.00025830604135990143
        },
        "worst_index": [
          27,
          494,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "bias_percent": 0.30544610720932724,
        "rms_normalized_error_percent": 2.9473571820173428,
        "absolute_error": {
          "p95": 9.640472853789106e-06,
          "p99": 1.9093247829005122e-05,
          "maximum": 0.00011051353067159653
        },
        "worst_index": [
          4,
          425,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "bias_percent": 0.12983787917146547,
        "rms_normalized_error_percent": 2.7716354011376434,
        "absolute_error": {
          "p95": 7.677452231291682e-06,
          "p99": 3.055890556424856e-05,
          "maximum": 0.0001053904416039586
        },
        "worst_index": [
          9,
          370,
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
        "bias_percent": -0.004582739823760227,
        "rms_normalized_error_percent": 1.2798516443548034,
        "absolute_error": {
          "p95": 3.922919859178364e-05,
          "p99": 8.526374585926533e-05,
          "maximum": 0.0001727016642689705
        },
        "worst_index": [
          7,
          559,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_0_grid",
        "bias_percent": -0.014547785288800115,
        "rms_normalized_error_percent": 2.2312076720630802,
        "absolute_error": {
          "p95": 7.923146313260077e-06,
          "p99": 1.5943833204801194e-05,
          "maximum": 5.5576907470822334e-05
        },
        "worst_index": [
          1,
          457,
          0
        ],
        "passed": true
      },
      {
        "identifier": "atrium_borrowed_light_office_1_grid",
        "bias_percent": 0.0010555709335932828,
        "rms_normalized_error_percent": 2.070174427950479,
        "absolute_error": {
          "p95": 6.072732503525913e-06,
          "p99": 2.1553889382630587e-05,
          "maximum": 9.12968534976244e-05
        },
        "worst_index": [
          3,
          417,
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.007835154453686833,
                "cvrmse_percent": 10.239389888760062,
                "rms_normalized_rmse_percent": 2.836225107700525,
                "reference_energy": 23.99849241409902,
                "candidate_energy": 24.00037273304622,
                "relative_energy_error_percent": 0.007835154453686833,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.931454750727477e-06,
                  "p95": 7.103418465703726e-05,
                  "p99": 0.0002174637047573924,
                  "maximum": 0.000448250793851912
                },
                "worst": {
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "sky_patch_index": 557,
                  "rgb_channel": 0,
                  "reference": 0.004740746458992362,
                  "candidate": 0.00429249566514045
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.042647491314812366,
                "cvrmse_percent": 75.35041899318826,
                "rms_normalized_rmse_percent": 4.395480561608183,
                "reference_energy": 5.321134198073199,
                "candidate_energy": 5.318864867828227,
                "relative_energy_error_percent": 0.04264749131481236,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 8.429698937106878e-06,
                  "p90": 4.995484068786049e-05,
                  "p95": 0.00012477836571633816,
                  "p99": 0.0003282304387539625,
                  "maximum": 0.0007809747476130724
                },
                "worst": {
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "sky_patch_index": 519,
                  "rgb_channel": 0,
                  "reference": 0.0008605216862633824,
                  "candidate": 7.954693865031004e-05
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
                "nmbe_percent": 0.06882715839121727,
                "cvrmse_percent": 40.01762729658129,
                "rms_normalized_rmse_percent": 3.5008532530761167,
                "reference_energy": 0.959284324847431,
                "candidate_energy": 0.9599445729891158,
                "relative_energy_error_percent": 0.06882715839121727,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.412555765360594e-06,
                  "maximum": 0.0001790869573596865
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "sky_patch_index": 416,
                  "rgb_channel": 0,
                  "reference": 0.0020394737366586924,
                  "candidate": 0.0018603867792990059
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.12252054654688953,
                "cvrmse_percent": 347.24581411325437,
                "rms_normalized_rmse_percent": 5.88849624661687,
                "reference_energy": 0.18630044931779643,
                "candidate_energy": 0.1865287056465199,
                "relative_energy_error_percent": 0.12252054654688953,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.077914435489221e-06,
                  "p95": 1.3663762729265727e-05,
                  "p99": 3.3157224265778495e-05,
                  "maximum": 0.00029992171039339155
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "sky_patch_index": 370,
                  "rgb_channel": 0,
                  "reference": -0.00013186511932872236,
                  "candidate": 0.0001680565910646692
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
                "nmbe_percent": 0.01636580314700218,
                "cvrmse_percent": 31.167911665436428,
                "rms_normalized_rmse_percent": 4.562591643639884,
                "reference_energy": 2.0015206868724817,
                "candidate_energy": 2.001848251808042,
                "relative_energy_error_percent": 0.01636580314700218,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.102014620206319e-05,
                  "maximum": 0.0001919943024404347
                },
                "worst": {
                  "global_sensor_index": 75,
                  "local_sensor_index": 3,
                  "sky_patch_index": 424,
                  "rgb_channel": 0,
                  "reference": 0.002072128001600504,
                  "candidate": 0.0022641223040409386
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -3.700258138875556,
                "cvrmse_percent": 1020.406657081931,
                "rms_normalized_rmse_percent": 6.6795920114140435,
                "reference_energy": 0.08975696620725948,
                "candidate_energy": 0.08643572675996758,
                "relative_energy_error_percent": 3.700258138875556,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.8713853547942605e-06,
                  "p95": 1.072965596904396e-05,
                  "p99": 7.232400821521878e-05,
                  "maximum": 0.0003159278421662748
                },
                "worst": {
                  "global_sensor_index": 74,
                  "local_sensor_index": 2,
                  "sky_patch_index": 373,
                  "rgb_channel": 0,
                  "reference": 0.00015813653590157628,
                  "candidate": -0.0001577913062646985
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 695.830374956131,
            "full": 797.6816250011325
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 274.300166987814,
            "full": 701.1204999871552
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 219.67850008513778,
            "full": 687.389750033617
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 234.75433292333037,
            "full": 706.8703330587596
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 233.6386670358479,
            "full": 751.4507500454783
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 232.23149997647852,
            "full": 706.2214160105214
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 227.75433294009417,
            "full": 701.3369579799473
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 213.76424992922693,
            "full": 753.0894998926669
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.014956130006199182,
                "cvrmse_percent": 8.194627440644469,
                "rms_normalized_rmse_percent": 2.2692042225232436,
                "reference_energy": 23.99876347268639,
                "candidate_energy": 24.002352758951247,
                "relative_energy_error_percent": 0.014956130006199182,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.0771479941904545e-06,
                  "p95": 6.88754953444004e-05,
                  "p99": 0.00016321497969329357,
                  "maximum": 0.00042209599632769823
                },
                "worst": {
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "sky_patch_index": 557,
                  "rgb_channel": 0,
                  "reference": 0.002768754493445158,
                  "candidate": 0.0023466584971174598
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.05110873129892972,
                "cvrmse_percent": 33.18352950283624,
                "rms_normalized_rmse_percent": 3.487090315070622,
                "reference_energy": 9.985389347692486,
                "candidate_energy": 9.980285941881622,
                "relative_energy_error_percent": 0.05110873129892972,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.068882193067111e-05,
                  "p90": 5.271282279863957e-05,
                  "p95": 0.0001035777386277914,
                  "p99": 0.0002607259666547179,
                  "maximum": 0.0006197988986968994
                },
                "worst": {
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "sky_patch_index": 557,
                  "rgb_channel": 0,
                  "reference": 3.966991789638996e-05,
                  "candidate": 0.0006594688165932894
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
                "nmbe_percent": 0.01495392891725481,
                "cvrmse_percent": 33.65271366384771,
                "rms_normalized_rmse_percent": 2.9449887618353556,
                "reference_energy": 0.9601484686036201,
                "candidate_energy": 0.9602920485231152,
                "relative_energy_error_percent": 0.014953928917254809,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.719499990344048e-07,
                  "maximum": 0.00016961904475465417
                },
                "worst": {
                  "global_sensor_index": 45,
                  "local_sensor_index": 9,
                  "sky_patch_index": 372,
                  "rgb_channel": 0,
                  "reference": 0.0015983879566192627,
                  "candidate": 0.0017680070013739169
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.5743282878628032,
                "cvrmse_percent": 92.98140689181857,
                "rms_normalized_rmse_percent": 5.303707137462763,
                "reference_energy": 0.6433172719892326,
                "candidate_energy": 0.6470120250629741,
                "relative_energy_error_percent": 0.5743282878628032,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.6273534058086625e-06,
                  "p90": 1.0849735099327543e-05,
                  "p95": 1.5916610209387727e-05,
                  "p99": 3.4738351132546086e-05,
                  "maximum": 0.00018741743406280875
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "sky_patch_index": 369,
                  "rgb_channel": 0,
                  "reference": 0.00011289998656138778,
                  "candidate": -7.451744750142097e-05
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "start_sensor_index": 72,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.023246312952911383,
                "cvrmse_percent": 27.682442378613143,
                "rms_normalized_rmse_percent": 4.0562343809582515,
                "reference_energy": 2.00387396493079,
                "candidate_energy": 2.0043397917438597,
                "relative_energy_error_percent": 0.023246312952911387,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.6052286052145064e-05,
                  "maximum": 0.00018631794955581427
                },
                "worst": {
                  "global_sensor_index": 82,
                  "local_sensor_index": 10,
                  "sky_patch_index": 327,
                  "rgb_channel": 0,
                  "reference": 0.0018849220359697938,
                  "candidate": 0.002071239985525608
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.25861200435138454,
                "cvrmse_percent": 129.01720165227096,
                "rms_normalized_rmse_percent": 6.029705413999181,
                "reference_energy": 0.6597427930369086,
                "candidate_energy": 0.6580366189762721,
                "relative_energy_error_percent": 0.25861200435138454,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.823906927711505e-06,
                  "p90": 8.347843049705272e-06,
                  "p95": 1.2957058288520784e-05,
                  "p99": 6.700149970129132e-05,
                  "maximum": 0.00028042541816830635
                },
                "worst": {
                  "global_sensor_index": 74,
                  "local_sensor_index": 2,
                  "sky_patch_index": 459,
                  "rgb_channel": 0,
                  "reference": 9.290745947510004e-05,
                  "candidate": -0.0001875179586932063
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 391.58583292737603,
            "full": 9138.497416046448
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 349.29537505377084,
            "full": 8921.814917004667
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 338.42479204759,
            "full": 9172.63116594404
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 345.14679200947285,
            "full": 9067.418207996525
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0018751821662882076,
                "cvrmse_percent": 6.540066878543792,
                "rms_normalized_rmse_percent": 1.8104863168374046,
                "reference_energy": 24.00301191816652,
                "candidate_energy": 24.003462018365383,
                "relative_energy_error_percent": 0.0018751821662882078,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.3351757224409557e-06,
                  "p95": 4.7011475544422865e-05,
                  "p99": 0.00012942345347255468,
                  "maximum": 0.0002462557749822736
                },
                "worst": {
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "sky_patch_index": 560,
                  "rgb_channel": 0,
                  "reference": 0.007164605078287423,
                  "candidate": 0.006918349303305149
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.02973316673535479,
                "cvrmse_percent": 24.029779502878124,
                "rms_normalized_rmse_percent": 2.5276889912911225,
                "reference_energy": 9.994757973432845,
                "candidate_energy": 9.997729731485881,
                "relative_energy_error_percent": 0.029733166735354793,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.442824426107109e-06,
                  "p90": 3.781518171308563e-05,
                  "p95": 7.494412420783192e-05,
                  "p99": 0.0001873731380328536,
                  "maximum": 0.0003809619229286909
                },
                "worst": {
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "sky_patch_index": 448,
                  "rgb_channel": 0,
                  "reference": 0.0012300757225602865,
                  "candidate": 0.0008491137996315956
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
                "nmbe_percent": -0.1384862783651945,
                "cvrmse_percent": 21.434237411084215,
                "rms_normalized_rmse_percent": 1.8741703648236394,
                "reference_energy": 0.9602426483920681,
                "candidate_energy": 0.9589128440850345,
                "relative_energy_error_percent": 0.1384862783651945,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.666901077143848e-06,
                  "maximum": 9.949374361895025e-05
                },
                "worst": {
                  "global_sensor_index": 40,
                  "local_sensor_index": 4,
                  "sky_patch_index": 377,
                  "rgb_channel": 0,
                  "reference": 0.0013155629858374596,
                  "candidate": 0.0012160692422185093
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.6054451739262633,
                "cvrmse_percent": 67.7037348038945,
                "rms_normalized_rmse_percent": 3.899331181084879,
                "reference_energy": 0.6487468462787227,
                "candidate_energy": 0.6526746527505161,
                "relative_energy_error_percent": 0.6054451739262633,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.2283874184504384e-06,
                  "p90": 7.664456069278488e-06,
                  "p95": 1.1743212553483318e-05,
                  "p99": 2.4843262508511543e-05,
                  "maximum": 0.00020089902682229877
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "sky_patch_index": 418,
                  "rgb_channel": 0,
                  "reference": -5.173572571948171e-05,
                  "candidate": 0.00014916330110281706
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "start_sensor_index": 72,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.0568271184594522,
                "cvrmse_percent": 19.269183848692524,
                "rms_normalized_rmse_percent": 2.822318628818679,
                "reference_energy": 2.003304320932557,
                "candidate_energy": 2.0021659008129973,
                "relative_energy_error_percent": 0.05682711845945221,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.333351924084127e-05,
                  "maximum": 0.00012047494965372607
                },
                "worst": {
                  "global_sensor_index": 74,
                  "local_sensor_index": 2,
                  "sky_patch_index": 378,
                  "rgb_channel": 0,
                  "reference": 0.0003620343777583912,
                  "candidate": 0.00048250932741211727
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.49136596833319984,
                "cvrmse_percent": 92.3588426364626,
                "rms_normalized_rmse_percent": 4.333163919819499,
                "reference_energy": 0.6620924021289074,
                "candidate_energy": 0.6653456988718887,
                "relative_energy_error_percent": 0.49136596833319973,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.3365771280859917e-06,
                  "p90": 5.909333594900099e-06,
                  "p95": 9.007651669890038e-06,
                  "p99": 4.62509083263285e-05,
                  "maximum": 0.00023407526896335185
                },
                "worst": {
                  "global_sensor_index": 75,
                  "local_sensor_index": 3,
                  "sky_patch_index": 328,
                  "rgb_channel": 0,
                  "reference": -0.00010736851254478097,
                  "candidate": 0.00012670675641857088
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 338.0764579633251,
            "full": 9490.259208949283
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 333.80512497387826,
            "full": 9439.435707987286
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 338.66399992257357,
            "full": 9502.645959029905
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 338.4540840052068,
            "full": 9753.42212500982
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 333.00170791335404,
            "full": 9312.266541994177
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 331.78341609891504,
            "full": 9244.461999973282
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 346.6300420695916,
            "full": 9778.582417056896
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 348.6067079938948,
            "full": 9655.574999982491
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
            "identifier": "atrium_borrowed_light_atrium_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.010712915642565848,
                "cvrmse_percent": 5.269898364956707,
                "rms_normalized_rmse_percent": 1.4600649472746214,
                "reference_energy": 24.005698135234013,
                "candidate_energy": 24.003126425043376,
                "relative_energy_error_percent": 0.010712915642565848,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.1354499040171504e-06,
                  "p95": 3.5346951335668564e-05,
                  "p99": 0.00010367948561906815,
                  "maximum": 0.00022272160276770592
                },
                "worst": {
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "sky_patch_index": 555,
                  "rgb_channel": 0,
                  "reference": 0.0069458675570786,
                  "candidate": 0.007168589159846306
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.05922772954532212,
                "cvrmse_percent": 20.612146054646246,
                "rms_normalized_rmse_percent": 2.1678253888312033,
                "reference_energy": 9.990551922348587,
                "candidate_energy": 9.99646909942124,
                "relative_energy_error_percent": 0.05922772954532212,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.5158659456064925e-06,
                  "p90": 3.619770141085619e-05,
                  "p95": 6.457208655774593e-05,
                  "p99": 0.00015444704331457615,
                  "maximum": 0.00032748677767813206
                },
                "worst": {
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "sky_patch_index": 541,
                  "rgb_channel": 0,
                  "reference": 0.0006801537238061428,
                  "candidate": 0.00035266694612801075
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
                "nmbe_percent": -0.16483115375434287,
                "cvrmse_percent": 22.278337021765847,
                "rms_normalized_rmse_percent": 1.9483796518505503,
                "reference_energy": 0.9597374999941621,
                "candidate_energy": 0.9581555535999087,
                "relative_energy_error_percent": 0.16483115375434287,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.9789010770618916e-06,
                  "maximum": 0.0001059825299307704
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 1,
                  "sky_patch_index": 494,
                  "rgb_channel": 0,
                  "reference": 0.002307516522705555,
                  "candidate": 0.0024134990526363254
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.0323324184276309,
                "cvrmse_percent": 64.60144948672364,
                "rms_normalized_rmse_percent": 3.7271092991266013,
                "reference_energy": 0.6510024552799756,
                "candidate_energy": 0.6512129401177909,
                "relative_energy_error_percent": 0.03233241842763089,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.243981614607037e-06,
                  "p90": 7.715639003436089e-06,
                  "p95": 1.1413495030865306e-05,
                  "p99": 2.4190987460315228e-05,
                  "maximum": 0.0001413265708833933
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "sky_patch_index": 494,
                  "rgb_channel": 0,
                  "reference": 0.0001510794973000884,
                  "candidate": 9.752926416695118e-06
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
                "nmbe_percent": -0.07249761362630144,
                "cvrmse_percent": 14.559927167695529,
                "rms_normalized_rmse_percent": 2.1339104223964576,
                "reference_energy": 2.004587571886077,
                "candidate_energy": 2.0031342937334102,
                "relative_energy_error_percent": 0.07249761362630144,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.5483008357696235e-05,
                  "maximum": 9.191804565489292e-05
                },
                "worst": {
                  "global_sensor_index": 75,
                  "local_sensor_index": 3,
                  "sky_patch_index": 328,
                  "rgb_channel": 0,
                  "reference": 0.0019055180018767715,
                  "candidate": 0.0019974360475316644
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.15471419943591247,
                "cvrmse_percent": 71.23936659963347,
                "rms_normalized_rmse_percent": 3.341084199909984,
                "reference_energy": 0.6621091859270507,
                "candidate_energy": 0.6631335628534494,
                "relative_energy_error_percent": 0.15471419943591244,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.3264666449686047e-06,
                  "p90": 5.829742758578507e-06,
                  "p95": 8.788420018390752e-06,
                  "p99": 3.845046740025282e-05,
                  "maximum": 0.00012656598119065166
                },
                "worst": {
                  "global_sensor_index": 81,
                  "local_sensor_index": 9,
                  "sky_patch_index": 328,
                  "rgb_channel": 0,
                  "reference": 0.00011309696128591895,
                  "candidate": -1.3469019904732704e-05
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 595.4981670947745,
            "full": 16518.28866591677
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 598.0921249138191,
            "full": 16400.470791966654
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 583.4372920216992,
            "full": 16547.557083074935
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 598.40975003317,
            "full": 16426.72433296684
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 21220.730583067052,
      "worker_pool_size": 12,
      "invocation_count": 7
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/atrium_borrowed_light/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 78145.71666694246,
      "worker_pool_size": 12,
      "invocation_count": 7
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      108,
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
        "identifier": "atrium_borrowed_light_atrium_grid",
        "full_identifier": "atrium_borrowed_light_atrium_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -1.5432083209500536,
            "cvrmse_percent": 14.465039831597002,
            "rms_normalized_rmse_percent": 4.045788025541006,
            "reference_energy": 24.001344877539083,
            "candidate_energy": 23.63095412624898,
            "relative_energy_error_percent": 1.5432083209500536,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.725290298461914e-09,
              "p95": 1.8398870452074334e-05,
              "p99": 0.00020123893045820296,
              "maximum": 0.0012144509237259626
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 509,
              "rgb_channel": 0,
              "reference": 0.0012144509237259626,
              "candidate": 0.0,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.44058136607249265,
            "cvrmse_percent": 50.44047320009173,
            "rms_normalized_rmse_percent": 5.308258908479591,
            "reference_energy": 9.996577879374227,
            "candidate_energy": 9.952534819992778,
            "relative_energy_error_percent": 0.44058136607251047,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 9.120798495132476e-06,
              "p90": 3.7279624666553e-05,
              "p95": 6.717955693602562e-05,
              "p99": 0.0003474452969385311,
              "maximum": 0.001269147265702486
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 521,
              "rgb_channel": 0,
              "reference": 0.0018029473721981049,
              "candidate": 0.0005338001064956188,
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
            "nmbe_percent": -1.218997447681644,
            "cvrmse_percent": 10.812572229173691,
            "rms_normalized_rmse_percent": 3.8699289867842013,
            "reference_energy": 33.99792275691331,
            "candidate_energy": 33.58348894624176,
            "relative_energy_error_percent": 1.2189974476816547,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 8.870985766407102e-06,
              "p90": 3.2711922540329454e-05,
              "p95": 4.9182650400325656e-05,
              "p99": 0.000196349123143591,
              "maximum": 0.001269159372895956
            },
            "worst": {
              "global_sensor_index": 31,
              "local_sensor_index": 31,
              "sky_patch_index": 521,
              "rgb_channel": 0,
              "reference": 0.00815492868423462,
              "candidate": 0.006885769311338663,
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
            "nmbe_percent": 0.022337097386452263,
            "cvrmse_percent": 8.364116384548517,
            "rms_normalized_rmse_percent": 0.7313977807624535,
            "reference_energy": 0.9588268793086172,
            "candidate_energy": 0.9590410534024159,
            "relative_energy_error_percent": 0.022337097386452263,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 4.307366907596588e-08,
              "maximum": 5.270994734019041e-05
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 491,
              "rgb_channel": 0,
              "reference": 0.0012057150015607476,
              "candidate": 0.001258424948900938,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.46157360521092294,
            "cvrmse_percent": 40.84119085087054,
            "rms_normalized_rmse_percent": 2.3584197347162363,
            "reference_energy": 0.6512273491041736,
            "candidate_energy": 0.6482214555507939,
            "relative_energy_error_percent": 0.46157360521092294,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.2248437588624483e-06,
              "p90": 6.370346818584952e-06,
              "p95": 8.738153155718464e-06,
              "p99": 1.5170742699410766e-05,
              "maximum": 6.11181603744626e-05
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 3,
              "sky_patch_index": 545,
              "rgb_channel": 0,
              "reference": 0.00011035817442461848,
              "candidate": 4.924001405015588e-05,
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
            "nmbe_percent": -0.17339288393615898,
            "cvrmse_percent": 15.93617402085152,
            "rms_normalized_rmse_percent": 2.2751741242772487,
            "reference_energy": 1.6100542284127908,
            "candidate_energy": 1.6072625089532098,
            "relative_energy_error_percent": 0.17339288393615898,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.225114928615767e-06,
              "p90": 6.3591851358069175e-06,
              "p95": 8.710754627827555e-06,
              "p99": 1.4927940355846658e-05,
              "maximum": 4.678725963458419e-05
            },
            "worst": {
              "global_sensor_index": 39,
              "local_sensor_index": 3,
              "sky_patch_index": 376,
              "rgb_channel": 0,
              "reference": 0.0006870304932817817,
              "candidate": 0.0006402432336471975,
              "position": [
                6.5,
                2.5,
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
            "nmbe_percent": -0.03702766820649462,
            "cvrmse_percent": 4.693532072983746,
            "rms_normalized_rmse_percent": 0.6882520789598133,
            "reference_energy": 2.004155770185548,
            "candidate_energy": 2.0034136780366225,
            "relative_energy_error_percent": 0.03702766820649462,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 5.412206519395113e-06,
              "maximum": 4.994310438632965e-05
            },
            "worst": {
              "global_sensor_index": 74,
              "local_sensor_index": 2,
              "sky_patch_index": 378,
              "rgb_channel": 0,
              "reference": 0.0003819783159997314,
              "candidate": 0.00043192142038606107,
              "position": [
                6.5,
                3.5,
                3.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.07460176433448804,
            "cvrmse_percent": 41.245093859272025,
            "rms_normalized_rmse_percent": 1.9351452420387651,
            "reference_energy": 0.662326532856854,
            "candidate_energy": 0.6618324255776873,
            "relative_energy_error_percent": 0.07460176433448804,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.5496352716581896e-06,
              "p90": 5.851854439242745e-06,
              "p95": 8.146998879965395e-06,
              "p99": 1.748068825691007e-05,
              "maximum": 6.426661275327206e-05
            },
            "worst": {
              "global_sensor_index": 76,
              "local_sensor_index": 4,
              "sky_patch_index": 333,
              "rgb_channel": 0,
              "reference": -4.169659223407507e-05,
              "candidate": 2.2570020519196987e-05,
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
            "nmbe_percent": -0.04636068376234108,
            "cvrmse_percent": 9.936496940881632,
            "rms_normalized_rmse_percent": 1.8768999633891228,
            "reference_energy": 2.666482303042402,
            "candidate_energy": 2.66524610361431,
            "relative_energy_error_percent": 0.04636068376234107,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.5478570958293858e-06,
              "p90": 5.827463246532738e-06,
              "p95": 8.067945600487292e-06,
              "p99": 1.6574238543398678e-05,
              "maximum": 5.565688479691744e-05
            },
            "worst": {
              "global_sensor_index": 83,
              "local_sensor_index": 11,
              "sky_patch_index": 331,
              "rgb_channel": 0,
              "reference": 0.0004511657461989671,
              "candidate": 0.00039550886140204966,
              "position": [
                7.5,
                0.5,
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
        "identifier": "atrium_borrowed_light_atrium_grid",
        "full_identifier": "atrium_borrowed_light_atrium_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -1.5432083209500536,
            "cvrmse_percent": 14.465039831597002,
            "rms_normalized_rmse_percent": 4.045788025541006,
            "reference_energy": 24.001344877539083,
            "candidate_energy": 23.63095412624898,
            "relative_energy_error_percent": 1.5432083209500536,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.725290298461914e-09,
              "p95": 1.8398870452074334e-05,
              "p99": 0.00020123893045820296,
              "maximum": 0.0012144509237259626
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 509,
              "rgb_channel": 0,
              "reference": 0.0012144509237259626,
              "candidate": 0.0,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 87.14500879572469,
            "cvrmse_percent": 147.0655173523926,
            "rms_normalized_rmse_percent": 8.574292630306665,
            "reference_energy": 5.31808723301636,
            "candidate_energy": 9.952534819992778,
            "relative_energy_error_percent": 87.14500879572466,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.57433811284136e-05,
              "p90": 0.00016403343398678776,
              "p95": 0.0002234257262898609,
              "p99": 0.00040636840640217997,
              "maximum": 0.0013547552734962665
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 509,
              "rgb_channel": 0,
              "reference": -0.0011751552738132887,
              "candidate": 0.0001795999996829778,
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
            "nmbe_percent": 14.543449612556415,
            "cvrmse_percent": 22.752365851428063,
            "rms_normalized_rmse_percent": 7.313312074965507,
            "reference_energy": 29.319432110555443,
            "candidate_energy": 33.58348894624176,
            "relative_energy_error_percent": 14.54344961255641,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.543049676110968e-05,
              "p90": 0.0001527217787952396,
              "p95": 0.00019428724772296846,
              "p99": 0.00033322698436677456,
              "maximum": 0.0011176727712154388
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 525,
              "rgb_channel": 0,
              "reference": 0.007140863221138716,
              "candidate": 0.006023190449923277,
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
        "identifier": "atrium_borrowed_light_office_0_grid",
        "full_identifier": "atrium_borrowed_light_office_0_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.022337097386452263,
            "cvrmse_percent": 8.364116384548517,
            "rms_normalized_rmse_percent": 0.7313977807624535,
            "reference_energy": 0.9588268793086172,
            "candidate_energy": 0.9590410534024159,
            "relative_energy_error_percent": 0.022337097386452263,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 4.307366907596588e-08,
              "maximum": 5.270994734019041e-05
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 491,
              "rgb_channel": 0,
              "reference": 0.0012057150015607476,
              "candidate": 0.001258424948900938,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 246.2681758457665,
            "cvrmse_percent": 443.46414041674353,
            "rms_normalized_rmse_percent": 7.562001096325041,
            "reference_energy": 0.18720214584187556,
            "candidate_energy": 0.6482214555507939,
            "relative_energy_error_percent": 246.2681758457665,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.6700000691780588e-06,
              "p90": 2.058000063698273e-05,
              "p95": 2.8979999115108512e-05,
              "p99": 5.048999810242094e-05,
              "maximum": 0.00015037134289741516
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 495,
              "rgb_channel": 0,
              "reference": -9.204144589602947e-05,
              "candidate": 5.832989700138569e-05,
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
            "nmbe_percent": 40.24623056489772,
            "cvrmse_percent": 72.36967404602478,
            "rms_normalized_rmse_percent": 7.55474203514877,
            "reference_energy": 1.1460290251504928,
            "candidate_energy": 1.6072625089532098,
            "relative_energy_error_percent": 40.24623056489772,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.6700000691780588e-06,
              "p90": 2.0587595690813067e-05,
              "p95": 2.8912243578815833e-05,
              "p99": 5.022095865570009e-05,
              "maximum": 0.00015045935288071632
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 495,
              "rgb_channel": 0,
              "reference": 0.0023393542505800724,
              "candidate": 0.0024898136034607887,
              "position": [
                6.5,
                3.5,
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
            "nmbe_percent": -0.03702766820649462,
            "cvrmse_percent": 4.693532072983746,
            "rms_normalized_rmse_percent": 0.6882520789598133,
            "reference_energy": 2.004155770185548,
            "candidate_energy": 2.0034136780366225,
            "relative_energy_error_percent": 0.03702766820649462,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 5.412206519395113e-06,
              "maximum": 4.994310438632965e-05
            },
            "worst": {
              "global_sensor_index": 74,
              "local_sensor_index": 2,
              "sky_patch_index": 378,
              "rgb_channel": 0,
              "reference": 0.0003819783159997314,
              "candidate": 0.00043192142038606107,
              "position": [
                6.5,
                3.5,
                3.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 672.942589702224,
            "cvrmse_percent": 1171.9758523714495,
            "rms_normalized_rmse_percent": 7.322397380610194,
            "reference_energy": 0.08562504310089292,
            "candidate_energy": 0.6618324255776873,
            "relative_energy_error_percent": 672.9425897022242,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.549999968934571e-06,
              "p90": 2.246000076411292e-05,
              "p95": 3.553234273567796e-05,
              "p99": 6.576676514669089e-05,
              "maximum": 0.00017941714031621814
            },
            "worst": {
              "global_sensor_index": 89,
              "local_sensor_index": 17,
              "sky_patch_index": 281,
              "rgb_channel": 0,
              "reference": -0.00012148712994530797,
              "candidate": 5.793001037091017e-05,
              "position": [
                8.5,
                0.5,
                3.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 27.53711234542716,
            "cvrmse_percent": 47.85215174371033,
            "rms_normalized_rmse_percent": 7.296860375631885,
            "reference_energy": 2.089780813286441,
            "candidate_energy": 2.66524610361431,
            "relative_energy_error_percent": 27.537112345427165,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.550742571358569e-06,
              "p90": 2.241000038338825e-05,
              "p95": 3.527999797370285e-05,
              "p99": 6.577999738510698e-05,
              "maximum": 0.00016103911912068725
            },
            "worst": {
              "global_sensor_index": 89,
              "local_sensor_index": 17,
              "sky_patch_index": 281,
              "rgb_channel": 0,
              "reference": 0.0009662429220043123,
              "candidate": 0.0011272820411249995,
              "position": [
                8.5,
                0.5,
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
      "bias_percent": -1.0932770678140942,
      "rms_normalized_error_percent": 2.05256125507528,
      "absolute_error": {
        "p95": 0.5249723966947345,
        "p99": 3.608551040265829,
        "maximum": 3.7589055414511208
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 21.145438784357193,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 2.05256125507528
    },
    "overcast": {
      "bias_percent": -1.075378611227667,
      "rms_normalized_error_percent": 2.059989001966997,
      "absolute_error": {
        "p95": 0.4372777938842773,
        "p99": 3.290195121765132,
        "maximum": 3.4355316162109375
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 18.616369247436523,
      "reference_fraction_of_uniform": 0.8803964257240295,
      "rms_normalized_to_uniform_percent": 1.8455266732659419
    },
    "horizon": {
      "bias_percent": -0.2676252821067979,
      "rms_normalized_error_percent": 5.795357823875849,
      "absolute_error": {
        "p95": 0.009944884430446886,
        "p99": 0.014429338790547376,
        "maximum": 0.01839484398331695
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": true,
      "reference_mean": 0.04846068237286519,
      "reference_fraction_of_uniform": 0.0022917794644542943,
      "rms_normalized_to_uniform_percent": 0.012582989641413767
    },
    "north": {
      "bias_percent": -0.6297693485209238,
      "rms_normalized_error_percent": 1.4996310825422279,
      "absolute_error": {
        "p95": 0.07282443046569814,
        "p99": 0.36609806537628026,
        "maximum": 0.7654438018798828
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.1400136947631836,
      "reference_fraction_of_uniform": 0.14849603176116943,
      "rms_normalized_to_uniform_percent": 0.2626660529108112
    },
    "east": {
      "bias_percent": -0.2914540655875638,
      "rms_normalized_error_percent": 0.38226072932991956,
      "absolute_error": {
        "p95": 0.05846633911132809,
        "p99": 0.07303477764129636,
        "maximum": 0.09039115905761719
      },
      "worst_index": [
        1
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.0161070823669434,
      "reference_fraction_of_uniform": 0.14263629913330078,
      "rms_normalized_to_uniform_percent": 0.06825244059017341
    },
    "south": {
      "bias_percent": -0.9841802607818758,
      "rms_normalized_error_percent": 1.7064039349978855,
      "absolute_error": {
        "p95": 0.14091372489929196,
        "p99": 0.43409489631652665,
        "maximum": 0.7723636627197266
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.156545877456665,
      "reference_fraction_of_uniform": 0.14927786588668823,
      "rms_normalized_to_uniform_percent": 0.30020543490837714
    },
    "west": {
      "bias_percent": -2.7150422162656174,
      "rms_normalized_error_percent": 4.855704202892317,
      "absolute_error": {
        "p95": 0.2850563287734985,
        "p99": 1.5949345302581766,
        "maximum": 1.6492576599121094
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.025270938873291,
      "reference_fraction_of_uniform": 0.19036118686199188,
      "rms_normalized_to_uniform_percent": 0.9187471803313555
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
          "nmbe_percent": -1.48319984549288,
          "cvrmse_percent": 6.676772789188206,
          "absolute_error_percentiles_lux": {
            "p50": 9.33551025390625,
            "p90": 72.88916015625,
            "p95": 118.28525390624964,
            "p99": 376.153675537109
          },
          "maximum_absolute_error_lux": 4794.271484375,
          "worst": {
            "sensor_index": 31,
            "position": [
              5.5,
              4.5,
              0.75
            ],
            "hour_of_year": 3829.5,
            "foton_lux": 32200.673828125,
            "radiance_lux": 36994.9453125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.20343987823439966,
            "maximum_error_percentage_points": 1.091095890410955,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.10224126312587956,
            "maximum_error_percentage_points": 0.523941553020066,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.09294901065449007,
            "maximum_error_percentage_points": 0.657123287671233,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.41924277016742845,
            "maximum_error_percentage_points": 1.9445205479452028,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.4824733637747339,
            "maximum_error_percentage_points": 2.356986301369863,
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
          "nmbe_percent": -0.2918006569154104,
          "cvrmse_percent": 8.247480989465771,
          "absolute_error_percentiles_lux": {
            "p50": 0.684624195098877,
            "p90": 9.55821685791016,
            "p95": 15.894392013549803,
            "p99": 31.713105087280248
          },
          "maximum_absolute_error_lux": 112.96661376953125,
          "worst": {
            "sensor_index": 2,
            "position": [
              6.5,
              3.5,
              0.75
            ],
            "hour_of_year": 2868.5,
            "foton_lux": 990.0435791015625,
            "radiance_lux": 877.0769653320312
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.14985159817351568,
            "maximum_error_percentage_points": 2.601369863013698,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1995780775727438,
            "maximum_error_percentage_points": 0.8928773164694803,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.5391324200913243,
            "maximum_error_percentage_points": 2.521369863013703,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.5360464231354639,
            "maximum_error_percentage_points": 2.521369863013696,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0032153729071537473,
            "maximum_error_percentage_points": 0.08150684931506902,
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
          "nmbe_percent": 0.05224192734820318,
          "cvrmse_percent": 3.215075706323388,
          "absolute_error_percentiles_lux": {
            "p50": 1.1989364624023438,
            "p90": 11.065567016601562,
            "p95": 16.81744842529296,
            "p99": 34.66585540771465
          },
          "maximum_absolute_error_lux": 166.80322265625,
          "worst": {
            "sensor_index": 9,
            "position": [
              7.5,
              2.5,
              3.75
            ],
            "hour_of_year": 4455.5,
            "foton_lux": 6130.185546875,
            "radiance_lux": 5963.38232421875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.20173515981735127,
            "maximum_error_percentage_points": 0.680547945205479,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.20874087090664972,
            "maximum_error_percentage_points": 0.6221614395538282,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.5157343987823445,
            "maximum_error_percentage_points": 3.2910958904109577,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.519006849315068,
            "maximum_error_percentage_points": 3.2910958904109577,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.009086757990867615,
            "maximum_error_percentage_points": 0.057945205479452255,
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
      "maximum_error_percentage_points": 0.004989833047943648,
      "metrics": {
        "da": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.004794520547945158,
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
            "maximum_error_percentage_points": 0.004893514554794365,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.004989833047943648,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.0049855522260315865,
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
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
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
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "atrium_borrowed_light_atrium_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_0_grid",
            "maximum_error_percentage_points": 0.004383561643835243,
            "passed": true
          },
          {
            "identifier": "atrium_borrowed_light_office_1_grid",
            "maximum_error_percentage_points": 0.0046575342465753344,
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
      "study_preparation_seconds": 0.0405080410419032,
      "weather_seconds": 0.1582898749038577,
      "metric_reduction_seconds": 0.45505241700448096,
      "write_seconds": 0.0750595829449594,
      "total_seconds": 0.6892112500499934,
      "cold_end_to_end_seconds": 0.7297192910918966,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.029906125040724874,
      "engine_upload_seconds": 0.00100775,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.32200612500309944,
      "engine_annual_reduction_seconds": 0.0041483750101178885,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.32200612500309944
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.0405080410419032,
      "weather_seconds": 0.10996420797891915,
      "metric_reduction_seconds": 0.07031483296304941,
      "write_seconds": 0.0527993330033496,
      "total_seconds": 0.2333282500039786,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.2333282500039786,
      "raw_export_seconds": 0.02852579194586724,
      "engine_upload_seconds": 0.00012725,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.004615666694007814,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.022732999990694225,
      "full": 0.31384112499654293
    }
  },
  "elapsed_seconds": 296.8245739999693,
  "result_class": "passed"
}
```
